# Raw Zabbix Alert Patterns

> Alert pattern is not a confirmed incident.

## Site Pattern Family Summary

> Use this section first for Zabbix-alert questions. Individual alert patterns are evidence details, not the primary answer shape.

### CCW | Network reachability

- Pattern count: `8`
- Raw alert count across full export: `12`
- Investigation priorities: `HIGH, MEDIUM`
- Sample signatures: `cisco ios: unavailable by icmp ping, unavailable by icmp ping, zabbix proxy: utilization of icmp pinger processes over 75%`
- Sample hosts: `VNMCCW-FPT-GoogleDNS, VNMCCW-FPT-wms.ssc.shopee.vn, VNMCCW-PE-FPT-58.186.223.217, VNMCCW-PE-VNPT-14.238.87.209, VNMCCW-PE-VNPT-wms.ssc.shopee.vn, VNMCCW-PNASW04, VNMCCW-VNPT-GoogleDNS, VNMCCW-VSSPM02`
- Example alert pattern IDs: `ALP-169E6406F728, ALP-2627FC49476B, ALP-A7A009EBB0BA, ALP-D22E642D2402, ALP-A035897B33D7`

### CCW | Other

- Pattern count: `7`
- Raw alert count across full export: `16`
- Investigation priorities: `LOW`
- Sample signatures: `interface gi1/0/1(vnpt): link down, interface gi2/0/3(fpt): link down, interface gi2/0/9(backoffice): link down, interface po18(hub-w4): link down, interface te1/1/1(vnpt): link down, interface te1/1/2(hub-w4): link down, interface te2/1/2(hub-w4): link down`
- Sample hosts: `VNMCCW-PNASW-OFFICE, VNMCCW-PNCSW01, VNMCCW-PNWSW01`
- Example alert pattern IDs: `ALP-FE978C1E0C20, ALP-19E27B689C58, ALP-4B2D9244DF77, ALP-EF2FC71AF04A, ALP-37ECD17812E6, ALP-6330A778B101, ALP-A4089FD15772`

### CCW | HTTP monitoring

- Pattern count: `3`
- Raw alert count across full export: `11`
- Investigation priorities: `LOW`
- Sample signatures: `http monitoring`
- Sample hosts: `VNMCCW-VSEMS01, VNMCCW-VSSPM01, VNMCCW-VSSPM02`
- Example alert pattern IDs: `ALP-6D1757618413, ALP-7A23D4CE212F, ALP-8C989B803A73`

### CPL | Network reachability

- Pattern count: `12`
- Raw alert count across full export: `16`
- Investigation priorities: `HIGH`
- Sample signatures: `cisco ios: unavailable by icmp ping, unavailable by icmp ping, vnmcpl-pnwfw01 is down!, vnmcpl-pnwfw02 is down!`
- Sample hosts: `VNMCPL-FPT-GoogleDNS, VNMCPL-PNASW0401, VNMCPL-PNASW0402, VNMCPL-PNASW0501, VNMCPL-PNASW0502, VNMCPL-PNASW0503, VNMCPL-PNASW0504, VNMCPL-PNASW0601, VNMCPL-PNSSW01, VNMCPL-PNWFW01, VNMCPL-PNWFW02, VNMCPL-VTHL-GoogleDNS`
- Example alert pattern IDs: `ALP-AD0FEAB4CF54, ALP-BF6FF8E976BE, ALP-1D167D124B85, ALP-685FDC71F87F, ALP-8BA568D15E14, ALP-93A5CD8B721E, ALP-AC5823A356F9, ALP-BB3EEB369423`

### CPL | HTTP monitoring

- Pattern count: `21`
- Raw alert count across full export: `1167`
- Investigation priorities: `MEDIUM, LOW`
- Sample signatures: `confluence http monitoring, git http monitoring, google http monitoring, hris http monitoring, itcenter http monitoring, jira http monitoring, shopee confluence http monitoring`
- Sample hosts: `VNMCPL-VSSPM01, VNMCPL-VSSPM02, VNMCPL-VSSPM03, VNMCPL-VSSPM04`
- Example alert pattern IDs: `ALP-7B851AF85826, ALP-E08CEB52B684, ALP-9D95052D0965, ALP-460C038618E4, ALP-6F2F9F50A046, ALP-744043C0F1DE, ALP-D05FEF044AE4, ALP-FDC327088884`

### CPL | Other

- Pattern count: `13`
- Raw alert count across full export: `13`
- Investigation priorities: `LOW`
- Sample signatures: `interface gi1/0/1(host<value>-gi1-vmnic0): link down, interface gi1/0/2(host<value>-gi2-vmnic0): link down, interface gi1/0/3(host<value>-gi6): link down, interface gi1/0/4(vmotion): link down, interface gi1/0/47(host8o-idrac): link down, interface gi2/0/1(host<value>-gi2-vmnic1): link down, interface gi2/0/2(host<value>-gi2-vmnic1): link down, interface gi2/0/3(host<value>-gi6): link down, interface gi2/0/4(vmotion): link down, interface gi2/0/47(host<value>-idrac): link down`
- Sample hosts: `VNMCPL-PNSSW01, VNMCPL-PNWSW01`
- Example alert pattern IDs: `ALP-5A159D9F292E, ALP-90723BD1730B, ALP-A9E721DBF400, ALP-B331868ACD35, ALP-BACB26822D0F, ALP-C6A753AA8DAF, ALP-DDAF4871FEF9, ALP-E45DD97FFD35`

### CPL | Zabbix agent/active check

- Pattern count: `2`
- Raw alert count across full export: `5`
- Investigation priorities: `LOW`
- Sample signatures: `windows: active checks are not available`
- Sample hosts: `VNMCPL-VSDHC01, VNMCPL-VSDHC02`
- Example alert pattern IDs: `ALP-981B0724F60D, ALP-47027752FDAD`

### CPL | Host restart/uptime

- Pattern count: `2`
- Raw alert count across full export: `4`
- Investigation priorities: `LOW`
- Sample signatures: `windows: host has been restarted (uptime < <value>)`
- Sample hosts: `VNMCPL-VSDHC01, VNMCPL-VSDHC02`
- Example alert pattern IDs: `ALP-C3F11E8E54C2, ALP-A37DF63F13A8`

### MBD | Network reachability

- Pattern count: `4`
- Raw alert count across full export: `31`
- Investigation priorities: `HIGH, MEDIUM`
- Sample signatures: `unavailable by icmp ping`
- Sample hosts: `VNMMBD-FPT-FMS-143.92.82.164, VNMMBD-NETNAM-FMS-143.92.82.164, VNMMBD-NETNAM-spx.shopee.vn, VNMMBD-PE-FPT-42.116.48.97`
- Example alert pattern IDs: `ALP-17B01F3BB308, ALP-300E3E1681E3`

### MBD | Power/UPS

- Pattern count: `2`
- Raw alert count across full export: `4`
- Investigation priorities: `HIGH`
- Sample signatures: `apc ups: ups is on battery`
- Sample hosts: `VNMMBD-UPS01, VNMMBD-UPS02`
- Example alert pattern IDs: `ALP-8CD6ED07FBD2, ALP-AA4ADE38C413`

### MBD | HTTP monitoring

- Pattern count: `4`
- Raw alert count across full export: `10`
- Investigation priorities: `LOW`
- Sample signatures: `http monitoring`
- Sample hosts: `VNMMBD-VSEMS01, VNMMBD-VSSPM01, VNMMBD-VSSPM02, VNMMBD-VSSPM03`
- Example alert pattern IDs: `ALP-30B215136C84, ALP-8022BF11F7B8, ALP-8C1FAECDB82B, ALP-C8F733B66B3A`

### MBD | Other

- Pattern count: `7`
- Raw alert count across full export: `9`
- Investigation priorities: `LOW`
- Sample signatures: `dell idrac: nic [nic.embedded.1-1-1/ac:b4:80:4f:b9:cc]: link down, interface te2/1/8(ul-fpt): link down, interface xgigabitethernet1/0/1(): link down, interface xgigabitethernet1/0/17(vnmmbd-pnasw17): link down, interface xgigabitethernet1/0/18(vnmmbd-pnasw18): link down, interface xgigabitethernet1/0/23(asm-b): link down, interface xgigabitethernet1/0/47(vnmmbd-pndsw01): link down`
- Sample hosts: `VNMMBD-PNCSW01, VNMMBD-PNDSW01-B, VNMMBD-PNWSW01, VNMMBD-psesx01`
- Example alert pattern IDs: `ALP-8D8DBC00B238, ALP-E4A386D887F2, ALP-031BE4B5C2DB, ALP-40578C2A8D55, ALP-42399D834774, ALP-42F4BF748BE6, ALP-EC47E5EBE854`

### MBD | Host restart/uptime

- Pattern count: `4`
- Raw alert count across full export: `4`
- Investigation priorities: `LOW`
- Sample signatures: `windows: host has been restarted (uptime < <value>)`
- Sample hosts: `VNMMBD-PSSJP1, VNMMBD-PSSJP2, VNMMBD-VSDHC01, VNMMBD-VSDHC02`
- Example alert pattern IDs: `ALP-32F434F90DB7, ALP-3899CD2333EC, ALP-90793ED28AF7, ALP-D05553CC376F`

### MBD | Zabbix agent/active check

- Pattern count: `4`
- Raw alert count across full export: `4`
- Investigation priorities: `LOW`
- Sample signatures: `windows: active checks are not available, windows: zabbix agent is not available (or nodata for <value>)`
- Sample hosts: `VNMMBD-VSDHC02, VNMMBD-VSSJC1`
- Example alert pattern IDs: `ALP-4B29B0B74364, ALP-6E01E457377C, ALP-C031A95EC809, ALP-F00DBD58B8BB`

### MDN | Power/UPS

- Pattern count: `2`
- Raw alert count across full export: `2`
- Investigation priorities: `HIGH`
- Sample signatures: `apc ups: ups is on battery`
- Sample hosts: `VNMMDN-UPS01, VNMMDN-UPS02`
- Example alert pattern IDs: `ALP-2CDF8339EE29, ALP-CFD7410A0332`

### MDN | Network reachability

- Pattern count: `3`
- Raw alert count across full export: `3`
- Investigation priorities: `MEDIUM`
- Sample signatures: `unavailable by icmp ping`
- Sample hosts: `VNMMDN-FPT-210.245.97.132, VNMMDN-FPT-Google, VNMMDN-Netnam-FMS-Google`
- Example alert pattern IDs: `ALP-556C5581035F, ALP-6B66EDD4D5A6, ALP-9E76E02BF1B3`

### MDN | HTTP monitoring

- Pattern count: `3`
- Raw alert count across full export: `11`
- Investigation priorities: `LOW`
- Sample signatures: `http monitoring`
- Sample hosts: `VNMMDN-VSEMS01, VNMMDN-VSSPM01, VNMMDN-VSSPM02`
- Example alert pattern IDs: `ALP-F5572970729B, ALP-A0947B93EBA0, ALP-B8C29BDC1FFA`

### MDN | Host restart/uptime

- Pattern count: `3`
- Raw alert count across full export: `6`
- Investigation priorities: `LOW`
- Sample signatures: `windows: host has been restarted (uptime < <value>)`
- Sample hosts: `VNMMDN-PSSJP1, VNMMDN-VSDHC01, VNMMDN-VSDHC02`
- Example alert pattern IDs: `ALP-7637E316BAF5, ALP-6A54DDB78966, ALP-E97AD6C8AC63`

### MDN | Other

- Pattern count: `1`
- Raw alert count across full export: `1`
- Investigation priorities: `LOW`
- Sample signatures: `interface 50:00:e0:4f:9b:80/1/c9300x-nm-8y/1: link down`
- Sample hosts: `VNMMDN-PNCSW01-1-2`
- Example alert pattern IDs: `ALP-95C8531458B4`

### MS2 | Network reachability

- Pattern count: `9`
- Raw alert count across full export: `97`
- Investigation priorities: `HIGH, MEDIUM`
- Sample signatures: `unavailable by icmp ping`
- Sample hosts: `VNMMS2-FPT-FMS-143.92.82.164, VNMMS2-FPT-FMS-143.92.88.13, VNMMS2-FPT-FMS-34.8.101.13, VNMMS2-FPT-FMS-45.119.218.130, VNMMS2-FPT-FMS-45.119.218.141, VNMMS2-FPT-Google, VNMMS2-FPT-GoogleDNS, VNMMS2-NetNam-spx.shopee.vn, VNMMS2-VNPT-GoogleDNS`
- Example alert pattern IDs: `ALP-D0FCFBCBA8AA, ALP-CAD1A664558A, ALP-1CBDABDA59C1, ALP-50D1D2232E0A, ALP-EB009B8995C2`

### MS2 | HTTP monitoring

- Pattern count: `5`
- Raw alert count across full export: `16`
- Investigation priorities: `LOW`
- Sample signatures: `http monitoring`
- Sample hosts: `VNMMS2-VSEMS01, VNMMS2-VSSPM01, VNMMS2-VSSPM02, VNMMS2-VSSPM03, VNMMS2-VSSPM04`
- Example alert pattern IDs: `ALP-7FEC14B7A1CA, ALP-13B43D07AA25, ALP-F21C496048BA, ALP-4C656B6E6B0E, ALP-8343732F4E8F`

### MS2 | Host restart/uptime

- Pattern count: `4`
- Raw alert count across full export: `4`
- Investigation priorities: `LOW`
- Sample signatures: `windows: host has been restarted (uptime < <value>)`
- Sample hosts: `VNMMS2-PSSJP1, VNMMS2-PSSJP2, VNMMS2-VSDHC01, VNMMS2-VSDHC02`
- Example alert pattern IDs: `ALP-2BE3251B74A9, ALP-8502BDAE29F6, ALP-DDC89EABBC6F, ALP-F78AB4D74642`

### MS2 | Other

- Pattern count: `1`
- Raw alert count across full export: `1`
- Investigation priorities: `LOW`
- Sample signatures: `interface xgigabitethernet0/0/22(*** asm ***): link down`
- Sample hosts: `VNMMS2-PNCSW01`
- Example alert pattern IDs: `ALP-DDC053EAD407`

### MSB | Network reachability

- Pattern count: `19`
- Raw alert count across full export: `73`
- Investigation priorities: `HIGH, MEDIUM`
- Sample signatures: `cisco ios: unavailable by icmp ping, unavailable by icmp ping, zabbix proxy: utilization of icmp pinger processes over 75%`
- Sample hosts: `VNMMSB-FPT-FMS-143.92.82.164, VNMMSB-FPT-FMS-143.92.88.13, VNMMSB-FPT-FMS-34.8.101.13, VNMMSB-FPT-FMS-45.119.218.130, VNMMSB-FPT-FMS-45.119.218.141, VNMMSB-FPT-Google, VNMMSB-FPT-GoogleDNS, VNMMSB-FPT-spx.shopee.vn, VNMMSB-PE-FPT-42.115.45.57, VNMMSB-PNASW-Hub22, VNMMSB-VNPT-FMS-45.119.218.130, VNMMSB-VNPT-FTTH-143.92.82.164`
- Example alert pattern IDs: `ALP-E2A7575F1806, ALP-9966AD21D215, ALP-C6ED613558DD, ALP-740A41E15833`

### MSB | Other

- Pattern count: `14`
- Raw alert count across full export: `58`
- Investigation priorities: `LOW`
- Sample signatures: `interface eth-trunk35(sw30b-hub12-poe-sw): link down, interface eth-trunk4(san3-bond): link down, interface gigabitethernet0/0/25(ap-lab2-server): link down, interface gigabitethernet0/0/26(ap-lab1-server): link down, interface gigabitethernet0/0/27(w-testing-802.1x): link down, interface gigabitethernet0/0/28(thangdv-wifi-test): link down, interface gigabitethernet1/0/27(): link down, interface gigabitethernet1/0/28(): link down, interface te1/1/7(fpt<value>/<value>-uplink): link down, interface te2/1/7(vnpt-ftth-<value>/<value>-uplink): link down`
- Sample hosts: `VNMMSB-PNCSW01, VNMMSB-PNSSW01, VNMMSB-PNWSW01, VNMMSB-VSCDC01, VNMMSB-VSCDC02`
- Example alert pattern IDs: `ALP-2D3FBB654BE3, ALP-4BF58F585699, ALP-E3F1CEF16485, ALP-6C309587E8D5, ALP-176B73406A1D, ALP-3F151F71EFF2, ALP-408776FCDC35, ALP-EC07B63B6BF1`

### MSB | Host restart/uptime

