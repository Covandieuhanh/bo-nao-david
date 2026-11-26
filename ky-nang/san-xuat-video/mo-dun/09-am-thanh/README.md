---
description: "Khối 09 âm thanh: nhạc nền theo tuyến, hiệu ứng tiếng, cân âm −14 LUFS."
---

# Khối 09-am-thanh: Âm thanh: nhạc kênh, tiếng ký hiệu, ting, vút; cân giọng −20 LUFS, bản cuối −14 LUFS

**Dùng trong:** cả 4
**Đầu vào:** âm thanh gốc
**Đầu ra:** trộn trong xem-truoc-ban-dung.py / xuat-chuong-trinh.mjs
**Tham số hồ sơ:** chung: `nhac.*` (nguồn duy nhất của mức nhạc), ghep-vlog: nhac_duoi_giong_LU, thuong-hieu.json: musicGapLU, highlight: nhac_chu_chinh
**Sửa khối này thì chạy lại:** 17

**File thật (code, một bản duy nhất):**
- `cat-doan-noi-bat/assets/nhac/`
- `dung-video-theo-phong-cach/assets/hieu-ung-am-thanh/`
- `dung-video-theo-phong-cach/scripts/xem-truoc-ban-dung.py` · `scripts/chuan-am.py`
- `dung-video-theo-phong-cach/assets/mau-dung-ghep/xuat-chuong-trinh.mjs`

## Luật
- **Âm thanh nhận diện:** tiếng ký hiệu `sting.wav` lúc hiện tiêu đề mở đầu; "ting" ở màn chốt; "vút" chỉ dùng khi bật kiểu tua cũ.
- **Thư viện nhạc kênh** `cat-doan-noi-bat/assets/nhac` (README liệt kê bài + nguồn). Claude TỰ chọn bài theo tuyến nội dung, không hỏi
  David (David đã tải nhiều nhạc cho từng loại nội dung). Khi David tải bài mới về `~/Music/nhac-nen`, Claude đặt tên theo tuyến, chép vào thư viện,
  đo `ebur128` và ghi mức cân chỉnh vào hồ sơ chung `nhac.muc` (gain = 10^((−15 − I)/20)), thêm vào `nhac.tuyen`.
- **Mức cân chỉnh từng bài: nguồn duy nhất** `ho-so-thuong-hieu/chung.json`, khoá `nhac.muc` (danh-sach-cat-vlog.py, xem-truoc-ban-dung.py, danh-sach-cat-doan-noi-bat.py, ap-dung-doan-noi-bat.py, chuong-trinh.jsx ghép đều đọc
  từ đây). `MUSIC.tracks` viết thủ công mà không ghi `gain` thì chuong-trinh.jsx tự lấy `nhac.muc`; không ghi `gain: 1`.

## Chuẩn âm lượng chung (mọi đầu ra: làm video, podcast, highlight, vlog ghép — mẫu: 3 clip "Đi trainer")
Mức âm lượng nằm ở nguồn duy nhất: hồ sơ chung `nhac`.
- **Giọng được cân chỉnh về −20 LUFS** lúc tạo dự án.
- **Giọng và nhạc:** nhạc thấp hơn giọng khoảng 23 dB lúc đang nói (`khoang_trong_duoi_giong_LU` 14, `nen_ty_le` 3, `nen_nha_ms` 400).
- **Cả bài:** −14 LUFS, sai số 0,5 LU (`nhac.do_to_cuoi_LUFS`), đỉnh −1,5 dB.
- **Giọng thu nhỏ thì được kéo lên, nhạc lớn thì được hạ xuống:** mức nhạc được tính theo độ lớn giọng đo được của từng video, rồi cả bài được đưa về chuẩn,
  nên giọng nhỏ hay lớn đều ra cùng một mức.
- `scripts/chuan-am.py <video>` tự chạy ở cuối mỗi lần xuất; thêm `--chi-do` để chỉ đo.
- **Kiểm bản cuối:** cả bài −14 LUFS ±0,5, đỉnh tối đa −1,5 dB, tiếng rè (highpass 12 kHz) **so với giọng** tăng tối đa 1 dB, nhạc lúc nói thấp
  hơn giọng 22–24 LU (khối 17). Không so sánh âm lượng thô với nguồn: giọng nhỏ được kéo lên −14 LUFS nên có chênh lệch là đúng.

## Nhạc theo tuyến nội dung
1. Sau khi chép lời, Claude đọc toàn bộ lời nói rồi chọn MỘT tuyến trong bảng hồ sơ chung `nhac.tuyen` (vui · tam_su · mat_mat · y_nghia ·
   kien_thuc), ghi `tuyen: '<tuyến>'` vào `chuyen-dong/src/du-an.js` (1 video: ghi SAU ap-dung-lam-sach.py — script này ghi đè du-an.js) + lý do 1 dòng
   vào ke-hoach-canh.md. Không ghi thì `xem-truoc-ban-dung.py` DỪNG (không có bài mặc định, để tránh gắn nhạc sôi động cho bài tâm sự).
   Cách chọn: tuyến là cảm xúc chủ đạo mà người xem cần (hình mẫu: Hieu Nguyen / Have A Sip tâm sự phù hợp piano ấm; Khoai Lang Thang du lịch phù hợp
   upbeat; video kiến thức thì dùng ambient trung tính). Chỉ định thủ công bài: `nhac: '<bài>'` trong `du-an.js`; tắt nhạc: `nhac: ''`.
2. Vlog ghép và highlight đổi tông theo đoạn (`TONE` soi / lang, multi-clip mục 2c, highlight luật 9); mức nhạc vẫn theo chuẩn chung.
3. **Chọn nhạc theo chính nội dung, từ cả thư viện**: thư viện nhạc là cả thư mục `cat-doan-noi-bat/assets/nhac/`, không chỉ bài đầu tuyến. Claude đọc nội dung, chọn bài phù hợp nhất trong cả thư viện, ghi `nhac: '<bài>'` vào `du-an.js` và lý do vào `ke-hoach-canh.md`; tiêu chí duy nhất là phù hợp với nội dung (không có luật "mỗi video một bài": hai video cùng phù hợp một bài thì dùng chung). Sau bước ghép, Claude đối chiếu dòng "nhạc nền: …" với kế hoạch. Nhạc David tải vào Drive `Tài nguyên làm video/` thì Claude đưa vào thư viện (tên theo tuyến, đo `ebur128`, ghi `nhac.muc`, thêm vào `nhac.tuyen`) rồi push lên GitHub; thư viện càng nhiều bài thì càng chọn được bài đúng.
