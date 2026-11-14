---
name: quy-tac-phien-telegram-tu-chay
description: Phiên việc giao qua Telegram tự làm tới kết quả, không xin phép từng bước; chỉ hỏi khi đăng/gửi, tốn tiền, đẩy đè GitHub, xoá ổ đĩa (12/11/2026)
metadata:
  type: feedback
---

Phiên việc giao qua Telegram: xoá file, cài/gỡ phần mềm, sửa cấu hình máy hoặc Claude, sudo, thao tác GitHub thường → **tự chạy, ghi sổ** `~/Documents/2-ca-nhan/so-tay/.trang-thai/tu-duyet.log`, kể lại trong tin báo cáo cuối. Chỉ còn hỏi David: đăng/gửi ra ngoài, bấm/điền trên web (luật 4), tốn tiền, đẩy đè GitHub / xoá repo (luật 6), xoá ổ đĩa. Nhà chính: `tu-dong-hoa/so-tay/cong-duyet.py` (mẫu có `!` = hỏi) + README so-tay.

**Why:** 12/11/2026 David vừa đồng ý 3 yêu cầu xin phép GA36, V52X, FNDA: "tôi thấy mấy yêu cầu này cần phải tự động vì đa phần tôi đều đồng ý với các đề xuất rồi, nên không cần phải hỏi như thế này cho các trường hợp tương tự sau nữa nhé. tôi chỉ quan tâm kết quả thôi". Bản 11/11 (mọi việc rủi ro đều hỏi) đã bỏ.

**How to apply:** việc mới bị hỏi mà David hay đồng ý → chuyển mẫu đó sang mức tự chạy. Liên quan [[quy-tac-goi-y-de-david-chon]], [[quy-tac-ky-nang-tu-cai-tien]].

**14/11/2026 (việc #14):** "từ giờ có mở phiên hãy mở công khai để trên app cũng thấy nhé, tôi còn tiện theo dõi. Và cập nhật thêm là các phiên cứ xong hoàn chỉnh rồi, hỏi xác nhận tôi nếu xong rồi thì có thể đóng phiên cho đỡ nhiều. vì cái gì cũng lưu vào file ở máy rồi nên không lo" → mọi phiên tự bật Remote Control (`remoteControlAtStartup`, `cai-hook.py`); xong hoàn chỉnh thì hỏi "Đóng phiên nhé?", David đồng ý thì đóng (`chuan-muc-lam-viec.md` mục 5, `giao-viec.sh`, `quy-tac-bot.md`).

**14/11/2026 (việc #22):** phiên việc trình đủ 4 phần trước, gửi qua `bao-cao.sh "#N ❓ Chờ anh duyệt 4 phần: …"`; duyệt rồi mới tự chạy như trên: [[quy-tac-duyet-ke-hoach-4-phan]].
