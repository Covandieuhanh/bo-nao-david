---
name: video-do-hoa-ke-chuyen
description: "Mọi video đều có nhiều loại motion graphics để kể lại câu chuyện, không theo mẫu cố định; ở mọi bước, AI sáng tạo bên trong bộ khung, tiêu chí và nhận diện thương hiệu (2026-11-07, 09/11, gộp 10/11)"
metadata:
  type: feedback
---

**Luôn có motion graphics** (07/11/2026): "dựng nhẹ" không có nghĩa là chỉ có phụ đề và nhạc. Motion graphics được hiểu rộng là **điểm nhấn thu hút ánh mắt
của người xem vào ý đang nói**, gồm nhiều loại: hình vẽ hoặc biểu tượng xuất hiện để minh hoạ ý; chữ giải thích, chữ nhấn cụm then chốt; làm nổi bật người đang
nói (làm tối nền, khoanh vùng hoặc viền sáng…; không zoom vào / ra — David 13/11/2026); cảnh minh hoạ toàn màn hình chỉ là một loại. Điểm nhấn đặt trên người được phép nếu không
che mặt. Claude không làm đồ hoạ cho đoạn chạm lằn ranh.

**Motion kể chuyện** (09/11/2026): motion graphic dùng để **diễn tả lại câu chuyện**, không phải "đưa hình vào cho có", không theo mẫu cố định.
Một hình có thể diễn tả 1–2 ý hoặc chạy từ đầu tới cuối; khi một ý nhắc lại ý trước thì hình **vẽ tiếp** lên phần đã có. Claude chỉ giữ cố định chữ ký
nhận diện ([[video-tham-my-chi-giu-nhan-dien]]); phần còn lại được sáng tạo theo từng video, nhưng chọn ít kiểu ([[video-tham-my-chi-giu-nhan-dien]]).

**Mọi bước AI làm** (09/11/2026, David): "phần nào cố định thì làm app, phần nào AI thì gọi AI, và AI phải thể hiện sức mạnh nhiều nhất
bằng cách sáng tạo — chỉ dựa trên bộ khung và tiêu chí, bên trong hoàn toàn sáng tạo cho hợp nội dung video. Đó là cốt lõi."
Nguồn của luật: `ky-nang/chuan-muc-lam-viec.md` (đầu file). Ứng dụng đã bị bỏ ngày 10/11/2026; mọi bước được làm trong phiên Claude ([[video-bo-ung-dung]]).

**Why:**
- Ngày 07/11/2026, video "Đi bộ hằng ngày" ra bản chỉ có phụ đề và nhạc; David hỏi vì sao không có motion graphics và giải thích rằng motion graphics có nhiều loại.
- Ngày 09/11/2026 David thấy bản cải tiến chuyển động "giống hệt như cũ", vì Claude tự giữ quá chặt (màu, font, bố cục, danh mục kiểu cảnh).
  Lúc đó Claude còn giữ "nền, màu chủ đạo, biểu tượng cùng kiểu vẽ"; từ 10/11 Claude chỉ giữ chữ ký nhận diện.
- Ghi nhớ `video-luon-co-motion-graphics` được gộp vào đây ở lần tái bản 2 (10/11/2026).

**How to apply:** khối 07 (motion kể chuyện) và `quy-tac-chung.md` (mọi video đều có điểm nhấn). Cảnh tự vẽ dùng `type: 've'`, mã nguồn riêng nằm ở
`chuyen-dong/src/rieng/`, mạch hình ở `ky-nang/san-xuat-video/dung-video-theo-phong-cach/assets/mau-remotion/src/thu-vien/mach.js`, chuyển động ở `ky-nang/san-xuat-video/dung-video-theo-phong-cach/assets/mau-remotion/src/thu-vien/chuyen-dong.js`. Các quy tắc vẫn giữ: chữ nguyên văn ([[video-chu-nguyen-van]]),
không che mặt ([[video-bo-cuc-tu-can-bang]]), đã vào là đứng yên. Với podcast chỉ có tiếng: [[video-podcast-phu-hinh-30]].

Gốc: khối 4 (Bản chất và kiểm sai) của tu-duy-goc.md — bản chất của motion graphics là kể lại câu chuyện; đưa hình vào cho có là làm hình thức.
