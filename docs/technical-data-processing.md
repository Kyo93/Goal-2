# Technical Data Processing Guide

Tài liệu này mô tả chi tiết cách project xử lý từng raw Excel file để tạo
Alpha Knowledge Package. Nguồn triển khai chính nằm trong
`src/itops_alpha/converter.py`; script entrypoint là
`scripts/build_alpha_knowledge_package.py`.

## 1. Mục tiêu pipeline

Pipeline đọc ba raw export trong `01-RawData/`, tùy chọn đọc master data trong
`03-Data clean logic/reference doc/it-operations-master-data-template.xlsx`, sau đó sinh package tại
`02-Output/alpha-knowledge-package/`.

Nguyên tắc xử lý quan trọng:

- Incident form là nguồn duy nhất tạo `CONFIRMED_INCIDENT`.
- Zabbix export chỉ tạo monitoring signal hoặc alert pattern, không tự động trở
  thành confirmed incident.
- Issue ticket là bằng chứng user impact, không tự động trở thành incident.
- Mọi record giữ `source_ref` theo format
  `<filename>#<sheet_name>:row-<excel_row_number>` để audit ngược về raw row.
- Row lỗi parse hoặc thiếu khóa bắt buộc bị đưa vào `rejected_rows`; pipeline
  không tự sửa dữ liệu nguồn.
- Các field trống sau normalize được ghi là `UNKNOWN` nếu field đó cần tồn tại
  trong output.

## 2. Luồng tổng quát

```text
01-RawData/ISP Incident Report/SEA - Corp IT- ILL- Incident Report   (Responses).xlsx
  -> load_incidents()
  -> confirmed_incidents
  -> group_incident_recurrence()

01-RawData/zbx_problems_export.xlsx
  -> load_zabbix_alerts()
  -> group_alert_patterns()

01-RawData/Ticket/*.csv
  -> load_issue_tickets()
  -> ticket_evidence

confirmed_incidents + alert_patterns + ticket_evidence + recurrence_patterns
  -> build_operational_stories()
  -> 02_operational_timeline.md
  -> normalized_data.xlsx
```

Các output chính:

| Output | Nội dung |
| --- | --- |
| `00_report_context.md` | Count, coverage period, warnings tổng quan |
| `01_executive_summary.md` | Tóm tắt executive từ source profile và top patterns |
| `02_operational_timeline.md` | View điều tra chính theo timeline |
| `02_confirmed_incidents.md` | Incident đã xác nhận từ incident form |
| `03_recurrence_patterns.md` | Nhóm incident lặp lại |
| `04_alert_patterns.md` | Nhóm alert Zabbix theo host và signature |
| `05_ticket_impact.md` | Ticket evidence da gop comment |
| `05_ticket_impact_index.md` | Index ticket partitions theo thang |
| `05_ticket_impact_YYYY_MM.md` | Ticket evidence theo monthly partition |
| `06_data_quality.md` | Warning, rejected rows, coverage gaps |
| `normalized_data.xlsx` | Audit workbook gồm các sheet normalized |
| `manifest.json` | Version, input hashes, source profile, warnings |
| `validation_report.*` | Validation gate trước khi upload |

## 3. Xử lý chung cho mọi raw file

### 3.1 Đọc workbook và sheet

Hàm `_load_sheet()` dùng `openpyxl.load_workbook(..., read_only=True,
data_only=True)`.

- Header lấy từ row đầu tiên.
- Header được normalize bằng `clean_text()`: ép về string, trim, gom whitespace.
- Nếu không truyền tên sheet, converter đọc worksheet đầu tiên.
- Nếu truyền tên sheet, converter bắt buộc đọc sheet đó.
- Workbook được đóng sau khi load raw rows.

### 3.2 Validate schema

Hàm `_validate_columns()` so sánh header đã normalize với set cột bắt buộc của
từng source.

Nếu thiếu cột bắt buộc, pipeline raise `ValueError` và dừng build. Đây là lỗi
schema, không phải rejected row.

### 3.3 Blank row, rejected row, và source reference

Trong từng adapter:

- Blank row được bỏ qua và tăng `skipped_blank_rows`.
- Non-blank row được tính vào `input_rows`.
- Row không parse được timestamp, date/time, hoặc thiếu key bắt buộc như ticket
  id sẽ vào `rejected_rows`.
- `source_ref()` tạo lineage theo Excel row thật, bắt đầu data row từ row 2.

### 3.4 Parse ngày giờ

