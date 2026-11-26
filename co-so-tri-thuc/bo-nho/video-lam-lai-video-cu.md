---
name: video-lam-lai-video-cu
description: Làm lại video cũ của kênh "Cường Kể Chuyện": bỏ lời chào, phần giới thiệu kênh cũ, chữ và viền in sẵn trong hình; mỗi video xuất ra một bản riêng; Claude làm trọn rồi David góp ý sau (2026-11-08)
metadata:
  type: project
---

Ngày 08/11/2026 David đưa 4 video cũ (kênh cũ "Cường Kể Chuyện", 2024) để làm lại theo skill mới. Yêu cầu: Claude tự chọn hướng, làm từ đầu đến cuối mà không hỏi lại, mỗi video render ra một bản riêng (không ghép). David xem kết quả rồi mới góp ý.

Video cũ thường có những thành phần cần bỏ:
- **Lời chào và giới thiệu kênh cũ** ở đầu video: tên kênh cũ, "tài chính cá nhân", CEO, công ty dược mỹ phẩm, chứng khoán, kinh doanh truyền thống. Phần này chạm lằn ranh kinh doanh nên được cắt hoàn toàn.
- **Màn tiêu đề mở đầu cũ**, ví dụ "PODCAST TẬP 4".
- **Chữ hoặc viền in cố định trong hình:** dải chữ ở đáy (tên tập, ngày, Cuongkechuyen.vn) và viền trắng bo góc. Cách xử lý: cắt khung hình rồi phóng to lại.

Lời kết chung không nhắc tên kênh ("hẹn gặp lại các bạn…") thì được giữ lại.

**Why:** kênh hiện tại là "David Trần - Trainer định hướng"; mọi dấu vết của kênh cũ và hướng kinh doanh phải được loại bỏ khỏi video.

**How to apply:** đây là ngoại lệ của luật "video dài không cắt" ([[video-dai-khong-cat]]): Claude chỉ cắt đúng các đoạn kể trên. Cách làm được ghi trong `mo-dun/02-lam-sach` và `ky-nang/san-xuat-video/dung-video-theo-phong-cach/references/loi-thuong-gap.md`. Dự án nằm ở `~/Movies/tap-{thi-lai-dai-hoc, su-tap-trung, cuoc-song-giau-co, dung-mua-thu-ban-thich}`. Liên quan [[video-bo-cuc-tu-can-bang]].

Nguồn của luật: `ky-nang/san-xuat-video/mo-dun/02-lam-sach/README.md` ("Làm lại video cũ"). Ghi nhớ này lưu ngày, lời David và lý do.

Gốc: khối 1 (Bóc tách) của tu-duy-goc.md — video cũ phải bóc ra phần thuộc kênh cũ chạm lằn ranh để bỏ, và giữ phần nội dung còn hợp kênh hiện tại.
