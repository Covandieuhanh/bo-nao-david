---
name: video-app-dung-video
description: "App dựng video trên Mac (localhost:8765) = skill chạy tự động: cố định thì máy, phán đoán thì AI làm y như skill; lọc đúng chuẩn, David tự duyệt"
metadata:
  node_type: memory
  type: project
  originSessionId: 87c9809c-02a8-4c04-96d7-ab8e1a33d71e
  modified: 2026-11-09T00:20:04.755Z
---

Từ 08–09/11/2026 David dựng video "1 người nói" bằng app `skills/dung-video/app/` (README trong đó), chạy nền trên Mac:
http://localhost:8765 (chỉ máy này). 2 cổng David duyệt; sổ góp ý 💬 Trao đổi; tự rà soát skill đổi; thanh hạn mức Claude.

David chốt 09/11: phiếu lọc **cứ chấm và báo đúng chuẩn** (kể cả "⛔ Không làm", cảnh báo lằn ranh) — video nào David vẫn muốn làm thì
David tự duyệt. Không hạ chuẩn để chiều, không tự quyết thay.

**Why:** David cần báo cáo trung thực để tự quyết; quyết định là của David.

**How to apply:** sửa app không được nới bộ lọc khối 00 hay luật dựng cho "qua cổng"; lỗi app thì sửa app, không sửa chuẩn.
Không tự Duyệt / Chạy tiếp / Làm lại việc của David ([[luat-khong-tu-chay-viec-cua-david]]); không khởi động lại app khi việc
của David đang chạy — chờ nó tạm dừng. Liên quan [[nao-ho-so-va-bo-loc]], [[luat-goi-y-de-david-chon]].


## Nguyên tắc app — David chốt 09/11/2026 (thay hướng "khuôn JSON + vòng duyệt" của Codex)
- App = **skill chạy tự động**: bước có lệnh cố định thì máy chạy; bước cần phán đoán thì AI (Claude Code hoặc Codex) làm **y như
  skill**, ngay trong thư mục dự án, đọc đúng SKILL.md + README khối (`app/goi_ai.py`, phiếu bước `"loai": "ai"`).
- **App làm khác skill là sai.** Không khuôn JSON, không luật riêng của app, không vòng duyệt/sửa lồng nhau mà skill không có.
  Kết quả video quan trọng nhất; token phụ. Lần Codex thêm vòng lặp làm chậm ×4 (65 phút AI cho 54 giây video) → David dừng, bỏ.
- Công thức `lam-video` đã làm lại theo nguyên tắc này (khớp 12 bước `video-style-edit` + 2 cổng `dang-da-kenh`); thử 09/11 đoạn
  54 giây: mỗi bước AI một lượt 3,5–5 phút, 4 phép đo đạt. Highlight, podcast, vlog còn kiểu cũ → làm lại cùng cách.

**Why:** David muốn thay việc ngồi chat với skill bằng app, không muốn một hệ thứ hai cho ra video khác.

**How to apply:** sửa luật dựng → sửa skill/khối (app tự theo); sửa app chỉ ở phần máy. Thêm bước AI = phiếu `buoc/<id>.json`
loại `ai` trỏ tới bước của skill, không viết lại luật vào phiếu.
