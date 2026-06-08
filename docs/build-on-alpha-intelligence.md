# Hướng Dẫn Build Trên Alpha Intelligence

## Kiến Trúc Được Chốt

```text
3 raw sources
  -> manual Alpha processing workflows / local converter baseline
  -> validated Markdown knowledge package + workflow outputs
  -> Alpha Knowledge Expert
  -> Alpha Super Agent
  -> evidence-backed investigation answers
```

Deterministic Python logic tính số liệu. Với hướng hiện tại, processor code được copy thủ công vào Alpha Code Executor/workflow nodes; repo này không cần được Alpha gọi qua API. Alpha Knowledge giữ vai trò context/fallback, còn exact site/time-range counts nên đến từ workflow result khi có.

## Bước 0: Kiểm Tra Package

Mở:

```text
02-Output/alpha-knowledge-package/validation_report.md
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

4. Upload đúng bộ Markdown package:

```text
00_report_context.md
01_executive_summary.md
02_operational_timeline.md
02_confirmed_incidents.md
03_recurrence_patterns.md
04_alert_patterns.md
05_ticket_impact.md
05_ticket_impact_index.md
05_ticket_impact_YYYY_MM.md
06_data_quality.md
```

5. Chờ hệ thống hoàn tất ingest/indexing trước khi test retrieval.

Ưu tiên upload bộ summary/timeline/alert và `05_ticket_impact_index.md` trong cùng một lần refresh. Ticket detail có thể upload theo monthly partition liên quan đến câu hỏi nếu Alpha giới hạn dung lượng.

`05_ticket_impact_index.md` dùng để chọn tháng theo activity window và có sẵn `Top symptom families`, `Top resolution signals`, `Top comment signals`. File `05_ticket_impact_YYYY_MM.md` mới là nơi chứa chi tiết từng ticket: `symptom_family`, `resolution_signal`, `initial_comments_sample`, `key_comments_sample`, `final_comments_sample`, và `comments_summary`. Khi test Super Agent về ITCenter, hãy upload ít nhất index và partition tháng đang hỏi.

## Bước 2: Tạo Super Agent

1. Tạo một Super Agent mới.
2. Đặt tên:

```text
IT Operations Investigation Assistant
```

3. Attach Knowledge Expert `IT Operations Historical Intelligence` làm skill/knowledge source.
4. Bật Inspect Mode trong giai đoạn validation để kiểm tra Expert đã được gọi và evidence nào được truy xuất.
5. Nếu UI cho phép chỉnh sampling, dùng temperature thấp, khoảng `0.1` đến `0.2`, để câu trả lời vận hành ổn định hơn.

Tên menu hoặc nút có thể thay đổi theo version UI Alpha. Giữ đúng hai quan hệ bắt buộc: Super Agent phải attach Expert, và Expert phải ingest đúng bộ Markdown cùng version.

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
3. Distinguish SOURCE FACT, COMPUTED FACT, POTENTIAL_IMPACT, NO_DIRECT_EVIDENCE, AI INFERENCE, and UNKNOWN.
4. Cite record IDs and source references in the answer.
5. If evidence is missing or mappings are not confirmed, state the limitation.
6. Do not invent RCA, affected users, resolution status, or preventive actions.
7. Prefer concise management-ready operational summaries with a concrete follow-up/gaps section.
8. For date-range questions, start with 02_operational_timeline.md and summarize in timestamp order.
9. Distinguish responsibility domains: INHOUSE, ISP, EXTERNAL, and UNKNOWN.
10. Treat correlated evidence as context, not proof of RCA or user impact.
11. Answer with operational stories: ordered milestones, conclusion, evidence coverage, and investigation gaps.
12. Distinguish RELATED_TO_CONFIRMED_INCIDENT, TIME_ALIGNED_CONTEXT_ONLY, USER_IMPACT_SIGNAL, LIKELY_NOISE_OR_THRESHOLD_REVIEW, and UNCONFIRMED_MONITORING_SIGNAL.
13. For date-range site questions, do not answer with raw labels only. Write for a middle-management operations reader.
14. Use this format for date-range site questions:
    - Management summary: what happened, severity/impact signal, recovery, and owner/domain if supported.
    - What happened: timestamp-ordered incident/signal narrative in plain language.
    - Impact and evidence: what evidence exists, what is missing, and what that means.
    - Operational conclusion: what is confirmed, what is contextual, and what management should take away.
    - Follow-up / gaps: concrete checks or missing evidence.
15. Explain NO_DIRECT_EVIDENCE as missing direct ticket/user evidence, not proof that no user was affected.
16. Explain POTENTIAL_IMPACT as possible impact without direct ticket/user confirmation.
17. Keep date-range site answers concise: 2-4 short paragraphs or 5-8 bullets.
18. Use record IDs and source references in a compact evidence line, not as the main body.
19. Avoid overusing audit labels such as SOURCE FACT, COMPUTED FACT, and NO_MATCHING_ZABBIX_SIGNAL in the management-facing text.
20. Do not end operational answers with a generic "if you want" offer.
21. Same-site/time Zabbix correlation is not enough to prove RCA support. If the alert signature does not match the incident type/RCA, describe it as time-aligned context only.
22. For fiber/cable/routing incidents, treat network-relevant Zabbix signatures such as ICMP, ping, interface, link, packet loss, latency, unreachable, or unavailable as stronger supporting context. Treat host restart/uptime alerts as context only unless another source explicitly links them.
23. Evidence priority for incomplete or conflicting data:
    - ISP Incident Report first for confirmed incident existence, start/end time, RCA, resolution status, ISP/provider, and responsibility domain.
    - ITcenter ticket second for direct user evidence, affected scope, business/user symptoms, escalation, and impact confirmation.
    - Zabbix Alert third for monitoring signals, telemetry, timing context, recurrence, and technical symptoms.
24. The priority order does not mean lower-priority evidence is ignored. Use lower-priority sources to add context, confirm timing, or expose gaps.
25. If sources conflict, do not silently merge them. State the conflict and cite the record IDs/source references.
26. For user impact, direct ITcenter ticket/user evidence outranks incident description. Zabbix alone cannot confirm user impact.
27. For Zabbix-alert questions, answer by pattern family and problem signature before listing episode IDs.
28. For Zabbix-alert questions, prioritize investigation using `pattern_family`, `investigation_priority`, `query_alert_count`, `query_first_seen_at`, `query_last_seen_at`, and whether multiple hosts fired together.
29. For Zabbix-alert questions, explain what the pattern means operationally: HTTP monitoring, Network reachability, Zabbix agent/active check, Host restart/uptime, Power/UPS, or Other.
30. If `monitoring_family_summary` or the `Site Pattern Family Summary` section is available, use it as the primary source for the answer.
31. Do not start Zabbix-alert answers by listing individual `OPS-ALP-*` records. Use at most 3 episode IDs in the main body; put the rest in a compact evidence line only if needed.
32. For site/date-range questions, do not answer from arbitrary retrieved fragments. Prefer the deterministic query workflow/result. If no query result is available, retrieve `02_operational_timeline.md` and `04_alert_patterns.md` summary sections before answering.
33. For Zabbix-alert questions, if only individual `OPS-ALP-*` records are retrieved and no `monitoring_family_summary`, `monitoring_pattern_summary`, or `Site Pattern Family Summary` is available, state that the retrieved context is incomplete and ask to run/refresh the query. Do not claim a complete monthly/site summary from partial records.
34. Never say "at least 1 alert" when the user asks for a complete site/month alert summary unless the retrieved context is explicitly partial. Use exact counts only from `monitoring_family_summary`, `monitoring_pattern_summary`, or `Site Pattern Family Summary`.
35. For repeatability, the same site/date-range question must use the same source hierarchy: query result first, then `Site Pattern Family Summary`, then individual evidence records.
```

