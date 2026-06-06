# Design: Alpha Processing and Query Tools for ISP Report Automation

## Context and Technical Approach

The existing converter remains the source of truth for deterministic processing. Alpha should orchestrate the processing and explain the validated output, but it should not count raw spreadsheet rows or infer confirmed incidents from alert fragments.

The architecture now has two separate tool types:

```text
Processing tools = normalize raw source data
Query tool       = filter/group the normalized timeline for user questions
Knowledge files  = context and explanation rules
SuperAgent       = management-ready answer writer
```

For site/time-range questions, the SuperAgent must call the query tool first. Knowledge retrieval alone is not stable enough for exact counting, month filtering, or Zabbix pattern grouping.

The processing tool is a staged wrapper around:

```text
scripts/build_alpha_knowledge_package.py
src/itops_alpha/converter.py
scripts/run_alpha_processing_tool.py
src/itops_alpha/processing_tool.py
```

## Proposed Flow

```text
Incident report raw export -> Incident Processor -> confirmed_incidents.json
Zabbix export file         -> Zabbix Processor   -> zabbix_alerts.json + alert_patterns.json
Issue report raw export    -> Ticket Processor   -> ticket_evidence.json

confirmed_incidents.json
+ zabbix_alerts.json
+ alert_patterns.json
+ ticket_evidence.json
  -> Connector / correlation engine
  -> validation report
  -> if PASS: generated Markdown package
  -> Knowledge Expert refresh
  -> Super Agent validation prompts
```

For user investigations:

```text
User question with site/time range
  -> SuperAgent calls Query IT Ops Timeline
  -> query tool reads operational_timeline.json or equivalent normalized timeline state
  -> query tool returns filtered JSON
  -> SuperAgent explains the tool result
```

The processing flow builds data. The query flow answers filtered questions.

## Tool Contract

### Stage 1: Incident Processor

Input:

- `incident_report_file`
- `processed_dir`

Output:

- `confirmed_incidents.json`

### Stage 2: Zabbix Processor

Input:

- `zabbix_export`
- `processed_dir`

Alpha does not call the internal Zabbix API directly. The Zabbix API pull runs outside
Alpha from a machine/network that can reach internal Zabbix, then the exported CSV/XLSX
file is uploaded to this processor.

Output:

- `zabbix_alerts.json`
- `alert_patterns.json`

### Stage 3: Ticket Processor

Input:

- `issue_report_file`
- `processed_dir`

Output:

- `ticket_evidence.json`

### Stage 4: Connector

Input:

- `processed_dir`
- `output_dir`
- optional `master_data`

Output:

- `ok`
- `validation_status`
- `upload_allowed`
- `source_profile`
- `warnings`
- `knowledge_files`
- `audit_files`
- `operational_timeline_json`

### Stage 5: Query IT Ops Timeline

Input:

- `site_code`
- `from_at`
- `to_at`
- `source_scope`

Allowed `source_scope` values:

```text
all
incident
ticket
zabbix
```

Output:

- `ok`
- `site_code`
- `from_at`
- `to_at`
- `source_scope`
- `matched_event_count`
- `counts_by_episode_type`
- `events`
- `confirmed_incidents`
- `related_tickets`
- `monitoring_family_summary`
- `monitoring_pattern_summary`
- `answer_contract`

The query output is the primary source for exact counts and time-range grouping. The SuperAgent should not recompute these values from Markdown fragments.

### Full Run Inputs

Required:

- `incident_report_file`
- `issue_report_file`
- `zabbix_export_files`

Optional:

- `master_data_file`
- `report_month`
- `host_group`
- `package_version`

### Full Run Outputs

Required:

- `ok`
- `validation_status`
- `upload_allowed`
- `source_profile`
- `warnings`
- `knowledge_files`
- `audit_files`

The wrapper must expose the eight Markdown files as the Knowledge Expert inputs:

```text
00_report_context.md
01_executive_summary.md
02_operational_timeline.md
02_confirmed_incidents.md
03_recurrence_patterns.md
04_alert_patterns.md
05_ticket_impact.md
06_data_quality.md
```

Audit outputs remain available but should not be the primary Knowledge Expert source:

```text
manifest.json
validation_report.json
validation_report.md
normalized_data.xlsx
operational_timeline.json
```

`operational_timeline.json` is not a Knowledge upload target. It is machine-readable state for the query workflow/tool.

## Guardrails

- A failed validation report blocks Knowledge Expert refresh.
- Raw Zabbix alerts remain monitoring signals only.
- Incident form remains the only source of confirmed incidents.
- Ticket evidence remains user-impact evidence only.
- Master data is factual only when `review_status=CONFIRMED`.
- Tool output must include enough counts for Alpha-side sanity checks.
- Time-range answers must use the query tool when available.
- Knowledge-only answers must not claim exact time-range counts unless those counts are explicitly present in retrieved documents.
- Same-site/time Zabbix correlation is context only unless the alert signature supports the incident type or RCA.
- Zabbix-only alerts must remain `MONITORING_SIGNAL`, not confirmed incidents.
- Evidence priority for incomplete data is: ISP Incident Report, then ITcenter Ticket, then Zabbix Alert.

## Verification

- Run the three processors against the current sample files.
- Run the connector against processed source JSON.
- Run the full CLI against the current supplied raw files.
- Compare source profile with the existing validated package.
- Confirm `validation_status = PASS` and `upload_allowed = true`.
- Refresh Alpha Knowledge Expert with the generated Markdown.
- Run `Query IT Ops Timeline` for a known site/month Zabbix question.
- Confirm the query result returns `monitoring_family_summary` and exact time-window counts.
- Re-run the six Super Agent validation prompts.
- Record any mismatch before allowing recurring use.
