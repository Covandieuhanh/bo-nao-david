---
name: quy-tac-thu-bang-doan-ngan
description: "Khi thử skill dựng video, Claude chỉ dùng một đoạn ngắn TRỌN VẸN MỘT Ý (không cố định số giây), không chạy toàn bộ video dài"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 87c9809c-02a8-4c04-96d7-ab8e1a33d71e
  modified: 2026-11-09T01:45:31.283Z
---

Khi cần chạy thử một loại video (skill), Claude cắt một đoạn ngắn **trọn vẹn một ý** của video nguồn rồi thử trên đoạn đó;
không cố định 60 hay 90 giây, không chạy toàn bộ video dài. Đoạn ngắn trọn ý cho kết quả tốt thì video dài cũng tốt (vì cùng cách làm).

**Why:** 09/11/2026 việc thử highlight chạy toàn bộ video 14 phút, chiếm thiết bị hàng chục phút; David: "chỉ cần thử ngắn thôi… không nhất thiết
cố định 60 hay 90 giây… thử trọn vẹn một ý là được… làm đoạn ngắn trọn vẹn ý mà ra kết quả tốt thì làm đoạn dài đương nhiên sẽ tốt".

**How to apply:** Claude chọn đoạn từ đầu tới cuối một ý (đọc bản chép lời), cắt bằng ffmpeg vào thư mục thử riêng (`tap-thu-…`), chạy thử ngay
trong phiên Claude theo skill (app đã bỏ 10/11/2026), cho David xem bản cuối, xong thì dọn các file thử. Liên quan
[[quy-tac-khong-tu-chay-viec-cua-david]].

Nguồn của luật: `ky-nang/san-xuat-video/quy-tac-chung.md` mục 8. Ghi nhớ này giữ ngày, lời David, lý do.

Gốc: khối 2 (Hành động) của tu-duy-goc.md — giải bài nhỏ hơn mà trọn một ý là đủ kiểm cách làm; đoạn ngắn ra kết quả tốt thì video dài cùng cách làm cũng tốt.
