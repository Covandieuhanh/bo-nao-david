---
description: "Khối 05 tránh che chủ thể: lớp phủ không chạm mặt người nói, giữ trong vùng an toàn."
---

# Khối 05-tranh-che-chu-the: Tránh che người: lớp phủ không chạm mặt + đầu + vai + ngực; không có chỗ thì đặt vào khoảng trống thật bằng cảnh tự vẽ, không che người

**Dùng trong:** làm video, ghép vlog, highlight người nói
**Đầu vào:** kiem-tra/khuon-mat/*.json + canh.js / danh-sach-cat.js
**Đầu ra:** vi-tri.js (1 video) · bao-ve.js (ghép) + kiem-tra/khuon-mat/{placement,guard}.md
**Tham số hồ sơ:** chung: `hai_trang_thai` (false nghĩa là bố cục tự cân). Không có mức trần số giây, không có tỷ lệ mặt bắt buộc
**Sửa khối này thì chạy lại:** 17 (render lại các cảnh đã đổi vị trí)

**File thật (mã nguồn, một bản duy nhất):**
- `dung-video-theo-phong-cach/scripts/vi-tri-khuon-mat.sh`
- `dung-video-theo-phong-cach/scripts/vi-tri-khuon-mat.py`
- `dung-video-theo-phong-cach/scripts/bao-ve-lop-phu.py`
- `dung-video-theo-phong-cach/assets/mau-remotion/src/bo-cuc.js (Place)`

## Luật
- Lớp phủ (loại không toàn màn hình) **không chạm mặt + đầu + vai + ngực** của người nói; chỉ chạm tay, bụng hoặc nền thì được.
- Không có vị trí hay cỡ nào tránh được thì **không chuyển sang toàn màn hình, không làm mờ người**: người dựng xem ảnh chụp ở đầu, giữa và cuối
  cảnh, tìm khoảng trống thật (trần nhà, cửa kính, tường, khoảng trên đầu) rồi viết cảnh tự vẽ `ve` có vị trí `o` (mẫu: `nhan-tram.jsx`,
  `duong-may.jsx` trong `assets/mau-remotion/src/rieng/`); rút gọn chữ cho vừa chỗ. Chỉ dùng toàn màn hình khi đoạn đó không có người trên hình (`khong_nguoi: true`).
  **Lưu ý mã nguồn hiện tại (24/11/2026):** `vi-tri-khuon-mat.py` (1 video) và `bao-ve-lop-phu.py` (ghép) vẫn TỰ chuyển lớp phủ che mặt sang toàn màn
  hình theo quyết định cũ ngày 04/11; mã nguồn chưa đổi, chờ David quyết định trên Mac chính. Trong lúc chờ, người dựng đọc `placement.md` / `guard.md`, lớp nào báo
  "→ toàn màn hình" thì người dựng đặt lại vào khoảng trống thật như trên rồi chạy lại, không để công cụ tự chuyển. Các khối 06, 07 và bảng khối
  nhắc "tự chuyển toàn màn hình" là đang mô tả mã nguồn này.
- Khung có nhiều người: không dùng `o-nguoi` / `o-tron` (hai kiểu này chỉ giữ người đang nói); `the-canh` hết chỗ sẽ tự thu vào ô nên phải chụp thử.
- Công cụ phát hiện khuôn mặt có thể bỏ sót người cúi đầu hoặc quay nghiêng: luôn kiểm ảnh chụp thử xem lớp phủ có đè lên ai không; bỏ sót thì thêm hộp của người đó vào `mat.js`.
- Lớp phủ (thẻ, chữ to, tên) tự **thu nhỏ còn 78 %** để thấy hình nhiều hơn; vị trí mặc định ngay trên dải phụ đề, mặt nằm thấp thì dời lên
  đỉnh vùng an toàn hoặc khoảng trống khác. Component vẫn được thiết kế trên dải gốc; `Place` đảm nhận vị trí.
- Tít ghim (highlight) che đầu người nói thì tự ẩn.
- Giữ lớp phủ cho một cảnh: `place: {full: false}` (1 video) · `keep: true` (OVERLAYS, ghép).
- Lệnh: với 1 video chạy `zsh dung-video-theo-phong-cach/scripts/vi-tri-khuon-mat.sh "$P"` sau mỗi lần sửa canh.js; với ghép chạy `python3 -I dung-video-theo-phong-cach/scripts/nang-khung.py "$P"`
  rồi `python3 -I dung-video-theo-phong-cach/scripts/bao-ve-lop-phu.py "$P"` sau mỗi lần sửa danh-sach-cat.js. Đọc bảng `kiem-tra/khuon-mat/placement.md` / `guard.md`.
- Bố cục do khối 07 chọn; khối này đảm nhận thẻ tiêu đề mở đầu (highlight) và các lớp được chỉ định thủ công bằng `place`.
- Cảnh `nhan` và `bocuc` không đi qua vi-tri-khuon-mat.py: `vi-tri-nhan.py` (được gọi trong vi-tri-khuon-mat.sh) ghi **mọi người** trong khung + **người đang nói** vào `chuyen-dong/src/mat.js`; `src/thu-vien/cho.js` tìm khoảng trống quanh mọi người, nhan.jsx / bo-cuc.jsx đặt đồ hoạ sát người đang nói, co cỡ theo chỗ trống, không đè lên ai. Khung dọc hẹp thì đặt dưới cằm; khung ngang không đặt dưới cằm.

## Làm mờ vùng riêng tư trên màn hình được quay
Video quay màn hình máy tính hay điện thoại: trước khi dựng, mở vài khung **cỡ lớn** và tìm thứ người ngoài không được đọc: đường link thư mục
Drive hay link chia sẻ riêng, danh sách tên phiên làm việc, tên người, số điện thoại, mật khẩu, token. Có thì làm mờ **đúng vùng đó**
(giữ nguyên lời nói và phần còn lại của màn hình) bằng `dung-video-theo-phong-cach/scripts/lam-mo-vung-rieng.py` (bám màn hình quay cầm tay,
cách khai báo ở đầu script), chạy trên `tu-lieu/video-goc.mp4` sau bước làm sạch. Kiểm bằng ảnh rải mỗi giây và phóng to chỗ máy lia.
Báo cáo và gói đăng ghi rõ đã làm mờ gì, còn gì vẫn đọc được.
