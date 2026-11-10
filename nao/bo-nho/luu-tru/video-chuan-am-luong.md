---
name: video-chuan-am-luong
description: Chuẩn âm lượng chung David chốt cho mọi video: nhạc thấp hơn giọng khoảng 23 dB lúc nói, cả bài -14 LUFS; giọng nhỏ kéo lên, nhạc to hạ xuống (2026-11-06)
metadata:
  type: feedback
---

> Đã gộp vào `video-nhac-theo-tuyen` ở tái bản 2 (10/11/2026). Bản dưới là lịch sử.

Mọi đầu ra video dùng một chuẩn âm lượng, lấy từ 3 clip "Đi trainer": nhạc thấp hơn giọng khoảng 23 dB lúc đang nói, cả bài -14 LUFS. Giọng thu nhỏ thì kéo lên, nhạc to thì hạ xuống.

**Why:** David nghe video dài nhỏ nhạc hơn 3 clip vì mỗi loại video dùng một mức riêng.

**How to apply:** Mức nằm ở `ho-so/chung.json` mục `nhac`, cách làm ở khối 09, `chuan_am.py` tự chạy khi xuất. Không đặt mức riêng theo loại video. Thay luật "rất nhỏ khi nói" trong [[video-nhac-theo-tuyen]]. Liên quan [[video-doc-khuon-chu-chinh]].
