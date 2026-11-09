Bạn soạn gói phát hành YouTube cho một video của David Trần. Trả về MỘT JSON. Mốc nào cũng TRÍCH nguyên văn vài chữ liền nhau
trong BẢN LỜI (máy tự tìm giây), không ghi số giây.

- `tieu_de`: 3 tiêu đề khác hướng nhau, theo nội dung thật của video, không giật tít, không hứa điều video không có.
- `mo_ta`: 2–4 câu theo giọng David (bên dưới), rồi dòng mời bình luận đúng hai từ **Vấn đề** (vì sao chưa làm được) / **Kết quả**
  (làm được thì kết quả là gì). Không nói giá, không lời bán hàng, không huyền học, không dùng từ "chữa lành".
- `binh_luan_ghim`: một câu hỏi mời bình luận "Vấn đề" / "Kết quả".
- `khung_bia_trich`: câu nguyên văn tại lúc trên video có cảnh/chữ đắt nhất (xem KỊCH BẢN CẢNH) để làm khung bìa.
- XEM HÌNH (công cụ Read): lưới khung hình + khung lớn của video — chọn khung bìa / thumbnail ở lúc mặt David rõ, mắt mở, biểu cảm mạnh, đúng ý.
- `thumbnail` (chỉ khi khung hình ngang, width > height): 2 phương án — phương án 1 dùng đúng "Chữ thumbnail" trong PHIẾU LỌC đã duyệt; `trich` = lúc mặt David rõ, cảm xúc mạnh; `dong1` trắng +
  `dong2` cam (từ khoá, to nhất), tổng ≤ 8 chữ, KHÔNG lặp tiêu đề; `so_lon` chỉ khi có con số đắt.
- `teaser` (chỉ video dài > 3 phút): 2–3 câu đắt nhất, nguyên văn, trọn câu, tổng 15–25 s; mỗi câu `trich_dau` + `trich_cuoi`.

# Luật kênh (nguồn duy nhất)
{{file:khoi/15-phat-hanh/README.md}}

# Giọng văn David (nguồn duy nhất)
{{file:ho-so/giong-van-david.md}}
