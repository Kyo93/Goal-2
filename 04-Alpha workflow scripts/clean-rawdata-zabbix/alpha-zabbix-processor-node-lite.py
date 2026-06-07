import csv
import hashlib
import io
import json
import re
from collections import defaultdict
from datetime import date, datetime, time
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


ZABBIX_REQUIRED_COLUMNS = [
    "Severity",
    "Time",
    "Recovery time",
    "Status",
    "Host",
    "Problem",
    "Duration",
    "Ack",
    "Actions",
    "Tags",
]

ZABBIX_NORMALIZED_REQUIRED_COLUMNS = [
    "event_id",
    "started_at_local",
    "recovered_at_local",
    "status",
    "severity",
    "host",
    "site_code",
    "problem_raw",
    "problem_signature",
    "duration_text",
    "acknowledged",
    "action_count",
    "domain",
    "component",
    "scope",
    "tags_json",
]

MAX_SOURCE_REFS_PER_PATTERN = 20
DEFAULT_MAX_PATTERNS = 500
DEFAULT_RETURN_MARKDOWN = True
PACKAGE_SECTION = "04_alert_patterns"
KNOWLEDGE_FILENAME = "04_alert_patterns.md"


def _clean_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (datetime, date, time)):
        return str(value)
    return re.sub(r"\s+", " ", str(value).replace("\u00a0", " ")).strip()


def _normalize_header(value: Any) -> str:
    return re.sub(r"[^a-z0-9]+", "", _clean_text(value).lower())


RAW_HEADER_ALIASES = {_normalize_header(name): name for name in ZABBIX_REQUIRED_COLUMNS}
NORMALIZED_HEADER_ALIASES = {
    _normalize_header(name): name for name in ZABBIX_NORMALIZED_REQUIRED_COLUMNS
}


def _stable_hash(*parts: Any, length: int = 12) -> str:
    payload = "\x1f".join(_clean_text(part).lower() for part in parts)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:length].upper()


def _unknown(value: Any) -> str:
    text = _clean_text(value)
    return text if text else "UNKNOWN"


def _derive_site_code_from_host(host: Any) -> str:
    match = re.match(r"^VNM([A-Z0-9]{3})", _clean_text(host).upper())
    return match.group(1) if match else "UNKNOWN"


def _normalize_problem_signature(problem: Any) -> str:
    text = _clean_text(problem).lower()
    text = re.sub(
        r"current:\s*\d+(?:\.\d+)?\s*mbps",
        "current:<value> mbps",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"\d+(?:\.\d+)?(?:-\d+(?:\.\d+)?)?\s*(?:mbps|gbps|%|hz|m|s|c|°c|℃)\b",
        "<value>",
        text,
        flags=re.IGNORECASE,
    )
    return text


def _decode_bytes(data: bytes) -> str:
    for encoding in ("utf-8-sig", "utf-8", "latin-1"):
        try:
            return data.decode(encoding, errors="strict")
        except UnicodeDecodeError:
            continue
    return data.decode("latin-1", errors="replace")


def _extract_file_content(file_obj: Any) -> Optional[Any]:
    if isinstance(file_obj, (bytes, bytearray)):
        return bytes(file_obj)
    if hasattr(file_obj, "read"):
        try:
            return file_obj.read()
        except Exception:
            return None
    if isinstance(file_obj, dict):
        for key in ("body", "content", "text", "data", "file_body", "bytes"):
            if key in file_obj and file_obj[key] is not None:
                return file_obj[key]
    return None


def _extract_file_name(file_obj: Any, source_label: Optional[str]) -> str:
    if source_label:
        return _clean_text(source_label)
    if isinstance(file_obj, dict):
        for key in ("source_label", "file_name", "filename", "name", "id"):
            if file_obj.get(key):
                return _clean_text(file_obj.get(key))
    if isinstance(file_obj, (str, Path)):
        return Path(str(file_obj)).name
    return "zabbix_export.csv"