Preferred final-answer shape for date-range site questions:

```text
Trong khoảng [from_at] đến [to_at], site [site_code] ghi nhận [count] sự kiện vận hành.
[Nêu sự kiện chính, thời điểm, đã khôi phục chưa, RCA/domain nếu có evidence.]
[Nêu Zabbix/ticket evidence tìm thấy hoặc không tìm thấy, giải thích impact.]
Kết luận vận hành: [điều đã xác nhận] và [gap/follow-up cụ thể].
```

For example, do not answer only:

```text
matched_event_count: 1
CONFIRMED_INCIDENT: INC-3
User impact: NO_DIRECT_EVIDENCE
```

Instead, write:

```text
Trong khoảng thời gian được hỏi, site MS2 ghi nhận 1 sự cố vận hành đã xác nhận: high latency.
Sự cố bắt đầu lúc ... và được ghi nhận khôi phục lúc ..., tổng thời gian khoảng ... phút. RCA trong incident form cho biết nguyên nhân liên quan international routing fluctuations, nên episode này được phân loại theo hướng ISP/routing.

Không tìm thấy Zabbix signal cùng site hoặc ticket người dùng khớp trực tiếp với cửa sổ sự cố. Vì vậy, hiện chưa có bằng chứng trực tiếp để định lượng user impact; điều này không có nghĩa là chắc chắn không có người dùng bị ảnh hưởng.

Kết luận vận hành: MS2 có một sự cố high latency ngắn, đã resolved, RCA liên quan ISP/routing. Cần theo dõi recurrence của nhóm MS2/VNPT high latency nếu câu hỏi quản lý cần đánh giá xu hướng lặp lại.
```

