---
name: video-nhac-theo-tuyen
description: Claude TỰ chọn nhạc theo tuyến nội dung từ kho nhạc kênh (không hỏi David); mức cân từng bài một nguồn ở chung.json nhac.muc; ~23 dB dưới giọng
metadata:
  node_type: memory
  type: feedback
  originSessionId: d6267332-097f-4c05-989b-af19b70dff05
  modified: 2026-11-05T02:31:03.858Z
---

Mỗi video phải chọn nhạc theo tuyến nội dung (vui / tâm sự / mất mát / ý nghĩa / kiến thức → bảng ở hồ sơ chung `nhac`), ghi `project.tuyen`; không có mặc định. Mức nhạc theo [[video-chuan-am-luong]]: thấp hơn giọng khoảng 23 dB lúc nói (sửa 08/11, thay câu cũ "nhẹ 1 xíu, tắt hẳn cũng được"). Dùng bài trong kho nhạc kênh, Claude tự chọn, không hỏi David và không cảnh báo "nhạc nghe điện tử". Bài mới David tải ở `~/Music/nhac-nen` → đưa vào kho theo tuyến, đo mức, ghi `nhac.muc` (khối 09). Luôn cân mức từng bài.

**Why:** 2026-11-05 podcast tâm sự "Mục tiêu và sứ mệnh" bị gắn bài Upbeat Vlog mặc định, nhạc chỉ thấp hơn giọng 17 LU → David: "nhạc to… tông chưa phù hợp… phải tự chọn được nhạc theo tuyến nội dung".

**Bổ sung 08/11/2026:** vlog The View Vũng Tàu — Claude chỉ dùng 6 bài cũ, quên cân mức (nhạc to gấp đôi), lại hỏi David "nhạc có thể nghe điện tử". David: "đã tải rất nhiều nhạc để phù hợp với từng nội dung… sao không tự đánh giá để tự ghép nhạc phù hợp". Đã thêm tuyến du_lich, kham_pha, ngam_canh.

**How to apply:** đọc lời → chọn tuyến → ghi project.tuyen + lý do. Tuyến kiến thức còn chờ David tải 1 bài ambient/lo-fi từ Pixabay. Liên quan [[video-kien-truc-skill]] (khối 09).