def _resolve_file_path(file_obj: Any) -> Optional[Path]:
    if isinstance(file_obj, (str, Path)):
        path = Path(str(file_obj))
    elif isinstance(file_obj, dict):
        path = None
        for key in ("path", "file_path", "filepath", "file"):
            if file_obj.get(key):
                path = Path(str(file_obj[key]))
                break
        if path is None:
            return None
    else:
        return None

    if path.exists():
        return path
    alt = Path.cwd() / str(path)
    return alt if alt.exists() else None


def _looks_like_html(text: str) -> bool:
    t = text.lstrip().lower()
    return (
        t.startswith("<!doctype html")
        or t.startswith("<html")
        or ("<head" in t and "<body" in t)
        or "accounts.google.com" in t
    )


def _csv_text_from_input(file_obj: Any, body: Any, source_label: Optional[str]) -> Tuple[str, str]:
    label = _extract_file_name(file_obj, source_label)
    content = body if body is not None else _extract_file_content(file_obj)

    if content is not None:
        if isinstance(content, (bytes, bytearray)):
            return _decode_bytes(bytes(content)), label
        return str(content), label

    path = _resolve_file_path(file_obj)
    if path is None:
        raise ValueError("No readable CSV body or file path found")
    return _decode_bytes(path.read_bytes()), label or path.name


def _parse_tags(value: Any) -> Dict[str, List[str]]:
    text = _clean_text(value)
    if not text:
        return {}
    try:
        payload = json.loads(text)
        if isinstance(payload, dict):
            out: Dict[str, List[str]] = {}
            for key, raw in payload.items():
                if isinstance(raw, list):
                    vals = [_clean_text(item) for item in raw if _clean_text(item)]
                else:
                    vals = [_clean_text(raw)] if _clean_text(raw) else []
                if vals:
                    out[_clean_text(key)] = vals
            return out
    except Exception:
        pass

    tags: Dict[str, List[str]] = defaultdict(list)
    for token in text.split(", "):
        if ": " not in token:
            continue
        key, val = token.split(": ", 1)
        if val and val not in tags[key]:
            tags[key].append(val)
    return dict(tags)


def _join_unique(values: Iterable[str]) -> str:
    unique = sorted({value for value in values if value and value != "UNKNOWN"})
    return ",".join(unique) if unique else "UNKNOWN"


def _family(signature: str, host: str, component: str, domain: str) -> str:
    joined = " ".join([signature, host, component, domain]).lower()
    if "http monitoring" in signature.lower():
        return "HTTP monitoring"
    if any(
        term in joined
        for term in (
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
        )
    ):
        return "Network reachability"
    if any(term in joined for term in ("active checks", "zabbix agent", "nodata")):
        return "Zabbix agent/active check"
    if any(term in joined for term in ("restarted", "uptime")):
        return "Host restart/uptime"
    if any(term in joined for term in ("ups", "battery", "frequency", "power")):
        return "Power/UPS"
    if any(term in joined for term in ("cpu", "memory", "disk", "filesystem", "space")):
        return "Resource/capacity"
    return "Other"


def _priority(pattern: Dict[str, Any]) -> str:
    family = pattern["pattern_family"]
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
    return "LOW"


def _why(pattern: Dict[str, Any]) -> str:
    host = _clean_text(pattern.get("host"))
    signature = _clean_text(pattern.get("problem_signature"))
    family = pattern["pattern_family"]
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
        return f"{host} reported `{signature}`. This points to monitoring-agent health."
    if family == "Host restart/uptime":
        return f"{host} reported `{signature}`. This is host-health context."
    if family == "Power/UPS":
        return f"{host} reported `{signature}`. This may indicate power/UPS instability."
    return f"{host} reported `{signature}`. Treat as monitoring context until corroborated."


