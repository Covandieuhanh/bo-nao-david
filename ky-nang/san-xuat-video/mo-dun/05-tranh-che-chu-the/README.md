---
description: "Khối 05 tránh che người: lớp phủ không chạm mặt, vùng an toàn."
---

# Khối 05-tranh-che-chu-the: Tránh che người: lớp phủ không chạm mặt + đầu + vai + ngực; không có chỗ thì đặt vào chỗ trống thật bằng cảnh tự vẽ, không che người

**Dùng trong:** làm video, ghép vlog, highlight người nói
**Đầu vào:** kiem-tra/khuon-mat/*.json + canh.js / danh-sach-cat.js
**Đầu ra:** vi-tri.js (1 video) · bao-ve.js (ghép) + kiem-tra/khuon-mat/{placement,guard}.md
**Tham số hồ sơ:** chung: `hai_trang_thai` (false = bố cục tự cân). Không trần giây, không tỷ lệ mặt
**Sửa khối này thì chạy lại:** 17 (render lại cảnh đổi chỗ)

**File thật (code, một bản duy nhất):**
- `dung-video-theo-phong-cach/scripts/vi-tri-khuon-mat.sh`
- `dung-video-theo-phong-cach/scripts/vi-tri-khuon-mat.py`
- `dung-video-theo-phong-cach/scripts/bao-ve-lop-phu.py`
- `dung-video-theo-phong-cach/assets/khuon-remotion/src/bo-cuc.js (Place)`

## Luật
- Lớp phủ (không toàn màn hình) **không chạm mặt + đầu + vai + ngực** người nói; chỉ chạm tay / bụng / nền thì được.
- Không có vị trí / cỡ nào tránh được thì **không chuyển sang toàn màn hình, không làm mờ người**: người dựng xem ảnh đầu / giữa / cuối
  cảnh, tìm chỗ trống thật (trần, cửa kính, tường, khoảng trên đầu) rồi viết cảnh tự vẽ `ve` có vị trí `o` (mẫu: `nhan-tram.jsx`,
  `duong-may.jsx` trong `assets/khuon-remotion/src/rieng/`); rút chữ cho vừa chỗ. Toàn màn hình chỉ khi đoạn đó không có người trên hình (`khong_nguoi: true`).
- Khung nhiều người: không dùng `o-nguoi` / `o-tron` (chỉ giữ người đang nói); `the-canh` hết chỗ sẽ tự thu vào ô nên phải chụp thử.
- Máy dò mặt có thể bỏ sót người cúi đầu, quay nghiêng: luôn soi ảnh chụp thử xem có đè ai không; sót thì thêm hộp người đó vào `mat.js`.
- Lớp phủ (thẻ, chữ to, tên) tự **thu nhỏ còn 78 %** để thấy hình nhiều hơn; mặc định ngay trên dải phụ đề, mặt nằm thấp thì dời lên
  đỉnh vùng an toàn hoặc chỗ trống khác. Component vẫn thiết kế trên dải gốc; `Place` lo vị trí.
- Tít ghim (highlight) che đầu thì tự ẩn.
- Giữ lớp phủ cho một cảnh: `place: {full: false}` (1 video) · `keep: true` (OVERLAYS, ghép).
- Lệnh: 1 video `zsh dung-video-theo-phong-cach/scripts/vi-tri-khuon-mat.sh "$P"` sau mỗi lần sửa canh.js; ghép `python3 -I dung-video-theo-phong-cach/scripts/nang-lop.py "$P"`
  rồi `python3 -I dung-video-theo-phong-cach/scripts/bao-ve-lop-phu.py "$P"` sau mỗi lần sửa danh-sach-cat.js. Đọc bảng `kiem-tra/khuon-mat/placement.md` / `guard.md`.
- Bố cục do khối 07 chọn; khối này lo thẻ tít mở (highlight) và các lớp đặt tay `place`.
- Cảnh `nhan` và `bocuc` không qua vi-tri-khuon-mat.py: `vi-tri-nhan.py` (gọi trong vi-tri-khuon-mat.sh) ghi **mọi người** trong khung + **người đang nói** vào `chuyen-dong/src/mat.js`; `src/thu-vien/cho.js` tìm khoảng trống quanh mọi người, nhan.jsx / bo-cuc.jsx đặt graphic sát người đang nói, co theo chỗ, không đè ai. Khung dọc hẹp thì dưới cằm; khung ngang không đặt dưới cằm.