`parse_datetime()` chấp nhận:

- Python `datetime`
- Python `date`
- ISO datetime qua `datetime.fromisoformat`
- Các format string:
  - `%b %d, %Y @ %H:%M:%S.%f`
  - `%b %d, %Y @ %H:%M:%S`
  - `%Y-%m-%dT%H:%M:%S.%f`
  - `%Y-%m-%dT%H:%M:%S`
  - `%Y-%m-%d %H:%M:%S`
  - `%Y-%m-%d`

`parse_time()` chấp nhận:

- Python `datetime`
- Python `time`
- `%H:%M:%S`
- `%H:%M`

Timezone bị loại bỏ bằng `replace(tzinfo=None)`. Output timestamp được render
bằng ISO seconds, ví dụ `2026-05-19T16:32:36`.

## 4. Raw file: Incident Report

### 4.1 File và sheet

Raw file:

```text
01-RawData/ISP Incident Report/SEA - Corp IT- ILL- Incident Report   (Responses).xlsx
```

Adapter:

```text
load_incidents()
```

Sheet được đọc:

```text
Form Responses 1
```

Workbook hiện có thêm sheet `MS2 -VNPT`, nhưng converter không đọc sheet này.
Điều này giúp tránh double count khi sheet phụ là subset hoặc view thủ công.

### 4.2 Cột bắt buộc

```text
Timestamp
ISP
SITE / Location
Incident DATE
Incident TIME
Reporter
Incindent Type
Severity
Incident description
Initial Cause
Troubleshooting actions
Root Cause
Incident resolution date
Incident resolution time
Measures to prevent recurrence of incidents (if any)
```

Lưu ý: header raw có thể có khoảng trắng hoặc newline thừa, ví dụ
`SITE / Location ` hoặc `Reporter \n`; `normalize_header()` sẽ trim/gom
whitespace nên vẫn match được cột bắt buộc.

### 4.3 Chuẩn hóa từng row

Mỗi non-blank row được chuyển thành một incident record:

| Output field | Cách tạo |
| --- | --- |
| `incident_id` | `INC-<excel_row_number>` |
| `source_ref` | File, sheet, row gốc |
| `submitted_at` | Parse từ `Timestamp`; cho phép trống |
| `started_at` | Ghép `Incident DATE` + `Incident TIME` |
| `resolved_at` | Ghép `Incident resolution date` + `Incident resolution time` nếu có date |
| `duration_minutes` | `(resolved_at - started_at)` theo phút, làm tròn 2 chữ số; `None` nếu chưa resolved |
| `site_code` | Lấy phần trước `" - "` từ `SITE / Location`; trống thành `UNKNOWN` |
| `site_name` | Clean từ `SITE / Location`; trống thành `UNKNOWN` |
| `isp` | Clean từ `ISP`; trống thành `UNKNOWN` |
| `reporter` | Clean từ `Reporter`; trống thành `UNKNOWN` |
| `incident_type` | Clean từ `Incindent Type`; trống thành `UNKNOWN` |
| `severity` | Clean từ `Severity`; trống thành `UNKNOWN` |
| `description` | Preserve multiline từ `Incident description`; trống thành `UNKNOWN` |
| `initial_cause` | Preserve multiline từ `Initial Cause`; trống thành `UNKNOWN` |
| `troubleshooting_actions` | Preserve multiline từ `Troubleshooting actions`; trống thành `UNKNOWN` |
| `root_cause` | Preserve multiline từ `Root Cause`; trống thành `UNKNOWN` |
| `preventive_action` | Preserve multiline từ recurrence prevention column; trống thành `UNKNOWN` |
| `resolution_status` | `RESOLVED` nếu có `resolved_at`, ngược lại `UNKNOWN` |
| `recurrence_key` | `<site_code>|<isp>|<incident_type>` lower-case |
| `evidence_label` | `SOURCE FACT` |

### 4.4 Rejected row rule

Incident row bị reject nếu:

- `Timestamp` không parse được khi có giá trị.
- `Incident DATE` hoặc `Incident TIME` không parse được.
- `Incident resolution date/time` không parse được khi có resolution date.

### 4.5 Recurrence pattern từ incident

`group_incident_recurrence()` gom incident theo `recurrence_key`.

Output chính:

