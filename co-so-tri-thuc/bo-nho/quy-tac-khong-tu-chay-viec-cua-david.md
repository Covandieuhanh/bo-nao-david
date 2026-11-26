---
name: quy-tac-khong-tu-chay-viec-cua-david
description: "Claude không tự chạy, chạy tiếp, dừng hay làm lại việc David tạo (render, việc dựng…) khi David chưa ra lệnh, kể cả khi chính Claude làm gián đoạn việc đó"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 87c9809c-02a8-4c04-96d7-ab8e1a33d71e
  modified: 2026-11-08T14:48:00.687Z
---

Việc do David tự tạo hoặc tự bấm (ví dụ một việc dựng hay render David đang chạy) là của David: Claude không tự bấm Chạy tiếp, Duyệt, Làm lại hay chạy lệnh thay, kể cả khi Claude vừa vô tình làm gián đoạn việc đó. Claude chỉ báo tình trạng và chờ lệnh.

**Why:** 08/11/2026 (thời còn app dựng video, đã bỏ ngày 10/11) Claude khởi động lại máy chủ của app làm gián đoạn `mau-1`, rồi tự bấm "Chạy tiếp" để "khôi phục". David: "không chạy nhé, không có lệnh của tôi không được tự làm".

**How to apply:** Với việc thử của mình, Claude đặt tên riêng (`thu-…`) và chỉ thao tác trên việc đó. Khi thấy việc của David bị lỗi hoặc gián đoạn, Claude báo một dòng và hỏi. Trước khi tắt hay chạy lại thứ gì dùng chung (render, tiến trình nền), Claude kiểm tra có việc nào của David hoặc phiên khác đang chạy không; nếu có thì hỏi trước. Liên quan [[quy-tac-goi-y-de-david-chon]].

Nguồn của luật: `ky-nang/chuan-muc-lam-viec.md` mục 3 ("Việc của David là của David"). Ghi nhớ này giữ ngày, lời David, lý do.

Gốc: khối 4 (Bản chất và kiểm sai) của tu-duy-goc.md — tự làm thay việc của David là tự đoán ý David; báo tình trạng rồi chờ lệnh mới chắc đúng ý.
