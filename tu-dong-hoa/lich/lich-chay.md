# Lịch việc tự chạy (giờ Mac)

Máy canh bot (`tu-dong-hoa/so-tay/canh-bot.sh`, launchd, luôn chạy) đọc file này mỗi phút. Tới giờ thì chạy `tu-dong-hoa/lich/chay-lich.sh <tên>`:
gọi Claude Code trong Terminal với lời giao ở `loi-giao/<tên>.md`. Không cần mở app Claude, tài khoản Claude nào đang đăng nhập trong Terminal cũng chạy.
Kết quả ghi `~/Documents/2-ca-nhan/so-tay/.trang-thai/lich-<tên>.log`; lỗi thì báo bot.

Dạng dòng giống `nhac-viec.md`: `- mỗi ngày HH:MM · <tên>` · `- mỗi thứ 6 HH:MM · <tên>` · `- chỉ ngày YYYY-MM-DD HH:MM · <tên>` (một lần). Dừng: `(đã dừng) ` ngay sau `· `.

Việc cần trình duyệt của app Claude (tổng hợp tin nhắn) nằm ở `lich-app.json`, máy tự cài vào app theo tài khoản đang mở (`cai-lich-app.py`).

- mỗi ngày 23:00 · gom-phan-loai-dem
- mỗi thứ 6 06:30 · dong-goi-tuan
- chỉ ngày 2026-11-15 06:30 · dong-goi-tuan
