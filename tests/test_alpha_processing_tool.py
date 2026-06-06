import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
FIXTURES = ROOT / "tests" / "fixtures"
sys.path.insert(0, str(SRC))

from itops_alpha.processing_tool import (  # noqa: E402
    connect_processed_sources,
    process_incident_source,
    process_ticket_source,
    process_zabbix_source,
    query_timeline_file,
)


class AlphaProcessingToolTest(unittest.TestCase):
    def test_three_source_processors_create_connectable_canonical_outputs(self):
        with tempfile.TemporaryDirectory() as temporary:
            processed_dir = Path(temporary) / "processed"

            incident_result = process_incident_source(
                FIXTURES / "SEA - Corp IT- ILL- Incident Report   (Responses).xlsx",
                processed_dir,
            )
            zabbix_result = process_zabbix_source(
                FIXTURES / "zbx_problems_export.xlsx",
                processed_dir,
            )
            ticket_result = process_ticket_source(
                FIXTURES / "IssueReport.xlsx",
                processed_dir,
            )

            self.assertTrue(incident_result["ok"])
            self.assertTrue(zabbix_result["ok"])
            self.assertTrue(ticket_result["ok"])
            self.assertEqual(incident_result["source_type"], "incident_report")
            self.assertEqual(zabbix_result["source_type"], "zabbix_export")
            self.assertEqual(ticket_result["source_type"], "issue_report")

            expected_intermediates = {
                "confirmed_incidents.json",
                "zabbix_alerts.json",
                "alert_patterns.json",
                "ticket_evidence.json",
            }
            self.assertTrue(expected_intermediates.issubset({p.name for p in processed_dir.iterdir()}))

            incidents = json.loads((processed_dir / "confirmed_incidents.json").read_text("utf-8"))
            patterns = json.loads((processed_dir / "alert_patterns.json").read_text("utf-8"))
            tickets = json.loads((processed_dir / "ticket_evidence.json").read_text("utf-8"))

            self.assertEqual(incidents["records"][0]["evidence_label"], "SOURCE FACT")
            self.assertEqual(patterns["records"][0]["evidence_label"], "COMPUTED FACT")
            self.assertEqual(tickets["records"][0]["evidence_label"], "SOURCE FACT")

    def test_connector_builds_alpha_readable_package_from_three_processed_sources(self):
        with tempfile.TemporaryDirectory() as temporary:
            processed_dir = Path(temporary) / "processed"
            package_dir = Path(temporary) / "package"
            process_incident_source(
                FIXTURES / "SEA - Corp IT- ILL- Incident Report   (Responses).xlsx",
                processed_dir,
            )
            process_zabbix_source(FIXTURES / "zbx_problems_export.xlsx", processed_dir)
            process_ticket_source(FIXTURES / "IssueReport.xlsx", processed_dir)

            package = connect_processed_sources(
                processed_dir=processed_dir,
                output_dir=package_dir,
                master_data_path=FIXTURES / "master_data.xlsx",
                generated_at="2026-06-05T00:00:00Z",
            )

            self.assertTrue(package["ok"])
            self.assertEqual(package["validation_status"], "PASS")
            self.assertTrue(package["upload_allowed"])
            self.assertEqual(len(package["knowledge_files"]), 8)
            self.assertTrue((package_dir / "02_operational_timeline.md").exists())
            self.assertTrue((package_dir / "operational_timeline.json").exists())
            self.assertTrue((package_dir / "validation_report.json").exists())

            query = query_timeline_file(
                package_dir / "operational_timeline.json",
                site_code="CCW",
                from_at="2026-05-19T16:00:00",
                to_at="2026-05-19T17:00:00",
            )
            self.assertTrue(query["ok"])
            self.assertGreaterEqual(query["matched_event_count"], 1)
            self.assertIn("markdown", query)


if __name__ == "__main__":
    unittest.main()