def _assessment(pattern: Dict[str, Any]) -> str:
    if pattern["pattern_family"] == "HTTP monitoring" and int(pattern["alert_count"]) > 1:
        return "LIKELY_NOISE_OR_THRESHOLD_REVIEW"
    return "UNCONFIRMED_MONITORING_SIGNAL"


def _canonical_mapping(headers: Sequence[str]) -> Tuple[Dict[str, str], bool, List[str]]:
    raw_map: Dict[str, str] = {}
    norm_map: Dict[str, str] = {}
    for header in headers:
        norm = _normalize_header(header)
        if norm in RAW_HEADER_ALIASES:
            raw_map[RAW_HEADER_ALIASES[norm]] = header
        if norm in NORMALIZED_HEADER_ALIASES:
            norm_map[NORMALIZED_HEADER_ALIASES[norm]] = header
    is_normalized = all(col in norm_map for col in ZABBIX_NORMALIZED_REQUIRED_COLUMNS)
    required = ZABBIX_NORMALIZED_REQUIRED_COLUMNS if is_normalized else ZABBIX_REQUIRED_COLUMNS
    mapping = norm_map if is_normalized else raw_map
    missing = [col for col in required if col not in mapping]
    return mapping, is_normalized, missing


def _row_value(row: Dict[str, Any], mapping: Dict[str, str], name: str) -> Any:
    return row.get(mapping[name], "")


def _update_pattern(patterns: Dict[Tuple[str, str], Dict[str, Any]], record: Dict[str, str]) -> None:
    key = (record["host"], record["problem_signature"])
    pattern = patterns.get(key)
    if pattern is None:
        pattern = {
            "record_type": "ZABBIX_ALERT_PATTERN",
            "alert_pattern_id": f"ALP-{_stable_hash(record['host'], record['problem_signature'])}",
            "source_refs": [],
            "source_reference_count": 0,
            "first_seen_at": record["seen_at"],
            "last_seen_at": record["seen_at"],
            "last_recovered_at": record["recovered_at"],
            "alert_count": 0,
            "resolved_count": 0,
            "open_count": 0,
            "host": record["host"],
            "site_code": record["site_code"],
            "severity_values": set(),
            "problem_signature": record["problem_signature"],
            "domain_values": set(),
            "component_values": set(),
            "scope_values": set(),
            "assessment": "RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT",
            "evidence_label": "COMPUTED FACT",
        }
        patterns[key] = pattern

    pattern["alert_count"] += 1
    if record["status"] == "RESOLVED":
        pattern["resolved_count"] += 1
    else:
        pattern["open_count"] += 1
    if record["seen_at"] and record["seen_at"] < pattern["first_seen_at"]:
        pattern["first_seen_at"] = record["seen_at"]
    if record["seen_at"] and record["seen_at"] > pattern["last_seen_at"]:
        pattern["last_seen_at"] = record["seen_at"]
    if record["recovered_at"] and record["recovered_at"] > pattern["last_recovered_at"]:
        pattern["last_recovered_at"] = record["recovered_at"]
    pattern["severity_values"].add(record["severity"])
    pattern["domain_values"].add(record["domain"])
    pattern["component_values"].add(record["component"])
    pattern["scope_values"].add(record["scope"])
    pattern["source_reference_count"] += 1
    if len(pattern["source_refs"]) < MAX_SOURCE_REFS_PER_PATTERN:
        pattern["source_refs"].append(record["source_ref"])


