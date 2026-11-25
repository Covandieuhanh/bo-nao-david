---
name: quy-tac-phien-telegram-tu-chay
description: "Phiên việc giao qua Telegram: trình 4 phần chờ duyệt, duyệt rồi tự làm tới kết quả, ghi sổ; chỉ hỏi khi đăng/gửi, tốn tiền, đẩy đè GitHub, xoá ổ đĩa; mọi phiên bật Remote Control, xong thì hỏi đóng (12/11, 14/11/2026)"
metadata:
  type: feedback
---

Phiên việc giao qua Telegram trình đủ 4 phần trước, gửi qua `bao-cao.sh "#N ❓ Chờ anh duyệt 4 phần: …"` ([[quy-tac-duyet-ke-hoach-4-phan]]).
Duyệt rồi tự làm tới kết quả: xoá file, cài/gỡ phần mềm, sửa cấu hình máy hoặc Claude, sudo, thao tác GitHub thường thì **tự chạy, ghi sổ**
`~/Documents/2-ca-nhan/so-tay/.trang-thai/tu-duyet.log`, kể lại trong tin báo cáo cuối. Chỉ hỏi David: đăng/gửi ra ngoài, bấm/điền trên web
(luật 4), tốn tiền, đẩy đè GitHub / xoá repo (luật 6), xoá ổ đĩa.

Mọi phiên tự bật Remote Control (`remoteControlAtStartup`, `cai-hook.py`) để David theo dõi trên app. Việc xong hoàn chỉnh thì hỏi
"Đóng phiên nhé?", David đồng ý thì đóng.

**How to apply:** việc mới bị hỏi mà David hay đồng ý thì chuyển mẫu đó sang mức tự chạy. Liên quan [[quy-tac-goi-y-de-david-chon]],
[[quy-tac-ky-nang-tu-cai-tien]].

Nguồn của luật: `tu-dong-hoa/so-tay/cong-duyet.py` (mẫu có `!` = hỏi) + README so-tay; đóng phiên ở `ky-nang/chuan-muc-lam-viec.md` mục 5,
`giao-viec.sh`, `quy-tac-bot.md`. Ghi nhớ này giữ ngày, lời David, lý do.

## Sổ
- 11/11/2026: mọi việc rủi ro đều hỏi.
- 12/11/2026 David vừa đồng ý 3 yêu cầu xin phép GA36, V52X, FNDA: "tôi thấy mấy yêu cầu này cần phải tự động vì đa phần tôi đều đồng ý với
  các đề xuất rồi, nên không cần phải hỏi như thế này cho các trường hợp tương tự sau nữa nhé. tôi chỉ quan tâm kết quả thôi" thì bỏ bản 11/11.
- 14/11/2026 (việc #14): "từ giờ có mở phiên hãy mở công khai để trên app cũng thấy nhé, tôi còn tiện theo dõi. Và cập nhật thêm là các
  phiên cứ xong hoàn chỉnh rồi, hỏi xác nhận tôi nếu xong rồi thì có thể đóng phiên cho đỡ nhiều. vì cái gì cũng lưu vào file ở máy rồi nên
  không lo" thì Remote Control mọi phiên, hỏi đóng phiên.
- 14/11/2026 (việc #22): phiên việc trình 4 phần trước khi tự chạy ([[quy-tac-duyet-ke-hoach-4-phan]]).
- 20/11/2026: "tôi cảm giác là hiện tại đang bị gộp quá nhiều tính năng trên 1 con bot telegram… mỗi bot telegram làm một việc để dễ
  quản lý và tương tác hơn" thì David duyệt tách hai bot theo cách dùng: Sổ nhớ (đời sống) và Điều hành (phiên Claude, duyệt bằng nút,
  báo cáo, cảnh báo máy; script, không tốn token). Không chia theo ba hướng nghề: bot là cửa tương tác, không phải kho nội dung. Nhà
  của luật: `tu-dong-hoa/dieu-hanh/README.md`.
