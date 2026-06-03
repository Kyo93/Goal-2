# Executive Summary

## Deterministic KPIs

- Confirmed incidents: `52`
- Raw Zabbix alerts before grouping: `1000`
- Alert patterns after grouping: `76`
- Operational stories: `128`
- Unique tickets: `923`
- Issue-report comment rows: `2652`

## Operational Story Coverage

- Confirmed-incident stories: `52`
- Monitoring-signal stories: `76`
- Signals related to confirmed incidents: `0`
- Signals with direct user-impact evidence: `0`
- Signals needing noise or threshold review: `37`
- Unconfirmed monitoring signals: `39`

## Confirmed Incident Responsibility Classification

- `ISP`: `42`
- `INHOUSE`: `3`
- `EXTERNAL`: `1`
- `UNKNOWN`: `6`

## Confirmed Incident User-Impact Evidence

- `CONFIRMED`: `0`
- `ESTIMATED`: `5`
- `NO_EVIDENCE`: `47`

## Top Incident Recurrence Patterns

- `REC-C20AAAEB5882` MS2 | VNPT | High latency: `16` confirmed incidents
- `REC-71D845EC848B` XAS | CMC | Fiber optic cable failure: `4` confirmed incidents
- `REC-5D2EF81B54EB` MSB | VNPT | High latency: `3` confirmed incidents
- `REC-18D19523524A` MSB | FPT | Others: `2` confirmed incidents
- `REC-73E7E72ECD1B` MS2 | VNPT | Packet loss: `2` confirmed incidents
- `REC-C1DB9B82BE18` SWS | FPT | Fiber optic cable failure: `2` confirmed incidents
- `REC-C78CA8A62DC3` XAS | FPT | Fiber optic cable failure: `2` confirmed incidents
- `REC-DBB68D47F06F` SPV-Mocap | FPT | Others: `2` confirmed incidents
- `REC-083ECC631E49` SWS | FPT | Total outage: `1` confirmed incidents
- `REC-194DBD113F3F` MS2 | VNPT | Fiber optic cable failure: `1` confirmed incidents
- `REC-195A558F4A80` MS2 | FPT | Intermittent connectivity: `1` confirmed incidents
- `REC-2A02490A6900` CCW | VNPT | Others: `1` confirmed incidents
- `REC-4AC18D0EACE9` MS2 | VNPT | Bandwidth degradation: `1` confirmed incidents
- `REC-51667705957F` CTW | VNPT | Fiber optic cable failure: `1` confirmed incidents
- `REC-595B258EF8B2` WBN | FPT | Bandwidth degradation: `1` confirmed incidents
- `REC-64F6DA5CDA8A` MS2 | NETNAM | Fiber optic cable failure: `1` confirmed incidents
- `REC-6D743EAD6A3B` MBD | FPT | Fiber optic cable failure: `1` confirmed incidents
- `REC-705AF5886130` SNT | FPT | High latency: `1` confirmed incidents
- `REC-834ECCE34E95` CCW | VNPT | Fiber optic cable failure: `1` confirmed incidents
- `REC-8607728E784F` MDN | FPT | Fiber optic cable failure: `1` confirmed incidents

## High-Volume Alert Patterns

- `ALP-86E60C0C5C83` VNMCCW-PNWSW01 | fpt download gi2/0/3><value>,current:<value> mbps: `171` raw alerts
- `ALP-8251DC672F11` VNMCCW-PNASW011 | switch 1 - inlet temp sensor, green : temperature is above warning threshold: >50: `109` raw alerts
- `ALP-B7EAE4BAAD66` VNMCCW-PNASW05 | switch 1 - inlet temp sensor, green : temperature is above warning threshold: >50: `79` raw alerts
- `ALP-079F1ABCD016` VNMSNT-UPSF2201 | apc ups: unacceptable input frequency (out of range <value> for <value>): `70` raw alerts
- `ALP-810793E3F806` VNMCCW-PNASW04 | switch 2 - inlet temp sensor, green : temperature is above warning threshold: >50: `70` raw alerts
- `ALP-24CD7EE7CAA3` VNMCCW-PNASW04 | switch 3 - inlet temp sensor, green : temperature is above warning threshold: >50: `60` raw alerts
- `ALP-6725C5E8CE6D` VNMCCW-PNWSW01 | fpt upload gi2/0/3><value>,current:<value> mbps: `55` raw alerts
- `ALP-DDE7801896DE` VNMCCW-PNWSW01 | vnpt download gi1/0/1><value>,current:<value> mbps: `41` raw alerts
- `ALP-FA12954E19C4` VNMCCW-PNWSW01 | vnpt upload gi1/0/1><value>,current:<value> mbps: `29` raw alerts
- `ALP-DBDD4F005911` VNMCCW-PNASW11 | switch 2 - inlet temp sensor, green : temperature is above warning threshold: >50: `26` raw alerts
- `ALP-901B0D90D8D2` VNMCCW-PNWLC01 | s-retail-pda-number of users: 251: `23` raw alerts
- `ALP-461D468B1691` VNMCPL-FPT-Google | high icmp ping response time: `22` raw alerts
- `ALP-18D37040131C` VNMCPL-GNL-Google | high icmp ping response time: `21` raw alerts
- `ALP-667DFE8635E4` VNMCPL-NETNAM1-Google | high icmp ping response time: `21` raw alerts
- `ALP-74CBD0380FB3` VNMCCW-PNASW0202 | switch 1 - inlet temp sensor, green : temperature is above warning threshold: >50: `21` raw alerts
- `ALP-7C40C8ED034D` VNMCPL-NETNAM2-Google | high icmp ping response time: `20` raw alerts
- `ALP-BAE939D95D9C` VNMCCW-PNASW04 | switch 1 - inlet temp sensor, green : temperature is above warning threshold: >50: `17` raw alerts
- `ALP-29C13EBF308E` VNMCCW-PNASW05 | switch 2 - inlet temp sensor, green : temperature is above warning threshold: >50: `14` raw alerts
- `ALP-7C1A2BB86139` VNMCCW-PNASW11 | switch 1 - inlet temp sensor, green : temperature is above warning threshold: >50: `11` raw alerts
- `ALP-AE10DD3DBB85` VNMRVF-UPS01 | apc ups: unacceptable input frequency (out of range <value> for <value>): `10` raw alerts
