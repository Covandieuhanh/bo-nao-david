---
name: quy-tac-hoc-la-bo-sung
description: Học video mẫu mới là BỔ SUNG vào skill, không thay thế những gì David đã sửa; lỗi cũ đã sửa không được quay lại; số của khung dọc không dùng cho khung ngang (2026-11-08)
metadata:
  type: feedback
---

Học từ mẫu mới (bố cục, trình bày, âm thanh) chỉ được **thêm** vào skill. Không xoá, không thay những thứ David đã chốt hoặc đã sửa nhiều lần (dấu góc, không đè chữ, thanh thời gian, phụ đề…).

**Why:** 08/11/2026 David xem 4 video cũ làm lại, thấy dấu góc đè hình, điểm nhấn chồng lên dấu góc, thiếu thanh thời gian, dấu góc thấp. David nói "học là bổ sung chứ không phải thay thế đi các thứ trong skill đã xây dựng". Tra lại thì gốc lỗi là template viết cho khung dọc, áp sang khung ngang người nói lần đầu (chi tiết ở `dung-video-theo-phong-cach/references/loi-thuong-gap.md`).

**Từ 10/11/2026:** "bổ sung" giờ gồm cả thẩm mỹ (nền, kết cấu, kiểu hình, chữ nhấn) — chỉ giữ chữ ký nhận diện: [[video-tham-my-chi-giu-nhan-dien]].

**How to apply:**
- Trước khi thêm gì từ bài học: đọc luật và gotchas liên quan, giữ nguyên các chặn cũ, thêm chặn mới cho thành phần mới (ví dụ thành phần mới phải tránh dấu góc, phụ đề, thanh thời gian).
- Khung mới (ngang/dọc) lần đầu chạy: chụp đủ lớp (cảnh + phụ đề + dấu góc + thanh) trước khi render, không chỉ chụp lớp cảnh.
- David gửi video mẫu để học: dùng skill `phan-tich-video-mau` (cửa vào) → quy trình 10 bước ở `ky-nang/san-xuat-video/thiet-ke-bo-cuc/README.md` mục 4: phiếu học David duyệt trước, kiểm không phá sau (David chọn phương án A, 08/11/2026).
- David góp ý mà bảo không render lại: chỉ sửa skill, chụp thử ảnh để kiểm. Liên quan [[video-khong-tu-render]], [[video-bo-cuc-tu-can]].
