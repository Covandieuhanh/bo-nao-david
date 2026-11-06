# Khối 08-ket-thuc: Kết: màn chốt (cta) · thẻ cuối (nhận diện / dẫn bản đầy đủ) · màn kết YouTube 15–20 s · lịch phát

**Dùng trong:** cả 4
**Đầu vào:** câu chốt, tên chủ đề/tập, lịch David đưa
**Đầu ra:** cảnh cta · composition the-cuoi · ENDCARD (edl.js)
**Tham số hồ sơ:** chung: youtube.man_ket_s, highlight: the_cuoi_s
**Sửa khối này → chạy lại:** 17

**File thật (code, một bản duy nhất):**
- `video-style-edit/assets/remotion-template/src/cta.js`
- `…/components/Action.jsx (Cta)`
- `…/components/EndCard.jsx`
- `…/components/YtEnd.jsx`
- `montage Show.jsx (CtaEnd, EndCard)`

## Luật
- **Ngoại lệ podcast đồ hoạ dọc trích ngắn** (David chốt 2026-11-06): không màn chốt `cta`, không câu kêu gọi trong lời; kết bằng màn hình cuối 3 s mời xem bản đầy đủ trên YouTube (`endcard.tease`). "Vấn đề" / "Kết quả" và câu hỏi tự soi nằm ở mô tả + bình luận ghim. Xem `cat-highlight-video/SKILL.md`.
- **Màn chốt THEO LUẬT KÊNH David** (`ho-so/kenh.json`, David chốt 05/11/2026 — thắng các gợi ý kind bên dưới cho kênh thương hiệu):
  kiểu dẫn dắt của bài do phiếu lọc (khối 00) gán theo tỉ lệ **4 Không · 4 Gợi mở · 2 Mời** (bài thứ 5 và 10 mỗi chục là Mời):
  - **Không** → `comment`: mời bình luận đúng một trong hai từ — "Bình luận **Vấn đề** nếu bạn đang kẹt ở đây" / "**Kết quả**" khi làm được.
  - **Gợi mở** → `comment`: một câu hỏi tự soi gắn với bài + mời bình luận "Vấn đề" / "Kết quả".
  - **Mời** → `moi`: "Nhắn mình một chữ **'gỡ'**…" — KHÔNG nói giá, không nói gói, không hứa kết quả.
  Bài đăng Facebook cá nhân (đời thường) thì không cần màn chốt kiểu kênh.
- **Màn chốt** (`cta`, ~4 s cuối mọi video): video lùi vào khung bo góc, một câu kêu gọi + biểu tượng + tick + "ting". Câu: video
  thường Claude tự viết (giọng David, ≤ 55 ký tự, một hành động — luat-chung 1a); highlight = nguyên văn câu mệnh lệnh của người nói.
- **Thẻ cuối**: nhận diện (chủ đề + DAVID, ~1,6 s) mọi video có chủ đề; highlight = dẫn bản đầy đủ ("XEM BẢN ĐẦY ĐỦ" + tên tập gốc + người nói, `the_cuoi_s`).
- **Màn kết YouTube** (video > 3 phút đăng YouTube): `project.ytEnd = 20` (1 video/podcast, ghi sau làm sạch) · plan.json `"ytEnd": 20` (vlog)
  — khung chừa 2 ô video + nút đăng ký, nhạc kênh nhỏ; David gắn phần tử trong YouTube Studio.
- **Lịch phát** David đưa: `project.schedule` / `STAGE.schedule` / plan.json `"schedule"` / `"endcard": {"schedule"}` — không tự đặt.
