# Specification: Operational Timeline Investigation

## Goal

Make the selected time range the primary investigation axis.

For any requested period, the Alpha Super Agent must be able to summarize:

1. What confirmed IT incidents occurred.
2. What Zabbix signals were detected.
3. Whether there is evidence of user impact.
4. Whether the responsibility domain is `INHOUSE`, `ISP`, `EXTERNAL`, or `UNKNOWN`.
5. What confirmed RCA and resolution evidence exists.
6. Whether related patterns recur.

## Operational Episode Contract

The primary output is not a flat list of source records. It is an ordered list
of operational episodes. Each episode must contain:

- `episode_id`
- `episode_type`
- `started_at`
- `ended_at`
- `site_code`
- `headline`
- ordered `milestones`
- `signal_assessment`
- `user_impact_status`
- `responsibility_domain`
- `confirmed_rca`
- `resolution_status`
- `recurrence_summary`
- `evidence_coverage`
- `investigation_gaps`
- source record IDs and references

The rendered Markdown must read as an operational story:

```text
09:02 Zabbix detected high latency at host MS2.
09:08 Repeated alerts were grouped into a signal pattern.
09:15 A ticket reported slow access for users at MS2.
09:22 IT recorded a confirmed incident.
10:10 Confirmed RCA: ISP routing fluctuation.
10:25 Service recovered.

Conclusion:
- User impact: CONFIRMED
- Responsibility domain: ISP
- Evidence coverage: Zabbix + incident form + ticket
- Recurrence: 16 confirmed incidents
```

When a source is unavailable for an episode, render the gap explicitly instead
of omitting it or inventing a milestone.

## Episode Types

### `CONFIRMED_INCIDENT`

Created from one normalized incident-form row.

This event can include related Zabbix alert-pattern IDs and ticket IDs when
deterministic correlation rules match. Correlation does not create RCA.

### `MONITORING_SIGNAL`

Created from one grouped Zabbix pattern.

This episode is monitoring evidence. It is never a confirmed incident, even when
its site and time window overlap a confirmed incident.

## Signal Assessment

- `RELATED_TO_CONFIRMED_INCIDENT`: deterministically correlated with an incident.
- `USER_IMPACT_SIGNAL`: no incident correlation, but direct site-explicit ticket evidence exists.
- `LIKELY_NOISE_OR_THRESHOLD_REVIEW`: repeated signal without incident or ticket evidence.
- `UNCONFIRMED_MONITORING_SIGNAL`: monitoring evidence without enough support for a stronger assessment.

The converter never labels an alert as definitive noise. Noise remains a review candidate.

## Responsibility Domain

The converter classifies confirmed RCA text conservatively:

- `ISP`: provider, uplink, routing, transit, fiber, or cable evidence.
- `INHOUSE`: explicitly internal device, configuration, switch, firewall, or local segment evidence.
- `EXTERNAL`: explicitly external utility, electricity, or third-party dependency evidence.
- `UNKNOWN`: missing RCA or no supported keyword rule.

The classification is a `COMPUTED FACT` with an explicit basis. It does not
replace the original RCA text.

## User Impact

- `CONFIRMED`: at least one directly correlated ticket with explicit site-code text.
- `ESTIMATED`: incident description explicitly reports user or service impact, but
  there is no directly correlated ticket.
- `NO_EVIDENCE`: no direct or estimated user-impact evidence for a confirmed incident.
- `UNKNOWN`: monitoring-only signal event.

## Correlation Rules

Use deterministic correlation only:

1. Site code must match exactly.
2. Time windows must overlap with a fixed buffer.
3. Ticket text must explicitly contain the site code as a token.
4. Store the correlation basis in the event.

## Guardrails

- Raw Zabbix alerts never become confirmed incidents.
- Correlation never becomes RCA.
- Missing evidence stays `UNKNOWN` or `NO_EVIDENCE`.
- Original RCA and source references remain visible.