- Pattern count: `7`
- Raw alert count across full export: `9`
- Investigation priorities: `LOW`
- Sample signatures: `windows: host has been restarted (uptime < <value>)`
- Sample hosts: `VNMMSB-PSSJP1, VNMMSB-PSSJP2, VNMMSB-VSCDC01, VNMMSB-VSCDC02, VNMMSB-VSDHC01, VNMMSB-VSDHC02, VNMMSB-VSNPS01`
- Example alert pattern IDs: `ALP-12E1592973B6, ALP-FCB38E8F143B, ALP-1ACCDDA4E22B, ALP-6F75CFE0BFF3, ALP-943BE1CC9684, ALP-C0D0547A5EB2, ALP-D3800D122BE2`

### MSB | HTTP monitoring

- Pattern count: `7`
- Raw alert count across full export: `8`
- Investigation priorities: `LOW`
- Sample signatures: `google http monitoring, hris http monitoring, itcenter http monitoring`
- Sample hosts: `VNMMSB-VSSPM01, VNMMSB-VSSPM02, VNMMSB-VSSPM03`
- Example alert pattern IDs: `ALP-64B121F6A433, ALP-3A3CD95E1262, ALP-784607BD3933, ALP-83F3E80812B5, ALP-A090C47934DD, ALP-ADB14EE9325B, ALP-C57961CC104D`

### MSB | Zabbix agent/active check

- Pattern count: `6`
- Raw alert count across full export: `6`
- Investigation priorities: `LOW`
- Sample signatures: `windows: active checks are not available, windows: zabbix agent is not available (or nodata for <value>)`
- Sample hosts: `VNMMSB-PSSJP2, VNMMSB-VSCDC01, VNMMSB-VSCDC02, VNMMSB-VSDHC02`
- Example alert pattern IDs: `ALP-5081189920F7, ALP-9D1DC3A5A925, ALP-B0472F3ECDF7, ALP-DC34A037CC91, ALP-EE35CFAF0367, ALP-F6D0BF16C98C`

### MSH | HTTP monitoring

- Pattern count: `11`
- Raw alert count across full export: `54`
- Investigation priorities: `MEDIUM, LOW`
- Sample signatures: `google http monitoring, hris http monitoring, itcenter http monitoring, jira http monitoring, shopee confluence http monitoring, space http monitoring`
- Sample hosts: `VNMMSH-VSSPM01, VNMMSH-VSSPM02`
- Example alert pattern IDs: `ALP-8E6AC4150C80, ALP-FC8A681995B1, ALP-3EB6409BA309, ALP-01E4CBEDDEBE, ALP-9E2AEE42C23D, ALP-BB890BC9C9F8, ALP-5B5E5BD02F39, ALP-7F7A2D2BCBD0`

### MSH | Other

- Pattern count: `22`
- Raw alert count across full export: `175`
- Investigation priorities: `LOW`
- Sample signatures: `interface gi1/0/13(2f-d25): link down, interface gi1/0/14(2f-d26): link down, interface gi1/0/15(2f-d27): link down, interface gi1/0/16(2f-d28): link down, interface gi1/0/17(2f-d29): link down, interface gi1/0/22(2f-d34): link down, interface gi1/0/29(wired-users): link down, interface gi1/0/4(wired-users): link down, interface gi1/0/8(): link down, interface gi1/0/9(): link down`
- Sample hosts: `VNMMSH-PNCSW01, VNMMSH-PNSSW01, VNMMSH-PNWSW01, VNMMSH-VSDHC02, VNMMSH-VSSPM01`
- Example alert pattern IDs: `ALP-E7E97D0E219A, ALP-B1488C926411, ALP-9449A45503C7, ALP-BC88B7D92FB9, ALP-0EAC2ABF80AC, ALP-AD5AA6FC1FB8, ALP-FDF85018772E, ALP-788ECF082C30`

### MSH | Zabbix agent/active check

- Pattern count: `3`
- Raw alert count across full export: `6`
- Investigation priorities: `LOW`
- Sample signatures: `windows: active checks are not available, windows: zabbix agent is not available (or nodata for <value>)`
- Sample hosts: `VNMMSH-VSDHC01, VNMMSH-VSDHC02`
- Example alert pattern IDs: `ALP-63A681653D3E, ALP-C8D9E49F883D, ALP-E6D0338FF897`

### MSH | Host restart/uptime

- Pattern count: `2`
- Raw alert count across full export: `4`
- Investigation priorities: `LOW`
- Sample signatures: `windows: host has been restarted (uptime < <value>)`
- Sample hosts: `VNMMSH-VSDHC01, VNMMSH-VSDHC02`
- Example alert pattern IDs: `ALP-C380821D118B, ALP-A0899C9F3685`

### RVF | Power/UPS

- Pattern count: `2`
- Raw alert count across full export: `97`
- Investigation priorities: `HIGH`
- Sample signatures: `apc ups: unacceptable input frequency (out of range <value> for <value>)`
- Sample hosts: `VNMRVF-UPS01, VNMRVF-UPS02`
- Example alert pattern IDs: `ALP-AE10DD3DBB85, ALP-46174DEDA3A4`

### RVF | HTTP monitoring

- Pattern count: `19`
- Raw alert count across full export: `102`
- Investigation priorities: `MEDIUM, LOW`
- Sample signatures: `confluence http monitoring, google http monitoring, hris http monitoring, itcenter http monitoring, jira http monitoring, shopee confluence http monitoring`
- Sample hosts: `VNMRVF-VSZABPRX-GNL1, VNMRVF-VSZABPRX-ISP1, VNMRVF-VSZABPRX-ISP2, VNMRVF-VSZABPRX-ISP3`
- Example alert pattern IDs: `ALP-0956650F5A4C, ALP-43F27E19DD21, ALP-968676F48AAF, ALP-D8563BF0B2A5, ALP-43AFF3060676, ALP-484B720DB953, ALP-7D5EB2CD1DDF, ALP-A8B5D5531BA6`

### RVF | Host restart/uptime

- Pattern count: `2`
- Raw alert count across full export: `2`
- Investigation priorities: `LOW`
- Sample signatures: `windows: host has been restarted (uptime < <value>)`
- Sample hosts: `VNMRVF-VSDHC01, VNMRVF-VSDHC02`
- Example alert pattern IDs: `ALP-2EEB6A045E46, ALP-746BFE15BC81`

### SGN | HTTP monitoring

- Pattern count: `23`
- Raw alert count across full export: `1169`
- Investigation priorities: `MEDIUM, LOW`
- Sample signatures: `git http monitoring, google http monitoring, hris http monitoring, itcenter http monitoring, jira http monitoring, shopee confluence http monitoring, space http monitoring`
- Sample hosts: `VNMSGN-VSEMS01, VNMSGN-VSSPM01, VNMSGN-VSSPM02, VNMSGN-VSSPM03`
- Example alert pattern IDs: `ALP-22F4B209BB36, ALP-77CAA12D786F, ALP-FE28092FA2A4, ALP-550ED7DB3F47, ALP-161D4179FDA9, ALP-43E03B32158E, ALP-5BA58770C8AF, ALP-DB00D177E05F`

### SGN | Other

- Pattern count: `12`
- Raw alert count across full export: `67`
- Investigation priorities: `LOW`
- Sample signatures: `interface gi1/0/11(data): link down, interface gi1/0/13(data): link down, interface gi1/0/14(data): link down, interface gi1/0/15(data): link down, interface gi1/0/16(data): link down, interface gi1/0/17(data): link down, interface gi1/0/18(data): link down, interface gi1/0/20(data): link down, interface gi1/0/24(data): link down, interface gi1/0/5(data): link down`
- Sample hosts: `VNMSGN-F24-Studio-SW01, VNMSGN-PNWSW2501`
- Example alert pattern IDs: `ALP-E508F0A30F14, ALP-A67C22A71598, ALP-3C94BCE98493, ALP-1A3F306FCB8F, ALP-115D48183243, ALP-8DB77EB6AD73, ALP-13C2484F33DF, ALP-C061A474B203`

### SGN | Host restart/uptime

- Pattern count: `2`
- Raw alert count across full export: `3`
- Investigation priorities: `LOW`
- Sample signatures: `windows: host has been restarted (uptime < <value>)`
- Sample hosts: `VNMSGN-VSDHC01, VNMSGN-VSDHC02`
- Example alert pattern IDs: `ALP-A1CD3F2D2972, ALP-E91C7BC7C5E8`

### SGN | Zabbix agent/active check

- Pattern count: `1`
- Raw alert count across full export: `1`
- Investigation priorities: `LOW`
- Sample signatures: `windows: active checks are not available`
- Sample hosts: `VNMSGN-VSDHC02`
- Example alert pattern IDs: `ALP-7A7AC21E2062`

### SNT | Power/UPS

- Pattern count: `12`
- Raw alert count across full export: `440`
- Investigation priorities: `HIGH`
- Sample signatures: `2: unacceptable phase 2 input voltage (out of range 197-243v for <value>), 3.1: battery has high temperature (over 55℃ for <value>), 3.2: battery has high temperature (over 55℃ for <value>), 3: unacceptable phase 3 input voltage (out of range 197-243v for <value>), apc ups: battery has high temperature (over 55℃ for <value>), apc ups: unacceptable input frequency (out of range <value> for <value>), apc ups: ups is hardware failure bypass, apc ups: ups is on battery, switch 2 - power supply b, normal: power supply is in critical state, switch 3 - power supply a, normal: power supply is in critical state`
- Sample hosts: `VNMSNT-PNASW0901, VNMSNT-PNASW0902, VNMSNT-UPSF2201`
- Example alert pattern IDs: `ALP-079F1ABCD016, ALP-AB3C1A209D93, ALP-5E69C4448C78, ALP-40F5382B2C17, ALP-ADA6C918C671, ALP-577879E16B1D, ALP-5DD89370D4CE, ALP-919D1DAA3ADF`

### SNT | Network reachability

- Pattern count: `4`
- Raw alert count across full export: `4`
- Investigation priorities: `HIGH`
- Sample signatures: `cisco ios: unavailable by icmp ping`
- Sample hosts: `VNMSNT-PNASW0801, VNMSNT-PNASW0802, VNMSNT-PNASW0803, VNMSNT-PNASW0804`
- Example alert pattern IDs: `ALP-773FF6B91B85, ALP-A24FE3830B4B, ALP-B259C1B104BD, ALP-B8846D1E4DB8`

### SNT | HTTP monitoring

- Pattern count: `29`
- Raw alert count across full export: `1376`
- Investigation priorities: `MEDIUM, LOW`
- Sample signatures: `confluence http monitoring, git http monitoring, google http monitoring, hris http monitoring, itcenter http monitoring, jira http monitoring, shopee confluence http monitoring, space http monitoring`
- Sample hosts: `VNMSNT-VSEMS01, VNMSNT-VSSPM01, VNMSNT-VSSPM02, VNMSNT-VSSPM03, VNMSNT-VSSPM04`
- Example alert pattern IDs: `ALP-1DA83526E8C0, ALP-8C45EBECE8B9, ALP-557802E2665D, ALP-551CCB8820FE, ALP-80599BC38B81, ALP-4C0ACA243192, ALP-7259165E30FF, ALP-B272469C4059`

### SNT | Other

- Pattern count: `13`
- Raw alert count across full export: `13`
- Investigation priorities: `LOW`
- Sample signatures: `interface gi1/0/34(cctv): link down, interface gi2/0/17(genesys): link down, interface po24(8data2): link down, interface po25(8poe1): link down, interface po26(8poe2): link down, interface te1/0/23(8data1): link down, interface te1/0/24(8data2): link down, interface te1/0/25(8poe1): link down, interface te1/0/26(8poe2): link down, interface te1/0/30(7poe2): link down`
- Sample hosts: `VNMSNT-PNCSW2201, VNMSNT-PNSSW2201, VNMSNT-PNWSW2201, VNMSNT-VSDHC01`
- Example alert pattern IDs: `ALP-0AD00BFAE5B7, ALP-0E065BD2D502, ALP-29F27FAA81CA, ALP-2CA2E82FFCE3, ALP-32DAF214489F, ALP-701EB4EAF3E4, ALP-93544488C14D, ALP-C8F1CFFBCC61`

### SNT | Host restart/uptime

- Pattern count: `2`
- Raw alert count across full export: `2`
- Investigation priorities: `LOW`
- Sample signatures: `windows: host has been restarted (uptime < <value>)`
- Sample hosts: `VNMSNT-VSDHC01, VNMSNT-VSDHC02`
- Example alert pattern IDs: `ALP-65018137D406, ALP-7A327195B442`

### SNT | Zabbix agent/active check

- Pattern count: `2`
- Raw alert count across full export: `2`
- Investigation priorities: `LOW`
- Sample signatures: `windows: active checks are not available, windows: zabbix agent is not available (or nodata for <value>)`
- Sample hosts: `VNMSNT-VSDHC01`
- Example alert pattern IDs: `ALP-591C77AE607B, ALP-86345183DF87`

### SWS | Power/UPS

- Pattern count: `2`
- Raw alert count across full export: `4`
- Investigation priorities: `HIGH`
- Sample signatures: `apc ups: ups is on battery`
- Sample hosts: `VNMSWS-UPS01, VNMSWS-UPS02`
- Example alert pattern IDs: `ALP-438E82AC906B, ALP-BEB9E5C2842C`

### SWS | Network reachability

- Pattern count: `1`
- Raw alert count across full export: `1`
- Investigation priorities: `HIGH`
- Sample signatures: `zabbix proxy: utilization of icmp pinger processes over 75%`
- Sample hosts: `VNMSWS-VSSPM01`
- Example alert pattern IDs: `ALP-A0A7C8335F8A`

### SWS | HTTP monitoring

- Pattern count: `1`
- Raw alert count across full export: `5`
- Investigation priorities: `LOW`
- Sample signatures: `http monitoring`
- Sample hosts: `VNMSWS-VSEMS01`
- Example alert pattern IDs: `ALP-F43B329C01A5`

### SWS | Host restart/uptime

- Pattern count: `4`
- Raw alert count across full export: `5`
- Investigation priorities: `LOW`
- Sample signatures: `windows: host has been restarted (uptime < <value>)`
- Sample hosts: `VNMSWS-PSSJP1, VNMSWS-PSSJP2, VNMSWS-VSDHC01, VNMSWS-VSDHC02`
- Example alert pattern IDs: `ALP-21A98CCEA4A6, ALP-13911D374776, ALP-6C98DB159A7E, ALP-C05AD23FBDDF`

### SWS | Other

- Pattern count: `2`
- Raw alert count across full export: `4`
- Investigation priorities: `LOW`
- Sample signatures: `interface ethernet1/10(): link down, interface twe2/0/4(ul-pa02): link down`
- Sample hosts: `VNMSWS-PNCSW01, VNMSWS-PNWFW02`
- Example alert pattern IDs: `ALP-9EC6DA7FB4A6, ALP-A68F358A138F`

### UNKNOWN | Host restart/uptime

- Pattern count: `2`
- Raw alert count across full export: `2`
- Investigation priorities: `LOW`
- Sample signatures: `windows: host has been restarted (uptime < <value>)`
- Sample hosts: `VNW3-VSDHC01, VNW3-VSDHC02`
- Example alert pattern IDs: `ALP-978DF6D26A6B, ALP-E89923DA4A76`

### WBN | HTTP monitoring

- Pattern count: `10`
- Raw alert count across full export: `52`
- Investigation priorities: `MEDIUM, LOW`
- Sample signatures: `google http monitoring, hris http monitoring, itcenter http monitoring, jira http monitoring, shopee confluence http monitoring`
- Sample hosts: `VNMWBN-VSSPM01, VNMWBN-VSSPM02`
- Example alert pattern IDs: `ALP-AB43BE0559B5, ALP-F49D6521EF17, ALP-7488F88C19DF, ALP-99E67BCA8B6A, ALP-E98E242414FE, ALP-FF594A117625, ALP-1B829EB90695, ALP-79E5CF0FEB8B`

### WBN | Other

- Pattern count: `2`
- Raw alert count across full export: `5`
- Investigation priorities: `LOW`
- Sample signatures: `interface gi2/1/4(fpt-300/<value>-uplink): link down, interface tunnel.36(to-cp-fpt): link down`
- Sample hosts: `VNMWBN-PNWFW01, VNMWBN-PNWSW01`
- Example alert pattern IDs: `ALP-6543D8B05E3C, ALP-FA0CAF592E23`

### WBN | Host restart/uptime

- Pattern count: `2`
- Raw alert count across full export: `2`
- Investigation priorities: `LOW`
- Sample signatures: `windows: host has been restarted (uptime < <value>)`
- Sample hosts: `VNMWBN-VSDHC01, VNMWBN-VSDHC02`
- Example alert pattern IDs: `ALP-2AB4588032FC, ALP-97B938A73B4B`

### WBN | Zabbix agent/active check

