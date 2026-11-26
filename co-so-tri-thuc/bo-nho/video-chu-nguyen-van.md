---
name: video-chu-nguyen-van
description: "Mọi chữ trên video là nguyên văn lời David và chỉ phục vụ nội dung: không dùng thẻ tiêu đề do Claude tự rút ý, màn chốt không do Claude tự viết, không dùng số đếm chạy, không dùng nhãn kỹ thuật ×1,6 / slow-mo (07/11; gộp 15/11)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: fbdca2f7-d150-4f29-9b51-a450fb69af85
  modified: 2026-11-07T11:46:51.064Z
---

Claude được dùng mọi loại motion graphics, nhưng **không được sáng tạo sai lời chính xác của David**:
- Không làm thẻ tiêu đề mở đầu mặc định, vì tiêu đề do Claude tự rút ý có thể chưa đúng điều David muốn truyền tải.
- Chữ trên màn hình là cụm nguyên văn liền mạch trong lời nói; cụm đó được tách thành nhiều mảnh, nhưng không được bỏ chữ làm đổi nghĩa (ví dụ: bỏ "muốn" trong "không muốn làm một mình").
- Màn chốt dùng câu David nói ở cuối video, không dùng câu Claude tự viết.
- Không dùng số đếm chạy (từ 0 đến 60) vì các khung hình ở giữa hiện những con số David không nói; chỉ liệt kê đúng các con số David nói.

**Why:** ngày 07/11/2026, ở video "Đi bộ hằng ngày", thẻ tiêu đề bị cắt dòng ở khung ngang và David thấy tiêu đề có thể lệch ý; khi rà soát lại, Claude còn thấy 4 chỗ chữ lệch so với lời nói.

**How to apply:** trước khi render, Claude rà soát từng chữ đồ hoạ với phu-de.js tại cùng mốc thời gian. Câu hỏi "Vấn đề / Kết quả" do Claude tự viết chỉ đặt ở bài đăng và bình luận ghim, không đưa lên video. Liên quan [[quy-tac-noi-dung-cua-david]], [[video-do-hoa-ke-chuyen]].

## Gộp từ `video-chu-nguyen-van` (15/11/2026, vòng tự học hằng tuần: giảm số ghi nhớ xuống 40)

Video không hiện nhãn tốc độ hay ghi chú kỹ thuật (×1,6, ×0,5, "tua nhanh", "slow-mo", "xem chậm"). Hiệu ứng tua nhanh và phát chậm vẫn được dùng, chỉ không có chú thích.

**Why:** người dùng thấy các ghi chú kỹ thuật là thừa; chữ trên màn hình chỉ nên phục vụ nội dung.
**How to apply:** nguồn của luật `ky-nang/san-xuat-video/quy-tac-chung.md` mục 4 (Hình); cách làm ở `ky-nang/san-xuat-video/dung-video-theo-phong-cach/references/nhieu-doan-video.md`, mẫu bỏ `speed`. Quy tắc áp dụng cho mọi video, kể cả khi Claude tự viết component mới.

Gốc: khối 4 (R&D) của tu-duy-goc.md — chữ tự rút ý có thể lệch điều David muốn nói; giữ nguyên văn là cách chắc chắn không làm sai ý.
