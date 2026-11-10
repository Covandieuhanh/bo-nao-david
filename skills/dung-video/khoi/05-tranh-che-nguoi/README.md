# Khối 05-tranh-che-nguoi: Tránh che người: lớp phủ không chạm mặt + đầu + vai + ngực; không có chỗ → tự toàn màn hình (dài theo nội dung)

**Dùng trong:** làm video, ghép vlog, highlight người nói
**Đầu vào:** check/faces/*.json + scenes.js / edl.js
**Đầu ra:** placement.js (1 video) · guard.js (ghép) + check/faces/{placement,guard}.md
**Tham số hồ sơ:** chung: `hai_trang_thai` (false = bố cục tự cân). Không trần giây, không tỷ lệ mặt
**Sửa khối này → chạy lại:** 17 (render lại cảnh đổi chỗ)

**File thật (code, một bản duy nhất):**
- `video-style-edit/scripts/face_place.sh`
- `video-style-edit/scripts/face_place.py`
- `video-style-edit/scripts/overlay_guard.py`
- `video-style-edit/assets/remotion-template/src/layout.js (Place)`

## Luật
- Lớp phủ (không toàn màn hình) **không chạm mặt + đầu + vai + ngực** người nói; chỉ chạm tay / bụng / nền thì được.
- Không có vị trí / cỡ nào tránh được → **tự thành cảnh toàn màn hình** (nền tối + quầng cam, nội dung phóng ra giữa, phụ đề vẫn
  chạy), dài theo nội dung. Muốn vừa thấy người vừa thấy ý → dùng bố cục `bocuc` (`o-nguoi`, `the-canh`) thay vì lớp phủ.
- Lớp phủ (thẻ, chữ to, tên) tự **thu nhỏ còn 78 %** để thấy hình nhiều hơn; mặc định ngay trên dải phụ đề, mặt nằm thấp thì dời lên
  đỉnh vùng an toàn hoặc chỗ trống khác. Component vẫn thiết kế trên dải gốc; `Place` lo vị trí.
- Tít ghim (highlight) che đầu → tự ẩn.
- Giữ lớp phủ cho một cảnh: `place: {full: false}` (1 video) · `keep: true` (OVERLAYS, ghép).
- Lệnh: 1 video `zsh video-style-edit/scripts/face_place.sh "$P"` sau mỗi lần sửa scenes.js; ghép `python3 -I video-style-edit/scripts/lift.py "$P"`
  rồi `python3 -I video-style-edit/scripts/overlay_guard.py "$P"` sau mỗi lần sửa edl.js. Đọc bảng `check/faces/placement.md` / `guard.md`.
- Bố cục do khối 07 chọn; khối này lo thẻ tít mở (highlight) và các lớp đặt tay `place`.
- Cảnh `nhan` và `bocuc` không qua face_place.py: `nhan_place.py` (gọi trong face_place.sh) ghi **mọi người** trong khung + **người đang nói** vào `motion/src/mat.js`; `src/lib/cho.js` tìm khoảng trống quanh mọi người, Nhan.jsx / BoCuc.jsx đặt graphic sát người đang nói, co theo chỗ, không đè ai. Khung dọc hẹp thì dưới cằm; khung ngang không đặt dưới cằm.