- Pattern count: `1`
- Raw alert count across full export: `1`
- Investigation priorities: `LOW`
- Sample signatures: `windows: active checks are not available`
- Sample hosts: `VNMWBN-VSDHC01`
- Example alert pattern IDs: `ALP-CCD676EF5C72`

## Individual Alert Patterns

## ALP-079F1ABCD016 | VNMSNT-UPSF2201

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `apc ups: unacceptable input frequency (out of range <value> for <value>)`
- Pattern family: `Power/UPS`
- Investigation priority: `HIGH`
- Why it matters: VNMSNT-UPSF2201 reported `apc ups: unacceptable input frequency (out of range <value> for <value>)`. This may indicate power/UPS instability and deserves facility or device-side verification.
- Raw alert count: `347`
- Resolved alerts: `347`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `power`
- Component: `power`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4392; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4387; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4368; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4343; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4342; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4152; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4142; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4030; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4009; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3995; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3876; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3871; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3865; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3844; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3840; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3806; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3792; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3791; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3788; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3785`
- Source reference count: `347`

## ALP-7B851AF85826 | VNMCPL-VSSPM03

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `git http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMCPL-VSSPM03 reported `git http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `321`
- Resolved alerts: `321`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4428; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4423; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4389; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4388; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4383; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4370; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4324; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4302; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4301; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4293; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4277; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4265; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4246; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4174; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4173; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4145; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4118; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4110; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4109; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4067`
- Source reference count: `321`

## ALP-1DA83526E8C0 | VNMSNT-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `git http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMSNT-VSSPM02 reported `git http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `307`
- Resolved alerts: `307`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4475; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4469; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4434; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4421; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4416; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4391; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4382; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4378; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4376; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4371; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4328; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4278; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4271; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4270; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4235; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4230; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4194; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4178; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4160; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4113`
- Source reference count: `307`

## ALP-E08CEB52B684 | VNMCPL-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `git http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMCPL-VSSPM02 reported `git http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `301`
- Resolved alerts: `301`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4467; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4438; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4412; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4377; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4369; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4311; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4309; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4306; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4299; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4298; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4247; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4245; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4233; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4187; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4163; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4147; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4134; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4132; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4119; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4115`
- Source reference count: `301`

## ALP-22F4B209BB36 | VNMSGN-VSEMS01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `git http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMSGN-VSEMS01 reported `git http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `292`
- Resolved alerts: `292`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4463; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4432; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4431; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4425; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4415; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4407; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4355; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4335; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4326; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4305; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4266; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4255; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4250; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4240; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4196; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4189; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4177; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4159; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4151; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4143`
- Source reference count: `292`

## ALP-8C45EBECE8B9 | VNMSNT-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `git http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMSNT-VSSPM01 reported `git http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `289`
- Resolved alerts: `289`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4470; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4288; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4284; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4279; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4275; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4242; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4232; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4198; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4185; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4149; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4146; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4137; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4127; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4116; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4111; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4094; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4090; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4058; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4035; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4017`
- Source reference count: `289`

## ALP-9D95052D0965 | VNMCPL-VSSPM04

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `git http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMCPL-VSSPM04 reported `git http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `289`
- Resolved alerts: `289`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4460; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4441; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4440; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4433; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4429; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4420; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4418; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4401; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4393; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4364; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4330; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4296; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4291; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4200; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4193; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4190; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4170; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4168; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4158; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4156`
- Source reference count: `289`

## ALP-77CAA12D786F | VNMSGN-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `git http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMSGN-VSSPM02 reported `git http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `284`
- Resolved alerts: `284`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4439; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4427; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4424; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4403; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4399; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4386; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4385; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4374; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4372; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4332; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4331; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4329; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4295; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4273; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4272; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4257; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4256; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4239; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4236; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4231`
- Source reference count: `284`

## ALP-FE28092FA2A4 | VNMSGN-VSSPM03

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `git http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMSGN-VSSPM03 reported `git http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `282`
- Resolved alerts: `282`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4414; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4410; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4402; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4390; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4375; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4344; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4308; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4294; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4292; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4253; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4234; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4228; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4195; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4191; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4188; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4176; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4141; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4140; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4133; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4129`
- Source reference count: `282`

## ALP-557802E2665D | VNMSNT-VSSPM03

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `git http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMSNT-VSSPM03 reported `git http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `248`
- Resolved alerts: `248`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4468; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4465; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4442; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4430; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4408; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4406; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4404; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4394; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4384; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4363; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4333; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4310; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4248; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4238; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4201; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4197; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4172; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4165; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4139; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4076`
- Source reference count: `248`

## ALP-551CCB8820FE | VNMSNT-VSEMS01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `git http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMSNT-VSEMS01 reported `git http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `228`
- Resolved alerts: `228`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4473; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4471; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4464; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4436; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4435; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4422; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4413; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4398; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4381; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4337; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4319; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4289; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4287; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4281; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4276; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4249; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4244; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4229; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4171; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4169`
- Source reference count: `228`

## ALP-550ED7DB3F47 | VNMSGN-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `git http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMSGN-VSSPM01 reported `git http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `204`
- Resolved alerts: `204`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4466; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4437; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4426; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4417; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4400; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4380; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4307; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4303; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4283; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4274; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4267; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4251; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4243; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4241; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4186; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4175; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4164; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4101; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4100; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4099`
- Source reference count: `204`

## ALP-460C038618E4 | VNMCPL-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `git http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMCPL-VSSPM01 reported `git http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `164`
- Resolved alerts: `164`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4478; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4327; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4297; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4290; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4268; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4237; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4166; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4154; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4114; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4060; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4053; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4013; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3951; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3931; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3867; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3859; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3848; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3831; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3822; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3816`
- Source reference count: `164`

## ALP-80599BC38B81 | VNMSNT-VSSPM04

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `git http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMSNT-VSSPM04 reported `git http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `155`
- Resolved alerts: `155`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4472; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4411; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4409; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4405; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4379; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4373; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4365; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4254; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4252; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4161; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4136; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4128; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4050; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4038; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4008; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3929; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3928; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3885; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3875; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3854`
- Source reference count: `155`

## ALP-AE10DD3DBB85 | VNMRVF-UPS01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `apc ups: unacceptable input frequency (out of range <value> for <value>)`
- Pattern family: `Power/UPS`
- Investigation priority: `HIGH`
- Why it matters: VNMRVF-UPS01 reported `apc ups: unacceptable input frequency (out of range <value> for <value>)`. This may indicate power/UPS instability and deserves facility or device-side verification.
- Raw alert count: `55`
- Resolved alerts: `55`
- Open alerts: `0`
- Site code: `RVF`
- Domain: `power`
- Component: `power`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4367; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3870; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3769; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3740; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3559; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3442; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3411; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3331; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2996; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2973; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2872; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2870; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2859; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2553; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2503; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2207; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2197; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2124; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2112; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2032`
- Source reference count: `55`

## ALP-E7E97D0E219A | VNMMSH-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/17(2f-d29): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-PNSSW01 reported `interface gi1/0/17(2f-d29): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `44`
- Resolved alerts: `44`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4336; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4334; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4304; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4300; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4286; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4280; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4199; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4153; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3947; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3934; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3902; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3652; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3472; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3470; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3469; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3002; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2879; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2765; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2666; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2255`
- Source reference count: `44`

## ALP-46174DEDA3A4 | VNMRVF-UPS02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `apc ups: unacceptable input frequency (out of range <value> for <value>)`
- Pattern family: `Power/UPS`
- Investigation priority: `HIGH`
- Why it matters: VNMRVF-UPS02 reported `apc ups: unacceptable input frequency (out of range <value> for <value>)`. This may indicate power/UPS instability and deserves facility or device-side verification.
- Raw alert count: `42`
- Resolved alerts: `42`
- Open alerts: `0`
- Site code: `RVF`
- Domain: `power`
- Component: `power`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4366; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3768; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3655; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3558; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3416; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3330; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2995; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2972; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2871; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2858; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2552; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2500; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2206; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1940; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1921; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1893; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1849; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1844; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1822; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1817`
- Source reference count: `42`

## ALP-B1488C926411 | VNMMSH-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `linux: load average is too high (per cpu load over 0.75 for <value>)`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-VSSPM01 reported `linux: load average is too high (per cpu load over 0.75 for <value>)`. Treat as monitoring context until corroborated.
- Raw alert count: `41`
- Resolved alerts: `41`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `os`
- Component: `cpu`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4419; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4184; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4006; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3811; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3703; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3593; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3524; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3423; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3360; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3263; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3022; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2939; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2914; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2813; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2711; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2589; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2565; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2558; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2509; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2391`
- Source reference count: `41`

## ALP-D0FCFBCBA8AA | VNMMS2-NetNam-spx.shopee.vn

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMMS2-NetNam-spx.shopee.vn reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `38`
- Resolved alerts: `38`
- Open alerts: `0`
- Site code: `MS2`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4322; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4321; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4320; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4316; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4315; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4313; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4312; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3176; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3174; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3173; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3170; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3167; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3165; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3163; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3161; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3159; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3155; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3151; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3150; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3148`
- Source reference count: `38`

## ALP-17B01F3BB308 | VNMMBD-NETNAM-spx.shopee.vn

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMMBD-NETNAM-spx.shopee.vn reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `26`
- Resolved alerts: `26`
- Open alerts: `0`
- Site code: `MBD`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4318; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4314; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3177; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3175; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3172; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3169; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3166; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3164; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3162; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3158; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3156; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3154; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3153; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3152; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3149; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3147; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3144; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3143; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3140; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3139`
- Source reference count: `26`

## ALP-CAD1A664558A | VNMMS2-FPT-FMS-45.119.218.141

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMMS2-FPT-FMS-45.119.218.141 reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `26`
- Resolved alerts: `26`
- Open alerts: `0`
- Site code: `MS2`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3397; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2127; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2123; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2113; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2111; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2104; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2100; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2093; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2089; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2083; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2061; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2055; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2049; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2040; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2026; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2018; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2010; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1996; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1990; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1972`
- Source reference count: `26`

## ALP-1CBDABDA59C1 | VNMMS2-FPT-FMS-45.119.218.130

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMMS2-FPT-FMS-45.119.218.130 reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `25`
- Resolved alerts: `25`
- Open alerts: `0`
- Site code: `MS2`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2126; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2122; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2110; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2103; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2099; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2096; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2088; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2082; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2068; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2064; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2058; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2046; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2039; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2029; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2017; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2009; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1999; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1989; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1975; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1970`
- Source reference count: `25`

## ALP-AB3C1A209D93 | VNMSNT-UPSF2201

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `3.1: battery has high temperature (over 55℃ for <value>)`
- Pattern family: `Power/UPS`
- Investigation priority: `HIGH`
- Why it matters: VNMSNT-UPSF2201 reported `3.1: battery has high temperature (over 55℃ for <value>)`. This may indicate power/UPS instability and deserves facility or device-side verification.
- Raw alert count: `25`
- Resolved alerts: `25`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `power`
- Component: `temperature`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4477; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4462; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4340; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4262; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4260; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4123; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4097; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4082; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4023; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3826; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3824; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3124; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2990; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2982; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2979; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2949; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2670; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2664; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2545; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2185`
- Source reference count: `25`

## ALP-E2A7575F1806 | VNMMSB-FPT-FMS-45.119.218.130

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMMSB-FPT-FMS-45.119.218.130 reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `25`
- Resolved alerts: `25`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2557; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2120; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2114; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2108; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2105; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2097; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2094; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2090; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2084; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2069; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2062; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2056; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2047; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2041; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2027; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2019; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2011; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1997; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1973; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1966`
- Source reference count: `25`

## ALP-5E69C4448C78 | VNMSNT-UPSF2201

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `3.2: battery has high temperature (over 55℃ for <value>)`
- Pattern family: `Power/UPS`
- Investigation priority: `HIGH`
- Why it matters: VNMSNT-UPSF2201 reported `3.2: battery has high temperature (over 55℃ for <value>)`. This may indicate power/UPS instability and deserves facility or device-side verification.
- Raw alert count: `24`
- Resolved alerts: `24`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `power`
- Component: `temperature`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4476; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4461; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4339; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4261; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4259; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4125; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4096; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4081; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3827; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3823; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3123; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2989; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2981; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2978; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2948; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2669; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2663; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2548; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2184; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2117`
- Source reference count: `24`

## ALP-9966AD21D215 | VNMMSB-FPT-FMS-45.119.218.141

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMMSB-FPT-FMS-45.119.218.141 reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `24`
- Resolved alerts: `24`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2121; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2115; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2109; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2106; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2098; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2095; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2091; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2085; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2070; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2063; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2057; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2048; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2042; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2028; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2020; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2012; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1998; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1974; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1967; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1963`
- Source reference count: `24`

## ALP-40F5382B2C17 | VNMSNT-UPSF2201

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `apc ups: battery has high temperature (over 55℃ for <value>)`
- Pattern family: `Power/UPS`
- Investigation priority: `HIGH`
- Why it matters: VNMSNT-UPSF2201 reported `apc ups: battery has high temperature (over 55℃ for <value>)`. This may indicate power/UPS instability and deserves facility or device-side verification.
- Raw alert count: `20`
- Resolved alerts: `20`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `power`
- Component: `temperature`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4474; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4264; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4258; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4124; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4083; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3830; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3486; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3121; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2987; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2980; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2951; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2668; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2665; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2547; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2187; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2116; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1931; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1670; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5062; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5003`
- Source reference count: `20`

## ALP-E508F0A30F14 | VNMSGN-F24-Studio-SW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/24(data): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-F24-Studio-SW01 reported `interface gi1/0/24(data): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `18`
- Resolved alerts: `18`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3308; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3134; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3064; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2876; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2756; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1687; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1685; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-914; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-707; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-692; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-659; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-528; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-518; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-413; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-288; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-243; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-29; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4616`
- Source reference count: `18`

## ALP-4C0ACA243192 | VNMSNT-VSSPM04

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `jira http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMSNT-VSSPM04 reported `jira http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `17`
- Resolved alerts: `17`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4218; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4208; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3500; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3220; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2800; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2695; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2373; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1885; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1757; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1330; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1250; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1026; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-745; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-558; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-130; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4893; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4769`
- Source reference count: `17`

## ALP-7259165E30FF | VNMSNT-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `jira http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMSNT-VSSPM02 reported `jira http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `17`
- Resolved alerts: `17`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4220; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4211; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3512; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3224; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2802; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2690; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2347; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1865; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1741; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1334; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1246; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1015; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-732; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-557; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-129; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4885; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4753`
- Source reference count: `17`

## ALP-9449A45503C7 | VNMMSH-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/13(2f-d25): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-PNSSW01 reported `interface gi1/0/13(2f-d25): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `17`
- Resolved alerts: `17`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3781; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3666; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3662; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3661; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3630; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2650; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2645; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2550; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1082; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-929; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-618; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-612; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-553; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5095; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4957; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4709; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4606`
- Source reference count: `17`

## ALP-ADA6C918C671 | VNMSNT-UPSF2201

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `apc ups: ups is hardware failure bypass`
- Pattern family: `Power/UPS`
- Investigation priority: `HIGH`
- Why it matters: VNMSNT-UPSF2201 reported `apc ups: ups is hardware failure bypass`. This may indicate power/UPS instability and deserves facility or device-side verification.
- Raw alert count: `17`
- Resolved alerts: `17`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `power`
- Component: `health,power`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4338; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4263; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4126; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4103; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3829; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3485; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3118; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2988; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2950; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2667; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2546; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2186; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2119; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1669; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5061; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5002; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4723`
- Source reference count: `17`

## ALP-B272469C4059 | VNMSNT-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `jira http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMSNT-VSSPM01 reported `jira http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `17`
- Resolved alerts: `17`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4216; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4210; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3513; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3247; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2791; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2697; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2349; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1879; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1737; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1320; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1220; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1016; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-735; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-562; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-161; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4878; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4755`
- Source reference count: `17`

## ALP-BC88B7D92FB9 | VNMMSH-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/16(2f-d28): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-PNSSW01 reported `interface gi1/0/16(2f-d28): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `17`
- Resolved alerts: `17`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4323; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4285; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4162; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4157; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4080; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3901; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3783; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2661; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2647; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1537; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1373; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-46; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4958; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4837; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4707; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4624; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4612`
- Source reference count: `17`

## ALP-CB87DC54115C | VNMSNT-VSEMS01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `jira http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMSNT-VSEMS01 reported `jira http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `17`
- Resolved alerts: `17`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4224; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4221; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4212; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3515; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3225; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2793; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2698; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2351; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1881; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1739; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1337; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1222; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-737; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-563; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-138; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4887; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4765`
- Source reference count: `17`

