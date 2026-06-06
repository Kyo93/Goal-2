# Executive Summary

## Deterministic KPIs

- Confirmed incidents: `52`
- Raw Zabbix alerts before grouping: `10425`
- Alert patterns after grouping: `352`
- Operational stories: `404`
- Unique tickets: `923`
- Issue-report comment rows: `2652`

## Operational Story Coverage

- Confirmed-incident stories: `52`
- Monitoring-signal stories: `352`
- Signals related to confirmed incidents: `1`
- Signals time-aligned as context only: `19`
- Signals with direct user-impact evidence: `4`
- Signals needing noise or threshold review: `232`
- Unconfirmed monitoring signals: `96`

## Confirmed Incident Responsibility Classification

- `ISP`: `42`
- `INHOUSE`: `3`
- `EXTERNAL`: `1`
- `UNKNOWN`: `6`

## Confirmed Incident User-Impact Evidence

- `CONFIRMED`: `0`
- `POTENTIAL_IMPACT`: `5`
- `NO_DIRECT_EVIDENCE`: `47`

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

- `ALP-24B71D258D3E` VNMMSH-VSDHC01 | windows: high cpu utilization (over 90% for <value>): `1525` raw alerts
- `ALP-079F1ABCD016` VNMSNT-UPSF2201 | apc ups: unacceptable input frequency (out of range <value> for <value>): `536` raw alerts
- `ALP-8C45EBECE8B9` VNMSNT-VSSPM01 | git http monitoring: `521` raw alerts
- `ALP-9D95052D0965` VNMCPL-VSSPM04 | git http monitoring: `499` raw alerts
- `ALP-77CAA12D786F` VNMSGN-VSSPM02 | git http monitoring: `494` raw alerts
- `ALP-7B851AF85826` VNMCPL-VSSPM03 | git http monitoring: `483` raw alerts
- `ALP-E08CEB52B684` VNMCPL-VSSPM02 | git http monitoring: `472` raw alerts
- `ALP-1DA83526E8C0` VNMSNT-VSSPM02 | git http monitoring: `468` raw alerts
- `ALP-22F4B209BB36` VNMSGN-VSEMS01 | git http monitoring: `460` raw alerts
- `ALP-FE28092FA2A4` VNMSGN-VSSPM03 | git http monitoring: `455` raw alerts
- `ALP-551CCB8820FE` VNMSNT-VSEMS01 | git http monitoring: `413` raw alerts
- `ALP-557802E2665D` VNMSNT-VSSPM03 | git http monitoring: `389` raw alerts
- `ALP-550ED7DB3F47` VNMSGN-VSSPM01 | git http monitoring: `347` raw alerts
- `ALP-460C038618E4` VNMCPL-VSSPM01 | git http monitoring: `265` raw alerts
- `ALP-80599BC38B81` VNMSNT-VSSPM04 | git http monitoring: `232` raw alerts
- `ALP-B1488C926411` VNMMSH-VSSPM01 | linux: load average is too high (per cpu load over 0.75 for <value>): `156` raw alerts
- `ALP-F5572970729B` VNMMDN-VSSPM01 | http monitoring: `123` raw alerts
- `ALP-A0947B93EBA0` VNMMDN-VSEMS01 | http monitoring: `122` raw alerts
- `ALP-B8C29BDC1FFA` VNMMDN-VSSPM02 | http monitoring: `101` raw alerts
- `ALP-AE10DD3DBB85` VNMRVF-UPS01 | apc ups: unacceptable input frequency (out of range <value> for <value>): `67` raw alerts
