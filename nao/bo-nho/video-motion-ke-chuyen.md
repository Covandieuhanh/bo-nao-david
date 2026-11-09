---
name: video-motion-ke-chuyen
description: "Motion graphic kể chuyện, AI tự do sáng tạo: chỉ giữ nền, màu chủ đạo, kiểu vẽ biểu tượng; ý quay lại thì vẽ tiếp (mạch hình) (2026-11-09)"
metadata:
  type: feedback
---

David chốt 09/11/2026: motion graphic là để **diễn tả lại câu chuyện**, không phải "đưa hình vào cho có", không dập khuôn máy móc.
Chỉ giữ cái lớn: **nền, màu chủ đạo, biểu tượng cùng một kiểu vẽ** (+ bộ nhận diện chung). Còn lại AI sáng tạo theo từng video:
một hình có thể diễn tả 1–2 ý hoặc chạy từ đầu tới cuối; ý nào nhắc lại ý trước thì hình **vẽ tiếp** lên cái đã có.

**Why:** David thấy bản nâng chuyển động 09/11 "giống hệt như cũ" — vì Claude tự giữ quá chặt (màu, font, bố cục, danh mục kiểu cảnh).

**How to apply:** khối 07 mục "Motion graphic KỂ CHUYỆN" (luật 1 mới của video-style-edit). Cảnh tự vẽ `type: 've'`, code riêng ở
`motion/src/rieng/`, mạch hình `lib/mach.js`, chuyển động `lib/chuyen-dong.js`. Vẫn giữ: chữ nguyên văn
([[video-chu-nguyen-van]]), không che mặt ([[video-bo-cuc-tu-can]]), đã vào là đứng yên. Thay phần "một màn = một ý" cũ; bổ sung
[[video-luon-co-motion-graphics]], [[luat-hoc-la-bo-sung]] (học là bổ sung chỉ áp cho cái lớn, motion thì tự do).
