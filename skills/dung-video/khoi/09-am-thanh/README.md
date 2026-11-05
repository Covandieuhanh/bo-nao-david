# Khối 09-am-thanh: Âm thanh: nhạc kênh cố định, tiếng ký hiệu, ting, vút; cân giọng −20 LUFS, bản cuối −14 LUFS

**Dùng trong:** cả 4
**Đầu vào:** tiếng gốc
**Đầu ra:** trộn trong render_preview.py / render-show.mjs
**Tham số hồ sơ:** ghep-vlog: nhac_duoi_giong_LU, brand.json: musicGapLU
**Sửa khối này → chạy lại:** 17

**File thật (code, một bản duy nhất):**
- `cat-highlight-video/assets/music/`
- `video-style-edit/assets/sfx/`
- `video-style-edit/scripts/render_preview.py`
- `video-style-edit/assets/montage-template/render-show.mjs`

## Luật
- Nhạc chỉ các bài cố định: `cat-highlight-video/assets/music` (soi-*, lang-*) + 2 bài intro vlog — không tự thêm bài; thiếu thì báo David.
- Tiếng ký hiệu `sting.wav` lúc hiện tiêu đề mở đầu; "ting" ở màn chốt; "vút" chỉ khi bật kiểu tua cũ.
- Giọng cân −20 LUFS; nhạc dưới lời: vlog thấp hơn giọng `nhac_duoi_giong_LU`, 1 video / podcast rất nhỏ (brand.json `musicGapLU`); bản cuối −14 LUFS.
- Kiểm bản cuối: âm lượng chênh nguồn ≤ 0,5 dB, tiếng rè (highpass 12 kHz) ≤ 1 dB (khối 17).

## Nhạc nền theo TUYẾN NỘI DUNG + mức nhạc khi nói (David chốt 2026-11-05)
1. Sau khi chép lời, Claude đọc toàn bộ lời → chọn MỘT tuyến trong bảng hồ sơ chung `nhac.tuyen` (vui · tam_su · mat_mat · y_nghia ·
   kien_thuc), ghi `tuyen: '<tuyến>'` vào `motion/src/project.js` (1 video: ghi SAU clean_apply — nó viết đè project.js) + lý do 1 dòng
   vào ke-hoach-canh.md. Không ghi → `render_preview.py` DỪNG (hết mặc định "Upbeat Vlog" — 2026-11-05 podcast tâm sự bị gắn nhạc sôi động).
   Cách chọn: tuyến = cảm xúc chủ đạo người xem cần (hình mẫu: Hieu Nguyen / Have A Sip tâm sự → piano ấm; Khoai Lang Thang du lịch →
   upbeat; video kiến thức → ambient trung tính). Ép tay bài: `music: '<bài>'`; tắt: `music: ''`.
2. Mức: khoảng trống / mở / kết = giọng − `khoang_trong_duoi_giong_LU` (20); khi đang nói nén theo giọng (ngưỡng = giọng −
   `nen_nguong_duoi_giong_dB` 14, tỉ lệ 20, nhả 1,5 s — không "bơm" theo từng hơi thở) → đo được 30–33 LU dưới giọng (trước: chỉ 17 LU → "nhạc to").
3. Vlog ghép giữ tông theo đoạn (`TONE` soi/lang) như cũ; highlight giữ mức cũ.