| Output field | Cách tạo |
| --- | --- |
| `recurrence_id` | `REC-<stable_hash(recurrence_key)>` |
| `incident_count` | Số incident trong nhóm |
| `incident_ids` | Danh sách incident id theo thời gian |
| `first_seen_at`, `last_seen_at` | Min/max `started_at` |
| `root_causes` | Join unique root causes khác `UNKNOWN` |
| `evidence_label` | `COMPUTED FACT` |

Với raw snapshot hiện tại:

```text
input_rows = 52
normalized_incidents = 52
rejected_incident_rows = 0
skipped_blank_rows = 1
incident_period_start = 2025-12-01T07:35:00
incident_period_end = 2026-05-29T12:20:00
recurrence_patterns = 27
```

Top recurrence hiện tại:

| Site | ISP | Incident type | Count |
| --- | --- | --- | ---: |
| `MS2` | `VNPT` | `High latency` | 16 |
| `XAS` | `CMC` | `Fiber optic cable failure` | 4 |
| `MSB` | `VNPT` | `High latency` | 3 |
| `MSB` | `FPT` | `Others` | 2 |
| `MS2` | `VNPT` | `Packet loss` | 2 |

## 5. Raw file: Zabbix Problems Export

### 5.1 File và sheet

Raw input cũ:

```text
01-RawData/zbx_problems_export.xlsx
```

Raw input mới khi Zabbix phải download nhiều lần vì giới hạn 1000 dòng:

```text
01-RawData/Export zabbix/*.csv
```

Adapter:

```text
load_zabbix_alerts()
```

Nếu `01-RawData/Export zabbix/` tồn tại, `build_knowledge_package()` ưu tiên thư
mục này và đọc toàn bộ `*.csv` theo thứ tự tên file. Nếu thư mục không tồn tại,
converter fallback về file Excel `01-RawData/zbx_problems_export.xlsx`.

Với Excel, converter đọc worksheet đầu tiên, hiện là:

```text
zbx_problems_export(1) (1)
```

Với CSV, `source_ref` dùng sheet label `csv`, ví dụ:

```text
zbx_problems_export 2d-4d.csv#csv:row-2
```

### 5.2 Cột bắt buộc

```text
Severity
Time
Recovery time
Status
Host
Problem
Duration
Ack
Actions
Tags
```

### 5.3 Chuẩn hóa từng row

Mỗi non-blank row được chuyển thành một alert record:

| Output field | Cách tạo |
| --- | --- |
| `alert_id` | `ALT-<stable_hash(source_filename, row_number)>` |
| `source_ref` | File, sheet, row gốc |
| `seen_at` | Parse từ `Time` |
| `recovered_at` | Parse từ `Recovery time` nếu có |
| `status` | Clean từ `Status`; trống thành `UNKNOWN` |
| `severity` | Clean từ `Severity`; trống thành `UNKNOWN` |
| `host` | Clean từ `Host`; trống thành `UNKNOWN` |
| `site_code` | Regex `^VNM([A-Z0-9]{3})` từ hostname; không match thành `UNKNOWN` |
| `problem` | Clean từ `Problem`; trống thành `UNKNOWN` |
| `problem_signature` | Normalize dynamic metric value trong `Problem` |
| `duration` | Clean từ `Duration`; trống thành `UNKNOWN` |
| `ack` | Clean từ `Ack`; trống thành `UNKNOWN` |
| `actions` | Clean từ `Actions`; trống thành `UNKNOWN` |
| `domain` | Tag `class`, join unique values |
| `component` | Tag `component`, join unique values |
| `scope` | Tag `scope`, join unique values |
| `tags` | JSON string của parsed tags |
| `evidence_label` | `SOURCE FACT` |

### 5.4 Parse tags

`parse_tags()` tách field `Tags` theo `", "`, rồi chỉ nhận token có dạng:

```text
key: value
```

Nếu cùng key có nhiều value, value trùng bị loại. Output tags được giữ ở dạng
dict rồi serialize JSON với `ensure_ascii=False` và `sort_keys=True`.

### 5.5 Normalize problem signature

`normalize_problem_signature()` lower-case problem text và thay số đo động bằng
placeholder để gom các alert cùng bản chất:

- `current: 115.17 Mbps` thành `current:<value> mbps`
- Giá trị có đơn vị `mbps`, `gbps`, `%`, `hz`, `m`, `s`, `℃`, `°c` thành
  `<value>`

Ví dụ:

```text
FPT Download Gi2/0/3>100M,Current:115.17 Mbps
-> fpt download gi2/0/3><value>,current:<value> mbps
```

### 5.6 Alert pattern

