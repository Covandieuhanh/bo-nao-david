---
description: "Tách một buổi nói dài (buổi gặp, buổi 1:1, bài giảng) thành nhiều video theo hướng công việc: chọn đoạn, cắt, mỗi video một dự án, dựng, phát hành."
---

# Tách buổi dài thành nhiều video theo hướng

Dùng khi David nói "cắt đoạn thừa, phân ra thành các video theo hướng công việc" hoặc gửi một buổi nói dài nhiều chủ đề. Làm thật lần đầu
22/11/2026 (buổi gặp 37 phút thành 3 video); kế hoạch dùng lại được ở [vi-du-tach-video.json](vi-du-tach-video.json).

## 1. Làm sạch + chép lời buổi gốc một lần
Công thức "Làm video" bước 1–5 cho cả buổi (một dự án `tap-<buổi>`): làm sạch, chép lời đã soát (`chuyen-dong/src/phu-de.js`). Các video
tách ra dùng lại đúng phụ đề này, không chép lời lại.

## 2. Phân hướng theo khối 00 mục 0b (bắt buộc)
Chia đoạn, gán hướng, ghép trọn ý, ghi `<thư mục tập>/phan-huong.md` + nhật ký nội dung từng hướng (`du-an/nhat-ky-noi-dung/`), đối chiếu
kho 100 với hướng trainer: làm đúng [khối 00 mục 0b](../../mo-dun/00-sang-loc-noi-dung/README.md). Thêm khi tách từ một buổi dài:
- In lời theo khối 20 giây (mốc + chữ) để đọc hết một lượt; đoạn **thừa** gồm cả đoạn cầm máy cho xem màn hình mà máy quay không thấy.
- Phần đời thường / hành trình của David không thuộc hẳn hướng nào ra được bản riêng "nhân hiệu" (cây nội dung kênh trainer, khối 00 mục 1).
- Mốc mỗi đoạn lấy **đúng đầu / cuối câu** trong phụ đề (in các dòng quanh mốc để chọn); câu vướng lằn ranh nằm giữa đoạn thì tách đoạn
  bỏ riêng câu đó. Trình David bảng "video · hướng · đoạn · dài" + đoạn cắt + mục cần chốt (4 phần), có mặc định.

## 3. Cắt + tạo dự án
Viết `ke-hoach-tach.json` theo mẫu `vi-du-tach-video.json` (mỗi video: `doan`, `topic`, `tuyen`, `ytEnd`) rồi:
```bash
python3 -I $SKILL/scripts/tach-video.py ke-hoach-tach.json
```
Mỗi video ra `~/Movies/tap-<tên>/2-ban-day-du` có sẵn video gốc đã nối (đệm 0,12 s, fade âm 50 ms), phụ đề dời mốc, `du-an.js`,
`canh.js` khung có hàm `g()`, `ke-hoach-canh.md` khung, `kiem-tra/tach-video.json`.

## 4. Dựng từng video (như "Làm video", từ bước chẩn đoán)
- `canh.js`: viết mốc theo **video gốc** (đối chiếu phụ đề gốc dễ), bọc bằng `g(giây)`; cảnh tự vẽ dùng `ve(id, đầu, cuối, {…})`.
- Chẩn đoán + mở kho hình mẫu chọn cách cho từng ý (`thiet-ke-bo-cuc/tu-chon.md` bước 4d), ghi `Nguồn kho:`; các video cùng buổi được
  phép chung một kiểu hình (máy soát nhắc P1 "giống tập trước" thì bỏ qua được).
- `node $SKILL/scripts/soat-canh.mjs <dự án>` → `bash $SKILL/scripts/anh-kiem-canh.sh <dự án>` (lưới ảnh mỗi cảnh trên khung thật) → soát
  bằng mắt: không che ai, chữ đọc được.
- Render: `cd <dự án>/chuyen-dong && node xuat-video.mjs` → `python3 -I $SKILL/scripts/xem-truoc-ban-dung.py <dự án>` → video từ khoảng
  4 phút trở lên thêm teaser `doan-gioi-thieu.py <dự án> <từ-đến> …` (mốc trong video đã cắt = `g(giây gốc)`); video ngắn bỏ teaser.

## 5. Phát hành từng video
Ảnh thu nhỏ `anh-thu-nho.sh` (nguồn = giây trong video đã cắt), `phat-hanh/phat-hanh.md`: 3 tiêu đề, mô tả, chương (cộng độ dài teaser
trong `phat-hanh/doan-gioi-thieu.json`), bình luận ghim, màn kết gắn các video cùng bộ, mục "Cần David quyết trước khi đăng". Gửi David
bản nhẹ dưới 30 MB mỗi video.
