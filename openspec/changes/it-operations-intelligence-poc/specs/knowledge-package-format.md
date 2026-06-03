# Specification: Alpha Knowledge Package Format

## Goal

Define a portable package that Alpha Intelligence Knowledge Expert can retrieve reliably and that humans can audit.

## Required Output Files

| File | Purpose |
| --- | --- |
| `manifest.json` | Package version, generated timestamp, file hashes, source profile, and converter warnings |
| `validation_report.json` | Machine-readable quality-gate result, reconciliation counts, invariant checks, warnings, and failures |
| `validation_report.md` | Human-readable quality-gate summary used before upload to Alpha |
| `00_report_context.md` | Agent guardrails, definitions, coverage period, and how to interpret evidence |
| `01_executive_summary.md` | Deterministically calculated KPIs and notable patterns |
| `02_operational_timeline.md` | Primary date-range investigation stories with ordered milestones and conclusions |
| `02_confirmed_incidents.md` | One section per confirmed incident |
| `03_recurrence_patterns.md` | One section per deterministic incident recurrence group |
| `04_alert_patterns.md` | One section per grouped Zabbix alert pattern |
| `05_ticket_impact.md` | One section per user ticket with impact evidence |
| `06_data_quality.md` | Missing fields, mapping coverage, and limitations |
| `normalized_data.xlsx` | Human-audit workbook with normalized table sheets |

## Upload Gate

Only upload a generated package into Alpha Intelligence when:

```text
validation_report.status = PASS
```

Any failed required invariant sets the package status to `FAIL`.

## Validation Report

The report must include:

- Input filename and SHA-256 hash.
- Input row counts.
- Normalized record counts.
- Skipped blank-row counts.
- Rejected-row counts and reasons.
- Reconciliation invariants.
- Known sample-pattern checks when running against the supplied sample dataset.
- Missing RCA and missing preventive-action counts.
- Master-data coverage and unconfirmed-row warnings.
- Incident-site and alert-host counts without confirmed master-data mappings.
- Final `PASS` or `FAIL` status.

Required reconciliation rules:

```text
incident_form_rows = normalized_incidents + rejected_incident_rows
zabbix_rows = normalized_alert_rows + rejected_alert_rows
issue_comment_rows = aggregated_ticket_comment_count + rejected_comment_rows
```

## Evidence Labels

- `SOURCE FACT`: imported from a source row.
- `COMPUTED FACT`: calculated deterministically by Python.
- `ESTIMATED`: derived from incomplete or unconfirmed mapping.
- `UNKNOWN`: not supported by available data.

## Operational Timeline Contract

The timeline is the first retrieval source for questions about a selected period.
It must contain operational stories:

- One `CONFIRMED_INCIDENT` event per normalized incident.
- One `MONITORING_SIGNAL` episode per grouped Zabbix pattern.
- Ordered milestones and stable `OPS-...` IDs.
- Responsibility domain: `INHOUSE`, `ISP`, `EXTERNAL`, or `UNKNOWN`.
- User-impact status: `CONFIRMED`, `ESTIMATED`, `NO_EVIDENCE`, or `UNKNOWN`.
- Related incident, alert-pattern, and ticket IDs when deterministic correlation rules match.
- A correlation basis that clearly states correlation is not proof of cause.

Raw Zabbix patterns remain monitoring evidence even when correlated with an incident.
Converter-derived responsibility domains are computed classifications based on
confirmed RCA text; they are not new source facts.

## Stable IDs

- Confirmed incident: `INC-<source-row-number>`
- Operational episode: `OPS-INC-<source-row-number>` or `OPS-ALP-<sha256-prefix>`
- Alert pattern: `ALP-<sha256-prefix>`
- Ticket evidence: `TKT-<ticket-id>`
- Recurrence group: `REC-<sha256-prefix>`

## Source References

Use:

```text
<filename>#<sheet-name>:row-<number>
```

Example:

```text
SEA - Corp IT- ILL- Incident Report   (Responses).xlsx#Form Responses 1:row-3
```

## Markdown Chunking Rules

- Use one `##` heading per record.
- Keep source references inside each record section.
- Put summary documents before detailed evidence documents.
- Avoid tables with hundreds of rows in Markdown; use repeated record sections for retrieval.
- Keep raw comment text in the audit workbook. Include concise deterministic excerpts or aggregated summaries in Markdown.

## Audit Workbook Sheets

- `confirmed_incidents`
- `operational_timeline`
- `alert_patterns`
- `ticket_evidence`
- `recurrence_patterns`
- `data_quality`
- `source_profile`
