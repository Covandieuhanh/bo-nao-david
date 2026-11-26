---
name: video-nhan-dien-chung
description: "Mọi loại video dùng chung một bộ nhận diện; video dọc ngắn bỏ thanh thời gian và thẻ cuối; chữ nhấn theo kiểu nhãn dán đặc màu ở vùng ngực, không chạm mặt, không có nền đen mờ (08/11, 10/11, 13/11; gộp 15/11)"
metadata:
  type: feedback
---

Mọi loại video (1 video người nói, podcast, ghép vlog, highlight; ngang hay dọc) dùng chung một bộ nhận diện: vùng an toàn, dấu góc
● DAVID ở góc trên bên trái, thanh thời gian ở đáy, phụ đề nằm trên thanh, màn chốt, thẻ cuối không có nút phát, không có logo nền tảng. Chỉ motion
graphics được tự do chọn theo loại video và theo từng cảnh.

**Video dọc ngắn** (video dọc tối đa 90 s, mọi highlight, podcast dọc trích ngắn — 10/11/2026): **không thanh thời gian, không thẻ cuối**; màn chốt
là ô chứa câu nguyên văn nằm trên khung hình (không thu nhỏ video), kết thúc ở chữ cuối để video tự phát lặp lại. Lời dẫn về bản đầy đủ và lời mời bình luận được đặt ở
caption và bình luận ghim. Video ngang và video dọc dài giữ thanh thời gian, thẻ cuối và màn kết YouTube.

**Why:**
- Ngày 08/11/2026 David thấy video dài thiếu thanh thời gian, dấu góc bị lệch; khi rà soát, Claude thấy mỗi mẫu dựng tự viết nhận diện riêng nên sửa một chỗ
  thì chỗ khác không đổi theo. David chọn gom về một nguồn duy nhất: "đã nói là cho các loại có những tiêu chuẩn giống nhau mà".
- Ngày 10/11/2026 David thấy nên bỏ thanh thời gian và thẻ cuối ở video dọc ngắn; Claude phân tích: nền tảng đã có thanh riêng, "còn 0:20" khiến người xem
  lướt qua, màn "hết rồi" và thẻ cuối làm đứt vòng lặp Shorts/Reels. Kênh chưa có số liệu video ngắn; Claude kiểm tra lại sau 3–4 video (khối 16: tỉ
  lệ xem hết, giây người xem rời đi).
- Ghi nhớ `video-doc-ngan-khong-thanh` được gộp vào đây ở lần tái bản 2 (10/11/2026).

**How to apply:** vị trí chỉ được lấy từ `ky-nang/san-xuat-video/thu-vien-tai-nguyen/nhan-dien-thuong-hieu.js` (`khung(W, H)`), các thành phần `dau-goc.jsx`,
`thanh-thoi-gian.jsx`, `than-man-ket.jsx`; bảng nằm ở `ky-nang/san-xuat-video/thu-vien-tai-nguyen/nhan-dien-chung.md`; nguồn luật cho video dọc ngắn là `quy-tac-chung.md` mục 5, hệ thống tự nhận diện bằng
`nganDoc()` / `NGAN_DOC` (`thanh.js`). Claude không viết số vị trí riêng trong mẫu dựng. Khi sửa nhận diện, Claude chụp ảnh kiểm tra cả khung ngang lẫn khung dọc trên dự
án đã duyệt. Liên quan [[quy-tac-hoc-la-bo-sung]], [[video-bo-cuc-tu-can-bang]], [[video-doc-mau-chu-chinh]], [[video-tham-my-chi-giu-nhan-dien]].

## Gộp từ `video-nhan-dien-chung` (15/11/2026, vòng tự học hằng tuần: giảm số ghi nhớ xuống 40)

Ngày 13/11/2026, ở clip A "Quy chuẩn, hợp pháp" (tap-giao-dich-hang-hoa), David nhận xét: "không thích phần chữ mô tả bị dính vào mặt của nhân vật và lại còn có nền đen mờ, rất mất thẩm mỹ, chuyển hẳn sang kiểu khác".

**Why:** kiểu chữ to cũ (`pow`) căn đáy trên dải phụ đề nên hai dòng chữ cỡ 150 chạm tới cằm, kèm dải tối mờ (Scrim) phủ nửa khung hình.

**How to apply:** luật nằm ở `ky-nang/san-xuat-video/thu-vien-tai-nguyen/nhan-dien-chung.md` mục 2. Kiểu chuẩn là nhãn dán: mỗi dòng là một nhãn đặc màu (nền trắng chữ sẫm, dòng cuối nền cam chữ trắng), căn đáy vào đáy dải phụ đề (phụ đề nhường chỗ), không có Scrim; `pow` không bị lưới chặn dải phụ đề cắt. Mã nguồn: `Pow` trong `dung-video-theo-phong-cach/assets/mau-dung-ghep/src/chuong-trinh.jsx`. Khi chụp thử, Claude luôn kiểm khoảng cách giữa chữ và cằm. Liên quan [[video-phu-de-mot-cho-chu]], [[video-bo-cuc-tu-can-bang]].

Gốc: khối 1 (Bóc tách) của tu-duy-goc.md — tách rõ phần nhận diện giữ cứng chung cho mọi video với phần motion graphics tự do, nên người xem luôn nhận ra là của David.
