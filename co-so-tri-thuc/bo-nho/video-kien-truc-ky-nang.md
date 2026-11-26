---
name: video-kien-truc-ky-nang
description: "Kiến trúc bộ skill video (hồ sơ tham số, 20 khối, thư viện hình, mẫu chuẩn; mỗi thay đổi chỉ sửa đúng một chỗ) và bộ 5 video chuẩn 06/11 (04/11, 06/11; gộp 15/11)"
metadata:
  type: project
---

Bộ skill video (`ky-nang/san-xuat-video`, lối tắt `~/.claude/skills/san-xuat-video`) được tái cấu trúc ngày 2026-11-04 theo ý David: "tách nhỏ để sau này cải tiến chỉ sửa một phần, không viết lại khung".
Kiến trúc có 5 lớp: `nguyen-tac.md` (7 điểm chung của 80 video) · `nhan-dien-thuong-hieu.md` (chọn loại) · `ho-so-thuong-hieu/<loai>.json+.md` (tham số sao chép từ hình mẫu; script đọc qua `ky-nang/san-xuat-video/mo-dun/ho_so.py`, khung dựng đọc `chuyen-dong/src/ho-so.json`) · `mo-dun/00…20` (README gồm luật, đầu vào và đầu ra, phụ thuộc) · `thu-vien-tai-nguyen/` (một bộ thành phần hình; mẫu dựng nối bằng lối tắt `src/thu-vien`, dự án chép bản thật bằng `cp -RL`). 4 skill là các công thức mỏng. Công cụ kiểm tra: `ky-nang/san-xuat-video/mau-chuan/kiem-mau.py` (5 mẫu ở `mau.json`, so với chuẩn bằng SSIM; xem mục gộp bên dưới).

Lịch sử thay đổi giá trị hồ sơ tham số (ngày, giá trị cũ thành giá trị mới, lý do) được ghi ở `ky-nang/san-xuat-video/ho-so-thuong-hieu/nhat-ky-thay-doi.md`, không ghi trong file hồ sơ.

**Why:** David sửa skill rất nhiều lần, mỗi lần phải cập nhật lại toàn bộ; David vẫn đang tìm phong cách nên thay đổi là bình thường.
**How to apply:** khi đổi con số, Claude sửa `ho-so`; khi đổi cách làm, Claude sửa đúng một khối hoặc `thu-vien-tai-nguyen`; sau mỗi lần sửa, Claude chạy `kiem-mau.py`; Claude không ghi cố định tham số vào mã nguồn hoặc SKILL. Bố cục tự cân bằng, không còn luật 2 trạng thái ([[video-bo-cuc-tu-can-bang]], 07/11). Thói quen chung của mọi skill: `ky-nang/chuan-muc-lam-viec.md`. Liên quan [[quy-tac-noi-dung-cua-david]].

Nguồn của luật: `ky-nang/san-xuat-video/tong-quan.md`. Ghi nhớ này lưu ngày, lời David và lý do.

## Gộp từ `video-kien-truc-ky-nang` (15/11/2026, vòng tự học hằng tuần: giảm số ghi nhớ xuống 40)

David chốt 06/11/2026: bộ bản chuẩn gồm đúng 5 video, được dựng bằng skill sau khi thêm luật chuyển động. Video ngắn và video dài sau này được làm theo các bản này.

- 3 clip: `~/Movies/tap-di-trainer/3-doan-noi-bat/clip-A|B|C`, kế hoạch nằm ở `~/Movies/tap-di-trainer/3-doan-noi-bat`.
- Video dài "Đi trainer cho người làm trainer": `~/Movies/tap-di-trainer/2-ban-day-du`.
- Video dài "Mục tiêu và sứ mệnh": `~/Movies/tap-muc-tieu-su-menh/2-ban-day-du`.

Các dự án cũ (vlog, highlight Haruku, podcast năng lực, Miếu Bà Cam, VF3...) đã được chuyển vào Thùng rác cùng ngày; bản hoàn thành của Miếu Bà Cam và VF3 vẫn còn ở Drive `thanh-pham/vlog/`; nội dung bài đăng cũ đã bị bỏ khỏi repo ngày 07/11/2026 (repo chỉ lưu bộ não), bản sao nằm ở Drive `sao-luu-mac/` (tra cứu [kho-drive.md](../../du-an/kho-drive.md)).

**Why:** David muốn máy chỉ lưu bản mới nhất. Trước khi dọn dẹp, máy chỉ còn dưới 5 GB dung lượng trống.

**How to apply:** Bộ mẫu `ky-nang/san-xuat-video/mau-chuan/mau.json` hiện chỉ có 5 video này, nên không còn kiểm tra tự động cho loại video có người nói và loại ghép vlog. Khi có video mới thuộc các loại đó được duyệt, Claude thêm lại vào bộ mẫu. Liên quan [[video-doc-mau-chu-chinh]], [[video-dai-khong-cat]].

Gốc: khối 1 (Bóc tách) của tu-duy-goc.md — tách bộ skill thành các khối nhỏ không trùng nên mỗi lần cải tiến chỉ sửa đúng một chỗ, không viết lại khung.
