---
name: quy-tac-viec-gi-cung-co-quy-trinh
description: "Mọi việc đều có quy trình, đi từ gốc lên (cây quy trình quy-trinh.md); GitHub luôn dựng lại được kết quả của lần trao đổi mới nhất trên mọi phiên, mọi thiết bị"
metadata:
  type: feedback
---

Mọi việc đều đi theo **cây quy trình** `quy-trinh.md`: quy trình gốc 7 bước cho mọi việc, rồi nhánh, rồi lá (câu David thường nói, file quy
trình, xong khi). Việc chưa có quy trình lá thì Claude làm theo quy trình gốc, làm xong thì viết thành quy trình lá trước khi báo xong. Mọi luật, cách làm, script vừa dùng để tạo ra kết quả
phải nằm trong GitHub (không chỉ ở thư mục tạm, bộ nhớ riêng của AI, lịch sử chat); script không ghi cố định công cụ mà chỉ một thiết bị có.

**Why:** 22/11/2026 — David: *"luôn luôn ở các phiên mới hoặc ai mới hay thiết bị mới hoàn toàn khi đọc được github là có thể làm ra ngay
được kết quả như những trao đổi mới nhất. Luôn luôn như vậy"*; rồi *"Sắp xếp tất cả mọi thứ, điều gì cũng cần phải có quy trình để thực
hiện. Như vậy thì mới đảm bảo sự giống nhau ở tất cả các kết quả"*; duyệt: *"Tất cả phần chung phải có quy trình. Quy trình từ gốc rồi đến
các phần khác đều phải có. Luôn đi từ gốc phát triển lên"*. Tình trạng lúc đó: script tách video chỉ nằm ở thư mục tạm, 6 script ghi cố định bộ mã hoá của
Mac, thiết bị mới chưa được cài công cụ tải link, hai bảng chọn skill bị chép trùng, vài việc thường giao (nhận link, đoạn thử) chưa có quy trình.

Cùng ngày, David chốt điểm duyệt: *"Phần nào đến bước duyệt thì vẫn phải chờ duyệt… những yêu cầu đặc biệt giống như là tự động làm video
cho đến khi ra kết quả luôn và bỏ qua các bước duyệt thì mới bỏ qua thôi, chứ còn không có trường hợp nào mà chạy lệch quy trình cả"*, từ đó có
ba điểm duyệt Đ1 (4 phần) · Đ2 (đăng, gửi, xoá, tài khoản — không bao giờ bỏ) · Đ3 (thông tin về David); chế độ tự chạy chỉ bỏ Đ1 khi lời
David nói rõ; mỗi quy trình lá ghi điểm duyệt (`quy-trinh.md` mục 1, 3). Từ 26/11/2026: việc đã có lá thì tự chạy là mặc định, không có Đ1; Claude không đăng bài (Đ2 còn gửi tin, tài khoản); cần đổi thì sửa quy trình ([[quy-tac-duyet-ke-hoach-4-phan]]).

**How to apply:** khi bắt đầu việc, Claude tra `quy-trinh.md`; khi kết thúc việc, Claude tự rà soát bằng câu "một phiên mới chỉ đọc GitHub có làm ra đúng kết quả này không?"
(`chuan-muc-lam-viec.md` mục 4). Công cụ kiểm tra `tu-dong-hoa/kiem-quy-trinh.py` chặn việc đẩy lên GitHub khi quy trình lá thiếu file / "Xong khi" hoặc skill
không có quy trình lá. Nguồn của luật: `quy-trinh.md`, `AGENTS.md` luật 6, `chuan-muc-lam-viec.md` mục 1 và 4. Liên quan
[[quy-tac-duyet-ke-hoach-4-phan]], [[co-so-tri-thuc-github-ban-goc]].

Gốc: khối 2 (Hành động) của tu-duy-goc.md — cùng một quy trình gốc thì mọi phiên, mọi máy, mọi người ra cùng một kết quả.
