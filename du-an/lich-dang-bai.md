---
description: "Hệ thống lịch đăng bài Facebook cá nhân: tuần nào cũng 4 bài kể cả không có video — kho 8 bài nền, lịch tự soạn sáng thứ 6, ảnh ChatGPT, duyệt cả tuần qua Telegram, nhắc 19:45, David tự bấm; kèm sổ lịch."
---

# Hệ thống lịch đăng bài — Facebook cá nhân

Hồ sơ hình ảnh (định vị, 4 trụ, 5 kiểu bài nền, luật ảnh): [hinh-anh-facebook-ca-nhan.md](hinh-anh-facebook-ca-nhan.md) · khung lịch: `kenh.json` → `lich.facebook_ca_nhan`.
**Bài và ảnh** (sản phẩm, không lên GitHub): `~/Documents/1-nghe-nghiep/bai-dang/` — mỗi ngày đăng một thư mục `YYYY-MM-DD/` (`bai.md`, `anh.png`), kho ở `kho-bai-nen/`, bản tóm tuần `tuan-YYYY-MM-DD.md`.

## Mục tiêu
Không tuần nào trống: **4 bài/tuần** (T3 video · T5 bài viết công nghệ · T6 video · CN bài viết con người / đời thường, 20:00 giờ Việt Nam). Đo bằng: số tuần đủ bài, số người kể chuyện của họ (bình luận, tin nhắn).

## Cách chạy
| Khi | Ai | Làm gì |
|---|---|---|
| **Thứ 6 07:30** | lịch tự chạy `lich-dang-tuan` (`tu-dong-hoa/lich/`) | soạn 4 bài cho CN, T3, T5, T6 sắp tới (giữ bài đã có), làm ảnh, bù kho đủ 8, ghi sổ, gửi Telegram, đặt nhắc 19:45 |
| Thứ 6 trong ngày | David | trả lời bot: "duyệt tuần" hoặc "sửa bài <ngày>: …" |
| **19:45 ngày đăng** | bot Sổ nhớ (`nhac-viec.md`) | nhắc David đăng, trỏ tới tin bài + ảnh đã gửi sáng thứ 6 |
| 20:00 | David | tự bấm đăng trên Facebook cá nhân (trang cá nhân không hẹn giờ được) |
| Đóng gói tuần | skill `san-pham-hoa` | đếm người bình luận kể chuyện, nhắn riêng; ghi câu chuyện nào kéo được người kể |

**Chọn bài cho từng ô:**
- **Ô video (T3, T6):** video David đã duyệt trong `du-an/danh-muc-noi-dung.md` chưa lên Facebook cá nhân; chữ lấy nguyên văn lời David (luật 3). Không có → bài nền từ kho.
- **Ô bài viết (T5, CN):** soạn mới từ lời David tuần qua (`~/Documents/2-ca-nhan/so-tay/kho-du-lieu/`, sổ nhớ) đúng trụ của ngày; chưa đủ nguyên liệu → bài nền từ kho.
- **Kho bài nền:** luôn **8 bài đã soạn**, đủ 5 kiểu (hồ sơ mục 4); lấy ra bao nhiêu soạn bù bấy nhiêu. Bài nền dùng rồi chuyển sang thư mục ngày đăng.
- **Ảnh:** theo hồ sơ mục 5 (ảnh của David trước, ChatGPT trên Chrome khi không có gì).

## Sổ lịch
Trạng thái: nháp · đã gửi duyệt · duyệt · đã đăng · thay (ghi lý do).

| Ngày | Ô | Trụ | Bài | Nguồn | Trạng thái |
|---|---|---|---|---|---|
| T5 19/11 | bài viết | 1 | Tin nhắn khách đổ về nhiều nơi, sót việc → gom về một bảng mỗi sáng | bài nền #1 | nháp |
| T6 20/11 | video | 2 | "Bận cả ngày mà không ra kết quả" (clip A nếu dựng, không thì bản đầy đủ) · video chưa duyệt kịp thì bài nền #6 | `~/Movies/tap-ban-ca-ngay` | nháp · chờ duyệt video |
| CN 22/11 | bài viết | 2 | Lần đầu dẫn người: ngừng làm thay | soạn mới | nháp |
| T3 24/11 | video | 2 | Clip 76 s "Mục tiêu và sứ mệnh" | David ok 07/11 | nháp |

## Kho bài nền (8)
| # | Kiểu | Trụ | Bài |
|---|---|---|---|
| 2 | Kết quả thật | 4 | Mình chỉ quay và nói ý, phần dựng video máy làm |
| 3 | Cách mình làm việc | 1 | Bốn bước trước mọi việc: Mục tiêu · Kế hoạch · Quy trình · Thực thi |
| 4 | Bài học dẫn người | 2 | Thước đo của mình: người được đồng hành tự đứng được |
| 5 | Câu hỏi cho người xem | 1 | Máy móc chỉ là công cụ: việc nào ở chỗ bạn lặp lại mỗi ngày? |
| 6 | Cách mình làm việc | 3 | Làm theo đợt năng lượng, việc trí óc tối đa 4 tiếng/ngày |
| 7 | Bài học dẫn người | 2 | Ba tầng làm chủ: vì sao bắt đầu từ bản thân |
| 8 | Vấn đề → cách giải | 1 | Một trợ lý trên Telegram nhắc việc, ghi nhớ thay mình |
| 9 | Kết quả thật | 4 | Cuối tuần, báo cáo tự gom về: tuần này có gì, nỗi đau nào lặp lại |

## Nhật ký
- 17/11/2026: David duyệt hệ thống (kho 8 bài nền, lịch thứ 6 07:30, duyệt cả tuần qua Telegram, nhắc 19:45, David tự bấm, làm Facebook cá nhân trước) và giao dùng ChatGPT trên Chrome tạo ảnh khi không có nội dung David chuẩn bị.
