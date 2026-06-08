# IT Operations Report Context

## Rules for Alpha Intelligence

- Raw alerts are evidence, not confirmed incidents.
- Use statistics exactly as provided in this package. Do not count retrieved fragments.
- Distinguish `SOURCE FACT`, `COMPUTED FACT`, `POTENTIAL_IMPACT`, `AI INFERENCE`, `NO_DIRECT_EVIDENCE`, and `UNKNOWN`.
- Cite record IDs and source references.
- Never invent RCA, affected users, resolution status, or preventive actions.
- Start date-range investigations with `02_operational_timeline.md`.
- Treat timeline correlation as context, not proof of RCA or user impact.
- Same-site/time Zabbix correlation is not enough to prove support for an incident RCA.
  Treat semantically unrelated alerts as `TIME_ALIGNED_CONTEXT_ONLY`.
- Evidence priority for incomplete or conflicting data:
  1. ISP Incident Report for confirmed incident existence, start/end time, RCA,
     resolution status, ISP/provider, and responsibility domain.
  2. ITcenter ticket for direct user evidence, affected scope, business/user
     symptoms, escalation, and impact confirmation.
  3. Zabbix Alert for monitoring signals, telemetry, timing context, recurrence,
     and technical symptoms.
- Do not ignore lower-priority evidence. Use it to add context, confirm timing, or expose gaps.
- If sources conflict, state the conflict and cite record IDs/source references.
- For user impact, direct ITcenter ticket/user evidence outranks incident description.
  Zabbix alone cannot confirm user impact.
- For Zabbix-alert questions, answer by pattern family and problem signature before listing episode IDs.
- For Zabbix-alert questions, prioritize investigation using `pattern_family`,
  `investigation_priority`, query alert count, query first/last seen time, and whether
  multiple hosts fired together.
- For site/date-range questions, do not answer from arbitrary retrieved fragments.
  Prefer the deterministic query workflow/result. If no query result is available,
  retrieve `02_operational_timeline.md` and `04_alert_patterns.md` summary sections
  before answering.
- If only individual `OPS-ALP-*` records are retrieved for a Zabbix-alert question,
  state that the context is incomplete and ask to run or refresh the query. Do not
  claim a complete monthly/site summary from partial records.
- Never say "at least 1 alert" for a complete site/month alert summary unless the
  retrieved context is explicitly partial. Use exact counts only from
  `monitoring_family_summary`, `monitoring_pattern_summary`, or `Site Pattern Family Summary`.
- Distinguish responsibility domains: `INHOUSE`, `ISP`, `EXTERNAL`, and `UNKNOWN`.
- For date-range site questions, write a middle-management brief with:
  management summary, what happened, impact and evidence, operational conclusion,
  and follow-up/gaps.
- Lead with the operational takeaway and use plain language before technical labels.
- Keep date-range site answers concise: 2-4 short paragraphs or 5-8 bullets.
- Do not return only raw fields such as `matched_event_count`, `related_ticket_ids`, or `evidence_coverage`.
- Do not over-expose audit labels such as `SOURCE FACT`, `COMPUTED FACT`, or `NO_MATCHING_ZABBIX_SIGNAL`
  unless they are needed to explain evidence quality.
- Explain `NO_DIRECT_EVIDENCE` as missing direct ticket/user evidence, not proof that no user was affected.
- Explain `POTENTIAL_IMPACT` as possible impact without direct ticket/user confirmation.

## Source Profile

- Confirmed incidents: `52`
- Raw Zabbix alerts: `5199`
- Operational stories: `417`
- Unique tickets: `2681`
- Issue-report comment rows: `9525`
- Ticket monthly partitions: `3`
- Confirmed incident period: `2025-12-01T07:35:00` to `2026-05-29T12:20:00`
- Raw alert period: `2026-05-01T00:40:06` to `2026-06-06T16:57:37`
- Ticket evidence period: `2025-07-31T04:43:41` to `2026-06-07T10:30:16`
- Ticket activity period: `2026-04-01T10:48:19` to `2026-06-07T10:30:16`

## Data Quality Warnings

- Unconfirmed master-data rows ignored as facts: 102
- Sites without confirmed master-data mapping: 14
- Alert hosts without confirmed master-data mapping: 170
- Incidents missing RCA: 2
- Incidents missing preventive action: 35
