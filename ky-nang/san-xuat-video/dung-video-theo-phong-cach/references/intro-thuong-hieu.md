---
description: "Quy trình lá B14: dựng intro thương hiệu DAVID TRẦN (10–15 giây, khung ngang, sôi động) từ nhiều video quay ngang, cắt theo nhịp nhạc, ba hồi, chốt tên."
---

# Intro thương hiệu DAVID TRẦN (cây quy trình lá B14)

**Khi nào dùng:** David muốn một đoạn intro riêng (tên, hình ảnh, năng lượng) đặt đầu video dài, từ một thư mục tư liệu quay ngang.
Bản đầu làm 23/11/2026 (việc #41): `~/Movies/cho-dang/tap-intro-david-tran-2311/ban-dai/intro-david-tran.mp4`, Drive `thanh-pham/` cùng tên.

**Đầu vào:** link thư mục Drive (lá B2 tải về `~/Movies/tap-<tên>/1-goc/`) · chữ trên intro (mặc định chỉ tên **DAVID TRẦN**: chữ trên
video chỉ lấy từ David) · độ dài (mặc định 12 giây).

## Các bước
1. **Tải + xem cảnh:** lá B2. Xem nhanh mỗi video bằng ảnh lưới nhảy thẳng tới mốc thời gian (`ffmpeg -ss <giây> -i <file> -frames:v 1`,
   đừng dùng bộ lọc `fps` trên video dài: phải giải mã cả file, rất chậm). Bỏ video quay dọc hay quay nằm nghiêng (David 23/11: "ghép
   các cảnh ngang thôi"), bỏ video đã dựng sẵn có phụ đề in trong hình, bỏ thư mục thử máy.
2. **Chọn khoảng 15 đoạn** theo ba ý người xem cần thấy: lịch sự (sơ mi, cà vạt, ngồi viết sổ) · đi gặp, chia sẻ bên ngoài (quán cà phê,
   cửa hàng của khách) · kết nối (làm cùng đội, gọi video cho khách, vẫy tay chào). Ưu tiên khoảnh khắc có động tác (vẫy tay, giơ tay
   khi nói). Ghi vào `danh-sach-canh.txt` (mẫu: `assets/khuon-intro/danh-sach-canh.txt`).
3. **Logo tổ chức khác** (ví dụ chữ DFS trên tường văn phòng): mặc định tránh, hỏi David ở 4 phần. Tránh bằng `bo-logo` (cắt mép rồi
   phóng lại) hoặc chọn đoạn khác; soát từng khung của đoạn đó, vì máy quay cầm tay làm logo trôi vào mép.
4. **Cắt đoạn:** `bash assets/khuon-intro/cat-canh.sh <thư mục 1-goc> <danh-sach-canh.txt> <dự án>/public/canh`.
5. **Dự án dựng:** chép `assets/khuon-intro/` vào `~/Movies/tap-<tên>/3-du-an/`, `npm ci`, chép nhạc `cat-doan-noi-bat/assets/nhac/intro-soi.mp3`
   và `hieu-ung-am-thanh/{sting,tua}.wav` vào `public/`. Đổi bài nhạc thì đo lại nhịp và pha, sửa `NHIP`, `PHA` trong `Intro.jsx`.
6. **Ba hồi theo phách nhạc** (`src/Intro.jsx`): hồi 1 (phách 0–8) mỗi cảnh một phách hoặc nửa phách, đập vào bằng zoom, chớp trắng,
   vệt cam chéo · hồi 2 (phách 8–17) hai bộ ba ô chéo viền trắng, ô giữa viền cam, đường cam có chấm nối các ô = kết nối · hồi 3 (từ phách
   17, có tiếng sting) cảnh vẫy tay toàn khung, hai nhãn dán **DAVID** (nền trắng chữ sẫm) và **TRẦN** (nền cam chữ trắng), từng chữ nảy
   lên. Mỗi ô có số `fx` = chỗ mặt người theo chiều ngang (%): chỉnh cho ô không cắt mất David.
7. **Chụp thử khung then chốt** rồi tự soát: `npx remotion still src/index.jsx IntroNgang <ra.jpg> --frame=<n> --scale=0.35`
   (khung 3, 75, 140, 175, 230, 278, 300, 355).
8. **Xuất + cân âm:** `npx remotion render src/index.jsx IntroNgang <thô.mp4> --codec=h264 --crf=16`, rồi
   `ffmpeg -i <thô.mp4> -c:v copy -af loudnorm=I=-14:TP=-1.5:LRA=11 -ar 48000 -c:a aac -b:a 256k -movflags +faststart <ban-cuoi>.mp4`.
9. **Giao:** chép vào `~/Movies/cho-dang/<tập>/ban-dai/`, `zsh scripts/cho-dang.sh gui <tập>` (Drive `thanh-pham/`), gửi file cho David
   (dưới 30 MB gửi thẳng).

## Điểm duyệt
Đ1 trước bước 2 (4 phần: chữ trên intro, độ dài, khung, logo). Góp ý sau khi giao là lời duyệt cho chính thay đổi đó (lá B13).

## Xong khi
- Bản cuối 1920×1080, 10–15 giây, âm lượng khoảng −14 LUFS, nằm ở Chờ đăng và Drive `thanh-pham/` đã lên mây.
- Soát 16 khung đều: tên không chạm mặt, không lộ logo tổ chức khác, ô nào cũng thấy người.

## Kiểm gì
- Mọi đoạn đúng chiều (video iPhone có xoay −90 / −180 vẫn đứng thẳng sau khi cắt).
- Ô dọc hẹp ở hồi 2 dễ cắt mất người ngồi lệch một bên: soát lại sau khi đổi đoạn.

## Lỗi hay gặp
- Shell zsh không tách chữ khi `set -- $bien`: chạy vòng lặp đọc danh sách bằng bash (script đã làm vậy).
- File DJI có nhiều luồng hình (bản xem trước 1280×720): luôn `-map 0:v:0`.
