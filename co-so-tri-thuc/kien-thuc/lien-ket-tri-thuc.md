---
description: Liên kết tri thức cho AI — vì sao mạng lưới file liên kết với nhau (chỉ mục, bản đồ, mô tả, đường liên kết) giúp Claude tra cứu nhanh, tốn ít token, ít bỏ sót; so sánh Claude với Obsidian; ứng dụng Obsidian không cần thiết.
---

# Liên kết tri thức cho AI (Claude và Obsidian)

> Ghi 14/11/2026 từ trao đổi với David.

## Bản chất

- **Obsidian** liên kết bằng đường liên kết do người viết tạo (`[[...]]`, backlink, graph): chắc chắn, thấy được toàn cảnh, nhưng không hiểu nghĩa.
- **Claude** hiểu nghĩa, liên kết được ý giữa các file không có liên kết với nhau, tổng hợp tốt; nhưng mỗi phiên Claude bắt đầu lại từ đầu, chỉ liên kết được những gì đã tìm và đọc, dễ bỏ sót khi file dùng chữ khác với từ khoá.
- Yếu tố giúp Claude là **mạng lưới liên kết viết trong file**, không phải ứng dụng. Liên kết nằm trong file nên được lưu cùng GitHub; ứng dụng Obsidian chỉ để mở xem bản đồ, không bắt buộc.

## Vì sao giảm token

Khi không có chỉ mục, Claude phải tìm toàn văn và mở nhiều file để đoán; kho càng lớn càng tốn token và càng dễ bỏ sót. Khi có chỉ mục và bản đồ, Claude grep một file nhỏ rồi mở trực tiếp 1–3 file đúng. Chỉ khi kho rất lớn (khoảng 1.000 ghi chú trở lên) mới cần bổ sung tìm kiếm theo nghĩa.

## Liên quan
- [quy-uoc-lien-ket.md](../quy-uoc-lien-ket.md) — bộ quy tắc liên kết đang áp dụng.
- [du-an/lien-ket-tri-thuc.md](../../du-an/lien-ket-tri-thuc.md) — kế hoạch, số đo trước / sau.
