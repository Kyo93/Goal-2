# Alpha Processing Tool Runbook

## Purpose

This runbook describes the staged processing contract for moving ISP report generation into Alpha orchestration.

Alpha should orchestrate the steps. Deterministic Python code should normalize, group, correlate, validate, and render the package.

## Stage Commands

Run from the project root.

### 1. Incident Processor

```powershell
python scripts\run_alpha_processing_tool.py incident `
  --incident-report-file "01-RawData\ISP Incident Report\SEA - Corp IT- ILL- Incident Report   (Responses).xlsx" `
  --processed-dir 02-Output\alpha-processing-tool\processed
```

Output:

```text
confirmed_incidents.json
```

### 2. Zabbix Processor

```powershell
python scripts\run_alpha_processing_tool.py zabbix `
  --zabbix-export "01-RawData\Export zabbix" `
  --processed-dir 02-Output\alpha-processing-tool\processed
```

Output:

```text
zabbix_alerts.json
alert_patterns.json
```

### 3. Ticket Processor

```powershell
python scripts\run_alpha_processing_tool.py ticket `
  --issue-report-file 01-RawData\Ticket\IssueReport.xlsx `
  --processed-dir 02-Output\alpha-processing-tool\processed
```

Output:

```text
ticket_evidence.json
```

### 4. Connector

```powershell
python scripts\run_alpha_processing_tool.py connect `
  --processed-dir 02-Output\alpha-processing-tool\processed `
  --master-data input\it-operations-master-data-template.xlsx `
  --output-dir 02-Output\alpha-processing-tool\package
```

The connector generates the eight Markdown files for Knowledge Expert ingestion, plus audit files.
It also writes `operational_timeline.json`, which is the preferred deterministic input for
site/time-range questions.

### 5. Query Operational Timeline

Use this when Alpha/Super Agent asks: "from A to B, at site C, what happened?"

```powershell
python scripts\run_alpha_processing_tool.py query-timeline `
  --timeline-file 02-Output\alpha-processing-tool\package\operational_timeline.json `
  --site-code MS2 `
  --from-at 2025-12-03T00:00:00 `
  --to-at 2025-12-04T00:00:00
```

Output:

```text
OPERATIONAL_TIMELINE_QUERY_RESULT JSON, plus a Markdown summary.
```

The query matches only same-site events whose `started_at`/`ended_at` window overlaps the requested range.
It does not infer RCA or user impact.

Same-site/time Zabbix correlation is treated as context first. The connector separates:

- `RELATED_TO_CONFIRMED_INCIDENT`: alert signature supports the incident type/RCA.
- `TIME_ALIGNED_CONTEXT_ONLY`: alert overlaps the same site/time, but does not directly support the incident type/RCA.
- `NO_MATCHING_ZABBIX_SIGNAL`: no same-site Zabbix signal matched the incident window.

Example: a Windows `host has been restarted` alert during a `Fiber optic cable failure`
incident is `TIME_ALIGNED_CONTEXT_ONLY`, not proof that Zabbix confirmed the fiber fault.

When data is incomplete or sources disagree, use this evidence priority:

1. ISP Incident Report: confirmed incident existence, start/end time, RCA, resolution status, ISP/provider, responsibility domain.
2. ITcenter ticket: direct user evidence, affected scope, business/user symptoms, escalation, impact confirmation.
3. Zabbix Alert: monitoring signals, telemetry, timing context, recurrence, technical symptoms.

Lower-priority evidence is still useful as context. If sources conflict, state the conflict and cite the record IDs/source references.

The Super Agent should not return the query fields as the final answer. It should turn
the query result into a management-readable answer:

```text
1. Management summary
2. What happened
3. Impact and evidence
4. Operational conclusion
5. Follow-up / gaps
```

`NO_DIRECT_EVIDENCE` means no direct ticket/user evidence was found. It does not prove
that no user was affected.

`POTENTIAL_IMPACT` means the incident type/description suggests possible impact, but
there is no direct ticket/user confirmation.

For Zabbix-alert questions such as "site CPL has what Zabbix alerts in May", answer by
pattern family and problem signature first. Use `monitoring_family_summary` and
`monitoring_pattern_summary` before listing episode IDs. Prioritize investigation using
`investigation_priority`, `query_alert_count`, `query_first_seen_at`, `query_last_seen_at`,
and whether multiple hosts fired together.

Do not start Zabbix-alert answers by listing individual `OPS-ALP-*` records. Use at most
3 episode IDs in the main body; keep the rest in a compact evidence line only if needed.
If the workflow uses Knowledge/RAG instead of the query tool, start from the `Site Pattern
Family Summary` section in `04_alert_patterns.md`.

If repeated runs of the same Zabbix-alert question produce different answers, the Super
Agent is likely answering from partial RAG fragments. Fix by forcing the workflow to call
`query-timeline` first and pass the full query result to the Super Agent. A complete
site/month Zabbix answer must use `monitoring_family_summary` and
`monitoring_pattern_summary`; individual `OPS-ALP-*` records are evidence details only.

Preferred Zabbix-alert answer shape:

```text
Trong khoảng [from_at] đến [to_at], site [site_code] ghi nhận [pattern_count] Zabbix monitoring patterns.
Nhóm đáng chú ý nhất là [pattern_family/signature] vì [why_it_matters], xuất hiện trên [hosts] trong khoảng [first] đến [last].
Nêu nhóm HTTP/noise nếu nhiều nhưng ít ý nghĩa điều tra; ưu tiên network/firewall/ICMP nếu có.
Nếu không có confirmed incident/ticket khớp trực tiếp, user impact vẫn là UNKNOWN.
```

Keep the final answer concise for a middle-management operations reader. Use record IDs
and source references in a compact evidence line, not as the main body.

## Full Command

```powershell
python scripts\run_alpha_processing_tool.py full `
  --incident-report-file "01-RawData\ISP Incident Report\SEA - Corp IT- ILL- Incident Report   (Responses).xlsx" `
  --zabbix-export "01-RawData\Export zabbix" `
  --issue-report-file 01-RawData\Ticket\IssueReport.xlsx `
  --master-data input\it-operations-master-data-template.xlsx `
  --processed-dir 02-Output\alpha-processing-tool\processed `
  --output-dir 02-Output\alpha-processing-tool\package
```

Only refresh Alpha Knowledge Expert when the JSON response contains:

```json
{
  "validation_status": "PASS",
  "upload_allowed": true
}
```

## Alpha Orchestration Shape

```text
Incident Processor
Zabbix Processor
Ticket Processor
  -> Connector
  -> if upload_allowed=true, refresh Knowledge Expert with knowledge_files
  -> Super Agent calls query-timeline for exact site/time-range investigations
  -> run Super Agent validation prompts
```

Super Agent should explain the validated package. It should not count raw rows, group alerts, or decide confirmed incidents directly.