def _finalize_patterns(patterns_by_key: Dict[Tuple[str, str], Dict[str, Any]], max_patterns: int) -> List[Dict[str, Any]]:
    patterns: List[Dict[str, Any]] = []
    for raw in patterns_by_key.values():
        pattern = {
            "record_type": raw["record_type"],
            "alert_pattern_id": raw["alert_pattern_id"],
            "source_refs": raw["source_refs"],
            "first_seen_at": raw["first_seen_at"],
            "last_seen_at": raw["last_seen_at"],
            "last_recovered_at": raw["last_recovered_at"] or "UNKNOWN",
            "alert_count": raw["alert_count"],
            "resolved_count": raw["resolved_count"],
            "open_count": raw["open_count"],
            "host": raw["host"],
            "site_code": raw["site_code"],
            "severity": _join_unique(raw["severity_values"]),
            "problem_signature": raw["problem_signature"],
            "domain": _join_unique(raw["domain_values"]),
            "component": _join_unique(raw["component_values"]),
            "scope": _join_unique(raw["scope_values"]),
            "assessment": raw["assessment"],
            "evidence_label": raw["evidence_label"],
            "source_reference_count": raw["source_reference_count"],
        }
        pattern["pattern_family"] = _family(
            pattern["problem_signature"], pattern["host"], pattern["component"], pattern["domain"]
        )
        pattern["investigation_priority"] = _priority(pattern)
        pattern["why_it_matters"] = _why(pattern)
        pattern["signal_assessment"] = _assessment(pattern)
        patterns.append(pattern)
    patterns.sort(key=lambda item: (-int(item["alert_count"]), item["alert_pattern_id"]))
    return patterns[: max(0, max_patterns)]


def _md_code(value: Any) -> str:
    return "`" + _clean_text(value).replace("`", "'") + "`"


def _sample_unique(patterns: Sequence[Dict[str, Any]], key: str, limit: int) -> str:
    values: List[str] = []
    seen = set()
    for pattern in patterns:
        value = _clean_text(pattern.get(key))
        if not value or value == "UNKNOWN" or value in seen:
            continue
        values.append(value)
        seen.add(value)
        if len(values) >= limit:
            break
    return ", ".join(_md_code(value) for value in values) if values else _md_code("UNKNOWN")


def _priority_list(patterns: Sequence[Dict[str, Any]]) -> str:
    rank = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    values = sorted(
        {_clean_text(pattern.get("investigation_priority")) for pattern in patterns if pattern.get("investigation_priority")},
        key=lambda value: (rank.get(value, 99), value),
    )
    return ", ".join(_md_code(value) for value in values) if values else _md_code("UNKNOWN")


def _render_site_pattern_family_summary(patterns: List[Dict[str, Any]]) -> List[str]:
    if not patterns:
        return []

    grouped: Dict[Tuple[str, str], List[Dict[str, Any]]] = defaultdict(list)
    for pattern in patterns:
        site_code = _clean_text(pattern.get("site_code")) or "UNKNOWN"
        family = _clean_text(pattern.get("pattern_family")) or "Other"
        grouped[(site_code, family)].append(pattern)

    lines = [
        "## Site Pattern Family Summary",
        "",
        "> Use this section first for Zabbix-alert questions. Individual alert patterns are evidence details, not the primary answer shape.",
        "",
    ]
    for (site_code, family), group in sorted(
        grouped.items(),
        key=lambda item: (item[0][0], -sum(int(pattern.get("alert_count") or 0) for pattern in item[1]), item[0][1]),
    ):
        group_sorted = sorted(group, key=lambda item: (-int(item.get("alert_count") or 0), item["alert_pattern_id"]))
        raw_alert_count = sum(int(pattern.get("alert_count") or 0) for pattern in group_sorted)
        lines.extend(
            [
                f"### {site_code} | {family}",
                "",
                f"- Pattern count: {_md_code(len(group_sorted))}",
                f"- Raw alert count across full export: {_md_code(raw_alert_count)}",
                f"- Investigation priorities: {_priority_list(group_sorted)}",
                f"- Sample signatures: {_sample_unique(group_sorted, 'problem_signature', 8)}",
                f"- Sample hosts: {_sample_unique(group_sorted, 'host', 12)}",
                f"- Example alert pattern IDs: {_sample_unique(group_sorted, 'alert_pattern_id', 8)}",
                "",
            ]
        )
    return lines


