---
name: video-bo-cuc-tu-can
description: Bố cục video tự cân theo nội dung, bỏ mọi con số cố định; học video mẫu chỉ học trình bày, không đổi thẩm mỹ; khung gốc ở skills/dung-video/trinh-bay (2026-11-07)
metadata:
  type: feedback
---

David chốt ngày 07/11/2026:

1. **Thẩm mỹ của David là gốc:** màu, phối cảnh, animation sẵn có. Học từ video mẫu thì **chỉ học trình bày**: bố cục, cách sắp xếp và hiển thị, thứ tự hiện, cách nối cảnh, hiệu ứng âm thanh. Không chép màu, font hay kiểu chuyển động của họ.
2. **Bỏ hết con số cố định về bố cục.** Đã bỏ luật 2 trạng thái, toàn màn hình ≤ 4 s, mặt hiện ≥ 60%, cảnh minh hoạ 3–5 s, nhãn ≤ 3 chữ, mật độ cảnh. Thước đo duy nhất: hợp với nội dung chính video đó, và người xem đón nhận được.
3. **Video ngang** nhiều chỗ, tự do bố trí. **Video dọc** người xem dùng điện thoại, nên mỗi lúc đừng hiện quá nhiều thứ.
4. Phải có **khung gốc để học mọi loại video sau này**, càng học càng thêm tài nguyên để tự chọn khi dựng.

Vẫn giữ: chuẩn âm lượng ([[video-chuan-am-luong]]), không che mặt (thu người vào ô thì không tính là che), chữ nguyên văn ([[video-chu-nguyen-van]]), phụ đề luôn chạy. Mấy video đầu dùng bố cục mới thì chụp khung cho David duyệt trước khi render.

**Why:** mỗi lần học mà chép cả thẩm mỹ sẽ xung đột với gốc và phải sửa lại rất khó. Còn con số cứng thì ép mọi video vào một khuôn, không hợp nội dung.

**How to apply:** khung gốc ở `skills/dung-video/trinh-bay/`. `README.md` có tiêu chí và quy trình học, `bo-cuc.md` là danh mục bố cục, `am-thanh.md` là chỗ đặt tiếng, `nguon-hoc/` ghi mỗi nguồn một file. Code bố cục nằm ở `BoCuc.jsx` (type `bocuc`: `the-canh`, `o-nguoi`, `chuong`). Học nguồn mới thì chỉ thêm mục mới. Nguồn đầu tiên đã học: Sang Huỳnh 07/11. Liên quan [[video-khong-cai-hyperframes]], [[video-luon-co-motion-graphics]], [[video-kien-truc-skill]].
