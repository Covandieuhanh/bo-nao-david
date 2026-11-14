---
name: quy-tac-tu-trien-khai-nhin-thay-duoc
description: Việc gì cũng tự triển khai hết tới khi chắc chắn dùng được, không dừng chờ duyệt; ưu tiên app Claude, không chạy ẩn/nền — chạy thành phiên David thấy và kiểm được (14/11/2026)
metadata:
  type: feedback
---

Giao việc thì **tự triển khai trọn**, thử thật tới khi chắc dùng được rồi mới báo; không dừng giữa chừng xin duyệt kế hoạch (chỉ dừng khi David nói đúng chữ "làm kế hoạch", xem [[quy-tac-duyet-ke-hoach-4-phan]]). Việc tự chạy (lịch, việc định kỳ) phải **chạy thành phiên hiện trong app Claude** (phiên Remote Control như `giao-viec.sh`, `tu-dong-hoa/lich/chay-lich.sh`; không dùng Scheduled tasks của app vì app chỉ đọc lịch lúc khởi động, thử 14/11 22:52 không chạy), không `claude -p` chạy ngầm, không tiến trình nền David không thấy. David dùng app Claude là chính, chỉ đổi tài khoản Claude khi hết token: mọi thứ phải chạy lại được sau khi đổi tài khoản, không cần làm AI khác.

**Why:** 14/11/2026 23:xx (việc #22), sau khi Claude trình kế hoạch 4 phần rồi dừng chờ và đưa lịch gom/đóng gói sang chạy ngầm bằng Terminal: "làm cái gì cũng cần phải chắc chắn là tự động triển khai hết, chứ không phải chờ để duyệt, phải làm hướng chắc chắn dùng được. hiện thì tôi khá là ưu tiên sử dụng trên app claude này, cùng lắm chỉ đổi tài khoản khi hết token thôi nên cũng đừng làm cái gì ẩn hay chạy nền, cứ chạy trên các phiên hoặc làm cách nào để tôi nhìn thấy và kiểm tra được".

**How to apply:** trước khi báo xong, tự chạy thử thật (lịch thì đặt lượt thử vài phút sau và chờ kết quả). Chọn cách đã chứng minh chạy được hơn cách hay mà chưa thử. Liên quan [[quy-tac-phien-telegram-tu-chay]], [[quy-tac-ket-qua-hon-toc-do]].
