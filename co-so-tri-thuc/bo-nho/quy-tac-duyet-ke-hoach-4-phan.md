---
name: quy-tac-duyet-ke-hoach-4-phan
description: Với mọi việc, Claude trình đủ 4 phần (Mục tiêu · Kế hoạch · Quy trình · Thực thi), David duyệt rồi Claude mới làm; sau khi được duyệt, Claude tự làm trọn tới khi chắc chắn dùng được; việc tự chạy phải hiện thành phiên trong app, không chạy ngầm (14/11/2026)
metadata:
  type: feedback
---

**Mọi việc** (kể cả chỉ gửi video, sửa skill, sửa hệ thống): Claude trình đủ 4 phần **Mục tiêu · Kế hoạch · Quy trình · Thực thi** (danh sách kiểm chia nhỏ nhất) kèm điểm cần chốt có đề xuất đứng đầu, rồi **dừng chờ David "duyệt"**. Khi chưa được duyệt, Claude không tạo hoặc sửa file. Sau khi được duyệt, Claude **tự làm trọn liên tục**, tự chạy thử thật tới khi chắc chắn dùng được, không dừng xin phép giữa chừng. Miễn trừ: câu hỏi nhanh, tra cứu, bot ghi sổ, lịch tự chạy đã duyệt. Việc tự chạy phải hiện thành phiên trong app Claude (Remote Control: `giao-viec.sh`, `tu-dong-hoa/lich/chay-lich.sh`), không dùng `claude -p` chạy ngầm, không dùng Scheduled tasks của app (app chỉ đọc lịch lúc khởi động, lần thử 14/11 22:52 không chạy). David dùng app Claude là chính, chỉ đổi tài khoản Claude khi hết token: mọi thứ phải chạy lại được sau khi đổi tài khoản. Luật ở `ky-nang/chuan-muc-lam-viec.md` mục 2.

**Why:** 14/11/2026 (việc Văn Phòng Shop) Claude viết kế hoạch xong thì dựng ngay: "cần từng bước 1". 14/11 23:xx (việc #22) Claude dừng chờ duyệt rồi chuyển lịch sang chạy ngầm: "làm cái gì cũng cần phải chắc chắn là tự động triển khai hết, chứ không phải chờ để duyệt, phải làm hướng chắc chắn dùng được… đừng làm cái gì ẩn hay chạy nền, cứ chạy trên các phiên hoặc làm cách nào để tôi nhìn thấy và kiểm tra được". Sau đó Claude hiểu nhầm thành "chỉ khi nói làm kế hoạch", David sửa: "4 bước của tôi đều cần phải duyệt khi muốn làm 1 cái gì đó, đầy đủ mục tiêu, kế hoạch, quy trình, thực thi. cứ phải viết đủ hết thì mới thực thi… Luôn phải đủ 4 bước". David duyệt 3 miễn trừ (câu hỏi nhanh, bot ghi sổ, lịch đã duyệt) và việc video cũng phải trình 4 phần.

**How to apply:** kiểu "chờ duyệt" mà David không muốn là dừng giữa chừng sau khi đã duyệt; còn trước khi làm thì Claude luôn trình 4 phần. Phiên Telegram gửi 4 phần qua `bao-cao.sh "#N ❓ Chờ anh duyệt 4 phần: …"`. Liên quan [[quy-tac-phien-telegram-tu-chay]], [[quy-tac-goi-y-de-david-chon]], [[quy-tac-ket-qua-hon-toc-do]].

Gốc: khối 2 (Hành động) của tu-duy-goc.md — Mục tiêu, Kế hoạch, Quy trình, Thực thi chính là vòng hành động gốc; duyệt trước thì sai được sửa trên giấy, không phải sửa trên kết quả.
