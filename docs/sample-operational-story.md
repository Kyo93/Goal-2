# Sample Operational Story Answers

## Important Coverage Limitation

The supplied exports do not contain one period with a complete
`Zabbix + ticket + confirmed incident` evidence chain:

- Zabbix export coverage: `2026-05-12T17:34:13` to `2026-05-19T16:32:36`.
- Confirmed incident before that window: `INC-51` on `2026-05-10`.
- Next confirmed incident after that window: `INC-52` on `2026-05-26`.
- No issue ticket passed the conservative same-site, overlapping-window, and
  issue-relevance checks for a Zabbix monitoring story.

The converter therefore reports missing links explicitly. It does not fabricate
the ideal full-chain example.

## Example: Confirmed Incident Story

Selected period: `2026-05-10`

```text
13:20 IT recorded confirmed incident INC-51 at MDN: Others.
17:50 Service recovered according to the confirmed incident record.
2026-05-11 10:21 Confirmed RCA recorded: The issue belongs to Shopee's local segment.

Conclusion:
- Episode type: CONFIRMED_INCIDENT
- User impact: POTENTIAL_IMPACT
- Responsibility domain: INHOUSE
- Resolution status: RESOLVED
- Evidence coverage: INCIDENT FORM
- Recurrence: 1 confirmed incident

Investigation gaps:
- No same-site Zabbix signal matched this incident window.
- No direct site-explicit ticket matched this incident window.
```

## Example: Monitoring-Signal Story

Selected period: `2026-05-12` to `2026-05-19`

```text
2026-05-12 18:38 Zabbix detected UPS input-frequency alerts at VNMSNT-UPSF2201.
2026-05-19 16:32 The converter grouped 70 raw alerts into ALP-079F1ABCD016.
2026-05-19 16:41 Latest recovered Zabbix observation was recorded.

Conclusion:
- Episode type: MONITORING_SIGNAL
- Signal assessment: LIKELY_NOISE_OR_THRESHOLD_REVIEW
- User impact: UNKNOWN
- Responsibility domain: UNKNOWN
- Resolution status: SIGNAL_RECOVERED
- Evidence coverage: ZABBIX

Investigation gaps:
- No confirmed incident matched this monitoring-signal window.
- No direct site-explicit ticket matched this monitoring-signal window.
```

## What A Complete Future Story Looks Like

When future exports contain matching evidence, the same converter emits:

```text
09:02 Zabbix detected high latency at host MS2.
09:08 Repeated alerts were grouped into a monitoring signal.
09:15 Ticket TKT-... provided direct site-explicit user evidence.
09:22 IT recorded confirmed incident INC-...
10:10 Confirmed RCA recorded: ISP routing fluctuation.
10:25 Service recovered.

Conclusion:
- User impact: CONFIRMED
- Responsibility domain: ISP
- Evidence coverage: ZABBIX + INCIDENT FORM + TICKET
- Recurrence: 16 confirmed incidents
```
