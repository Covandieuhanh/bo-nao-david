---
description: "Lịch việc tự chạy trên Mac: giờ chạy, tên việc, lời giao; máy canh bot đọc mỗi phút."
---

# Lịch việc tự chạy (giờ Mac)

Máy canh bot (`tu-dong-hoa/so-tay/canh-bot.sh`) đọc file này mỗi phút. Tới giờ thì chạy `tu-dong-hoa/lich/chay-lich.sh <tên>`: mở **một phiên Claude Code hiện trong app Claude**
(Remote Control, tên "Lịch · <tên> · dd/mm", có Claude in Chrome), giao lời ở `loi-giao/<tên>.md`. Anh mở app là thấy phiên đang chạy, xem và gõ tiếp được.
Tài khoản nào đang đăng nhập Claude cũng chạy (đổi tài khoản thì máy canh bot mở sẵn Terminal để đăng nhập lại). Không dùng lịch trong app (Scheduled tasks): app chỉ đọc lịch lúc khởi động, lại gắn theo tài khoản.
Phiên lần trước của cùng việc được đóng khi lần mới bắt đầu. Sổ chạy: `~/Documents/2-ca-nhan/so-tay/.trang-thai/canh-bot.log` (dòng `chay lich`).

Dạng dòng giống `nhac-viec.md`: `- mỗi ngày HH:MM · <tên>` · `- mỗi thứ 6 HH:MM · <tên>` · `- chỉ ngày YYYY-MM-DD HH:MM · <tên>` (một lần). Dừng: `(đã dừng) ` ngay sau `· `.

- mỗi ngày 07:00 · tong-hop-tin-nhan
- mỗi ngày 23:00 · gom-phan-loai-dem
- mỗi thứ 6 06:30 · dong-goi-tuan
- chỉ ngày 2026-11-15 06:30 · dong-goi-tuan
