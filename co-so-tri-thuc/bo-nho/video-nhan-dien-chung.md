---
name: video-nhan-dien-chung
description: "Mọi loại video cùng một bộ nhận diện; video dọc ngắn bỏ thanh và thẻ cuối; chữ nhấn kiểu nhãn dán đặc màu ở ngực, không chạm mặt, không nền đen mờ (08/11, 10/11, 13/11; gộp 15/11)"
metadata:
  type: feedback
---

Mọi loại video (1 video người nói, podcast, ghép vlog, highlight; ngang hay dọc) dùng chung một bộ nhận diện: vùng an toàn, dấu góc
● DAVID góc trên trái, thanh thời gian ở đáy, phụ đề trên thanh, màn chốt, thẻ cuối không nút phát, không logo nền tảng. Chỉ motion
graphics là tự do chọn theo loại video, theo từng cảnh.

**Video dọc ngắn** (dọc ≤ 90 s, mọi highlight, podcast dọc trích ngắn — 10/11/2026): **không thanh thời gian, không thẻ cuối**; màn chốt
là ô câu nguyên văn nằm trên khung hình (không thu nhỏ video), kết ở chữ cuối để video tự lặp. Dẫn về bản đầy đủ, mời bình luận để ở
caption + bình luận ghim. Video ngang và dọc dài giữ thanh, thẻ cuối, màn kết YouTube.

**Why:**
- 08/11/2026 David thấy video dài thiếu thanh thời gian, dấu góc lệch; rà ra thì mỗi khuôn dựng tự viết nhận diện riêng nên sửa một chỗ
  không đổi chỗ khác. David chọn gom về một chỗ: "đã nói là cho các loại có những tiêu chuẩn giống nhau mà".
- 10/11/2026 David thấy nên bỏ thanh và thẻ cuối ở dọc ngắn; Claude phân tích: nền tảng đã có thanh riêng, "còn 0:20" khiến người xem
  lướt, màn "hết rồi" và thẻ cuối làm đứt vòng lặp Shorts/Reels. Kênh chưa có số liệu video ngắn — kiểm lại sau 3–4 video (khối 16: tỉ
  lệ xem hết, giây rời).
- Gộp ghi nhớ `video-doc-ngan-khong-thanh` vào đây ở tái bản 2 (10/11/2026).

**How to apply:** vị trí chỉ lấy từ `ky-nang/san-xuat-video/thu-vien-tai-nguyen/nhan-dien-thuong-hieu.js` (`khung(W, H)`), thành phần `dau-goc.jsx`,
`thanh-thoi-gian.jsx`, `than-man-ket.jsx`; bảng ở `thu-vien-tai-nguyen/nhan-dien-chung.md`; nhà luật dọc ngắn `quy-tac-chung.md` mục 5, máy tự nhận
`nganDoc()` / `NGAN_DOC` (`thanh.js`). Không viết số vị trí riêng trong khuôn dựng. Sửa nhận diện → chụp kiểm cả ngang lẫn dọc trên dự
án đã duyệt. Liên quan [[quy-tac-hoc-la-bo-sung]], [[video-bo-cuc-tu-can]], [[video-doc-khuon-chu-chinh]], [[video-tham-my-chi-giu-nhan-dien]].

## Gộp từ `video-nhan-dien-chung` (15/11/2026, tự học tuần: giảm ghi nhớ về 40)

13/11/2026, clip A "Quy chuẩn, hợp pháp" (tap-giao-dich-hang-hoa): David: "không thích phần chữ mô tả bị dính vào mặt của nhân vật và lại còn có nền đen mờ, rất mất thẩm mỹ, chuyển hẳn sang kiểu khác".

**Why:** chữ to cũ (`pow`) canh đáy trên dải phụ đề nên hai dòng chữ cỡ 150 lên tới cằm, kèm dải tối mờ (Scrim) phủ nửa khung.

**How to apply:** luật ở `ky-nang/san-xuat-video/thu-vien-tai-nguyen/nhan-dien-chung.md` mục 2. Kiểu chuẩn là nhãn dán: mỗi dòng một nhãn đặc (trắng chữ sẫm, dòng cuối cam chữ trắng), canh đáy vào đáy dải phụ đề (phụ đề nhường), không Scrim; `pow` không bị lưới chặn dải phụ đề cắt. Code: `Pow` trong `dung-video-theo-phong-cach/assets/khuon-dung-ghep/src/chuong-trinh.jsx`. Chụp thử luôn soát khoảng cách chữ ↔ cằm. Liên quan [[video-phu-de-mot-cho-chu]], [[video-bo-cuc-tu-can]].