def _render_markdown(patterns: List[Dict[str, Any]], summary: Dict[str, Any]) -> str:
    lines = [
        "# Raw Zabbix Alert Patterns",
        "",
        "> Alert pattern is not a confirmed incident.",
        "",
        "```yaml",
        "record_type: ZABBIX_ALERT_PATTERN_SOURCE",
        f"package_section: {summary.get('package_section', PACKAGE_SECTION)}",
        f"knowledge_filename: {summary.get('knowledge_filename', KNOWLEDGE_FILENAME)}",
        f"source_dataset: {summary.get('source_label', 'UNKNOWN')}",
        f"source_type: {summary['source_type']}",
        f"input_rows: {summary['input_rows']}",
        f"record_count: {summary['record_count']}",
        f"alert_pattern_count: {summary['alert_pattern_count']}",
        f"rejected_row_count: {summary['rejected_row_count']}",
        f"duplicate_rows: {summary['duplicate_rows']}",
        f"reconciliation_passed: {str(summary['reconciliation_passed']).lower()}",
        f"upload_ready: {str(summary['upload_ready']).lower()}",
        "validation_status: PASS" if summary["upload_ready"] else "validation_status: FAIL",
        "note: Raw Zabbix alert patterns are monitoring signals, not confirmed incidents.",
        "```",
        "",
    ]
    lines.extend(_render_site_pattern_family_summary(patterns))
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
                f"last_recovered_at: {pattern['last_recovered_at']}",
                f"alert_count: {pattern['alert_count']}",
                f"resolved_count: {pattern['resolved_count']}",
                f"open_count: {pattern['open_count']}",
                f"severity: {pattern['severity']}",
                f"pattern_family: {pattern['pattern_family']}",
                f"investigation_priority: {pattern['investigation_priority']}",
                f"signal_assessment: {pattern['signal_assessment']}",
                f"domain: {pattern['domain']}",
                f"component: {pattern['component']}",
                f"scope: {pattern['scope']}",
                f"assessment: {pattern['assessment']}",
                f"evidence_label: {pattern['evidence_label']}",
                f"source_reference_count: {pattern['source_reference_count']}",
                "problem_signature: |",
                "  " + pattern["problem_signature"].replace("\n", "\n  "),
                "why_it_matters: |",
                "  " + pattern["why_it_matters"].replace("\n", "\n  "),
                "source_refs_sample: |",
                "  " + "; ".join(pattern["source_refs"]),
                "```",
                "",
            ]
        )
    return "\n".join(lines).strip() + "\n"


def _safe_file_stem(value: Any, fallback: str = "zabbix-alert-patterns") -> str:
    stem = Path(_clean_text(value)).stem
    stem = re.sub(r"[^A-Za-z0-9._-]+", "-", stem).strip("-._")
    return stem or fallback


def _make_markdown_file(markdown: str) -> Any:
    # Alpha file outputs preserve the filename best when the file-like object has a name.
    md_text = markdown or ""
    md_bytes = md_text.encode("utf-8")

    try:
        Path(KNOWLEDGE_FILENAME).write_bytes(md_bytes)
    except Exception:
        pass

    if md_text and len(md_bytes) < 100:
        raise ValueError("Generated markdown file is unexpectedly small")

    bio = io.BytesIO(md_bytes)
    bio.name = KNOWLEDGE_FILENAME
    bio.seek(0)
    return bio


