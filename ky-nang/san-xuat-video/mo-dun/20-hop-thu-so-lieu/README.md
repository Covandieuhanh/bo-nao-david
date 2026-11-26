---
description: "Khối 20 hộp thư và số liệu: tổng hợp bình luận, tin nhắn, đọc số liệu 24 giờ sau khi đăng."
---

# Khối 20-hop-thu-so-lieu: Tổng hợp bình luận và tin nhắn · đọc số liệu 24 giờ / 7 ngày (CHỈ ĐỌC)

**Dùng trong:** skill `phan-phoi-da-kenh` bước 7–8 · **Trình duyệt:** trình duyệt riêng trong app (đã đăng nhập) · **Đầu ra:** `hop-thu-<ngày>.md`,
`so-lieu.md` của dự án, cập nhật sổ `~/Movies/_danh-muc-noi-dung/danh-muc-noi-dung.md`.

## Luật
- **Chỉ đọc.** Không trả lời bình luận / tin nhắn, không xoá, không ẩn, không đổi cài đặt. Khi cần trả lời, Claude soạn bản nháp, David duyệt
  từng câu, rồi Claude mới gửi (mỗi lần gửi là một lần David đồng ý).
- **Thước đo chính:** số người nhắn "gỡ" + số bình luận "Vấn đề" / "Kết quả" (`kenh.json`). Lượt xem / tỉ lệ giữ chân chỉ dùng để tìm chỗ người xem rời đi.
- Claude không chép tên, số điện thoại, ảnh của người bình luận / nhắn tin vào file (chỉ đếm và tóm tắt ý câu hỏi, ẩn danh).

## 24 giờ sau khi đăng
Claude kiểm tra bài đã lên đúng (link, giờ, ảnh bìa, caption) ở 3 nền tảng rồi ghi "đã đăng" và link vào sổ.

## Tổng hợp hộp thư (khi David hỏi, hoặc trong buổi nhìn lại cuối tuần)
- **Trang Facebook:** `https://business.facebook.com/latest/inbox` (Messenger + bình luận) rồi đếm tin có chữ "gỡ", tóm tắt các câu hỏi.
- **YouTube:** Studio → Bình luận · **TikTok:** TikTok Studio → Bình luận.
- Viết `hop-thu-<ngày>.md`: "Người xem đang hỏi gì" (nhóm theo chủ đề, ẩn danh) · số "gỡ" · số "Vấn đề" / "Kết quả" · nháp trả lời (nếu David muốn).
  Với câu hỏi lặp lại ít nhất 3 lần, Claude đề xuất thành ý video tiếp theo (đưa vào kho, gắn nhãn nhánh).

## Số liệu 7 ngày (khối 16 + mau-so-lieu.md)
- **YouTube:** Studio thì Số liệu phân tích (lượt xem, thời lượng xem trung bình, tỉ lệ giữ chân, giây rời nhiều nhất).
- **Trang Facebook:** Business Suite → Thông tin chi tiết → Nội dung (lượt xem Reels, thời gian xem, tin nhắn bắt đầu).
- **TikTok:** TikTok Studio → Số liệu phân tích → bài viết (lượt xem, thời gian xem trung bình, xem hết).
- Claude điền `so-lieu.md`; so sánh theo kiểu dẫn dắt (Không / Gợi mở / Mời) và theo nhánh (gốc / công việc / quan hệ) rồi đưa ra 1–3 đề xuất cho lần sau (báo lỗi, không tự đổi luật).
