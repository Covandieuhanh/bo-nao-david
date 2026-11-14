# Xuất slide ra PowerPoint (mở được bằng app Mở Tài Liệu, Keynote, PowerPoint)

Đầu ra: `~/Documents/1-nghe-nghiep/goi-dao-tao-dung-video-ai/slide-pptx/` (không lên GitHub).

| File ra | Từ đâu | Sửa chữ được |
|---|---|---|
| `bai-1…8-*.pptx` | mã gốc `../bai-N/` → bản xem `slide-ban-xem/bai-N.html` (`build_ban_xem.py`) → chụp (`shot.mjs`) → `build_pptx.py` | không (mỗi slide là ảnh) |
| `ghi-chu-trainer-8-bai.docx` | ghi chú trainer của 8 bài (`build_docx.py`) | có |
| `bai-0-tong-quan-goi.pptx` | `1-quy-trinh.md`, `2-lo-trinh.md`, `4-phieu-khao-sat-va-nghiem-thu.md` (`build_extra.py`) | có |
| `bo-bieu-mau.pptx` | `bo-bieu-mau/01…04` (`build_extra.py`) | có |

**Cho người chưa biết gì về công nghệ** (David chốt 13/11/2026): mỗi bài có slide "Hiểu bằng chuyện đời thường" (chuyện quen thuộc → việc trên máy) và "Từ mới của bài" (thuật ngữ + nghĩa một câu), ngay sau slide mục tiêu; bài 1 có thêm "Mở cửa sổ lệnh". Nội dung ở `them_slide.py`. Slide nào có lệnh máy thì mỗi dòng lệnh kèm dòng "→ nghĩa là" hoặc thay bằng lời AI báo lại, chữ tiếng Anh dịch nghĩa (`viet_lai_de_hieu.py`, kiểu `.mean`, `.say`, `.fact` trong `deck.css`); bài 0 có hình tổng quan, 8 bước bằng hình, từ điển nhỏ (`build_extra.py`). Biểu tượng Lucide; trong pptx sửa được, biểu tượng là ảnh PNG do `icons.mjs` vẽ (`pic()` trong `deck_lib.py`).

**Luật để Quick Look của macOS mở được** (đã thử 13/11/2026):
- Không ghi chú (notes) trong pptx: Quick Look treo. Ghi chú để file docx riêng.
- Không dùng hình vẽ (ô bo góc, chấm tròn) lặp giữa các slide: Quick Look lẫn hình của slide trước. Ô nền dùng bảng 1 ô (`box()` trong `deck_lib.py`).
- Chữ có dấu (ắ, ụ, ề…) phải khai cùng một font cho latin + ea + cs + sym, lang vi-VN (`vi_fonts()` trong `deck_lib.py`, tự chạy khi lưu). Thiếu thì Quick Look nhảy sang Times, dấu lệch.
- Dãn dòng: chữ thường 1,3 + cách đoạn 0,35 cỡ chữ; tít 1,15; mã 1,35; ô bảng 1,2.

**Chạy lại** (cần Chrome, Node có `@playwright/cli`, Python):
```bash
python3 -m venv venv && venv/bin/pip install python-pptx python-docx pillow
```
```bash
python3 them_slide.py && python3 build_ban_xem.py ~/Documents/1-nghe-nghiep/goi-dao-tao-dung-video-ai/slide-ban-xem
```
```bash
node shot.mjs ~/Documents/1-nghe-nghiep/goi-dao-tao-dung-video-ai/slide-ban-xem png
```
```bash
venv/bin/python build_pptx.py png ~/Documents/1-nghe-nghiep/goi-dao-tao-dung-video-ai/slide-pptx
```
```bash
venv/bin/python build_docx.py png ~/Documents/1-nghe-nghiep/goi-dao-tao-dung-video-ai/slide-pptx
```
```bash
venv/bin/python build_extra.py ~/Documents/1-nghe-nghiep/goi-dao-tao-dung-video-ai/slide-pptx
```
Kiểm hiển thị từng slide như Quick Look thấy: `bash check.sh <file.pptx> <thư mục ra>` rồi xem `sheet-*.png`.
Sửa slide 8 bài: sửa `../bai-N/slides/*.html` (thứ tự ở `deck.json`, kiểu ở `../deck.css`), ảnh thật ánh xạ ở `anh-blob.json`.
Sửa nội dung `1-quy-trinh.md`, `2-lo-trinh.md`, phiếu hay biểu mẫu thì sửa cả `build_extra.py` cho khớp rồi xuất lại.
