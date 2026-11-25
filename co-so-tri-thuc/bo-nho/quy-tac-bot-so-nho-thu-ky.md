---
name: quy-tac-bot-so-nho-thu-ky
description: "Bot Sổ nhớ là thư ký tổng hợp, chạy tiết kiệm token: Sonnet, ít công cụ, luật lõi gọn, nối dòng không đọc file, dọn phiên sau 10 phút; điều khiển phiên ở bot Điều hành (22/11/2026)"
metadata:
  type: feedback
---

Bot Sổ nhớ chỉ làm **thư ký tổng hợp** đời David (ghi sổ, lịch, nhắc, lời hứa, chuẩn bị gặp, tài chính, thói quen, tin nhắn tổng hợp, soạn nháp để David tự gửi). Mọi việc mở / điều khiển phiên Claude thuộc bot Điều hành.
Chạy tiết kiệm token: Sonnet, chỉ công cụ cần, luật lõi gọn và hướng dẫn chi tiết đọc khi cần, nối dòng bằng `them-dong.sh`, dọn phiên sau 10 phút nghỉ. Nguồn của luật: `tu-dong-hoa/so-tay/README.md` mục "Tiết kiệm token bot Sổ nhớ".

**Why:** 22/11/2026 23:41 (việc #40) David: "bot Telegram này… rất tốn token… chủ yếu bot Telegram này tôi cho nó hoạt động như một thư ký… phần bot điều khiển các phiên đã tách ra thành một bot khác rồi". Duyệt đề xuất: "phân loại đúng các công năng… để tối ưu tất cả token có thể mà vẫn duy trì được mọi thứ liên quan đến vai trò của một thư ký tổng hợp và nhắc nhở". Đo: mỗi lượt từ khoảng 93 nghìn còn 13–15 nghìn token.

**How to apply:** thêm việc cho bot thì viết vào `quy-tac-bot/<việc>.md` (đọc khi cần), không phình luật lõi; không cho bot đọc cả file dài; việc cần phiên Claude thì đưa sang bot Điều hành hoặc lịch tự chạy. Liên quan [[quy-tac-phien-telegram-tu-chay]].
