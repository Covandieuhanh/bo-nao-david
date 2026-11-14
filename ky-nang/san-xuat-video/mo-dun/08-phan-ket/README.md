# Khối 08-phan-ket: Kết: màn chốt (cta) · thẻ cuối (nhận diện / dẫn bản đầy đủ) · màn kết YouTube 15–20 s · lịch phát

**Dùng trong:** cả 4
**Đầu vào:** câu chốt, tên chủ đề/tập, lịch David đưa
**Đầu ra:** cảnh cta · composition the-cuoi · ENDCARD (danh-sach-cat.js)
**Tham số hồ sơ:** chung: youtube.man_ket_s, highlight: the_cuoi_s
**Sửa khối này → chạy lại:** 17

**File thật (code, một bản duy nhất):**
- `dung-video-theo-phong-cach/assets/khuon-remotion/src/keu-goi-hanh-dong.js`
- `…/thanh-phan/hanh-dong.jsx (Cta)`
- `…/thanh-phan/man-ket.jsx`
- `…/thanh-phan/man-ket-youtube.jsx`
- `montage chuong-trinh.jsx (CtaEnd, EndCard)`

## Luật
- **Màn chốt** (`cta`, ~4 s cuối mọi video): video lùi vào khung bo góc, một câu + biểu tượng + tick + "ting".
  Câu = **NGUYÊN VĂN lời người nói**: video của David dùng câu David nói ở cuối (lời kêu gọi, lời chào…); highlight và podcast dọc
  trích ngắn theo `cat-doan-noi-bat` luật 4 (có câu kêu gọi nguyên văn → màn chốt bằng câu đó; không có → kết ở câu chốt ý). Không
  tự viết; `kind` theo ý câu (`comment` · `save` · `follow` · `share` · `moi`). Không hỏi David chọn câu chốt — quy trình đã định, nêu
  câu đã dùng trong báo cáo.
- **Video dọc ngắn** (luật ở `thu-vien-tai-nguyen/nhan-dien-chung.md` mục 1): màn chốt không thu nhỏ video — ô câu nguyên văn nằm trên khung
  hình, đáy vùng an toàn; không thẻ cuối, video kết ở chữ cuối để tự lặp. Các dòng dưới về thẻ cuối chỉ cho video ngang / dọc dài.
- **Dẫn dắt theo luật kênh** (`ho-so-thuong-hieu/kenh.json`): câu tự soạn **không lên video**, nằm ở **mô tả + bình luận ghim**. Kiểu dẫn dắt của
  bài do phiếu lọc (khối 00) gán theo tỉ lệ **4 Không · 4 Gợi mở · 2 Mời** (bài thứ 5 và 10 mỗi chục là Mời):
  - **Không** → mô tả + ghim mời bình luận đúng một trong hai từ: "**Vấn đề**" (đang kẹt) / "**Kết quả**" (làm được).
  - **Gợi mở** → mô tả + ghim: một câu hỏi tự soi gắn với bài + mời bình luận "Vấn đề" / "Kết quả".
  - **Mời** → mô tả + ghim: "Nhắn mình một chữ **'gỡ'**…" — KHÔNG nói giá, không nói gói, không hứa kết quả.
  David tự nói câu mời / câu hỏi trong video → màn chốt dùng đúng câu đó. Bài Facebook cá nhân (đời thường) không cần dẫn dắt kiểu kênh.
- **Thẻ cuối** (video ngang / dọc dài): nhận diện (chủ đề + DAVID, ~1,6 s) mọi video có chủ đề; dẫn bản đầy đủ = "Bản đầy đủ trên kênh
  …" + tên tập gốc + người nói (`the_cuoi_s`). Không nút phát, không logo nền tảng, không câu gợi tò mò tự viết.
- **Màn kết YouTube** (video > 3 phút đăng YouTube): `project.ytEnd = 20` (1 video/podcast, ghi sau làm sạch) · ke-hoach.json `"ytEnd": 20`
  (vlog) — khung chừa 2 ô video + nút đăng ký, nhạc kênh nhỏ; David gắn phần tử trong YouTube Studio.
- **Lịch phát** David đưa: `project.schedule` / `STAGE.schedule` / ke-hoach.json `"schedule"` / `"endcard": {"schedule"}` — không tự đặt.