## ALP-0956650F5A4C | VNMRVF-VSZABPRX-GNL1

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `jira http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMRVF-VSZABPRX-GNL1 reported `jira http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `16`
- Resolved alerts: `16`
- Open alerts: `0`
- Site code: `RVF`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3504; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3226; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2792; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2685; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2352; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1882; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1745; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1617; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1321; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1263; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1247; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-738; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-564; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-139; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4874; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4749`
- Source reference count: `16`

## ALP-7C9CD18C7FC5 | VNMSNT-VSSPM03

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `jira http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMSNT-VSSPM03 reported `jira http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `16`
- Resolved alerts: `16`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4219; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4209; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3501; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3222; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2801; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2688; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2346; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1866; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1740; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1331; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1218; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-746; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-559; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-160; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4884; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4748`
- Source reference count: `16`

## ALP-161D4179FDA9 | VNMSGN-VSSPM03

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `jira http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMSGN-VSSPM03 reported `jira http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `15`
- Resolved alerts: `15`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3518; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3218; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2805; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2693; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2362; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1871; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1750; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1691; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1322; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1232; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-742; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-567; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-149; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4890; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4750`
- Source reference count: `15`

## ALP-43E03B32158E | VNMSGN-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `jira http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMSGN-VSSPM01 reported `jira http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `15`
- Resolved alerts: `15`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3507; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3238; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2786; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2687; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2367; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1875; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1754; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1706; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1326; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1236; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-750; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-569; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-135; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4882; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4751`
- Source reference count: `15`

## ALP-43F27E19DD21 | VNMRVF-VSZABPRX-ISP1

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `jira http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMRVF-VSZABPRX-ISP1 reported `jira http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `15`
- Resolved alerts: `15`
- Open alerts: `0`
- Site code: `RVF`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3514; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3248; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2788; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2691; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2350; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1880; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1742; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1336; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1262; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1221; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-736; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-571; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-162; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4879; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4764`
- Source reference count: `15`

## ALP-5BA58770C8AF | VNMSGN-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `jira http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMSGN-VSSPM02 reported `jira http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `15`
- Resolved alerts: `15`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3519; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3234; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2797; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2702; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2363; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1873; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1752; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1693; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1324; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1234; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-749; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-568; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-132; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4881; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4759`
- Source reference count: `15`

## ALP-6F2F9F50A046 | VNMCPL-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `jira http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMCPL-VSSPM01 reported `jira http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `15`
- Resolved alerts: `15`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3517; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3252; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2795; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2692; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2360; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1870; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1749; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1341; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1229; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-741; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-645; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-566; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-146; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4880; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4766`
- Source reference count: `15`

## ALP-8E6AC4150C80 | VNMMSH-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `jira http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMSH-VSSPM01 reported `jira http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `15`
- Resolved alerts: `15`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3520; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3254; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2798; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2703; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2364; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1874; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1753; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1705; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1325; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1235; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-743; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-575; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-168; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4892; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4768`
- Source reference count: `15`

## ALP-968676F48AAF | VNMRVF-VSZABPRX-ISP3

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `jira http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMRVF-VSZABPRX-ISP3 reported `jira http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `15`
- Resolved alerts: `15`
- Open alerts: `0`
- Site code: `RVF`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3511; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3215; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2790; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2689; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2343; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1867; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1738; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1332; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1261; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1219; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-733; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-560; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-128; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4877; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4763`
- Source reference count: `15`

## ALP-D8563BF0B2A5 | VNMRVF-VSZABPRX-ISP2

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `jira http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMRVF-VSZABPRX-ISP2 reported `jira http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `15`
- Resolved alerts: `15`
- Open alerts: `0`
- Site code: `RVF`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3503; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3223; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2803; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2696; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2348; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1868; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1744; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1335; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1264; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1211; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-734; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-561; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-137; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4886; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4754`
- Source reference count: `15`

## ALP-DB00D177E05F | VNMSGN-VSEMS01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `jira http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMSGN-VSEMS01 reported `jira http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `15`
- Resolved alerts: `15`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3508; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3255; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2806; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2704; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2368; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1877; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1755; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1707; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1328; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1217; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-744; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-570; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-152; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4883; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4761`
- Source reference count: `15`

## ALP-FC8A681995B1 | VNMMSH-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `jira http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMSH-VSSPM02 reported `jira http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `15`
- Resolved alerts: `15`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3502; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3253; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2796; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2701; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2380; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1872; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1751; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1692; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1323; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1233; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-748; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-574; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-150; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4891; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4767`
- Source reference count: `15`

## ALP-744043C0F1DE | VNMCPL-VSSPM04

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `jira http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMCPL-VSSPM04 reported `jira http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `14`
- Resolved alerts: `14`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3516; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3228; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2794; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2686; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2377; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1869; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1746; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1338; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1224; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-739; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-572; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-140; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4875; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4756`
- Source reference count: `14`

## ALP-A67C22A71598 | VNMSGN-F24-Studio-SW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/20(data): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-F24-Studio-SW01 reported `interface gi1/0/20(data): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `14`
- Resolved alerts: `13`
- Open alerts: `1`
- Site code: `SGN`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3771; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3567; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3563; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3306; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3130; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3065; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1681; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-927; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-835; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-677; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-519; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-414; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-244; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-31`
- Source reference count: `14`

## ALP-AB43BE0559B5 | VNMWBN-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `jira http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMWBN-VSSPM01 reported `jira http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `14`
- Resolved alerts: `14`
- Open alerts: `0`
- Site code: `WBN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3510; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3256; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2787; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2684; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2370; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1878; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1756; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1329; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1238; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-751; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-577; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-154; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4876; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4762`
- Source reference count: `14`

## ALP-D05FEF044AE4 | VNMCPL-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `jira http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMCPL-VSSPM02 reported `jira http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `14`
- Resolved alerts: `14`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3506; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3216; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2789; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2700; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2355; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1884; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1748; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1340; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1226; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-740; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-573; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-141; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4889; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4758`
- Source reference count: `14`

## ALP-F49D6521EF17 | VNMWBN-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `jira http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMWBN-VSSPM02 reported `jira http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `14`
- Resolved alerts: `14`
- Open alerts: `0`
- Site code: `WBN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3509; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3239; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2799; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2694; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2382; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1876; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1743; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1327; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1249; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-752; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-576; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-151; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4894; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4760`
- Source reference count: `14`

## ALP-FDC327088884 | VNMCPL-VSSPM03

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `jira http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `MEDIUM`
- Why it matters: VNMCPL-VSSPM03 reported `jira http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `14`
- Resolved alerts: `14`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3505; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3229; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2804; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2699; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2354; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1883; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1747; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1339; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1225; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-747; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-565; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-164; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4888; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4757`
- Source reference count: `14`

## ALP-0EAC2ABF80AC | VNMMSH-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi2/0/9(2f-d23-tplink-16ports): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-PNSSW01 reported `interface gi2/0/9(2f-d23-tplink-16ports): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `13`
- Resolved alerts: `13`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4325; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3948; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3888; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3440; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2977; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2566; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1835; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1363; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1057; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-938; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-419; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4706; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4609`
- Source reference count: `13`

## ALP-2D3FBB654BE3 | VNMMSB-PNCSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface xgigabitethernet1/0/27(sw30b-hub22-poe-sw-xge1/0/4): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-PNCSW01 reported `interface xgigabitethernet1/0/27(sw30b-hub22-poe-sw-xge1/0/4): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `13`
- Resolved alerts: `13`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3569; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2748; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2658; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2654; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2639; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2561; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1318; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1314; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-945; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-944; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-942; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-933; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-697`
- Source reference count: `13`

## ALP-AD5AA6FC1FB8 | VNMMSH-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/15(2f-d27): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-PNSSW01 reported `interface gi1/0/15(2f-d27): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `10`
- Resolved alerts: `10`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3404; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1834; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1081; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-930; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-841; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-418; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-269; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4956; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4705; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4608`
- Source reference count: `10`

## ALP-02E68BDBC9C9 | VNMSNT-VSEMS01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `shopee confluence http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-VSEMS01 reported `shopee confluence http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `9`
- Resolved alerts: `9`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4226; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4215; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4204; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3980; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3231; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2358; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1230; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1019; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-145`
- Source reference count: `9`

## ALP-3C94BCE98493 | VNMSGN-F24-Studio-SW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/15(data): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-F24-Studio-SW01 reported `interface gi1/0/15(data): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `9`
- Resolved alerts: `9`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3190; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3061; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2900; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2892; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2130; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-425; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-30; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5128; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4611`
- Source reference count: `9`

## ALP-4BF58F585699 | VNMMSB-VSCDC02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: high memory utilization (>90% for <value>)`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-VSCDC02 reported `windows: high memory utilization (>90% for <value>)`. Treat as monitoring context until corroborated.
- Raw alert count: `9`
- Resolved alerts: `8`
- Open alerts: `1`
- Site code: `MSB`
- Domain: `os`
- Component: `memory`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3145; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3094; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3037; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3033; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4986; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4980; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4665; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4654; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4626`
- Source reference count: `9`

## ALP-E3F1CEF16485 | VNMMSB-PNCSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface xgigabitethernet0/0/27(sw30b-hub22-poe-sw-xge0/0/4): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-PNCSW01 reported `interface xgigabitethernet0/0/27(sw30b-hub22-poe-sw-xge0/0/4): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `9`
- Resolved alerts: `9`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3568; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2659; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2657; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2653; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1333; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1319; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-943; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-934; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-698`
- Source reference count: `9`

## ALP-087E56F6D62B | VNMSNT-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `shopee confluence http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-VSSPM02 reported `shopee confluence http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `8`
- Resolved alerts: `8`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4214; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4203; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3996; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3230; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2378; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1212; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1017; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-143`
- Source reference count: `8`

## ALP-6C309587E8D5 | VNMMSB-VSCDC01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: high memory utilization (>90% for <value>)`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-VSCDC01 reported `windows: high memory utilization (>90% for <value>)`. Treat as monitoring context until corroborated.
- Raw alert count: `8`
- Resolved alerts: `8`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `os`
- Component: `memory`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2926; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2919; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2881; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2874; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2660; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2649; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-480; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-321`
- Source reference count: `8`

## ALP-B98F56ADD27C | VNMSNT-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `shopee confluence http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-VSSPM01 reported `shopee confluence http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `8`
- Resolved alerts: `8`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4225; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4205; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3986; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3250; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2357; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1228; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1018; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-165`
- Source reference count: `8`

## ALP-FDF85018772E | VNMMSH-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/22(2f-d34): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-PNSSW01 reported `interface gi1/0/22(2f-d34): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `8`
- Resolved alerts: `8`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3949; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3408; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1660; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-661; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5102; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4959; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4704; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4610`
- Source reference count: `8`

## ALP-176B73406A1D | VNMMSB-PNCSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface eth-trunk35(sw30b-hub12-poe-sw): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-PNCSW01 reported `interface eth-trunk35(sw30b-hub12-poe-sw): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `7`
- Resolved alerts: `7`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2656; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2652; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2562; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1317; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-941; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-932; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-699`
- Source reference count: `7`

## ALP-3EB6409BA309 | VNMMSH-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `shopee confluence http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-VSSPM01 reported `shopee confluence http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `7`
- Resolved alerts: `7`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3998; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3242; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2372; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1696; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1239; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-696; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-169`
- Source reference count: `7`

## ALP-6CC3E76FFF18 | VNMSNT-VSSPM03

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `shopee confluence http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-VSSPM03 reported `shopee confluence http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `7`
- Resolved alerts: `7`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4213; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4202; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3985; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3249; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2356; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1227; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-142`
- Source reference count: `7`

## ALP-7FEC14B7A1CA | VNMMS2-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMS2-VSSPM01 reported `http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `7`
- Resolved alerts: `7`
- Open alerts: `0`
- Site code: `MS2`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3688; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3671; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3468; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3403; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2753; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1763; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1548`
- Source reference count: `7`

## ALP-C6ED613558DD | VNMMSB-PNASW-Hub22

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `cisco ios: unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMMSB-PNASW-Hub22 reported `cisco ios: unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `7`
- Resolved alerts: `7`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `network`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2655; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2651; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2560; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1316; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-940; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-931; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-695`
- Source reference count: `7`

## ALP-FE978C1E0C20 | VNMCCW-PNASW-OFFICE

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi2/0/9(backoffice): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMCCW-PNASW-OFFICE reported `interface gi2/0/9(backoffice): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `7`
- Resolved alerts: `7`
- Open alerts: `0`
- Site code: `CCW`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3884; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3882; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3048; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1369; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1350; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-946; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-711`
- Source reference count: `7`

## ALP-01E4CBEDDEBE | VNMMSH-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `shopee confluence http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-VSSPM02 reported `shopee confluence http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `6`
- Resolved alerts: `6`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3983; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3244; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2384; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1697; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1245; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-156`
- Source reference count: `6`

## ALP-1A3F306FCB8F | VNMSGN-F24-Studio-SW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/5(data): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-F24-Studio-SW01 reported `interface gi1/0/5(data): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `6`
- Resolved alerts: `6`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3565; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3132; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3062; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1682; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4619; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4615`
- Source reference count: `6`

## ALP-2BF8F51D3C34 | VNMSGN-VSSPM03

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `shopee confluence http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-VSSPM03 reported `shopee confluence http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `6`
- Resolved alerts: `6`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4000; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3243; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2374; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1694; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1251; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-155`
- Source reference count: `6`

## ALP-43AFF3060676 | VNMRVF-VSZABPRX-ISP1

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `shopee confluence http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMRVF-VSZABPRX-ISP1 reported `shopee confluence http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `6`
- Resolved alerts: `6`
- Open alerts: `0`
- Site code: `RVF`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3990; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3236; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2366; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1614; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1248; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-133`
- Source reference count: `6`

## ALP-484B720DB953 | VNMRVF-VSZABPRX-ISP2

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `shopee confluence http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMRVF-VSZABPRX-ISP2 reported `shopee confluence http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `6`
- Resolved alerts: `6`
- Open alerts: `0`
- Site code: `RVF`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3981; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3235; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2365; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1613; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1215; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-167`
- Source reference count: `6`

## ALP-5222B2692D5C | VNMSGN-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `shopee confluence http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-VSSPM01 reported `shopee confluence http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `6`
- Resolved alerts: `6`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3994; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3245; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2383; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1695; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1243; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-158`
- Source reference count: `6`

## ALP-5AAEBF45DE41 | VNMSGN-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `shopee confluence http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-VSSPM02 reported `shopee confluence http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `6`
- Resolved alerts: `6`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4001; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3246; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2376; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1698; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1244; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-159`
- Source reference count: `6`

## ALP-7D5EB2CD1DDF | VNMRVF-VSZABPRX-ISP3

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `shopee confluence http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMRVF-VSZABPRX-ISP3 reported `shopee confluence http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `6`
- Resolved alerts: `6`
- Open alerts: `0`
- Site code: `RVF`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3997; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3251; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2359; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1612; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1210; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-144`
- Source reference count: `6`

## ALP-99D165C7290A | VNMSNT-VSSPM04

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `shopee confluence http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-VSSPM04 reported `shopee confluence http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `6`
- Resolved alerts: `6`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3987; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3232; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2379; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1213; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1011; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-147`
- Source reference count: `6`

## ALP-9F5684E55F8F | VNMSGN-VSEMS01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `shopee confluence http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-VSEMS01 reported `shopee confluence http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `6`
- Resolved alerts: `6`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3999; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3241; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2371; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1708; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1240; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-136`
- Source reference count: `6`

## ALP-A8B5D5531BA6 | VNMRVF-VSZABPRX-GNL1

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `shopee confluence http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMRVF-VSZABPRX-GNL1 reported `shopee confluence http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `6`
- Resolved alerts: `6`
- Open alerts: `0`
- Site code: `RVF`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3991; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3237; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2381; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1616; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1216; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-134`
- Source reference count: `6`

## ALP-F5572970729B | VNMMDN-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMDN-VSSPM01 reported `http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `6`
- Resolved alerts: `6`
- Open alerts: `0`
- Site code: `MDN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3673; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3395; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3391; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-498; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-496; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-286`
- Source reference count: `6`

## ALP-FF8D34DADB81 | VNMCPL-VSSPM03

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `shopee confluence http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-VSSPM03 reported `shopee confluence http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `6`
- Resolved alerts: `6`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3989; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3217; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2344; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1214; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-652; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-166`
- Source reference count: `6`

## ALP-30992FCAC4B8 | VNMCPL-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `shopee confluence http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-VSSPM02 reported `shopee confluence http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `5`
- Resolved alerts: `5`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3984; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3227; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2353; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1223; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-163`
- Source reference count: `5`

