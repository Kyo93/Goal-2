# Implementation Checklist

Use this file as the execution tracker for building the Alpha processing and query workflow.

When a step is completed on Alpha, update the checkbox from `[ ]` to `[x]` and add a short verification note under that step.

## 1. Architecture and Contract

- [x] 1.1 Freeze the architecture decision.
  - Decision: use separate processing workflows, a connector workflow, and a query workflow/tool.
  - Reference: `docs/alpha-workflow-architecture.md`.

- [x] 1.2 Keep deterministic logic outside the SuperAgent.
  - Decision: SuperAgent explains; tools normalize, count, group, correlate, and validate.

- [x] 1.3 Define evidence priority for incomplete data.
  - Priority: ISP Incident Report, then ITcenter Ticket, then Zabbix Alert.

- [x] 1.4 Define Knowledge vs tool responsibility.
  - Knowledge Markdown is for context and explanation.
  - Query tool is for exact site/time-range counts and grouping.

## 2. Local Tool Baseline

- [x] 2.1 Add source-specific processor commands.
  - Verify: incident, Zabbix, and ticket sources each generate canonical JSON locally.

- [x] 2.2 Add connector command for processed sources.
  - Verify: connector reads canonical JSON and generates the Alpha package.

- [x] 2.3 Return machine-readable processing status.
  - Verify: response includes `ok`, `validation_status`, `upload_allowed`, `source_profile`, `warnings`, `knowledge_files`, and `audit_files`.

- [x] 2.4 Add query timeline command locally.
  - Verify: query accepts `site_code`, `from_at`, `to_at`, and `source_scope`.

- [x] 2.5 Validate local Zabbix site/month query.
  - Verify expected CPL May 2026 result:
    - `matched_event_count = 37`
    - Network reachability: 12 patterns / 16 alerts
    - HTTP monitoring: 21 patterns / 987 alerts
    - Host restart/uptime: 2 patterns / 2 alerts
    - Zabbix agent/active check: 2 patterns / 2 alerts

## 3. Alpha Processing Workflows

- [x] 3.1 Build `Clean Rawdata - ISP` workflow on Alpha.
  - Verify: workflow accepts raw Google Sheet/CSV/XLSX incident report and returns normalized JSON/Markdown.
  - Current baseline: `record_count = 54`, `rejected_row_count = 0`.

- [x] 3.2 Add ISP output fields needed by downstream query.
  - Required fields: `record_type`, `incident_id`, `site_code`, `started_at`, `resolved_at`, `duration_minutes`, `incident_type`, `severity`, `resolution_status`, `responsibility_domain`, `root_cause`, `evidence_label`, `source_ref`.
  - Local code ready: `docs/alpha-incident-processor-node.py` now emits `record_type`, `duration_minutes`, `responsibility_domain`, and `responsibility_basis`.
  - Safety note: local code preserves Alpha's working `confirmed_incidents_file` / `02_confirmed_incidents.md` file payload path, mojibake cleanup, Markdown header, and tiny-file guards.
  - Local verify: XLSX sample returns `record_type=CONFIRMED_INCIDENT`, `duration_minutes=8`, `responsibility_domain=ISP` for `INC-3`; Markdown/file payload size both equal `57405` bytes.
  - Alpha verify: pass. One sample incident record contains all required downstream query fields and `02_confirmed_incidents.md` generation still works.

- [ ] 3.3 Build `Clean Rawdata - Zabbix` workflow on Alpha.
  - Input: uploaded Zabbix CSV/XLSX export or file body. Alpha does not connect to internal Zabbix directly.
  - Local/VPN pull: use `scripts/zabbix_data_pull_tool.py` to export normalized CSV from Zabbix API, then upload that file to Alpha.
  - Output: `zabbix_alerts.json`, `alert_patterns.json`, Markdown summary, processing summary.
  - Verify: output includes `pattern_family`, `problem_signature`, `host`, `site_code`, `first_seen_at`, `last_seen_at`, `last_recovered_at`, `investigation_priority`, and `signal_assessment`.

- [ ] 3.4 Validate Zabbix processor with CPL data.
  - Verify: CPL has pattern families including Network reachability, HTTP monitoring, Host restart/uptime, and Zabbix agent/active check.
  - Verify: Zabbix-only records are not marked as confirmed incidents.

- [ ] 3.5 Build `Clean Rawdata - ITcenter` workflow on Alpha.
  - Input: ITcenter ticket export.
  - Output: `ticket_evidence.json`, Markdown summary, processing summary.
  - Verify: ticket records include `ticket_id`, `site_code`, `created_at`, `symptom`, `affected_scope`, `evidence_label`, and `source_ref`.

## 4. Alpha Connector Workflow

- [ ] 4.1 Build `Connect IT Ops Sources` workflow.
  - Input: normalized incident, Zabbix, alert pattern, and ticket JSON.
  - Output: `operational_timeline.json`, Markdown Knowledge package, validation result.

- [ ] 4.2 Add correlation rules.
  - Verify: same-site/time Zabbix correlation is separated into:
    - `RELATED_TO_CONFIRMED_INCIDENT`
    - `TIME_ALIGNED_CONTEXT_ONLY`
    - `NO_MATCHING_ZABBIX_SIGNAL`

