# Xuất slide ra PowerPoint (mở được bằng app Mở Tài Liệu, Keynote, PowerPoint)

Đầu ra: `~/Documents/1-nghe-trainer/goi-dung-video-ai/slide-pptx/` (không lên GitHub).

| File ra | Từ đâu | Sửa chữ được |
|---|---|---|
| `bai-1…8-*.pptx` | chụp từng slide của bản xem `slide-ban-xem/bai-N.html` (`shot.mjs` → `build_pptx.py`) | không (mỗi slide là ảnh) |
| `ghi-chu-trainer-8-bai.docx` | ghi chú trainer của 8 bài (`build_docx.py`) | có |
| `bai-0-tong-quan-goi.pptx` | `1-quy-trinh.md`, `2-lo-trinh.md`, `4-phieu-khao-sat-va-nghiem-thu.md` (`build_extra.py`) | có |
| `bo-bieu-mau.pptx` | `bo-bieu-mau/01…04` (`build_extra.py`) | có |

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
node shot.mjs ~/Documents/1-nghe-trainer/goi-dung-video-ai/slide-ban-xem png
```
```bash
venv/bin/python build_pptx.py png ~/Documents/1-nghe-trainer/goi-dung-video-ai/slide-pptx
```
```bash
venv/bin/python build_docx.py png ~/Documents/1-nghe-trainer/goi-dung-video-ai/slide-pptx
```
```bash
venv/bin/python build_extra.py ~/Documents/1-nghe-trainer/goi-dung-video-ai/slide-pptx
```
Kiểm hiển thị từng slide như Quick Look thấy: `bash check.sh <file.pptx> <thư mục ra>` rồi xem `sheet-*.png`.
Sửa nội dung `1-quy-trinh.md`, `2-lo-trinh.md`, phiếu hay biểu mẫu thì sửa cả `build_extra.py` cho khớp rồi xuất lại.
