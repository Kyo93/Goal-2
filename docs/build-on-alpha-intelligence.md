# Hướng Dẫn Build Trên Alpha Intelligence

## Kiến Trúc Được Chốt

```text
3 raw Excel files
  -> local Python converter
  -> validated Markdown knowledge package
  -> Alpha Knowledge Expert
  -> Alpha Super Agent
  -> evidence-backed investigation answers
```

Python tính số liệu. Alpha truy xuất và giải thích. Không yêu cầu chạy Python bên trong Alpha Workflow cho MVP.

## Bước 0: Kiểm Tra Package

Mở:

```text
output/alpha-knowledge-package/validation_report.md
```

Chỉ tiếp tục nếu:

```text
Status: PASS
Upload allowed: YES
```

Không upload `normalized_data.xlsx` như nguồn knowledge chính. File Excel này dành cho audit bằng con người.

## Bước 1: Tạo Knowledge Expert

Trong Alpha Intelligence:

1. Mở project space dùng cho PoC.
2. Tạo một Knowledge Expert mới.
3. Đặt tên:

```text
IT Operations Historical Intelligence
```

4. Upload đúng tám file:

```text
00_report_context.md
01_executive_summary.md
02_operational_timeline.md
02_confirmed_incidents.md
03_recurrence_patterns.md
04_alert_patterns.md
05_ticket_impact.md
06_data_quality.md
```

5. Chờ hệ thống hoàn tất ingest/indexing trước khi test retrieval.

Ưu tiên upload đủ tám file trong cùng một lần refresh để summary và evidence detail không lệch version.

## Bước 2: Tạo Super Agent

1. Tạo một Super Agent mới.
2. Đặt tên:

```text
IT Operations Investigation Assistant
```

3. Attach Knowledge Expert `IT Operations Historical Intelligence` làm skill/knowledge source.
4. Bật Inspect Mode trong giai đoạn validation để kiểm tra Expert đã được gọi và evidence nào được truy xuất.
5. Nếu UI cho phép chỉnh sampling, dùng temperature thấp, khoảng `0.1` đến `0.2`, để câu trả lời vận hành ổn định hơn.

Tên menu hoặc nút có thể thay đổi theo version UI Alpha. Giữ đúng hai quan hệ bắt buộc: Super Agent phải attach Expert, và Expert phải ingest đủ tám Markdown.

## Bước 3: Thêm Instruction

Paste instruction sau vào Super Agent:

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
8. For date-range questions, start with 02_operational_timeline.md and summarize in timestamp order.
9. Distinguish responsibility domains: INHOUSE, ISP, EXTERNAL, and UNKNOWN.
10. Treat correlated evidence as context, not proof of RCA or user impact.
11. Answer with operational stories: ordered milestones, conclusion, evidence coverage, and investigation gaps.
12. Distinguish RELATED_TO_CONFIRMED_INCIDENT, USER_IMPACT_SIGNAL, LIKELY_NOISE_OR_THRESHOLD_REVIEW, and UNCONFIRMED_MONITORING_SIGNAL.
```

## Bước 4: Thêm Preset Questions

```text
Summarize confirmed incidents in the latest available month.
Build an operational timeline for 2026-05-01 to 2026-05-19. Include Zabbix signals, user-impact evidence, responsibility domain, RCA, and resolution status.
Which incident patterns recur most often?
What happened at MS2 and was the issue resolved permanently?
Which alert patterns may be noisy and need threshold review?
Which conclusions are limited by missing master data?
Which tickets provide direct evidence of affected users?
```

## Bước 5: Validation Trên Alpha

Chạy lần lượt:

| Prompt | Kết quả tối thiểu cần thấy |
| --- | --- |
| `How many confirmed incidents are in this package?` | Trả lời `52`, không dùng `1000` raw alerts làm incident count. |
| `Which incident pattern recurs most often?` | Có `REC-C20AAAEB5882`, `MS2 | VNPT | High latency`, count `16`. |
| `Was the MS2 recurring issue permanently fixed?` | Dẫn evidence và nói rõ giới hạn nếu preventive action hoặc evidence chưa đủ. Không tự kết luận dứt điểm. |
| `How many Zabbix alerts are confirmed incidents?` | Phân biệt alert evidence với confirmed incident; không tự chuyển đổi alert thành incident. |
| `Which conclusions are limited by missing data?` | Nêu thiếu RCA, preventive action, và master data chưa confirmed. |
| `Show direct user impact evidence.` | Trích ticket ID và source reference, không suy diễn site impact nếu chưa có mapping confirmed. |

Trong Inspect Mode, kiểm tra:

- Knowledge Expert đã được gọi.
- Câu trả lời có record ID, ví dụ `REC-...`, `INC-...`, `ALP-...`, hoặc ticket ID.
- Câu trả lời có source reference dạng `<filename>#<sheet>:row-<number>`.
- Khi evidence thiếu, agent dùng `UNKNOWN` hoặc nói rõ limitation.

## Bước 6: Refresh Package Sau Này

1. Chạy lại converter local.
2. Chỉ tiếp tục nếu validation report là `PASS`.
3. Trong Expert, thay bộ tám Markdown cũ bằng bộ mới theo cùng một version refresh.
4. Chờ indexing hoàn tất.
5. Chạy lại sáu prompt validation.

MVP chưa tự động sync hoặc upload qua API Alpha.

## Timeline-First Validation

For a selected time range, verify that the agent:

- starts from `02_operational_timeline.md`;
- summarizes operational stories and milestones in timestamp order;
- distinguishes `CONFIRMED_INCIDENT` from `MONITORING_SIGNAL`;
- reports `INHOUSE`, `ISP`, `EXTERNAL`, or `UNKNOWN`;
- distinguishes `RELATED_TO_CONFIRMED_INCIDENT`, `USER_IMPACT_SIGNAL`,
  `LIKELY_NOISE_OR_THRESHOLD_REVIEW`, and `UNCONFIRMED_MONITORING_SIGNAL`;
- states when no incident-to-Zabbix or direct ticket correlation is supported;
- treats correlation as context, not proof of RCA.

## Hạn Chế Hiện Tại

- Master data hiện chưa có row `CONFIRMED`; `102` row seed đang bị bỏ qua như fact.
- `14` site từ incident chưa có master-data mapping `CONFIRMED`.
- `33` alert host chưa có master-data mapping `CONFIRMED`.
- `35` incident thiếu preventive action.
- `2` incident thiếu RCA.
- `05_ticket_impact.md` lớn khoảng `1.1 MB`. Nếu UI Alpha áp upload limit hoặc retrieval ticket detail không ổn định, phase tiếp theo nên chia file ticket theo batch nhưng giữ nguyên record heading và lineage.

## Tài Liệu Alpha Chính Thức

- [About the product](https://ai.insea.io/guide/about-the-product)
- [Quick start](https://ai.insea.io/guide/quick-start)
- [Super Agent](https://ai.insea.io/guide/super-agent)
- [Skill Experts](https://ai.insea.io/guide/skill-experts)
