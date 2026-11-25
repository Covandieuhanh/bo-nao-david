---
description: "Biểu mẫu 02 cho học viên: quy trình vận hành chuẩn (SOP) dựng video bằng AI."
---

# Biểu mẫu 02 · Quy trình vận hành chuẩn (SOP) dựng video (Bài 2, 8)

> **Cách lưu:** chép phần dưới đường kẻ vào thư mục `lam-video`, đặt tên file theo trợ lý AI đang dùng để nó tự tìm đọc: Codex đọc `AGENTS.md`, Claude Code đọc `CLAUDE.md`, Gemini CLI đọc `GEMINI.md`. Điền mục 1. Giao việc chỉ cần nói: **"Dựng tap-ten-video"**, kèm muốn gì nếu khác mặc định.

---

# Quy trình vận hành chuẩn (SOP) dựng video

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
├── AGENTS.md          SOP này
├── nhac/              nhạc nền miễn phí bản quyền
└── tap-<ten-video>/
    ├── 1-goc/         tư liệu gốc (không sửa, không xoá)
    ├── 2-lam/         loi.srt, canh.md, ke-hoach.md, file tạm
    └── 3-xuat/        ban-ngang.mp4, ban-doc.mp4, clip-1.mp4…, anh-bia.jpg
```

## 3. Khi tôi nói "Dựng tap-…": làm một mạch 8 bước
1. **Nạp**: đo độ dài, khung, chất lượng từng file trong `1-goc/`.
2. **Hiểu**: chép lời bằng Whisper (nếu có tiếng nói) → `loi.srt`, xoá dòng ở đoạn lặng hoặc chỉ có nhạc (Whisper hay bịa đặt chữ ở đó); chụp khung hình rải đều, mô tả cảnh → `canh.md`.
3. **Kế hoạch** → `ke-hoach.md`: dòng thời gian (đoạn giữ, thứ tự cảnh), chỗ chữ, hình, nhạc. Video kiến thức quay xa, người nhỏ trong khung: đặt người một bên, phần còn lại làm bảng ý chính + hình minh hoạ. Ghép nhiều video gốc thành một: cắt phần tôi đánh dấu không công khai (chuyện riêng, người chưa đồng ý xuất hiện), bỏ ý còn dở ở cuối để mỗi ý trọn, mở đầu bằng một câu then chốt cắt từ chính video. Video > 5 phút hoặc nhiều cảnh: cho tôi xem kế hoạch trước khi dựng.
4. **Dựng thô** bằng ffmpeg: cắt, ghép theo kế hoạch.
5. **Làm sạch**: xoay đúng chiều, cắt khung, sáng màu nhẹ, giảm ồn. Quay ngồi (ngoài trời, ghế thấp): cắt khung tới ngang bụng để không lộ chân, trông lịch sự.
6. **Phụ đề, chữ, đồ hoạ**: phụ đề 5–8 chữ mỗi lần; chữ nhấn lấy đúng lời; đồ hoạ bằng Remotion khi cần; không che mặt, ô thu nhỏ không cắt vào mặt; chữ trên nền đặc màu tương phản để đọc rõ.
7. **Nhạc, âm thanh**: nhạc thấp dưới giọng; chuẩn âm `loudnorm` khoảng −14 LUFS.
8. **Xuất + tự kiểm**: các khung ở mục 1 (bản dọc bám chủ thể), clip ngắn nếu tôi cần, ảnh bìa từ khung hình của chính video → `3-xuat/`. Chụp 6 khung rải đều kiểm chữ che, lệch khung, chính tả; đo âm lượng. Lỗi thì tự sửa rồi kiểm lại. Trước khi xuất bản dài, kiểm ổ trống (ít nhất gấp 3 dung lượng bản xuất); xong bước nào xoá file tạm của bước đó trong `2-lam/`.

Xong báo ngắn, mỗi ý một dòng, gọi bằng tên dễ hiểu (tên video, tên file), không dùng ký hiệu riêng: file ở đâu · đã chọn gì vì sao · câu cần tôi xác nhận để cuối cùng.

## 4. Luật
- Chữ trên video lấy **đúng lời trong video**; không bịa đặt lời.
- Dễ hiểu hơn cầu kì: mỗi video ít kiểu hiệu ứng.
- Không sửa, không xoá `1-goc/`. Hỏi tôi trước khi xoá file khác hay làm gì tốn tiền. Không hỏi, không lưu mật khẩu.
- Tôi phản hồi thì sửa video, **rồi sửa đúng một câu trong SOP này** để lần sau tự đúng, báo tôi câu đã sửa.
