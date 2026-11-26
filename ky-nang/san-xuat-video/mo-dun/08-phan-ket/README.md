---
description: "Khối 08 phần kết: màn chốt nguyên văn, thẻ cuối, dẫn bản đầy đủ."
---

# Khối 08-phan-ket: Kết: màn chốt (cta) · thẻ cuối (nhận diện / dẫn bản đầy đủ) · màn kết YouTube 15–20 s · lịch phát hành

**Dùng trong:** cả 4
**Đầu vào:** câu chốt, tên chủ đề/tập, lịch do David cung cấp
**Đầu ra:** cảnh cta · composition the-cuoi · ENDCARD (danh-sach-cat.js)
**Tham số hồ sơ:** chung: youtube.man_ket_s, highlight: the_cuoi_s
**Sửa khối này thì chạy lại:** 17

**File thật (code, một bản duy nhất):**
- `dung-video-theo-phong-cach/assets/mau-remotion/src/keu-goi-hanh-dong.js`
- `…/thanh-phan/hanh-dong.jsx (Cta)`
- `…/thanh-phan/man-ket.jsx`
- `…/thanh-phan/man-ket-youtube.jsx`
- `montage chuong-trinh.jsx (CtaEnd, EndCard)`

## Luật
- **Màn chốt** (`cta`, khoảng 4 s cuối mọi video): video thu vào khung bo góc, một câu + biểu tượng + tick + "ting".
  Câu là **NGUYÊN VĂN lời người nói**: video của David dùng câu David nói ở cuối (lời kêu gọi, lời chào…); highlight và podcast dọc
  trích ngắn theo `cat-doan-noi-bat` luật 4 (có câu kêu gọi nguyên văn thì màn chốt dùng câu đó; không có thì kết ở câu chốt ý). Claude không
  tự viết; `kind` theo ý của câu (`comment` · `save` · `follow` · `share` · `moi`). Claude không hỏi David chọn câu chốt — quy trình đã định sẵn; Claude nêu
  câu đã dùng trong báo cáo.
- **Video dọc ngắn** (luật ở `thu-vien-tai-nguyen/nhan-dien-chung.md` mục 1): màn chốt không thu nhỏ video — ô câu nguyên văn nằm trên khung
  hình, ở đáy vùng an toàn; không có thẻ cuối, video kết thúc ở chữ cuối để tự lặp. Các dòng dưới về thẻ cuối chỉ áp dụng cho video ngang / dọc dài.
- **Dẫn dắt theo luật kênh** (`ho-so-thuong-hieu/kenh.json`): câu do Claude tự soạn **không đưa lên video**, chỉ nằm ở **mô tả + bình luận ghim**. Kiểu dẫn dắt của
  bài do phiếu lọc (khối 00) gán theo tỉ lệ **4 Không · 4 Gợi mở · 2 Mời** (bài thứ 5 và thứ 10 trong mỗi chục bài là Mời):
  - **Không** thì mô tả + bình luận ghim mời người xem bình luận đúng một trong hai từ: "**Vấn đề**" (đang vướng mắc) / "**Kết quả**" (đã làm được).
  - **Gợi mở** thì mô tả + bình luận ghim: một câu hỏi tự xét bản thân gắn với bài + mời bình luận "Vấn đề" / "Kết quả".
  - **Mời** thì mô tả + bình luận ghim: bài con người "Nhắn mình một chữ **'gỡ'**…", bài công nghệ "nhắn mình hai chữ **'số hoá'**" — không hứa kết quả; bài con người không nói giá, không nói gói; bài công nghệ (hướng 3) được nói giá sản phẩm công nghệ.
  Khi David tự nói câu mời / câu hỏi trong video thì màn chốt dùng đúng câu đó. Bài Facebook cá nhân (đời thường) không cần dẫn dắt theo kiểu kênh.
- **Thẻ cuối** (video ngang / dọc dài): nhận diện (chủ đề + DAVID, khoảng 1,6 s) cho mọi video có chủ đề; dẫn bản đầy đủ gồm "Bản đầy đủ trên kênh
  …" + tên tập gốc + người nói (`the_cuoi_s`). Không có nút phát, không có logo nền tảng, không có câu gợi tò mò tự viết.
- **Màn kết YouTube** (video dài hơn 3 phút đăng YouTube): `project.ytEnd = 20` (1 video/podcast, ghi sau bước làm sạch) · ke-hoach.json `"ytEnd": 20`
  (vlog) — khung chừa 2 ô video + nút đăng ký, nhạc kênh nhỏ; David tự gắn phần tử trong YouTube Studio.
- **Lịch phát hành** do David cung cấp: `project.schedule` / `STAGE.schedule` / ke-hoach.json `"schedule"` / `"endcard": {"schedule"}` — Claude không tự đặt.
