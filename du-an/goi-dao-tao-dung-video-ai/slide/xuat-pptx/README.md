# Xuất slide ra PowerPoint (mở được bằng app Mở Tài Liệu, Keynote, PowerPoint)

Đầu ra: `~/Documents/1-nghe-nghiep/goi-dao-tao-dung-video-ai/slide-pptx/` (không lên GitHub).

| File ra | Từ đâu | Sửa chữ được |
|---|---|---|
| `bai-1…8-*.pptx` | mã gốc `../bai-N/` → bản xem `slide-ban-xem/bai-N.html` (`dung-ban-xem.py`) → chụp (`chup-man-hinh.mjs`) → `xuat-pptx.py` | không (mỗi slide là ảnh) |
| `ghi-chu-trainer-8-bai.docx` | ghi chú trainer của 8 bài (`xuat-docx.py`) | có |
| `bai-0-tong-quan-goi.pptx` | `1-quy-trinh.md`, `2-lo-trinh.md`, `4-phieu-khao-sat-va-nghiem-thu.md` (`dung-phan-them.py`) | có |
| `bo-bieu-mau.pptx` | `bo-bieu-mau/01…04` (`dung-phan-them.py`) | có |

**Cho người chưa biết gì về công nghệ** (David chốt 13/11/2026): mỗi bài có slide "Hiểu bằng chuyện đời thường" (chuyện quen thuộc → việc trên máy) và "Từ mới của bài" (thuật ngữ + nghĩa một câu), ngay sau slide mục tiêu; bài 1 có thêm "Mở cửa sổ lệnh". Nội dung ở `them-slide.py`. Slide nào có lệnh máy thì mỗi dòng lệnh kèm dòng "→ nghĩa là" hoặc thay bằng lời AI báo lại, chữ tiếng Anh dịch nghĩa (`viet-lai-de-hieu.py`, kiểu `.mean`, `.say`, `.fact` trong `giao-dien-slide.css`); bài 0 có hình tổng quan, 8 bước bằng hình, từ điển nhỏ (`dung-phan-them.py`). Biểu tượng Lucide; trong pptx sửa được, biểu tượng là ảnh PNG do `bieu-tuong.mjs` vẽ (`pic()` trong `thu_vien_slide.py`).

**Luật để Quick Look của macOS mở được** (đã thử 13/11/2026):
- Không ghi chú (notes) trong pptx: Quick Look treo. Ghi chú để file docx riêng.
- Không dùng hình vẽ (ô bo góc, chấm tròn) lặp giữa các slide: Quick Look lẫn hình của slide trước. Ô nền dùng bảng 1 ô (`box()` trong `thu_vien_slide.py`).
- Chữ có dấu (ắ, ụ, ề…) phải khai cùng một font cho latin + ea + cs + sym, lang vi-VN (`vi_fonts()` trong `thu_vien_slide.py`, tự chạy khi lưu). Thiếu thì Quick Look nhảy sang Times, dấu lệch.
- Dãn dòng: chữ thường 1,3 + cách đoạn 0,35 cỡ chữ; tít 1,15; mã 1,35; ô bảng 1,2.

**Chạy lại** (cần Chrome, Node có `@playwright/cli`, Python):
```bash
python3 -m venv venv && venv/bin/pip install python-pptx python-docx pillow
```
```bash
python3 them-slide.py && python3 dung-ban-xem.py ~/Documents/1-nghe-nghiep/goi-dao-tao-dung-video-ai/slide-ban-xem
```
```bash
node chup-man-hinh.mjs ~/Documents/1-nghe-nghiep/goi-dao-tao-dung-video-ai/slide-ban-xem png
```
```bash
venv/bin/python xuat-pptx.py png ~/Documents/1-nghe-nghiep/goi-dao-tao-dung-video-ai/slide-pptx
```
```bash
venv/bin/python xuat-docx.py png ~/Documents/1-nghe-nghiep/goi-dao-tao-dung-video-ai/slide-pptx
```
```bash
venv/bin/python dung-phan-them.py ~/Documents/1-nghe-nghiep/goi-dao-tao-dung-video-ai/slide-pptx
```
Kiểm hiển thị từng slide như Quick Look thấy: `bash kiem-tra.sh <file.pptx> <thư mục ra>` rồi xem `sheet-*.png`.
Sửa slide 8 bài: sửa `../bai-N/slides/*.html` (thứ tự ở `deck.json`, kiểu ở `../giao-dien-slide.css`), ảnh thật ánh xạ ở `anh-blob.json`.
Sửa nội dung `1-quy-trinh.md`, `2-lo-trinh.md`, phiếu hay biểu mẫu thì sửa cả `dung-phan-them.py` cho khớp rồi xuất lại.
