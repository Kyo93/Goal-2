# IT Operations Knowledge Package for Alpha Intelligence

MVP này chuyển đổi ba file Excel raw thành bộ tài liệu chuẩn để upload vào Alpha Intelligence. Python chịu trách nhiệm tính toán và kiểm tra dữ liệu; Alpha Knowledge Expert và Super Agent chịu trách nhiệm truy xuất và trả lời linh hoạt.

## Bắt Đầu Nhanh

1. Đọc [hướng dẫn chạy converter](docs/build-alpha-knowledge-package.md).
2. Kiểm tra `output/alpha-knowledge-package/validation_report.md`.
3. Chỉ khi report có `Status: PASS` và `Upload allowed: YES`, làm theo [hướng dẫn build trên Alpha](docs/build-on-alpha-intelligence.md).
4. Dùng [biên bản kiểm chứng sample package](docs/sample-package-validation.md) làm baseline đối soát.
5. Đọc [sample operational story](docs/sample-operational-story.md) để xem câu trả
   lời theo khoảng thời gian và giới hạn coverage của raw exports hiện tại.

## Lệnh Build

```powershell
python -m pip install -r requirements.txt

python scripts\build_alpha_knowledge_package.py `
  --raw-dir RawData `
  --master-data input\it-operations-master-data-template.xlsx `
  --output-dir output\alpha-knowledge-package
```

## Phạm Vi MVP

- Có: chuẩn hóa raw data, giữ source lineage, thống kê deterministic, audit workbook, validation gate, Markdown cho Alpha Knowledge Expert.
- Trục điều tra chính: `02_operational_timeline.md`, kể operational story theo
  milestones, conclusion, evidence coverage, gaps, responsibility domain và
  user-impact status.
- Không có: dashboard local, database, realtime sync, upload Alpha tự động, hoặc AI tự sửa dữ liệu nguồn.

Hai file HTML trong `docs/` là tài liệu ý tưởng từ phase trước. Chúng được giữ lại để tham khảo nhưng không phải kiến trúc MVP hiện tại.
