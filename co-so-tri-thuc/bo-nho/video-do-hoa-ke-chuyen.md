---
name: video-motion-ke-chuyen
description: "Mọi video có motion graphics nhiều loại để kể lại câu chuyện, không khuôn; mọi bước AI sáng tạo trong khung + tiêu chí + nhận diện (2026-11-07, 09/11, gộp 10/11)"
metadata:
  type: feedback
---

**Luôn có motion graphics** (07/11/2026): "dựng nhẹ" không có nghĩa chỉ phụ đề + nhạc. Motion graphics hiểu rộng là **điểm nhấn kéo mắt
người xem vào ý đang nói**, nhiều loại: hình vẽ / biểu tượng bật ra minh hoạ ý; chữ giải thích, chữ nhấn cụm đắt; làm nổi người đang
nói (làm tối nền, khoanh / viền sáng…; không zoom vào / ra — David 13/11/2026); cảnh minh hoạ toàn màn hình chỉ là một loại. Điểm nhấn trên người được phép nếu không
che mặt. Đoạn chạm lằn ranh không làm đồ hoạ.

**Motion kể chuyện** (09/11/2026): motion graphic là để **diễn tả lại câu chuyện**, không phải "đưa hình vào cho có", không dập khuôn.
Một hình có thể diễn tả 1–2 ý hoặc chạy từ đầu tới cuối; ý nào nhắc lại ý trước thì hình **vẽ tiếp** lên cái đã có. Chỉ giữ cứng chữ ký
nhận diện ([[video-tham-my-chi-giu-nhan-dien]]); còn lại sáng tạo theo từng video, nhưng chọn ít kiểu ([[video-hieu-hon-cau-ki]]).

**Mọi bước AI làm** (09/11/2026, David): "phần nào cố định thì làm app, phần nào AI thì gọi AI, và AI phải thể hiện sức mạnh nhiều nhất
bằng cách sáng tạo — chỉ dựa trên bộ khung và tiêu chí, bên trong hoàn toàn sáng tạo cho hợp nội dung video. Đó là cốt lõi."
Nhà của luật: `ky-nang/chuan-muc-lam-viec.md` (đầu file). App đã bỏ 10/11/2026, mọi bước làm trong phiên Claude ([[video-bo-app]]).

**Why:**
- 07/11/2026 video "Đi bộ hằng ngày" ra bản chỉ phụ đề + nhạc; David hỏi sao không có motion graphics, giải thích có nhiều loại.
- 09/11/2026 David thấy bản nâng chuyển động "giống hệt như cũ" — vì Claude tự giữ quá chặt (màu, font, bố cục, danh mục kiểu cảnh).
  Lúc đó còn giữ "nền, màu chủ đạo, biểu tượng cùng kiểu vẽ"; từ 10/11 chỉ giữ chữ ký nhận diện.
- Gộp ghi nhớ `video-luon-co-motion-graphics` vào đây ở tái bản 2 (10/11/2026).

**How to apply:** khối 07 (motion kể chuyện) và `quy-tac-chung.md` (mọi video đều có điểm nhấn). Cảnh tự vẽ `type: 've'`, code riêng ở
`chuyen-dong/src/rieng/`, mạch hình `thu-vien/mach.js`, chuyển động `thu-vien/chuyen-dong.js`. Vẫn giữ: chữ nguyên văn ([[video-chu-nguyen-van]]),
không che mặt ([[video-bo-cuc-tu-can]]), đã vào là đứng yên. Podcast chỉ có tiếng: [[video-podcast-phu-hinh-30]].
