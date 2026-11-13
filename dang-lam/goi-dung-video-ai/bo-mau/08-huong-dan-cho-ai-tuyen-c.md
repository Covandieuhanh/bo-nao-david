# Mẫu 08 · File dặn trợ lý AI (tuyến C)

> Chép phần dưới đường kẻ vào file `AGENTS.md` ở thư mục `lam-video` (Claude Code đọc `CLAUDE.md`, Gemini CLI đọc `GEMINI.md`: tạo file đó với một dòng "Đọc AGENTS.md"). Dán hồ sơ (mẫu 03) vào mục 1. Học viên giao việc chỉ cần nói: **"Làm video tap-ten-y"**.

---

# Hướng dẫn làm video

## 1. Tôi là ai
[dán hồ sơ, giọng văn, nhận diện, luật kênh từ mẫu 03]

## 2. Thư mục
```
lam-video/
├── AGENTS.md            file này
├── so-video.md          sổ video + số liệu (mẫu 06)
├── kho-y.md             kho ý (mẫu 02)
├── nhac/                nhạc nền miễn phí bản quyền
└── tap-<ten-y>/
    ├── 1-goc/           file quay gốc (không sửa, không xoá)
    ├── 2-ban-dai/       loi.srt, phieu-loc.md, ke-hoach.md, ban-cuoi.mp4
    ├── 3-clip/          clip-1.mp4, clip-2.mp4…
    └── phat-hanh.md     tiêu đề, mô tả, chữ đăng, ảnh bìa
```

## 3. Khi tôi nói "Làm video tap-…": làm một mạch 9 bước
1. **Chép lời** file trong `1-goc/` bằng Whisper (tiếng Việt), ra `loi.srt` có mốc thời gian. Soát chữ nghe nhầm, tên riêng; chỗ không chắc ghi lại để hỏi tôi một lần cuối việc.
2. **Lọc** theo phiếu lọc (5 tiêu chí, mẫu 02) → `phieu-loc.md`. Điểm ≤ 4: dừng, báo tôi.
3. **Kế hoạch dựng** → `ke-hoach.md`: đoạn cắt (khoảng lặng, câu nói hỏng), bảng chữ nhấn + hình minh hoạ theo giây, nhạc.
4. **Dựng bản dài** bằng ffmpeg (và Remotion khi cần đồ hoạ): cắt theo kế hoạch → phụ đề 5–8 chữ mỗi lần → chữ nhấn, hình → nhạc thấp dưới giọng → chuẩn âm `loudnorm` khoảng −14 LUFS → `ban-cuoi.mp4`.
5. **Tự kiểm**: chụp 6 khung hình rải đều, xem chữ có che mặt, có lệch khung, có lỗi chính tả không; đo âm lượng. Lỗi thì sửa rồi kiểm lại.
6. **Clip dọc**: chọn 1–3 đoạn đạt 4 câu (bối cảnh · ý trọn · mang về · chừa lại), đổi khung 9:16 bám người nói, tít bằng đúng lời trong đoạn → `3-clip/`.
7. **Phát hành** → `phat-hanh.md` (lời dặn bước 6, mẫu 04) + ảnh bìa lấy từ khung hình của chính video.
8. **Ghi sổ** `so-video.md`: dòng mới, trạng thái "chờ đăng".
9. **Báo tôi** ngắn: file ở đâu, đã chọn gì vì sao, chỗ cần tôi xác nhận.

## 4. Luật
- Chữ trên video, tiêu đề, phụ đề **lấy đúng lời tôi nói**; không bịa lời.
- Dễ hiểu hơn cầu kì: mỗi video ít kiểu hiệu ứng.
- **Không tự đăng, không xoá file gốc, không tiêu tiền**: hỏi tôi trước. Không hỏi, không lưu mật khẩu, mã OTP.
- Tôi góp ý → sửa video, **rồi sửa đúng một câu trong file này** để lần sau tự đúng, báo tôi câu đã sửa.
- Tôi đưa số liệu → điền sổ, kết luận Kết quả / Vấn đề, đề xuất đúng 1 điều sửa.
