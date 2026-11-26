---
description: "Bộ nhận diện chung của mọi loại video: vị trí, thành phần cố định, ngôn ngữ thiết kế."
---

# Bộ nhận diện chung — mọi loại video

**Mọi loại video có cùng tiêu chuẩn** (vị trí, thành phần cố định, ngôn ngữ thiết kế). Chỉ **motion graphics** là tự do chọn theo loại
video và theo từng cảnh. Nguồn code duy nhất: `nhan-dien-thuong-hieu.js` (`khung(W, H)`), `dau-goc.jsx`, `thanh-thoi-gian.jsx`, `than-man-ket.jsx`,
`bien-thiet-ke.js`, `thuong-hieu.json`, `kieu-phu-de.js`, `keu-goi-hanh-dong.js`, `bieu-tuong.jsx`. Mẫu 1 video, podcast, ghép vlog, highlight đều đọc ở đây.

## 0. Chữ ký nhận diện — yếu tố thẩm mỹ duy nhất phải giữ

> "Về thẩm mỹ thì tôi chỉ cần duy nhất 1 thứ là người xem có thể nhận diện được dù xem video nào cũng là của cùng 1 người làm." — David

Người dựng giữ ở MỌI video, mọi cảnh có chữ:
1. Các thành phần cố định ở mục 1 (dấu góc ● DAVID, phụ đề, thanh thời gian, màn chốt, thẻ cuối) — đúng vị trí, đúng kiểu.
2. **Màu nhấn cam** `C.accent` là màu nhấn duy nhất (khoảng 10 % khung). Màu nền và màu phụ được phép đổi theo nội dung.
3. **Hai font chính** `HEAD` (Barlow Condensed) cho chữ to, `BODY` (Be Vietnam Pro) cho chữ thường. Font phụ `NHAN` (chữ có chân,
   nghiêng) chỉ dùng cho **một từ nhấn** trong cụm (`*từ*` trong ChuHien), không thay font chính.

Ngoài ba điều trên là **tự do sáng tạo theo nội dung**: nền tối / sáng / giấy / người mờ, kết cấu, ánh sáng, kiểu hình (biểu tượng nét
tròn, phấn vẽ tay, ảnh), bố cục, chuyển động. Phép thử: che dấu góc đi, nếu người xem quen kênh vẫn đoán được là video của David nhờ màu cam + chữ
+ phụ đề thì đạt. Màu nhấn, hai font chính, nhạc kênh (`bien-thiet-ke.js`, `thuong-hieu.json`) không đổi khi học video mẫu.

## 1. Thành phần cố định (có ở mọi video)

| Thành phần | Khung dọc 1080×1920 | Khung ngang 1920×1080 | Code |
|---|---|---|---|
| Vùng an toàn | x 70–900, y 210–1420 (chừa nút, chữ của Reels/TikTok) | lề 5 % mọi phía (title safe SMPTE 90 %) | `khung().safe` |
| Dấu góc ● DAVID │ chủ đề (ô nền sẫm đặc `C.nen`) | góc trên trái, top 228 | góc trên trái, top 54 (sát mép vùng an toàn) | `dau-goc.jsx`, `khung().brand` |
| Thanh thời gian (đã chạy · thanh · còn m:ss) | y 1386, cao 30 — chỉ video dọc dài | y 996, cao 30 (sát đáy, 92–95 % chiều cao) | `thanh-thoi-gian.jsx`, `khung().tl` |
| Phụ đề | luôn chạy, đáy ngay trên thanh thời gian (y 1374) | như dọc (y 982) | `kieu-phu-de.js`, `khung().capBottom` |
| Màn chốt (`cta`) | câu nguyên văn tối đa 55 ký tự, tick + "ting" | như dọc, ô video 50 % bề ngang, ẩn dấu góc | `keu-goi-hanh-dong.js`, `hanh-dong.jsx` / `chuong-trinh.jsx` |
| Thẻ cuối | chỉ video dọc dài: nhận diện / dẫn về bản đầy đủ | nhận diện (chủ đề + DAVID) | `than-man-ket.jsx` |
| Màn kết YouTube (video dài) | — | 15–20 s, khung chừa 2 video + nút đăng ký | `man-ket-youtube.jsx` |

