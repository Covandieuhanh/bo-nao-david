---
description: "Khối 05 tránh che người: lớp phủ không chạm mặt, vùng an toàn."
---

# Khối 05-tranh-che-chu-the: Tránh che người: lớp phủ không chạm mặt + đầu + vai + ngực; không có chỗ → tự toàn màn hình (dài theo nội dung)

**Dùng trong:** làm video, ghép vlog, highlight người nói
**Đầu vào:** kiem-tra/khuon-mat/*.json + canh.js / danh-sach-cat.js
**Đầu ra:** vi-tri.js (1 video) · bao-ve.js (ghép) + kiem-tra/khuon-mat/{placement,guard}.md
**Tham số hồ sơ:** chung: `hai_trang_thai` (false = bố cục tự cân). Không trần giây, không tỷ lệ mặt
**Sửa khối này → chạy lại:** 17 (render lại cảnh đổi chỗ)

**File thật (code, một bản duy nhất):**
- `dung-video-theo-phong-cach/scripts/vi-tri-khuon-mat.sh`
- `dung-video-theo-phong-cach/scripts/vi-tri-khuon-mat.py`
- `dung-video-theo-phong-cach/scripts/bao-ve-lop-phu.py`
- `dung-video-theo-phong-cach/assets/khuon-remotion/src/bo-cuc.js (Place)`

## Luật
- Lớp phủ (không toàn màn hình) **không chạm mặt + đầu + vai + ngực** người nói; chỉ chạm tay / bụng / nền thì được.
- Không có vị trí / cỡ nào tránh được → **tự thành cảnh toàn màn hình** (nền tối + quầng cam, nội dung phóng ra giữa, phụ đề vẫn
  chạy), dài theo nội dung. Muốn vừa thấy người vừa thấy ý → dùng bố cục `bocuc` (`o-nguoi`, `the-canh`) thay vì lớp phủ.
- Lớp phủ (thẻ, chữ to, tên) tự **thu nhỏ còn 78 %** để thấy hình nhiều hơn; mặc định ngay trên dải phụ đề, mặt nằm thấp thì dời lên
  đỉnh vùng an toàn hoặc chỗ trống khác. Component vẫn thiết kế trên dải gốc; `Place` lo vị trí.
- Tít ghim (highlight) che đầu → tự ẩn.
- Giữ lớp phủ cho một cảnh: `place: {full: false}` (1 video) · `keep: true` (OVERLAYS, ghép).
- Lệnh: 1 video `zsh dung-video-theo-phong-cach/scripts/vi-tri-khuon-mat.sh "$P"` sau mỗi lần sửa canh.js; ghép `python3 -I dung-video-theo-phong-cach/scripts/nang-lop.py "$P"`
  rồi `python3 -I dung-video-theo-phong-cach/scripts/bao-ve-lop-phu.py "$P"` sau mỗi lần sửa danh-sach-cat.js. Đọc bảng `kiem-tra/khuon-mat/placement.md` / `guard.md`.
- Bố cục do khối 07 chọn; khối này lo thẻ tít mở (highlight) và các lớp đặt tay `place`.
- Cảnh `nhan` và `bocuc` không qua vi-tri-khuon-mat.py: `vi-tri-nhan.py` (gọi trong vi-tri-khuon-mat.sh) ghi **mọi người** trong khung + **người đang nói** vào `chuyen-dong/src/mat.js`; `src/thu-vien/cho.js` tìm khoảng trống quanh mọi người, nhan.jsx / bo-cuc.jsx đặt graphic sát người đang nói, co theo chỗ, không đè ai. Khung dọc hẹp thì dưới cằm; khung ngang không đặt dưới cằm.