## ALP-4C3768F55AC8 | VNMCPL-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `shopee confluence http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-VSSPM01 reported `shopee confluence http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `5`
- Resolved alerts: `5`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3993; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3221; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2375; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1242; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-157`
- Source reference count: `5`

## ALP-6D1757618413 | VNMCCW-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMCCW-VSSPM01 reported `http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `5`
- Resolved alerts: `5`
- Open alerts: `0`
- Site code: `CCW`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3401; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1605; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5153; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5145; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5143`
- Source reference count: `5`

## ALP-7488F88C19DF | VNMWBN-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `shopee confluence http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMWBN-VSSPM02 reported `shopee confluence http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `5`
- Resolved alerts: `5`
- Open alerts: `0`
- Site code: `WBN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3988; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3233; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2361; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1231; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-148`
- Source reference count: `5`

## ALP-75F370D51820 | VNMCPL-VSSPM04

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `shopee confluence http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-VSSPM04 reported `shopee confluence http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `5`
- Resolved alerts: `5`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3992; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3240; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2345; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1241; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-170`
- Source reference count: `5`

## ALP-99E67BCA8B6A | VNMWBN-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `shopee confluence http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMWBN-VSSPM01 reported `shopee confluence http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `5`
- Resolved alerts: `5`
- Open alerts: `0`
- Site code: `WBN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3982; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3219; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2369; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1237; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-153`
- Source reference count: `5`

## ALP-F43B329C01A5 | VNMSWS-VSEMS01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSWS-VSEMS01 reported `http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `5`
- Resolved alerts: `5`
- Open alerts: `0`
- Site code: `SWS`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3462; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2632; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1659; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-769; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4941`
- Source reference count: `5`

## ALP-09155739FD0E | VNMSGN-VSEMS01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `itcenter http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-VSEMS01 reported `itcenter http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `4`
- Resolved alerts: `4`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2621; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1160; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1152; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1136`
- Source reference count: `4`

## ALP-115D48183243 | VNMSGN-F24-Studio-SW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/11(data): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-F24-Studio-SW01 reported `interface gi1/0/11(data): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `4`
- Resolved alerts: `3`
- Open alerts: `1`
- Site code: `SGN`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2882; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2878; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2877; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2757`
- Source reference count: `4`

## ALP-3C7E97F05B37 | VNMCPL-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `google http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-VSSPM02 reported `google http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `4`
- Resolved alerts: `4`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2894; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2889; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1814; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-651`
- Source reference count: `4`

## ALP-63A681653D3E | VNMMSH-VSDHC02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: active checks are not available`
- Pattern family: `Zabbix agent/active check`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-VSDHC02 reported `windows: active checks are not available`. This points to monitoring-agent availability rather than confirmed user impact unless supported by ticket or incident evidence.
- Raw alert count: `4`
- Resolved alerts: `4`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `os`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2751; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2750; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1508; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4722`
- Source reference count: `4`

## ALP-788ECF082C30 | VNMMSH-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/4(wired-users): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-PNSSW01 reported `interface gi1/0/4(wired-users): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `4`
- Resolved alerts: `4`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1192; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1083; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5090; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5087`
- Source reference count: `4`

## ALP-8DB77EB6AD73 | VNMSGN-F24-Studio-SW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/17(data): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-F24-Studio-SW01 reported `interface gi1/0/17(data): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `4`
- Resolved alerts: `3`
- Open alerts: `1`
- Site code: `SGN`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3063; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-705; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-527; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5129`
- Source reference count: `4`

## ALP-9472E3130DB1 | VNMSNT-VSSPM04

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `space http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-VSSPM04 reported `space http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `4`
- Resolved alerts: `4`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4217; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4207; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4182; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1025`
- Source reference count: `4`

## ALP-981B0724F60D | VNMCPL-VSDHC02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: active checks are not available`
- Pattern family: `Zabbix agent/active check`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-VSDHC02 reported `windows: active checks are not available`. This points to monitoring-agent availability rather than confirmed user impact unless supported by ticket or incident evidence.
- Raw alert count: `4`
- Resolved alerts: `3`
- Open alerts: `1`
- Site code: `CPL`
- Domain: `os`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1493; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4507; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4496; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4480`
- Source reference count: `4`

## ALP-9E2AEE42C23D | VNMMSH-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `google http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-VSSPM02 reported `google http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `4`
- Resolved alerts: `4`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2885; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1809; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1776; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-957`
- Source reference count: `4`

## ALP-A0947B93EBA0 | VNMMDN-VSEMS01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMDN-VSEMS01 reported `http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `4`
- Resolved alerts: `4`
- Open alerts: `0`
- Site code: `MDN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3674; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1956; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-499; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5038`
- Source reference count: `4`

## ALP-E27238F0A5A8 | VNMMSH-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi2/0/6(new-ap): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-PNSSW01 reported `interface gi2/0/6(new-ap): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `4`
- Resolved alerts: `4`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4622; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4621; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4620; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4535`
- Source reference count: `4`

## ALP-E3B1DE2AC12E | VNMSGN-VSEMS01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `hris http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-VSEMS01 reported `hris http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `4`
- Resolved alerts: `4`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2616; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1141; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1135; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1111`
- Source reference count: `4`

## ALP-13B43D07AA25 | VNMMS2-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMS2-VSSPM02 reported `http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `3`
- Resolved alerts: `3`
- Open alerts: `0`
- Site code: `MS2`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3930; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1547; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-757`
- Source reference count: `3`

## ALP-13C2484F33DF | VNMSGN-F24-Studio-SW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/14(data): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-F24-Studio-SW01 reported `interface gi1/0/14(data): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `3`
- Resolved alerts: `3`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3572; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3562; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-62`
- Source reference count: `3`

## ALP-21C6B54A3E59 | VNMSGN-VSSPM03

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `hris http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-VSSPM03 reported `hris http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `3`
- Resolved alerts: `3`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1151; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1138; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1125`
- Source reference count: `3`

## ALP-300E3E1681E3 | VNMMBD-NETNAM-FMS-143.92.82.164

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMMBD-NETNAM-FMS-143.92.82.164 reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `3`
- Resolved alerts: `3`
- Open alerts: `0`
- Site code: `MBD`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4317; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3178; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2906`
- Source reference count: `3`

## ALP-30B215136C84 | VNMMBD-VSEMS01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMBD-VSEMS01 reported `http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `3`
- Resolved alerts: `3`
- Open alerts: `0`
- Site code: `MBD`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-703; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4969; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4838`
- Source reference count: `3`

## ALP-5E7AD2B3F5CD | VNMSNT-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `space http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-VSSPM02 reported `space http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `3`
- Resolved alerts: `3`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4223; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4183; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1023`
- Source reference count: `3`

## ALP-6543D8B05E3C | VNMWBN-PNWFW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface tunnel.36(to-cp-fpt): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMWBN-PNWFW01 reported `interface tunnel.36(to-cp-fpt): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `3`
- Resolved alerts: `3`
- Open alerts: `0`
- Site code: `WBN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1798; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4860; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4848`
- Source reference count: `3`

## ALP-6F1E089FBF4D | VNMSGN-VSSPM03

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `itcenter http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-VSSPM03 reported `itcenter http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `3`
- Resolved alerts: `3`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2624; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1161; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1101`
- Source reference count: `3`

## ALP-7039E6E4C1A5 | VNMSNT-VSSPM03

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `space http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-VSSPM03 reported `space http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `3`
- Resolved alerts: `3`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4222; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4206; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4180`
- Source reference count: `3`

## ALP-7637E316BAF5 | VNMMDN-PSSJP1

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMMDN-PSSJP1 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `3`
- Resolved alerts: `3`
- Open alerts: `0`
- Site code: `MDN`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4269; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1542; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-729`
- Source reference count: `3`

## ALP-7A23D4CE212F | VNMCCW-VSEMS01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMCCW-VSEMS01 reported `http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `3`
- Resolved alerts: `3`
- Open alerts: `0`
- Site code: `CCW`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3476; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1606; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5146`
- Source reference count: `3`

## ALP-8022BF11F7B8 | VNMMBD-VSSPM03

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMBD-VSSPM03 reported `http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `3`
- Resolved alerts: `3`
- Open alerts: `0`
- Site code: `MBD`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3041; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4970; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4966`
- Source reference count: `3`

## ALP-8C989B803A73 | VNMCCW-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMCCW-VSSPM02 reported `http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `3`
- Resolved alerts: `3`
- Open alerts: `0`
- Site code: `CCW`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3477; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1604; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5150`
- Source reference count: `3`

## ALP-9089098A65A0 | VNMMSH-VSDHC02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: high memory utilization (>90% for <value>)`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-VSDHC02 reported `windows: high memory utilization (>90% for <value>)`. Treat as monitoring context until corroborated.
- Raw alert count: `3`
- Resolved alerts: `3`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `os`
- Component: `memory`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2807; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2782; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2771`
- Source reference count: `3`

## ALP-AD0FEAB4CF54 | VNMCPL-FPT-GoogleDNS

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMCPL-FPT-GoogleDNS reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `3`
- Resolved alerts: `3`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4361; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4359; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1815`
- Source reference count: `3`

## ALP-BF6FF8E976BE | VNMCPL-VTHL-GoogleDNS

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMCPL-VTHL-GoogleDNS reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `3`
- Resolved alerts: `3`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4362; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4357; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1805`
- Source reference count: `3`

## ALP-C061A474B203 | VNMSGN-F24-Studio-SW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/16(data): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-F24-Studio-SW01 reported `interface gi1/0/16(data): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `3`
- Resolved alerts: `3`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-937; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-936; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-928`
- Source reference count: `3`

## ALP-C380821D118B | VNMMSH-VSDHC02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-VSDHC02 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `3`
- Resolved alerts: `3`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2749; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1503; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4720`
- Source reference count: `3`

## ALP-C3F11E8E54C2 | VNMCPL-VSDHC02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-VSDHC02 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `3`
- Resolved alerts: `3`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1492; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4506; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4495`
- Source reference count: `3`

## ALP-E98E242414FE | VNMWBN-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `itcenter http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMWBN-VSSPM01 reported `itcenter http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `3`
- Resolved alerts: `3`
- Open alerts: `0`
- Site code: `WBN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1808; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5104; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5097`
- Source reference count: `3`

## ALP-F21C496048BA | VNMMS2-VSSPM03

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMS2-VSSPM03 reported `http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `3`
- Resolved alerts: `3`
- Open alerts: `0`
- Site code: `MS2`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3482; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1433; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-420`
- Source reference count: `3`

## ALP-F35DA0E7A925 | VNMSGN-F24-Studio-SW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/18(data): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-F24-Studio-SW01 reported `interface gi1/0/18(data): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `3`
- Resolved alerts: `3`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3570; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3566; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3561`
- Source reference count: `3`

## ALP-FB1AE7107599 | VNMRVF-VSZABPRX-ISP3

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `itcenter http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMRVF-VSZABPRX-ISP3 reported `itcenter http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `3`
- Resolved alerts: `3`
- Open alerts: `0`
- Site code: `RVF`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3366; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2133; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1128`
- Source reference count: `3`

## ALP-FF594A117625 | VNMWBN-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `google http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMWBN-VSSPM02 reported `google http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `3`
- Resolved alerts: `3`
- Open alerts: `0`
- Site code: `WBN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2897; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5108; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5099`
- Source reference count: `3`

## ALP-0CC55237067A | VNMSNT-VSSPM03

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `itcenter http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-VSSPM03 reported `itcenter http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2622; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1137`
- Source reference count: `2`

## ALP-12E1592973B6 | VNMMSB-VSCDC02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-VSCDC02 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1839; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1501`
- Source reference count: `2`

## ALP-169E6406F728 | VNMCCW-FPT-GoogleDNS

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMCCW-FPT-GoogleDNS reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `CCW`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3667; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3473`
- Source reference count: `2`

## ALP-1924544ABA94 | VNMMSH-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi2/0/47(2f-d07-printer): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-PNSSW01 reported `interface gi2/0/47(2f-d07-printer): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1191; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1080`
- Source reference count: `2`

## ALP-19E27B689C58 | VNMCCW-PNCSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface te2/1/2(hub-w4): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMCCW-PNCSW01 reported `interface te2/1/2(hub-w4): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `CCW`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3051; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-713`
- Source reference count: `2`

## ALP-1A953F4706CD | VNMRVF-VSZABPRX-ISP2

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `hris http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMRVF-VSZABPRX-ISP2 reported `hris http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `RVF`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1609; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1386`
- Source reference count: `2`

## ALP-1B829EB90695 | VNMWBN-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `hris http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMWBN-VSSPM02 reported `hris http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `WBN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5107; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5101`
- Source reference count: `2`

## ALP-21A98CCEA4A6 | VNMSWS-PSSJP1

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMSWS-PSSJP1 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `SWS`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3001; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-802`
- Source reference count: `2`

## ALP-2627FC49476B | VNMCCW-FPT-wms.ssc.shopee.vn

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMCCW-FPT-wms.ssc.shopee.vn reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `CCW`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3474; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3396`
- Source reference count: `2`

## ALP-2BE6CD64345B | VNMRVF-VSZABPRX-ISP2

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `itcenter http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMRVF-VSZABPRX-ISP2 reported `itcenter http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `RVF`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4397; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2402`
- Source reference count: `2`

## ALP-3A858B63EFD9 | VNMSGN-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `itcenter http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-VSSPM02 reported `itcenter http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4396; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1388`
- Source reference count: `2`

## ALP-3F151F71EFF2 | VNMMSB-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gigabitethernet0/0/28(thangdv-wifi-test): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-PNSSW01 reported `interface gigabitethernet0/0/28(thangdv-wifi-test): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `2`
- Resolved alerts: `1`
- Open alerts: `1`
- Site code: `MSB`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4965; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4856`
- Source reference count: `2`

## ALP-408776FCDC35 | VNMMSB-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gigabitethernet0/0/27(w-testing-802.1x): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-PNSSW01 reported `interface gigabitethernet0/0/27(w-testing-802.1x): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `2`
- Resolved alerts: `1`
- Open alerts: `1`
- Site code: `MSB`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4859; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4858`
- Source reference count: `2`

## ALP-438E82AC906B | VNMSWS-UPS02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `apc ups: ups is on battery`
- Pattern family: `Power/UPS`
- Investigation priority: `HIGH`
- Why it matters: VNMSWS-UPS02 reported `apc ups: ups is on battery`. This may indicate power/UPS instability and deserves facility or device-side verification.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `SWS`
- Domain: `power`
- Component: `health,power`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2766; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2764`
- Source reference count: `2`

## ALP-4B2D9244DF77 | VNMCCW-PNCSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface po18(hub-w4): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMCCW-PNCSW01 reported `interface po18(hub-w4): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `CCW`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3049; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-712`
- Source reference count: `2`

## ALP-4C656B6E6B0E | VNMMS2-VSEMS01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMS2-VSEMS01 reported `http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `MS2`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1549; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-844`
- Source reference count: `2`

## ALP-50D1D2232E0A | VNMMS2-FPT-FMS-143.92.82.164

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMMS2-FPT-FMS-143.92.82.164 reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `MS2`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3398; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3342`
- Source reference count: `2`

## ALP-64B121F6A433 | VNMMSB-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `google http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-VSSPM01 reported `google http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2896; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2884`
- Source reference count: `2`

## ALP-6A54DDB78966 | VNMMDN-VSDHC01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMMDN-VSDHC01 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `MDN`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-494; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-285`
- Source reference count: `2`

## ALP-740A41E15833 | VNMMSB-FPT-Google

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMMSB-FPT-Google reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1800; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1796`
- Source reference count: `2`

## ALP-79E5CF0FEB8B | VNMWBN-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `google http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMWBN-VSSPM01 reported `google http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `WBN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5105; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5100`
- Source reference count: `2`

## ALP-84056644F10D | VNMWBN-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `hris http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMWBN-VSSPM01 reported `hris http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `WBN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5103; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5096`
- Source reference count: `2`

## ALP-8C1FAECDB82B | VNMMBD-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMBD-VSSPM02 reported `http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `MBD`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2129; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4967`
- Source reference count: `2`

## ALP-8CD6ED07FBD2 | VNMMBD-UPS01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `apc ups: ups is on battery`
- Pattern family: `Power/UPS`
- Investigation priority: `HIGH`
- Why it matters: VNMMBD-UPS01 reported `apc ups: ups is on battery`. This may indicate power/UPS instability and deserves facility or device-side verification.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `MBD`
- Domain: `power`
- Component: `health,power`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1202; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1060`
- Source reference count: `2`

