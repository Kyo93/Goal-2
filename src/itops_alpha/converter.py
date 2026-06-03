from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable

from openpyxl import Workbook, load_workbook


PACKAGE_VERSION = "1.2.0"
ISSUE_REPORT_FILENAME = "IssueReport.xlsx"
INCIDENT_REPORT_FILENAME = "SEA - Corp IT- ILL- Incident Report   (Responses).xlsx"
ZABBIX_FILENAME = "zbx_problems_export.xlsx"
ZABBIX_EXPORT_DIRNAME = "Export zabbix"

ISSUE_REQUIRED_COLUMNS = {
    "itcenter.ticket.comment.created_at",
    "itcenter.ticket.id",
    "itcenter.ticket.category_en_name",
    "itcenter.ticket.classification_name",
    "itcenter.ticket.full_title",
    "itcenter.ticket.service_recipient.user.business_unit",
    "itcenter.ticket.service_recipient.user.department_name",
    "itcenter.ticket.service_recipient.user.name",
    "itcenter.ticket.service_recipient.user.email",
    "itcenter.ticket.assignee.user.name",
    "itcenter.ticket.comment.text",
}

INCIDENT_REQUIRED_COLUMNS = {
    "Timestamp",
    "ISP",
    "SITE / Location",
    "Incident DATE",
    "Incident TIME",
    "Reporter",
    "Incindent Type",
    "Severity",
    "Incident description",
    "Initial Cause",
    "Troubleshooting actions",
    "Root Cause",
    "Incident resolution date",
    "Incident resolution time",
    "Measures to prevent recurrence of incidents (if any)",
}

ZABBIX_REQUIRED_COLUMNS = {
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
}

ZABBIX_NORMALIZED_REQUIRED_COLUMNS = {
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
}

MARKDOWN_FILENAMES = [
    "00_report_context.md",
    "01_executive_summary.md",
    "02_operational_timeline.md",
    "02_confirmed_incidents.md",
    "03_recurrence_patterns.md",
    "04_alert_patterns.md",
    "05_ticket_impact.md",
    "06_data_quality.md",
]


@dataclass
class AdapterResult:
    records: list[dict[str, Any]]
    input_rows: int
    skipped_blank_rows: int = 0
    duplicate_rows: int = 0
    rejected_rows: list[dict[str, Any]] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def clean_text(value: Any) -> str:
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()


def clean_multiline_text(value: Any) -> str:
    if value is None:
        return ""
    return str(value).replace("\r\n", "\n").replace("\r", "\n").strip()


def normalize_header(value: Any) -> str:
    return clean_text(value)


def stable_hash(*parts: Any, length: int = 12) -> str:
    payload = "\x1f".join(clean_text(part).lower() for part in parts)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:length].upper()


def source_ref(filename: str, sheet_name: str, row_number: int) -> str:
    return f"{filename}#{sheet_name}:row-{row_number}"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_datetime(value: Any) -> datetime:
    if isinstance(value, datetime):
        return value.replace(tzinfo=None)
    if isinstance(value, date):
        return datetime.combine(value, time.min)
    text = clean_text(value)
    if not text:
        raise ValueError("empty datetime value")
    formats = [
        "%b %d, %Y @ %H:%M:%S.%f",
        "%b %d, %Y @ %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S.%f",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %I:%M:%S %p",
        "%Y-%m-%d",
    ]
    try:
        return datetime.fromisoformat(text).replace(tzinfo=None)
    except ValueError:
        pass
    for date_format in formats:
        try:
            return datetime.strptime(text, date_format)
        except ValueError:
            continue
    raise ValueError(f"invalid datetime value: {text}")


def parse_time(value: Any) -> time:
    if isinstance(value, datetime):
        return value.time()
    if isinstance(value, time):
        return value
    text = clean_text(value)
    if not text:
        return time.min
    for time_format in ["%H:%M:%S", "%H:%M"]:
        try:
            return datetime.strptime(text, time_format).time()
        except ValueError:
            continue
    raise ValueError(f"invalid time value: {text}")


def combine_date_time(date_value: Any, time_value: Any) -> datetime:
    parsed_date = parse_datetime(date_value).date()
    parsed_time = parse_time(time_value)
    return datetime.combine(parsed_date, parsed_time)


def iso_datetime(value: datetime | None) -> str:
    return "" if value is None else value.isoformat(timespec="seconds")


def _is_blank_row(values: Iterable[Any]) -> bool:
    return not any(clean_text(value) for value in values)


def _load_sheet(path: Path, sheet_name: str | None = None):
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    workbook = load_workbook(path, read_only=True, data_only=True)
    worksheet = workbook[sheet_name] if sheet_name else workbook.worksheets[0]
    raw_rows = list(worksheet.iter_rows(values_only=True))
    if not raw_rows:
        workbook.close()
        raise ValueError(f"No rows found in {path.name}#{worksheet.title}")
    headers = [normalize_header(value) for value in raw_rows[0]]
    loaded_sheet_name = worksheet.title
    workbook.close()
    return loaded_sheet_name, headers, raw_rows[1:]


def _load_csv_rows(path: Path):
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        raw_rows = list(reader)
    if not raw_rows:
        raise ValueError(f"No rows found in {path.name}")
    headers = [normalize_header(value) for value in raw_rows[0]]
    return "csv", headers, raw_rows[1:]


def _validate_columns(path: Path, sheet_name: str, headers: list[str], required: set[str]):
    missing = sorted(required - set(headers))
    if missing:
        raise ValueError(
            f"Missing required columns in {path.name}#{sheet_name}: {', '.join(missing)}"
        )


def _row_dict(headers: list[str], values: Iterable[Any]) -> dict[str, Any]:
    values = list(values)
    padded = values + [""] * max(0, len(headers) - len(values))
    return {header: padded[index] if index < len(padded) else "" for index, header in enumerate(headers)}


def derive_site_code(site_name: Any) -> str:
    text = clean_text(site_name)
    if not text:
        return "UNKNOWN"
    return text.split(" - ", 1)[0].strip()


def derive_site_code_from_host(host: Any) -> str:
    match = re.match(r"^VNM([A-Z0-9]{3})", clean_text(host).upper())
    return match.group(1) if match else "UNKNOWN"


def load_incidents(path: Path) -> AdapterResult:
    sheet_name, headers, rows = _load_sheet(path, "Form Responses 1")
    _validate_columns(path, sheet_name, headers, INCIDENT_REQUIRED_COLUMNS)
    records: list[dict[str, Any]] = []
    rejected_rows: list[dict[str, Any]] = []
    skipped_blank_rows = 0
    input_rows = 0

    for row_number, values in enumerate(rows, start=2):
        if _is_blank_row(values):
            skipped_blank_rows += 1
            continue
        input_rows += 1
        row = _row_dict(headers, values)
        reference = source_ref(path.name, sheet_name, row_number)
        try:
            submitted_at = (
                parse_datetime(row["Timestamp"]) if clean_text(row["Timestamp"]) else None
            )
            started_at = combine_date_time(row["Incident DATE"], row["Incident TIME"])
            resolved_at = None
            if clean_text(row["Incident resolution date"]):
                resolved_at = combine_date_time(
                    row["Incident resolution date"], row["Incident resolution time"]
                )
        except ValueError as error:
            rejected_rows.append({"source_ref": reference, "reason": str(error)})
            continue

        site_code = derive_site_code(row["SITE / Location"])
        isp = clean_text(row["ISP"]) or "UNKNOWN"
        incident_type = clean_text(row["Incindent Type"]) or "UNKNOWN"
        duration_minutes = (
            round((resolved_at - started_at).total_seconds() / 60, 2)
            if resolved_at is not None
            else None
        )
        records.append(
            {
                "incident_id": f"INC-{row_number}",
                "source_ref": reference,
                "submitted_at": iso_datetime(submitted_at),
                "started_at": iso_datetime(started_at),
                "resolved_at": iso_datetime(resolved_at),
                "duration_minutes": duration_minutes,
                "site_code": site_code,
                "site_name": clean_text(row["SITE / Location"]) or "UNKNOWN",
                "isp": isp,
                "reporter": clean_text(row["Reporter"]) or "UNKNOWN",
                "incident_type": incident_type,
                "severity": clean_text(row["Severity"]) or "UNKNOWN",
                "description": clean_multiline_text(row["Incident description"]) or "UNKNOWN",
                "initial_cause": clean_multiline_text(row["Initial Cause"]) or "UNKNOWN",
                "troubleshooting_actions": clean_multiline_text(row["Troubleshooting actions"])
                or "UNKNOWN",
                "root_cause": clean_multiline_text(row["Root Cause"]) or "UNKNOWN",
                "preventive_action": clean_multiline_text(
                    row["Measures to prevent recurrence of incidents (if any)"]
                )
                or "UNKNOWN",
                "resolution_status": "RESOLVED" if resolved_at else "UNKNOWN",
                "recurrence_key": "|".join(
                    [site_code.lower(), isp.lower(), incident_type.lower()]
                ),
                "evidence_label": "SOURCE FACT",
            }
        )
    return AdapterResult(
        records=records,
        input_rows=input_rows,
        skipped_blank_rows=skipped_blank_rows,
        rejected_rows=rejected_rows,
    )


