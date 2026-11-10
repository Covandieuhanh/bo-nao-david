---
name: video-nhan-dien-chung
description: Mọi loại video cùng một bộ nhận diện (vùng an toàn, dấu góc, thanh thời gian (trừ video dọc ngắn, 10/11), phụ đề, màn chốt, thẻ cuối không logo); chỉ motion graphics tự do theo loại, theo cảnh (2026-11-08)
metadata:
  type: feedback
---

Mọi loại video (1 video người nói, podcast, ghép vlog, highlight; ngang hay dọc) dùng chung một bộ nhận diện: vùng an toàn, dấu góc ● DAVID góc trên trái, **thanh thời gian ở đáy** (video ngang, dọc dài — video dọc ngắn bỏ thanh và thẻ cuối từ 10/11/2026, màn chốt trên hình: [[video-doc-ngan-khong-thanh]]), phụ đề trên thanh, màn chốt, thẻ cuối không nút phát, không logo nền tảng. Chỉ motion graphics là tự do chọn theo loại video, theo từng cảnh.

**Why:** 08/11/2026 David thấy video dài thiếu thanh thời gian, dấu góc lệch; rà ra thì mỗi khuôn dựng tự viết nhận diện riêng nên sửa một chỗ không đổi chỗ khác. David chọn gom về một chỗ và nói "đã nói là cho các loại có những tiêu chuẩn giống nhau mà".

**How to apply:** vị trí chỉ lấy từ `skills/dung-video/thu-vien-hinh/nhan-dien.js` (`khung(W, H)`), thành phần `DauGoc.jsx`, `ThanhThoiGian.jsx`, `EndCardBody.jsx`; bảng ở `thu-vien-hinh/nhan-dien-chung.md`. Không viết số vị trí riêng trong khuôn dựng. Sửa nhận diện → chụp kiểm cả ngang lẫn dọc trên dự án đã duyệt. Liên quan [[luat-hoc-la-bo-sung]], [[video-bo-cuc-tu-can]].
