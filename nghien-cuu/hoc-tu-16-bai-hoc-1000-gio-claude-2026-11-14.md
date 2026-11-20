---
description: "Nghiên cứu bài 16 bài học sau 1000 giờ dùng Claude (Nhật Anh AI, 14/11): ý áp dụng cho bộ não."
---

# Học từ "16 bài học sau 1000 giờ dùng Claude" (Nhật Anh AI) — 14/11/2026

Nguồn: https://nhatanh.ai/1000-gio/ (bài viết đi kèm video YouTube kênh Nhật Anh AI). Ghi tóm tắt ý, không chép nguyên văn.

## Đối chiếu với hệ của David

| # | Ý chính của bài | Hệ của David | Làm gì |
|---|---|---|---|
| 1–2 | Claude Code làm được mọi thứ là file; không cần biết code; dùng chế độ Auto, tránh Bypass | Đã dùng cho video, slide, bot | **Đã làm 14/11**: phiên việc Telegram chạy `--permission-mode auto`, giữ cổng duyệt |
| 3 | Nói thay vì gõ | Bot đã nghe tin thoại | — |
| 4 | Đưa ví dụ thật thay vì tính từ | Skill `phan-tich-video-mau` | — |
| 5 | Phỏng vấn từng câu, ghi ngay vào file | `thu-thap-yeu-cau` hỏi theo vòng nhưng chưa ghi file | **Đã thêm** bước ghi `du-an/phong-van/` |
| 6 | Nhắc lần 2 thì thành quy tắc | `hoc-lien-tuc` gom tín hiệu cuối tuần | **Đã thêm** "nhắc lần hai thì thành luật ngay" (chuan-muc mục 4) |
| 7 | CLAUDE.md ngắn, dạng mục lục (tối đa 50 dòng) | CLAUDE.md 3 dòng, AGENTS 62 dòng; `david.md` 137 dòng nạp ở mọi phiên | **Đã làm 14/11**: `david.md` còn 50 dòng (mục 1–3), mục 4–9 chuyển nguyên văn sang 4 file, bảng số mục giữ nguyên |
| 8 | 3 lớp trí nhớ: quy tắc · ghi chú · việc đang dở | AGENTS + `bo-nho/` + `bao-cao-trang-thai.md` | — |
| 9 | Context dài thì dễ sót; tóm tắt sớm (`/autocompact`) | Bot tự `/clear` sau 30 phút nghỉ | **Đã làm 14/11**: `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=60` (cai-hook.py + cài đặt bot) |
| 10 | Bàn giao trước khi mở phiên mới | Có file theo dõi | **Đã thêm** dòng "viết lời bàn giao" (chuan-muc mục 5) |
| 11 | Lên kế hoạch bằng model to, làm bằng model nhỏ | Nhắc đổi mô hình ở bước nhẹ | — |
| 12 | Sub-agent dùng Haiku cho đọc/tìm/tóm tắt | Chưa có | **Đã tạo** agent `nghien-cuu` (Haiku), `tac-tu/` |
| 13 | `/goal` để làm tới khi đạt điều kiện | "Xong khi" trong mọi skill | Dùng `/goal` cho việc dài nhiều lượt khi cần |
| 14 | Eval: luôn kiểm tra kết quả, 4 nấc | Báo cáo "đã kiểm / chưa kiểm" | **Đã thêm** "tự soát trước khi báo xong" 4 nấc (chuan-muc mục 4); bài học 14/11: dựng thử bắt 5 lỗi đổi tên |
| 15 | Chạy Claude Code 24/7 trên VPS | Bot chạy trên Mac (gập máy là dừng) | **Chưa cần** (David 14/11: để trên máy này, chưa lên VPS) |
| 16 | Bộ não trên GitHub, AGENTS.md cho mọi AI | Đã có (`bo-nao-david`) | — |
