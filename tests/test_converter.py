import json
import sys
import tempfile
import unittest
from pathlib import Path

from openpyxl import load_workbook


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
FIXTURES = ROOT / "tests" / "fixtures"
sys.path.insert(0, str(SRC))

from itops_alpha.converter import (  # noqa: E402
    build_operational_timeline,
    build_operational_stories,
    build_knowledge_package,
    build_validation_report,
    classify_responsibility_domain,
    group_alert_patterns,
    group_incident_recurrence,
    load_confirmed_master_data,
    load_incidents,
    load_issue_tickets,
    load_zabbix_alerts,
    normalize_problem_signature,
    source_ref,
)


class ConverterTest(unittest.TestCase):
    def test_source_ref_is_stable_and_human_readable(self):
        self.assertEqual(
            source_ref("IssueReport.xlsx", "Issue Export", 2),
            "IssueReport.xlsx#Issue Export:row-2",
        )

    def test_incident_adapter_reads_main_sheet_only_and_rejects_invalid_timestamp(self):
        result = load_incidents(
            FIXTURES / "SEA - Corp IT- ILL- Incident Report   (Responses).xlsx"
        )
        self.assertEqual(result.input_rows, 4)
        self.assertEqual(len(result.records), 3)
        self.assertEqual(len(result.rejected_rows), 1)
        self.assertIn("not-a-date", result.rejected_rows[0]["reason"])
        self.assertEqual(result.records[0]["incident_id"], "INC-3")
        self.assertIn("#Form Responses 1:row-3", result.records[0]["source_ref"])

    def test_issue_adapter_aggregates_comments_by_ticket_without_losing_count(self):
        result = load_issue_tickets(FIXTURES / "IssueReport.xlsx")
        self.assertEqual(result.input_rows, 3)
        self.assertEqual(len(result.records), 2)
        self.assertEqual(sum(record["comment_count"] for record in result.records), 3)
        ticket = next(record for record in result.records if record["ticket_id"] == "TKT-100")
        self.assertEqual(ticket["comment_count"], 2)
        self.assertEqual(len(ticket["source_refs"]), 2)

    def test_zabbix_adapter_groups_metric_variants_but_preserves_raw_count(self):
        result = load_zabbix_alerts(FIXTURES / "zbx_problems_export.xlsx")
        self.assertEqual(result.input_rows, 6)
        self.assertEqual(len(result.records), 5)
        self.assertEqual(len(result.rejected_rows), 1)
        patterns = group_alert_patterns(result.records)
        self.assertEqual(len(patterns), 3)
        fpt = next(pattern for pattern in patterns if pattern["host"] == "VNMCCW-PNWSW01")
        self.assertEqual(fpt["alert_count"], 2)
        self.assertIn("<value>", fpt["problem_signature"])

    def test_zabbix_adapter_reads_multi_csv_exports_and_deduplicates_overlap(self):
        with tempfile.TemporaryDirectory() as temporary:
            export_dir = Path(temporary) / "Export zabbix"
            export_dir.mkdir()
            header = '"Severity","Time","Recovery time","Status","Host","Problem","Duration","Ack","Actions","Tags"\n'
            duplicate = '"High","2026-06-03 03:11:37 PM","2026-06-03 03:12:07 PM","RESOLVED","VNMMS2-FPT-FMS-45.119.218.130","Unavailable by ICMP ping","30s","No","Actions (2)","Application: Status"\n'
            unique = '"Warning","2026-06-03 03:10:37 PM","2026-06-03 03:10:52 PM","RESOLVED","VNMMSB-FPT-FMS-45.119.218.130","High ICMP ping loss","15s","No","Actions (2)","Application: Status"\n'
            (export_dir / "part-a.csv").write_text(header + duplicate, encoding="utf-8")
            (export_dir / "part-b.csv").write_text(header + duplicate + unique, encoding="utf-8")

            result = load_zabbix_alerts(export_dir)

        self.assertEqual(result.input_rows, 3)
        self.assertEqual(len(result.records), 2)
        self.assertEqual(result.duplicate_rows, 1)
        self.assertEqual(len(result.rejected_rows), 0)
        self.assertEqual(result.records[0]["seen_at"], "2026-06-03T15:11:37")
        self.assertIn("part-a.csv#csv:row-2", result.records[0]["source_ref"])

    def test_problem_signature_replaces_dynamic_values(self):
        signature = normalize_problem_signature(
            "FPT Download Gi2/0/3>100M,Current:115.17 Mbps"
        )
        self.assertEqual(
            signature,
            "fpt download gi2/0/3><value>,current:<value> mbps",
        )

    def test_master_data_uses_confirmed_rows_only(self):
        data = load_confirmed_master_data(FIXTURES / "master_data.xlsx")
        self.assertEqual(set(data["sites"]), {"CCW"})
        self.assertEqual(set(data["hosts"]), {"VNMCCW-PNWSW01"})
        self.assertEqual(data["unconfirmed_rows"], 2)

    def test_incident_recurrence_is_deterministic(self):
        incidents = load_incidents(
            FIXTURES / "SEA - Corp IT- ILL- Incident Report   (Responses).xlsx"
        ).records
        recurrence = group_incident_recurrence(incidents)
        ms2 = next(pattern for pattern in recurrence if pattern["site_code"] == "MS2")
        self.assertEqual(ms2["incident_count"], 2)
        self.assertTrue(ms2["recurrence_id"].startswith("REC-"))

    def test_responsibility_domain_classification_is_conservative_and_auditable(self):
        self.assertEqual(
            classify_responsibility_domain(
                "The issue was caused by international routing fluctuations."
            ),
            ("ISP", "RCA keyword rule: routing"),
        )
        self.assertEqual(
            classify_responsibility_domain("The issue belongs to Shopee's local segment."),
            ("INHOUSE", "RCA keyword rule: local segment"),
        )
        self.assertEqual(
            classify_responsibility_domain("UNKNOWN"),
            ("UNKNOWN", "RCA does not support responsibility classification"),
        )

    def test_operational_timeline_links_only_matching_site_and_time_windows(self):
        incidents = [
            {
                "incident_id": "INC-3",
                "source_ref": "incident.xlsx#main:row-3",
                "started_at": "2026-05-19T16:10:00",
                "resolved_at": "2026-05-19T16:40:00",
                "site_code": "CCW",
                "incident_type": "High latency",
                "description": "Users are experiencing slow access.",
                "root_cause": "FPT uplink routing issue.",
                "resolution_status": "RESOLVED",
            }
        ]
        alert_patterns = [
            {
                "alert_pattern_id": "ALP-MATCH",
                "source_refs": ["zabbix.xlsx#main:row-2"],
                "first_seen_at": "2026-05-19T16:20:00",
                "last_seen_at": "2026-05-19T16:30:00",
                "site_code": "CCW",
                "host": "VNMCCW-PNWSW01",
                "problem_signature": "high latency",
                "alert_count": 2,
            },
            {
                "alert_pattern_id": "ALP-WRONG-SITE",
                "source_refs": ["zabbix.xlsx#main:row-3"],
                "first_seen_at": "2026-05-19T16:20:00",
                "last_seen_at": "2026-05-19T16:30:00",
                "site_code": "SNT",
                "host": "VNMSNT-UPSF2201",
                "problem_signature": "power",
                "alert_count": 1,
            },
        ]
        tickets = [
            {
                "ticket_id": "TKT-100",
                "source_refs": ["IssueReport.xlsx#main:row-2"],
                "first_comment_at": "2026-05-19T16:15:00",
                "last_comment_at": "2026-05-19T16:25:00",
                "title": "CCW users cannot access service",
                "comments_summary": "CCW users report slow access.",
            },
            {
                "ticket_id": "TKT-200",
                "source_refs": ["IssueReport.xlsx#main:row-3"],
                "first_comment_at": "2026-05-19T16:15:00",
                "last_comment_at": "2026-05-19T16:25:00",
                "title": "SNT issue",
                "comments_summary": "SNT power alert.",
            },
        ]

        timeline = build_operational_timeline(incidents, alert_patterns, tickets)
        incident = next(event for event in timeline if event["event_id"] == "EVT-INC-3")
        signal = next(event for event in timeline if event["event_id"] == "EVT-ALP-MATCH")

        self.assertEqual(incident["event_type"], "CONFIRMED_INCIDENT")
        self.assertEqual(incident["related_alert_pattern_ids"], ["ALP-MATCH"])
        self.assertEqual(incident["related_ticket_ids"], ["TKT-100"])
        self.assertEqual(incident["user_impact_status"], "CONFIRMED")
        self.assertEqual(incident["responsibility_domain"], "ISP")
        self.assertEqual(signal["event_type"], "ZABBIX_ALERT_PATTERN")
        self.assertEqual(signal["related_incident_ids"], ["INC-3"])

    def test_operational_timeline_uses_event_level_alert_overlap(self):
        incidents = [
            {
                "incident_id": "INC-MDN",
                "source_ref": "incident.xlsx#main:row-10",
                "started_at": "2026-05-10T13:20:00",
                "resolved_at": "2026-05-10T17:50:00",
                "site_code": "MDN",
                "incident_type": "Others",
                "description": "Local segment issue.",
                "root_cause": "The issue belongs to Shopee's local segment.",
                "resolution_status": "RESOLVED",
            },
            {
                "incident_id": "INC-MBD",
                "source_ref": "incident.xlsx#main:row-11",
                "started_at": "2026-05-29T12:20:00",
                "resolved_at": "2026-05-30T15:48:00",
                "site_code": "MBD",
                "incident_type": "Fiber optic cable failure",
                "description": "Fiber attenuation near customer site.",
                "root_cause": "Fiber attenuation on the cable section.",
                "resolution_status": "RESOLVED",
            },
        ]
        alerts = [
            {
                "alert_id": "ALT-MDN-1",
                "source_ref": "zabbix.csv#csv:row-2",
                "seen_at": "2026-05-05T09:39:20",
                "recovered_at": "2026-05-05T09:40:20",
                "status": "RESOLVED",
                "severity": "High",
                "host": "VNMMDN-VSSPM01",
                "site_code": "MDN",
                "problem": "HTTP Monitoring",
                "problem_signature": "http monitoring",
                "duration": "1m",
                "ack": "No",
                "actions": "UNKNOWN",
                "domain": "UNKNOWN",
                "component": "UNKNOWN",
                "scope": "UNKNOWN",
                "tags": "{}",
                "evidence_label": "SOURCE FACT",
            },
            {
                "alert_id": "ALT-MDN-2",
                "source_ref": "zabbix.csv#csv:row-3",
                "seen_at": "2026-05-30T15:31:20",
                "recovered_at": "2026-05-30T15:32:20",
                "status": "RESOLVED",
                "severity": "High",
                "host": "VNMMDN-VSSPM01",
                "site_code": "MDN",
                "problem": "HTTP Monitoring",
                "problem_signature": "http monitoring",
                "duration": "1m",
                "ack": "No",
                "actions": "UNKNOWN",
                "domain": "UNKNOWN",
                "component": "UNKNOWN",
                "scope": "UNKNOWN",
                "tags": "{}",
                "evidence_label": "SOURCE FACT",
            },
            {
                "alert_id": "ALT-MBD-1",
                "source_ref": "zabbix.csv#csv:row-4",
                "seen_at": "2026-05-29T11:05:04",
                "recovered_at": "2026-05-30T15:42:34",
                "status": "RESOLVED",
                "severity": "High",
                "host": "VNMMBD-PE-FPT-42.116.48.97",
                "site_code": "MBD",
                "problem": "Unavailable by ICMP ping",
                "problem_signature": "unavailable by icmp ping",
                "duration": "1d 4h 37m 30s",
                "ack": "No",
                "actions": "UNKNOWN",
                "domain": "UNKNOWN",
                "component": "UNKNOWN",
                "scope": "UNKNOWN",
                "tags": "{}",
                "evidence_label": "SOURCE FACT",
            },
        ]
        patterns = group_alert_patterns(alerts)

        timeline = build_operational_timeline(incidents, patterns, [], alerts=alerts)

        mdn = next(event for event in timeline if event["event_id"] == "EVT-INC-MDN")
        mbd = next(event for event in timeline if event["event_id"] == "EVT-INC-MBD")

        self.assertEqual(mdn["related_alert_pattern_ids"], [])
        self.assertEqual(mbd["related_alert_pattern_ids"], ["ALP-CDCB1323E9CB"])

    def test_operational_stories_render_sequence_conclusion_and_explicit_gaps(self):
        incidents = [
            {
                "incident_id": "INC-3",
                "source_ref": "incident.xlsx#main:row-3",
                "submitted_at": "2026-05-19T16:22:00",
                "started_at": "2026-05-19T16:10:00",
                "resolved_at": "2026-05-19T16:40:00",
                "site_code": "CCW",
                "isp": "FPT",
                "incident_type": "High latency",
                "description": "CCW users are experiencing slow access.",
                "root_cause": "FPT uplink routing issue.",
                "resolution_status": "RESOLVED",
            }
        ]
        alert_patterns = [
            {
                "alert_pattern_id": "ALP-MATCH",
                "source_refs": ["zabbix.xlsx#main:row-2", "zabbix.xlsx#main:row-3"],
                "first_seen_at": "2026-05-19T16:02:00",
                "last_seen_at": "2026-05-19T16:08:00",
                "last_recovered_at": "2026-05-19T16:09:00",
                "site_code": "CCW",
                "host": "VNMCCW-PNWSW01",
                "problem_signature": "high latency",
                "alert_count": 2,
                "resolved_count": 2,
                "open_count": 0,
            }
        ]
        tickets = [
            {
                "ticket_id": "TKT-100",
                "source_refs": ["IssueReport.xlsx#main:row-2"],
                "first_comment_at": "2026-05-19T16:15:00",
                "last_comment_at": "2026-05-19T16:25:00",
                "title": "CCW users cannot access service",
                "comments_summary": "CCW users report slow access.",
            }
        ]
        recurrence = [
            {
                "recurrence_id": "REC-MATCH",
                "incident_ids": ["INC-3", "INC-4"],
                "incident_count": 2,
            }
        ]

        stories = build_operational_stories(incidents, alert_patterns, tickets, recurrence)
        incident = next(story for story in stories if story["episode_id"] == "OPS-INC-3")
        signal = next(story for story in stories if story["episode_id"] == "OPS-ALP-MATCH")

        self.assertEqual(incident["evidence_coverage"], "ZABBIX + INCIDENT FORM + TICKET")
        self.assertEqual(incident["recurrence_summary"], "2 confirmed incidents (REC-MATCH)")
        self.assertIn("Confirmed RCA", " ".join(item["message"] for item in incident["milestones"]))
        self.assertIn("Service recovered", " ".join(item["message"] for item in incident["milestones"]))
        self.assertEqual(signal["signal_assessment"], "RELATED_TO_CONFIRMED_INCIDENT")
        self.assertIn("Zabbix detected", signal["milestones"][0]["message"])
        self.assertIn("Grouped 2 raw alerts", " ".join(item["message"] for item in signal["milestones"]))

    def test_monitoring_story_does_not_claim_user_impact_from_unrelated_same_site_ticket(self):
        stories = build_operational_stories(
            incidents=[],
            alert_patterns=[
                {
                    "alert_pattern_id": "ALP-UPS",
                    "source_refs": ["zabbix.xlsx#main:row-2"],
                    "first_seen_at": "2026-05-19T16:02:00",
                    "last_seen_at": "2026-05-19T16:08:00",
                    "last_recovered_at": "2026-05-19T16:09:00",
                    "site_code": "SNT",
                    "host": "VNMSNT-UPSF2201",
                    "problem_signature": "ups input frequency out of range",
                    "domain": "power",
                    "component": "power",
                    "alert_count": 2,
                    "resolved_count": 2,
                    "open_count": 0,
                }
            ],
            tickets=[
                {
                    "ticket_id": "TKT-NETWORK",
                    "source_refs": ["IssueReport.xlsx#main:row-2"],
                    "first_comment_at": "2026-05-19T16:03:00",
                    "last_comment_at": "2026-05-19T16:04:00",
                    "title": "SNT network segmentation review",
                    "comments_summary": "Review wireless security policy.",
                }
            ],
            recurrence=[],
        )

        signal = stories[0]
        self.assertEqual(signal["user_impact_status"], "UNKNOWN")
        self.assertEqual(signal["related_ticket_ids"], [])
        self.assertEqual(signal["signal_assessment"], "LIKELY_NOISE_OR_THRESHOLD_REVIEW")

    def test_validation_report_fails_when_reconciliation_is_wrong(self):
        report = build_validation_report(
            source_profile={
                "incident_form_rows": 4,
                "normalized_incidents": 2,
                "rejected_incident_rows": 1,
                "zabbix_rows": 0,
                "normalized_alert_rows": 0,
                "rejected_alert_rows": 0,
                "issue_comment_rows": 0,
                "aggregated_ticket_comment_count": 0,
                "rejected_comment_rows": 0,
            },
            warnings=[],
            known_checks=[],
        )
        self.assertEqual(report["status"], "FAIL")
        self.assertFalse(report["invariants"][0]["passed"])

    def test_package_contains_alpha_documents_audit_workbook_and_pass_gate(self):
        with tempfile.TemporaryDirectory() as temporary:
            output_dir = Path(temporary) / "package"
            package = build_knowledge_package(
                raw_dir=FIXTURES,
                master_data_path=FIXTURES / "master_data.xlsx",
                output_dir=output_dir,
                generated_at="2026-06-02T00:00:00Z",
            )
            required = {
                "manifest.json",
                "validation_report.json",
                "validation_report.md",
                "00_report_context.md",
                "01_executive_summary.md",
                "02_operational_timeline.md",
                "02_confirmed_incidents.md",
                "03_recurrence_patterns.md",
                "04_alert_patterns.md",
                "05_ticket_impact.md",
                "06_data_quality.md",
                "normalized_data.xlsx",
            }
            self.assertEqual({path.name for path in output_dir.iterdir()}, required)
            report = json.loads((output_dir / "validation_report.json").read_text("utf-8"))
            self.assertEqual(report["status"], "PASS")
            self.assertTrue(package["upload_allowed"])
            manifest = json.loads((output_dir / "manifest.json").read_text("utf-8"))
            self.assertIn(
                "master_data.xlsx",
                {item["filename"] for item in manifest["inputs"]},
            )
            workbook = load_workbook(output_dir / "normalized_data.xlsx", read_only=True)
            self.assertEqual(
                workbook.sheetnames,
                [
                    "operational_timeline",
                    "confirmed_incidents",
                    "alert_patterns",
                    "ticket_evidence",
                    "recurrence_patterns",
                    "data_quality",
                    "source_profile",
                ],
            )
            quality_rows = list(workbook["data_quality"].iter_rows(values_only=True))
            quality_text = "\n".join(
                " | ".join(str(value) for value in row if value is not None)
                for row in quality_rows
            )
            workbook.close()
            timeline_text = (output_dir / "02_operational_timeline.md").read_text("utf-8")
            self.assertIn("# Operational Timeline", timeline_text)
            self.assertIn("CONFIRMED_INCIDENT", timeline_text)
            self.assertIn("MONITORING_SIGNAL", timeline_text)
            self.assertIn("### Timeline", timeline_text)
            self.assertIn("### Conclusion", timeline_text)
            self.assertIn("Evidence coverage", timeline_text)
            self.assertIn("Investigation gaps", timeline_text)
            self.assertIn("Incidents missing RCA", quality_text)
            self.assertIn("Sites without confirmed master-data mapping", quality_text)

    def test_explicit_missing_master_data_fails_clearly(self):
        with tempfile.TemporaryDirectory() as temporary:
            with self.assertRaisesRegex(FileNotFoundError, "master-data"):
                build_knowledge_package(
                    raw_dir=FIXTURES,
                    master_data_path=Path(temporary) / "missing-master-data.xlsx",
                    output_dir=Path(temporary) / "package",
                    generated_at="2026-06-02T00:00:00Z",
                )

    def test_package_is_deterministic_for_same_inputs_and_generated_at(self):
        with tempfile.TemporaryDirectory() as temporary:
            first = Path(temporary) / "first"
            second = Path(temporary) / "second"
            for output_dir in [first, second]:
                build_knowledge_package(
                    raw_dir=FIXTURES,
                    master_data_path=FIXTURES / "master_data.xlsx",
                    output_dir=output_dir,
                    generated_at="2026-06-02T00:00:00Z",
                )
            for filename in [
                "manifest.json",
                "validation_report.json",
                "validation_report.md",
                "00_report_context.md",
                "01_executive_summary.md",
                "02_operational_timeline.md",
                "02_confirmed_incidents.md",
                "03_recurrence_patterns.md",
                "04_alert_patterns.md",
                "05_ticket_impact.md",
                "06_data_quality.md",
            ]:
                self.assertEqual(
                    (first / filename).read_bytes(),
                    (second / filename).read_bytes(),
                    filename,
                )


