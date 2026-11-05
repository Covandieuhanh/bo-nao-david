# Khối 18-xuat-app-dung: Xuất timeline DaVinci / dự án CapCut (chỉ khi David yêu cầu)

**Dùng trong:** làm video, podcast
**Đầu vào:** các cảnh đã render
**Đầu ra:** davinci/timeline.fcpxml · draft CapCut
**Tham số hồ sơ:** —
**Sửa khối này → chạy lại:** —

**File thật (code, một bản duy nhất):**
- `video-style-edit/scripts/{build_timeline.py,capcut_setup.sh,build_capcut.py}`
- `video-style-edit/references/handoff.md`

## Cách làm (chuyển nguyên văn từ SKILL.md cũ — ngày 2026-11-04)

## Timeline cho app dựng (chỉ khi được yêu cầu)

Người dùng nói "cần timeline DaVinci/CapCut", "muốn tự chỉnh trong DaVinci"… — lúc đầu hoặc sau khi giao. Đang làm mà
chưa rõ họ cần không thì **được hỏi** (một câu ngắn, kèm câu hỏi khác nếu có, không dừng các bước đang chạy).
- **DaVinci Resolve**: `python3 $SKILL/scripts/safe_guide.py "$P"` (nếu chưa có) → `python3 -I $SKILL/scripts/build_timeline.py "$P"`
  → viết `davinci/HUONG-DAN.md` theo `references/handoff.md` → `open -R "$P/davinci/timeline.fcpxml"`.
- **CapCut** (không nhập được FCPXML) → tạo thẳng **dự án CapCut** (draft) bằng pycapcut, sau khi đã render các cảnh:
  ```bash
  PY=$(zsh $SKILL/scripts/capcut_setup.sh)            # lần đầu cài pycapcut 0.0.4 vào ~/.cache/video-style-edit/capcut-venv
  $PY $SKILL/scripts/build_capcut.py "$P"             # → draft "edit-<tên>" trong thư mục dự án CapCut + $P/phu-de.srt
  ```
  Draft gồm: track chính = video sạch (có tiếng); track "Hieu ung" = mỗi cảnh một clip `<id>.mov` nền trong suốt đúng mốc
  (kéo/cắt/xoá từng cảnh); track "Phu de" = phụ đề là **chữ CapCut** sửa được (chữ, font, màu, vị trí), **cùng font
  với video** (BODY trong theme.js, đậm — người dùng thích font mặc định Be Vietnam Pro): TTF tải từ kho Google Fonts, kèm trong
  `<draft>/fonts` và cài vào `~/Library/Fonts` để chọn được trong CapCut. Media được
  liên kết cứng vào `<draft>/media` (CapCut App Store chạy sandbox). Hiệu ứng chuyển động trong clip là ảnh đã dựng —
  sửa chữ trong thẻ/chữ to thì sửa scenes.js → render lại cảnh → chạy lại build_capcut.py (draft bị ghi đè: báo người dùng).
  Bản Mac đọc `draft_info.json` và đường dẫn kiểu `/Users/<tên>/Movies/CapCut/...` — script đã lo (xem gotchas).
  Báo người dùng: **thoát hẳn CapCut rồi mở lại** để thấy dự án; chưa tự mở thử được thì nói rõ là chưa kiểm; nếu clip hiệu ứng hiện nền đen (CapCut không đọc kênh alpha)
  → báo lại để đổi định dạng clip. Đường dẫn khác: tham số thứ 2 = thư mục draft (CapCut → Cài đặt → Vị trí lưu bản nháp).

