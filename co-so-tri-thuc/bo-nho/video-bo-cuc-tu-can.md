---
name: video-bo-cuc-tu-can
description: Bố cục video tự cân theo nội dung, bỏ mọi con số cố định; graphic tránh mọi người, bám người đang nói; khung gốc học mọi loại video ở ky-nang/san-xuat-video/thiet-ke-bo-cuc (2026-11-07, 08/11)
metadata:
  type: feedback
---

David chốt ngày 07/11/2026:

1. **Học từ video mẫu:** bố cục, cách sắp xếp và hiển thị, thứ tự hiện, cách nối cảnh, hiệu ứng âm thanh — và từ 10/11/2026 cả phần thẩm mỹ làm tài nguyên; chỉ giữ cứng chữ ký nhận diện ([[video-tham-my-chi-giu-nhan-dien]]).
2. **Bỏ hết con số cố định về bố cục.** Đã bỏ luật 2 trạng thái, toàn màn hình ≤ 4 s, mặt hiện ≥ 60%, cảnh minh hoạ 3–5 s, nhãn ≤ 3 chữ, mật độ cảnh. Thước đo duy nhất: hợp với nội dung chính video đó, và người xem đón nhận được.
3. **Video ngang** nhiều chỗ, tự do bố trí. **Video dọc** người xem dùng điện thoại, nên mỗi lúc đừng hiện quá nhiều thứ.
4. **Thêm 08/11/2026 (video phỏng vấn 2 người):** mọi motion graphic không có gì cố định: vị trí, cỡ, tỉ lệ ô thu nhỏ (không bắt buộc 16:9), phía đặt thẻ đều tự bố trí theo video. Khung có nhiều người thì graphic **không được đè hay làm mờ bất kỳ ai**; zoom, chuyển cảnh, ô thu nhỏ phải **bám đúng người đang nói**.
5. Phải có **khung gốc để học mọi loại video sau này**, càng học càng thêm tài nguyên để tự chọn khi dựng.

Vẫn giữ: chuẩn âm lượng ([[video-nhac-theo-tuyen]]), không che mặt (thu người vào ô thì không tính là che), chữ nguyên văn ([[video-chu-nguyen-van]]), phụ đề luôn chạy. Mấy video đầu dùng bố cục mới thì chụp khung cho David duyệt trước khi render.

**Why:** con số cứng ép mọi video vào một khuôn, không hợp nội dung. Bản 07/11 còn "thẩm mỹ của David là gốc, chỉ học trình bày, không chép màu/phong-chu" (vì chép thẩm mỹ thì xung đột với gốc); 10/11/2026 David nới thành chỉ giữ chữ ký nhận diện, nên điểm 1 đã viết lại ở tái bản 2.

**How to apply:** học video mẫu theo [[quy-tac-hoc-la-bo-sung]]. Khung gốc ở `ky-nang/san-xuat-video/thiet-ke-bo-cuc/`. `README.md` có tiêu chí và quy trình học, `bo-cuc.md` là danh mục bố cục, `am-thanh.md` là chỗ đặt tiếng, `nguon-tham-khao/` ghi mỗi nguồn một file. Code bố cục nằm ở `bo-cuc.jsx`; người trong khung và người đang nói do `vi-tri-nhan.py` ghi vào `mat.js`, chỗ trống tính ở `src/thu-vien/cho.js` (type `bocuc`: `the-canh`, `o-nguoi`, `chuong`). Học nguồn mới thì chỉ thêm mục mới. Nguồn đầu tiên đã học: Sang Huỳnh 07/11. Liên quan [[video-khong-cai-hyperframes]], [[video-do-hoa-ke-chuyen]], [[video-kien-truc-ky-nang]].
