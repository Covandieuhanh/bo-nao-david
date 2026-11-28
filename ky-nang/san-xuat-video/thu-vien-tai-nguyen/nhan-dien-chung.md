---
description: "Bộ nhận diện chung của mọi loại video: vị trí, thành phần cố định, ngôn ngữ thiết kế."
---

# Bộ nhận diện chung — mọi loại video

**Mọi loại video có cùng tiêu chuẩn** (vị trí, thành phần cố định, ngôn ngữ thiết kế). Chỉ **motion graphics** là tự do chọn theo loại
video và theo từng cảnh. Nguồn code duy nhất: `nhan-dien-thuong-hieu.js` (`khung(W, H)`), `dau-goc.jsx`, `thanh-thoi-gian.jsx`, `than-man-ket.jsx`,
`bien-thiet-ke.js`, `thuong-hieu.json`, `kieu-phu-de.js`, `keu-goi-hanh-dong.js`, `bieu-tuong.jsx`. Mẫu 1 video, podcast, ghép vlog, highlight đều đọc ở đây.

## 0. Chữ ký nhận diện — phần thẩm mỹ phải giữ

> "Về thẩm mỹ thì tôi chỉ cần duy nhất 1 thứ là người xem có thể nhận diện được dù xem video nào cũng là của cùng 1 người làm." — David

Người dựng giữ ở MỌI video:
1. Các thành phần cố định ở mục 1 (dấu góc ● DAVID, phụ đề, thanh thời gian, màn chốt, thẻ cuối) — đúng vị trí, đúng kiểu, hai font chính
   `HEAD` (Barlow Condensed) / `BODY` (Be Vietnam Pro), nhạc kênh (`bien-thiet-ke.js`, `thuong-hieu.json`). Người xem nhận ra kênh nhờ
   hình thức và vị trí của các thành phần này, không nhờ một màu riêng.
2. **Màu không phải nhận diện** (David 28/11/2026: *"nhận diện của kênh không nhất thiết phải là màu cam với nền đen hay nền trắng đâu nhé.
   dùng bất kì màu sắc nào cũng được"*). Không ép cam, nền đen hay nền trắng vào hiệu ứng nào.
3. **Đã học từ hình mẫu thì mọi thứ đúng theo hình mẫu, cả hiệu ứng lẫn motion graphics** (David 28/11/2026: *"đã học từ hình mẫu
   thì mọi thứ chuẩn đúng theo hình mẫu ở cả hiệu ứng và cả motion graphics nhé. Sau đó thì giá trị của bạn nằm ở phân tích những thứ đã
   học đó để cho áp dụng vào chuẩn phù hợp với nội dung mà video đang nhắc đến thôi. đừng sáng tạo và thêm linh tinh nữa"*). Giữ đúng
   màu nền, màu chữ, màu nhấn, font, cỡ và tỉ lệ chữ, bo góc, bóng, khoảng trống, bố cục, vị trí so với người, thứ tự hiện, chuyển động,
   nhịp của chính mẫu đó (số đo ở `thiet-ke-bo-cuc/nguon-tham-khao/`, giao diện ở `bien-thiet-ke.js` `GIAO_DIEN`). Không thêm chi tiết mẫu
   không có (mảng tối giả, lưới, cách xếp khác, viền, quầng sáng), không phối màu lại. Font của mẫu không có trên máy thì dùng font gần
   nhất cùng nhóm và ghi trong phiếu học — đó là chỗ duy nhất được thay.
   **Vì sao** (David 28/11/2026): *"khi học từ hình mẫu thì thẩm mỹ chuẩn hơn, khi tự xây dựng thì thẩm mỹ hay bị các lỗi nhỏ"*.
   Mẫu đã được kiểm qua người xem thật; phần tự dựng chưa ai kiểm nên lỗi nhỏ lọt qua.
4. **Giá trị của Claude là phân tích và chọn**: đọc nội dung đang nói, chọn đúng hiệu ứng đã học hợp với nội dung đó, đặt đúng lúc, đúng
   chỗ trống. Nội dung không có hiệu ứng mẫu nào hợp thì giữ người và phụ đề, không tự chế hiệu ứng mới. Mẫu đòi điều kiện mà cảnh không có
   (ví dụ nét phấn trắng cần tường tối) thì chọn hiệu ứng khác, không sửa mẫu cho vừa. Font phụ `NHAN` chỉ dùng cho **một từ nhấn** khi
   mẫu có kiểu nhấn đó.

Nhận diện kênh nằm ở phần cố định: che hiệu ứng đi, người xem quen kênh vẫn nhận ra là video của David nhờ dấu góc, phụ đề, thanh thời gian,
màn chốt và nhạc. Không có phần "tự do sáng tạo" ở hiệu ứng: chỉ chọn trong những gì đã học từ mẫu. **Ngoại lệ tạm:** video podcast (`dung-podcast`)
giữ sơ đồ và minh hoạ hiện có cho tới khi học được mẫu podcast, hoặc có mẫu khác thay thế được (David 28/11/2026).

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
- **Video dọc ngắn** (Reels/TikTok/Shorts — dọc tối đa 90 s, mọi highlight khung dọc, podcast dọc trích ngắn): **không có thanh thời gian, không có thẻ
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
