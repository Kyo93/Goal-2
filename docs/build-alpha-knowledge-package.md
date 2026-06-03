# Hướng Dẫn Chạy IT Operations Converter

## Mục Tiêu

Script local Python đọc toàn bộ ba file Excel raw, chuẩn hóa dữ liệu, tính thống kê deterministic, và sinh package để upload thủ công vào Alpha Intelligence.

AI không được tự đếm fragment truy xuất từ RAG và không được biến raw alert thành incident đã xác nhận.

## Điều Kiện Chạy

- Python 3.11 trở lên.
- Chạy lệnh tại thư mục gốc project.
- Cài dependency:

```powershell
python -m pip install -r requirements.txt
```

## Input Bắt Buộc

Đặt ba file đúng tên trong `RawData/`:

```text
RawData/
  IssueReport.xlsx
  SEA - Corp IT- ILL- Incident Report   (Responses).xlsx
  zbx_problems_export.xlsx
```

Input tùy chọn:

```text
input/it-operations-master-data-template.xlsx
```

Chỉ row có `review_status=CONFIRMED` trong master data được coi là fact. Các row `NEEDS_REVIEW`, `DRAFT`, hoặc `REJECTED` không được dùng làm mapping chính thức.

## Build Package

```powershell
python scripts\build_alpha_knowledge_package.py `
  --raw-dir RawData `
  --master-data input\it-operations-master-data-template.xlsx `
  --output-dir output\alpha-knowledge-package
```

Có thể bỏ `--master-data` khi chưa có workbook đã review:

```powershell
python scripts\build_alpha_knowledge_package.py `
  --raw-dir RawData `
  --output-dir output\alpha-knowledge-package
```

## Output

```text
output/alpha-knowledge-package/
  manifest.json
  validation_report.json
  validation_report.md
  00_report_context.md
  01_executive_summary.md
  02_operational_timeline.md
  02_confirmed_incidents.md
  03_recurrence_patterns.md
  04_alert_patterns.md
  05_ticket_impact.md
  06_data_quality.md
  normalized_data.xlsx
```

- Upload vào Alpha: tám file Markdown, bao gồm `02_operational_timeline.md`.
- Giữ để audit local: `manifest.json`, hai file `validation_report.*`, và `normalized_data.xlsx`.

## Timeline-First Investigation

`02_operational_timeline.md` is the primary entry point for date-range questions.
It contains ordered operational stories:

- `CONFIRMED_INCIDENT`: an incident story with RCA, resolution, recurrence, and gaps.
- `MONITORING_SIGNAL`: a grouped Zabbix-signal story with detection, grouping,
  recovery evidence, noise-review assessment, and gaps.

Each story includes timestamped milestones, conclusion, responsibility domain,
user-impact status, evidence coverage, investigation gaps, and related IDs. Correlation is
investigation context, not proof of RCA or user impact.

## Upload Gate

Mở:

```text
output/alpha-knowledge-package/validation_report.md
```

Chỉ upload khi có cả hai dòng:

```text
Status: PASS
Upload allowed: YES
```

Converter kiểm tra ba reconciliation invariant:

```text
incident_form_rows = normalized_incidents + rejected_incident_rows
zabbix_rows = normalized_alert_rows + rejected_alert_rows
issue_comment_rows = aggregated_ticket_comment_count + rejected_comment_rows
```

Với sample raw hiện tại, baseline là:

```text
confirmed incidents = 52
raw Zabbix alerts = 1000
unique tickets = 923
issue comment rows = 2652
MS2 | VNPT | High latency = 16 confirmed incidents
XAS | CMC | Fiber optic cable failure = 4 confirmed incidents
```

## Refresh Dữ Liệu

1. Thay ba file trong `RawData/` bằng export mới, giữ đúng filename.
2. Review và cập nhật master data nếu có mapping mới.
3. Chạy lại converter.
4. Kiểm tra `validation_report.md`.
5. Spot-check `normalized_data.xlsx`.
6. Chỉ khi status là `PASS`, cập nhật tám Markdown trong Knowledge Expert.

## Cảnh Báo Thường Gặp

### Openpyxl Data Validation Warning

Khi đọc master-data template, console có thể hiện:

```text
Data Validation extension is not supported and will be removed
```

Converter chỉ đọc master workbook và không ghi đè file nguồn. Warning này không làm package fail. Nếu sau này dùng Python để ghi lại master workbook, cần backup file trước vì Excel dropdown validation có thể bị loại bỏ.

### Validation FAIL

Không upload package. Mở `validation_report.md`, sau đó kiểm tra:

- File input có đổi schema hoặc thiếu cột bắt buộc.
- Timestamp không parse được.
- Tổng row input không reconcile với row normalized và rejected.
- Known sample check bị sai sau khi thay đổi logic grouping.

## Chạy Test

```powershell
python -m unittest discover -s tests -v
```

Test suite bao gồm fixture nhỏ và integration check trên ba raw file đang cung cấp.
