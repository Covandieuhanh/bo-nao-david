---
name: video-nhac-theo-tuyen
description: Claude TỰ chọn nhạc theo tuyến nội dung từ kho nhạc của kênh (không hỏi David), cân chỉnh mức âm lượng từng bài; chuẩn âm thanh chung cho mọi video — nhạc ~23 dB dưới giọng, cả bài −14 LUFS (2026-11-05, 06/11, 08/11, gộp 10/11)
metadata:
  type: feedback
---

**Chọn nhạc:** với mỗi video, Claude chọn nhạc theo tuyến nội dung (vui / tâm sự / mất mát / ý nghĩa / kiến thức / du lịch / khám phá / ngắm cảnh, theo
bảng ở hồ sơ chung `nhac`), ghi `project.tuyen` và lý do; không có mặc định. Claude dùng bài trong kho nhạc của kênh, tự chọn, không hỏi David
và không cảnh báo "nhạc nghe điện tử". Với bài mới David tải về `~/Music/nhac-nen`, Claude đưa vào kho theo tuyến, đo mức âm lượng và ghi `nhac.muc` (khối 09).
Claude luôn cân chỉnh mức âm lượng từng bài.

**Chuẩn âm lượng chung** (06/11/2026, lấy từ 3 clip "Đi trainer"): ở mọi video đầu ra, nhạc thấp hơn giọng khoảng 23 dB khi đang có lời nói, cả bài
đạt −14 LUFS. Giọng thu nhỏ thì tăng lên, nhạc to thì hạ xuống. Claude không đặt mức riêng theo loại video.

**Why:**
- Ngày 05/11/2026, podcast tâm sự "Mục tiêu và sứ mệnh" bị gắn bài Upbeat Vlog mặc định, nhạc chỉ thấp hơn giọng 17 LU; David nhận xét: "nhạc to… tông
  chưa phù hợp… phải tự chọn được nhạc theo tuyến nội dung".
- Ngày 06/11/2026 David nghe thấy nhạc của video dài nhỏ hơn 3 clip vì mỗi loại video dùng một mức riêng, nên chuyển sang một chuẩn chung (thay câu cũ "rất nhỏ khi
  nói", "nhẹ 1 xíu, tắt hẳn cũng được").
- Ngày 08/11/2026, ở vlog The View Vũng Tàu, Claude chỉ dùng 6 bài cũ, quên cân chỉnh mức âm lượng (nhạc to gấp đôi), lại còn hỏi "nhạc có thể nghe điện tử". David:
  "đã tải rất nhiều nhạc để phù hợp với từng nội dung… sao không tự đánh giá để tự ghép nhạc phù hợp". Claude đã thêm các tuyến du_lich, kham_pha,
  ngam_canh.
- Ghi nhớ `video-chuan-am-luong` được gộp vào đây ở lần tái bản 2 (10/11/2026).

**How to apply:** Claude đọc lời nói, chọn tuyến rồi ghi project.tuyen kèm lý do. Mức âm lượng nằm ở `ky-nang/san-xuat-video/ho-so-thuong-hieu/chung.json` mục `nhac`, cách làm nằm ở khối 09,
`chuan-am.py` tự chạy khi xuất video. Tuyến kiến thức còn chờ David tải 1 bài ambient/lo-fi (đã ghi ở `chung.json`). Liên quan
[[video-kien-truc-ky-nang]], [[video-doc-mau-chu-chinh]].

Gốc: khối 1 (Bóc tách) của tu-duy-goc.md — nhạc và mọi phần dựng chọn theo nội dung của chính video, tuyến chỉ là gợi ý mặc định; cùng một chuẩn âm lượng đo được cho mọi video.
