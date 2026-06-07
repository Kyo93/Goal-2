# Sample Package Validation Record

## Phạm Vi

Biên bản này ghi lại quality gate cho package sinh từ ba raw export hiện có tại ngày `2026-06-02`.

Lệnh build:

```powershell
python scripts\build_alpha_knowledge_package.py `
  --raw-dir 01-RawData `
  --master-data "03-Data clean logic\reference doc\it-operations-master-data-template.xlsx" `
  --output-dir 02-Output\alpha-knowledge-package
```

## Automated Gate

```text
python -m unittest discover -s tests -v
Ran 16 tests
OK
```

Build kép với cùng input và cùng `generated_at`:

```text
text_content_mismatches = []
audit_workbook_values_equal = true
validation_status = PASS
upload_allowed = true
```

## Reconciliation

| Metric | Count |
| --- | ---: |
| Confirmed incidents | 52 |
| Raw Zabbix alerts | 5199 |
| Alert patterns | 365 |
| Unique tickets | 2681 |
| Issue comment rows | 9525 |
| Incident recurrence patterns | 27 |
| Operational stories | 417 |
| Timeline confirmed-incident events | 52 |
| Timeline Zabbix-pattern events | 365 |
| Rejected incident rows | 0 |
| Rejected alert rows | 0 |
| Rejected ticket-comment rows | 0 |

Các invariant incident, Zabbix, và issue-comment reconciliation đều `PASS`.

## Retrieval Structure Check

| Markdown | `##` sections | Source-reference sections |
| --- | ---: | ---: |
| `02_operational_timeline.md` | 418 including usage section | 417 |
| `02_confirmed_incidents.md` | 52 | 52 |
| `03_recurrence_patterns.md` | 27 | 27 |
| `04_alert_patterns.md` | 367 | 365 |
| `05_ticket_impact.md` | 2681 | 2681 |
| `05_ticket_impact_index.md` | 2 | 0 |
| `05_ticket_impact_2026_04.md` | 1561 | 1561 |
| `05_ticket_impact_2026_05.md` | 1282 | 1282 |
| `05_ticket_impact_2026_06.md` | 500 | 500 |

Tất cả Markdown đọc được bằng UTF-8 và không phát hiện mojibake marker.

## Operational Story Audit

`02_operational_timeline.md` is now the primary date-range investigation entry point.
The audit workbook contains an `operational_timeline` sheet with `417` story rows.
Every story includes `Timeline`, `Conclusion`, and `Investigation gaps`.

Confirmed-incident responsibility classification:

| Domain | Incident count |
| --- | ---: |
| `ISP` | 42 |
| `INHOUSE` | 3 |
| `EXTERNAL` | 1 |
| `UNKNOWN` | 6 |

Confirmed-incident user-impact evidence:

| Status | Incident count |
| --- | ---: |
| `CONFIRMED` | 0 |
| `POTENTIAL_IMPACT` | 5 |
| `NO_DIRECT_EVIDENCE` | 47 |

The current raw exports produce no conservative incident-to-Zabbix or direct
site-explicit ticket correlations. The generated package reports both limitations
instead of inventing links.

Monitoring-signal assessment:

| Assessment | Story count |
| --- | ---: |
| `RELATED_TO_CONFIRMED_INCIDENT` | 0 |
| `USER_IMPACT_SIGNAL` | 0 |
| `LIKELY_NOISE_OR_THRESHOLD_REVIEW` | 37 |
| `UNCONFIRMED_MONITORING_SIGNAL` | 39 |

See [sample-operational-story.md](sample-operational-story.md) for concrete
date-range answers and the explicit source-coverage limitation.

## Human Spot-Check

Đã kiểm tra trực tiếp workbook `normalized_data.xlsx`.

### Confirmed Incidents

Đã kiểm tra 10 record đầu và source lineage:

```text
INC-3, INC-4, INC-5, INC-6, INC-7,
INC-8, INC-9, INC-10, INC-11, INC-12
```

Mỗi record có source reference dạng:

```text
SEA - Corp IT- ILL- Incident Report   (Responses).xlsx#Form Responses 1:row-<number>
```

### Tickets

Đã kiểm tra 10 ticket đầu, comment count, user email, và danh sách source rows:

```text
2178317, 2235273, 2243543, 2245770, 2271913,
2273336, 2278414, 2282341, 2282457, 2288910
```

### Alert Patterns

Đã kiểm tra 10 alert pattern có volume cao nhất:

```text
ALP-86E60C0C5C83, ALP-8251DC672F11, ALP-B7EAE4BAAD66,
ALP-079F1ABCD016, ALP-810793E3F806, ALP-24CD7EE7CAA3,
ALP-6725C5E8CE6D, ALP-DDE7801896DE, ALP-FA12954E19C4,
ALP-DBDD4F005911
```

Pattern volume cao nhất:

```text
ALP-86E60C0C5C83
host = VNMCCW-PNWSW01
raw alert count = 171
problem signature = fpt download gi2/0/3><value>,current:<value> mbps
```

Metric động đã được thay bằng `<value>` mà vẫn giữ source refs.

### High-Count Recurrence

Đã kiểm tra toàn bộ group có ít nhất 2 confirmed incidents:

| Recurrence ID | Site | ISP | Type | Count |
| --- | --- | --- | --- | ---: |
| `REC-C20AAAEB5882` | MS2 | VNPT | High latency | 16 |
| `REC-71D845EC848B` | XAS | CMC | Fiber optic cable failure | 4 |
| `REC-5D2EF81B54EB` | MSB | VNPT | High latency | 3 |
| `REC-18D19523524A` | MSB | FPT | Others | 2 |
| `REC-73E7E72ECD1B` | MS2 | VNPT | Packet loss | 2 |
| `REC-C1DB9B82BE18` | SWS | FPT | Fiber optic cable failure | 2 |
| `REC-C78CA8A62DC3` | XAS | FPT | Fiber optic cable failure | 2 |
| `REC-DBB68D47F06F` | SPV-Mocap | FPT | Others | 2 |

### Data-Quality Warnings

Đã kiểm tra toàn bộ warning hiện tại:

```text
Unconfirmed master-data rows ignored as facts: 102
Sites without confirmed master-data mapping: 14
Alert hosts without confirmed master-data mapping: 33
Incidents missing RCA: 2
Incidents missing preventive action: 35
```

Năm warning đã có trong `validation_report.md`, `06_data_quality.md`, và sheet `data_quality` của audit workbook.

## Kết Luận

Package sample hiện có:

```text
Status = PASS
Upload allowed = YES
```

Phần chưa thể xác minh tự động local là hành vi retrieval thực tế sau khi upload vào Alpha. Thực hiện checklist trong `docs/build-on-alpha-intelligence.md` bằng tài khoản nội bộ trước khi dùng PoC cho vận hành.
