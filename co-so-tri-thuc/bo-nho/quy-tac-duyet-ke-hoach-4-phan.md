---
name: quy-tac-duyet-ke-hoach-4-phan
description: Việc gì cũng trình đủ 4 phần (Mục tiêu · Kế hoạch · Quy trình · Thực thi), David duyệt rồi mới làm; duyệt rồi tự làm trọn tới khi chắc dùng được; việc tự chạy hiện thành phiên trong app, không chạy ngầm (14/11/2026)
metadata:
  type: feedback
---

**Mọi việc** (kể cả chỉ gửi video, sửa skill, sửa hệ thống): trình đủ 4 phần **Mục tiêu · Kế hoạch · Quy trình · Thực thi** (checklist nhỏ nhất) kèm điểm cần chốt có đề xuất đứng đầu, rồi **dừng chờ David "duyệt"**. Chưa duyệt thì không tạo/sửa file. Duyệt rồi **tự làm trọn một mạch**, tự thử thật tới khi chắc dùng được, không dừng xin phép giữa chừng. Miễn: câu hỏi nhanh, tra cứu, bot ghi sổ, lịch tự chạy đã duyệt. Việc tự chạy phải hiện thành phiên trong app Claude (Remote Control: `giao-viec.sh`, `tu-dong-hoa/lich/chay-lich.sh`), không `claude -p` chạy ngầm, không dùng Scheduled tasks của app (app chỉ đọc lịch lúc khởi động, thử 14/11 22:52 không chạy). David dùng app Claude là chính, chỉ đổi tài khoản Claude khi hết token: mọi thứ phải chạy lại được sau khi đổi tài khoản. Luật ở `ky-nang/chuan-muc-lam-viec.md` mục 2.

**Why:** 14/11/2026 (việc Văn Phòng Shop) Claude viết kế hoạch xong dựng luôn: "cần từng bước 1". 14/11 23:xx (việc #22) Claude dừng chờ duyệt rồi đưa lịch sang chạy ngầm: "làm cái gì cũng cần phải chắc chắn là tự động triển khai hết, chứ không phải chờ để duyệt, phải làm hướng chắc chắn dùng được… đừng làm cái gì ẩn hay chạy nền, cứ chạy trên các phiên hoặc làm cách nào để tôi nhìn thấy và kiểm tra được". Rồi Claude hiểu thành "chỉ khi nói làm kế hoạch", David sửa: "4 bước của tôi đều cần phải duyệt khi muốn làm 1 cái gì đó, đầy đủ mục tiêu, kế hoạch, quy trình, thực thi. cứ phải viết đủ hết thì mới thực thi… Luôn phải đủ 4 bước". David duyệt 3 miễn trừ (câu hỏi nhanh, bot ghi sổ, lịch đã duyệt) và video cũng trình 4 phần.

**How to apply:** "chờ duyệt" David ghét là dừng giữa chừng sau khi đã duyệt; còn trước khi làm thì luôn trình 4 phần. Phiên Telegram gửi 4 phần qua `bao-cao.sh "#N ❓ Chờ anh duyệt 4 phần: …"`. Liên quan [[quy-tac-phien-telegram-tu-chay]], [[quy-tac-goi-y-de-david-chon]], [[quy-tac-ket-qua-hon-toc-do]].