## ALP-8D8DBC00B238 | VNMMBD-psesx01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `dell idrac: nic [nic.embedded.1-1-1/ac:b4:80:4f:b9:cc]: link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMBD-psesx01 reported `dell idrac: nic [nic.embedded.1-1-1/ac:b4:80:4f:b9:cc]: link down`. Treat as monitoring context until corroborated.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `MBD`
- Domain: `hardware`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2340; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2331`
- Source reference count: `2`

## ALP-9EC6DA7FB4A6 | VNMSWS-PNWFW02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface ethernet1/10(): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSWS-PNWFW02 reported `interface ethernet1/10(): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `SWS`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3376; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2999`
- Source reference count: `2`

## ALP-A1CD3F2D2972 | VNMSGN-VSDHC02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-VSDHC02 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1002; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4511`
- Source reference count: `2`

## ALP-A4AD09D79E19 | VNMSNT-VSEMS01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `google http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-VSEMS01 reported `google http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2893; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1010`
- Source reference count: `2`

## ALP-A68F358A138F | VNMSWS-PNCSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface twe2/0/4(ul-pa02): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSWS-PNCSW01 reported `interface twe2/0/4(ul-pa02): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `SWS`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3377; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2998`
- Source reference count: `2`

## ALP-A7A009EBB0BA | VNMCCW-PE-FPT-58.186.223.217

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMCCW-PE-FPT-58.186.223.217 reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `CCW`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3480; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5152`
- Source reference count: `2`

## ALP-AA4ADE38C413 | VNMMBD-UPS02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `apc ups: ups is on battery`
- Pattern family: `Power/UPS`
- Investigation priority: `HIGH`
- Why it matters: VNMMBD-UPS02 reported `apc ups: ups is on battery`. This may indicate power/UPS instability and deserves facility or device-side verification.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `MBD`
- Domain: `power`
- Component: `health,power`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1204; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1061`
- Source reference count: `2`

## ALP-AAFB8AF740C8 | VNMCPL-VSSPM03

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `google http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-VSSPM03 reported `google http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2888; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-647`
- Source reference count: `2`

## ALP-B3579C4A769F | VNMSNT-VSEMS01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `space http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-VSEMS01 reported `space http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4181; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1014`
- Source reference count: `2`

## ALP-B59E873F2699 | VNMSGN-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `hris http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-VSSPM02 reported `hris http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4395; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1387`
- Source reference count: `2`

## ALP-BB890BC9C9F8 | VNMMSH-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `google http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-VSSPM01 reported `google http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1810; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1779`
- Source reference count: `2`

## ALP-BDBD2015F837 | VNMRVF-VSZABPRX-GNL1

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `hris http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMRVF-VSZABPRX-GNL1 reported `hris http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `RVF`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1611; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1132`
- Source reference count: `2`

## ALP-BEB9E5C2842C | VNMSWS-UPS01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `apc ups: ups is on battery`
- Pattern family: `Power/UPS`
- Investigation priority: `HIGH`
- Why it matters: VNMSWS-UPS01 reported `apc ups: ups is on battery`. This may indicate power/UPS instability and deserves facility or device-side verification.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `SWS`
- Domain: `power`
- Component: `health,power`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2762; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-260`
- Source reference count: `2`

## ALP-BFDF2113B363 | VNMWBN-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `itcenter http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMWBN-VSSPM02 reported `itcenter http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `WBN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5106; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5098`
- Source reference count: `2`

## ALP-C8F733B66B3A | VNMMBD-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMBD-VSSPM01 reported `http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `MBD`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3672; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4968`
- Source reference count: `2`

## ALP-D22E642D2402 | VNMCCW-PE-VNPT-wms.ssc.shopee.vn

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMCCW-PE-VNPT-wms.ssc.shopee.vn reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `CCW`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3475; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5147`
- Source reference count: `2`

## ALP-D3970D0F19CF | VNMRVF-VSZABPRX-GNL1

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `confluence http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMRVF-VSZABPRX-GNL1 reported `confluence http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `RVF`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4227; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1619`
- Source reference count: `2`

## ALP-DAA1EB558801 | VNMSNT-VSSPM04

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `hris http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-VSSPM04 reported `hris http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3576; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1009`
- Source reference count: `2`

## ALP-E4A386D887F2 | VNMMBD-PNCSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface xgigabitethernet1/0/17(vnmmbd-pnasw17): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMBD-PNCSW01 reported `interface xgigabitethernet1/0/17(vnmmbd-pnasw17): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `MBD`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2984; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2899`
- Source reference count: `2`

## ALP-E544765B0602 | VNMMSH-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/29(wired-users): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-PNSSW01 reported `interface gi1/0/29(wired-users): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1539; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1193`
- Source reference count: `2`

## ALP-E72A76EFC4A3 | VNMSNT-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `space http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-VSSPM01 reported `space http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4179; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1024`
- Source reference count: `2`

## ALP-E93FF7A65BE9 | VNMCPL-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `google http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-VSSPM01 reported `google http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2895; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-653`
- Source reference count: `2`

## ALP-EB009B8995C2 | VNMMS2-VNPT-GoogleDNS

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMMS2-VNPT-GoogleDNS reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `MS2`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4360; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4358`
- Source reference count: `2`

## ALP-EC07B63B6BF1 | VNMMSB-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gigabitethernet1/0/27(): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-PNSSW01 reported `interface gigabitethernet1/0/27(): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `2`
- Resolved alerts: `1`
- Open alerts: `1`
- Site code: `MSB`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4862; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4857`
- Source reference count: `2`

## ALP-EF2FC71AF04A | VNMCCW-PNCSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface te1/1/2(hub-w4): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMCCW-PNCSW01 reported `interface te1/1/2(hub-w4): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `CCW`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3050; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-714`
- Source reference count: `2`

## ALP-F46BBBBA3D24 | VNMSNT-VSSPM03

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `hris http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-VSSPM03 reported `hris http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2623; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1130`
- Source reference count: `2`

## ALP-FA0CAF592E23 | VNMWBN-PNWSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi2/1/4(fpt-300/<value>-uplink): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMWBN-PNWSW01 reported `interface gi2/1/4(fpt-300/<value>-uplink): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `WBN`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4861; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4849`
- Source reference count: `2`

## ALP-FCB38E8F143B | VNMMSB-VSCDC01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-VSCDC01 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `2`
- Resolved alerts: `2`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1840; zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-308`
- Source reference count: `2`

## ALP-031BE4B5C2DB | VNMMBD-PNWSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface te2/1/8(ul-fpt): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMBD-PNWSW01 reported `interface te2/1/8(ul-fpt): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MBD`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-433`
- Source reference count: `1`

## ALP-0389BEF33E3C | VNMSNT-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `hris http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-VSSPM02 reported `hris http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1006`
- Source reference count: `1`

## ALP-0A71C29255C5 | VNMMSH-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi2/0/6(): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-PNSSW01 reported `interface gi2/0/6(): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4985`
- Source reference count: `1`

## ALP-0AD00BFAE5B7 | VNMSNT-PNCSW2201

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface po24(8data2): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-PNCSW2201 reported `interface po24(8data2): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4449`
- Source reference count: `1`

## ALP-0BC7939B7CD7 | VNMMSH-PNCSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface po101(sw1z-serverroom-dist-sw): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-PNCSW01 reported `interface po101(sw1z-serverroom-dist-sw): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2866`
- Source reference count: `1`

## ALP-0E065BD2D502 | VNMSNT-PNCSW2201

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface po26(8poe2): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-PNCSW2201 reported `interface po26(8poe2): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4455`
- Source reference count: `1`

## ALP-0E415E2C8384 | VNMSGN-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `space http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-VSSPM01 reported `space http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1709`
- Source reference count: `1`

## ALP-0F4DA46294A9 | VNMMS2-FPT-Google

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMS2-FPT-Google reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MS2`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3402`
- Source reference count: `1`

## ALP-13911D374776 | VNMSWS-PSSJP2

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMSWS-PSSJP2 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SWS`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-684`
- Source reference count: `1`

## ALP-158FC3370766 | VNMSNT-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `google http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-VSSPM02 reported `google http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2887`
- Source reference count: `1`

## ALP-17C98F8C50FA | VNMMSB-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface eth-trunk4(san3-bond): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-PNSSW01 reported `interface eth-trunk4(san3-bond): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3571`
- Source reference count: `1`

## ALP-1ACCDDA4E22B | VNMMSB-PSSJP2

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-PSSJP2 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4282`
- Source reference count: `1`

## ALP-1D167D124B85 | VNMCPL-PNWFW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `vnmcpl-pnwfw01 is down!`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMCPL-PNWFW01 reported `vnmcpl-pnwfw01 is down!`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2265`
- Source reference count: `1`

## ALP-1EBDC53DA16E | VNMMSB-FPT-FMS-34.8.101.13

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMSB-FPT-FMS-34.8.101.13 reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1806`
- Source reference count: `1`

## ALP-215907792A0E | VNMRVF-VSZABPRX-ISP3

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `hris http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMRVF-VSZABPRX-ISP3 reported `hris http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `RVF`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1129`
- Source reference count: `1`

## ALP-2762F10D0530 | VNMCPL-VSSPM03

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `hris http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-VSSPM03 reported `hris http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-650`
- Source reference count: `1`

## ALP-27677A872C3F | VNMSNT-VSEMS01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `confluence http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-VSEMS01 reported `confluence http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1007`
- Source reference count: `1`

## ALP-29D8B173B21D | VNMMSB-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gigabitethernet0/0/26(ap-lab1-server): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-PNSSW01 reported `interface gigabitethernet0/0/26(ap-lab1-server): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4851`
- Source reference count: `1`

## ALP-29F27FAA81CA | VNMSNT-PNCSW2201

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface te1/0/25(8poe1): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-PNCSW2201 reported `interface te1/0/25(8poe1): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4452`
- Source reference count: `1`

## ALP-2AB4588032FC | VNMWBN-VSDHC02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMWBN-VSDHC02 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `WBN`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1507`
- Source reference count: `1`

## ALP-2B540009008E | VNMMSB-VNPT-FMS-45.119.218.130

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMSB-VNPT-FMS-45.119.218.130 reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4703`
- Source reference count: `1`

## ALP-2BE3251B74A9 | VNMMS2-PSSJP2

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMMS2-PSSJP2 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MS2`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-800`
- Source reference count: `1`

## ALP-2C985DC126EE | VNMMSB-VNPT-FTTH-GoogleDNS

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMSB-VNPT-FTTH-GoogleDNS reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4352`
- Source reference count: `1`

## ALP-2CA2E82FFCE3 | VNMSNT-PNWSW2201

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi2/0/17(genesys): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-PNWSW2201 reported `interface gi2/0/17(genesys): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2411`
- Source reference count: `1`

## ALP-2CDF8339EE29 | VNMMDN-UPS02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `apc ups: ups is on battery`
- Pattern family: `Power/UPS`
- Investigation priority: `HIGH`
- Why it matters: VNMMDN-UPS02 reported `apc ups: ups is on battery`. This may indicate power/UPS instability and deserves facility or device-side verification.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MDN`
- Domain: `power`
- Component: `health,power`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-120`
- Source reference count: `1`

## ALP-2EEB6A045E46 | VNMRVF-VSDHC01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMRVF-VSDHC01 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `RVF`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1607`
- Source reference count: `1`

## ALP-30B3DE0E9A38 | VNMMSB-FPT-FMS-143.92.82.164

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMSB-FPT-FMS-143.92.82.164 reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1804`
- Source reference count: `1`

## ALP-32DAF214489F | VNMSNT-PNCSW2201

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface te2/0/26(8poe2): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-PNCSW2201 reported `interface te2/0/26(8poe2): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4456`
- Source reference count: `1`

## ALP-32F434F90DB7 | VNMMBD-VSDHC02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMMBD-VSDHC02 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MBD`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4964`
- Source reference count: `1`

## ALP-33AB508A8035 | VNMMSB-VSSPM03

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `zabbix proxy: utilization of icmp pinger processes over 75%`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMSB-VSSPM03 reported `zabbix proxy: utilization of icmp pinger processes over 75%`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `software`
- Component: `data-collector`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4345`
- Source reference count: `1`

## ALP-34774A67A59C | VNMMSB-VNPT-FTTH-143.92.82.164

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMSB-VNPT-FTTH-143.92.82.164 reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4351`
- Source reference count: `1`

## ALP-378E5E671857 | VNMMSH-PNWSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/9(): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-PNWSW01 reported `interface gi1/0/9(): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4982`
- Source reference count: `1`

## ALP-37ECD17812E6 | VNMCCW-PNWSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/1(vnpt): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMCCW-PNWSW01 reported `interface gi1/0/1(vnpt): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CCW`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3479`
- Source reference count: `1`

## ALP-3899CD2333EC | VNMMBD-VSDHC01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMMBD-VSDHC01 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MBD`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4853`
- Source reference count: `1`

## ALP-395C9A3167B7 | VNMCPL-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `hris http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-VSSPM01 reported `hris http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-640`
- Source reference count: `1`

## ALP-3A3CD95E1262 | VNMMSB-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `itcenter http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-VSSPM02 reported `itcenter http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1807`
- Source reference count: `1`

## ALP-3DAA28DDB22C | VNMSNT-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `hris http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-VSSPM01 reported `hris http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1008`
- Source reference count: `1`

## ALP-40578C2A8D55 | VNMMBD-PNCSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface xgigabitethernet1/0/47(vnmmbd-pndsw01): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMBD-PNCSW01 reported `interface xgigabitethernet1/0/47(vnmmbd-pndsw01): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MBD`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2986`
- Source reference count: `1`

## ALP-42399D834774 | VNMMBD-PNDSW01-B

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface xgigabitethernet1/0/1(): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMBD-PNDSW01-B reported `interface xgigabitethernet1/0/1(): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MBD`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2985`
- Source reference count: `1`

## ALP-42F4BF748BE6 | VNMMBD-PNDSW01-B

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface xgigabitethernet1/0/23(asm-b): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMBD-PNDSW01-B reported `interface xgigabitethernet1/0/23(asm-b): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MBD`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4341`
- Source reference count: `1`

## ALP-47027752FDAD | VNMCPL-VSDHC01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: active checks are not available`
- Pattern family: `Zabbix agent/active check`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-VSDHC01 reported `windows: active checks are not available`. This points to monitoring-agent availability rather than confirmed user impact unless supported by ticket or incident evidence.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `os`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-642`
- Source reference count: `1`

## ALP-4B29B0B74364 | VNMMBD-VSSJC1

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: zabbix agent is not available (or nodata for <value>)`
- Pattern family: `Zabbix agent/active check`
- Investigation priority: `LOW`
- Why it matters: VNMMBD-VSSJC1 reported `windows: zabbix agent is not available (or nodata for <value>)`. This points to monitoring-agent availability rather than confirmed user impact unless supported by ticket or incident evidence.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MBD`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2721`
- Source reference count: `1`

## ALP-4E324F9319C9 | VNMSGN-F24-Studio-SW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/13(data): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-F24-Studio-SW01 reported `interface gi1/0/13(data): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `0`
- Open alerts: `1`
- Site code: `SGN`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1671`
- Source reference count: `1`

## ALP-506890DD3166 | VNMMSB-VNPT-GoogleDNS

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMSB-VNPT-GoogleDNS reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4356`
- Source reference count: `1`

## ALP-5081189920F7 | VNMMSB-VSDHC02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: zabbix agent is not available (or nodata for <value>)`
- Pattern family: `Zabbix agent/active check`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-VSDHC02 reported `windows: zabbix agent is not available (or nodata for <value>)`. This points to monitoring-agent availability rather than confirmed user impact unless supported by ticket or incident evidence.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3683`
- Source reference count: `1`

## ALP-556C5581035F | VNMMDN-FPT-210.245.97.132

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMDN-FPT-210.245.97.132 reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MDN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2911`
- Source reference count: `1`

## ALP-577879E16B1D | VNMSNT-PNASW0901

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `switch 2 - power supply b, normal: power supply is in critical state`
- Pattern family: `Power/UPS`
- Investigation priority: `HIGH`
- Why it matters: VNMSNT-PNASW0901 reported `switch 2 - power supply b, normal: power supply is in critical state`. This may indicate power/UPS instability and deserves facility or device-side verification.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `network`
- Component: `power`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3465`
- Source reference count: `1`

## ALP-591C77AE607B | VNMSNT-VSDHC01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: active checks are not available`
- Pattern family: `Zabbix agent/active check`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-VSDHC01 reported `windows: active checks are not available`. This points to monitoring-agent availability rather than confirmed user impact unless supported by ticket or incident evidence.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `os`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1654`
- Source reference count: `1`

## ALP-5977C8EFB475 | VNMMSB-PNWSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface te1/1/7(fpt<value>/<value>-uplink): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-PNWSW01 reported `interface te1/1/7(fpt<value>/<value>-uplink): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1403`
- Source reference count: `1`

## ALP-5A159D9F292E | VNMCPL-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface po2(host<value>-vswitch0): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-PNSSW01 reported `interface po2(host<value>-vswitch0): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `0`
- Open alerts: `1`
- Site code: `CPL`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5110`
- Source reference count: `1`

## ALP-5B5E5BD02F39 | VNMMSH-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `hris http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-VSSPM02 reported `hris http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1777`
- Source reference count: `1`