def _build_error(reason: str, source_label: str = "zabbix_export") -> Dict[str, Any]:
    summary = {
        "ok": False,
        "source_type": "zabbix_csv",
        "package_section": PACKAGE_SECTION,
        "knowledge_filename": KNOWLEDGE_FILENAME,
        "source_label": source_label,
        "input_rows": 0,
        "record_count": 0,
        "alert_pattern_count": 0,
        "rejected_row_count": 1,
        "duplicate_rows": 0,
        "reconciliation_passed": False,
        "upload_ready": False,
        "error": reason,
    }
    json_result = {
        "ok": False,
        "summary": summary,
        "records": [],
        "records_omitted": 0,
        "rejected_rows": [
            {
                "row_number": None,
                "source_ref": source_label,
                "reason": reason,
                "row_data": {},
            }
        ],
    }
    patterns_result = {"ok": False, "record_count": 0, "records": []}
    return {
        "json_text": json.dumps(json_result, ensure_ascii=False, indent=2),
        "alert_patterns_text": json.dumps(patterns_result, ensure_ascii=False, indent=2),
        "json_result": json_result,
        "alert_patterns_result": patterns_result,
        "markdown": "",
        "knowledge_file": _make_markdown_file(""),
        "knowledge_filename": KNOWLEDGE_FILENAME,
        "package_section": PACKAGE_SECTION,
        "summary": summary,
    }


def _to_int(value: Any, default: int) -> int:
    try:
        return int(value)
    except Exception:
        return default


def _to_bool(value: Any, default: bool = DEFAULT_RETURN_MARKDOWN) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return default
    text = _clean_text(value).lower()
    if text in ("1", "true", "yes", "y", "on"):
        return True
    if text in ("0", "false", "no", "n", "off"):
        return False
    return default