`group_alert_patterns()` gom alert theo:

```text
(host, problem_signature)
```

Output chính:

| Output field | Cách tạo |
| --- | --- |
| `alert_pattern_id` | `ALP-<stable_hash(host, problem_signature)>` |
| `source_refs` | Tất cả raw alert rows thuộc nhóm |
| `first_seen_at`, `last_seen_at` | Min/max `seen_at` trong nhóm |
| `last_recovered_at` | Max `recovered_at` không trống |
| `alert_count` | Số raw alerts trong nhóm |
| `resolved_count` | Số row có `status == "RESOLVED"` |
| `open_count` | Số row có status khác `RESOLVED` |
| `severity`, `domain`, `component`, `scope` | Join unique non-UNKNOWN values |
| `assessment` | Luôn là `RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT` |
| `evidence_label` | `COMPUTED FACT` |

Patterns được sort theo `alert_count` giảm dần, rồi theo `alert_pattern_id`.

Khi đọc nhiều CSV, converter dedupe các row trùng hệt nhau giữa các lần export
theo 10 cột Zabbix bắt buộc. Duplicate row tăng `duplicate_rows`, không tạo
alert record mới, và được tính vào validation reconciliation.

Với raw snapshot hiện tại trong `01-RawData/Export zabbix/`:

```text
input_rows = 6454
normalized_alert_rows = 5942
duplicate_alert_rows = 512
rejected_alert_rows = 0
skipped_blank_rows = 0
alert_period_start = 2026-05-04T15:37:52
alert_period_end = 2026-06-03T15:11:37
alert_patterns = 347
```

Top alert patterns hiện tại:

| Host | Site | Count | Severity | Domain | Component | Signature |
| --- | --- | ---: | --- | --- | --- | --- |
| `VNMMSH-VSDHC01` | `MSH` | 354 | `Average,Warning` | `os` | `cpu` | `windows: high cpu utilization...` |
| `VNMSNT-UPSF2201` | `SNT` | 309 | `High` | `power` | `power` | `apc ups: unacceptable input frequency...` |
| `VNMCPL-VSSPM03` | `CPL` | 247 | `Disaster` | `UNKNOWN` | `UNKNOWN` | `git http monitoring` |
| `VNMSNT-VSSPM02` | `SNT` | 240 | `Disaster` | `UNKNOWN` | `UNKNOWN` | `git http monitoring` |
| `VNMSNT-VSSPM01` | `SNT` | 237 | `Disaster` | `UNKNOWN` | `UNKNOWN` | `git http monitoring` |

## 6. Raw source: ITcenter Ticket monthly CSV

### 6.1 File và sheet

Raw file:

```text
01-RawData/Ticket/*.csv
```

Adapter:

```text
load_issue_tickets()
```

Converter đọc tất cả CSV trong thư mục Ticket:

```text
monthly CSV partition files
```

Converter group cùng một `itcenter.ticket.id` xuyên nhiều file tháng, và giữ source file/partition month trong output.

### 6.2 Cột bắt buộc

```text
itcenter.ticket.id
itcenter.ticket.created_at
itcenter.ticket.full_title
itcenter.ticket.category_en_name
itcenter.ticket.classification_name
itcenter.ticket.service_recipient.user.business_unit
itcenter.ticket.service_recipient.user.entity_name
itcenter.ticket.location_full_name
itcenter.ticket.comment.created_by.user.email
itcenter.ticket.comment.text
itcenter.ticket.comment.updated_at
itcenter.ticket.comment.created_at
itcenter.ticket.service_recipient.user.office_display
itcenter.ticket.subclassification_name
```

### 6.3 Chuẩn hóa và gộp ticket

Raw file là comment-level export: một ticket có thể xuất hiện nhiều row, mỗi row
là một comment. Adapter gom theo `itcenter.ticket.id`.

Trong lúc đọc từng comment row:

- Parse `itcenter.ticket.comment.created_at`.
- Parse `itcenter.ticket.created_at` làm mốc user/business impact khi có.
- Reject row nếu timestamp không parse được.
- Reject row nếu ticket id trống.
- Lưu `source_refs`, `comment_times`, `comment_updated_times`, `source_files`, `partition_months`, và `comments`.
- Metadata ticket như category, classification, title, entity, location, office, subclassification lấy từ
  row đầu tiên gặp theo ticket id.

Sau khi đọc xong, mỗi ticket record có:

