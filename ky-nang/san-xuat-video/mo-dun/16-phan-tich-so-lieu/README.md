---
description: "Khối 16 số liệu sau khi đăng: đọc số liệu, báo lỗi, không tự quyết định."
---

# Khối 16-phan-tich-so-lieu: Số liệu sau đăng (báo lỗi, không quyết định): ảnh chụp số liệu 7 ngày → so-lieu.md

**Dùng trong:** cả 4
**Đầu vào:** ảnh chụp YouTube Studio / TikTok
**Đầu ra:** so-lieu.md của dự án + so-lieu-tong.md
**Tham số hồ sơ:** —
**Sửa khối này thì chạy lại:** —

**File thật (code, một bản duy nhất):**
- `mau-so-lieu.md` (mẫu ghi số liệu, nằm ngay trong khối này)

## Luật
- Mỗi video giao kèm `<dự án>/so-lieu.md` (chép từ `mau-so-lieu.md`). 7 ngày sau khi đăng, David gửi ảnh chụp số liệu (YouTube Studio /
  TikTok / Facebook) thì Claude điền: lượt xem, tỉ lệ xem hết / thời lượng xem trung bình, giây rời nhiều nhất, % còn lại ở giây 3, CTR
  thumbnail (video ngang YouTube), lưu / chia sẻ / bình luận. Tổng hợp nhiều video ở `san-xuat-video/so-lieu-tong.md`.
- Số liệu dùng để **báo lỗi**, không thay hình mẫu: người xem rời đi hàng loạt ở 0–3 s nghĩa là câu mở sai; người xem rời đi ở một cảnh nghĩa là cảnh đó có lỗi. Claude so với video trước rồi đề xuất **một**
  chỉnh sửa vào `ho-so-thuong-hieu/<loai>` hoặc luật (kèm dẫn chứng); David duyệt rồi Claude mới đổi và ghi nhật ký thay đổi.

## Thước đo chính theo kênh David (`ho-so-thuong-hieu/kenh.json`)
Claude ghi trước tiên **số người nhắn "gỡ"** (Messenger của trang và bình luận) và số bình luận "Vấn đề" / "Kết quả" của mỗi bài; lượt xem và tỉ lệ giữ chân
chỉ dùng để tìm chỗ người xem rời đi. Claude ghi kèm kiểu dẫn dắt của bài (Không / Gợi mở / Mời) để so sánh kiểu nào trong tỉ lệ 4 · 4 · 2 chuyển đổi tốt hơn.
Cập nhật trạng thái bài trong sổ `~/Movies/_danh-muc-noi-dung/danh-muc-noi-dung.md`.
