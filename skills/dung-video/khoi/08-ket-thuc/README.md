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
- **Podcast đồ hoạ dọc trích ngắn** (08/11, thay ngoại lệ 06/11): màn chốt và thẻ cuối theo **cùng luật highlight** (`cat-highlight-video` luật 4 và 11): có câu kêu gọi nguyên văn → màn chốt bằng câu đó, không có → kết ở câu chốt ý; thẻ cuối "Bản đầy đủ trên kênh …" + tên tập gốc, không nút phát, không logo nền tảng, không câu gợi tò mò tự viết. "Vấn đề" / "Kết quả" và câu hỏi tự soi nằm ở mô tả + bình luận ghim. Xem `cat-highlight-video/SKILL.md`.
- **Dẫn dắt THEO LUẬT KÊNH David** (`ho-so/kenh.json`, 05/11; sửa 08/11: câu tự soạn **không lên video**, nằm ở **mô tả + bình luận ghim**):
  kiểu dẫn dắt của bài do phiếu lọc (khối 00) gán theo tỉ lệ **4 Không · 4 Gợi mở · 2 Mời** (bài thứ 5 và 10 mỗi chục là Mời):
  - **Không** → mô tả + ghim mời bình luận đúng một trong hai từ: "**Vấn đề**" (đang kẹt) / "**Kết quả**" (làm được).
  - **Gợi mở** → mô tả + ghim: một câu hỏi tự soi gắn với bài + mời bình luận "Vấn đề" / "Kết quả".
  - **Mời** → mô tả + ghim: "Nhắn mình một chữ **'gỡ'**…" — KHÔNG nói giá, không nói gói, không hứa kết quả.
  David tự nói câu mời / câu hỏi trong video → màn chốt dùng đúng câu đó, `kind` theo ý câu (`comment` / `moi`).
  Bài đăng Facebook cá nhân (đời thường) thì không cần dẫn dắt kiểu kênh.
- **Màn chốt** (`cta`, ~4 s cuối mọi video): video lùi vào khung bo góc, một câu kêu gọi + biểu tượng + tick + "ting".
  Câu = **NGUYÊN VĂN lời người nói** (07/11): video của David dùng câu David nói ở cuối (lời kêu gọi, lời chào…); highlight theo
  `cat-highlight-video` luật 4. Không tự viết; `kind` theo ý câu.
- **Video dọc ngắn** (David chốt 10/11/2026, nhà luật: `luat-chung.md` mục 5): màn chốt không thu nhỏ video — ô câu nguyên văn nằm trên khung hình, đáy vùng an toàn; **không thẻ cuối**, video kết ở chữ cuối để tự lặp. Mọi dòng dưới về thẻ cuối chỉ cho video ngang / dọc dài.
- **Thẻ cuối**: nhận diện (chủ đề + DAVID, ~1,6 s) mọi video có chủ đề; highlight = dẫn bản đầy đủ ("Bản đầy đủ trên kênh …" + tên tập gốc + người nói, không nút phát, `the_cuoi_s`).
- **Màn kết YouTube** (video > 3 phút đăng YouTube): `project.ytEnd = 20` (1 video/podcast, ghi sau làm sạch) · plan.json `"ytEnd": 20` (vlog)
  — khung chừa 2 ô video + nút đăng ký, nhạc kênh nhỏ; David gắn phần tử trong YouTube Studio.
- **Lịch phát** David đưa: `project.schedule` / `STAGE.schedule` / plan.json `"schedule"` / `"endcard": {"schedule"}` — không tự đặt.