| Output field | Cách tạo |
| --- | --- |
| `ticket_id` | Raw ticket id |
| `source_refs` | Tat ca comment row thuoc ticket |
| `ticket_created_at` | Earliest raw ticket created timestamp |
| `evidence_started_at` | `ticket_created_at` neu co, fallback `first_comment_at` |
| `evidence_time_basis` | `ticket_created_at` hoac `first_comment_at_fallback` |
| `first_comment_at` | Min comment timestamp |
| `last_comment_at` | Max comment timestamp |
| `last_activity_at` | Max comment created/updated timestamp |
| `comment_count` | So comment rows da doc |
| `source_files` | CSV files co comment cua ticket |
| `partition_months` | Comment activity months cua ticket |
| `comments_summary` | Join toi da 3 comment dau tien bang `" | "` |
| `impact_evidence` | Bang `title` |
| `evidence_label` | `SOURCE FACT` |

Records được sort theo `ticket_id`.

Với raw snapshot hiện tại:

```text
input_rows = 9525
normalized_tickets = 2681
aggregated_ticket_comment_count = 9525
rejected_comment_rows = 0
skipped_blank_rows = 0
ticket_partition_count = 3
ticket_period_start = 2025-07-31T04:43:41
ticket_period_end = 2026-06-07T10:30:16
ticket_activity_period_start = 2026-04-01T10:48:19
ticket_activity_period_end = 2026-06-07T10:30:16
```

## 7. Master data workbook

Optional input:

```text
03-Data clean logic/reference doc/it-operations-master-data-template.xlsx
```

Adapter:

```text
load_confirmed_master_data()
```

Sheets được đọc nếu tồn tại:

| Sheet | Key field |
| --- | --- |
| `sites` | `site_code` |
| `hosts` | `host_name` |
| `network_links` | `link_code` |
| `services` | `service_code` |
| `user_groups` | `group_code` |
| `service_dependencies` | `dependency_id` |

Chỉ row có:

```text
review_status = CONFIRMED
```

mới được đưa vào dict master data. Các row khác tăng `unconfirmed_rows` và không
được coi là fact.

Với workbook hiện tại:

```text
confirmed sites = 0
confirmed hosts = 0
confirmed network_links = 0
confirmed services = 0
confirmed user_groups = 0
confirmed service_dependencies = 0
unconfirmed_rows = 102
```

Vì vậy package hiện tại có warning:

```text
Unconfirmed master-data rows ignored as facts: 102
Sites without confirmed master-data mapping: 14
Alert hosts without confirmed master-data mapping: 33
```

## 8. Correlation và operational stories

### 8.1 Time-window correlation

Correlation dùng `_time_windows_overlap()` với buffer mặc định 60 phút:

```text
left_start - 60min <= right_end
and
right_start <= left_end + 60min
```

Correlation chỉ là investigation context, không phải bằng chứng RCA hoặc user
impact.

### 8.2 Incident với Zabbix

Confirmed incident match với alert pattern khi:

- `pattern.site_code == incident.site_code`
- incident window overlap với alert pattern window trong buffer 60 phút

Nếu match, incident story có `related_alert_pattern_ids`, và alert pattern story
có `related_incident_ids`.

### 8.3 Incident với ticket

Ở `build_operational_timeline()`, ticket match incident khi:

- Ticket title/comment/impact evidence chứa site code dạng token độc lập.
- Ticket time window overlap incident window trong buffer 60 phút.

Ở `build_operational_stories()`, rule ticket chặt hơn:

- Phải chứa site code.
- Phải match relevance token/category với incident text hoặc alert pattern text.
- Phải overlap time window.

Relevance matching dùng:

- Token overlap với title.
- Ít nhất 2 token overlap với ticket text.
- Category overlap cho `network`, `power`, `hardware`.

### 8.4 User impact status

Incident story:

- `CONFIRMED` nếu có related ticket.
- `POTENTIAL_IMPACT` nếu không có ticket nhưng description chứa keyword như `user`,
  `impact`, `affected`, `service interruption`, `service disruption`,
  `service is down`, `outage`.
- `NO_DIRECT_EVIDENCE` nếu không có bằng chứng user impact trực tiếp.

Monitoring signal story:

- `CONFIRMED` nếu có related ticket.
- `UNKNOWN` nếu không có related ticket.

### 8.5 Responsibility domain

`classify_responsibility_domain()` chỉ dùng `root_cause` từ incident form.

Rule keyword:

