---
name: video-app-dung-video
description: "App dựng video trên Mac (localhost:8765, iPhone qua Tailscale) — lọc/chấm phải đúng chuẩn, không chiều; David tự duyệt video nào vẫn muốn làm"
metadata:
  node_type: memory
  type: project
  originSessionId: 87c9809c-02a8-4c04-96d7-ab8e1a33d71e
  modified: 2026-11-09T00:20:04.755Z
---

Từ 08–09/11/2026 David dựng video "1 người nói" bằng app `skills/dung-video/app/` (README trong đó), chạy nền trên Mac:
http://localhost:8765, iPhone qua Tailscale http://macbook-david:8765. 3 bước Claude (lọc, kịch bản, phát hành), còn lại máy chạy;
2 cổng David duyệt; sổ góp ý 💬 Trao đổi; tự rà soát skill đổi.

David chốt 09/11: phiếu lọc **cứ chấm và báo đúng chuẩn** (kể cả "⛔ Không làm", cảnh báo lằn ranh) — video nào David vẫn muốn làm thì
David tự duyệt. Không hạ chuẩn để chiều, không tự quyết thay.

**Why:** David cần báo cáo trung thực để tự quyết; quyết định là của David.

**How to apply:** sửa app không được nới bộ lọc khối 00 hay luật dựng cho "qua cổng"; lỗi app thì sửa app, không sửa chuẩn.
Không tự Duyệt / Chạy tiếp / Làm lại việc của David ([[luat-khong-tu-chay-viec-cua-david]]); không khởi động lại app khi việc
của David đang chạy — chờ nó tạm dừng. Liên quan [[nao-ho-so-va-bo-loc]], [[luat-goi-y-de-david-chon]].


## David xác nhận 09/11/2026 — chất lượng trước token
- App chỉ có giá trị nếu video render đạt cùng tiêu chuẩn thẩm mỹ, nội dung và kỹ thuật như AI dùng skill trực tiếp. Tiết kiệm token là mục tiêu phụ; không đổi chất lượng lấy token.
- David yêu cầu hỗ trợ cả Claude và Codex, không khoá app vào Claude. Đã cho phép kiểm thử dự án đọc sách với Codex/OpenAI trong phiên Codex ngày 09/11.
- Đã thêm adapter hai AI, chọn AI trong giao diện, duyệt lại sau sửa, chụp thử video người nói, chặn lỗi kỹ thuật và chia trang ảnh kiểm. CLI Codex đã nhận ảnh, trả kế hoạch hợp lệ và render được bản thử riêng.
- **Chưa kết luận ngang skill 100%.** Kiểm thử đơn vị/luồng không chứng minh thẩm mỹ; bản thử vẫn cần xem và đánh giá lại. Chưa chạy nghiệm thu toàn bộ podcast, highlight, vlog bằng Codex.
- App hiện chỉ sửa tự động trong khuôn kế hoạch; lỗi cần thay code/template/nguồn phải báo dừng, chưa có agent tự sửa code.
- Nguồn: David xác nhận và yêu cầu triển khai trong chat Codex ngày 09/11/2026; không coi đề xuất kỹ thuật là quyết định mở rộng phạm vi khác của David.
