---
description: "Khối 11 dựng ghép nhiều clip: hiểu clip, giữ / bỏ, bản đồ cảnh."
---

# Khối 11-dung-ghep: Ghép cảnh từ nhiều clip: hiểu clip, giữ/bỏ, bản đồ liên kết, khung vlog, danh-sach-cat.js

**Dùng trong:** ghép vlog nhiều cảnh khác nhau, highlight người nói (clip ngắn). **Không dùng** cho bản dài người nói ghép từ nhiều file của cùng buổi: nối file rồi dựng khuôn 1 video (đủ kho bố cục, bảng ghi chú, chương — `thiet-ke-bo-cuc/tu-chon.md` bước 0).
**Bắt buộc trước kịch bản:** `chan-doan.py <dự án>` + `ke-hoach-canh.md` mục Chẩn đoán (render bị chặn nếu thiếu).
**Đầu vào:** nhiều clip
**Đầu ra:** danh-sach-cat.js / ke-hoach.json + ke-hoach-ghep.md + lien-ket.jpg
**Tham số hồ sơ:** ghep-vlog: *
**Sửa khối này thì chạy lại:** 04 (nang-lop.py), 05 (bao-ve-lop-phu.py), 17

**File thật (code, một bản duy nhất):**
- `dung-video-theo-phong-cach/references/nhieu-doan-video.md (chi tiết)`
- `dung-video-theo-phong-cach/scripts/{tao-dung-ghep.sh,danh-sach-cat-vlog.py,khung-loi.py,bang-lien-ket.py}`
- `dung-video-theo-phong-cach/assets/khuon-dung-ghep/`