Preferred shape for Zabbix-alert questions:

```text
Trong khoảng [from_at] đến [to_at], site [site_code] ghi nhận [pattern_count] Zabbix monitoring patterns.
Nhóm đáng chú ý nhất là [pattern_family/signature] vì [why_it_matters], xuất hiện trên [hosts] trong khoảng [first] đến [last].
[Nêu nhóm HTTP/noise nếu nhiều nhưng ít ý nghĩa điều tra; nêu nhóm network/firewall/ICMP nếu đáng ưu tiên.]
Không có confirmed incident/ticket khớp trực tiếp thì user impact là UNKNOWN/NO_DIRECT_EVIDENCE.
Evidence line: [episode IDs/source refs compact].
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
| `How many confirmed incidents are in this package?` | Trả lời `52`, không dùng `5199` raw alerts làm incident count. |
| `Which incident pattern recurs most often?` | Có `REC-C20AAAEB5882`, `MS2 | VNPT | High latency`, count `16`. |
| `Was the MS2 recurring issue permanently fixed?` | Dẫn evidence và nói rõ giới hạn nếu preventive action hoặc evidence chưa đủ. Không tự kết luận dứt điểm. |
| `How many Zabbix alerts are confirmed incidents?` | Phân biệt alert evidence với confirmed incident; không tự chuyển đổi alert thành incident. |
| `Which conclusions are limited by missing data?` | Nêu thiếu RCA, preventive action, và master data chưa confirmed. |
| `Show direct user impact evidence.` | Trích ticket ID và source reference, không suy diễn site impact nếu chưa có mapping confirmed. |
| `For May 2026 ITCenter tickets, what are the top symptom families?` | Dùng `05_ticket_impact_index.md`, nêu `Top symptom families` của partition `2026-05`, không đếm lại từ fragments. |
| `Show VPN-related ITCenter tickets in May 2026 and their resolution signals.` | Dùng `05_ticket_impact_2026_05.md`, trích ticket IDs, `symptom_family = vpn_or_remote_access`, `resolution_signal`, và source refs. |
| `For a ticket with truncated comments, can you still audit the raw source?` | Giải thích marker `[truncated; see source_refs]` nghĩa là Markdown đã excerpt, audit bằng `source_refs`/workbook; không giả vờ có full transcript trong Knowledge. |

Trong Inspect Mode, kiểm tra:

- Knowledge Expert đã được gọi.
- Câu trả lời có record ID, ví dụ `REC-...`, `INC-...`, `ALP-...`, hoặc ticket ID.
- Câu trả lời có source reference dạng `<filename>#<sheet>:row-<number>`.
- Khi evidence thiếu, agent dùng `UNKNOWN` hoặc nói rõ limitation.

## Bước 6: Refresh Package Sau Này

1. Chạy lại converter local.
2. Chỉ tiếp tục nếu validation report là `PASS`.
3. Trong Expert, thay bộ Markdown cũ bằng bộ mới theo cùng một version refresh; với ticket detail, thay index và các monthly partitions cần dùng.
4. Chờ indexing hoàn tất.
5. Chạy lại sáu prompt validation.

MVP chưa tự động sync hoặc upload qua API Alpha. Đây là quyết định có chủ ý: build workflow thủ công trên Alpha, upload raw/Markdown thủ công khi cần, và dùng repo này làm source of truth cho code/contract.

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
- Ticket detail đã được chia theo monthly partitions: `05_ticket_impact_index.md` + `05_ticket_impact_YYYY_MM.md`. Dùng index trước, sau đó upload/retrieve tháng liên quan để tránh vượt giới hạn dung lượng Alpha.

## Tài Liệu Alpha Chính Thức

- [About the product](https://ai.insea.io/guide/about-the-product)
- [Quick start](https://ai.insea.io/guide/quick-start)
- [Super Agent](https://ai.insea.io/guide/super-agent)
- [Skill Experts](https://ai.insea.io/guide/skill-experts)
