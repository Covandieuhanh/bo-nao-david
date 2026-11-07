# Khối 05-tranh-che-nguoi: Tránh che người: lớp phủ không chạm mặt + đầu + vai + ngực; không có chỗ → tự toàn màn hình ≤ 4 s

**Dùng trong:** làm video, ghép vlog, highlight người nói
**Đầu vào:** check/faces/*.json + scenes.js / edl.js
**Đầu ra:** placement.js (1 video) · guard.js (ghép) + check/faces/{placement,guard}.md
**Tham số hồ sơ:** chung: toan_man_max_s, mat_hien_min, hai_trang_thai
**Sửa khối này → chạy lại:** 17 (render lại cảnh đổi chỗ)

**File thật (code, một bản duy nhất):**
- `video-style-edit/scripts/face_place.sh`
- `video-style-edit/scripts/face_place.py`
- `video-style-edit/scripts/overlay_guard.py`
- `video-style-edit/assets/remotion-template/src/layout.js (Place)`

## Luật
- Lớp phủ (không toàn màn hình) **không chạm mặt + đầu + vai + ngực** người nói; chỉ chạm tay / bụng / nền thì được.
- Không có vị trí / cỡ nào tránh được → **tự thành cảnh toàn màn hình** (nền tối + quầng cam, nội dung phóng ra giữa, phụ đề vẫn
  chạy), dài tối đa `toan_man_max_s` để mặt vẫn hiện ≥ `mat_hien_min`.
- Tít ghim (highlight) che đầu → tự ẩn (David chốt 2026-11-04).
- Giữ lớp phủ cho một cảnh: `place: {full: false}` (1 video) · `keep: true` (OVERLAYS, ghép).
- Lệnh: 1 video `zsh video-style-edit/scripts/face_place.sh "$P"` sau mỗi lần sửa scenes.js; ghép `python3 -I video-style-edit/scripts/lift.py "$P"`
  rồi `python3 -I video-style-edit/scripts/overlay_guard.py "$P"` sau mỗi lần sửa edl.js. Đọc bảng `check/faces/placement.md` / `guard.md`.
- Khi `hai_trang_thai` = true (mặc định): mọi lớp chữ không phải thẻ tít mở đầu / dấu kênh đều vẽ toàn màn hình (khối 07) — khối này
  còn lo phần thẻ tít mở và các lớp đặt tay `place`.
- Cảnh `nhan` (điểm nhấn trên người) không qua face_place.py: `nhan_place.py` (gọi trong face_place.sh) ghi mặt từng cảnh vào `motion/src/mat.js`, Nhan.jsx tự đặt chữ / biểu tượng bên phía trống, khung dọc hẹp thì dưới cằm.
