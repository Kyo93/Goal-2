# Validation Report

**Status:** `PASS`

**Upload allowed:** `YES`

## Reconciliation Invariants

- `PASS` incident row reconciliation: input=52, accounted=52
- `PASS` zabbix row reconciliation: input=1000, accounted=1000
- `PASS` issue comment reconciliation: input=2652, accounted=2652

## Known Checks

- `PASS` sample recurrence MS2 | VNPT | High latency: expected=16, actual=16
- `PASS` sample recurrence XAS | CMC | Fiber optic cable failure: expected=4, actual=4

## Warnings

- Alert hosts without confirmed master-data mapping: 33
- Incidents missing RCA: 2
- Incidents missing preventive action: 35
- No direct site-explicit ticket correlations matched confirmed incidents
- No incident-to-Zabbix timeline correlations matched the current exports
- Sites without confirmed master-data mapping: 14
- Unconfirmed master-data rows ignored as facts: 102