## ALP-5D25CF3F9C92 | VNMCCW-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `zabbix proxy: utilization of icmp pinger processes over 75%`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMCCW-VSSPM02 reported `zabbix proxy: utilization of icmp pinger processes over 75%`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CCW`
- Domain: `software`
- Component: `data-collector`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5144`
- Source reference count: `1`

## ALP-5DD89370D4CE | VNMSNT-UPSF2201

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `3: unacceptable phase 3 input voltage (out of range 197-243v for <value>)`
- Pattern family: `Power/UPS`
- Investigation priority: `HIGH`
- Why it matters: VNMSNT-UPSF2201 reported `3: unacceptable phase 3 input voltage (out of range 197-243v for <value>)`. This may indicate power/UPS instability and deserves facility or device-side verification.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `power`
- Component: `power`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4457`
- Source reference count: `1`

## ALP-5E2F23C33812 | VNMCPL-VSSPM04

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `google http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-VSSPM04 reported `google http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-649`
- Source reference count: `1`

## ALP-6330A778B101 | VNMCCW-PNWSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface te1/1/1(vnpt): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMCCW-PNWSW01 reported `interface te1/1/1(vnpt): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CCW`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5151`
- Source reference count: `1`

## ALP-65018137D406 | VNMSNT-VSDHC01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-VSDHC01 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1649`
- Source reference count: `1`

## ALP-6800C5E0DF8A | VNMCCW-VNPT-GoogleDNS

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMCCW-VNPT-GoogleDNS reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CCW`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5148`
- Source reference count: `1`

## ALP-685FDC71F87F | VNMCPL-PNASW0504

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `cisco ios: unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMCPL-PNASW0504 reported `cisco ios: unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `network`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2259`
- Source reference count: `1`

## ALP-69B703E5D70F | VNMSGN-PNWSW2501

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/1/1(viettelidc-grn): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-PNWSW2501 reported `interface gi1/1/1(viettelidc-grn): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4854`
- Source reference count: `1`

## ALP-6B66EDD4D5A6 | VNMMDN-Netnam-FMS-Google

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMDN-Netnam-FMS-Google reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MDN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3670`
- Source reference count: `1`

## ALP-6C98DB159A7E | VNMSWS-VSDHC02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMSWS-VSDHC02 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SWS`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1665`
- Source reference count: `1`

## ALP-6D8FB8F22DF8 | VNMRVF-VSZABPRX-GNL1

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `itcenter http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMRVF-VSZABPRX-GNL1 reported `itcenter http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `RVF`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1618`
- Source reference count: `1`

## ALP-6E01E457377C | VNMMBD-VSDHC02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: active checks are not available`
- Pattern family: `Zabbix agent/active check`
- Investigation priority: `LOW`
- Why it matters: VNMMBD-VSDHC02 reported `windows: active checks are not available`. This points to monitoring-agent availability rather than confirmed user impact unless supported by ticket or incident evidence.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MBD`
- Domain: `os`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1888`
- Source reference count: `1`

## ALP-6ECC84A13DA9 | VNMCCW-PE-VNPT-14.238.87.209

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMCCW-PE-VNPT-14.238.87.209 reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CCW`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5149`
- Source reference count: `1`

## ALP-6F75CFE0BFF3 | VNMMSB-VSDHC02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-VSDHC02 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1509`
- Source reference count: `1`

## ALP-701EB4EAF3E4 | VNMSNT-VSDHC01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: high swap space usage (less than 20% free)`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-VSDHC01 reported `windows: high swap space usage (less than 20% free)`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `os`
- Component: `memory,storage`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1677`
- Source reference count: `1`

## ALP-715B814B3F78 | VNMMSB-FPT-GoogleDNS

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMSB-FPT-GoogleDNS reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1811`
- Source reference count: `1`

## ALP-741B9E5DD901 | VNMSGN-VSEMS01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `google http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-VSEMS01 reported `google http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2898`
- Source reference count: `1`

## ALP-746BFE15BC81 | VNMRVF-VSDHC02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMRVF-VSDHC02 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `RVF`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1608`
- Source reference count: `1`

## ALP-773FF6B91B85 | VNMSNT-PNASW0801

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `cisco ios: unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMSNT-PNASW0801 reported `cisco ios: unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `network`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4445`
- Source reference count: `1`

## ALP-784607BD3933 | VNMMSB-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `hris http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-VSSPM02 reported `hris http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1797`
- Source reference count: `1`

## ALP-79F64BE83962 | VNMMSH-PNWSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/8(): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-PNWSW01 reported `interface gi1/0/8(): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4984`
- Source reference count: `1`

## ALP-7A327195B442 | VNMSNT-VSDHC02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-VSDHC02 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1657`
- Source reference count: `1`

## ALP-7A6A6B2F3886 | VNMCPL-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `itcenter http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-VSSPM02 reported `itcenter http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-646`
- Source reference count: `1`

## ALP-7A7AC21E2062 | VNMSGN-VSDHC02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: active checks are not available`
- Pattern family: `Zabbix agent/active check`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-VSDHC02 reported `windows: active checks are not available`. This points to monitoring-agent availability rather than confirmed user impact unless supported by ticket or incident evidence.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `os`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4512`
- Source reference count: `1`

## ALP-7BEA8E6CB5D2 | VNMRVF-VSZABPRX-GNL1

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `google http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMRVF-VSZABPRX-GNL1 reported `google http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `RVF`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1615`
- Source reference count: `1`

## ALP-7C0331E2C3F9 | VNMMS2-FPT-FMS-143.92.88.13

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMS2-FPT-FMS-143.92.88.13 reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MS2`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3399`
- Source reference count: `1`

## ALP-7F7A2D2BCBD0 | VNMMSH-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `space http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-VSSPM01 reported `space http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1689`
- Source reference count: `1`

## ALP-828108BA1BC0 | VNMSGN-PNWSW2501

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi2/1/2(cmc-grn): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-PNWSW2501 reported `interface gi2/1/2(cmc-grn): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `0`
- Open alerts: `1`
- Site code: `SGN`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1297`
- Source reference count: `1`

## ALP-8338B49EE2A0 | VNMMSH-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi2/0/11(host5d-idrac-temp): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-PNSSW01 reported `interface gi2/0/11(host5d-idrac-temp): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3483`
- Source reference count: `1`

## ALP-8343732F4E8F | VNMMS2-VSSPM04

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMS2-VSSPM04 reported `http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MS2`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1546`
- Source reference count: `1`

## ALP-83F3E80812B5 | VNMMSB-VSSPM03

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `itcenter http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-VSSPM03 reported `itcenter http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4346`
- Source reference count: `1`

## ALP-8431FCD99A93 | VNMMSH-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `hris http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-VSSPM01 reported `hris http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1780`
- Source reference count: `1`

## ALP-8502BDAE29F6 | VNMMS2-VSDHC01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMMS2-VSDHC01 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MS2`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1545`
- Source reference count: `1`

## ALP-8512B88F2512 | VNMMBD-FPT-FMS-143.92.82.164

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMBD-FPT-FMS-143.92.82.164 reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MBD`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3343`
- Source reference count: `1`

## ALP-86345183DF87 | VNMSNT-VSDHC01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: zabbix agent is not available (or nodata for <value>)`
- Pattern family: `Zabbix agent/active check`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-VSDHC01 reported `windows: zabbix agent is not available (or nodata for <value>)`. This points to monitoring-agent availability rather than confirmed user impact unless supported by ticket or incident evidence.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1650`
- Source reference count: `1`

## ALP-8640D0A99E69 | VNMMSB-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gigabitethernet1/0/28(): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-PNSSW01 reported `interface gigabitethernet1/0/28(): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `0`
- Open alerts: `1`
- Site code: `MSB`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4855`
- Source reference count: `1`

## ALP-8BA568D15E14 | VNMCPL-PNASW0402

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `cisco ios: unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMCPL-PNASW0402 reported `cisco ios: unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `network`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2264`
- Source reference count: `1`

## ALP-8E2A248C8ADD | VNMSGN-VSSPM03

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `space http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-VSSPM03 reported `space http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1704`
- Source reference count: `1`

## ALP-90723BD1730B | VNMCPL-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi2/0/47(host<value>-idrac): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-PNSSW01 reported `interface gi2/0/47(host<value>-idrac): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `0`
- Open alerts: `1`
- Site code: `CPL`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5111`
- Source reference count: `1`

## ALP-90793ED28AF7 | VNMMBD-PSSJP2

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMMBD-PSSJP2 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MBD`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-660`
- Source reference count: `1`

## ALP-919D1DAA3ADF | VNMSNT-UPSF2201

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `2: unacceptable phase 2 input voltage (out of range 197-243v for <value>)`
- Pattern family: `Power/UPS`
- Investigation priority: `HIGH`
- Why it matters: VNMSNT-UPSF2201 reported `2: unacceptable phase 2 input voltage (out of range 197-243v for <value>)`. This may indicate power/UPS instability and deserves facility or device-side verification.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `power`
- Component: `power`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4458`
- Source reference count: `1`

## ALP-93544488C14D | VNMSNT-PNCSW2201

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface po25(8poe1): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-PNCSW2201 reported `interface po25(8poe1): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4448`
- Source reference count: `1`

## ALP-93A5CD8B721E | VNMCPL-PNASW0601

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `cisco ios: unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMCPL-PNASW0601 reported `cisco ios: unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `network`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2258`
- Source reference count: `1`

## ALP-943BE1CC9684 | VNMMSB-VSDHC01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-VSDHC01 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-313`
- Source reference count: `1`

## ALP-9576674AA3D1 | VNMMSB-PE-FPT-42.115.45.57

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMSB-PE-FPT-42.115.45.57 reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1801`
- Source reference count: `1`

## ALP-95C8531458B4 | VNMMDN-PNCSW01-1-2

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface 50:00:e0:4f:9b:80/1/c9300x-nm-8y/1: link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMDN-PNCSW01-1-2 reported `interface 50:00:e0:4f:9b:80/1/c9300x-nm-8y/1: link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MDN`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2912`
- Source reference count: `1`

## ALP-978DF6D26A6B | VNW3-VSDHC02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNW3-VSDHC02 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `UNKNOWN`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1663`
- Source reference count: `1`

## ALP-97B938A73B4B | VNMWBN-VSDHC01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMWBN-VSDHC01 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `WBN`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-310`
- Source reference count: `1`

## ALP-9D1DC3A5A925 | VNMMSB-VSDHC02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: active checks are not available`
- Pattern family: `Zabbix agent/active check`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-VSDHC02 reported `windows: active checks are not available`. This points to monitoring-agent availability rather than confirmed user impact unless supported by ticket or incident evidence.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `os`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3687`
- Source reference count: `1`

## ALP-9D6FB01CB240 | VNMMSH-PNWSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface po6(host6d-vswitch1): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-PNWSW01 reported `interface po6(host6d-vswitch1): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4981`
- Source reference count: `1`

## ALP-9E76E02BF1B3 | VNMMDN-FPT-Google

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMDN-FPT-Google reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MDN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3669`
- Source reference count: `1`

## ALP-9F30948925E8 | VNMMSB-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gigabitethernet0/0/25(ap-lab2-server): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-PNSSW01 reported `interface gigabitethernet0/0/25(ap-lab2-server): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4852`
- Source reference count: `1`

## ALP-9FEAFFFBD7D9 | VNMSNT-VSSPM03

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `google http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-VSSPM03 reported `google http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2886`
- Source reference count: `1`

## ALP-A035897B33D7 | VNMCCW-PNASW04

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `cisco ios: unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMCCW-PNASW04 reported `cisco ios: unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CCW`
- Domain: `network`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-710`
- Source reference count: `1`

## ALP-A0899C9F3685 | VNMMSH-VSDHC01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-VSDHC01 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4835`
- Source reference count: `1`

## ALP-A090C47934DD | VNMMSB-VSSPM03

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `hris http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-VSSPM03 reported `hris http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4348`
- Source reference count: `1`

## ALP-A0A7C8335F8A | VNMSWS-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `zabbix proxy: utilization of icmp pinger processes over 75%`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMSWS-VSSPM01 reported `zabbix proxy: utilization of icmp pinger processes over 75%`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `0`
- Open alerts: `1`
- Site code: `SWS`
- Domain: `software`
- Component: `data-collector`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-768`
- Source reference count: `1`

## ALP-A214305CA9E3 | VNMSNT-PNASW0902

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `switch 4 - power supply a, normal: power supply is in critical state`
- Pattern family: `Power/UPS`
- Investigation priority: `HIGH`
- Why it matters: VNMSNT-PNASW0902 reported `switch 4 - power supply a, normal: power supply is in critical state`. This may indicate power/UPS instability and deserves facility or device-side verification.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `network`
- Component: `power`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3463`
- Source reference count: `1`

## ALP-A24FE3830B4B | VNMSNT-PNASW0802

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `cisco ios: unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMSNT-PNASW0802 reported `cisco ios: unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `network`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4446`
- Source reference count: `1`

## ALP-A37DF63F13A8 | VNMCPL-VSDHC01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-VSDHC01 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-641`
- Source reference count: `1`

## ALP-A4089FD15772 | VNMCCW-PNWSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi2/0/3(fpt): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMCCW-PNWSW01 reported `interface gi2/0/3(fpt): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CCW`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3481`
- Source reference count: `1`

## ALP-A4BA48DD3E68 | VNMSNT-PNASW0902

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `switch 6 - power supply a, normal: power supply is in critical state`
- Pattern family: `Power/UPS`
- Investigation priority: `HIGH`
- Why it matters: VNMSNT-PNASW0902 reported `switch 6 - power supply a, normal: power supply is in critical state`. This may indicate power/UPS instability and deserves facility or device-side verification.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `network`
- Component: `power`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3464`
- Source reference count: `1`

## ALP-A7B1C779DB26 | VNMMSB-FPT-FMS-143.92.88.13

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMSB-FPT-FMS-143.92.88.13 reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1803`
- Source reference count: `1`

## ALP-A8AC346B8ED6 | VNMSGN-VSEMS01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `space http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-VSEMS01 reported `space http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1703`
- Source reference count: `1`

## ALP-A9E721DBF400 | VNMCPL-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi2/0/1(host<value>-gi2-vmnic1): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-PNSSW01 reported `interface gi2/0/1(host<value>-gi2-vmnic1): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `0`
- Open alerts: `1`
- Site code: `CPL`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5113`
- Source reference count: `1`

## ALP-AB38560C5F2E | VNMMS2-FPT-GoogleDNS

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMS2-FPT-GoogleDNS reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MS2`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3400`
- Source reference count: `1`

## ALP-AC5823A356F9 | VNMCPL-PNASW0503

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `cisco ios: unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMCPL-PNASW0503 reported `cisco ios: unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `network`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2263`
- Source reference count: `1`

## ALP-ADB14EE9325B | VNMMSB-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `google http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-VSSPM02 reported `google http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1799`
- Source reference count: `1`

## ALP-B0472F3ECDF7 | VNMMSB-VSCDC01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: active checks are not available`
- Pattern family: `Zabbix agent/active check`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-VSCDC01 reported `windows: active checks are not available`. This points to monitoring-agent availability rather than confirmed user impact unless supported by ticket or incident evidence.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `os`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-307`
- Source reference count: `1`

## ALP-B259C1B104BD | VNMSNT-PNASW0804

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `cisco ios: unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMSNT-PNASW0804 reported `cisco ios: unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `network`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4443`
- Source reference count: `1`

## ALP-B331868ACD35 | VNMCPL-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/4(vmotion): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-PNSSW01 reported `interface gi1/0/4(vmotion): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `0`
- Open alerts: `1`
- Site code: `CPL`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5120`
- Source reference count: `1`

## ALP-B5D5D69DC10D | VNMMSB-VNPT-FTTH-spx.shopee.vn

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMSB-VNPT-FTTH-spx.shopee.vn reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4353`
- Source reference count: `1`