| Domain | Keywords |
| --- | --- |
| `ISP` | `routing`, `uplink`, `transit`, `fiber`, `fibre`, `cable`, `cáp`, `provider`, `vnpt`, `fpt`, `cmc`, `netnam` |
| `INHOUSE` | `local segment`, `internal`, `switch`, `firewall`, `configuration`, `linecard`, `junos`, `wifi controller`, `access point` |
| `EXTERNAL` | `electricity`, `utility`, `power supply`, `third-party`, `third party` |
| `UNKNOWN` | RCA trống, `UNKNOWN`, hoặc không match keyword |

Raw Zabbix alert pattern luôn có responsibility `UNKNOWN`.

### 8.6 Monitoring signal assessment

Alert pattern story được đánh giá:

| Assessment | Điều kiện |
| --- | --- |
| `RELATED_TO_CONFIRMED_INCIDENT` | Có related incident id |
| `USER_IMPACT_SIGNAL` | Không có incident nhưng có related ticket |
| `LIKELY_NOISE_OR_THRESHOLD_REVIEW` | Không có incident/ticket và `alert_count > 1` |
| `UNCONFIRMED_MONITORING_SIGNAL` | Không có incident/ticket và chỉ một alert |

Với raw snapshot hiện tại:

```text
operational_timeline_events = 399
timeline_confirmed_incident_events = 52
timeline_zabbix_pattern_events = 347
signal_assessment_related_to_incident = 15
signal_assessment_user_impact = 4
signal_assessment_noise_review = 171
signal_assessment_unconfirmed = 157
user_impact_incidents_confirmed = 0
user_impact_incidents_potential_impact = 5
user_impact_incidents_no_direct_evidence = 47
```

Evidence coverage hiện tại:

```text
INCIDENT FORM = 52 stories
ZABBIX = 328 stories
ZABBIX + INCIDENT FORM = 18 stories
ZABBIX + TICKET = 4 stories
```

Nghĩa là raw snapshot hiện tại đã có correlation context giữa Zabbix với một số
incident/ticket, nhưng vẫn chưa có full-chain story kiểu
`ZABBIX + INCIDENT FORM + TICKET`.

## 9. Validation gate

`build_validation_report()` tạo ba reconciliation invariant:

```text
incident_form_rows = normalized_incidents + rejected_incident_rows
zabbix_rows = normalized_alert_rows + rejected_alert_rows + duplicate_alert_rows
issue_comment_rows = aggregated_ticket_comment_count + rejected_comment_rows
```

Ngoài ra `_known_sample_checks()` chạy khi raw snapshot match sample baseline:

```text
normalized_incidents = 52
normalized_alert_rows = 5199
normalized_tickets = 2681
```

Khi match baseline, hai recurrence check bắt buộc là:

```text
MS2 | VNPT | High latency = 16
XAS | CMC | Fiber optic cable failure = 4
```

Package chỉ được upload khi:

```text
validation_status = PASS
upload_allowed = true
```

Với output hiện tại, `validation_report.md` đang PASS.

## 10. File integrity và manifest

`manifest.json` ghi:

- `package_version`
- `generated_at`
- `upload_allowed`
- `validation_status`
- SHA-256 của từng input file
- `source_profile`
- warnings

Input được hash bằng streaming SHA-256 qua `sha256_file()`, giúp phát hiện raw
file đã đổi giữa các lần build.

## 11. Các giới hạn kỹ thuật hiện tại

- Converter đọc các source theo contract:
  - `01-RawData/Ticket/*.csv`, hoặc fallback legacy `IssueReport.xlsx`
  - `SEA - Corp IT- ILL- Incident Report   (Responses).xlsx`
  - `zbx_problems_export.xlsx`
- Incident workbook chỉ đọc sheet `Form Responses 1`.
- Legacy Issue workbook và Zabbix workbook chỉ đọc worksheet đầu tiên; monthly Ticket CSV đọc theo từng file trong thư mục.
- Không có timezone-aware normalization; timezone bị bỏ khi parse datetime.
- Master data chưa `CONFIRMED` sẽ không enrichment output.
- Correlation không chứng minh RCA, chỉ tạo investigation context.
- Ticket correlation phụ thuộc site code xuất hiện trong title/comment/evidence.
- Zabbix host-to-site phụ thuộc naming convention `VNM<site_code>`.
- Problem signature normalization hiện mới xử lý một số pattern metric/unit phổ
  biến.
- Pipeline không ghi đè raw file và không tự sửa dữ liệu sai.
