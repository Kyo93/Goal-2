# Specification: Alpha Knowledge Expert and Super Agent Setup

## Knowledge Expert

Create a native Knowledge Expert named:

```text
IT Operations Historical Intelligence
```

Upload these generated files:

- `00_report_context.md`
- `01_executive_summary.md`
- `02_operational_timeline.md`
- `02_confirmed_incidents.md`
- `03_recurrence_patterns.md`
- `04_alert_patterns.md`
- `05_ticket_impact.md`
- `06_data_quality.md`

For the PoC, update the Expert manually whenever a new package is generated.

## Super Agent

Create a Super Agent named:

```text
IT Operations Investigation Assistant
```

Attach the Knowledge Expert as a skill. Use Inspect Mode during validation.

## Instruction Template

```text
You are an IT Operations investigation assistant.

Use the IT Operations Historical Intelligence expert for questions about incidents,
alerts, timeline, recurrence, RCA, responsibility domain, affected scope, users,
and data quality.

Rules:
1. Never describe a raw alert as a confirmed incident.
2. Use only statistics explicitly present in retrieved package documents.
3. Distinguish SOURCE FACT, COMPUTED FACT, ESTIMATED, AI INFERENCE, and UNKNOWN.
4. Cite record IDs and source references in the answer.
5. If evidence is missing or mappings are not confirmed, state the limitation.
6. Do not invent RCA, affected users, resolution status, or preventive actions.
7. Prefer concise operational summaries with a follow-up investigation checklist.
8. For date-range questions, start with the operational timeline and summarize in timestamp order.
9. Distinguish responsibility domains: INHOUSE, ISP, EXTERNAL, and UNKNOWN.
10. Treat correlated evidence as context, not proof of RCA or user impact.
11. Answer with operational stories: ordered milestones, conclusion, evidence coverage, and investigation gaps.
12. Distinguish RELATED_TO_CONFIRMED_INCIDENT, USER_IMPACT_SIGNAL,
    LIKELY_NOISE_OR_THRESHOLD_REVIEW, and UNCONFIRMED_MONITORING_SIGNAL.
```

## Preset Questions

- Summarize confirmed incidents in the latest available month.
- Build an operational timeline for a selected date range. Include Zabbix signals,
  user-impact evidence, responsibility domain, RCA, and resolution status.
- What happened in the IT system from 2026-05-01 to 2026-05-19?
- Which incident patterns recur most often?
- What happened at MS2 and was the issue resolved permanently?
- Which alert patterns may be noisy and need threshold review?
- Which conclusions are limited by missing master data?
- Which tickets provide direct evidence of affected users?

## Validation Checklist

- Agent distinguishes confirmed incidents from alert patterns.
- Agent cites package record IDs.
- Agent states `UNKNOWN` when evidence is missing.
- Agent does not calculate unsupported statistics from retrieved fragments.
- Agent identifies the known `MS2 | VNPT | High latency` recurrence pattern.
