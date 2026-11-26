---
description: "Tài liệu podcast có quay người (chưa có skill), rút từ 7 podcast Việt lượt xem cao."
---

# Tài liệu: podcast QUAY NGƯỜI (để dùng sau này — chưa có skill)

*Rút ra từ 7 podcast có quay người, lượt xem cao ở Việt Nam (xem `hoc-tu-20-podcast-vn.md` mục A1–A7) + bài học từ 20 highlight
(`../../cat-doan-noi-bat/references/hoc-tu-20-doan-noi-bat-vn.md`). Dùng khi David bắt đầu quay podcast có người: Claude đọc file này trước khi
lập kế hoạch quay, rồi viết skill dựng riêng (hoặc mở rộng `dung-video-theo-phong-cach` ở chế độ ghép nhiều góc máy).*

## 1. Quay (bối cảnh + máy quay)
- **Bối cảnh có không khí riêng, cố định cho cả series**: bàn cà phê gỗ + cây xanh + đèn vàng (Have A Sip); phòng tối đèn tím (Chú 3 Duy);
  studio kệ sách (Tuấn Tiền Tỉ); quán ăn thật (Trấn Thành). Khán giả nhận ra chương trình chỉ qua khung hình.
- **Tối thiểu 3 góc máy**: rộng 2 người · cận khách · cận người dẫn (+ qua vai nếu có máy thứ 4). Đặt micro trong hình (dấu hiệu nhận biết
  "podcast"). Clip highlight dọc cần góc cận đủ nét để cắt 9:16.
- **Ghi âm riêng từng người** (2 micro) — giúp việc dựng cắt theo người đang nói và làm phụ đề đổi màu theo người nói dễ hơn.
- Đồ uống / đạo cụ của chương trình đặt trên bàn (Have A Sip — tên chương trình "a sip").

## 2. Dựng bản dài
- **Teaser 15–30 s** ghép 3–5 câu then chốt của tập, đặt trước lời chào (A2, A7); hoặc đoạn nền đen có chữ hiện dần + logo (A6).
- Nhận diện động 4–8 s (logo chương trình) sau teaser.
- Cắt theo người đang nói; chèn **cảnh phản ứng** của người nghe ở câu then chốt; đổi qua lại giữa góc rộng và góc cận mỗi 6–30 s (bản dài không cần nhịp dồn dập).
- Chèn **ảnh tư liệu / ảnh đời thật** đúng lúc lời nói nhắc tới (A7, highlight H17).
- Phụ đề trong hộp tối nhỏ ở phía dưới (bản dài); tên + vai trò của khách ở lần nói đầu.
- **Kết**: nơi nghe bản âm thanh (nếu có) · lịch tập sau ("Đón xem tập tiếp theo vào thứ … hàng tuần") · màn kết YouTube 15–20 s
  với 2 tập khác.

## 3. Thumbnail + tiêu đề (mẫu series)
- **Mẫu cố định cho mọi tập**, chỉ đổi chữ + ảnh: nền màu đậm (có thể đổi màu theo khách), tiêu đề 3–4 dòng in hoa bên trái với 1–2
  từ khoá màu nhấn, ảnh khách bên phải (cười / biểu cảm thật), nhãn tên chương trình ở góc, tên khách dưới tiêu đề.
- **Tiêu đề**: câu then chốt của khách (nguyên văn hoặc rút gọn đúng ý) + " – " + tên khách + " | #<Tên show> <số tập>".

## 4. Highlight từ mỗi tập (3–5 clip — skill `cat-doan-noi-bat`)
- Cắt qua lại giữa khách và người dẫn mỗi 2–3 s; phụ đề nhỏ trong ô tối (kiểu Have A Sip) hoặc nhịp chữ lớn (kiểu lan truyền) — chọn một kiểu, giữ cho cả series.
- 0–3 s: nhãn tên chương trình + lịch phát sóng/tập; kết 3–5 s: "Xem/Nghe bản đầy đủ" + tên tập.
- Mỗi clip một khoảnh khắc: câu đố, tiền cược, tâm sự (ảnh đời thật), câu mệnh lệnh.

## 5. Việc cần chuẩn bị trước khi viết skill
- Chọn tên chương trình + bối cảnh + mẫu thumbnail (làm 1 lần).
- Quy ước tên file: `cam-rong.mp4`, `cam-khach.mp4`, `cam-dan.mp4`, `mic-khach.wav`, `mic-dan.wav` để script đồng bộ theo âm thanh (vỗ tay ở đầu buổi quay).
- Skill cần thêm: đồng bộ nhiều máy quay theo sóng âm, tự chọn góc theo người đang nói (đã có phần dò người nói trong `phan-tich-doi-khung.sh` +
  `nguoi-noi.py`), teaser tự đề xuất câu then chốt.
