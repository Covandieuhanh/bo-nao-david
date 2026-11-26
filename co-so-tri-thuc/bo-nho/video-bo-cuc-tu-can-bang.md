---
name: video-bo-cuc-tu-can-bang
description: "Bố cục video tự cân bằng theo nội dung, không có con số cố định; graphic tránh mọi người trong khung, khung cắt bám theo người đang nói; khung gốc để học mọi loại video nằm ở ky-nang/san-xuat-video/thiet-ke-bo-cuc (2026-11-07, 08/11)"
metadata:
  type: feedback
---

1. **Học từ video mẫu:** bố cục, cách sắp xếp và hiển thị, thứ tự hiện, cách nối cảnh, hiệu ứng âm thanh, cả phần thẩm mỹ làm tài nguyên;
   chỉ giữ cố định chữ ký nhận diện ([[video-tham-my-chi-giu-nhan-dien]]).
2. **Không có con số cố định về bố cục** (không còn luật 2 trạng thái, giới hạn giây toàn màn hình, % mặt hiện, độ dài cảnh minh hoạ, số chữ
   nhãn, mật độ cảnh). Thước đo duy nhất: hợp với nội dung của chính video đó và người xem tiếp nhận được.
3. **Video ngang** có nhiều chỗ, được tự do bố trí. **Video dọc**: người xem dùng điện thoại, nên mỗi lúc không hiện quá nhiều thứ.
4. Motion graphic không có gì cố định: vị trí, cỡ, tỉ lệ ô thu nhỏ (không bắt buộc 16:9), phía đặt thẻ đều được tự bố trí theo video. Khung có
   nhiều người thì graphic **không được đè hay làm mờ bất kỳ ai**; khung cắt, chuyển cảnh, ô thu nhỏ **bám đúng người đang nói** (không dùng
   hiệu ứng zoom vào / ra — [[video-do-hoa-ke-chuyen]]).
5. Bộ não có **khung gốc để học mọi loại video sau này**, càng học thì càng thêm tài nguyên để tự chọn khi dựng.

Vẫn giữ: chuẩn âm lượng ([[video-nhac-theo-tuyen]]), không che mặt (thu người vào ô thì không tính là che), chữ nguyên văn
([[video-chu-nguyen-van]]), phụ đề luôn chạy. Với vài video đầu tiên dùng bố cục mới, Claude chụp khung cho David duyệt trước khi render.

**Why:** con số cố định buộc mọi video theo cùng một mẫu, không hợp với nội dung.

**How to apply:** học video mẫu theo [[quy-tac-hoc-la-bo-sung]]. Khung gốc ở `ky-nang/san-xuat-video/thiet-ke-bo-cuc/`. `README.md` có tiêu
chí và quy trình học, `bo-cuc.md` là danh mục bố cục, `am-thanh.md` là nơi ghi cách đặt tiếng, `nguon-tham-khao/` ghi mỗi nguồn một file. Code bố cục
nằm ở `bo-cuc.jsx`; người trong khung và người đang nói do `vi-tri-nhan.py` ghi vào `mat.js`, chỗ trống được tính ở `ky-nang/san-xuat-video/dung-video-theo-phong-cach/assets/mau-remotion/src/thu-vien/cho.js` (type
`bocuc`: `the-canh`, `o-nguoi`, `chuong`). Khi học nguồn mới, Claude chỉ thêm mục mới. Liên quan [[video-bo-ung-dung]],
[[video-do-hoa-ke-chuyen]], [[video-kien-truc-ky-nang]].

Nguồn của luật: `ky-nang/san-xuat-video/thiet-ke-bo-cuc/README.md` và `ky-nang/san-xuat-video/quy-tac-chung.md` mục 4. Ghi nhớ này giữ ngày,
lời David, lý do.

## Sổ
- 07/11/2026 David chốt điểm 1–3 và 5; bỏ luật 2 trạng thái, toàn màn hình tối đa 4 s, mặt hiện ít nhất 60%, cảnh minh hoạ 3–5 s, nhãn tối đa 3 chữ, mật độ
  cảnh. Bản này còn "thẩm mỹ của David là gốc, chỉ học trình bày, không chép màu/phông chữ" (vì việc sao chép thẩm mỹ sẽ xung đột với gốc). Nguồn
  đầu tiên đã học: Sang Huỳnh 07/11.
- 08/11/2026 (video phỏng vấn 2 người): thêm điểm 4.
- 10/11/2026 David nới luật thẩm mỹ thành chỉ giữ chữ ký nhận diện, nên điểm 1 được viết lại (tái bản 2).
- 13/11/2026 bỏ hiệu ứng zoom vào / ra ([[video-do-hoa-ke-chuyen]]); bám theo người nói bằng khung cắt (bản luật tái bản 3).

Gốc: khối 4 (R&D) của tu-duy-goc.md — bố cục suy từ nội dung và người xem, không theo con số cố định có sẵn, vì con số đúng cho video này có thể sai cho video khác.
