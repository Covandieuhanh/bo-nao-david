---
name: luat-khong-tu-chay-viec-cua-david
description: "Không tự chạy, chạy tiếp, dừng hay làm lại việc David tạo (render, việc dựng…) khi David chưa ra lệnh — kể cả khi chính Claude làm ngắt việc đó"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 87c9809c-02a8-4c04-96d7-ab8e1a33d71e
  modified: 2026-11-08T14:48:00.687Z
---

Việc do David tự tạo hoặc tự bấm (ví dụ một việc dựng hay render David đang chạy) là của David: Claude không tự bấm Chạy tiếp, Duyệt, Làm lại hay chạy lệnh thay, kể cả khi Claude vừa vô tình làm ngắt việc đó. Chỉ báo tình trạng và chờ lệnh.

**Why:** 08/11/2026 (thời còn app dựng video, đã bỏ 10/11) Claude khởi động lại máy chủ app làm ngắt `mau-1`, rồi tự bấm "Chạy tiếp" để "khôi phục". David: "không chạy nhé, không có lệnh của tôi không được tự làm".

**How to apply:** Việc thử của Claude thì đặt tên riêng (`thu-…`) và chỉ thao tác trên việc đó. Thấy việc của David bị lỗi/ngắt → báo một dòng + hỏi. Trước khi tắt hay chạy lại thứ gì dùng chung (render, tiến trình nền), kiểm có việc nào của David hoặc phiên khác đang chạy không; có thì hỏi trước. Liên quan [[luat-goi-y-de-david-chon]].