def main(
    zabbix_export_file=None,
    zabbix_export_body=None,
    source_label=None,
    max_patterns=DEFAULT_MAX_PATTERNS,
    return_markdown=DEFAULT_RETURN_MARKDOWN,
):
    try:
        text, label = _csv_text_from_input(zabbix_export_file, zabbix_export_body, source_label)
    except Exception as exc:
        return _build_error(f"Failed to read Zabbix input: {exc}")

    if _looks_like_html(text):
        return _build_error("Input looks like HTML/login page; expected CSV export", label)

    reader = csv.DictReader(io.StringIO(text))
    if not reader.fieldnames:
        return _build_error("CSV appears to have no header row", label)

    mapping, is_normalized, missing = _canonical_mapping(reader.fieldnames)
    if missing:
        return _build_error("Missing required columns: " + ", ".join(missing), label)

    input_rows = 0
    duplicate_rows = 0
    rejected_rows = 0
    seen_keys = set()
    patterns_by_key: Dict[Tuple[str, str], Dict[str, Any]] = {}

    for row_number, row in enumerate(reader, start=2):
        input_rows += 1
        try:
            if is_normalized:
                event_id = _clean_text(_row_value(row, mapping, "event_id"))
                dedupe_key = ("normalized", event_id) if event_id else (
                    _clean_text(_row_value(row, mapping, "started_at_local")),
                    _clean_text(_row_value(row, mapping, "host")),
                    _clean_text(_row_value(row, mapping, "problem_raw")),
                )
                host = _unknown(_row_value(row, mapping, "host"))
                problem = _unknown(_row_value(row, mapping, "problem_raw"))
                tags = _parse_tags(_row_value(row, mapping, "tags_json"))
                record = {
                    "source_ref": f"{label}:row-{row_number}",
                    "seen_at": _clean_text(_row_value(row, mapping, "started_at_local")),
                    "recovered_at": _clean_text(_row_value(row, mapping, "recovered_at_local")),
                    "status": _unknown(_row_value(row, mapping, "status")).upper(),
                    "severity": _unknown(_row_value(row, mapping, "severity")),
                    "host": host,
                    "site_code": _clean_text(_row_value(row, mapping, "site_code"))
                    or _derive_site_code_from_host(host),
                    "problem_signature": _clean_text(_row_value(row, mapping, "problem_signature"))
                    or _normalize_problem_signature(problem),
                    "domain": _clean_text(_row_value(row, mapping, "domain"))
                    or ",".join(tags.get("class", []))
                    or "UNKNOWN",
                    "component": _clean_text(_row_value(row, mapping, "component"))
                    or ",".join(tags.get("component", []))
                    or "UNKNOWN",
                    "scope": _clean_text(_row_value(row, mapping, "scope"))
                    or ",".join(tags.get("scope", []))
                    or "UNKNOWN",
                }
            else:
                dedupe_key = tuple(_clean_text(_row_value(row, mapping, col)) for col in ZABBIX_REQUIRED_COLUMNS)
                host = _unknown(_row_value(row, mapping, "Host"))
                problem = _unknown(_row_value(row, mapping, "Problem"))
                tags = _parse_tags(_row_value(row, mapping, "Tags"))
                record = {
                    "source_ref": f"{label}:row-{row_number}",
                    "seen_at": _clean_text(_row_value(row, mapping, "Time")),
                    "recovered_at": _clean_text(_row_value(row, mapping, "Recovery time")),
                    "status": _unknown(_row_value(row, mapping, "Status")).upper(),
                    "severity": _unknown(_row_value(row, mapping, "Severity")),
                    "host": host,
                    "site_code": _derive_site_code_from_host(host),
                    "problem_signature": _normalize_problem_signature(problem),
                    "domain": ",".join(tags.get("class", [])) or "UNKNOWN",
                    "component": ",".join(tags.get("component", [])) or "UNKNOWN",
                    "scope": ",".join(tags.get("scope", [])) or "UNKNOWN",
                }

            if dedupe_key in seen_keys:
                duplicate_rows += 1
                continue
            seen_keys.add(dedupe_key)
            _update_pattern(patterns_by_key, record)
        except Exception:
            rejected_rows += 1

    patterns = _finalize_patterns(patterns_by_key, _to_int(max_patterns, DEFAULT_MAX_PATTERNS))
    record_count = max(0, input_rows - duplicate_rows - rejected_rows)
    summary = {
        "ok": True,
        "source_type": "zabbix_csv",
        "package_section": PACKAGE_SECTION,
        "knowledge_filename": KNOWLEDGE_FILENAME,
        "source_label": label,
        "input_rows": input_rows,
        "record_count": record_count,
        "alert_pattern_count": len(patterns_by_key),
        "alert_pattern_returned_count": len(patterns),
        "rejected_row_count": rejected_rows,
        "duplicate_rows": duplicate_rows,
        "reconciliation_passed": record_count + rejected_rows + duplicate_rows == input_rows,
        "upload_ready": rejected_rows == 0 and record_count > 0 and len(patterns_by_key) > 0,
        "is_normalized_input": is_normalized,
        "records_omitted": record_count,
        "patterns_omitted": max(0, len(patterns_by_key) - len(patterns)),
    }
    patterns_result = {
        "ok": True,
        "source_type": "zabbix_alert_patterns",
        "record_type": "ALERT_PATTERN_COLLECTION",
        "record_count": len(patterns_by_key),
        "records": patterns,
        "records_omitted": max(0, len(patterns_by_key) - len(patterns)),
    }
    json_result = {
        "ok": True,
        "summary": summary,
        "records": [],
        "records_omitted": record_count,
        "rejected_rows": [],
    }
    should_return_markdown = _to_bool(return_markdown)
    markdown = _render_markdown(patterns, summary) if should_return_markdown else ""
    knowledge_file = _make_markdown_file(markdown) if should_return_markdown else _make_markdown_file("")
    return {
        "json_text": json.dumps(json_result, ensure_ascii=False, indent=2),
        "alert_patterns_text": json.dumps(patterns_result, ensure_ascii=False, indent=2),
        "json_result": json_result,
        "alert_patterns_result": patterns_result,
        "markdown": markdown,
        "knowledge_file": knowledge_file,
        "knowledge_filename": KNOWLEDGE_FILENAME,
        "package_section": PACKAGE_SECTION,
        "summary": summary,
    }
