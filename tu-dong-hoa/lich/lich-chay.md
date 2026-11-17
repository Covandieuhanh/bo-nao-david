---
description: "Lịch việc tự chạy trên Mac: giờ chạy, tên việc, lời giao; máy canh bot đọc mỗi phút."
---

# Lịch việc tự chạy (giờ Mac)

Máy canh bot (`tu-dong-hoa/so-tay/canh-bot.sh`) đọc file này mỗi phút. Tới giờ thì chạy `tu-dong-hoa/lich/chay-lich.sh <tên>`: mở **một phiên Claude Code hiện trong app Claude**
(Remote Control, tên "Lịch · <tên> · dd/mm", có Claude in Chrome), giao lời ở `loi-giao/<tên>.md`. Anh mở app là thấy phiên đang chạy, xem và gõ tiếp được.
Tài khoản nào đang đăng nhập Claude cũng chạy (đổi tài khoản thì máy canh bot mở sẵn Terminal để đăng nhập lại). Không dùng lịch trong app (Scheduled tasks): app chỉ đọc lịch lúc khởi động, lại gắn theo tài khoản.
Phiên lần trước của cùng việc được đóng khi lần mới bắt đầu. Sổ chạy: `~/Documents/2-ca-nhan/so-tay/.trang-thai/canh-bot.log` (dòng `chay lich`).

**Chạy bù khi lỡ giờ** (Mac gập máy ngủ, mất mạng; gặp 15–16/11): đuôi `· bù <N>h` cho việc lỡ còn chạy tới N giờ sau giờ hẹn (tổng hợp tin tới 23:00 cùng ngày, gom đêm tới 12:00 hôm sau, đóng gói tuần 48 giờ). Máy chỉ mở phiên lịch khi **có mạng và Mac đã thức hẳn** (hai vòng kiểm liền nhau), chưa đủ thì chờ, không đánh dấu đã chạy. Phiên chạy bù nhận thêm câu báo giờ gốc để làm cho đúng ngày của lịch. Có mạng lại sau ≥ 10 phút thì máy nhắn David một tin 📶 kể việc đã chạy bù và tin đã gửi lại.

**Khung đầu lời giao** (`loi-giao/<tên>.md`, giữa hai dòng `---`) bịt các chỗ hở (17/11):
- `chrome: bat-buoc` — chỉ mở phiên khi tiện ích Claude in Chrome đã nối (có tiến trình `chrome-native-host`); chưa nối thì mở ngầm Chrome nếu đang tắt, chờ, 10 phút chưa nối thì nhắn David, còn dưới 15 phút hạn bù thì chạy luôn.
- `kiem: <file>` (`{ngay}` = ngày của lịch) — 90 phút sau khi mở phiên, file chưa có, chưa mới, hay còn dòng `CHUA-DOC-DUOC` thì tự chạy lại một lần (cần Chrome thì chờ Chrome nối); lần 2 vẫn chưa được thì nhắn David.
- `nap-gon: co` — phiên không nạp mục lục bộ nhớ và kết nối claude.ai (Claude Docs), đỡ token; chỉ dùng cho việc không cần luật trong bộ nhớ.

Dạng dòng giống `nhac-viec.md`: `- mỗi ngày HH:MM · <tên>` · `- mỗi thứ 6 HH:MM · <tên>` · `- chỉ ngày YYYY-MM-DD HH:MM · <tên>` (một lần). Dừng: `(đã dừng) ` ngay sau `· `.

- mỗi ngày 07:00 · tong-hop-tin-nhan · bù 16h
- mỗi ngày 23:00 · gom-phan-loai-dem · bù 13h
- mỗi thứ 6 06:30 · dong-goi-tuan · bù 48h
- chỉ ngày 2026-11-15 06:30 · dong-goi-tuan
