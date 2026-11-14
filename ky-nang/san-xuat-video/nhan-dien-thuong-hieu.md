---
description: "Bộ định tuyến loại video: bước lọc, nhận diện loại (nói trước camera, vlog, podcast, highlight) → skill nào."
---

# Nhận diện loại video (bộ định tuyến — một chỗ duy nhất)

**Bước 0: BỘ LỌC NỘI DUNG** — `mo-dun/00-sang-loc-noi-dung`. David chỉ đưa tài nguyên, không kèm yêu cầu: chép lời → chấm theo hồ sơ
`~/.claude/david.md` → phiếu lọc (kết luận, kênh, dạng, độ dài) → 4 phần gọn lấy từ phiếu lọc, David duyệt (`phan-phoi-da-kenh` bước 0)
→ dựng một mạch theo loại dưới đây.
Kết luận ⛔ / 👤 / 🗂 thì KHÔNG dựng video (tiết kiệm thời gian — điều David kiêng nhất).

| Đầu vào David đưa | Loại | Công thức (skill) | Hồ sơ |
|---|---|---|---|
| 1 video có người nói trước camera | **Làm video** | `dung-video-theo-phong-cach` (chế độ 1 video) | `ho-so-thuong-hieu/lam-video` |
| ≥ 2 clip, hoặc 1 clip sự kiện / đi lại (không phải nói trước camera) | **Ghép vlog** | `dung-video-theo-phong-cach` (chế độ ghép — `references/nhieu-doan-video.md`) | `ho-so-thuong-hieu/ghep-vlog` |
| File tiếng, hoặc video podcast David không muốn dùng hình | **Podcast** | `dung-podcast` | `ho-so-thuong-hieu/podcast` |
| 1 video dài / thư mục dự án cũ + "cắt highlight / clip ngắn / Reels" | **Highlight** | `cat-doan-noi-bat` | `ho-so-thuong-hieu/doan-noi-bat` |

Điểm cần chốt trong 4 phần (`thu-thap-yeu-cau`, chỉ cái thật sự thiếu, kèm đề xuất): video > 3 phút → "có đăng YouTube không?" (bật màn kết,
chương, teaser, thumbnail nếu khung ngang) · podcast → tên chương trình / ảnh người nói · highlight → tên tập gốc nếu không có.
Không rõ loại (vd. 1 clip vừa nói vừa đi) → chọn theo việc người xem thấy nhiều nhất: người nói vào máy → Làm video; cảnh đi lại → Ghép vlog.
