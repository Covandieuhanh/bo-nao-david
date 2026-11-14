---
description: Liên kết tri thức cho AI — vì sao mạng lưới file nối nhau (chỉ mục, bản đồ, mô tả, đường nối) giúp Claude tra nhanh, ít token, ít sót; Claude so với Obsidian; app Obsidian không cần thiết.
---

# Liên kết tri thức cho AI (Claude và Obsidian)

> Ghi 14/11/2026 từ trao đổi với David.

## Bản chất

- **Obsidian** nối bằng đường nối người viết (`[[...]]`, backlink, graph): chắc chắn, thấy toàn cảnh, nhưng không hiểu nghĩa.
- **Claude** hiểu nghĩa, nối được ý giữa các file không link nhau, tổng hợp tốt; nhưng mỗi phiên bắt đầu lại, chỉ nối được những gì đã tìm và đọc, dễ sót khi file dùng chữ khác từ khoá.
- Cái giúp Claude là **mạng lưới liên kết viết trong file**, không phải app. Liên kết nằm trong file nên đi theo GitHub; app Obsidian chỉ để mở xem bản đồ cho vui.

## Vì sao giảm token

Không có chỉ mục: tìm toàn văn, mở nhiều file để đoán, kho càng lớn càng tốn và sót. Có chỉ mục + bản đồ: grep một file nhỏ, mở thẳng 1–3 file đúng. Khi kho rất lớn (khoảng 1.000 ghi chú trở lên) mới cần thêm tìm theo nghĩa.

## Liên quan
- [quy-uoc-lien-ket.md](../quy-uoc-lien-ket.md) — bộ quy tắc liên kết đang áp dụng.
- [du-an/lien-ket-tri-thuc.md](../../du-an/lien-ket-tri-thuc.md) — kế hoạch, số đo trước / sau.
