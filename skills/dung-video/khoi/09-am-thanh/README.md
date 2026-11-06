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
- Giọng cân −20 LUFS; nhạc dưới lời và bản cuối: theo chuẩn âm lượng chung.
- Kiểm bản cuối: âm lượng chênh nguồn ≤ 0,5 dB, tiếng rè (highpass 12 kHz) ≤ 1 dB (khối 17).

## Chuẩn âm lượng chung cho mọi đầu ra (David chốt 2026-11-06, theo 3 clip "Đi trainer")
Áp dụng cho làm video, podcast, highlight, vlog ghép. Mức nằm ở một chỗ: hồ sơ chung `nhac`.
- **Giọng và nhạc:** nhạc thấp hơn giọng khoảng 23 dB lúc đang nói (`khoang_trong_duoi_giong_LU` 14, `nen_ty_le` 3, `nen_nha_ms` 400).
- **Cả bài:** −14 LUFS, sai số 0,5 LU, đỉnh −1,5 dB.
- **Giọng thu nhỏ thì kéo lên, nhạc to thì hạ xuống:** nhạc tính theo độ to giọng đo được của từng video, rồi cả bài được đưa về chuẩn, nên giọng nhỏ hay to đều ra cùng một mức.
- `scripts/chuan_am.py <video>` tự chạy cuối mỗi lần xuất; thêm `--chi-do` để chỉ đo.
- Mức nhạc 30–33 LU ở mục dưới là luật cũ, không còn dùng.

## Nhạc nền theo TUYẾN NỘI DUNG + mức nhạc khi nói (David chốt 2026-11-05)
1. Sau khi chép lời, Claude đọc toàn bộ lời → chọn MỘT tuyến trong bảng hồ sơ chung `nhac.tuyen` (vui · tam_su · mat_mat · y_nghia ·
   kien_thuc), ghi `tuyen: '<tuyến>'` vào `motion/src/project.js` (1 video: ghi SAU clean_apply — nó viết đè project.js) + lý do 1 dòng
   vào ke-hoach-canh.md. Không ghi → `render_preview.py` DỪNG (hết mặc định "Upbeat Vlog" — 2026-11-05 podcast tâm sự bị gắn nhạc sôi động).
   Cách chọn: tuyến = cảm xúc chủ đạo người xem cần (hình mẫu: Hieu Nguyen / Have A Sip tâm sự → piano ấm; Khoai Lang Thang du lịch →
   upbeat; video kiến thức → ambient trung tính). Ép tay bài: `music: '<bài>'`; tắt: `music: ''`.
2. Mức: theo chuẩn âm lượng chung ở trên. Luật cũ 05/11 (khoảng trống 20 LU, nén tỉ lệ 20, 30–33 LU dưới giọng) bị David thay ngày 06/11 vì nhạc quá nhỏ.
3. Vlog ghép giữ tông theo đoạn (`TONE` soi/lang) như cũ; highlight giữ mức cũ.
