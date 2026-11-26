---
name: video-chi-hinh-cua-chinh-video
description: "Ảnh bìa và thumbnail chỉ lấy từ chính video đó; ảnh bìa podcast chỉ có tiếng thì không đưa khuôn mặt người và phải khớp nội dung (05/11, 06/11; gộp 15/11)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: d6267332-097f-4c05-989b-af19b70dff05
  modified: 2026-11-05T00:36:57.758Z
---

Khi làm một video, mọi hình ảnh (thumbnail, ảnh bìa, khung bìa, cảnh chèn) chỉ lấy từ chính video đó, hoặc từ ảnh David gửi riêng cho video đó. Claude không bao giờ lấy khuôn mặt hoặc cảnh từ video hay dự án khác, kể cả khi hình đó đẹp hơn. Với podcast không có hình người, thumbnail dùng khung đồ hoạ của chính podcast đó.

**Why:** ngày 2026-11-05, thumbnail của podcast "Mục tiêu và sứ mệnh" lấy khuôn mặt David từ vlog Miếu Bà Cam; David nhận xét: "đang bị lẫn lộn… không được phép liên quan đến các video khác".

**How to apply:** khi hỏi David về nguồn ảnh, Claude không đưa "lấy từ video cũ" thành một lựa chọn. Nguồn của luật: `ky-nang/san-xuat-video/mo-dun/14-anh-thu-nho/README.md` (bộ [[video-kien-truc-ky-nang]]). Ghi nhớ này lưu ngày, lời David và lý do.

## Gộp từ `video-chi-hinh-cua-chinh-video` (15/11/2026, vòng tự học hằng tuần: giảm số ghi nhớ xuống 40)

Với video podcast chỉ có tiếng, ảnh bìa không đưa khuôn mặt người, kể cả ảnh chụp riêng. Tiêu chí có khuôn mặt chỉ áp dụng cho video quay hình. Ảnh bìa phải liên quan tới nội dung trong video.

**Công thức ảnh bìa podcast David duyệt 06/11/2026 (đã đưa vào khối 14 và `anh-thu-nho.sh`):** nền có hoạ tiết, một hình đại diện cho ý chính (ví dụ: hình vẽ danh sách, không chữ), tiêu đề ngắn và góc "DAVID · PODCAST". Ảnh bìa không liệt kê các bước: khi giải pháp đã lộ trên ảnh bìa thì người xem không xem video. Ảnh bìa chỉ nêu nỗi đau hoặc giải pháp ở mức gợi mở. Mẫu: `mau-chuan/anh-thu-nho-podcast/chuan.jpg`.

**Why:** David thấy đề xuất "chụp ảnh mặt cho podcast" sai loại video: video không có người thì ảnh bìa có người là không khớp. David muốn nghiên cứu nội dung đưa lên ảnh bìa, gồm chữ podcast và câu nêu giải pháp hoặc nỗi đau. David xem đó là góc nhìn riêng của mình và cần Claude nghiên cứu độc lập.

**How to apply:** khi nghiên cứu cho một loại video, Claude chỉ lấy mẫu đúng loại video đó, không lấy kênh quay hình làm chuẩn đối chiếu cho podcast. Liên quan `video-chi-hinh-cua-chinh-video`, [[quy-tac-noi-dung-cua-david]].

Gốc: khối 1 (Bóc tách) của tu-duy-goc.md — mỗi video là một phần riêng, hình lấy từ video khác làm lẫn hai nội dung và sai với chính video đó.
