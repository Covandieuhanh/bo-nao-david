---
description: "Quy trình lá B14: dựng intro thương hiệu DAVID TRẦN (khung ngang, 12–15 giây, sang trọng kiểu intro diễn giả) từ thư mục tư liệu quay ngang, nhạc tiếng Anh có lời giấy phép CC BY, cắt theo phách, chốt tên trên nền đen."
---

# Intro thương hiệu DAVID TRẦN (cây quy trình lá B14)

**Khi nào dùng:** David muốn một đoạn intro riêng đặt đầu video dài, từ thư mục tư liệu.
Bản hiện hành làm 23/11/2026 (việc #41, bản 4): `~/Movies/cho-dang/tap-intro-david-tran-2311/ban-dai/intro-david-tran.mp4`,
Drive `thanh-pham/` cùng tên. Khuôn code: `assets/khuon-intro/`.

**Đầu vào:** link thư mục Drive (lá B2 tải về `~/Movies/tap-<tên>/1-goc/`) · chữ trên intro (mặc định chỉ tên **DAVID TRẦN**: chữ trên
video chỉ lấy từ David).

## Lời David đã chốt (23/11/2026)
- "Bỏ các hình ảnh ngoài đường phố với nhiều đối tượng gây nhiễu, chỉ giữ lại các hình ảnh chất lượng và sang trọng thôi."
- "Ghép các cảnh ngang thôi" (không làm bản dọc, không dùng video quay dọc).
- Nhạc tiếng Anh có lời, không vi phạm bản quyền. Logo tổ chức khác (DFS) thì tránh.
- "Đưa nhân vật làm trung tâm nhé. Các cảnh cần hiển thị được toàn cảnh để thể hiện được tính chất sân khấu và năng lực chia sẻ của tôi."
- "Có rất nhiều cảnh mà. Đan xen thêm nhé, không cảnh nào lấy lại 2 lần cả." · "Intro cần ấn tượng nên thẩm mỹ là quan trọng nhất."
  Được dùng cảnh quay dọc khi cảnh đó đắt (sân khấu, ký kết, đứng bảng giảng): đặt giữa khung ngang, mỗi cảnh một lần.

## Nguyên lý học từ intro diễn giả cùng lĩnh vực
Mẫu đã học 23/11: John Sanei, Jacob Brown, Tony Robbins Australia (quốc tế); Trần Hồng Hải, Ngô Bích Hà, TS. Khiêm Nguyễn (Việt Nam).
1. **Sang trọng nằm ở màu và sự tiết chế:** màu điện ảnh tối, ấm, ít màu, viền tối nhẹ, hạt phim rất nhẹ, khung 2,35:1. Ít cảnh nhưng
   cảnh nào cũng đẹp. Tránh khuôn rối mắt (hạt lấp lánh, hình khối dồn dập, chữ chạy liên tục) như các mẫu Việt kiểu cũ.
2. **Nhân vật làm trung tâm, cảnh toàn:** David ở giữa khung hoặc là điểm nhìn chính; cảnh rộng thấy cả không gian (sân khấu sự kiện,
   phòng đào tạo có học viên đang nghe, phòng thu talk show, buổi chia sẻ) để người xem thấy năng lực đứng lớp, chia sẻ. Khoảnh khắc thật:
   đang nói trước người khác, ngồi viết, chào người xem. Cảnh quay bằng chân máy đẹp hơn cảnh tự
   cầm máy; cảnh tự quay chỉ để ở đoạn cắt nhanh.
3. **Nhịp theo nhạc, có lớp, mỗi cảnh một lần:** mở chậm (2 cảnh toàn, mỗi cảnh 4 phách, máy đẩy chậm vào) → giữa (8 cảnh, mỗi cảnh
   2 phách, đan xen nơi chốn khác nhau) → cao trào (cảnh sân khấu lớn nhất, 4 phách, đẩy vào gần David) → cảnh chào (4 phách) → tên.
   Một nơi quay chỉ lấy một khoảnh khắc; thiếu cảnh thì kéo dài cảnh, không lặp. Vệt sáng ấm lóe qua ở các điểm nhấn của nhạc và lời.
4. **Chốt tên kiểu diễn giả:** nền đen ấm, DAVID TRẦN chữ HEAD giãn rộng rồi khép dần, hai vạch cam mảnh mở từ giữa, một vệt sáng quét
   qua chữ. Tên hiện đúng chữ đắt nhất của lời bài hát.

## Các bước
1. **Tải + xem cảnh:** lá B2. Album Google Photos chia sẻ: tải trang album (`curl -L <link>`), lấy các đường
   `https://lh3.googleusercontent.com/pw/...` (giữ thứ tự, bỏ trùng), tải từng mục bằng đuôi `=dv` (video gốc), đặt tên theo thứ tự. Xem nhanh bằng ảnh lưới nhảy thẳng tới mốc thời gian (`ffmpeg -ss <giây> -i <file> -frames:v 1`; đừng dùng
   bộ lọc `fps` trên video dài vì phải giải mã cả file). Bỏ video quay dọc hay nằm nghiêng, video đã dựng có chữ in trong hình, thư mục
   thử máy, cảnh đường phố, cửa hàng, ô tô, điện thoại đặt trên bàn.
2. **Chọn khoảng 15 đoạn** theo nguyên lý 2, ghi vào `danh-sach-canh.txt` (mẫu trong khuôn). Logo tổ chức khác: `bo-logo` (cắt mép)
   hoặc chọn đoạn khác, soát từng khung vì máy cầm tay làm logo trôi vào mép. Quán đông người phía sau: `phai` (lấy 2/3 bên phải).
   Cảnh quay dọc: `doc` (logo trên vách thì `doc-bo-tren`), đánh dấu `true` ở cột dọc của bảng `CANH` (cao trào: `'gan'`): khuôn tự đặt
   cảnh nét cao 980 điểm ảnh giữa khung, vượt lên trên hai dải đen, nền là chính cảnh đó phóng to, mờ, tối.
3. **Nhạc có lời, giấy phép rõ:** dùng `cat-doan-noi-bat/assets/nhac/intro-co-loi-1.mp3` (README kho nhạc có đoạn dùng, nhịp, câu ghi
   nguồn). Cần bài mới thì:
   - Pixabay, ccMixter, trang riêng của tác giả chặn máy tải (bước xác minh chống máy, trang báo cấm); Free Music Archive bắt đăng nhập
     mới cho tải. Không tìm cách vượt qua các bước này.
   - Internet Archive cho tải thẳng: `https://archive.org/advancedsearch.php?q=creator%3A(<tên>)&fl[]=identifier&fl[]=licenseurl&output=json`
     → `https://archive.org/metadata/<identifier>` → `https://archive.org/download/<identifier>/<tên file>`. Chỉ nhận giấy phép
     CC BY (không nhận NC: cấm thương mại; không nhận ND với bài sẽ cắt).
   - Chép lời bằng `whisper-cli -m ~/whisper-models/ggml-large-v3-turbo.bin -l en` để chắc có lời tiếng Anh hợp nghĩa (bỏ lời về rượu,
     tình yêu đôi lứa, chuyện buồn); chép từng chữ (`-ml 1 -sow`) trên đoạn định dùng để lấy mốc chữ đắt nhất.
   - Đo nhịp và pha trên đoạn đó, kiểm lại bằng mốc chữ (chữ đắt phải rơi đúng phách), rồi chọn điểm bắt đầu cách điểm chốt một số
     phách chia hết cho 4.
   - Ghi câu ghi nguồn vào `ghi-nguon-nhac.txt` cạnh bản cuối; mọi video dùng intro phải ghi câu đó ở mô tả.
4. **Cắt đoạn:** `bash assets/khuon-intro/cat-canh.sh <thư mục 1-goc> <danh-sach-canh.txt> <dự án>/public/canh` (màu điện ảnh chung đã
   nằm trong script).
5. **Dự án dựng:** chép `assets/khuon-intro/` vào `~/Movies/tap-<tên>/3-du-an/`, `npm ci`; cắt đoạn nhạc vào `public/nhac-intro.wav`
   (`ffmpeg -ss <đầu> -t <dài> -i <bài> -af "afade=t=in:d=0.12,afade=t=out:st=<dài-0,75>:d=0.75" -ar 48000`), chép
   `hieu-ung-am-thanh/sting.wav` vào `public/`. Đổi bài thì sửa `NHIP`, `TONG`, `TEN`, bảng `CANH`, `VET_SANG` trong `src/Intro.jsx`.
6. **Chụp thử khung then chốt** rồi tự soát: `npx remotion still src/index.jsx IntroNgang <ra.jpg> --frame=<n> --scale=0.33`.
7. **Xuất + cân âm:** `npx remotion render src/index.jsx IntroNgang <thô.mp4> --codec=h264 --crf=16`, rồi
   `ffmpeg -i <thô.mp4> -c:v copy -af loudnorm=I=-14:TP=-1.5:LRA=11 -ar 48000 -c:a aac -b:a 256k -movflags +faststart <ban-cuoi>.mp4`.
8. **Giao:** chép vào `~/Movies/cho-dang/<tập>/ban-dai/` (kèm `ghi-nguon-nhac.txt`), `zsh scripts/cho-dang.sh gui <tập>`, gửi file cho
   David. Học mẫu xong thì xoá video mẫu đã tải.

## Điểm duyệt
Đ1 trước khi chọn cảnh (chữ, độ dài, khung, logo, nguồn nhạc). Góp ý sau khi giao là lời duyệt cho chính thay đổi đó (lá B13).

## Xong khi
- Bản cuối 1920×1080, 12–15 giây, khoảng −14 LUFS, ở Chờ đăng và Drive `thanh-pham/` đã lên mây, kèm `ghi-nguon-nhac.txt`.
- Soát 16 khung đều: David là trung tâm ở mọi cảnh (kể cả từng khung của cảnh chào cuối, vì người cầm máy hay đi lệch), không cảnh đường
  phố hay người lạ gây nhiễu, không lộ logo tổ chức khác, tên hiện đúng chữ đắt của lời bài hát.

## Kiểm gì
- Mọi đoạn đúng chiều (video iPhone có xoay −90 / −180 vẫn đứng thẳng sau khi cắt).
- Chớp sáng lúc hiện tên không trắng toá cả khung (độ mờ tối đa khoảng 0,55).

## Lỗi hay gặp
- Shell zsh không tách chữ khi `set -- $bien`: chạy vòng lặp đọc danh sách bằng bash (script đã làm vậy).
- File DJI có nhiều luồng hình (bản xem trước 1280×720): luôn `-map 0:v:0`.
- Mốc whisper ở đoạn điệp khúc lặp nhiều lần hay bị ảo: lấy mốc bằng cách chép từng chữ trên đoạn ngắn đã cắt riêng.