Chủ đề ở dấu góc: `project.topic` (1 video), `show.name` (vlog), tên chương trình (podcast), tên tập gốc (highlight).
Mẫu tiêu đề: dòng nhỏ cam → gạch cam → chữ cô đặc in hoa trắng, dòng nhấn cam.

Luật kèm theo:
- **Không dùng logo nền tảng, không dùng nút phát đỏ** ở bất kỳ thẻ nào.
- Mọi lớp phủ góc trên nằm **dưới** `brand.bottom` (`BRAND_BOT`); mọi lớp phủ đáy nằm **trên** phụ đề và thanh thời gian. Không dùng
  số vị trí của khung dọc cho khung ngang.
- **Video dọc ngắn** (Reels/TikTok/Shorts — dọc tối đa 90 s, mọi highlight, podcast dọc trích ngắn): **không có thanh thời gian, không có thẻ
  cuối**; màn chốt hiện câu nguyên văn ngay trên khung hình (không thu nhỏ video), video kết thúc ở chữ cuối để tự lặp lại. Lý do: nền tảng đã
  có thanh riêng, "còn 0:20" và màn "hết rồi" khiến người xem lướt đi, thẻ cuối làm ngắt vòng lặp. Phần dẫn về bản đầy đủ / mời bình luận
  đặt ở caption và bình luận ghim. Công cụ tự nhận biết (`nganDoc()` trong `nhan-dien-thuong-hieu.js`, `NGAN_DOC` trong `thanh.js`).
- Chỉ định thủ công: thanh thời gian `project.thanh` / thẻ cuối `project.theCuoi` (mẫu 1 video, podcast) · `export const THANH` /
  `THE_CUOI` (danh-sach-cat.js mẫu ghép).
- Highlight có thanh của cả tập gốc (`HL.bar`) thì thanh đó thay thế thanh thường, cùng vị trí.

## 2. Phần tự do (motion graphics)

Bố cục và hiệu ứng bên trong video (thẻ, chữ to, minh hoạ, sơ đồ, người vào ô, màn chương, điểm nhấn trên người…) được chọn theo nội dung,
theo danh mục `../thiet-ke-bo-cuc/bo-cuc.md`. Tự do về **cái gì, lúc nào**; không tự do về **vị trí các thành phần cố định** ở mục 1.

**Chữ nhấn trên người nói** (`pow`, kể cả thẻ tiêu đề mở đầu): không chạm vào mặt, không dùng nền tối mờ phủ hình, vì chữ chồng lên mặt và nền
đen mờ làm mất thẩm mỹ. Kiểu chuẩn là **nhãn dán**: mỗi dòng một nhãn đặc màu (dòng trước nền trắng chữ sẫm, dòng cuối nền cam chữ
trắng), căn đáy theo đáy dải phụ đề (lúc này phụ đề nhường), khối chữ nằm ở vùng ngực, bụng, xa cằm. Code: `Pow` trong mẫu ghép `chuong-trinh.jsx`.

## 3. Sửa bộ nhận diện

1. Sửa đúng một chỗ trong thư mục này (không viết số vị trí riêng trong mẫu dựng).
2. Chụp kiểm cả khung ngang lẫn dọc, mỗi loại một dự án đã duyệt: podcast ngang (`tap-di-trainer/2-ban-day-du`), clip podcast dọc
   (`tap-di-trainer/3-doan-noi-bat/clip-A`), video người nói ngang (`tap-su-tap-trung/2-ban-day-du`, `tap-di-bo-hang-ngay/2-ban-day-du`),
   clip người nói dọc (`tap-*/3-doan-noi-bat/clip-A` của 4 video cũ).
3. Push lên GitHub.

## 4. Còn thiếu (ghi lại để không quên)

- **Mẫu ghép khung ngang:** vùng an toàn, dấu góc, thanh thời gian, phụ đề, màn chốt (ô video 50 % bề ngang), `pow` (`x`) và thẻ `title`
  `over` đã kiểm ở highlight ngang `tap-marketing-noi-dau-nhu-cau`. Thẻ địa điểm, thẻ tên, thẻ cuối vẫn đặt số theo khung dọc, chưa kiểm;
  khi làm vlog ngang đầu tiên thì chụp kiểm kỹ và sửa các thành phần đó theo `khung()`.
