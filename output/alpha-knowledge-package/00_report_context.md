# IT Operations Report Context

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

- Confirmed incidents: `52`
- Raw Zabbix alerts: `1000`
- Operational stories: `128`
- Unique tickets: `923`
- Issue-report comment rows: `2652`
- Confirmed incident period: `2025-12-01T07:35:00` to `2026-05-29T12:20:00`
- Raw alert period: `2026-05-12T17:34:13` to `2026-05-19T16:32:36`
- Ticket evidence period: `2026-05-01T06:35:37` to `2026-05-19T17:54:47`

## Data Quality Warnings

- Unconfirmed master-data rows ignored as facts: 102
- Sites without confirmed master-data mapping: 14
- Alert hosts without confirmed master-data mapping: 33
- Incidents missing RCA: 2
- Incidents missing preventive action: 35
- No incident-to-Zabbix timeline correlations matched the current exports
- No direct site-explicit ticket correlations matched confirmed incidents
