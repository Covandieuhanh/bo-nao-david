---
description: "Nghiên cứu bài 16 bài học sau 1000 giờ dùng Claude (Nhật Anh AI, 14/11): ý áp dụng cho bộ não."
---

# Học từ "16 bài học sau 1000 giờ dùng Claude" (Nhật Anh AI) — 14/11/2026

Nguồn: https://nhatanh.ai/1000-gio/ (bài viết đi kèm video YouTube của kênh Nhật Anh AI). File này ghi tóm tắt ý, không chép nguyên văn.

## Đối chiếu với hệ của David

| # | Ý chính của bài | Hệ của David | Hành động |
|---|---|---|---|
| 1–2 | Claude Code làm được mọi việc có dạng file; người dùng không cần biết lập trình; dùng chế độ Auto, tránh Bypass | David đã dùng cho video, slide, bot | **Đã làm 14/11**: phiên việc Telegram chạy `--permission-mode auto`, giữ điểm duyệt |
| 3 | Nói thay vì gõ | Bot đã nghe được tin nhắn thoại | — |
| 4 | Đưa ví dụ thật thay vì tính từ | Skill `phan-tich-video-mau` | — |
| 5 | Phỏng vấn từng câu, ghi ngay vào file | `thu-thap-yeu-cau` hỏi theo vòng nhưng chưa ghi vào file | **Đã thêm** bước ghi vào `du-an/phong-van/` |
| 6 | Nhắc lần 2 thì thành quy tắc | `hoc-lien-tuc` gom tín hiệu cuối tuần | **Đã thêm** "nhắc lần hai thì thành luật ngay" (chuẩn mực làm việc, mục 4) |
| 7 | CLAUDE.md ngắn, dạng mục lục (tối đa 50 dòng) | CLAUDE.md có 3 dòng, AGENTS.md có 62 dòng; `david.md` có 137 dòng và được nạp ở mọi phiên | **Đã làm 14/11**: `david.md` còn 50 dòng (mục 1–3), mục 4–9 được chuyển nguyên văn sang 4 file, bảng số mục giữ nguyên |
| 8 | 3 lớp trí nhớ: quy tắc · ghi chú · việc làm chưa xong | AGENTS.md, `bo-nho/` và `bao-cao-trang-thai.md` | — |
| 9 | Context dài thì dễ bỏ sót; tóm tắt sớm (`/autocompact`) | Bot tự `/clear` sau 30 phút nghỉ | **Đã làm 14/11**: `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=60` (cai-hook.py và cài đặt bot) |
| 10 | Bàn giao trước khi mở phiên mới | Đã có file theo dõi | **Đã thêm** dòng "viết lời bàn giao" (chuẩn mực làm việc, mục 5) |
| 11 | Lên kế hoạch bằng mô hình lớn, thực hiện bằng mô hình nhỏ | Đã có nhắc đổi mô hình ở bước nhẹ | — |
| 12 | Tác tử con (sub-agent) dùng Haiku để đọc, tìm, tóm tắt | Chưa có | **Đã tạo** tác tử `nghien-cuu` (Haiku) và thư mục `tac-tu/` |
| 13 | `/goal` để làm tới khi đạt điều kiện | "Xong khi" có trong mọi skill | Dùng `/goal` cho việc dài nhiều lượt khi cần |
| 14 | Đánh giá (eval): luôn kiểm tra kết quả, 4 nấc | Báo cáo "đã kiểm / chưa kiểm" | **Đã thêm** "tự soát trước khi báo xong" 4 nấc (chuẩn mực làm việc, mục 4); bài học 14/11: dựng thử đã phát hiện 5 lỗi đổi tên |
| 15 | Chạy Claude Code 24/7 trên VPS | Bot chạy trên Mac (gập máy thì dừng) | **Chưa cần** (David 14/11: để trên máy này, chưa lên VPS) |
| 16 | Bộ não trên GitHub, AGENTS.md cho mọi AI | Đã có (`bo-nao-david`) | — |
