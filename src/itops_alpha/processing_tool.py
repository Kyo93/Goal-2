from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .converter import (
    MARKDOWN_FILENAMES,
    PACKAGE_VERSION,
    build_operational_timeline_payload,
    build_operational_stories,
    build_validation_report,
    group_alert_patterns,
    group_incident_recurrence,
    load_confirmed_master_data,
    load_incidents,
    load_issue_tickets,
    load_zabbix_alerts,
    query_operational_timeline,
    sha256_file,
    _known_sample_checks,
    _render_alert_patterns,
    _render_context,
    _render_data_quality,
    _render_executive_summary,
    _render_incidents,
    _render_operational_query_result,
    _render_operational_timeline,
    _render_recurrence,
    _render_ticket_impact,
    _render_validation_markdown,
    _write_audit_workbook,
    _write_json,
)


PROCESSED_INCIDENTS = "confirmed_incidents.json"
PROCESSED_ZABBIX_ALERTS = "zabbix_alerts.json"
PROCESSED_ALERT_PATTERNS = "alert_patterns.json"
PROCESSED_TICKETS = "ticket_evidence.json"
OPERATIONAL_TIMELINE_JSON = "operational_timeline.json"


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _write_processed_payload(
    output_dir: Path,
    filename: str,
    source_type: str,
    source_path: Path,
    records: list[dict[str, Any]],
    input_rows: int,
    rejected_rows: list[dict[str, Any]],
    skipped_blank_rows: int,
    duplicate_rows: int = 0,
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": "1.0",
        "source_type": source_type,
        "source_path": str(source_path),
        "source_name": source_path.name,
        "source_sha256": sha256_file(source_path) if source_path.is_file() else "",
        "generated_at": _utc_now(),
        "input_rows": input_rows,
        "record_count": len(records),
        "rejected_rows": rejected_rows,
        "rejected_row_count": len(rejected_rows),
        "skipped_blank_rows": skipped_blank_rows,
        "duplicate_rows": duplicate_rows,
        "records": records,
    }
    if extra:
        payload.update(extra)
    _write_json(output_dir / filename, payload)
    return {
        "ok": True,
        "source_type": source_type,
        "output_file": str(output_dir / filename),
        "input_rows": input_rows,
        "record_count": len(records),
        "rejected_row_count": len(rejected_rows),
        "duplicate_rows": duplicate_rows,
    }


def process_incident_source(incident_report_file: Path, output_dir: Path) -> dict[str, Any]:
    result = load_incidents(Path(incident_report_file))
    return _write_processed_payload(
        Path(output_dir),
        PROCESSED_INCIDENTS,
        "incident_report",
        Path(incident_report_file),
        result.records,
        result.input_rows,
        result.rejected_rows,
        result.skipped_blank_rows,
    )


def process_zabbix_source(zabbix_export: Path, output_dir: Path) -> dict[str, Any]:
    result = load_zabbix_alerts(Path(zabbix_export))
    patterns = group_alert_patterns(result.records)
    output_dir = Path(output_dir)
    alert_result = _write_processed_payload(
        output_dir,
        PROCESSED_ZABBIX_ALERTS,
        "zabbix_export",
        Path(zabbix_export),
        result.records,
        result.input_rows,
        result.rejected_rows,
        result.skipped_blank_rows,
        result.duplicate_rows,
    )
    _write_processed_payload(
        output_dir,
        PROCESSED_ALERT_PATTERNS,
        "zabbix_alert_patterns",
        Path(zabbix_export),
        patterns,
        result.input_rows,
        [],
        result.skipped_blank_rows,
        result.duplicate_rows,
        extra={"source_alert_file": PROCESSED_ZABBIX_ALERTS},
    )
    alert_result["pattern_file"] = str(output_dir / PROCESSED_ALERT_PATTERNS)
    alert_result["pattern_count"] = len(patterns)
    return alert_result


def process_ticket_source(issue_report_file: Path, output_dir: Path) -> dict[str, Any]:
    result = load_issue_tickets(Path(issue_report_file))
    return _write_processed_payload(
        Path(output_dir),
        PROCESSED_TICKETS,
        "issue_report",
        Path(issue_report_file),
        result.records,
        result.input_rows,
        result.rejected_rows,
        result.skipped_blank_rows,
    )


