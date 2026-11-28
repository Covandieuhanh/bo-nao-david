---
description: "Báo cáo trạng thái: chỉ ghi việc còn mở (đang làm chưa xong, chờ David quyết định, câu hỏi mở), mỗi dòng có ngày và bước tiếp theo; việc xong chuyển sang du-an/dong-goi/. Cập nhật cuối mỗi việc."
---

# Trạng thái hiện tại

Cập nhật 25/11/2026 (máy Windows). **Luật của file này:** chỉ giữ việc còn mở, mỗi dòng có ngày và bước tiếp theo; việc đã xong, hoặc quá 14 ngày
không ai cập nhật, thì chuyển sang `du-an/dong-goi/` (bản cũ tới 23/11: [2026-11-25-bao-cao-trang-thai-cu.md](du-an/dong-goi/2026-11-25-bao-cao-trang-thai-cu.md)).
Với video, sổ [du-an/danh-muc-noi-dung.md](du-an/danh-muc-noi-dung.md) là nguồn đáng tin hơn file này. Khi có máy, AI kiểm tra lại trên máy trước khi báo David.

## Ưu tiên

Tạo doanh thu (David chốt 13/11/2026), ba hướng chạy song song (`co-so-tri-thuc/david.md` 4.1, 4.3). Thứ tự khi phải chọn: giải pháp công nghệ AI — gói cá nhân và giải pháp cho tổ chức qua đội đối tác David tổng điều hành từ 18/11 ([pheu-ban-hang-goi-cong-nghe.md](du-an/pheu-ban-hang-goi-cong-nghe.md)), rồi Giai đoạn 1 trainer (1–3 trường hợp thực tế), rồi kênh tài chính David Trần Official.

## Đang làm chưa xong

| Việc | Tình trạng | Bước tiếp theo |
|---|---|---|
| Bản xem đủ kho hiệu ứng (lá B15, 28/11) | Bản 2 trên Drive `thanh-pham/tap-kho-hieu-ung-2711/`: chỉ hiệu ứng có mẫu, giao diện lấy đúng mẫu; ngang 10:40 (43 cảnh), dọc 1:29 | Chờ David xem; chờ đường dẫn reel MagentX để đo trên dưới, ô tròn, thẻ câu hỏi |
| Bot Sổ nhớ: bộ nhận tin không cần Claude + chuyển tin sang bot Điều hành + tự kiểm hằng ngày (David duyệt 28/11, dừng giữa chừng theo lời David "làm sau nhé") | Đã viết, **chưa bật**: `tu-dong-hoa/so-tay/nhan-tin.py`, `tra-loi.py`, `settings-xu-ly.json`, luật nháp `quy-tac-bot.moi.md`, chế độ `--chuyen` trong `dieu-hanh/bot.py`, nhánh `MOI` trong `canh-bot.sh` (tắt khi chưa có file `.trang-thai/nhan-tin-moi`). Bot đang chạy vẫn theo cách cũ | Còn: `cai-nhan-tin.sh` (launchd `com.david.so-nho-nhan`), `do-bot.py` đọc `so-nho-tin.log`, lịch `[TU-KIEM]` 05:30 + canh-bot kiểm 06:30, chạy thử, bật công tắc, chép `quy-tac-bot.moi.md` đè `quy-tac-bot.md`, ghi README |
| Ba video bản dài từ buổi DJI_0031 (25/11, máy Windows): hàng hoá 5:10 · tập trung một đường 12:56 · AI may đo 3:39 | Đã xong, nằm trên Drive `thanh-pham/<tập>/` và `_buoi-tap-dji0031-2511/`, bản xem nhanh ở `D:\ket-qua-dji0031-2511`; **chưa duyệt** | David xem; David nói "chốt" thì AI xoá bản gốc theo quy trình; gói đăng để sẵn, David tự đăng; phụ đề ở các mốc "cần nghe lại" ghi trong gói đăng |
| Giữ gốc bộ não ổn định (25/11) | Đã xong: sổ dẫn chứng gốc và cổng kiểm soát `cong-kiem-soat-goc.py`, ngôn từ chuẩn toàn bộ não (`kiem-ngon-tu.py`), AI mới làm bài kiểm đạt 21/21 và 10/10 | Theo dõi lần đẩy GitHub tới: cổng kiểm soát chặn đúng; ý mới vào tầng 3 trước rồi mới thăng cấp |
| Kiểm chất lượng giữa thiết bị, AI và phiên mới (26/11) | Sau [đợt đánh giá 25–26/11](du-an/nang-cap/danh-gia-2026-11-25.md), đã bổ sung chuẩn bắt buộc, phạm vi sáng tạo và [các ca thực hành](co-so-tri-thuc/bai-kiem/thuc-hanh.md) | Chạy cùng đầu vào trên các cấu hình David dùng; ghi kết quả theo từng tiêu chí và số vòng sửa |

## Chờ David quyết định (câu hỏi mở từ trước, chưa thấy trả lời)

- (05–07/11) Cắt lại Clip 1 và 2 của "Đi trainer" theo luật mới? · "bạn ấy" hay "bạn em" ở khoảng 5:12 video dài "Mục tiêu"? · kế hoạch đăng "Đi trainer".
- (19/11) Trên Mac chạy một lần lệnh `! sudo pmset repeat wakeorpoweron MTWRFSU 06:55:00` để lịch 7:00 chạy được khi Mac ngủ.
- Fanpage: đổi tên thành "David Trần - Trainer định hướng", ảnh bìa còn chữ kinh doanh cũ · TikTok: gỡ liên kết ahasale, quyết định ẩn hay giữ video cũ chạm lằn ranh.

## Việc phải nhớ về sau

- 17/11: việc tổng hợp tin nhắn giao qua Telegram tự mở phiên kèm `--chrome` (giao-viec.sh nhận các từ khoá: tổng hợp tin, tong-hop-tin-nhan, Zalo, Messenger). Phiên lịch 7:00 vốn đã có Chrome.

- Việc sang Đức chỉ là dự định, AI không tính vào việc đang làm tới khi David khẳng định. AI không tư vấn thuế hay pháp lý thay họ.
- Cần tìm: người giữ nhịp kênh video.
- Sách CCL Press do David tự mua, không dùng bản không rõ nguồn gốc.
- Bot Sổ nhớ: máy gõ tin vào bot bằng bộ đệm screen (`stuff` âm thầm làm mất tin dài hơn khoảng 1024 byte, từng làm rơi khung hỏi thói quen 11:00 và 16:00 ngày 14/11). Tin dạng thẻ do máy gửi chỉ tính là đã gửi khi bot nhận; sổ trên máy ghi "bot da nhan" / "gui thang" trong `.trang-thai/canh-bot.log`.

## Sao lưu

Xem [huong-dan-cai-dat.md](huong-dan-cai-dat.md) mục 1 và 5. Repo chỉ giữ bộ não, việc làm chưa xong và mẫu; thành phẩm nằm ở Drive `thanh-pham/`.
