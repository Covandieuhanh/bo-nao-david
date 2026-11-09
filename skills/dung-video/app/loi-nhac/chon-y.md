XEM HÌNH trước (công cụ Read, nếu có ảnh): lưới khung hình của video nguồn — để biết bối cảnh, người nói, chỗ trống trong khung, rồi chọn cho hợp hình thật.

Bạn cắt highlight cho David Trần: từ BẢN LỜI một video dài, TỰ chọn ý ra các clip ngắn dọc. Trả về MỘT JSON phương án. Không hỏi David chọn
đoạn (luật 12 của skill). Mốc nào cũng TRÍCH nguyên văn vài chữ liền nhau trong BẢN LỜI (máy tự tìm giây), không ghi số giây.

# Khuôn trả về
- `endcard`: {title: tên tập gốc (chữ của bản gốc — lấy từ TIÊU ĐỀ BẢN DÀI nếu có, ngắn gọn), speaker: "David Trần"}.
- `options`: mỗi clip một ý KHÁC NHAU, đạt đủ 4 câu chọn ý; clip A = mạnh nhất. Mỗi option: `id` (A, B, C…), `tit` (cụm NGUYÊN VĂN đắt
  nhất của clip, ≤ 8 chữ, cho thẻ tít mở), `layout` (kiểu bố trí lời kêu gọi), `chon_y` {boi_canh, y_tron, mang_ve, chua_lai} (mỗi câu
  1–2 dòng, trả lời đúng câu hỏi của bảng 4 câu), `pieces` = các câu theo THỨ TỰ PHÁT: {trich_dau (4–8 chữ đầu câu), trich_cuoi (3–8 chữ
  cuối câu), role (CHAM · BOICANH · BUOC · HANHDONG · KEUGOI · KETQUA · CHUYEN), tone ("soi" | "lang"), zoom? (cú chốt), cta? (câu dùng cho
  màn chốt), cta_text? (vế nguyên văn ≤ 55 ký tự của câu màn chốt, `**cụm**` tô nhấn)}.
- Không có câu kêu gọi / giao việc nguyên văn → không đặt `cta` (clip kết ở câu chốt ý, lặng 1 s, thẻ cuối — luật 4).
- `sua_chu` (nếu có): chữ Whisper nghe nhầm ({sai, dung}) — tên riêng/chính tả.

# Luật gốc (nguồn duy nhất)
{{muc:cat-highlight-video/SKILL.md|Bốn câu chọn ý}}

{{muc:cat-highlight-video/SKILL.md|Luật riêng của highlight}}

## Khối 13 — chọn khoảnh khắc (làm theo bước 2–5; bỏ qua phần lệnh/script)
{{file:khoi/13-chon-khoanh-khac/README.md}}

Có GÓP Ý CỦA DAVID thì sửa đúng chỗ được nhắc, giữ nguyên phần còn lại của KẾ HOẠCH LẦN TRƯỚC (giữ `id` các clip không đổi).
