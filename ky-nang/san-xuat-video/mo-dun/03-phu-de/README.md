# Khối 03-phu-de: Phụ đề: dài = hộp tối đầy câu; ngắn = cụm 5–8 chữ cỡ bằng chữ thẻ, màu theo nghĩa; mỗi lúc một chỗ chữ

**Dùng trong:** cả 4
**Đầu vào:** kiem-tra/goc/moc-tung-tu.srt + ban-chep-loi.srt
**Đầu ra:** chuyen-dong/src/phu-de.js (1 video, podcast) · SUBS trong danh-sach-cat.js (ghép)
**Tham số hồ sơ:** chung: phu_de.*
**Sửa khối này → chạy lại:** 17 (render lại lớp phu-de)

**File thật (code, một bản duy nhất):**
- `dung-video-theo-phong-cach/scripts/phu-de.py`
- `dung-video-theo-phong-cach/assets/khuon-remotion/src/kieu-phu-de.js (một nguồn)`
- `dung-video-theo-phong-cach/assets/khuon-remotion/src/thanh-phan/phu-de.jsx`

## Cách làm

**Phụ đề đầy đủ** — luôn có: toàn bộ lời nói, đúng từng chữ, chạy suốt video. Kiểu phụ đề theo loại video: `quy-tac-chung.md` mục 3.
```bash
python3 -I $SKILL/scripts/phu-de.py "$P"          # kiem-tra/goc/moc-tung-tu.srt + ban-chep-loi.srt → chuyen-dong/src/phu-de.js (nháp)
```
Đọc lại TỪNG dòng trong `phu-de.js`, sửa tay:
- **Chính tả** lỗi Whisper (tên riêng, từ nghe nhầm như "tư giãn" → "thư giãn"). Giữ nguyên lời: không rút gọn, không
  diễn đạt lại, giữ cả "thì", "là", "cái".
- **Câu bị mất / câu bịa**: script bỏ câu kiểu "Hãy subscribe cho kênh…"; nếu chỗ đó người nói có nói thật (vd. "Xin chào"
  cuối video) thì đối chiếu `kiem-tra/lam-sach/ban-chep-loi.srt` (lần chạy khác) + `am-luong.txt` và thêm tay.
- **Chỗ ngắt dòng**: không tách đôi từ ghép ("chia | sẻ", "giải | trình"); ngắt trước từ nối (thì, là, nhưng, mà…).
Lớp motion graphic có chữ đang hiện → phụ đề ẩn đúng khoảng đó (phu-de.jsx `LOP`, chuong-trinh.jsx `nhuong`). Highlight: `danh-sach-cat-doan-noi-bat.py` chia dòng bằng quy hoạch động — ngắt ở hết câu / dấu phẩy / trước từ nối, không ngắt sau "rất, của, là, những…".
Phụ đề nằm trong dải 140 px ở **đáy vùng an toàn**; cảnh toàn màn hình chừa trống dải này (vị trí lớp phủ: khối 05). Render tự động
(`phu-de` → `phu-de.mov`, đè trên cùng ở bản cuối).

## Bảng tự sửa chữ (David tự sửa chữ, không tốn lượt Claude)
Áp dụng dự án có `chuyen-dong/src/canh.js` (làm video, podcast, clip podcast dọc). Dự án ghép (`danh-sach-cat.js`) chưa có: sửa qua Claude.
```bash
node $SKILL/scripts/chu-tren-man.mjs xuat "$P"            # → $P/chu-tren-man.txt: chữ từng cảnh, ý đang bàn, phụ đề
# David mở file, sửa phần sau dấu | rồi lưu
node $SKILL/scripts/chu-tren-man.mjs ap "$P"              # ghi vào canh.js / phu-de.js, tự soát cảnh, báo cảnh cần render
node $SKILL/scripts/chu-tren-man.mjs ap "$P" --render     # render đúng các cảnh chờ + xuất lại video-hoan-chinh.mp4
```
- Sao lưu ở `kiem-tra/truoc-sua-chu/`. Chữ đổi ở cả bảng lẫn kịch bản, dòng bị xoá / để trống, hoặc không xác định chắc chỗ sửa → **không ghi gì**, liệt kê để hỏi.
- Claude sửa kịch bản sau khi xuất bảng → xuất lại bảng. Phụ đề vẫn giữ đúng lời đã nói (luật "không bịa").
- Claude không tự chạy `--render` khi David chưa yêu cầu. Chỉ đổi chữ, không đổi mốc: chữ dài hơn nhiều thì chụp thử cảnh đó.
- Đồng bộ `hl` (từ tô màu của phụ đề) không tự đổi: sửa đúng từ đang tô thì nhờ Claude.
