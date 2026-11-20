---
name: video-bo-cuc-tu-can
description: "Bố cục video tự cân theo nội dung, không con số cố định; graphic tránh mọi người, khung cắt bám người đang nói; khung gốc học mọi loại video ở ky-nang/san-xuat-video/thiet-ke-bo-cuc (2026-11-07, 08/11)"
metadata:
  type: feedback
---

1. **Học từ video mẫu:** bố cục, cách sắp xếp và hiển thị, thứ tự hiện, cách nối cảnh, hiệu ứng âm thanh, cả phần thẩm mỹ làm tài nguyên;
   chỉ giữ cứng chữ ký nhận diện ([[video-tham-my-chi-giu-nhan-dien]]).
2. **Không con số cố định về bố cục** (không 2 trạng thái, không giới hạn giây toàn màn hình, % mặt hiện, độ dài cảnh minh hoạ, số chữ
   nhãn, mật độ cảnh). Thước đo duy nhất: hợp với nội dung chính video đó, và người xem đón nhận được.
3. **Video ngang** nhiều chỗ, tự do bố trí. **Video dọc** người xem dùng điện thoại, nên mỗi lúc đừng hiện quá nhiều thứ.
4. Motion graphic không có gì cố định: vị trí, cỡ, tỉ lệ ô thu nhỏ (không bắt buộc 16:9), phía đặt thẻ đều tự bố trí theo video. Khung có
   nhiều người thì graphic **không được đè hay làm mờ bất kỳ ai**; khung cắt, chuyển cảnh, ô thu nhỏ **bám đúng người đang nói** (không dùng
   hiệu ứng zoom vào / ra — [[video-do-hoa-ke-chuyen]]).
5. Có **khung gốc để học mọi loại video sau này**, càng học càng thêm tài nguyên để tự chọn khi dựng.

Vẫn giữ: chuẩn âm lượng ([[video-nhac-theo-tuyen]]), không che mặt (thu người vào ô thì không tính là che), chữ nguyên văn
([[video-chu-nguyen-van]]), phụ đề luôn chạy. Mấy video đầu dùng bố cục mới thì chụp khung cho David duyệt trước khi render.

**Why:** con số cứng ép mọi video vào một khuôn, không hợp nội dung.

**How to apply:** học video mẫu theo [[quy-tac-hoc-la-bo-sung]]. Khung gốc ở `ky-nang/san-xuat-video/thiet-ke-bo-cuc/`. `README.md` có tiêu
chí và quy trình học, `bo-cuc.md` là danh mục bố cục, `am-thanh.md` là chỗ đặt tiếng, `nguon-tham-khao/` ghi mỗi nguồn một file. Code bố cục
nằm ở `bo-cuc.jsx`; người trong khung và người đang nói do `vi-tri-nhan.py` ghi vào `mat.js`, chỗ trống tính ở `ky-nang/san-xuat-video/dung-video-theo-phong-cach/assets/khuon-remotion/src/thu-vien/cho.js` (type
`bocuc`: `the-canh`, `o-nguoi`, `chuong`). Học nguồn mới thì chỉ thêm mục mới. Liên quan [[video-bo-ung-dung]],
[[video-do-hoa-ke-chuyen]], [[video-kien-truc-ky-nang]].

Nhà của luật: `ky-nang/san-xuat-video/thiet-ke-bo-cuc/README.md` và `ky-nang/san-xuat-video/quy-tac-chung.md` mục 4. Ghi nhớ này giữ ngày,
lời David, lý do.

## Sổ
- 07/11/2026 David chốt điểm 1–3 và 5; bỏ luật 2 trạng thái, toàn màn hình tối đa 4 s, mặt hiện ít nhất 60%, cảnh minh hoạ 3–5 s, nhãn tối đa 3 chữ, mật độ
  cảnh. Bản này còn "thẩm mỹ của David là gốc, chỉ học trình bày, không chép màu/phông chữ" (vì chép thẩm mỹ thì xung đột với gốc). Nguồn
  đầu tiên đã học: Sang Huỳnh 07/11.
- 08/11/2026 (video phỏng vấn 2 người): thêm điểm 4.
- 10/11/2026 David nới thẩm mỹ thành chỉ giữ chữ ký nhận diện → điểm 1 viết lại (tái bản 2).
- 13/11/2026 bỏ hiệu ứng zoom vào / ra ([[video-do-hoa-ke-chuyen]]); bám người nói bằng khung cắt (bản luật tái bản 3).
