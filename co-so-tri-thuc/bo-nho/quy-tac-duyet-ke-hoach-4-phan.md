---
name: quy-tac-duyet-ke-hoach-4-phan
description: "Việc đã có quy trình thì tự động hoàn toàn, cần đổi thì sửa quy trình, không xin duyệt (26/11/2026); việc chưa có quy trình thì trình đủ 4 phần (Mục tiêu · Kế hoạch · Quy trình · Thực thi), David duyệt rồi mới làm, làm trọn rồi viết thành quy trình; việc tự chạy hiện thành phiên trong app, không chạy ngầm (14/11/2026)"
metadata:
  type: feedback
---

**Từ 26/11/2026:** việc đã có quy trình (một lá trong `quy-trinh.md`, kể cả gửi video, vòng tự học, nâng cấp) thì Claude tự làm trọn, không trình 4 phần, không dừng chờ duyệt; cần đổi thì sửa chính quy trình, ghi nhật ký, làm tiếp, báo sau. Đoạn dưới (14/11) nay chỉ áp cho **việc chưa có quy trình**.

**Việc chưa có quy trình** (14/11/2026): Claude trình đủ 4 phần **Mục tiêu · Kế hoạch · Quy trình · Thực thi** (danh sách kiểm chia nhỏ nhất) kèm điểm cần chốt có đề xuất đứng đầu, rồi **dừng chờ David "duyệt"**. Khi chưa được duyệt, Claude không tạo hoặc sửa file. Sau khi được duyệt, Claude **tự làm trọn liên tục**, tự chạy thử thật tới khi chắc chắn dùng được, không dừng xin phép giữa chừng. Miễn trừ: câu hỏi nhanh, tra cứu, bot ghi sổ, lịch tự chạy đã duyệt. Việc tự chạy phải hiện thành phiên trong app Claude (Remote Control: `giao-viec.sh`, `tu-dong-hoa/lich/chay-lich.sh`), không dùng `claude -p` chạy ngầm, không dùng Scheduled tasks của app (app chỉ đọc lịch lúc khởi động, lần thử 14/11 22:52 không chạy). David dùng app Claude là chính, chỉ đổi tài khoản Claude khi hết token: mọi thứ phải chạy lại được sau khi đổi tài khoản. Luật ở `ky-nang/chuan-muc-lam-viec.md` mục 2.

**Why:** 14/11/2026 (việc Văn Phòng Shop) Claude viết kế hoạch xong thì dựng ngay: "cần từng bước 1". 14/11 23:xx (việc #22) Claude dừng chờ duyệt rồi chuyển lịch sang chạy ngầm: "làm cái gì cũng cần phải chắc chắn là tự động triển khai hết, chứ không phải chờ để duyệt, phải làm hướng chắc chắn dùng được… đừng làm cái gì ẩn hay chạy nền, cứ chạy trên các phiên hoặc làm cách nào để tôi nhìn thấy và kiểm tra được". Sau đó Claude hiểu nhầm thành "chỉ khi nói làm kế hoạch", David sửa: "4 bước của tôi đều cần phải duyệt khi muốn làm 1 cái gì đó, đầy đủ mục tiêu, kế hoạch, quy trình, thực thi. cứ phải viết đủ hết thì mới thực thi… Luôn phải đủ 4 bước". David duyệt 3 miễn trừ (câu hỏi nhanh, bot ghi sổ, lịch đã duyệt) và việc video cũng phải trình 4 phần.

**Why (26/11/2026):** trong một tuần David nhắc khoảng 7 lần "tự động, không cần hỏi lại"; sau vòng tuần, David chốt: "quy trình nâng cấp và tất cả mọi thứ tôi làm ra quy trình là để tự động hoàn thành và nếu cần thì chỉ có sửa quy trình chứ không phải cứ phải duyệt, khi đã có quy trình rồi thì cần phải tự động hoàn toàn. gốc có rồi thì quy trình là thứ giúp tối ưu mọi lúc mà".

**How to apply:** có lá thì tự động hoàn toàn; chưa có lá thì trình 4 phần trước, duyệt rồi không dừng giữa chừng, xong viết thành lá. Luôn giữ Đ2 (bấm đăng thật, gửi, xoá, tài khoản), Đ3 (thông tin về David), đổi nghĩa tầng 0. Phiên Telegram gửi 4 phần qua `bao-cao.sh "#N ❓ Chờ anh duyệt 4 phần: …"`. Liên quan [[quy-tac-phien-telegram-tu-chay]], [[quy-tac-goi-y-de-david-chon]], [[quy-tac-ket-qua-hon-toc-do]].

Gốc: khối 2 (Hành động) của tu-duy-goc.md — Mục tiêu, Kế hoạch, Quy trình, Thực thi chính là vòng hành động gốc; duyệt trước thì sai được sửa trên giấy, không phải sửa trên kết quả.
