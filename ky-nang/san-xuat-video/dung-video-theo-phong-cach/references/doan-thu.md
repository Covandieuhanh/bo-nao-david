---
description: "Quy trình lá B5: dựng một đoạn thử ngắn để David xem cách trình bày mới trước khi dựng cả video (không render lại cả video)."
---

# Đoạn thử trước khi dựng cả video (cây quy trình lá B5)

**Khi nào dùng:** David nói "render một đoạn ngắn cho tôi xem", "đừng render cả video vội"; hoặc khi vừa đổi luật thẩm mỹ, kiểu cảnh lớn mà
video dài (đủ dài để việc dựng cả bản tốn nhiều công sức, Claude tự cân nhắc) — Claude dựng đoạn thử trước, tự xem và soát, rồi dựng luôn cả video; chỉ dừng chờ khi David yêu cầu xem trước.

**Đầu vào:** dự án gốc đã làm sạch, đã có phụ đề được rà soát chữ (`tu-lieu/video-goc.mp4`, `chuyen-dong/src/phu-de.js`).
Trong các lệnh dưới: `SKILL=~/Documents/bo-nao-david/ky-nang/san-xuat-video/dung-video-theo-phong-cach`.

## Các bước
1. **Chọn đoạn ngắn trọn vẹn ý, thể hiện rõ thay đổi nhất** (không cố định số giây, thường 1–2 phút — `quy-tac-chung.md` mục 8): đoạn có mật độ ý cao, có nhiều ý cần hình liền nhau (để thấy được nhiều cách trình bày và chuyển
   cảnh khác nhau). Mốc đầu / cuối trùng với đầu / cuối câu trong phụ đề.
2. **Cắt thành dự án thử:** lập kế hoạch tách một video, tên bắt đầu bằng `thu-`, chạy
   `python3 -I $SKILL/scripts/tach-video.py ke-hoach-thu.json` (`references/tach-theo-huong.md` mục 3) — kết quả nằm ở `~/Movies/tap-thu-<tên>/`.
3. **Dựng như video thật:** chẩn đoán, mở kho hình mẫu để chọn cách trình bày cho từng ý, ghi `Nguồn kho:` (`thiet-ke-bo-cuc/huong-dan-lua-chon.md` bước 4d);
   mỗi cảnh ghi nguồn trong `canh.js`; thay đổi hiệu ứng vào / ra giữa các cảnh.
4. **Rà soát:** `soat-canh.mjs` → `anh-kiem-canh.sh` → xem lưới ảnh: không che ai, chữ đọc được; sửa rồi chụp lại.
5. **Render đoạn thử:** `xuat-video.mjs` → `xem-truoc-ban-dung.py` (không teaser); làm bản dung lượng nhỏ dưới 30 MB.
6. **Gửi David** bản dung lượng nhỏ + bảng ngắn "giây · cảnh · cách làm · học từ đâu · hiệu ứng vào", rồi dừng, chờ David duyệt hoặc góp ý.
   Khi có góp ý thì Claude sửa skill đúng chỗ và làm lại đoạn thử; khi được duyệt thì Claude mới dựng cả video với cách đã duyệt.

## Điểm duyệt
- Không có Đ1: Claude tự chọn đoạn thử thấy rõ thay đổi nhất, ghi đoạn nào và cách trình bày trong tin giao.
- **Dừng sau bước 6**, chờ David xem đoạn thử (David yêu cầu xem trước nên đây là chỗ dừng của lá); chưa duyệt thì không dựng cả video. Lời David nói rõ "làm luôn cả video" thì không dừng ở đây.

## Xong khi
- David nhận đoạn thử (bản dung lượng nhỏ dưới 30 MB) kèm bảng cảnh, và đã nói duyệt hay sửa.
- Cả video chưa bị render lại khi David chưa duyệt đoạn thử.

## Kiểm gì
- Mỗi cảnh dùng một cách trình bày khác nhau lấy từ kho (trừ các ý giống nhau), có tên nguồn.
- Âm lượng đạt chuẩn khối 09 (−14 LUFS) như video thật.