class SuppliedRawDataIntegrationTest(unittest.TestCase):
    def test_supplied_raw_data_matches_known_counts_and_patterns(self):
        raw_dir = ROOT / "RawData"
        incidents = load_incidents(
            raw_dir / "SEA - Corp IT- ILL- Incident Report   (Responses).xlsx"
        )
        alerts = load_zabbix_alerts(raw_dir / "Export zabbix")
        tickets = load_issue_tickets(raw_dir / "IssueReport.xlsx")
        recurrence = group_incident_recurrence(incidents.records)
        alert_patterns = group_alert_patterns(alerts.records)
        timeline = build_operational_timeline(
            incidents.records,
            alert_patterns,
            tickets.records,
            alerts=alerts.records,
        )

        self.assertEqual(len(incidents.records), 52)
        self.assertEqual(len(alerts.records), 10425)
        self.assertEqual(len(tickets.records), 923)
        self.assertEqual(sum(ticket["comment_count"] for ticket in tickets.records), 2652)

        ms2 = next(
            pattern
            for pattern in recurrence
            if pattern["site_code"] == "MS2"
            and pattern["isp"] == "VNPT"
            and pattern["incident_type"] == "High latency"
        )
        xas = next(
            pattern
            for pattern in recurrence
            if pattern["site_code"] == "XAS"
            and pattern["isp"] == "CMC"
            and pattern["incident_type"] == "Fiber optic cable failure"
        )
        self.assertEqual(ms2["incident_count"], 16)
        self.assertEqual(xas["incident_count"], 4)
        self.assertEqual(len(alert_patterns), 352)
        self.assertEqual(len(timeline), 404)
        self.assertEqual(
            sum(event["event_type"] == "CONFIRMED_INCIDENT" for event in timeline),
            52,
        )
        self.assertEqual(
            sum(event["event_type"] == "ZABBIX_ALERT_PATTERN" for event in timeline),
            352,
        )
        may_incidents = {
            event["event_id"]: event["related_alert_pattern_ids"]
            for event in timeline
            if event["event_type"] == "CONFIRMED_INCIDENT"
            and event["started_at"].startswith("2026-05")
        }
        self.assertEqual(
            may_incidents["EVT-INC-51"],
            [],
            "MDN long-running alert patterns should not match without event overlap.",
        )
        self.assertEqual(may_incidents["EVT-INC-53"], ["ALP-21A98CCEA4A6"])
        self.assertEqual(
            may_incidents["EVT-INC-54"],
            ["ALP-6E01E457377C", "ALP-C031A95EC809", "ALP-CDCB1323E9CB"],
        )


if __name__ == "__main__":
    unittest.main()
