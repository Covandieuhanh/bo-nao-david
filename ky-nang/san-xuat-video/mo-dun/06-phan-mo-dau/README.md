# Khối 06-phan-mo-dau: Mở đầu 0–3 s: câu chạm, thẻ tít nguyên văn (highlight), đoạn ghép mở vlog, teaser podcast dài

**Dùng trong:** cả 4
**Đầu vào:** lời + bản đồ ý
**Đầu ra:** cảnh hook (canh.js) · pow 0–2,5 s (danh-sach-cat.js) · plan.json intro · doan-gioi-thieu.py
**Tham số hồ sơ:** lam-video: the_tit_mo_s, ghep-vlog: mo_dau.*, chung: youtube.teaser_*
**Sửa khối này → chạy lại:** 05, 17

**File thật (code, một bản duy nhất):**
- `dung-video-theo-phong-cach/assets/remotion-template/src/components/lop-phu.jsx (Hook)`
- `dung-video-theo-phong-cach/scripts/doan-gioi-thieu.py`
- `dung-video-theo-phong-cach/scripts/danh-sach-cat-vlog.py (intro)`

## Luật
- 0–3 s nói ngay video về cái gì / đang đặt cược gì (nguyen-tac 1).
- **Làm video, podcast: không thẻ tít mở đầu mặc định** — tít tự rút ý có thể chưa đúng điều David muốn truyền tải. 0–3 s là lời thật
  của David (câu chạm). Chỉ làm `hook` khi David yêu cầu, chữ nguyên văn. `hook` 2 dòng ở khung ngang đang bị cắt dòng 2 — sửa Hook
  trước khi dùng cho khung ngang.
- Thẻ tít (highlight, hoặc khi David yêu cầu) được đè lên người 0–2,5 s (khối 05 vẫn chuyển toàn màn hình nếu che mặt/thân trên).
- **Highlight:** thẻ tít = **cụm nguyên văn đắt nhất** của clip, ngắn, 2 dòng (`cat-doan-noi-bat` luật 7) (`"tit"` trong
  phuong-an.json → `danh-sach-cat-doan-noi-bat.py` tự đặt pow 0–2,5 s); khung 0,3 s = ảnh bìa.
- **Vlog:** đoạn ghép cảnh đắt nhất (2 phách/cảnh) hoặc câu nêu nhiệm vụ / tiền cược lên đầu — multi-clip.md 2d (kiểu 1/2/3). Thẻ tiêu
  đề trên đoạn ghép chỉ ghi tên chương trình / tên nơi hoặc lời nguyên văn.
- Video > 10 phút đăng YouTube: teaser 15–25 s câu đắt nhất sau render (`doan-gioi-thieu.py`, khối 15 chạy lại chương).
