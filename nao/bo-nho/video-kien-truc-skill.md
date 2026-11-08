---
name: video-kien-truc-skill
description: Kiến trúc bộ skill video sau tái cấu trúc 2026-11-04 — hồ sơ tham số, 20 khối (00–20, bỏ 18 xuất app dựng 08/11), thư viện hình chung, mẫu chuẩn; sửa đúng một chỗ
metadata:
  type: project
---

Bộ skill video (`~/.claude/skills/dung-video`) tái cấu trúc 2026-11-04 theo ý David: "tách nhỏ để sau này cải tiến chỉ sửa một phần, không viết lại khung".
5 lớp: `nguyen-tac.md` (7 điểm chung 80 video) · `nhan-dien.md` (chọn loại) · `ho-so/<loai>.json+.md` (tham số sao chép từ hình mẫu — script đọc qua `khoi/hoso.py`, khung dựng đọc `motion/src/hoso.json`) · `khoi/00…20` (README luật + đầu vào/ra + phụ thuộc) · `thu-vien-hinh/` (một bộ thành phần hình, template nối bằng lối tắt `src/lib`, dự án chép bản thật `cp -RL`). 4 skill = công thức mỏng. Kiểm: `mau-chuan/kiem-mau.py` (4 dự án mẫu, SSIM so chuẩn).

**Why:** David sửa skill rất nhiều lần, mỗi lần phải cập nhật lại toàn bộ; đang còn tìm phong cách nên thay đổi là bình thường.
**How to apply:** đổi con số → `ho-so`; đổi cách làm → đúng một khối / `thu-vien-hinh`; sau mỗi sửa chạy `kiem-mau.py`; không ghi cứng tham số vào code/SKILL. Bố cục tự cân, không còn luật 2 trạng thái ([[video-bo-cuc-tu-can]], 07/11). Thói quen chung mọi skill: `skills/thoi-quen-lam-viec.md`. Liên quan [[video-nguoi-xem-trung-tam]].
