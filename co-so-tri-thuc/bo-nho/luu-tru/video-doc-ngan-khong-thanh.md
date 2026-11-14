---
name: video-doc-ngan-khong-thanh
description: "Video dọc ngắn (Reels/TikTok/Shorts) bỏ thanh thời gian và thẻ cuối; màn chốt hiện chữ trên khung hình, kết ở chữ cuối để tự lặp (2026-11-10)"
metadata:
  type: feedback
---

> Đã gộp vào `video-nhan-dien-chung` ở tái bản 2 (10/11/2026). Bản dưới là lịch sử.

Video dọc ngắn (dọc ≤ 90 s, mọi highlight, podcast dọc trích ngắn): **không thanh thời gian, không thẻ cuối**; màn chốt là ô câu nguyên văn
nằm trên khung hình (không thu nhỏ video). Video ngang và dọc dài giữ thanh, thẻ cuối, màn kết YouTube.

**Why:** David thấy nên bỏ (10/11/2026); Claude phân tích: nền tảng đã có thanh riêng, "còn 0:20" khiến người xem lướt, màn "hết rồi" và thẻ
cuối làm đứt vòng lặp Shorts/Reels. Kênh chưa có số liệu video ngắn — kiểm lại sau 3–4 video (khối 16: tỉ lệ xem hết, giây rời).

**How to apply:** nhà luật `ky-nang/san-xuat-video/quy-tac-chung.md` mục 5; máy tự nhận `nganDoc()` (`thu-vien-tai-nguyen/nhan-dien-thuong-hieu.js`) / `NGAN_DOC`
(`thanh.js`). Dẫn về bản đầy đủ, mời bình luận để ở caption + bình luận ghim. Thay phần "thanh cả clip ngắn" của [[video-nhan-dien-chung]]
và màn hình cuối của [[video-doc-khuon-chu-chinh]].
