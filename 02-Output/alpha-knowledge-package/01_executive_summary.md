# Executive Summary

## Deterministic KPIs

- Confirmed incidents: `52`
- Raw Zabbix alerts before grouping: `5199`
- Alert patterns after grouping: `365`
- Operational stories: `417`
- Unique tickets: `2681`
- Issue-report comment rows: `9525`
- Ticket monthly partitions: `3`

## Operational Story Coverage

- Confirmed-incident stories: `52`
- Monitoring-signal stories: `365`
- Signals related to confirmed incidents: `2`
- Signals time-aligned as context only: `3`
- Signals with direct user-impact evidence: `37`
- Signals needing noise or threshold review: `165`
- Unconfirmed monitoring signals: `158`

## Confirmed Incident Responsibility Classification

- `ISP`: `42`
- `INHOUSE`: `3`
- `EXTERNAL`: `1`
- `UNKNOWN`: `6`

## Confirmed Incident User-Impact Evidence

- `CONFIRMED`: `2`
- `POTENTIAL_IMPACT`: `5`
- `NO_DIRECT_EVIDENCE`: `45`

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

- `ALP-079F1ABCD016` VNMSNT-UPSF2201 | apc ups: unacceptable input frequency (out of range <value> for <value>): `347` raw alerts
- `ALP-7B851AF85826` VNMCPL-VSSPM03 | git http monitoring: `321` raw alerts
- `ALP-1DA83526E8C0` VNMSNT-VSSPM02 | git http monitoring: `307` raw alerts
- `ALP-E08CEB52B684` VNMCPL-VSSPM02 | git http monitoring: `301` raw alerts
- `ALP-22F4B209BB36` VNMSGN-VSEMS01 | git http monitoring: `292` raw alerts
- `ALP-8C45EBECE8B9` VNMSNT-VSSPM01 | git http monitoring: `289` raw alerts
- `ALP-9D95052D0965` VNMCPL-VSSPM04 | git http monitoring: `289` raw alerts
- `ALP-77CAA12D786F` VNMSGN-VSSPM02 | git http monitoring: `284` raw alerts
- `ALP-FE28092FA2A4` VNMSGN-VSSPM03 | git http monitoring: `282` raw alerts
- `ALP-557802E2665D` VNMSNT-VSSPM03 | git http monitoring: `248` raw alerts
- `ALP-551CCB8820FE` VNMSNT-VSEMS01 | git http monitoring: `228` raw alerts
- `ALP-550ED7DB3F47` VNMSGN-VSSPM01 | git http monitoring: `204` raw alerts
- `ALP-460C038618E4` VNMCPL-VSSPM01 | git http monitoring: `164` raw alerts
- `ALP-80599BC38B81` VNMSNT-VSSPM04 | git http monitoring: `155` raw alerts
- `ALP-AE10DD3DBB85` VNMRVF-UPS01 | apc ups: unacceptable input frequency (out of range <value> for <value>): `55` raw alerts
- `ALP-E7E97D0E219A` VNMMSH-PNSSW01 | interface gi1/0/17(2f-d29): link down: `44` raw alerts
- `ALP-46174DEDA3A4` VNMRVF-UPS02 | apc ups: unacceptable input frequency (out of range <value> for <value>): `42` raw alerts
- `ALP-B1488C926411` VNMMSH-VSSPM01 | linux: load average is too high (per cpu load over 0.75 for <value>): `41` raw alerts
- `ALP-D0FCFBCBA8AA` VNMMS2-NetNam-spx.shopee.vn | unavailable by icmp ping: `38` raw alerts
- `ALP-17B01F3BB308` VNMMBD-NETNAM-spx.shopee.vn | unavailable by icmp ping: `26` raw alerts