def _read_processed(processed_dir: Path, filename: str) -> dict[str, Any]:
    path = processed_dir / filename
    if not path.exists():
        raise FileNotFoundError(f"Processed source file not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def query_timeline_file(
    timeline_file: Path,
    site_code: str,
    from_at: str,
    to_at: str,
) -> dict[str, Any]:
    payload = json.loads(Path(timeline_file).read_text(encoding="utf-8"))
    records = payload["records"] if isinstance(payload, dict) else payload
    result = query_operational_timeline(records, site_code, from_at, to_at)
    result["source_file"] = str(timeline_file)
    result["markdown"] = _render_operational_query_result(result)
    return result


def _build_source_profile(
    incidents_payload: dict[str, Any],
    alerts_payload: dict[str, Any],
    patterns: list[dict[str, Any]],
    tickets_payload: dict[str, Any],
    recurrence: list[dict[str, Any]],
    operational_stories: list[dict[str, Any]],
) -> dict[str, Any]:
    incidents = incidents_payload["records"]
    alerts = alerts_payload["records"]
    tickets = tickets_payload["records"]
    incident_stories = [
        story for story in operational_stories if story["episode_type"] == "CONFIRMED_INCIDENT"
    ]
    monitoring_stories = [
        story for story in operational_stories if story["episode_type"] == "MONITORING_SIGNAL"
    ]
    return {
        "incident_form_rows": incidents_payload["input_rows"],
        "normalized_incidents": len(incidents),
        "rejected_incident_rows": incidents_payload["rejected_row_count"],
        "zabbix_rows": alerts_payload["input_rows"],
        "normalized_alert_rows": len(alerts),
        "rejected_alert_rows": alerts_payload["rejected_row_count"],
        "duplicate_alert_rows": alerts_payload.get("duplicate_rows", 0),
        "issue_comment_rows": tickets_payload["input_rows"],
        "aggregated_ticket_comment_count": sum(
            record["comment_count"] for record in tickets
        ),
        "rejected_comment_rows": tickets_payload["rejected_row_count"],
        "normalized_tickets": len(tickets),
        "alert_patterns": len(patterns),
        "recurrence_patterns": len(recurrence),
        "operational_timeline_events": len(operational_stories),
        "timeline_confirmed_incident_events": len(incident_stories),
        "timeline_zabbix_pattern_events": len(monitoring_stories),
        "signal_assessment_related_to_incident": sum(
            story["signal_assessment"] == "RELATED_TO_CONFIRMED_INCIDENT"
            for story in monitoring_stories
        ),
        "signal_assessment_context_only": sum(
            story["signal_assessment"] == "TIME_ALIGNED_CONTEXT_ONLY"
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
        "user_impact_incidents_potential_impact": sum(
            story["user_impact_status"] == "POTENTIAL_IMPACT" for story in incident_stories
        ),
        "user_impact_incidents_no_direct_evidence": sum(
            story["user_impact_status"] == "NO_DIRECT_EVIDENCE" for story in incident_stories
        ),
        "incident_period_start": min(
            (record["started_at"] for record in incidents), default="UNKNOWN"
        ),
        "incident_period_end": max(
            (record["started_at"] for record in incidents), default="UNKNOWN"
        ),
        "alert_period_start": min(
            (record["seen_at"] for record in alerts), default="UNKNOWN"
        ),
        "alert_period_end": max(
            (record["seen_at"] for record in alerts), default="UNKNOWN"
        ),
        "ticket_period_start": min(
            (record["first_comment_at"] for record in tickets), default="UNKNOWN"
        ),
        "ticket_period_end": max(
            (record["last_comment_at"] for record in tickets), default="UNKNOWN"
        ),
    }


def _build_warnings(
    incidents: list[dict[str, Any]],
    patterns: list[dict[str, Any]],
    master_data: dict[str, Any],
    rejected_rows: list[dict[str, Any]],
    alerts_payload: dict[str, Any],
    incident_stories: list[dict[str, Any]],
) -> list[str]:
    unmapped_incident_sites = sorted(
        {
            record["site_code"]
            for record in incidents
            if record["site_code"] not in master_data["sites"]
        }
    )
    unmapped_alert_hosts = sorted(
        {
            pattern["host"]
            for pattern in patterns
            if pattern["host"] not in master_data["hosts"]
        }
    )
    warnings = [
        f"Rejected source rows: {len(rejected_rows)}" if rejected_rows else "",
        f"Duplicate Zabbix rows ignored after multi-export merge: {alerts_payload.get('duplicate_rows', 0)}"
        if alerts_payload.get("duplicate_rows", 0)
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
        f"Incidents missing RCA: {sum(record['root_cause'] == 'UNKNOWN' for record in incidents)}",
        f"Incidents missing preventive action: {sum(record['preventive_action'] == 'UNKNOWN' for record in incidents)}",
        "No incident-to-Zabbix timeline correlations matched the current exports"
        if not any(story["related_alert_pattern_ids"] for story in incident_stories)
        else "",
        "No direct site-explicit ticket correlations matched confirmed incidents"
        if not any(story["related_ticket_ids"] for story in incident_stories)
        else "",
    ]
    return [warning for warning in warnings if warning]


def connect_processed_sources(
    processed_dir: Path,
    output_dir: Path,
    master_data_path: Path | None = None,
    generated_at: str | None = None,
) -> dict[str, Any]:
    processed_dir = Path(processed_dir)
    output_dir = Path(output_dir)
    generated_at = generated_at or _utc_now()

    incidents_payload = _read_processed(processed_dir, PROCESSED_INCIDENTS)
    alerts_payload = _read_processed(processed_dir, PROCESSED_ZABBIX_ALERTS)
    patterns_payload = _read_processed(processed_dir, PROCESSED_ALERT_PATTERNS)
    tickets_payload = _read_processed(processed_dir, PROCESSED_TICKETS)

    incidents = incidents_payload["records"]
    alerts = alerts_payload["records"]
    alert_patterns = patterns_payload["records"]
    tickets = tickets_payload["records"]
    master_data = load_confirmed_master_data(Path(master_data_path) if master_data_path else None)
    recurrence = group_incident_recurrence(incidents)
    operational_stories = build_operational_stories(
        incidents, alert_patterns, tickets, recurrence, alerts=alerts
    )
    incident_stories = [
        story for story in operational_stories if story["episode_type"] == "CONFIRMED_INCIDENT"
    ]
    rejected_rows = (
        incidents_payload["rejected_rows"]
        + alerts_payload["rejected_rows"]
        + tickets_payload["rejected_rows"]
    )
    warnings = _build_warnings(
        incidents, alert_patterns, master_data, rejected_rows, alerts_payload, incident_stories
    )
    source_profile = _build_source_profile(
        incidents_payload,
        alerts_payload,
        alert_patterns,
        tickets_payload,
        recurrence,
        operational_stories,
    )
    report = build_validation_report(
        source_profile, warnings, _known_sample_checks(source_profile, recurrence)
    )
    data_quality_records = [
        {"record_type": "WARNING", "message": warning} for warning in warnings
    ] + [{"record_type": "REJECTED_ROW", **rejected_row} for rejected_row in rejected_rows]

    output_dir.mkdir(parents=True, exist_ok=True)
    manifest_inputs = [
        {
            "filename": filename,
            "input_type": "processed_source",
            "sha256": sha256_file(processed_dir / filename),
        }
        for filename in [
            PROCESSED_INCIDENTS,
            PROCESSED_ZABBIX_ALERTS,
            PROCESSED_ALERT_PATTERNS,
            PROCESSED_TICKETS,
        ]
    ]
    if master_data_path is not None:
        manifest_inputs.append(
            {
                "filename": Path(master_data_path).name,
                "input_type": "master_data",
                "sha256": sha256_file(Path(master_data_path)),
            }
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
    _write_json(
        output_dir / OPERATIONAL_TIMELINE_JSON,
        build_operational_timeline_payload(operational_stories, generated_at=generated_at),
    )
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
        _render_incidents(incidents), encoding="utf-8"
    )
    (output_dir / "03_recurrence_patterns.md").write_text(
        _render_recurrence(recurrence), encoding="utf-8"
    )
    (output_dir / "04_alert_patterns.md").write_text(
        _render_alert_patterns(alert_patterns), encoding="utf-8"
    )
    (output_dir / "05_ticket_impact.md").write_text(
        _render_ticket_impact(tickets), encoding="utf-8"
    )
    (output_dir / "06_data_quality.md").write_text(
        _render_data_quality(incidents, master_data, rejected_rows, warnings),
        encoding="utf-8",
    )
    _write_audit_workbook(
        output_dir / "normalized_data.xlsx",
        operational_stories,
        incidents,
        alert_patterns,
        tickets,
        recurrence,
        data_quality_records,
        source_profile,
    )
    return {
        "ok": report["upload_allowed"],
        "output_dir": str(output_dir),
        "validation_status": report["status"],
        "upload_allowed": report["upload_allowed"],
        "source_profile": source_profile,
        "warnings": warnings,
        "knowledge_files": [str(output_dir / filename) for filename in MARKDOWN_FILENAMES],
        "audit_files": [
            str(output_dir / "manifest.json"),
            str(output_dir / "validation_report.json"),
            str(output_dir / "validation_report.md"),
            str(output_dir / OPERATIONAL_TIMELINE_JSON),
            str(output_dir / "normalized_data.xlsx"),
        ],
    }


def run_full_processing(
    incident_report_file: Path,
    zabbix_export: Path,
    issue_report_file: Path,
    processed_dir: Path,
    output_dir: Path,
    master_data_path: Path | None = None,
    generated_at: str | None = None,
) -> dict[str, Any]:
    process_incident_source(incident_report_file, processed_dir)
    process_zabbix_source(zabbix_export, processed_dir)
    process_ticket_source(issue_report_file, processed_dir)
    return connect_processed_sources(
        processed_dir, output_dir, master_data_path=master_data_path, generated_at=generated_at
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run Alpha-callable IT Operations source processors and connector."
    )
    subparsers = parser.add_subparsers(dest="stage", required=True)

    incident = subparsers.add_parser("incident", help="Process the incident report source.")
    incident.add_argument("--incident-report-file", type=Path, required=True)
    incident.add_argument("--processed-dir", type=Path, required=True)

    zabbix = subparsers.add_parser("zabbix", help="Process the Zabbix export source.")
    zabbix.add_argument("--zabbix-export", type=Path, required=True)
    zabbix.add_argument("--processed-dir", type=Path, required=True)

    ticket = subparsers.add_parser("ticket", help="Process the issue ticket source.")
    ticket.add_argument("--issue-report-file", type=Path, required=True)
    ticket.add_argument("--processed-dir", type=Path, required=True)

    connect = subparsers.add_parser("connect", help="Connect processed sources into a package.")
    connect.add_argument("--processed-dir", type=Path, required=True)
    connect.add_argument("--output-dir", type=Path, required=True)
    connect.add_argument("--master-data", type=Path)
    connect.add_argument("--generated-at")

    query = subparsers.add_parser(
        "query-timeline",
        help="Query operational timeline events by site and time range.",
    )
    query.add_argument("--timeline-file", type=Path, required=True)
    query.add_argument("--site-code", required=True)
    query.add_argument("--from-at", required=True)
    query.add_argument("--to-at", required=True)

    full = subparsers.add_parser("full", help="Run all processors and connector.")
    full.add_argument("--incident-report-file", type=Path, required=True)
    full.add_argument("--zabbix-export", type=Path, required=True)
    full.add_argument("--issue-report-file", type=Path, required=True)
    full.add_argument("--processed-dir", type=Path, required=True)
    full.add_argument("--output-dir", type=Path, required=True)
    full.add_argument("--master-data", type=Path)
    full.add_argument("--generated-at")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.stage == "incident":
            result = process_incident_source(args.incident_report_file, args.processed_dir)
        elif args.stage == "zabbix":
            result = process_zabbix_source(args.zabbix_export, args.processed_dir)
        elif args.stage == "ticket":
            result = process_ticket_source(args.issue_report_file, args.processed_dir)
        elif args.stage == "connect":
            result = connect_processed_sources(
                args.processed_dir,
                args.output_dir,
                master_data_path=args.master_data,
                generated_at=args.generated_at,
            )
        elif args.stage == "query-timeline":
            result = query_timeline_file(
                args.timeline_file,
                args.site_code,
                args.from_at,
                args.to_at,
            )
        else:
            result = run_full_processing(
                args.incident_report_file,
                args.zabbix_export,
                args.issue_report_file,
                args.processed_dir,
                args.output_dir,
                master_data_path=args.master_data,
                generated_at=args.generated_at,
            )
    except Exception as error:  # noqa: BLE001 - CLI must return structured tool errors.
        result = {"ok": False, "error": type(error).__name__, "error_message": str(error)}
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result.get("ok") else 2


if __name__ == "__main__":
    raise SystemExit(main())
