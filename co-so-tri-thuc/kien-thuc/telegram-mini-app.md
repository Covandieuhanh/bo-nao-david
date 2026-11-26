---
description: Telegram Mini App — trang web HTML/JS mở ngay trong Telegram như một ứng dụng thật, nhận biết người dùng là ai; cách làm (telegram-web-app.js, HTTPS miễn phí, BotFather /newapp, kiểm tra initData), các chức năng, gợi ý cho trainer.
---

# Telegram Mini App

> Ghi 14/11/2026 từ trao đổi với David. Kiến thức chung, không phải quyết định.

## Bản chất

**Một trang web mở ngay bên trong Telegram**, trông như một ứng dụng. Người dùng không cần cài đặt, không cần đăng nhập: Telegram tự cho trang biết người dùng là ai.

## Cách làm

1. Viết trang web (HTML/JS), thêm `<script src="https://telegram.org/js/telegram-web-app.js"></script>`.
2. Đưa lên địa chỉ HTTPS (GitHub Pages, Vercel, Cloudflare Pages: miễn phí).
3. BotFather: `/newapp`, hoặc gắn địa chỉ vào nút Menu của bot.
4. Người dùng bấm nút trong bot hoặc liên kết `t.me/<tenbot>/<app>` để mở.
5. Khi có lưu dữ liệu: server kiểm tra `initData` (chữ ký Telegram gửi kèm) bằng token của bot để xác nhận đúng người dùng.

## Làm được

Nhận biết tên và ID người dùng · theo giao diện sáng/tối của Telegram · nút chính ở đáy · rung phản hồi · lưu dữ liệu trên đám mây Telegram · thanh toán bằng Stars · toàn màn hình · thêm biểu tượng ra màn hình chính.

## Áp vào việc của David

Gợi ý: đặt lịch buổi 1:1 (trưa giờ Việt Nam, cuối tuần) · check-in học viên hằng ngày (chuỗi ngày, tiến độ) · trang gói học kèm thanh toán Stars · bảng duyệt việc của David. Bước nhỏ nhất khi đủ điều kiện: Mini App check-in học viên phiên bản 0.

## Liên quan
- [telegram-bot.md](telegram-bot.md) — nền bot và tính năng Telegram.
- [danh-sach-y-tuong.md](../../du-an/danh-sach-y-tuong.md) mục 3 — điều kiện bắt đầu.
