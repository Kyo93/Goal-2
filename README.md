# IT Operations Knowledge Package for Alpha Intelligence

Project này chuẩn hóa 3 nguồn dữ liệu vận hành để Alpha Intelligent có thể trả lời câu hỏi theo site và khoảng thời gian:

- ISP Incident Report: confirmed incidents, RCA, resolution, responsibility domain.
- ITcenter Ticket: direct user/ticket evidence.
- Zabbix Alert: monitoring signal, telemetry, recurrence, and technical context.

Python xử lý phần deterministic như normalize, group, correlate, validate. Alpha Knowledge và SuperAgent dùng kết quả đã chuẩn hóa để giải thích cho người vận hành.

## Folder Chính

```text
01-RawData/              Raw exports dùng làm input local
02-Output/               Package, audit files, processed outputs
03-Data clean logic/     Tài liệu HTML mô tả logic làm sạch từng source
docs/                    Runbook, Alpha prompt, processor node code, architecture notes
openspec/                Plan/spec triển khai Alpha processing tool
scripts/                 Local helper scripts
src/                     Converter và processing/query tool code
tests/                   Unit/integration tests
```

## Build Local Package

```powershell
python -m pip install -r requirements.txt

python scripts\build_alpha_knowledge_package.py `
  --raw-dir 01-RawData `
  --master-data input\it-operations-master-data-template.xlsx `
  --output-dir 02-Output\alpha-knowledge-package
```

Chỉ upload Markdown lên Alpha Knowledge khi:

```text
02-Output/alpha-knowledge-package/validation_report.md
Status: PASS
Upload allowed: YES
```

## Alpha Processing Tool

Plan hiện tại nằm ở:

```text
openspec/changes/alpha-processing-tool/tasks.md
```

Tài liệu kiến trúc chính:

```text
docs/alpha-workflow-architecture.md
docs/alpha-processing-tool-runbook.md
```

Tài liệu logic làm sạch dữ liệu:

```text
03-Data clean logic/isp-incident-report-cleaning-logic.html
03-Data clean logic/zabbix-data-cleaning-logic.html
```

## Test

```powershell
python -m unittest discover -s tests -v
```
