---
name: video-phu-de-mot-cho-chu
description: Phụ đề clip dọc là cụm 5–8 chữ, cỡ bằng chữ trong thẻ (58), chữ thường; khi lớp chữ motion graphic hiện thì phụ đề nhường chỗ, mỗi thời điểm chỉ một vị trí có chữ (2026-11-08)
metadata:
  type: feedback
---

David chốt ngày 08/11/2026:
- **Phụ đề video dọc ngắn** (highlight, clip một người nói tối đa 90 s): mỗi lần phụ đề hiện một cụm trọn ý khoảng 5–8 chữ, tối đa 2 dòng, cỡ bằng chữ trong thẻ motion graphic (58), chữ thường, viền mảnh.
- **Mỗi lúc một chỗ chữ**, áp dụng cho mọi loại video và mọi khung hình: khi lớp motion graphic có chữ đang hiện (chữ to, thẻ, nhãn, sơ đồ, màn hành động, thẻ tiêu đề, màn chốt) thì phụ đề ẩn. Khi lớp đó kết thúc, phụ đề hiện tiếp đúng cụm đang nói. Video dài giữ kiểu phụ đề hộp tối.

**Why:** bản trước dùng kiểu 1–3 chữ to in hoa cỡ 84 (Hormozi/DOAC); David thấy 3–4 chữ mỗi lần là quá ngắn và chữ quá to; người xem không đọc được cả chữ trong hình lẫn phụ đề cùng lúc (David đã nói điều này một lần trước đó; luật 02/11 chỉ ẩn phụ đề khi thẻ toàn cảnh có câu trích).

**How to apply:** tham số nằm ở `ky-nang/san-xuat-video/ho-so-thuong-hieu/chung.json`, khoá `phu_de`; mã nguồn nằm ở `ky-nang/san-xuat-video/thu-vien-tai-nguyen/kieu-phu-de.js`, `phu-de.jsx` (`LOP`), phần dựng ghép `chuong-trinh.jsx` (`nhuong`); luật nằm ở `quy-tac-chung.md` mục 3. Với cảnh không có chữ mà muốn giữ phụ đề, người làm đặt `props.giuPhuDe = true`. Liên quan [[video-chu-nguyen-van]], [[video-nhan-dien-chung]].

Gốc: khối 4 (Bản chất và kiểm sai) của tu-duy-goc.md — người xem chỉ đọc được một chỗ chữ mỗi lúc, nên suy từ đó mà cho phụ đề nhường lớp chữ đồ hoạ.