## ALP-B8846D1E4DB8 | VNMSNT-PNASW0803

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `cisco ios: unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMSNT-PNASW0803 reported `cisco ios: unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `network`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4444`
- Source reference count: `1`

## ALP-B8C29BDC1FFA | VNMMDN-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMDN-VSSPM02 reported `http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MDN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-495`
- Source reference count: `1`

## ALP-BACB26822D0F | VNMCPL-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/1(host<value>-gi1-vmnic0): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-PNSSW01 reported `interface gi1/0/1(host<value>-gi1-vmnic0): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `0`
- Open alerts: `1`
- Site code: `CPL`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5112`
- Source reference count: `1`

## ALP-BB3EEB369423 | VNMCPL-PNASW0501

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `cisco ios: unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMCPL-PNASW0501 reported `cisco ios: unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `network`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2260`
- Source reference count: `1`

## ALP-BB5483F45134 | VNMMSB-VNPT-FTTH-Google

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMSB-VNPT-FTTH-Google reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4349`
- Source reference count: `1`

## ALP-C031A95EC809 | VNMMBD-VSDHC02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: zabbix agent is not available (or nodata for <value>)`
- Pattern family: `Zabbix agent/active check`
- Investigation priority: `LOW`
- Why it matters: VNMMBD-VSDHC02 reported `windows: zabbix agent is not available (or nodata for <value>)`. This points to monitoring-agent availability rather than confirmed user impact unless supported by ticket or incident evidence.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MBD`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1886`
- Source reference count: `1`

## ALP-C05AD23FBDDF | VNMSWS-VSDHC01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMSWS-VSDHC01 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SWS`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1661`
- Source reference count: `1`

## ALP-C0D0547A5EB2 | VNMMSB-VSNPS01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-VSNPS01 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-314`
- Source reference count: `1`

## ALP-C11640894E54 | VNMMSB-PNWSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface te2/1/7(vnpt-ftth-<value>/<value>-uplink): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-PNWSW01 reported `interface te2/1/7(vnpt-ftth-<value>/<value>-uplink): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4354`
- Source reference count: `1`

## ALP-C16BA6A2D932 | VNMCPL-PNASW0502

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `cisco ios: unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMCPL-PNASW0502 reported `cisco ios: unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `network`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2262`
- Source reference count: `1`

## ALP-C292F7633781 | VNMMSH-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `space http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-VSSPM02 reported `space http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1688`
- Source reference count: `1`

## ALP-C5593B47AC08 | VNMMSH-PNWSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface te1/1/7(fpt<value>/<value>-uplink): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-PNWSW01 reported `interface te1/1/7(fpt<value>/<value>-uplink): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2869`
- Source reference count: `1`

## ALP-C57961CC104D | VNMMSB-VSSPM03

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `google http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-VSSPM03 reported `google http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4347`
- Source reference count: `1`

## ALP-C6A753AA8DAF | VNMCPL-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi2/0/48(host<value>-idrac): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-PNSSW01 reported `interface gi2/0/48(host<value>-idrac): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `0`
- Open alerts: `1`
- Site code: `CPL`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5117`
- Source reference count: `1`

## ALP-C8D9E49F883D | VNMMSH-VSDHC02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: zabbix agent is not available (or nodata for <value>)`
- Pattern family: `Zabbix agent/active check`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-VSDHC02 reported `windows: zabbix agent is not available (or nodata for <value>)`. This points to monitoring-agent availability rather than confirmed user impact unless supported by ticket or incident evidence.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4721`
- Source reference count: `1`

## ALP-C8F1CFFBCC61 | VNMSNT-PNCSW2201

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface te2/0/25(8poe1): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-PNCSW2201 reported `interface te2/0/25(8poe1): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4454`
- Source reference count: `1`

## ALP-CCD676EF5C72 | VNMWBN-VSDHC01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: active checks are not available`
- Pattern family: `Zabbix agent/active check`
- Investigation priority: `LOW`
- Why it matters: VNMWBN-VSDHC01 reported `windows: active checks are not available`. This points to monitoring-agent availability rather than confirmed user impact unless supported by ticket or incident evidence.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `WBN`
- Domain: `os`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-312`
- Source reference count: `1`

## ALP-CDCB1323E9CB | VNMMBD-PE-FPT-42.116.48.97

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMBD-PE-FPT-42.116.48.97 reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MBD`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-432`
- Source reference count: `1`

## ALP-CFD7410A0332 | VNMMDN-UPS01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `apc ups: ups is on battery`
- Pattern family: `Power/UPS`
- Investigation priority: `HIGH`
- Why it matters: VNMMDN-UPS01 reported `apc ups: ups is on battery`. This may indicate power/UPS instability and deserves facility or device-side verification.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MDN`
- Domain: `power`
- Component: `health,power`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-121`
- Source reference count: `1`

## ALP-D05553CC376F | VNMMBD-PSSJP1

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMMBD-PSSJP1 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MBD`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-683`
- Source reference count: `1`

## ALP-D1920754A7A0 | VNMSNT-UPSF2201

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `apc ups: ups is on battery`
- Pattern family: `Power/UPS`
- Investigation priority: `HIGH`
- Why it matters: VNMSNT-UPSF2201 reported `apc ups: ups is on battery`. This may indicate power/UPS instability and deserves facility or device-side verification.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `power`
- Component: `health,power`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4459`
- Source reference count: `1`

## ALP-D3800D122BE2 | VNMMSB-PSSJP1

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-PSSJP1 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4617`
- Source reference count: `1`

## ALP-D43B71C6DCFA | VNMSNT-PNCSW2201

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface te1/0/30(7poe2): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-PNCSW2201 reported `interface te1/0/30(7poe2): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2490`
- Source reference count: `1`

## ALP-D50C2032C859 | VNMSNT-PNCSW2201

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface te1/0/23(8data1): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-PNCSW2201 reported `interface te1/0/23(8data1): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4450`
- Source reference count: `1`

## ALP-D5C79ADBA448 | VNMMSB-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `zabbix proxy: utilization of icmp pinger processes over 75%`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMSB-VSSPM01 reported `zabbix proxy: utilization of icmp pinger processes over 75%`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `0`
- Open alerts: `1`
- Site code: `MSB`
- Domain: `software`
- Component: `data-collector`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-311`
- Source reference count: `1`

## ALP-D8D267F610B0 | VNMMS2-FPT-FMS-34.8.101.13

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMS2-FPT-FMS-34.8.101.13 reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MS2`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3668`
- Source reference count: `1`

## ALP-D8D97AF05ACC | VNMMSB-VNPT-FTTH-143.92.88.13

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMSB-VNPT-FTTH-143.92.88.13 reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4350`
- Source reference count: `1`

## ALP-DBAC421A5888 | VNMRVF-VSZABPRX-ISP1

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `hris http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMRVF-VSZABPRX-ISP1 reported `hris http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `RVF`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1610`
- Source reference count: `1`

## ALP-DBD3239DB30B | VNMSNT-PNASW0902

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `switch 3 - power supply a, normal: power supply is in critical state`
- Pattern family: `Power/UPS`
- Investigation priority: `HIGH`
- Why it matters: VNMSNT-PNASW0902 reported `switch 3 - power supply a, normal: power supply is in critical state`. This may indicate power/UPS instability and deserves facility or device-side verification.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `network`
- Component: `power`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-3466`
- Source reference count: `1`

## ALP-DC34A037CC91 | VNMMSB-PSSJP2

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: zabbix agent is not available (or nodata for <value>)`
- Pattern family: `Zabbix agent/active check`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-PSSJP2 reported `windows: zabbix agent is not available (or nodata for <value>)`. This points to monitoring-agent availability rather than confirmed user impact unless supported by ticket or incident evidence.
- Raw alert count: `1`
- Resolved alerts: `0`
- Open alerts: `1`
- Site code: `MSB`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-434`
- Source reference count: `1`

## ALP-DDAF4871FEF9 | VNMCPL-PNWSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/3(host<value>-gi6): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-PNWSW01 reported `interface gi1/0/3(host<value>-gi6): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `0`
- Open alerts: `1`
- Site code: `CPL`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5121`
- Source reference count: `1`

## ALP-DDC053EAD407 | VNMMS2-PNCSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface xgigabitethernet0/0/22(*** asm ***): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMS2-PNCSW01 reported `interface xgigabitethernet0/0/22(*** asm ***): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MS2`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-709`
- Source reference count: `1`

## ALP-DDC89EABBC6F | VNMMS2-VSDHC02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMMS2-VSDHC02 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MS2`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1543`
- Source reference count: `1`

## ALP-E0910AC65DBF | VNMSGN-VSSPM02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `space http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-VSSPM02 reported `space http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1690`
- Source reference count: `1`

## ALP-E0F3EC588E32 | VNMCPL-PNWFW02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `vnmcpl-pnwfw02 is down!`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMCPL-PNWFW02 reported `vnmcpl-pnwfw02 is down!`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2266`
- Source reference count: `1`

## ALP-E45DD97FFD35 | VNMCPL-PNWSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi2/0/3(host<value>-gi6): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-PNWSW01 reported `interface gi2/0/3(host<value>-gi6): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `0`
- Open alerts: `1`
- Site code: `CPL`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5114`
- Source reference count: `1`

## ALP-E4E93AA18409 | VNMSNT-PNSSW2201

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/34(cctv): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-PNSSW2201 reported `interface gi1/0/34(cctv): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4447`
- Source reference count: `1`

## ALP-E5E787AEEC50 | VNMCPL-PNASW0401

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `cisco ios: unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMCPL-PNASW0401 reported `cisco ios: unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `network`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2261`
- Source reference count: `1`

## ALP-E6D0338FF897 | VNMMSH-VSDHC01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: active checks are not available`
- Pattern family: `Zabbix agent/active check`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-VSDHC01 reported `windows: active checks are not available`. This points to monitoring-agent availability rather than confirmed user impact unless supported by ticket or incident evidence.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `os`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4836`
- Source reference count: `1`

## ALP-E73E2E9B79D8 | VNMCPL-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `itcenter http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-VSSPM01 reported `itcenter http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-648`
- Source reference count: `1`

## ALP-E89923DA4A76 | VNW3-VSDHC01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNW3-VSDHC01 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `UNKNOWN`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1676`
- Source reference count: `1`

## ALP-E91C7BC7C5E8 | VNMSGN-VSDHC01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMSGN-VSDHC01 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SGN`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1664`
- Source reference count: `1`

## ALP-E97AD6C8AC63 | VNMMDN-VSDHC02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMMDN-VSDHC02 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MDN`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1506`
- Source reference count: `1`

## ALP-EA2547CCB5B4 | VNMCPL-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi2/0/2(host<value>-gi2-vmnic1): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-PNSSW01 reported `interface gi2/0/2(host<value>-gi2-vmnic1): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `0`
- Open alerts: `1`
- Site code: `CPL`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5118`
- Source reference count: `1`

## ALP-EAC35F59F3C7 | VNMRVF-VSZABPRX-ISP2

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `google http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMRVF-VSZABPRX-ISP2 reported `google http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `RVF`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2890`
- Source reference count: `1`

## ALP-EB7AA52C976B | VNMSNT-PNCSW2201

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface te1/0/24(8data2): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-PNCSW2201 reported `interface te1/0/24(8data2): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4453`
- Source reference count: `1`

## ALP-EC109E3B374B | VNMCPL-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `cisco ios: unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `HIGH`
- Why it matters: VNMCPL-PNSSW01 reported `cisco ios: unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `network`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2257`
- Source reference count: `1`

## ALP-EC47E5EBE854 | VNMMBD-PNCSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface xgigabitethernet1/0/18(vnmmbd-pnasw18): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMBD-PNCSW01 reported `interface xgigabitethernet1/0/18(vnmmbd-pnasw18): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MBD`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2983`
- Source reference count: `1`

## ALP-EDE4F54B9DA5 | VNMMSB-FPT-spx.shopee.vn

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `unavailable by icmp ping`
- Pattern family: `Network reachability`
- Investigation priority: `MEDIUM`
- Why it matters: VNMMSB-FPT-spx.shopee.vn reported `unavailable by icmp ping`. This can indicate short connectivity loss, device/path flap, or monitoring-path instability and should be checked before HTTP-only noise.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1802`
- Source reference count: `1`

## ALP-EE35CFAF0367 | VNMMSB-PSSJP2

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: active checks are not available`
- Pattern family: `Zabbix agent/active check`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-PSSJP2 reported `windows: active checks are not available`. This points to monitoring-agent availability rather than confirmed user impact unless supported by ticket or incident evidence.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `os`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-435`
- Source reference count: `1`

## ALP-EECED11193F9 | VNMMSH-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/14(2f-d26): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-PNSSW01 reported `interface gi1/0/14(2f-d26): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4962`
- Source reference count: `1`

## ALP-F00DBD58B8BB | VNMMBD-VSSJC1

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: active checks are not available`
- Pattern family: `Zabbix agent/active check`
- Investigation priority: `LOW`
- Why it matters: VNMMBD-VSSJC1 reported `windows: active checks are not available`. This points to monitoring-agent availability rather than confirmed user impact unless supported by ticket or incident evidence.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MBD`
- Domain: `os`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2724`
- Source reference count: `1`

## ALP-F03598513528 | VNMCPL-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface po3(host<value>-vswitch0): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-PNSSW01 reported `interface po3(host<value>-vswitch0): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `0`
- Open alerts: `1`
- Site code: `CPL`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5115`
- Source reference count: `1`

## ALP-F1668F6EA566 | VNMCPL-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi2/0/4(vmotion): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-PNSSW01 reported `interface gi2/0/4(vmotion): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `0`
- Open alerts: `1`
- Site code: `CPL`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5119`
- Source reference count: `1`

## ALP-F1C41227391E | VNMRVF-VSZABPRX-ISP3

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `google http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMRVF-VSZABPRX-ISP3 reported `google http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `RVF`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2134`
- Source reference count: `1`

## ALP-F4C168804DC2 | VNMCPL-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/47(host8o-idrac): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-PNSSW01 reported `interface gi1/0/47(host8o-idrac): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2875`
- Source reference count: `1`

## ALP-F6D0BF16C98C | VNMMSB-VSCDC02

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: active checks are not available`
- Pattern family: `Zabbix agent/active check`
- Investigation priority: `LOW`
- Why it matters: VNMMSB-VSCDC02 reported `windows: active checks are not available`. This points to monitoring-agent availability rather than confirmed user impact unless supported by ticket or incident evidence.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSB`
- Domain: `os`
- Component: `health,network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1502`
- Source reference count: `1`

## ALP-F78AB4D74642 | VNMMS2-PSSJP1

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `windows: host has been restarted (uptime < <value>)`
- Pattern family: `Host restart/uptime`
- Investigation priority: `LOW`
- Why it matters: VNMMS2-PSSJP1 reported `windows: host has been restarted (uptime < <value>)`. This is host-health context and should not be treated as service impact without another source.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MS2`
- Domain: `os`
- Component: `system`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-761`
- Source reference count: `1`

## ALP-F9EB35FEEFE0 | VNMCPL-VSSPM04

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `confluence http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-VSSPM04 reported `confluence http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `CPL`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2758`
- Source reference count: `1`

## ALP-FB03B1D03422 | VNMCPL-PNSSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface gi1/0/2(host<value>-gi2-vmnic0): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMCPL-PNSSW01 reported `interface gi1/0/2(host<value>-gi2-vmnic0): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `0`
- Open alerts: `1`
- Site code: `CPL`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-5116`
- Source reference count: `1`

## ALP-FB055D5123B8 | VNMMSH-PNCSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface twe2/0/10(sw1z-serverroom-dist-sw-te2/1/8): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-PNCSW01 reported `interface twe2/0/10(sw1z-serverroom-dist-sw-te2/1/8): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-2867`
- Source reference count: `1`

## ALP-FBB608413C7B | VNMSNT-PNCSW2201

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface te1/0/26(8poe2): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMSNT-PNCSW2201 reported `interface te1/0/26(8poe2): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `SNT`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4451`
- Source reference count: `1`

## ALP-FE3C38E2DC07 | VNMMSH-VSSPM01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `itcenter http monitoring`
- Pattern family: `HTTP monitoring`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-VSSPM01 reported `itcenter http monitoring`. This usually means application/service probe thresholds were crossed; investigate threshold sensitivity, maintenance windows, or repeated endpoint timeouts.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `UNKNOWN`
- Component: `UNKNOWN`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-1778`
- Source reference count: `1`

## ALP-FF540929BD75 | VNMMSH-PNWSW01

- Evidence label: `COMPUTED FACT`
- Assessment: `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT`
- Problem signature: `interface po5(host5d-vswitch1): link down`
- Pattern family: `Other`
- Investigation priority: `LOW`
- Why it matters: VNMMSH-PNWSW01 reported `interface po5(host5d-vswitch1): link down`. Treat as monitoring context until corroborated.
- Raw alert count: `1`
- Resolved alerts: `1`
- Open alerts: `0`
- Site code: `MSH`
- Domain: `network`
- Component: `network`
- Source references: `zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv#csv:row-4983`
- Source reference count: `1`
