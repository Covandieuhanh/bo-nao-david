---
description: "Quy trình lá B5: dựng một đoạn thử ngắn để David xem cách trình bày mới trước khi dựng cả video (không render lại cả video)."
---

# Đoạn thử trước khi dựng cả video (cây quy trình lá B5)

**Khi nào dùng:** David nói "render một đoạn ngắn cho tôi xem", "đừng render cả video vội"; hoặc vừa đổi luật thẩm mỹ, kiểu cảnh lớn mà
video dài (đủ dài để dựng cả bản tốn nhiều công, Claude tự cân) — dựng đoạn thử trước, David duyệt rồi mới dựng cả video.

**Đầu vào:** dự án gốc đã làm sạch, đã có phụ đề soát chữ (`tu-lieu/video-goc.mp4`, `chuyen-dong/src/phu-de.js`).
Trong các lệnh dưới: `SKILL=~/Documents/bo-nao-david/ky-nang/san-xuat-video/dung-video-theo-phong-cach`.

## Các bước
1. **Chọn đoạn ngắn trọn vẹn ý, thấy rõ thay đổi nhất** (không cố định số giây, thường 1–2 phút — `quy-tac-chung.md` mục 8): đoạn dày ý, có nhiều ý cần hình liền nhau (để thấy được nhiều cách trình bày và chuyển
   cảnh khác nhau). Mốc đầu / cuối đúng đầu / cuối câu trong phụ đề.
2. **Cắt thành dự án thử:** kế hoạch tách một video, tên bắt đầu `thu-`, chạy
   `python3 -I $SKILL/scripts/tach-video.py ke-hoach-thu.json` (`references/tach-theo-huong.md` mục 3) — ra `~/Movies/tap-thu-<tên>/`.
3. **Dựng như video thật:** chẩn đoán, mở kho hình mẫu chọn cách cho từng ý, ghi `Nguồn kho:` (`thiet-ke-bo-cuc/huong-dan-lua-chon.md` bước 4d);
   mỗi cảnh ghi nguồn trong `canh.js`; đổi hiệu ứng vào / ra qua các cảnh.
4. **Soát:** `soat-canh.mjs` → `anh-kiem-canh.sh` → xem lưới ảnh: không che ai, chữ đọc được; sửa rồi chụp lại.
5. **Render đoạn thử:** `xuat-video.mjs` → `xem-truoc-ban-dung.py` (không teaser); làm bản nhẹ dưới 30 MB.
6. **Gửi David** bản nhẹ + bảng ngắn "giây · cảnh · cách làm · học từ đâu · hiệu ứng vào", rồi dừng chờ David duyệt hoặc góp ý.
   Góp ý thì sửa skill đúng chỗ và làm lại đoạn thử; duyệt thì mới dựng cả video với cách đã duyệt.

## Điểm duyệt
- **Đ1** trước khi làm (4 phần: đoạn nào, cách trình bày dự kiến).
- **Dừng sau bước 6**, chờ David duyệt đoạn thử; chưa duyệt thì không dựng cả video. Chế độ tự chạy (David nói rõ) thì không dừng ở đây.

## Xong khi
- David nhận đoạn thử (bản nhẹ dưới 30 MB) kèm bảng cảnh, và đã nói duyệt hay sửa.
- Cả video chưa bị render lại khi David chưa duyệt đoạn thử.

## Kiểm gì
- Mỗi cảnh một cách khác nhau lấy từ kho (trừ ý giống nhau), có tên nguồn.
- Âm lượng đạt chuẩn khối 09 (−14 LUFS) như video thật.
