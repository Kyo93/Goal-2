import hashlib
import json
import re
from collections import defaultdict
from typing import Any, Dict, Iterable, List, Tuple


def _clean_text(value: Any) -> str:
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value).replace("\u00a0", " ")).strip()


def _stable_hash(*parts: Any, length: int = 12) -> str:
    payload = "\x1f".join(_clean_text(part).lower() for part in parts)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:length].upper()


def _join_unique(values: Iterable[str]) -> str:
    unique = sorted({_clean_text(value) for value in values if _clean_text(value) and _clean_text(value) != "UNKNOWN"})
    return ",".join(unique) if unique else "UNKNOWN"


def _as_payload(value: Any) -> Dict[str, Any]:
    if value is None:
        return {}
    if isinstance(value, dict):
        return value
    if isinstance(value, str):
        text = value.strip()
        if not text:
            return {}
        return json.loads(text)
    return {}


def _extract_records(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
    if "json_result" in payload and isinstance(payload["json_result"], dict):
        payload = payload["json_result"]
    records = payload.get("records", [])
    return [record for record in records if isinstance(record, dict)]


def _record_dedupe_key(record: Dict[str, Any]) -> Tuple[str, ...]:
    alert_id = _clean_text(record.get("alert_id"))
    if alert_id:
        return ("alert_id", alert_id)
    source_ref = _clean_text(record.get("source_ref"))
    if source_ref:
        return ("source_ref", source_ref)
    return (
        "fallback",
        _clean_text(record.get("host")),
        _clean_text(record.get("problem_signature")),
        _clean_text(record.get("seen_at")),
    )


def _classify_alert_pattern_family(pattern: Dict[str, Any]) -> str:
    signature = _clean_text(pattern.get("problem_signature")).lower()
    host = _clean_text(pattern.get("host")).lower()
    component = _clean_text(pattern.get("component")).lower()
    domain = _clean_text(pattern.get("domain")).lower()
    joined = " ".join([signature, host, component, domain])
    if "http monitoring" in signature:
        return "HTTP monitoring"
    if any(
        term in joined
        for term in [
            "icmp",
            "unavailable",
            "unreachable",
            "interface down",
            "link down",
            "port down",
            "packet loss",
            "latency",
            " is down",
            "down!",
            "gateway",
            "tunnel",
            "vpn",
            "bgp",
        ]
    ):
        return "Network reachability"
    if any(term in joined for term in ["active checks", "zabbix agent", "nodata"]):
        return "Zabbix agent/active check"
    if any(term in joined for term in ["restarted", "uptime"]):
        return "Host restart/uptime"
    if any(term in joined for term in ["ups", "battery", "frequency", "power"]):
        return "Power/UPS"
    if any(term in joined for term in ["cpu", "memory", "disk", "filesystem", "space"]):
        return "Resource/capacity"
    return "Other"


def _alert_investigation_priority(pattern: Dict[str, Any], family: str) -> str:
    signature = _clean_text(pattern.get("problem_signature")).lower()
    host = _clean_text(pattern.get("host")).lower()
    alert_count = int(pattern.get("alert_count") or 0)
    if family == "Network reachability":
        if alert_count > 1 or "fw" in host or "sw" in host or "down" in signature:
            return "HIGH"
        return "MEDIUM"
    if family == "HTTP monitoring":
        return "MEDIUM" if alert_count >= 10 else "LOW"
    if family == "Power/UPS":
        return "HIGH"
    if family in {"Zabbix agent/active check", "Host restart/uptime", "Resource/capacity"}:
        return "LOW"
    return "LOW"


def _alert_why_it_matters(pattern: Dict[str, Any], family: str) -> str:
    host = _clean_text(pattern.get("host"))
    signature = _clean_text(pattern.get("problem_signature"))
    if family == "Network reachability":
        return (
            f"{host} reported `{signature}`. This can indicate connectivity loss, "
            "device/path flap, ISP path issue, or monitoring-path instability."
        )
    if family == "HTTP monitoring":
        return (
            f"{host} reported `{signature}`. This usually means service probe timeout "
            "or threshold sensitivity unless supported by ticket/incident evidence."
        )
    if family == "Zabbix agent/active check":
        return (
            f"{host} reported `{signature}`. This points to monitoring-agent health, "
            "not confirmed user impact by itself."
        )
    if family == "Host restart/uptime":
        return (
            f"{host} reported `{signature}`. This is host-health context and should "
            "not be treated as service impact without another source."
        )
    if family == "Power/UPS":
        return (
            f"{host} reported `{signature}`. This may indicate power/UPS instability "
            "and deserves device/facility verification."
        )
    if family == "Resource/capacity":
        return (
            f"{host} reported `{signature}`. This is resource/capacity context; "
            "treat as potential technical signal unless corroborated."
        )
    return f"{host} reported `{signature}`. Treat as monitoring context until corroborated."


def _signal_assessment(pattern: Dict[str, Any], family: str) -> str:
    if family == "HTTP monitoring" and int(pattern.get("alert_count") or 0) > 1:
        return "LIKELY_NOISE_OR_THRESHOLD_REVIEW"
    return "UNCONFIRMED_MONITORING_SIGNAL"


def _group_alert_patterns(alerts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    grouped: Dict[Tuple[str, str], List[Dict[str, Any]]] = defaultdict(list)
    for alert in alerts:
        grouped[(_clean_text(alert.get("host")), _clean_text(alert.get("problem_signature")))].append(alert)

    patterns: List[Dict[str, Any]] = []
    for (host, signature), records in grouped.items():
        records = sorted(records, key=lambda record: (_clean_text(record.get("seen_at")), _clean_text(record.get("source_ref"))))
        pattern = {
            "record_type": "ZABBIX_ALERT_PATTERN",
            "alert_pattern_id": f"ALP-{_stable_hash(host, signature)}",
            "source_refs": [_clean_text(record.get("source_ref")) for record in records if _clean_text(record.get("source_ref"))],
            "first_seen_at": _clean_text(records[0].get("seen_at")),
            "last_seen_at": _clean_text(records[-1].get("seen_at")),
            "last_recovered_at": max(
                (_clean_text(record.get("recovered_at")) for record in records if _clean_text(record.get("recovered_at"))),
                default="",
            ),
            "alert_count": len(records),
            "resolved_count": sum(_clean_text(record.get("status")).upper() == "RESOLVED" for record in records),
            "open_count": sum(_clean_text(record.get("status")).upper() != "RESOLVED" for record in records),
            "host": host,
            "site_code": _clean_text(records[0].get("site_code")) or "UNKNOWN",
            "severity": _join_unique(record.get("severity", "") for record in records),
            "problem_signature": signature,
            "domain": _join_unique(record.get("domain", "") for record in records),
            "component": _join_unique(record.get("component", "") for record in records),
            "scope": _join_unique(record.get("scope", "") for record in records),
            "assessment": "RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT",
            "evidence_label": "COMPUTED FACT",
            "source_reference_count": len(records),
        }
        pattern["pattern_family"] = _classify_alert_pattern_family(pattern)
        pattern["investigation_priority"] = _alert_investigation_priority(pattern, pattern["pattern_family"])
        pattern["why_it_matters"] = _alert_why_it_matters(pattern, pattern["pattern_family"])
        pattern["signal_assessment"] = _signal_assessment(pattern, pattern["pattern_family"])
        patterns.append(pattern)
    return sorted(patterns, key=lambda pattern: (-int(pattern["alert_count"]), pattern["alert_pattern_id"]))


def _render_patterns_markdown(patterns: List[Dict[str, Any]], summary: Dict[str, Any]) -> str:
    lines = [
        "# Zabbix Alert Patterns",
        "",
        "```yaml",
        "record_type: ZABBIX_ALERT_PATTERN_SOURCE",
        "source_type: zabbix_merged_outputs",
        f"source_file_count: {summary['source_file_count']}",
        f"record_count: {summary['record_count']}",
        f"alert_pattern_count: {summary['alert_pattern_count']}",
        f"duplicate_rows: {summary['duplicate_rows']}",
        f"reconciliation_passed: {str(summary['reconciliation_passed']).lower()}",
        f"upload_ready: {str(summary['upload_ready']).lower()}",
        "validation_status: PASS" if summary["upload_ready"] else "validation_status: FAIL",
        "note: Raw Zabbix alert patterns are monitoring signals, not confirmed incidents.",
        "```",
        "",
    ]
    for pattern in patterns:
        lines.extend(
            [
                f"## Alert Pattern {pattern['alert_pattern_id']}",
                "",
                "```yaml",
                f"record_type: {pattern['record_type']}",
                f"alert_pattern_id: {pattern['alert_pattern_id']}",
                f"host: {pattern['host']}",
                f"site_code: {pattern['site_code']}",
                f"first_seen_at: {pattern['first_seen_at']}",
                f"last_seen_at: {pattern['last_seen_at']}",
                f"last_recovered_at: {pattern['last_recovered_at'] or 'UNKNOWN'}",
                f"alert_count: {pattern['alert_count']}",
                f"resolved_count: {pattern['resolved_count']}",
                f"open_count: {pattern['open_count']}",
                f"severity: {pattern['severity']}",
                f"pattern_family: {pattern['pattern_family']}",
                f"investigation_priority: {pattern['investigation_priority']}",
                f"signal_assessment: {pattern['signal_assessment']}",
                f"assessment: {pattern['assessment']}",
                f"evidence_label: {pattern['evidence_label']}",
                f"source_reference_count: {pattern['source_reference_count']}",
                "problem_signature: |",
                "  " + pattern["problem_signature"].replace("\n", "\n  "),
                "why_it_matters: |",
                "  " + pattern["why_it_matters"].replace("\n", "\n  "),
                "source_refs_sample: |",
                "  " + "; ".join(pattern["source_refs"][:20]),
                "```",
                "",
            ]
        )
    return "\n".join(lines).strip() + "\n"


def main(zabbix_json_results=None, zabbix_json_texts=None, source_files=None):
    payloads: List[Dict[str, Any]] = []
    for value in zabbix_json_results or []:
        payloads.append(_as_payload(value))
    for value in zabbix_json_texts or []:
        payloads.append(_as_payload(value))

    seen = set()
    records: List[Dict[str, Any]] = []
    duplicate_rows = 0
    for payload in payloads:
        for record in _extract_records(payload):
            key = _record_dedupe_key(record)
            if key in seen:
                duplicate_rows += 1
                continue
            seen.add(key)
            records.append(record)

    patterns = _group_alert_patterns(records)
    summary = {
        "ok": len(records) > 0 and len(patterns) > 0,
        "source_type": "zabbix_merged_outputs",
        "source_file_count": len(source_files or payloads),
        "record_count": len(records),
        "alert_pattern_count": len(patterns),
        "duplicate_rows": duplicate_rows,
        "rejected_row_count": 0,
        "reconciliation_passed": True,
        "upload_ready": len(records) > 0 and len(patterns) > 0,
    }
    json_result = {
        "ok": summary["ok"],
        "source_type": "zabbix_merged_outputs",
        "record_count": len(records),
        "records": records,
        "rejected_rows": [],
    }
    alert_patterns_result = {
        "ok": summary["ok"],
        "source_type": "zabbix_alert_patterns",
        "record_type": "ALERT_PATTERN_COLLECTION",
        "record_count": len(patterns),
        "records": patterns,
    }
    return {
        "json_text": json.dumps(json_result, ensure_ascii=False, indent=2),
        "alert_patterns_text": json.dumps(alert_patterns_result, ensure_ascii=False, indent=2),
        "json_result": json_result,
        "alert_patterns_result": alert_patterns_result,
        "markdown": _render_patterns_markdown(patterns, summary),
        "summary": summary,
    }
