---
name: quy-tac-bot-so-nho-thu-ky
description: "Bot Sổ nhớ là thư ký tổng hợp, chạy tiết kiệm token: dùng Sonnet, ít công cụ, luật lõi gọn, thêm dòng mà không đọc file, dọn phiên sau 10 phút; việc điều khiển phiên thuộc bot Điều hành (22/11/2026)"
metadata:
  type: feedback
---

Bot Sổ nhớ chỉ làm **thư ký tổng hợp** cho cuộc sống của David (ghi sổ, lịch, nhắc việc, lời hứa, chuẩn bị buổi gặp, tài chính, thói quen, tin nhắn tổng hợp, soạn bản nháp để David tự gửi). Mọi việc mở / điều khiển phiên Claude thuộc bot Điều hành.
Bot chạy tiết kiệm token: dùng Sonnet, chỉ dùng công cụ cần thiết, luật lõi gọn và hướng dẫn chi tiết chỉ đọc khi cần, thêm dòng bằng `them-dong.sh`, dọn phiên sau 10 phút không hoạt động. Nguồn của luật: `tu-dong-hoa/so-tay/README.md` mục "Tiết kiệm token bot Sổ nhớ".

**Why:** 22/11/2026 23:41 (việc #40) David: "bot Telegram này… rất tốn token… chủ yếu bot Telegram này tôi cho nó hoạt động như một thư ký… phần bot điều khiển các phiên đã tách ra thành một bot khác rồi". David duyệt đề xuất: "phân loại đúng các công năng… để tối ưu tất cả token có thể mà vẫn duy trì được mọi thứ liên quan đến vai trò của một thư ký tổng hợp và nhắc nhở". Kết quả đo: mỗi lượt giảm từ khoảng 93 nghìn xuống còn 13–15 nghìn token.

**How to apply:** khi thêm việc cho bot, Claude viết vào `quy-tac-bot/<việc>.md` (đọc khi cần), không làm luật lõi dài thêm; không cho bot đọc toàn bộ file dài; việc cần phiên Claude thì chuyển sang bot Điều hành hoặc lịch tự chạy. Liên quan [[quy-tac-phien-telegram-tu-chay]].

Gốc: khối 1 (Bóc tách) của tu-duy-goc.md — tách đúng công năng thư ký khỏi công năng điều khiển phiên thì mỗi bot chỉ làm một việc, và đo được số token giảm từ khoảng 93 nghìn còn 13 đến 15 nghìn mỗi lượt.
