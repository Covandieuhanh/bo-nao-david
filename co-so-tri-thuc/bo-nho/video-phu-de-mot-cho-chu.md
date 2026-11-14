---
name: video-phu-de-mot-cho-chu
description: Phụ đề clip dọc là cụm 5–8 chữ, cỡ bằng chữ thẻ (58), chữ thường; lớp chữ motion graphic hiện thì phụ đề nhường, mỗi lúc một chỗ chữ (2026-11-08)
metadata:
  type: feedback
---

David chốt ngày 08/11/2026:
- **Phụ đề video dọc ngắn** (highlight, clip một người ≤ 90 s): mỗi lần hiện một cụm trọn ý khoảng 5–8 chữ, tối đa 2 dòng, cỡ bằng chữ trong thẻ motion graphic (58), chữ thường, viền mảnh. Thay kiểu 1–3 chữ to in hoa cỡ 84 (Hormozi/DOAC).
- **Mỗi lúc một chỗ chữ**, áp cho mọi loại video và mọi khung: lớp motion graphic có chữ đang hiện (chữ to, thẻ, nhãn, sơ đồ, màn hành động, thẻ tít, màn chốt) thì phụ đề ẩn. Hết lớp đó, phụ đề hiện tiếp đúng cụm đang nói. Video dài giữ phụ đề hộp tối.

**Why:** David thấy 3–4 chữ một lần quá ngắn, chữ quá to; người xem không đọc được cả chữ hình lẫn phụ đề cùng lúc (đã nói một lần trước, luật 02/11 chỉ ẩn khi thẻ toàn cảnh có câu trích).

**How to apply:** tham số ở `ho-so-thuong-hieu/chung.json` → `phu_de`; code ở `thu-vien-tai-nguyen/kieu-phu-de.js`, `phu-de.jsx` (`LOP`), montage `chuong-trinh.jsx` (`nhuong`); luật ở `quy-tac-chung.md` mục 3. Cảnh không có chữ muốn giữ phụ đề: `props.giuPhuDe = true`. Liên quan [[video-chu-nguyen-van]], [[video-nhan-dien-chung]].
