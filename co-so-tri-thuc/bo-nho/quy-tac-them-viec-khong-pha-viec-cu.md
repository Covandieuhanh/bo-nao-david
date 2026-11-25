---
name: quy-tac-them-viec-khong-pha-viec-cu
description: Thêm việc / tính năng mới không được làm hỏng việc cũ đang chạy; chỉ sửa phần cũ khi 4 phần đã duyệt ghi rõ là sửa phần cũ; mọi thứ phải tự động (19/11/2026)
metadata:
  type: feedback
---

Thêm việc mới (tính năng, cờ, thư mục, bước) vào hệ đang chạy thì **việc cũ phải chạy y như trước**. Chỉ được đổi cách việc cũ chạy khi kế hoạch 4 phần đã duyệt ghi rõ "sửa cả phần cũ". Sửa xong phải **tự thử chính việc cũ** (chạy thật hoặc máy tự thử) trước khi coi là xong. Mọi thứ phải tự động, không trông vào David bấm tay.

**Why:** ngày 18/11/2026 em thêm thư mục công ty (`--add-dir bo-nao-veltrix`) vào lệnh mở phiên lịch để ghi mục 🏢. Từ đó mọi phiên lịch vướng ở hộp hỏi "tin cậy thư mục", không ai bấm. Hậu quả: 19/11 không có bản tổng hợp tin, gom đêm 18/11 cũng không chạy. David (19/11, việc #30): "mọi thứ phải tự động, những gì đã làm rồi thì sau này có bổ sung thêm việc khác thì cũng không được ảnh hưởng việc cũ chứ, trừ khi có yêu cầu duyệt theo kế hoạch có sửa cả các phần cũ".

**How to apply:**
- Sửa script dùng chung (lệnh mở phiên, máy canh bot, hook) thì trong phần Thực thi của 4 phần phải có bước "thử lại việc cũ".
- Lệnh mở phiên lịch có máy tự thử: `tu-dong-hoa/lich/thu-mo-phien.sh`. Máy canh bot tự chạy nó mỗi khi `chay-lich.sh` đổi, hỏng thì nhắn David.
- Phiên chạy ngầm không được để vướng ở hộp hỏi: canh sớm 3 phút (`lich-chay.md`). Bổ sung cho [[quy-tac-hoc-la-bo-sung]], [[quy-tac-duyet-ke-hoach-4-phan]].
