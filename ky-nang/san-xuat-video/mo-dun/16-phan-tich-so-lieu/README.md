# Khối 16-phan-tich-so-lieu: Số liệu sau đăng (báo lỗi, không quyết định): ảnh chụp số liệu 7 ngày → so-lieu.md

**Dùng trong:** cả 4
**Đầu vào:** ảnh chụp YouTube Studio / TikTok
**Đầu ra:** so-lieu.md của dự án + so-lieu-tong.md
**Tham số hồ sơ:** —
**Sửa khối này → chạy lại:** —

**File thật (code, một bản duy nhất):**
- `mau-so-lieu.md` (mẫu ghi số liệu, nằm ngay trong khối này)

## Luật
- Mỗi video giao kèm `<dự án>/so-lieu.md` (chép `mau-so-lieu.md`). 7 ngày sau đăng, David gửi ảnh chụp số liệu (YouTube Studio /
  TikTok / Facebook) → Claude điền: lượt xem, tỉ lệ xem hết / thời lượng xem trung bình, giây rời nhiều nhất, % còn lại ở giây 3, CTR
  thumbnail (video ngang YouTube), lưu / chia sẻ / bình luận. Tổng hợp nhiều video ở `san-xuat-video/so-lieu-tong.md`.
- Số liệu dùng để **báo lỗi**, không thay hình mẫu: rời ồ ạt ở 0–3 s → câu mở sai; rời ở một cảnh → cảnh đó. So với video trước → đề xuất **một**
  chỉnh sửa vào `ho-so-thuong-hieu/<loai>` hoặc luật (kèm bằng chứng), David duyệt rồi mới đổi và ghi changelog.

## Thước đo chính theo kênh David (`ho-so-thuong-hieu/kenh.json`)
Ghi trước tiên **số người nhắn "gỡ"** (Messenger trang + bình luận) và số bình luận "Vấn đề" / "Kết quả" của mỗi bài; lượt xem, giữ chân
chỉ để tìm chỗ người xem rời đi. Kèm kiểu dẫn dắt của bài (Không / Gợi mở / Mời) để so tỉ lệ 4 · 4 · 2 nào chuyển hoá tốt hơn.
Cập nhật trạng thái bài trong sổ `~/Movies/_danh-muc-noi-dung/danh-muc-noi-dung.md`.
