---
name: quy-tac-thu-bang-doan-ngan
description: "Thử skill dựng video thì chỉ dùng một đoạn ngắn TRỌN VẸN MỘT Ý (không cố định số giây), không chạy cả video dài"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 87c9809c-02a8-4c04-96d7-ab8e1a33d71e
  modified: 2026-11-09T01:45:31.283Z
---

Khi cần chạy thử một loại video (skill), cắt một đoạn ngắn **trọn vẹn một ý** của video nguồn rồi thử trên đoạn đó —
không cố định 60 hay 90 giây, không chạy cả video dài. Đoạn ngắn trọn ý ra kết quả tốt thì video dài cũng tốt (cùng cách làm).

**Why:** 09/11/2026 việc thử highlight chạy cả video 14 phút, chiếm máy hàng chục phút; David: "chỉ cần thử ngắn thôi… không nhất thiết
cố định 60 hay 90 giây… thử trọn vẹn một ý là được… làm đoạn ngắn trọn vẹn ý mà ra kết quả tốt thì làm đoạn dài đương nhiên sẽ tốt".

**How to apply:** chọn đoạn từ đầu tới cuối một ý (đọc bản lời), cắt bằng ffmpeg vào thư mục thử riêng (`tap-thu-…`), chạy thử ngay
trong phiên Claude theo skill (app đã bỏ 10/11/2026), cho David xem bản cuối, xong thì dọn đồ thử. Liên quan
[[quy-tac-khong-tu-chay-viec-cua-david]].

Nguồn của luật: `ky-nang/san-xuat-video/quy-tac-chung.md` mục 8. Ghi nhớ này giữ ngày, lời David, lý do.
