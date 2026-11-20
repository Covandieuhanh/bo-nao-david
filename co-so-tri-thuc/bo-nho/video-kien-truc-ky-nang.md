---
name: video-kien-truc-ky-nang
description: "Kiến trúc bộ skill video (hồ sơ tham số, 20 khối, thư viện hình, mẫu chuẩn; sửa đúng một chỗ) và bộ 5 video chuẩn 06/11 (04/11, 06/11; gộp 15/11)"
metadata:
  type: project
---

Bộ skill video (`ky-nang/san-xuat-video`, lối tắt `~/.claude/skills/san-xuat-video`) tái cấu trúc 2026-11-04 theo ý David: "tách nhỏ để sau này cải tiến chỉ sửa một phần, không viết lại khung".
5 lớp: `nguyen-tac.md` (7 điểm chung 80 video) · `nhan-dien-thuong-hieu.md` (chọn loại) · `ho-so-thuong-hieu/<loai>.json+.md` (tham số sao chép từ hình mẫu — script đọc qua `ky-nang/san-xuat-video/mo-dun/ho_so.py`, khung dựng đọc `chuyen-dong/src/ho-so.json`) · `mo-dun/00…20` (README luật + đầu vào/ra + phụ thuộc) · `thu-vien-tai-nguyen/` (một bộ thành phần hình, template nối bằng lối tắt `src/thu-vien`, dự án chép bản thật `cp -RL`). 4 skill = công thức mỏng. Kiểm: `ky-nang/san-xuat-video/mau-chuan/kiem-mau.py` (5 mẫu ở `mau.json`, SSIM so chuẩn — (mục gộp dưới)).

Lịch sử đổi giá trị hồ sơ tham số (ngày, cũ → mới, lý do) ở `ky-nang/san-xuat-video/ho-so-thuong-hieu/nhat-ky-thay-doi.md`, không ghi trong file hồ sơ.

**Why:** David sửa skill rất nhiều lần, mỗi lần phải cập nhật lại toàn bộ; đang còn tìm phong cách nên thay đổi là bình thường.
**How to apply:** đổi con số → `ho-so`; đổi cách làm → đúng một khối / `thu-vien-tai-nguyen`; sau mỗi sửa chạy `kiem-mau.py`; không ghi cứng tham số vào code/SKILL. Bố cục tự cân, không còn luật 2 trạng thái ([[video-bo-cuc-tu-can]], 07/11). Thói quen chung mọi skill: `ky-nang/chuan-muc-lam-viec.md`. Liên quan [[quy-tac-noi-dung-cua-david]].

Nhà của luật: `ky-nang/san-xuat-video/tong-quan.md`. Ghi nhớ này giữ ngày, lời David, lý do.

## Gộp từ `video-kien-truc-ky-nang` (15/11/2026, tự học tuần: giảm ghi nhớ về 40)

David chốt 06/11/2026: bản chuẩn gồm đúng 5 video, dựng bằng skill sau khi thêm luật chuyển động. Video ngắn và video dài sau này làm theo các bản này.

- 3 clip: `~/Movies/tap-di-trainer/3-doan-noi-bat/clip-A|B|C`, kế hoạch ở `~/Movies/tap-di-trainer/3-doan-noi-bat`.
- Video dài "Đi trainer cho người làm trainer": `~/Movies/tap-di-trainer/2-ban-day-du`.
- Video dài "Mục tiêu và sứ mệnh": `~/Movies/tap-muc-tieu-su-menh/2-ban-day-du`.

Các dự án cũ (vlog, highlight Haruku, podcast năng lực, Miếu Bà Cam, VF3...) đã chuyển vào Thùng rác cùng ngày; bản xong của Miếu Bà Cam và VF3 còn ở Drive `thanh-pham/vlog/`, chữ bài đăng cũ đã bỏ khỏi repo 07/11/2026 (repo chỉ giữ não), bản sao ở Drive `sao-luu-mac/` (tra [kho-drive.md](../../du-an/kho-drive.md)).

**Why:** David muốn máy chỉ giữ bản mới nhất. Máy còn dưới 5 GB trống trước khi dọn.

**How to apply:** Bộ mẫu `ky-nang/san-xuat-video/mau-chuan/mau.json` nay chỉ có 5 video này, nên không còn kiểm tra tự động cho loại có người nói và ghép vlog. Khi có video mới loại đó được duyệt thì thêm lại. Liên quan [[video-doc-khuon-chu-chinh]], [[video-dai-khong-cat]].
