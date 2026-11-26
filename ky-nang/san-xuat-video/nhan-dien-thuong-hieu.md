---
description: "Bộ định tuyến loại video: bước lọc, nhận diện loại (nói trước camera, vlog, podcast, highlight) và chọn skill tương ứng."
---

# Nhận diện loại video (bộ định tuyến — một chỗ duy nhất)

**Bước 0: BỘ LỌC NỘI DUNG** — `mo-dun/00-sang-loc-noi-dung`. David chỉ đưa tài nguyên, không kèm yêu cầu: Claude chép lời rồi chấm theo hồ sơ
`~/.claude/david.md`, lập phiếu lọc (kết luận, kênh, dạng, độ dài), trình 4 phần gọn lấy từ phiếu lọc để David duyệt (`phan-phoi-da-kenh` bước 0),
rồi dựng liên tục theo loại dưới đây.
Khi kết luận là ⛔ / 👤 / 🗂, Claude không dựng video (để tiết kiệm thời gian; lãng phí thời gian là điều David tránh nhất).

| Đầu vào David đưa | Loại | Công thức (skill) | Hồ sơ |
|---|---|---|---|
| 1 video có người nói trước camera | **Làm video** | `dung-video-theo-phong-cach` (chế độ 1 video) | `ho-so-thuong-hieu/lam-video` |
| ít nhất 2 clip, hoặc 1 clip sự kiện / đi lại (không phải nói trước camera) | **Ghép vlog** | `dung-video-theo-phong-cach` (chế độ ghép — `references/nhieu-doan-video.md`) | `ho-so-thuong-hieu/ghep-vlog` |
| File tiếng, hoặc video podcast David không muốn dùng hình | **Podcast** | `dung-podcast` | `ho-so-thuong-hieu/podcast` |
| 1 video dài / thư mục dự án cũ + "cắt highlight / clip ngắn / Reels" | **Highlight** | `cat-doan-noi-bat` | `ho-so-thuong-hieu/doan-noi-bat` |

Điểm cần chốt trong 4 phần (`thu-thap-yeu-cau`, chỉ hỏi điều thật sự còn thiếu, kèm đề xuất): video dài hơn 3 phút thì "có đăng YouTube không?" (bật màn kết,
chương, teaser, thumbnail nếu khung ngang) · podcast thì dùng tên chương trình / ảnh người nói · highlight thì dùng tên tập gốc nếu không có.
Khi không rõ loại (ví dụ: 1 clip vừa nói vừa đi), Claude chọn theo nội dung người xem thấy nhiều nhất: người nói vào camera thì chọn Làm video; cảnh đi lại thì chọn Ghép vlog.