def load_issue_tickets(path: Path) -> AdapterResult:
    sheet_name, headers, rows = _load_sheet(path)
    _validate_columns(path, sheet_name, headers, ISSUE_REQUIRED_COLUMNS)
    grouped: dict[str, dict[str, Any]] = {}
    rejected_rows: list[dict[str, Any]] = []
    skipped_blank_rows = 0
    input_rows = 0

    for row_number, values in enumerate(rows, start=2):
        if _is_blank_row(values):
            skipped_blank_rows += 1
            continue
        input_rows += 1
        row = _row_dict(headers, values)
        reference = source_ref(path.name, sheet_name, row_number)
        try:
            comment_at = parse_datetime(row["itcenter.ticket.comment.created_at"])
        except ValueError as error:
            rejected_rows.append({"source_ref": reference, "reason": str(error)})
            continue
        ticket_id = clean_text(row["itcenter.ticket.id"])
        if not ticket_id:
            rejected_rows.append({"source_ref": reference, "reason": "empty ticket id"})
            continue
        comment_text = clean_multiline_text(row["itcenter.ticket.comment.text"])
        ticket = grouped.setdefault(
            ticket_id,
            {
                "ticket_id": ticket_id,
                "source_refs": [],
                "comment_times": [],
                "comments": [],
                "category": clean_text(row["itcenter.ticket.category_en_name"]) or "UNKNOWN",
                "classification": clean_text(row["itcenter.ticket.classification_name"])
                or "UNKNOWN",
                "title": clean_text(row["itcenter.ticket.full_title"]) or "UNKNOWN",
                "business_unit": clean_text(
                    row["itcenter.ticket.service_recipient.user.business_unit"]
                )
                or "UNKNOWN",
                "department": clean_text(
                    row["itcenter.ticket.service_recipient.user.department_name"]
                )
                or "UNKNOWN",
                "user_name": clean_text(row["itcenter.ticket.service_recipient.user.name"])
                or "UNKNOWN",
                "user_email": clean_text(row["itcenter.ticket.service_recipient.user.email"])
                or "UNKNOWN",
                "assignee": clean_text(row["itcenter.ticket.assignee.user.name"]) or "UNKNOWN",
            },
        )
        ticket["source_refs"].append(reference)
        ticket["comment_times"].append(comment_at)
        ticket["comments"].append(comment_text)

    records = []
    for ticket_id in sorted(grouped):
        ticket = grouped[ticket_id]
        comments = [comment for comment in ticket.pop("comments") if comment]
        comment_times = ticket.pop("comment_times")
        ticket.update(
            {
                "first_comment_at": iso_datetime(min(comment_times)),
                "last_comment_at": iso_datetime(max(comment_times)),
                "comment_count": len(comment_times),
                "comments_summary": " | ".join(comments[:3]) or "UNKNOWN",
                "impact_evidence": ticket["title"],
                "evidence_label": "SOURCE FACT",
            }
        )
        records.append(ticket)
    return AdapterResult(
        records=records,
        input_rows=input_rows,
        skipped_blank_rows=skipped_blank_rows,
        rejected_rows=rejected_rows,
    )


def parse_tags(value: Any) -> dict[str, list[str]]:
    tags: defaultdict[str, list[str]] = defaultdict(list)
    for token in clean_text(value).split(", "):
        if ": " not in token:
            continue
        key, tag_value = token.split(": ", 1)
        if tag_value not in tags[key]:
            tags[key].append(tag_value)
    return dict(tags)


def parse_tags_json(value: Any) -> dict[str, list[str]]:
    text = clean_text(value)
    if not text:
        return {}
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        return parse_tags(text)
    if not isinstance(payload, dict):
        return {}
    tags: dict[str, list[str]] = {}
    for key, raw_values in payload.items():
        if isinstance(raw_values, list):
            values = [clean_text(item) for item in raw_values if clean_text(item)]
        else:
            values = [clean_text(raw_values)] if clean_text(raw_values) else []
        if values:
            tags[clean_text(key)] = values
    return tags


def normalize_problem_signature(problem: Any) -> str:
    text = clean_text(problem).lower()
    text = re.sub(
        r"current:\s*\d+(?:\.\d+)?\s*mbps",
        "current:<value> mbps",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"\d+(?:\.\d+)?(?:-\d+(?:\.\d+)?)?\s*(?:mbps|gbps|%|hz|m|s|℃|°c)\b",
        "<value>",
        text,
        flags=re.IGNORECASE,
    )
    return text


def _load_zabbix_sources(path: Path) -> list[tuple[Path, str, list[str], list[Iterable[Any]]]]:
    if path.is_dir():
        csv_paths = sorted(path.glob("*.csv"), key=lambda item: item.name.lower())
        if not csv_paths:
            raise FileNotFoundError(f"No CSV files found in Zabbix export directory: {path}")
        normalized_paths = [
            csv_path
            for csv_path in csv_paths
            if csv_path.name.lower().startswith("zbx_problems_normalized_")
        ]
        if normalized_paths:
            csv_paths = normalized_paths
        return [
            (csv_path, *_load_csv_rows(csv_path))
            for csv_path in csv_paths
        ]
    sheet_name, headers, rows = _load_sheet(path)
    return [(path, sheet_name, headers, rows)]


def load_zabbix_alerts(path: Path) -> AdapterResult:
    sources = _load_zabbix_sources(path)
    records: list[dict[str, Any]] = []
    rejected_rows: list[dict[str, Any]] = []
    skipped_blank_rows = 0
    input_rows = 0
    duplicate_rows = 0
    seen_rows: set[tuple[str, ...]] = set()

    for source_path, sheet_name, headers, rows in sources:
        header_set = set(headers)
        is_normalized = ZABBIX_NORMALIZED_REQUIRED_COLUMNS.issubset(header_set)
        if not is_normalized:
            _validate_columns(source_path, sheet_name, headers, ZABBIX_REQUIRED_COLUMNS)
        for row_number, values in enumerate(rows, start=2):
            if _is_blank_row(values):
                skipped_blank_rows += 1
                continue
            input_rows += 1
            row = _row_dict(headers, values)
            reference = source_ref(source_path.name, sheet_name, row_number)
            if is_normalized:
                dedupe_key = ("normalized", clean_text(row.get("event_id")))
            else:
                dedupe_key = tuple(clean_text(row.get(header)) for header in sorted(ZABBIX_REQUIRED_COLUMNS))
            if dedupe_key in seen_rows:
                duplicate_rows += 1
                continue
            seen_rows.add(dedupe_key)
            if is_normalized:
                try:
                    seen_at = parse_datetime(row["started_at_local"])
                    recovered_at = (
                        parse_datetime(row["recovered_at_local"])
                        if clean_text(row["recovered_at_local"])
                        else None
                    )
                except ValueError as error:
                    rejected_rows.append({"source_ref": reference, "reason": str(error)})
                    continue
                host = clean_text(row["host"]) or "UNKNOWN"
                problem = clean_text(row["problem_raw"]) or "UNKNOWN"
                tags = parse_tags_json(row["tags_json"])
                action_count = clean_text(row["action_count"])
                records.append(
                    {
                        "alert_id": f"ALT-ZBX-{clean_text(row['event_id'])}",
                        "source_ref": reference,
                        "seen_at": iso_datetime(seen_at),
                        "recovered_at": iso_datetime(recovered_at),
                        "status": clean_text(row["status"]) or "UNKNOWN",
                        "severity": clean_text(row["severity"]) or "UNKNOWN",
                        "host": host,
                        "site_code": clean_text(row["site_code"]) or derive_site_code_from_host(host),
                        "problem": problem,
                        "problem_signature": clean_text(row["problem_signature"])
                        or normalize_problem_signature(problem),
                        "duration": clean_text(row["duration_text"]) or "UNKNOWN",
                        "ack": "Yes" if clean_text(row["acknowledged"]).lower() == "true" else "No",
                        "actions": f"Actions ({action_count})" if action_count and action_count != "0" else "UNKNOWN",
                        "domain": clean_text(row["domain"]) or ",".join(tags.get("class", [])) or "UNKNOWN",
                        "component": clean_text(row["component"])
                        or ",".join(tags.get("component", []))
                        or "UNKNOWN",
                        "scope": clean_text(row["scope"]) or ",".join(tags.get("scope", [])) or "UNKNOWN",
                        "tags": json.dumps(tags, ensure_ascii=False, sort_keys=True),
                        "evidence_label": clean_text(row.get("evidence_label")) or "SOURCE FACT",
                    }
                )
            else:
                try:
                    seen_at = parse_datetime(row["Time"])
                    recovered_at = (
                        parse_datetime(row["Recovery time"])
                        if clean_text(row["Recovery time"])
                        else None
                    )
                except ValueError as error:
                    rejected_rows.append({"source_ref": reference, "reason": str(error)})
                    continue
                host = clean_text(row["Host"]) or "UNKNOWN"
                problem = clean_text(row["Problem"]) or "UNKNOWN"
                tags = parse_tags(row["Tags"])
                records.append(
                    {
                        "alert_id": f"ALT-{stable_hash(source_path.name, row_number)}",
                        "source_ref": reference,
                        "seen_at": iso_datetime(seen_at),
                        "recovered_at": iso_datetime(recovered_at),
                        "status": clean_text(row["Status"]) or "UNKNOWN",
                        "severity": clean_text(row["Severity"]) or "UNKNOWN",
                        "host": host,
                        "site_code": derive_site_code_from_host(host),
                        "problem": problem,
                        "problem_signature": normalize_problem_signature(problem),
                        "duration": clean_text(row["Duration"]) or "UNKNOWN",
                        "ack": clean_text(row["Ack"]) or "UNKNOWN",
                        "actions": clean_text(row["Actions"]) or "UNKNOWN",
                        "domain": ",".join(tags.get("class", [])) or "UNKNOWN",
                        "component": ",".join(tags.get("component", [])) or "UNKNOWN",
                        "scope": ",".join(tags.get("scope", [])) or "UNKNOWN",
                        "tags": json.dumps(tags, ensure_ascii=False, sort_keys=True),
                        "evidence_label": "SOURCE FACT",
                    }
                )
    return AdapterResult(
        records=records,
        input_rows=input_rows,
        skipped_blank_rows=skipped_blank_rows,
        duplicate_rows=duplicate_rows,
        rejected_rows=rejected_rows,
    )