- [ ] 4.3 Add evidence priority rules.
  - Verify: if sources disagree, the output preserves source conflict and prioritizes ISP Incident Report, then ITcenter Ticket, then Zabbix Alert.

- [ ] 4.4 Add Knowledge refresh gate.
  - Verify: Knowledge refresh is allowed only when `validation_status = PASS` and `upload_allowed = true`.

- [ ] 4.5 Generate uploadable Markdown files.
  - Verify: output includes the expected Markdown package files:
    - `00_report_context.md`
    - `01_executive_summary.md`
    - `02_operational_timeline.md`
    - `02_confirmed_incidents.md`
    - `03_ticket_evidence.md`
    - `04_alert_patterns.md`
    - site/summary/data-quality files used by the current package contract

## 5. Alpha Query Workflow / Tool

- [ ] 5.1 Build `Query IT Ops Timeline` workflow.
  - Input:
    ```json
    {
      "site_code": "CPL",
      "from_at": "2026-05-01T00:00:00",
      "to_at": "2026-06-01T00:00:00",
      "source_scope": "zabbix"
    }
    ```

- [ ] 5.2 Implement time-window filtering.
  - Verify: records match when their event/observation timestamp overlaps `from_at` to `to_at`.
  - Verify: long-running Zabbix patterns are counted only by observations inside the requested window.

- [ ] 5.3 Implement source filtering.
  - Supported `source_scope` values:
    - `all`
    - `incident`
    - `ticket`
    - `zabbix`

- [ ] 5.4 Return Zabbix family summary.
  - Required output fields:
    - `monitoring_family_summary`
    - `monitoring_pattern_summary`
    - `matched_event_count`
    - `counts_by_episode_type`
    - `answer_contract`

- [ ] 5.5 Validate CPL May 2026 Zabbix query on Alpha.
  - Expected:
    - `matched_event_count = 37`
    - Network reachability: 12 patterns / 16 alerts
    - HTTP monitoring: 21 patterns / 987 alerts
    - Host restart/uptime: 2 patterns / 2 alerts
    - Zabbix agent/active check: 2 patterns / 2 alerts

- [ ] 5.6 Validate MS2 date-range incident query on Alpha.
  - Input: `site_code = MS2`, `from_at = 2025-12-03T00:00:00`, `to_at = 2025-12-04T00:00:00`, `source_scope = all`.
  - Expected: one confirmed incident, no direct ticket/user evidence unless present in query result.

## 6. SuperAgent Integration

- [ ] 6.1 Expose `Query IT Ops Timeline` as a SuperAgent-callable tool.
  - Verify: SuperAgent can pass `site_code`, `from_at`, `to_at`, and `source_scope` into the workflow.

- [ ] 6.2 Update SuperAgent prompt.
  - Required rule: for site/time-range questions, call the query workflow first.
  - Required rule: do not compute exact counts from Knowledge-only fragments.

- [ ] 6.3 Configure Knowledge usage as context only for exact time-range questions.
  - Verify: Knowledge is used for definitions, evidence labels, and fallback context.
  - Verify: exact counts come from tool result when available.

- [ ] 6.4 Upload refreshed Markdown package to Knowledge.
  - Verify: all uploaded Markdown files are from the same validated package version.
  - Do not upload `.json` files to Knowledge.

## 7. Validation Prompts

- [ ] 7.1 Validate Zabbix site/month answer.
  - Prompt: `CPL trong thang 5/2026 co alert Zabbix gi?`
  - Expected: answer by pattern family first, not by individual `OPS-ALP-*` records.

- [ ] 7.2 Validate date-range site answer.
  - Prompt: `Trong khoang 2025-12-03T00:00:00 den 2025-12-04T00:00:00, o site MS2 co cac su kien gi xay ra?`
  - Expected: management-ready summary with timeline, evidence, impact limitation, and conclusion.

- [ ] 7.3 Validate unrelated same-window Zabbix context.
  - Prompt: ask about `OPS-INC-53`.
  - Expected: host restart/uptime alert is `TIME_ALIGNED_CONTEXT_ONLY` for fiber/cable incidents unless another source explicitly links it.

- [ ] 7.4 Validate source priority.
  - Prompt: ask a question where ISP incident, ticket, and Zabbix evidence are incomplete.
  - Expected: answer prioritizes ISP Incident Report, then ITcenter Ticket, then Zabbix Alert.

- [ ] 7.5 Validate no direct user evidence wording.
  - Expected: `NO_DIRECT_EVIDENCE` means missing direct ticket/user evidence, not proof that no users were affected.

- [ ] 7.6 Validate repeatability.
  - Run the same CPL May question three times.
  - Expected: same counts and same pattern-family ordering when the query tool is called.

## 8. Update Protocol

- [ ] 8.1 After each Alpha workflow is completed, update this checklist.
  - Add date/time and a one-line verification note under the completed task.

- [ ] 8.2 If Alpha output differs from local baseline, record the mismatch.
  - Include input file, workflow name, output summary, and suspected cause.

- [ ] 8.3 If a workflow contract changes, update both files:
  - `openspec/changes/alpha-processing-tool/design.md`
  - `docs/alpha-workflow-architecture.md`

- [ ] 8.4 Before declaring the Alpha build complete, all required validation prompts must pass.
