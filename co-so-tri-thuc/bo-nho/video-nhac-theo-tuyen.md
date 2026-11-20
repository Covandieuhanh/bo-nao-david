---
name: video-nhac-theo-tuyen
description: Claude TỰ chọn nhạc theo tuyến nội dung từ kho nhạc kênh (không hỏi David), cân mức từng bài; chuẩn âm chung mọi video — nhạc ~23 dB dưới giọng, cả bài −14 LUFS (2026-11-05, 06/11, 08/11, gộp 10/11)
metadata:
  type: feedback
---

**Chọn nhạc:** mỗi video chọn nhạc theo tuyến nội dung (vui / tâm sự / mất mát / ý nghĩa / kiến thức / du lịch / khám phá / ngắm cảnh →
bảng ở hồ sơ chung `nhac`), ghi `project.tuyen` + lý do; không có mặc định. Dùng bài trong kho nhạc kênh, Claude tự chọn, không hỏi David
và không cảnh báo "nhạc nghe điện tử". Bài mới David tải ở `~/Music/nhac-nen` → đưa vào kho theo tuyến, đo mức, ghi `nhac.muc` (khối 09).
Luôn cân mức từng bài.

**Chuẩn âm lượng chung** (06/11/2026, lấy từ 3 clip "Đi trainer"): mọi đầu ra video nhạc thấp hơn giọng khoảng 23 dB lúc đang nói, cả bài
−14 LUFS. Giọng thu nhỏ thì kéo lên, nhạc to thì hạ xuống. Không đặt mức riêng theo loại video.

**Why:**
- 05/11/2026 podcast tâm sự "Mục tiêu và sứ mệnh" bị gắn bài Upbeat Vlog mặc định, nhạc chỉ thấp hơn giọng 17 LU → David: "nhạc to… tông
  chưa phù hợp… phải tự chọn được nhạc theo tuyến nội dung".
- 06/11/2026 David nghe video dài nhỏ nhạc hơn 3 clip vì mỗi loại video dùng một mức riêng → một chuẩn chung (thay câu cũ "rất nhỏ khi
  nói", "nhẹ 1 xíu, tắt hẳn cũng được").
- 08/11/2026 vlog The View Vũng Tàu: Claude chỉ dùng 6 bài cũ, quên cân mức (nhạc to gấp đôi), lại hỏi "nhạc có thể nghe điện tử". David:
  "đã tải rất nhiều nhạc để phù hợp với từng nội dung… sao không tự đánh giá để tự ghép nhạc phù hợp". Đã thêm tuyến du_lich, kham_pha,
  ngam_canh.
- Gộp ghi nhớ `video-chuan-am-luong` vào đây ở tái bản 2 (10/11/2026).

**How to apply:** đọc lời → chọn tuyến → ghi project.tuyen + lý do. Mức ở `ky-nang/san-xuat-video/ho-so-thuong-hieu/chung.json` mục `nhac`, cách làm ở khối 09,
`chuan-am.py` tự chạy khi xuất. Tuyến kiến thức còn chờ David tải 1 bài ambient/lo-fi (ghi ở `chung.json`). Liên quan
[[video-kien-truc-ky-nang]], [[video-doc-khuon-chu-chinh]].
