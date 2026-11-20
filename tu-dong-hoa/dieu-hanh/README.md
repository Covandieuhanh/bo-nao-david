---
description: "Bot Điều hành trên Telegram: trạm điều khiển các phiên Claude trên Mac (giao việc, nhắn tiếp #N, đóng phiên, duyệt 🔐 ❓ bằng nút bấm, báo cáo, cảnh báo máy); chạy bằng script, không tốn token; cài đặt, cách dùng."
---

# Bot Điều hành (Telegram)

Từ 20/11/2026, David dùng **hai bot**, mỗi bot một kiểu việc (David duyệt 20/11):

| Bot | Lo việc gì | Chạy bằng |
|---|---|---|
| **Sổ nhớ** ([../so-tay/](../so-tay/README.md)) | Đời sống: ghi sổ, nhắc giờ, thói quen, ăn uống, thể trạng, tóm tắt sáng, tin nhắn tổng hợp 📬 | Phiên Claude (cần hiểu lời nói tự do) |
| **Điều hành** (đây) | Các phiên Claude: giao việc, nhắn tiếp `#N`, đóng phiên, nhắn phiên đang mở, xem đang chạy / việc dở, duyệt 🔐 ❓, báo cáo phiên, cảnh báo máy, 📶 | Script [bot.py](bot.py): trả lời tức thì, không tốn token, không phụ thuộc đăng nhập Claude |

Vì sao tách theo **cách dùng**, không theo ba hướng nghề: ba hướng nghề là cách phân loại nội dung, còn bot là cửa tương tác. Tin cần nhanh (duyệt, báo cáo) không được chìm giữa tin hỏi thăm ăn uống, và việc điều khiển không cần Claude hiểu lời. Chỉ thêm bot mới khi có dòng việc thật, ví dụ cảnh báo giá cho hướng tài chính.

## Cách dùng (nhắn bot)

- Một câu bình thường → giao việc cho Claude (`giao-viec.sh`, phiên hiện trong app Claude). Tin quá ngắn (dưới 12 chữ cái) không giao, trừ lệnh bài đăng ("lọc lại", "sửa bài <ngày>: …").
- `#N <lời>` hoặc trả lời (trích) tin `#N …` → nhắn tiếp cho việc #N. `đóng #N` hoặc nút **[Đóng phiên #N]** dưới tin ✅ → đóng phiên.
- `@<tên hoặc số phiên>: <lời>` → nhắn phiên David tự mở (`hop-thu-phien.py`). `/phien` liệt kê số.
- Tin 🔐 có nút **Đồng ý / Từ chối**; tin ❓ một câu có nút từng lựa chọn. Trả lời (trích) tin cũng được, kể cả "không, <lý do>". Một yêu cầu đang chờ thì nhắn ngắn "ok" / "không" là đủ.
- Lệnh: `/dang_chay` · `/viec` · `/viec_do` · `/phien` · `/suc_khoe` · `/vang` · `/ve` · `/huong_dan`. Tin thoại được nghe (`so-tay/nghe-thoai.sh`).
- Chỉ nhận tin của David (người trong `allowFrom` của Sổ nhớ); người lạ bị bỏ qua, ghi nhật ký.

## Đường tin đi

- `so-tay/bao-cao.sh` mặc định gửi qua bot Điều hành; `--so-nho` gửi qua Sổ nhớ (nhắc giờ ⏰ của máy canh, tin 📬 của `tong-hop-tin-nhan`). `--nut '<json>'` kèm nút bấm. Chưa có token Điều hành, hoặc bot Điều hành chưa nhắn được (David chưa bấm Start, lỗi 400/401/403/404), thì tin đi qua Sổ nhớ, không nút. Tin duyệt không vào hàng chờ gửi lại (hết hạn thì gửi muộn chỉ gây nhầm).
- `so-tay/duyet-tu-xa.py` (hook xin phép) gửi 🔐 ❓ kèm nút, chờ file `.trang-thai/duyet/<mã>.tra`; bot ghi file đó khi David bấm hay trả lời.
- Máy canh (`so-tay/canh-bot.sh`) xem nhịp `.trang-thai/dieu-hanh-nhip`: quá 10 phút thì khởi động lại bot, vẫn hỏng thì báo David qua Sổ nhớ (3 giờ một lần).

## Cài

1. Telegram → @BotFather → `/newbot`, đặt tên (ví dụ "Điều hành David"), lấy token. David tự làm, Claude không chạm token.
2. `bash tu-dong-hoa/dieu-hanh/cai-dat.sh "<token>"`: lưu token vào `~/.claude/channels/dieu-hanh/.env` (chmod 600, không lên GitHub), kiểm token, đăng ký launchd `com.david.dieu-hanh` (KeepAlive), chép luật mới cho Sổ nhớ, khởi động lại phiên Sổ nhớ và máy canh.
3. Mở bot trên Telegram, bấm Start (bot gửi trả lời được cho David chỉ sau khi David nhắn bot trước).

Thử không cần Telegram: `python3 -I tu-dong-hoa/dieu-hanh/bot.py --thu "/viec"` (in ra thay vì gửi; tin giao việc vẫn giao thật, đừng thử bằng câu giao việc). Nhật ký: `~/Documents/2-ca-nhan/so-tay/.trang-thai/dieu-hanh.log`.
