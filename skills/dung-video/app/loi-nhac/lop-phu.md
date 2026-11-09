XEM HÌNH trước (công cụ Read, nếu có ảnh): lưới khung hình của video nguồn — để biết bối cảnh, người nói, chỗ trống trong khung, rồi chọn cho hợp hình thật.

Bạn đặt lớp đồ hoạ cho các clip highlight DỌC (người nói, khung ghép clip) của David Trần. Trả về MỘT JSON. Không viết code, không ghi giây:
mỗi lớp có `trich` = 4–10 chữ NGUYÊN VĂN liền nhau trong KẾ HOẠCH CẮT (lời của chính clip đó) tại lúc lớp bắt đầu; `het` (tuỳ chọn) =
vài chữ lúc kết thúc; trong `props` mọi mốc (at, quoteAt, doneAt…) ghi `trich` / `trich_<khoá>`.

# Khuôn trả về
`clips`: [{id, overlays: [{type, trich, het?, props}], hl: [từ khoá nguyên văn sẽ tô màu trong phụ đề], cta_kind?: comment|save|follow|share|moi}],
`sua_chu`?: [{sai, dung}] chữ Whisper nghe nhầm trong phụ đề.
Thẻ tít mở (pow 0–2,5 s), dấu kênh, thẻ cuối, màn chốt, nhạc: máy đã đặt sẵn — KHÔNG thêm lại.
Kiểu lớp phủ dùng được: pow (props {text ≤ 14 ký tự/dòng}), action ({icon, quote, trich_doneAt}), chips ({items: [...]}), illus ({mode, items:
[{icon, trich, label?}], label?, num?}), diagram, callout, pointer, replay, nameCard, location, scene. Biểu tượng chỉ dùng: {{bieu_tuong}}
Mọi chữ trên màn hình NGUYÊN VĂN lời trong clip (chỉ chọn câu, bỏ chữ đầu/cuối, viết hoa). Mật độ: dày hơn ở `soi`, thưa hơn ở `lang`.

# Luật (nguồn duy nhất — bỏ qua phần lệnh/script)
{{muc:cat-highlight-video/SKILL.md|7A. Dựng}}

{{muc:cat-highlight-video/SKILL.md|Luật riêng của highlight}}

{{muc:video-style-edit/references/multi-clip.md|4. Điểm nhấn}}

Có GÓP Ý CỦA DAVID thì sửa đúng chỗ được nhắc, giữ nguyên phần còn lại của KẾ HOẠCH LẦN TRƯỚC.
