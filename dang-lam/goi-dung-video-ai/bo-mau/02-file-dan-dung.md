# Mẫu 02 · File dặn dựng (Bài 2, 8)

> Chép phần dưới đường kẻ vào file `AGENTS.md` ở thư mục `lam-video` (Claude Code đọc `CLAUDE.md`, Gemini CLI đọc `GEMINI.md`: tạo file đó với một dòng "Đọc AGENTS.md"). Điền mục 1. Giao việc chỉ cần nói: **"Dựng tap-ten-video"**, kèm muốn gì nếu khác mặc định.

---

# Hướng dẫn dựng video

## 1. Phong cách (học viên điền, sửa dần)
- Màu chính: …… · màu phụ: ……
- Kiểu chữ: tiêu đề …… · phụ đề ……
- Phụ đề: có / không · vị trí: dưới / giữa · cỡ: ……
- Dấu góc (tên / logo nhỏ): …… · nhạc: vui / lắng / không nhạc
- Khung xuất mặc định: ngang 16:9 · dọc 9:16 · vuông · (chọn)
- Video nói: giữ nguyên mạch / cắt gọn câu hỏng và khoảng lặng

## 2. Thư mục
```
lam-video/
├── AGENTS.md          file này
├── nhac/              nhạc nền miễn phí bản quyền
└── tap-<ten-video>/
    ├── 1-goc/         tư liệu gốc (không sửa, không xoá)
    ├── 2-lam/         loi.srt, canh.md, ke-hoach.md, file tạm
    └── 3-xuat/        ban-ngang.mp4, ban-doc.mp4, clip-1.mp4…, anh-bia.jpg
```

## 3. Khi tôi nói "Dựng tap-…": làm một mạch 8 bước
1. **Nạp**: đo độ dài, khung, chất lượng từng file trong `1-goc/`.
2. **Hiểu**: chép lời bằng Whisper (nếu có tiếng nói) → `loi.srt`; chụp khung hình rải đều, mô tả cảnh → `canh.md`.
3. **Kế hoạch** → `ke-hoach.md`: dòng thời gian (đoạn giữ, thứ tự cảnh), chỗ chữ, hình, nhạc. Video > 5 phút hoặc nhiều cảnh: cho tôi xem kế hoạch trước khi dựng.
4. **Dựng thô** bằng ffmpeg: cắt, ghép theo kế hoạch.
5. **Làm sạch**: xoay đúng chiều, cắt khung, sáng màu nhẹ, giảm ồn.
6. **Phụ đề, chữ, đồ hoạ**: phụ đề 5–8 chữ mỗi lần; chữ nhấn lấy đúng lời; đồ hoạ bằng Remotion khi cần; không che chủ thể.
7. **Nhạc, âm thanh**: nhạc thấp dưới giọng; chuẩn âm `loudnorm` khoảng −14 LUFS.
8. **Xuất + tự kiểm**: các khung ở mục 1 (bản dọc bám chủ thể), clip ngắn nếu tôi cần, ảnh bìa từ khung hình của chính video → `3-xuat/`. Chụp 6 khung rải đều kiểm chữ che, lệch khung, chính tả; đo âm lượng. Lỗi thì tự sửa rồi kiểm lại.

Xong báo ngắn: file ở đâu, đã chọn gì vì sao, chỗ cần tôi xác nhận.

## 4. Luật
- Chữ trên video lấy **đúng lời trong video**; không bịa lời.
- Dễ hiểu hơn cầu kì: mỗi video ít kiểu hiệu ứng.
- Không sửa, không xoá `1-goc/`. Hỏi tôi trước khi xoá file khác hay làm gì tốn tiền. Không hỏi, không lưu mật khẩu.
- Tôi góp ý → sửa video, **rồi sửa đúng một câu trong file này** để lần sau tự đúng, báo tôi câu đã sửa.
