---
description: "Khối 06 phần mở đầu 0–3 giây: câu chạm, thẻ tít nguyên văn."
---

# Khối 06-phan-mo-dau: Mở đầu 0–3 s: câu chạm, thẻ tiêu đề nguyên văn (highlight), đoạn ghép mở vlog, teaser podcast dài

**Dùng trong:** cả 4
**Đầu vào:** lời + bản đồ ý
**Đầu ra:** cảnh hook (canh.js) · pow 0–2,5 s (danh-sach-cat.js) · ke-hoach.json intro · doan-gioi-thieu.py
**Tham số hồ sơ:** lam-video: the_tit_mo_s, ghep-vlog: mo_dau.*, chung: youtube.teaser_*
**Sửa khối này thì chạy lại:** 05, 17

**File thật (mã nguồn, một bản duy nhất):**
- `dung-video-theo-phong-cach/assets/mau-remotion/src/thanh-phan/lop-phu.jsx (Hook)`
- `dung-video-theo-phong-cach/scripts/doan-gioi-thieu.py`
- `dung-video-theo-phong-cach/scripts/danh-sach-cat-vlog.py (intro)`

## Luật
- Trong 0–3 s đầu, video nói ngay chủ đề là gì hoặc đang đặt cược điều gì (nguyen-tac 1).
- **Làm video, podcast: không có thẻ tiêu đề mở đầu mặc định** — tít do AI tự rút ý có thể chưa đúng điều David muốn truyền tải. 0–3 s đầu là lời thật
  của David (câu chạm). Chỉ làm `hook` khi David yêu cầu, chữ phải nguyên văn. `hook` 2 dòng ở khung ngang đang bị cắt mất dòng 2; cần sửa Hook
  trước khi dùng cho khung ngang; hoặc dùng cảnh tự vẽ `IntroTieuDe` (`rieng/intro-tieu-de.jsx`: dòng chữ nhỏ + tên rơi xuống từng chữ + chữ to xuất hiện mạnh, quét sáng,
  đặt trên cảnh không có lời nói dài 3–3,5 giây; mẫu tham khảo: việc #39).
- Thẻ tít (highlight, hoặc khi David yêu cầu) được phép đè lên người trong 0–2,5 s (khối 05 vẫn chuyển sang toàn màn hình nếu thẻ che mặt hoặc thân trên).
- **Highlight:** thẻ tiêu đề là **cụm nguyên văn then chốt nhất** của clip, ngắn, 2 dòng (`cat-doan-noi-bat` luật 7) (`"tit"` trong
  phuong-an.json, rồi `danh-sach-cat-doan-noi-bat.py` tự đặt pow 0–2,5 s); khung hình ở giây 0,3 là ảnh bìa.
- **Vlog:** đưa đoạn ghép các cảnh ấn tượng nhất (2 phách mỗi cảnh) hoặc câu nêu nhiệm vụ / tiền cược lên đầu — theo nhieu-doan-video.md 2d (kiểu 1/2/3). Thẻ tiêu
  đề trên đoạn ghép chỉ ghi tên chương trình, tên địa điểm hoặc lời nguyên văn.
- Video dài hơn 10 phút đăng YouTube: làm teaser 15–25 s từ câu then chốt sau khi render (`doan-gioi-thieu.py`, khối 15 chạy lại chương).
