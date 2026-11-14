---
name: video-kien-truc-skill
description: Kiến trúc bộ skill video sau tái cấu trúc 2026-11-04 — hồ sơ tham số, 20 khối (00–17, 19, 20; khối 18 xuất app dựng đã bỏ 08/11), thư viện hình chung, mẫu chuẩn; sửa đúng một chỗ
metadata:
  type: project
---

Bộ skill video (`~/.claude/skills/san-xuat-video`) tái cấu trúc 2026-11-04 theo ý David: "tách nhỏ để sau này cải tiến chỉ sửa một phần, không viết lại khung".
5 lớp: `nguyen-tac.md` (7 điểm chung 80 video) · `nhan-dien-thuong-hieu.md` (chọn loại) · `ho-so-thuong-hieu/<loai>.json+.md` (tham số sao chép từ hình mẫu — script đọc qua `mo-dun/ho_so.py`, khung dựng đọc `chuyen-dong/src/ho-so.json`) · `mo-dun/00…20` (README luật + đầu vào/ra + phụ thuộc) · `thu-vien-tai-nguyen/` (một bộ thành phần hình, template nối bằng lối tắt `src/thu-vien`, dự án chép bản thật `cp -RL`). 4 skill = công thức mỏng. Kiểm: `mau-chuan/kiem-mau.py` (5 mẫu ở `mau.json`, SSIM so chuẩn — [[video-ban-chuan-2026-11-06]]).

**Why:** David sửa skill rất nhiều lần, mỗi lần phải cập nhật lại toàn bộ; đang còn tìm phong cách nên thay đổi là bình thường.
**How to apply:** đổi con số → `ho-so`; đổi cách làm → đúng một khối / `thu-vien-tai-nguyen`; sau mỗi sửa chạy `kiem-mau.py`; không ghi cứng tham số vào code/SKILL. Bố cục tự cân, không còn luật 2 trạng thái ([[video-bo-cuc-tu-can]], 07/11). Thói quen chung mọi skill: `ky-nang/chuan-muc-lam-viec.md`. Liên quan [[quy-tac-noi-dung-cua-david]].