def _join_unique(values: Iterable[str]) -> str:
    return ",".join(sorted({value for value in values if value and value != "UNKNOWN"})) or "UNKNOWN"


def group_alert_patterns(alerts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: defaultdict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for alert in alerts:
        grouped[(alert["host"], alert["problem_signature"])].append(alert)

    patterns = []
    for (host, signature), records in grouped.items():
        records = sorted(records, key=lambda record: (record["seen_at"], record["source_ref"]))
        patterns.append(
            {
                "alert_pattern_id": f"ALP-{stable_hash(host, signature)}",
                "source_refs": [record["source_ref"] for record in records],
                "first_seen_at": records[0]["seen_at"],
                "last_seen_at": records[-1]["seen_at"],
                "last_recovered_at": max(
                    (record["recovered_at"] for record in records if record["recovered_at"]),
                    default="",
                ),
                "alert_count": len(records),
                "resolved_count": sum(record["status"] == "RESOLVED" for record in records),
                "open_count": sum(record["status"] != "RESOLVED" for record in records),
                "host": host,
                "site_code": records[0]["site_code"],
                "severity": _join_unique(record["severity"] for record in records),
                "problem_signature": signature,
                "domain": _join_unique(record["domain"] for record in records),
                "component": _join_unique(record["component"] for record in records),
                "scope": _join_unique(record["scope"] for record in records),
                "assessment": "RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT",
                "evidence_label": "COMPUTED FACT",
            }
        )
    return sorted(patterns, key=lambda pattern: (-pattern["alert_count"], pattern["alert_pattern_id"]))


def group_incident_recurrence(incidents: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    for incident in incidents:
        grouped[incident["recurrence_key"]].append(incident)
    patterns = []
    for key, records in grouped.items():
        records = sorted(records, key=lambda record: (record["started_at"], record["incident_id"]))
        first = records[0]
        patterns.append(
            {
                "recurrence_id": f"REC-{stable_hash(key)}",
                "recurrence_key": key,
                "site_code": first["site_code"],
                "site_name": first["site_name"],
                "isp": first["isp"],
                "incident_type": first["incident_type"],
                "incident_count": len(records),
                "incident_ids": [record["incident_id"] for record in records],
                "source_refs": [record["source_ref"] for record in records],
                "first_seen_at": records[0]["started_at"],
                "last_seen_at": records[-1]["started_at"],
                "root_causes": _join_unique(record["root_cause"] for record in records),
                "evidence_label": "COMPUTED FACT",
            }
        )
    return sorted(patterns, key=lambda pattern: (-pattern["incident_count"], pattern["recurrence_id"]))


RESPONSIBILITY_RULES = [
    (
        "ISP",
        [
            "routing",
            "uplink",
            "transit",
            "fiber",
            "fibre",
            "cable",
            "cáp",
            "provider",
            "vnpt",
            "fpt",
            "cmc",
            "netnam",
        ],
    ),
    (
        "INHOUSE",
        [
            "local segment",
            "internal",
            "switch",
            "firewall",
            "configuration",
            "linecard",
            "junos",
            "wifi controller",
            "access point",
        ],
    ),
    (
        "EXTERNAL",
        [
            "electricity",
            "utility",
            "power supply",
            "third-party",
            "third party",
        ],
    ),
]


def classify_responsibility_domain(root_cause: Any) -> tuple[str, str]:
    text = clean_text(root_cause).lower()
    if not text or text == "unknown":
        return "UNKNOWN", "RCA does not support responsibility classification"
    for domain, keywords in RESPONSIBILITY_RULES:
        for keyword in keywords:
            if keyword in text:
                return domain, f"RCA keyword rule: {keyword}"
    return "UNKNOWN", "RCA does not support responsibility classification"


def _time_windows_overlap(
    left_start: str,
    left_end: str,
    right_start: str,
    right_end: str,
    buffer_minutes: int = 60,
) -> bool:
    left_start_at = parse_datetime(left_start)
    left_end_at = parse_datetime(left_end or left_start)
    right_start_at = parse_datetime(right_start)
    right_end_at = parse_datetime(right_end or right_start)
    buffer = timedelta(minutes=buffer_minutes)
    return left_start_at - buffer <= right_end_at and right_start_at <= left_end_at + buffer


def _alert_pattern_id_for_record(alert: dict[str, Any]) -> str:
    return f"ALP-{stable_hash(alert['host'], alert['problem_signature'])}"


def _alert_event_overlaps_incident(
    incident: dict[str, Any], alert: dict[str, Any], buffer_minutes: int
) -> bool:
    if alert["site_code"] != incident["site_code"]:
        return False
    alert_end = alert.get("recovered_at") or incident.get("resolved_at") or incident["started_at"]
    return _time_windows_overlap(
        incident["started_at"],
        incident.get("resolved_at") or incident["started_at"],
        alert["seen_at"],
        alert_end,
        buffer_minutes,
    )


def _related_alert_pattern_ids(
    incident: dict[str, Any],
    alert_patterns: list[dict[str, Any]],
    buffer_minutes: int,
    alerts: list[dict[str, Any]] | None = None,
) -> list[str]:
    if alerts is None:
        return sorted(
            pattern["alert_pattern_id"]
            for pattern in alert_patterns
            if pattern["site_code"] == incident["site_code"]
            and _time_windows_overlap(
                incident["started_at"],
                incident.get("resolved_at") or incident["started_at"],
                pattern["first_seen_at"],
                pattern["last_seen_at"],
                buffer_minutes,
            )
        )

    known_pattern_ids = {pattern["alert_pattern_id"] for pattern in alert_patterns}
    return sorted(
        {
            pattern_id
            for alert in alerts
            if _alert_event_overlaps_incident(incident, alert, buffer_minutes)
            for pattern_id in [_alert_pattern_id_for_record(alert)]
            if pattern_id in known_pattern_ids
        }
    )


def _text_contains_site_code(record: dict[str, Any], site_code: str) -> bool:
    if not site_code or site_code == "UNKNOWN":
        return False
    text = " ".join(
        clean_text(record.get(field))
        for field in ["title", "comments_summary", "impact_evidence"]
    )
    return bool(
        re.search(
            rf"(?<![A-Za-z0-9]){re.escape(site_code)}(?![A-Za-z0-9])",
            text,
            flags=re.IGNORECASE,
        )
    )


def _estimated_user_impact(description: Any) -> bool:
    text = clean_text(description).lower()
    return any(
        keyword in text
        for keyword in [
            "user",
            "impact",
            "affected",
            "service interruption",
            "service disruption",
            "service is down",
            "outage",
        ]
    )


def build_operational_timeline(
    incidents: list[dict[str, Any]],
    alert_patterns: list[dict[str, Any]],
    tickets: list[dict[str, Any]],
    buffer_minutes: int = 60,
    alerts: list[dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    related_incidents_by_alert: defaultdict[str, list[str]] = defaultdict(list)
    events: list[dict[str, Any]] = []

    for incident in incidents:
        related_alerts = _related_alert_pattern_ids(
            incident, alert_patterns, buffer_minutes, alerts
        )
        for alert_pattern_id in related_alerts:
            related_incidents_by_alert[alert_pattern_id].append(incident["incident_id"])
        related_tickets = [
            ticket["ticket_id"]
            for ticket in tickets
            if _text_contains_site_code(ticket, incident["site_code"])
            and _time_windows_overlap(
                incident["started_at"],
                incident["resolved_at"],
                ticket["first_comment_at"],
                ticket["last_comment_at"],
                buffer_minutes,
            )
        ]
        responsibility_domain, responsibility_basis = classify_responsibility_domain(
            incident["root_cause"]
        )
        user_impact_status = (
            "CONFIRMED"
            if related_tickets
            else "ESTIMATED"
            if _estimated_user_impact(incident["description"])
            else "NO_EVIDENCE"
        )
        correlation_basis = (
            f"Same-site buffered time-window correlation ({buffer_minutes} minutes); "
            "correlation is context, not proof of RCA or user impact."
        )
        events.append(
            {
                "event_id": f"EVT-{incident['incident_id']}",
                "event_type": "CONFIRMED_INCIDENT",
                "started_at": incident["started_at"],
                "ended_at": incident["resolved_at"] or "UNKNOWN",
                "site_code": incident["site_code"],
                "summary": f"{incident['incident_type']}: {incident['description']}",
                "responsibility_domain": responsibility_domain,
                "responsibility_basis": responsibility_basis,
                "user_impact_status": user_impact_status,
                "resolution_status": incident["resolution_status"],
                "confirmed_rca": incident["root_cause"],
                "related_incident_ids": [incident["incident_id"]],
                "related_alert_pattern_ids": sorted(related_alerts),
                "related_ticket_ids": sorted(related_tickets),
                "correlation_basis": correlation_basis,
                "source_refs": [incident["source_ref"]],
                "evidence_label": "COMPUTED FACT",
            }
        )

    for pattern in alert_patterns:
        events.append(
            {
                "event_id": f"EVT-{pattern['alert_pattern_id']}",
                "event_type": "ZABBIX_ALERT_PATTERN",
                "started_at": pattern["first_seen_at"],
                "ended_at": pattern["last_seen_at"],
                "site_code": pattern["site_code"],
                "summary": (
                    f"{pattern['host']}: {pattern['problem_signature']} "
                    f"({pattern['alert_count']} raw alerts)"
                ),
                "responsibility_domain": "UNKNOWN",
                "responsibility_basis": "Raw alert pattern cannot establish responsibility",
                "user_impact_status": "UNKNOWN",
                "resolution_status": "UNKNOWN",
                "confirmed_rca": "UNKNOWN",
                "related_incident_ids": sorted(
                    related_incidents_by_alert[pattern["alert_pattern_id"]]
                ),
                "related_alert_pattern_ids": [pattern["alert_pattern_id"]],
                "related_ticket_ids": [],
                "correlation_basis": (
                    f"Same-site buffered time-window correlation ({buffer_minutes} minutes); "
                    "raw alert pattern remains monitoring evidence, not a confirmed incident."
                ),
                "source_refs": pattern["source_refs"],
                "evidence_label": "COMPUTED FACT",
            }
        )
    return sorted(events, key=lambda event: (event["started_at"], event["event_id"]))


RELEVANCE_STOPWORDS = {
    "and",
    "are",
    "at",
    "for",
    "from",
    "has",
    "high",
    "into",
    "not",
    "of",
    "on",
    "out",
    "over",
    "same",
    "the",
    "this",
    "to",
    "with",
}


def _relevance_tokens(value: Any) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z0-9]+", clean_text(value).lower())
        if len(token) >= 3 and token not in RELEVANCE_STOPWORDS
    }


def _ticket_matches_relevance(ticket: dict[str, Any], relevance_text: str) -> bool:
    title_text = clean_text(ticket.get("title"))
    ticket_text = " ".join(
        clean_text(ticket.get(field))
        for field in ["title", "comments_summary", "impact_evidence"]
    )
    title_tokens = _relevance_tokens(title_text)
    ticket_tokens = _relevance_tokens(ticket_text)
    evidence_tokens = _relevance_tokens(relevance_text)
    if title_tokens & evidence_tokens:
        return True
    if len(ticket_tokens & evidence_tokens) >= 2:
        return True
    joined = f" {title_text.lower()} "
    categories = {
        "network": {
            "access",
            "bandwidth",
            "connect",
            "connection",
            "connectivity",
            "latency",
            "network",
            "offline",
            "routing",
            "slow",
            "unreachable",
            "uplink",
        },
        "power": {"ups", "power", "battery", "electricity", "frequency"},
        "hardware": {"temperature", "sensor", "hardware", "switch", "firewall"},
    }
    evidence_categories = {
        category
        for category, terms in categories.items()
        if evidence_tokens & terms
    }
    ticket_categories = {
        category
        for category, terms in categories.items()
        if any(term in joined for term in terms)
    }
    return bool(evidence_categories & ticket_categories)


def _related_tickets(
    tickets: list[dict[str, Any]],
    site_code: str,
    started_at: str,
    ended_at: str,
    relevance_text: str,
    buffer_minutes: int,
) -> list[dict[str, Any]]:
    return [
        ticket
        for ticket in tickets
        if _text_contains_site_code(ticket, site_code)
        and _ticket_matches_relevance(ticket, relevance_text)
        and _time_windows_overlap(
            started_at,
            ended_at,
            ticket["first_comment_at"],
            ticket["last_comment_at"],
            buffer_minutes,
        )
    ]


def _evidence_coverage(has_zabbix: bool, has_incident: bool, has_ticket: bool) -> str:
    labels = []
    if has_zabbix:
        labels.append("ZABBIX")
    if has_incident:
        labels.append("INCIDENT FORM")
    if has_ticket:
        labels.append("TICKET")
    return " + ".join(labels) or "NONE"


def _ordered_milestones(items: list[dict[str, str]]) -> list[dict[str, str]]:
    return sorted(items, key=lambda item: (item["at"] == "UNKNOWN", item["at"], item["type"]))


def build_operational_stories(
    incidents: list[dict[str, Any]],
    alert_patterns: list[dict[str, Any]],
    tickets: list[dict[str, Any]],
    recurrence: list[dict[str, Any]],
    buffer_minutes: int = 60,
    alerts: list[dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    related_incidents_by_alert: defaultdict[str, list[str]] = defaultdict(list)
    alert_patterns_by_id = {
        pattern["alert_pattern_id"]: pattern for pattern in alert_patterns
    }
    recurrence_by_incident = {
        incident_id: pattern
        for pattern in recurrence
        for incident_id in pattern["incident_ids"]
    }
    stories: list[dict[str, Any]] = []

    for incident in incidents:
        related_alerts = [
            alert_patterns_by_id[pattern_id]
            for pattern_id in _related_alert_pattern_ids(
                incident, alert_patterns, buffer_minutes, alerts
            )
            if pattern_id in alert_patterns_by_id
        ]
        for pattern in related_alerts:
            related_incidents_by_alert[pattern["alert_pattern_id"]].append(
                incident["incident_id"]
            )
        related_tickets = _related_tickets(
            tickets,
            incident["site_code"],
            incident["started_at"],
            incident["resolved_at"],
            " ".join(
                [
                    incident["incident_type"],
                    incident["description"],
                    incident["root_cause"],
                ]
            ),
            buffer_minutes,
        )
        responsibility_domain, responsibility_basis = classify_responsibility_domain(
            incident["root_cause"]
        )
        user_impact_status = (
            "CONFIRMED"
            if related_tickets
            else "ESTIMATED"
            if _estimated_user_impact(incident["description"])
            else "NO_EVIDENCE"
        )
        milestones = [
            {
                "at": incident["started_at"],
                "type": "INCIDENT_STARTED",
                "message": (
                    f"IT recorded confirmed incident {incident['incident_id']} at "
                    f"{incident['site_code']}: {incident['incident_type']}."
                ),
            },
            {
                "at": incident.get("submitted_at") or incident["started_at"],
                "type": "RCA_RECORDED",
                "message": f"Confirmed RCA recorded: {incident['root_cause']}",
            },
        ]
        for pattern in related_alerts:
            milestones.append(
                {
                    "at": pattern["first_seen_at"],
                    "type": "ZABBIX_DETECTED",
                    "message": (
                        f"Zabbix detected {pattern['problem_signature']} at "
                        f"{pattern['host']} ({pattern['alert_pattern_id']})."
                    ),
                }
            )
        for ticket in related_tickets:
            milestones.append(
                {
                    "at": ticket["first_comment_at"],
                    "type": "USER_TICKET",
                    "message": (
                        f"Ticket {ticket['ticket_id']} provided direct site-explicit "
                        f"user evidence: {ticket['title']}"
                    ),
                }
            )
        if incident["resolved_at"]:
            milestones.append(
                {
                    "at": incident["resolved_at"],
                    "type": "SERVICE_RECOVERED",
                    "message": "Service recovered according to the confirmed incident record.",
                }
            )
        recurrence_pattern = recurrence_by_incident.get(incident["incident_id"])
        recurrence_summary = (
            f"{recurrence_pattern['incident_count']} confirmed incidents "
            f"({recurrence_pattern['recurrence_id']})"
            if recurrence_pattern
            else "1 confirmed incident"
        )
        gaps = []
        if not related_alerts:
            gaps.append("No same-site Zabbix signal matched this incident window.")
        if not related_tickets:
            gaps.append("No direct site-explicit ticket matched this incident window.")
        if incident["root_cause"] == "UNKNOWN":
            gaps.append("Confirmed RCA is missing.")
        stories.append(
            {
                "episode_id": f"OPS-{incident['incident_id']}",
                "episode_type": "CONFIRMED_INCIDENT",
                "started_at": incident["started_at"],
                "ended_at": incident["resolved_at"] or "UNKNOWN",
                "site_code": incident["site_code"],
                "headline": f"{incident['site_code']} | {incident['incident_type']}",
                "milestones": _ordered_milestones(milestones),
                "signal_assessment": (
                    "RELATED_TO_CONFIRMED_INCIDENT"
                    if related_alerts
                    else "NO_MATCHING_ZABBIX_SIGNAL"
                ),
                "user_impact_status": user_impact_status,
                "responsibility_domain": responsibility_domain,
                "responsibility_basis": responsibility_basis,
                "confirmed_rca": incident["root_cause"],
                "resolution_status": incident["resolution_status"],
                "recurrence_summary": recurrence_summary,
                "evidence_coverage": _evidence_coverage(
                    bool(related_alerts), True, bool(related_tickets)
                ),
                "investigation_gaps": gaps or ["None."],
                "related_incident_ids": [incident["incident_id"]],
                "related_alert_pattern_ids": sorted(
                    pattern["alert_pattern_id"] for pattern in related_alerts
                ),
                "related_ticket_ids": sorted(ticket["ticket_id"] for ticket in related_tickets),
                "source_refs": [incident["source_ref"]],
                "evidence_label": "COMPUTED FACT",
            }
        )

    for pattern in alert_patterns:
        related_incident_ids = sorted(
            related_incidents_by_alert[pattern["alert_pattern_id"]]
        )
        related_tickets = _related_tickets(
            tickets,
            pattern["site_code"],
            pattern["first_seen_at"],
            pattern["last_seen_at"],
            " ".join(
                [
                    pattern["problem_signature"],
                    pattern.get("domain", ""),
                    pattern.get("component", ""),
                ]
            ),
            buffer_minutes,
        )
        if related_incident_ids:
            assessment = "RELATED_TO_CONFIRMED_INCIDENT"
        elif related_tickets:
            assessment = "USER_IMPACT_SIGNAL"
        elif pattern["alert_count"] > 1:
            assessment = "LIKELY_NOISE_OR_THRESHOLD_REVIEW"
        else:
            assessment = "UNCONFIRMED_MONITORING_SIGNAL"
        milestones = [
            {
                "at": pattern["first_seen_at"],
                "type": "ZABBIX_DETECTED",
                "message": (
                    f"Zabbix detected {pattern['problem_signature']} at "
                    f"{pattern['host']}."
                ),
            }
        ]
        if pattern["alert_count"] > 1:
            milestones.append(
                {
                    "at": pattern["last_seen_at"],
                    "type": "ALERTS_GROUPED",
                    "message": (
                        f"Grouped {pattern['alert_count']} raw alerts with the same "
                        f"host and normalized signature into {pattern['alert_pattern_id']}."
                    ),
                }
            )
        for ticket in related_tickets:
            milestones.append(
                {
                    "at": ticket["first_comment_at"],
                    "type": "USER_TICKET",
                    "message": (
                        f"Ticket {ticket['ticket_id']} provided direct site-explicit "
                        f"user evidence: {ticket['title']}"
                    ),
                }
            )
        if pattern.get("last_recovered_at"):
            milestones.append(
                {
                    "at": pattern["last_recovered_at"],
                    "type": "SIGNAL_RECOVERED",
                    "message": (
                        f"Latest recovered Zabbix observation recorded for "
                        f"{pattern['alert_pattern_id']}."
                    ),
                }
            )
        gaps = []
        if not related_incident_ids:
            gaps.append("No confirmed incident matched this monitoring-signal window.")
        if not related_tickets:
            gaps.append("No direct site-explicit ticket matched this monitoring-signal window.")
        stories.append(
            {
                "episode_id": f"OPS-{pattern['alert_pattern_id']}",
                "episode_type": "MONITORING_SIGNAL",
                "started_at": pattern["first_seen_at"],
                "ended_at": pattern["last_recovered_at"] or pattern["last_seen_at"],
                "site_code": pattern["site_code"],
                "headline": f"{pattern['site_code']} | {pattern['host']} | {pattern['problem_signature']}",
                "milestones": _ordered_milestones(milestones),
                "signal_assessment": assessment,
                "user_impact_status": "CONFIRMED" if related_tickets else "UNKNOWN",
                "responsibility_domain": "UNKNOWN",
                "responsibility_basis": "Raw alert pattern cannot establish responsibility",
                "confirmed_rca": "UNKNOWN",
                "resolution_status": (
                    "SIGNAL_RECOVERED" if pattern["open_count"] == 0 else "SIGNAL_OPEN"
                ),
                "recurrence_summary": f"{pattern['alert_count']} raw alerts in grouped pattern",
                "evidence_coverage": _evidence_coverage(
                    True, bool(related_incident_ids), bool(related_tickets)
                ),
                "investigation_gaps": gaps or ["None."],
                "related_incident_ids": related_incident_ids,
                "related_alert_pattern_ids": [pattern["alert_pattern_id"]],
                "related_ticket_ids": sorted(ticket["ticket_id"] for ticket in related_tickets),
                "source_refs": pattern["source_refs"],
                "evidence_label": "COMPUTED FACT",
            }
        )
    return sorted(stories, key=lambda story: (story["started_at"], story["episode_id"]))


def load_confirmed_master_data(path: Path | None) -> dict[str, Any]:
    result = {
        "sites": {},
        "hosts": {},
        "network_links": {},
        "services": {},
        "user_groups": {},
        "service_dependencies": {},
        "unconfirmed_rows": 0,
    }
    if path is None or not path.exists():
        return result
    workbook = load_workbook(path, read_only=True, data_only=True)
    sheet_keys = {
        "sites": "site_code",
        "hosts": "host_name",
        "network_links": "link_code",
        "services": "service_code",
        "user_groups": "group_code",
        "service_dependencies": "dependency_id",
    }
    for sheet_name, key_field in sheet_keys.items():
        if sheet_name not in workbook.sheetnames:
            continue
        worksheet = workbook[sheet_name]
        rows = list(worksheet.iter_rows(values_only=True))
        if not rows:
            continue
        headers = [normalize_header(value) for value in rows[0]]
        for values in rows[1:]:
            if _is_blank_row(values):
                continue
            row = _row_dict(headers, values)
            if clean_text(row.get("review_status")).upper() != "CONFIRMED":
                result["unconfirmed_rows"] += 1
                continue
            key = clean_text(row.get(key_field))
            if key:
                result[sheet_name][key] = {
                    header: clean_text(value) for header, value in row.items()
                }
    workbook.close()
    return result


def build_validation_report(
    source_profile: dict[str, int],
    warnings: list[str],
    known_checks: list[dict[str, Any]],
) -> dict[str, Any]:
    invariant_specs = [
        (
            "incident row reconciliation",
            source_profile.get("incident_form_rows", 0),
            source_profile.get("normalized_incidents", 0)
            + source_profile.get("rejected_incident_rows", 0),
        ),
        (
            "zabbix row reconciliation",
            source_profile.get("zabbix_rows", 0),
            source_profile.get("normalized_alert_rows", 0)
            + source_profile.get("rejected_alert_rows", 0)
            + source_profile.get("duplicate_alert_rows", 0),
        ),
        (
            "issue comment reconciliation",
            source_profile.get("issue_comment_rows", 0),
            source_profile.get("aggregated_ticket_comment_count", 0)
            + source_profile.get("rejected_comment_rows", 0),
        ),
    ]
    invariants = [
        {"name": name, "input_rows": input_rows, "accounted_rows": accounted_rows, "passed": input_rows == accounted_rows}
        for name, input_rows, accounted_rows in invariant_specs
    ]
    required_checks_passed = all(
        check.get("passed", False) for check in known_checks if check.get("required", True)
    )
    status = (
        "PASS"
        if all(invariant["passed"] for invariant in invariants) and required_checks_passed
        else "FAIL"
    )
    return {
        "status": status,
        "upload_allowed": status == "PASS",
        "source_profile": source_profile,
        "invariants": invariants,
        "known_checks": known_checks,
        "warnings": sorted(set(warnings)),
    }


def _known_sample_checks(
    source_profile: dict[str, int], recurrence: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    if (
        source_profile.get("normalized_incidents") != 52
        or source_profile.get("normalized_alert_rows") != 1000
        or source_profile.get("normalized_tickets") != 923
    ):
        return []
    by_key = {
        (pattern["site_code"], pattern["isp"], pattern["incident_type"]): pattern[
            "incident_count"
        ]
        for pattern in recurrence
    }
    expected = [
        (("MS2", "VNPT", "High latency"), 16),
        (("XAS", "CMC", "Fiber optic cable failure"), 4),
    ]
    return [
        {
            "name": "sample recurrence " + " | ".join(key),
            "expected": count,
            "actual": by_key.get(key, 0),
            "passed": by_key.get(key, 0) == count,
            "required": True,
        }
        for key, count in expected
    ]


def _write_json(path: Path, payload: Any):
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _escape_markdown(value: Any) -> str:
    return clean_multiline_text(value).replace("\n", "  \n")


def _render_validation_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Validation Report",
        "",
        f"**Status:** `{report['status']}`",
        "",
        f"**Upload allowed:** `{'YES' if report['upload_allowed'] else 'NO'}`",
        "",
        "## Reconciliation Invariants",
        "",
    ]
    for invariant in report["invariants"]:
        state = "PASS" if invariant["passed"] else "FAIL"
        lines.append(
            f"- `{state}` {invariant['name']}: input={invariant['input_rows']}, accounted={invariant['accounted_rows']}"
        )
    lines.extend(["", "## Known Checks", ""])
    if report["known_checks"]:
        for check in report["known_checks"]:
            state = "PASS" if check["passed"] else "FAIL"
            lines.append(
                f"- `{state}` {check['name']}: expected={check['expected']}, actual={check['actual']}"
            )
    else:
        lines.append("- No supplied-sample checks were applied.")
    lines.extend(["", "## Warnings", ""])
    if report["warnings"]:
        lines.extend(f"- {warning}" for warning in report["warnings"])
    else:
        lines.append("- None.")
    lines.append("")
    return "\n".join(lines)


def _render_context(profile: dict[str, int], warnings: list[str]) -> str:
    warning_lines = "\n".join(f"- {warning}" for warning in warnings) or "- None."
    return f"""# IT Operations Report Context

## Rules for Alpha Intelligence

- Raw alerts are evidence, not confirmed incidents.
- Use statistics exactly as provided in this package. Do not count retrieved fragments.
- Distinguish `SOURCE FACT`, `COMPUTED FACT`, `ESTIMATED`, `AI INFERENCE`, and `UNKNOWN`.
- Cite record IDs and source references.
- Never invent RCA, affected users, resolution status, or preventive actions.
- Start date-range investigations with `02_operational_timeline.md`.
- Treat timeline correlation as context, not proof of RCA or user impact.
- Distinguish responsibility domains: `INHOUSE`, `ISP`, `EXTERNAL`, and `UNKNOWN`.

## Source Profile

- Confirmed incidents: `{profile['normalized_incidents']}`
- Raw Zabbix alerts: `{profile['normalized_alert_rows']}`
- Operational stories: `{profile['operational_timeline_events']}`
- Unique tickets: `{profile['normalized_tickets']}`
- Issue-report comment rows: `{profile['aggregated_ticket_comment_count']}`
- Confirmed incident period: `{profile['incident_period_start']}` to `{profile['incident_period_end']}`
- Raw alert period: `{profile['alert_period_start']}` to `{profile['alert_period_end']}`
- Ticket evidence period: `{profile['ticket_period_start']}` to `{profile['ticket_period_end']}`

## Data Quality Warnings

{warning_lines}
"""


def _render_executive_summary(
    profile: dict[str, int], recurrence: list[dict[str, Any]], alerts: list[dict[str, Any]]
) -> str:
    lines = [
        "# Executive Summary",
        "",
        "## Deterministic KPIs",
        "",
        f"- Confirmed incidents: `{profile['normalized_incidents']}`",
        f"- Raw Zabbix alerts before grouping: `{profile['normalized_alert_rows']}`",
        f"- Alert patterns after grouping: `{len(alerts)}`",
        f"- Operational stories: `{profile['operational_timeline_events']}`",
        f"- Unique tickets: `{profile['normalized_tickets']}`",
        f"- Issue-report comment rows: `{profile['aggregated_ticket_comment_count']}`",
        "",
        "## Operational Story Coverage",
        "",
        f"- Confirmed-incident stories: `{profile['timeline_confirmed_incident_events']}`",
        f"- Monitoring-signal stories: `{profile['timeline_zabbix_pattern_events']}`",
        f"- Signals related to confirmed incidents: `{profile['signal_assessment_related_to_incident']}`",
        f"- Signals with direct user-impact evidence: `{profile['signal_assessment_user_impact']}`",
        f"- Signals needing noise or threshold review: `{profile['signal_assessment_noise_review']}`",
        f"- Unconfirmed monitoring signals: `{profile['signal_assessment_unconfirmed']}`",
        "",
        "## Confirmed Incident Responsibility Classification",
        "",
        f"- `ISP`: `{profile['responsibility_incidents_isp']}`",
        f"- `INHOUSE`: `{profile['responsibility_incidents_inhouse']}`",
        f"- `EXTERNAL`: `{profile['responsibility_incidents_external']}`",
        f"- `UNKNOWN`: `{profile['responsibility_incidents_unknown']}`",
        "",
        "## Confirmed Incident User-Impact Evidence",
        "",
        f"- `CONFIRMED`: `{profile['user_impact_incidents_confirmed']}`",
        f"- `ESTIMATED`: `{profile['user_impact_incidents_estimated']}`",
        f"- `NO_EVIDENCE`: `{profile['user_impact_incidents_no_evidence']}`",
        "",
        "## Top Incident Recurrence Patterns",
        "",
    ]
    for pattern in recurrence[:20]:
        lines.append(
            f"- `{pattern['recurrence_id']}` {pattern['site_code']} | {pattern['isp']} | {pattern['incident_type']}: `{pattern['incident_count']}` confirmed incidents"
        )
    lines.extend(["", "## High-Volume Alert Patterns", ""])
    for pattern in alerts[:20]:
        lines.append(
            f"- `{pattern['alert_pattern_id']}` {pattern['host']} | {pattern['problem_signature']}: `{pattern['alert_count']}` raw alerts"
        )
    lines.append("")
    return "\n".join(lines)


def _render_operational_timeline(stories: list[dict[str, Any]]) -> str:
    lines = [
        "# Operational Timeline",
        "",
        "> Primary date-range investigation stories. A monitoring signal remains evidence, not a confirmed incident.",
        "",
        "## How To Use This Timeline",
        "",
        "- Filter by the requested time range first.",
        "- Read `CONFIRMED_INCIDENT` and `MONITORING_SIGNAL` as different episode types.",
        "- Treat responsibility domain as a computed RCA classification.",
        "- Treat correlated evidence as investigation context, not proof of RCA or user impact.",
        "",
    ]
    for story in stories:
        lines.extend(
            [
                f"## {story['episode_id']} | {story['started_at']} | {story['episode_type']}",
                "",
                f"**{_escape_markdown(story['headline'])}**",
                "",
                "### Timeline",
                "",
            ]
        )
        lines.extend(
            f"- `{milestone['at']}` {milestone['message']}"
            for milestone in story["milestones"]
        )
        lines.extend(
            [
                "",
                "### Conclusion",
                "",
                f"- Episode type: `{story['episode_type']}`",
                f"- Signal assessment: `{story['signal_assessment']}`",
                f"- User impact: `{story['user_impact_status']}`",
                f"- Responsibility domain: `{story['responsibility_domain']}`",
                f"- Responsibility basis: {_escape_markdown(story['responsibility_basis'])}",
                f"- Confirmed RCA: {_escape_markdown(story['confirmed_rca'])}",
                f"- Resolution status: `{story['resolution_status']}`",
                f"- Recurrence: {_escape_markdown(story['recurrence_summary'])}",
                f"- Evidence coverage: `{story['evidence_coverage']}`",
                "",
                "### Investigation gaps",
                "",
            ]
        )
        lines.extend(f"- {gap}" for gap in story["investigation_gaps"])
        lines.extend(
            [
                "",
                "### Evidence",
                "",
                f"- Evidence label: `{story['evidence_label']}`",
                f"- Related incident IDs: `{', '.join(story['related_incident_ids']) or 'NONE'}`",
                f"- Related alert pattern IDs: `{', '.join(story['related_alert_pattern_ids']) or 'NONE'}`",
                f"- Related ticket IDs: `{', '.join(story['related_ticket_ids']) or 'NONE'}`",
                f"- Source references: `{'; '.join(story['source_refs'][:20])}`",
                f"- Source reference count: `{len(story['source_refs'])}`",
                "",
            ]
        )
    return "\n".join(lines)


def _render_incidents(incidents: list[dict[str, Any]]) -> str:
    lines = ["# Confirmed Incidents", ""]
    for record in incidents:
        lines.extend(
            [
                f"## {record['incident_id']} | {record['site_code']} | {record['incident_type']}",
                "",
                f"- Evidence label: `{record['evidence_label']}`",
                f"- Source: `{record['source_ref']}`",
                f"- Started: `{record['started_at']}`",
                f"- Resolved: `{record['resolved_at'] or 'UNKNOWN'}`",
                f"- ISP: `{record['isp']}`",
                f"- Severity: `{record['severity']}`",
                f"- Description: {_escape_markdown(record['description'])}",
                f"- Root cause: {_escape_markdown(record['root_cause'])}",
                f"- Troubleshooting: {_escape_markdown(record['troubleshooting_actions'])}",
                f"- Preventive action: {_escape_markdown(record['preventive_action'])}",
                "",
            ]
        )
    return "\n".join(lines)


def _render_recurrence(patterns: list[dict[str, Any]]) -> str:
    lines = ["# Confirmed Incident Recurrence Patterns", ""]
    for pattern in patterns:
        lines.extend(
            [
                f"## {pattern['recurrence_id']} | {pattern['site_code']} | {pattern['isp']} | {pattern['incident_type']}",
                "",
                f"- Evidence label: `{pattern['evidence_label']}`",
                f"- Confirmed incident count: `{pattern['incident_count']}`",
                f"- First seen: `{pattern['first_seen_at']}`",
                f"- Last seen: `{pattern['last_seen_at']}`",
                f"- Incident IDs: `{', '.join(pattern['incident_ids'])}`",
                f"- Root causes: {_escape_markdown(pattern['root_causes'])}",
                f"- Source references: `{'; '.join(pattern['source_refs'])}`",
                "",
            ]
        )
    return "\n".join(lines)


def _render_alert_patterns(patterns: list[dict[str, Any]]) -> str:
    lines = ["# Raw Zabbix Alert Patterns", "", "> Alert pattern is not a confirmed incident.", ""]
    for pattern in patterns:
        refs = pattern["source_refs"]
        lines.extend(
            [
                f"## {pattern['alert_pattern_id']} | {pattern['host']}",
                "",
                f"- Evidence label: `{pattern['evidence_label']}`",
                f"- Assessment: `{pattern['assessment']}`",
                f"- Problem signature: `{pattern['problem_signature']}`",
                f"- Raw alert count: `{pattern['alert_count']}`",
                f"- Resolved alerts: `{pattern['resolved_count']}`",
                f"- Open alerts: `{pattern['open_count']}`",
                f"- Site code: `{pattern['site_code']}`",
                f"- Domain: `{pattern['domain']}`",
                f"- Component: `{pattern['component']}`",
                f"- Source references: `{'; '.join(refs[:20])}`",
                f"- Source reference count: `{len(refs)}`",
                "",
            ]
        )
    return "\n".join(lines)


def _render_ticket_impact(tickets: list[dict[str, Any]]) -> str:
    lines = ["# Ticket Impact Evidence", "", "> Tickets provide direct user evidence but are not automatically incidents.", ""]
    for ticket in tickets:
        lines.extend(
            [
                f"## TKT-{ticket['ticket_id']}",
                "",
                f"- Evidence label: `{ticket['evidence_label']}`",
                f"- Ticket ID: `{ticket['ticket_id']}`",
                f"- Title: {_escape_markdown(ticket['title'])}",
                f"- Classification: `{ticket['classification']}`",
                f"- Business unit: `{ticket['business_unit']}`",
                f"- Department: `{ticket['department']}`",
                f"- User: `{ticket['user_name']}`",
                f"- Email: `{ticket['user_email']}`",
                f"- Comment count: `{ticket['comment_count']}`",
                f"- Comment summary: {_escape_markdown(ticket['comments_summary'])}",
                f"- Source references: `{'; '.join(ticket['source_refs'])}`",
                "",
            ]
        )
    return "\n".join(lines)


def _render_data_quality(
    incidents: list[dict[str, Any]],
    master_data: dict[str, Any],
    rejected_rows: list[dict[str, Any]],
    warnings: list[str],
) -> str:
    missing_rca = sum(record["root_cause"] == "UNKNOWN" for record in incidents)
    missing_preventive = sum(record["preventive_action"] == "UNKNOWN" for record in incidents)
    lines = [
        "# Data Quality",
        "",
        "## Coverage",
        "",
        f"- Incidents missing RCA: `{missing_rca}`",
        f"- Incidents missing preventive action: `{missing_preventive}`",
        f"- Confirmed master-data sites: `{len(master_data['sites'])}`",
        f"- Confirmed master-data hosts: `{len(master_data['hosts'])}`",
        f"- Unconfirmed master-data rows ignored as facts: `{master_data['unconfirmed_rows']}`",
        f"- Rejected source rows: `{len(rejected_rows)}`",
        "",
        "## Limitations",
        "",
        "- User and dependency impact is `UNKNOWN` unless supported by direct ticket evidence or confirmed master data.",
        "- Raw alerts are not confirmed incidents.",
        "",
        "## Warnings",
        "",
    ]
    lines.extend(f"- {warning}" for warning in warnings)
    if not warnings:
        lines.append("- None.")
    lines.extend(["", "## Rejected Rows", ""])
    lines.extend(
        f"- `{rejected['source_ref']}`: {rejected['reason']}" for rejected in rejected_rows
    )
    if not rejected_rows:
        lines.append("- None.")
    lines.append("")
    return "\n".join(lines)


def _excel_scalar(value: Any) -> Any:
    if isinstance(value, (list, dict)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return value


def _append_sheet(workbook: Workbook, name: str, records: list[dict[str, Any]]):
    worksheet = workbook.create_sheet(name)
    if not records:
        worksheet.append(["status"])
        worksheet.append(["NO RECORDS"])
        return
    headers: list[str] = []
    for record in records:
        for key in record:
            if key not in headers:
                headers.append(key)
    worksheet.append(headers)
    for record in records:
        worksheet.append([_excel_scalar(record.get(header, "")) for header in headers])
    worksheet.freeze_panes = "A2"
    worksheet.auto_filter.ref = worksheet.dimensions


def _write_audit_workbook(
    path: Path,
    timeline: list[dict[str, Any]],
    incidents: list[dict[str, Any]],
    alerts: list[dict[str, Any]],
    tickets: list[dict[str, Any]],
    recurrence: list[dict[str, Any]],
    data_quality: list[dict[str, Any]],
    source_profile: dict[str, Any],
):
    workbook = Workbook()
    workbook.remove(workbook.active)
    _append_sheet(workbook, "operational_timeline", timeline)
    _append_sheet(workbook, "confirmed_incidents", incidents)
    _append_sheet(workbook, "alert_patterns", alerts)
    _append_sheet(workbook, "ticket_evidence", tickets)
    _append_sheet(workbook, "recurrence_patterns", recurrence)
    _append_sheet(workbook, "data_quality", data_quality)
    _append_sheet(
        workbook,
        "source_profile",
        [{"metric": key, "value": value} for key, value in sorted(source_profile.items())],
    )
    workbook.save(path)


def build_knowledge_package(
    raw_dir: Path,
    master_data_path: Path | None,
    output_dir: Path,
    generated_at: str | None = None,
) -> dict[str, Any]:
    raw_dir = Path(raw_dir)
    output_dir = Path(output_dir)
    generated_at = generated_at or datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    issue_path = raw_dir / ISSUE_REPORT_FILENAME
    incident_path = raw_dir / INCIDENT_REPORT_FILENAME
    zabbix_file_path = raw_dir / ZABBIX_FILENAME
    zabbix_export_dir = raw_dir / ZABBIX_EXPORT_DIRNAME
    zabbix_path = zabbix_export_dir if zabbix_export_dir.exists() else zabbix_file_path
    inputs = [issue_path, incident_path, zabbix_path]
    for input_path in inputs:
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")
        if input_path.is_dir() and not any(input_path.glob("*.csv")):
            raise FileNotFoundError(f"No CSV files found in input directory: {input_path}")
    if master_data_path is not None:
        master_data_path = Path(master_data_path)
        if not master_data_path.exists():
            raise FileNotFoundError(
                f"Explicit master-data input file not found: {master_data_path}"
            )

    incidents = load_incidents(incident_path)
    alerts = load_zabbix_alerts(zabbix_path)
    tickets = load_issue_tickets(issue_path)
    master_data = load_confirmed_master_data(master_data_path)
    recurrence = group_incident_recurrence(incidents.records)
    alert_patterns = group_alert_patterns(alerts.records)
    operational_stories = build_operational_stories(
        incidents.records, alert_patterns, tickets.records, recurrence, alerts=alerts.records
    )
    incident_stories = [
        story
        for story in operational_stories
        if story["episode_type"] == "CONFIRMED_INCIDENT"
    ]
    monitoring_stories = [
        story
        for story in operational_stories
        if story["episode_type"] == "MONITORING_SIGNAL"
    ]

    rejected_rows = incidents.rejected_rows + alerts.rejected_rows + tickets.rejected_rows
    unmapped_incident_sites = sorted(
        {
            record["site_code"]
            for record in incidents.records
            if record["site_code"] not in master_data["sites"]
        }
    )
    unmapped_alert_hosts = sorted(
        {
            pattern["host"]
            for pattern in alert_patterns
            if pattern["host"] not in master_data["hosts"]
        }
    )
    warnings = [
        f"Rejected source rows: {len(rejected_rows)}" if rejected_rows else "",
        f"Duplicate Zabbix rows ignored after multi-export merge: {alerts.duplicate_rows}"
        if alerts.duplicate_rows
        else "",
        f"Unconfirmed master-data rows ignored as facts: {master_data['unconfirmed_rows']}"
        if master_data["unconfirmed_rows"]
        else "",
        f"Sites without confirmed master-data mapping: {len(unmapped_incident_sites)}"
        if unmapped_incident_sites
        else "",
        f"Alert hosts without confirmed master-data mapping: {len(unmapped_alert_hosts)}"
        if unmapped_alert_hosts
        else "",
        f"Incidents missing RCA: {sum(record['root_cause'] == 'UNKNOWN' for record in incidents.records)}",
        f"Incidents missing preventive action: {sum(record['preventive_action'] == 'UNKNOWN' for record in incidents.records)}",
        "No incident-to-Zabbix timeline correlations matched the current exports"
        if not any(story["related_alert_pattern_ids"] for story in incident_stories)
        else "",
        "No direct site-explicit ticket correlations matched confirmed incidents"
        if not any(story["related_ticket_ids"] for story in incident_stories)
        else "",
    ]
    warnings = [warning for warning in warnings if warning]
    source_profile = {
        "incident_form_rows": incidents.input_rows,
        "normalized_incidents": len(incidents.records),
        "rejected_incident_rows": len(incidents.rejected_rows),
        "zabbix_rows": alerts.input_rows,
        "normalized_alert_rows": len(alerts.records),
        "rejected_alert_rows": len(alerts.rejected_rows),
        "duplicate_alert_rows": alerts.duplicate_rows,
        "issue_comment_rows": tickets.input_rows,
        "aggregated_ticket_comment_count": sum(
            record["comment_count"] for record in tickets.records
        ),
        "rejected_comment_rows": len(tickets.rejected_rows),
        "normalized_tickets": len(tickets.records),
        "alert_patterns": len(alert_patterns),
        "recurrence_patterns": len(recurrence),
        "operational_timeline_events": len(operational_stories),
        "timeline_confirmed_incident_events": sum(
            story["episode_type"] == "CONFIRMED_INCIDENT" for story in operational_stories
        ),
        "timeline_zabbix_pattern_events": sum(
            story["episode_type"] == "MONITORING_SIGNAL" for story in operational_stories
        ),
        "signal_assessment_related_to_incident": sum(
            story["signal_assessment"] == "RELATED_TO_CONFIRMED_INCIDENT"
            for story in monitoring_stories
        ),
        "signal_assessment_user_impact": sum(
            story["signal_assessment"] == "USER_IMPACT_SIGNAL"
            for story in monitoring_stories
        ),
        "signal_assessment_noise_review": sum(
            story["signal_assessment"] == "LIKELY_NOISE_OR_THRESHOLD_REVIEW"
            for story in monitoring_stories
        ),
        "signal_assessment_unconfirmed": sum(
            story["signal_assessment"] == "UNCONFIRMED_MONITORING_SIGNAL"
            for story in monitoring_stories
        ),
        "responsibility_incidents_inhouse": sum(
            story["responsibility_domain"] == "INHOUSE" for story in incident_stories
        ),
        "responsibility_incidents_isp": sum(
            story["responsibility_domain"] == "ISP" for story in incident_stories
        ),
        "responsibility_incidents_external": sum(
            story["responsibility_domain"] == "EXTERNAL" for story in incident_stories
        ),
        "responsibility_incidents_unknown": sum(
            story["responsibility_domain"] == "UNKNOWN" for story in incident_stories
        ),
        "user_impact_incidents_confirmed": sum(
            story["user_impact_status"] == "CONFIRMED" for story in incident_stories
        ),
        "user_impact_incidents_estimated": sum(
            story["user_impact_status"] == "ESTIMATED" for story in incident_stories
        ),
        "user_impact_incidents_no_evidence": sum(
            story["user_impact_status"] == "NO_EVIDENCE" for story in incident_stories
        ),
        "incident_period_start": min(
            (record["started_at"] for record in incidents.records), default="UNKNOWN"
        ),
        "incident_period_end": max(
            (record["started_at"] for record in incidents.records), default="UNKNOWN"
        ),
        "alert_period_start": min(
            (record["seen_at"] for record in alerts.records), default="UNKNOWN"
        ),
        "alert_period_end": max(
            (record["seen_at"] for record in alerts.records), default="UNKNOWN"
        ),
        "ticket_period_start": min(
            (record["first_comment_at"] for record in tickets.records), default="UNKNOWN"
        ),
        "ticket_period_end": max(
            (record["last_comment_at"] for record in tickets.records), default="UNKNOWN"
        ),
    }
    known_checks = _known_sample_checks(source_profile, recurrence)
    report = build_validation_report(source_profile, warnings, known_checks)
    data_quality_records = [
        {"record_type": "WARNING", "message": warning} for warning in warnings
    ] + [
        {"record_type": "REJECTED_ROW", **rejected_row}
        for rejected_row in rejected_rows
    ]

    output_dir.mkdir(parents=True, exist_ok=True)
    manifest_inputs = [
        {
            "filename": path.name,
            "input_type": "master_data"
            if master_data_path is not None and path == master_data_path
            else "raw_export",
            "sha256": sha256_file(path),
        }
        for path in sorted(
            [path for path in inputs if path.is_file()]
            + ([master_data_path] if master_data_path is not None else [])
        )
    ]
    if zabbix_path.is_dir():
        manifest_inputs.extend(
            {
                "filename": f"{zabbix_path.name}/{path.name}",
                "input_type": "raw_export",
                "sha256": sha256_file(path),
            }
            for path in sorted(zabbix_path.glob("*.csv"), key=lambda item: item.name.lower())
        )
    manifest = {
        "package_version": PACKAGE_VERSION,
        "generated_at": generated_at,
        "upload_allowed": report["upload_allowed"],
        "validation_status": report["status"],
        "inputs": manifest_inputs,
        "source_profile": source_profile,
        "warnings": warnings,
    }
    _write_json(output_dir / "manifest.json", manifest)
    _write_json(output_dir / "validation_report.json", report)
    (output_dir / "validation_report.md").write_text(
        _render_validation_markdown(report), encoding="utf-8"
    )
    (output_dir / "00_report_context.md").write_text(
        _render_context(source_profile, warnings), encoding="utf-8"
    )
    (output_dir / "01_executive_summary.md").write_text(
        _render_executive_summary(source_profile, recurrence, alert_patterns),
        encoding="utf-8",
    )
    (output_dir / "02_operational_timeline.md").write_text(
        _render_operational_timeline(operational_stories), encoding="utf-8"
    )
    (output_dir / "02_confirmed_incidents.md").write_text(
        _render_incidents(incidents.records), encoding="utf-8"
    )
    (output_dir / "03_recurrence_patterns.md").write_text(
        _render_recurrence(recurrence), encoding="utf-8"
    )
    (output_dir / "04_alert_patterns.md").write_text(
        _render_alert_patterns(alert_patterns), encoding="utf-8"
    )
    (output_dir / "05_ticket_impact.md").write_text(
        _render_ticket_impact(tickets.records), encoding="utf-8"
    )
    (output_dir / "06_data_quality.md").write_text(
        _render_data_quality(incidents.records, master_data, rejected_rows, warnings),
        encoding="utf-8",
    )
    _write_audit_workbook(
        output_dir / "normalized_data.xlsx",
        operational_stories,
        incidents.records,
        alert_patterns,
        tickets.records,
        recurrence,
        data_quality_records,
        source_profile,
    )
    return {
        "output_dir": str(output_dir),
        "upload_allowed": report["upload_allowed"],
        "validation_status": report["status"],
        "source_profile": source_profile,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build an Alpha Intelligence IT Operations knowledge package."
    )
    parser.add_argument("--raw-dir", type=Path, required=True, help="Directory containing the three raw Excel exports.")
    parser.add_argument("--master-data", type=Path, help="Optional reviewed master-data workbook.")
    parser.add_argument("--output-dir", type=Path, required=True, help="Directory for the generated Alpha-ready package.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    package = build_knowledge_package(args.raw_dir, args.master_data, args.output_dir)
    print(json.dumps(package, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if package["upload_allowed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
