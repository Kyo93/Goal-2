# Processed Output View Guide

This guide maps the three raw sources to the processed files you can open after
running the converter.

## Quick View

Open:

```text
02-Output/alpha-knowledge-package/normalized_data.xlsx
```

Use these sheets:

| Sheet | What You See |
| --- | --- |
| `operational_timeline` | Final operational stories joining incidents, Zabbix signals, tickets, evidence coverage, and gaps |
| `confirmed_incidents` | Normalized ISP incident report rows |
| `alert_patterns` | Grouped Zabbix alert patterns |
| `ticket_evidence` | Aggregated issue tickets from comment rows |
| `recurrence_patterns` | Repeated confirmed incident groups |
| `data_quality` | Warnings and rejected rows |
| `source_profile` | Counts and coverage periods |

## Source-To-Output Map

### ISP Incident Report

Raw:

```text
01-RawData/ISP Incident Report/SEA - Corp IT- ILL- Incident Report   (Responses).xlsx
```

Processed views:

```text
02-Output/alpha-knowledge-package/02_confirmed_incidents.md
02-Output/alpha-knowledge-package/03_recurrence_patterns.md
normalized_data.xlsx -> confirmed_incidents
normalized_data.xlsx -> recurrence_patterns
```

### Zabbix Export

Raw:

```text
01-RawData/zbx_problems_export.xlsx
```

Processed views:

```text
02-Output/alpha-knowledge-package/04_alert_patterns.md
normalized_data.xlsx -> alert_patterns
```

### Issue Tickets

Raw:

```text
01-RawData/Ticket/*.csv
```

Processed views:

```text
02-Output/alpha-knowledge-package/05_ticket_impact.md
02-Output/alpha-knowledge-package/05_ticket_impact_index.md
02-Output/alpha-knowledge-package/05_ticket_impact_YYYY_MM.md
normalized_data.xlsx -> ticket_evidence
```

## Cross-Source View

Open:

```text
02-Output/alpha-knowledge-package/02_operational_timeline.md
```

or:

```text
normalized_data.xlsx -> operational_timeline
```

This is the main view for questions like:

- What happened during this time range?
- Which Zabbix signals appeared?
- Was there a confirmed incident?
- Was there ticket evidence of user impact?
- What is the responsibility domain?
- What evidence is missing?

## Current Sample Summary

The current processed package is version `1.2.0` and has validation status `PASS`.

Current counts:

```text
confirmed incidents: 52
raw Zabbix alerts: 5199
grouped Zabbix alert patterns: 365
unique tickets: 2681
ticket comment rows: 9525
operational stories: 417
```

Current cross-source result:

```text
ZABBIX + INCIDENT FORM + TICKET matches: 0
ZABBIX + INCIDENT FORM matches: 0
INCIDENT FORM + TICKET matches: 0
ZABBIX + TICKET matches: 0
```

That means the current raw exports can be viewed and audited, but they do not
contain a complete full-chain operational incident across all three sources.
