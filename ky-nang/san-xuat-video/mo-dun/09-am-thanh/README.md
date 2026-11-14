# Khối 09-am-thanh: Âm thanh: nhạc kênh, tiếng ký hiệu, ting, vút; cân giọng −20 LUFS, bản cuối −14 LUFS

**Dùng trong:** cả 4
**Đầu vào:** tiếng gốc
**Đầu ra:** trộn trong xem-truoc-ban-dung.py / xuat-chuong-trinh.mjs
**Tham số hồ sơ:** chung: `nhac.*` (một nguồn mức nhạc), ghep-vlog: nhac_duoi_giong_LU, brand.json: musicGapLU, highlight: nhac_chu_chinh
**Sửa khối này → chạy lại:** 17

**File thật (code, một bản duy nhất):**
- `cat-doan-noi-bat/assets/nhac/`
- `dung-video-theo-phong-cach/assets/hieu-ung-am-thanh/`
- `dung-video-theo-phong-cach/scripts/xem-truoc-ban-dung.py` · `scripts/chuan-am.py`
- `dung-video-theo-phong-cach/assets/khuon-dung-ghep/xuat-chuong-trinh.mjs`

## Luật
- **Âm thanh nhận diện:** tiếng ký hiệu `sting.wav` lúc hiện tiêu đề mở đầu; "ting" ở màn chốt; "vút" chỉ khi bật kiểu tua cũ.
- **Kho nhạc kênh** `cat-doan-noi-bat/assets/nhac` (README liệt kê bài + nguồn). Claude TỰ chọn bài theo tuyến nội dung, không hỏi
  David (David đã tải nhiều nhạc cho từng loại nội dung). Bài mới David tải về `~/Music/nhac-nen` → đặt tên theo tuyến, chép vào kho,
  đo `ebur128` và ghi mức cân vào hồ sơ chung `nhac.muc` (gain = 10^((−15 − I)/20)), thêm vào `nhac.tuyen`.
- **Mức cân từng bài: một nguồn** `ho-so-thuong-hieu/chung.json` → `nhac.muc` (vlog_edl, render_preview, hl_edl, hl_apply, chuong-trinh.jsx ghép đều đọc
  từ đây). `MUSIC.tracks` viết tay không ghi `gain` thì chuong-trinh.jsx tự lấy `nhac.muc`; đừng ghi `gain: 1`.

## Chuẩn âm lượng chung (mọi đầu ra: làm video, podcast, highlight, vlog ghép — mẫu: 3 clip "Đi trainer")
Mức nằm ở một chỗ: hồ sơ chung `nhac`.
- **Giọng cân −20 LUFS** lúc tạo dự án.
- **Giọng và nhạc:** nhạc thấp hơn giọng khoảng 23 dB lúc đang nói (`khoang_trong_duoi_giong_LU` 14, `nen_ty_le` 3, `nen_nha_ms` 400).
- **Cả bài:** −14 LUFS, sai số 0,5 LU (`nhac.do_to_cuoi_LUFS`), đỉnh −1,5 dB.
- **Giọng thu nhỏ thì kéo lên, nhạc to thì hạ xuống:** nhạc tính theo độ to giọng đo được của từng video, rồi cả bài được đưa về chuẩn,
  nên giọng nhỏ hay to đều ra cùng một mức.
- `scripts/chuan-am.py <video>` tự chạy cuối mỗi lần xuất; thêm `--chi-do` để chỉ đo.
- **Kiểm bản cuối:** cả bài −14 LUFS ±0,5, đỉnh ≤ −1,5 dB, tiếng rè (highpass 12 kHz) **so với giọng** tăng ≤ 1 dB, nhạc lúc nói thấp
  hơn giọng 22–24 LU (khối 17). Không so âm lượng thô với nguồn: giọng nhỏ được kéo lên −14 LUFS nên chênh là đúng.

## Nhạc theo tuyến nội dung
1. Sau khi chép lời, Claude đọc toàn bộ lời → chọn MỘT tuyến trong bảng hồ sơ chung `nhac.tuyen` (vui · tam_su · mat_mat · y_nghia ·
   kien_thuc), ghi `tuyen: '<tuyến>'` vào `motion/src/du-an.js` (1 video: ghi SAU clean_apply — nó viết đè du-an.js) + lý do 1 dòng
   vào ke-hoach-canh.md. Không ghi → `xem-truoc-ban-dung.py` DỪNG (không có bài mặc định, để không gắn nhạc sôi động cho bài tâm sự).
   Cách chọn: tuyến = cảm xúc chủ đạo người xem cần (hình mẫu: Hieu Nguyen / Have A Sip tâm sự → piano ấm; Khoai Lang Thang du lịch →
   upbeat; video kiến thức → ambient trung tính). Ép tay bài: `music: '<bài>'`; tắt: `music: ''`.
2. Vlog ghép và highlight đổi tông theo đoạn (`TONE` soi / lang, multi-clip mục 2c, highlight luật 9); mức nhạc vẫn theo chuẩn chung.
