# Implementation Checklist: IT Operations Knowledge Package for Alpha Intelligence

## 1. Converter Foundation

- [x] 1.1 Add project requirements for Python, `openpyxl`, and test tooling.
  - Verify: install dependencies in a clean environment and import required packages.

- [x] 1.2 Add golden Excel fixtures under `tests/fixtures/`.
  - Cover: valid rows, blank rows, missing optional values, malformed timestamps, duplicate ticket comments, changing Zabbix metric values, and unconfirmed master-data rows.
  - Verify: fixture contents are intentionally small and human-readable.

- [x] 1.3 Add converter CLI skeleton at `scripts/build_alpha_knowledge_package.py`.
  - Inputs: `--raw-dir`, optional `--master-data`, and `--output-dir`.
  - Verify: `--help` documents all inputs and missing directories fail clearly.

- [x] 1.4 Add shared source-lineage helpers.
  - Output source references as `<filename>#<sheet>:row-<number>`.
  - Verify: source references remain stable across repeated runs.

## 2. Source Adapters

- [x] 2.1 Implement and test the incident-form adapter.
  - Read only `Form Responses 1`; do not duplicate records from the `MS2 -VNPT` subset sheet.
  - Normalize start and resolution timestamps.
  - Verify: supplied file produces exactly 52 confirmed incidents.

- [x] 2.2 Implement and test the Zabbix adapter.
  - Parse tags, normalize problem signatures, preserve open/resolved status, and retain source lineage.
  - Verify: supplied file produces exactly 1,000 alert rows before grouping.

- [x] 2.3 Implement and test the issue-report adapter.
  - Aggregate comment rows by ticket ID while retaining user and assignee evidence.
  - Verify: supplied file produces exactly 923 unique tickets from 2,652 comment rows.

- [x] 2.4 Implement and test the optional master-data adapter.
  - Read only rows with `review_status=CONFIRMED` as authoritative.
  - Verify: unconfirmed seed rows do not become factual mappings.

## 3. Deterministic Analytics

- [x] 3.1 Add incident recurrence grouping.
  - Key: normalized `site_code + isp + incident_type`.
  - Verify: `MS2 | VNPT | High latency = 16`.
  - Verify: `XAS | CMC | Fiber optic cable failure = 4`.

- [x] 3.2 Add alert-pattern grouping.
  - Key: `host + normalized problem signature`.
  - Replace changing metric values with placeholders while retaining source references.
  - Verify: grouped counts never change the confirmed-incident count.

- [x] 3.3 Add ticket-impact summaries.
  - Preserve ticket IDs and direct user evidence.
  - Do not infer site impact unless supported by confirmed mapping or explicit ticket text.

- [x] 3.4 Add data-quality checks.
  - Report missing RCA, missing preventive action, unconfirmed master data, unresolved mappings, and parse warnings.

## 4. Package Rendering

- [x] 4.1 Generate `manifest.json`.
  - Include package version, generated timestamp, input hashes, source profile, and warnings.

- [x] 4.2 Generate `validation_report.json` and `validation_report.md`.
  - Include reconciliation counts, invariant checks, warnings, failures, master-data coverage, and final status.
  - Verify: any failed required invariant sets final status to `FAIL`.

- [x] 4.3 Generate Markdown documents for Knowledge Expert ingestion.
  - Render the Markdown files defined in `specs/knowledge-package-format.md`.
  - Verify: each evidence record has a stable ID, label, and source reference.

- [x] 4.4 Generate `normalized_data.xlsx`.
  - Add audit sheets for incidents, alert patterns, ticket evidence, recurrence patterns, data quality, and source profile.
  - Verify: workbook opens successfully with `openpyxl`.

- [x] 4.5 Add deterministic-run verification.
  - Run the converter twice against unchanged inputs.
  - Verify: record IDs and content are stable except for generated timestamp.

- [x] 4.6 Add upload-gate verification.
  - Verify: documentation and package status make it explicit that only a `PASS` package can be uploaded to Alpha.

## 5. Sample Package and Documentation

- [x] 5.1 Generate the Alpha-ready sample package from the supplied raw exports.
  - Output: `02-Output/alpha-knowledge-package/`.

- [x] 5.2 Add a local converter usage guide.
  - Explain regeneration, optional master data, output files, and common validation failures.

- [x] 5.3 Review generated Markdown for retrieval quality.
  - Check chunk headings, evidence IDs, source references, and operational readability.

- [x] 5.4 Perform and record a human spot-check.
  - Review at least 10 confirmed incidents, 10 tickets, 10 alert patterns, every high-count recurrence group, and every severe data-quality warning.

## 6. Alpha Intelligence Setup

The following steps require an internal Alpha Intelligence account and are documented in `docs/build-on-alpha-intelligence.md`.

- [x] 6.1 Create the `IT Operations Historical Intelligence` Knowledge Expert.
  - Upload generated Markdown files manually for the PoC.

- [x] 6.2 Create the `IT Operations Investigation Assistant` Super Agent.
  - Attach the Expert and apply the instruction template in `specs/alpha-super-agent-setup.md`.
  - Use Inspect Mode during validation.

- [x] 6.3 Run validation prompts.
  - Confirm the agent distinguishes incidents from alerts.
  - Confirm it cites retrieved record IDs and states limitations.

## 7. Quality Gate

- [x] 7.1 Run the full test suite.
- [x] 7.2 Generate the sample package from a clean output directory.
- [x] 7.3 Verify the sample package against expected counts.
- [x] 7.4 Confirm `validation_report.md` status is `PASS` before Alpha upload.
- [x] 7.5 Record any Alpha-side limitations discovered during validation.
  - Alpha-side validation passed for the six required prompts.
  - No blocker was reported before moving to processing-tool automation.

## 8. Timeline-First Investigation Upgrade

- [x] 8.1 Add an operational-timeline specification and stable event contract.
  - Include confirmed incidents, grouped Zabbix signal events, responsibility domain,
    user-impact status, related evidence IDs, and correlation basis.

- [x] 8.2 Add failing tests for responsibility classification and conservative correlation.
  - Verify: raw alerts remain alert-pattern events.
  - Verify: incident and alert link only when site and buffered time windows match.
  - Verify: unsupported responsibility remains `UNKNOWN`.

- [x] 8.3 Generate `02_operational_timeline.md`.
  - Verify: timeline contains every confirmed incident and every grouped Zabbix pattern.
  - Verify: timeline is ordered by timestamp and uses stable `EVT-...` IDs.

- [x] 8.4 Add `operational_timeline` to `normalized_data.xlsx`.
  - Verify: humans can audit episode type, milestones, impact status,
    responsibility domain, and source lineage.

- [x] 8.5 Update the Alpha setup instructions and validation prompts.
  - Verify: the Super Agent starts date-range investigations from the timeline.

- [x] 8.6 Regenerate and re-audit the supplied sample package.
  - Verify: package validation remains `PASS`.

- [x] 8.7 Replace flat timeline records with operational stories.
  - Verify: each episode has ordered milestones, conclusion, evidence coverage,
    investigation gaps, and a conservative signal assessment.

- [x] 8.8 Prevent false-positive ticket impact correlation.
  - Verify: same-site and same-window tickets still require issue relevance.
  - Verify: incidental keywords inside unrelated comments do not produce
    `CONFIRMED` user impact.
