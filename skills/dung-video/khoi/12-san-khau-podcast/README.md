# Khối 12-san-khau-podcast: Sân khấu podcast: tên tập, ý đang bàn (TOPICS + PHẦN n), sóng âm theo người nói, nền lắng

**Dùng trong:** podcast, highlight từ podcast
**Đầu vào:** audio.wav, captions.js
**Đầu ra:** speakers.js, envelope.js, STAGE/TOPICS trong scenes.js → nen.mp4
**Tham số hồ sơ:** podcast: *
**Sửa khối này → chạy lại:** 17 (render lại nen → podcast_base → render_preview)

**File thật (code, một bản duy nhất):**
- `podcast-style-edit/scripts/{speakers.py,diarize.py (pyannote),envelope.py,podcast_base.py,pod_stills.sh}`
- `video-style-edit/assets/remotion-template/src/components/Stage.jsx`
- `podcast-style-edit/references/podcast-design.md`

## Cách làm

### Ai đang nói
```bash
PY=$(zsh $SKILL/scripts/py_setup.sh)                     # lần đầu cài numpy vào venv dùng chung
$PY $SKILL/scripts/speakers.py "$P"                      # pyannote tự đếm người (ghi số nếu biết chắc) → motion/src/speakers.js + check/speakers.md
$PY $SKILL/scripts/envelope.py "$P"                      # sóng âm → motion/src/envelope.js
```
Đọc `check/speakers.md`: đoạn `?` hoặc đoạn mà lời không hợp người (câu hỏi ↔ câu trả lời) → sửa `spk` trong `speakers.js`.
Ranh giới đổi người đã được dời vào khoảng lặng thật. Sóng âm đổi màu theo người đang nói (cam = người 0, xanh = người 1).
Tên người nói: chỉ khi có trong lời ("mình là…", "chào anh X") hoặc David đưa — **không tự đặt nhãn**; không có tên thì
`STAGE.speakers = []` (không hiện tên, chỉ màu sóng âm) và hỏi tên trong báo cáo.

### Kịch bản: sân khấu + cảnh
Viết trong `motion/src/scenes.js` theo `references/podcast-design.md`:
- `STAGE` = `{show, title, speakers: [{name, role}]}` — `show`: tên chương trình David đưa (không có → bỏ trống, không hiện);
  `title`: ý chính của tập, trích lời; `speakers`: chỉ tên thật (mục trên), theo thứ tự người 0, 1 trong `speakers.js`.
- `TOPICS` = ý đang bàn ở giữa sân khấu, **phủ kín cả tập** (đổi thưa, mỗi 40–90 s theo ý lớn, mốc = lúc bắt đầu ý), 2 dòng (`'DÒNG 1\nDÒNG 2'`),
  ≤ 5 từ/dòng, trích lời. Tự ẩn khi có thẻ/chữ to.
- **Màn hành động + màn chốt:** câu người nói nêu việc người nghe làm được → `action` (khung dọc) hoặc `card` có icon (khung ngang —
  `action` chỉ có bản dọc); cảnh cuối luôn `{id: 'chot', type: 'cta', start: <thời lượng − 4>, end: <thời lượng>, props: {text, kind}}`
  (ô câu chốt giữa sân khấu; `text` = nguyên văn câu David nói cuối tập — khối 08).
- `SCENES`: không `hook` mở đầu (khối 06); cảnh theo lời, một màn một ý, một hình; hình phủ khoảng 30 % thời lượng theo nội dung
  (`podcast-style-edit` luật riêng). Thẻ/chữ to tự đặt ở vùng giữa sân khấu (`PF.ov` trong podframe.js).
- Cảnh toàn màn hình phải kết thúc nội dung trên dải phụ đề + thanh thời gian (dọc y < 1240, ngang y < 790).
Ghi `$P/ke-hoach-canh.md` (bảng cảnh + TOPICS).

