---
description: "Âm thanh theo bố cục: vị trí đặt tiếng ký hiệu, tiếng ting, tiếng vút theo từng cảnh."
---

# Âm thanh theo bố cục

File này chỉ ghi **vị trí đặt** tiếng. Tiếng dùng là bộ hiệu ứng âm thanh của kênh (`dung-video-theo-phong-cach/assets/hieu-ung-am-thanh`: `ting`, `tua`, `sting`, nhạc theo tuyến ở khối 09).
Mức âm lượng theo chuẩn chung (khối 09). Khi học thêm cách đặt mới, người làm thêm một dòng vào bảng và ghi nguồn.

| Lúc | Cách đặt | Học từ | Code |
|---|---|---|---|
| Thẻ / chữ quan trọng hiện ra | một tiếng sáng, ngắn, nhỏ (kiểu `ting`) đúng khung hình thẻ hiện lên; không đặt cho mọi dòng, chỉ đặt ở dòng then chốt | Sang Huỳnh 07/11 (phổ âm 0:01, 0:10, 0:15, 0:25) | chưa tự động (cta có `ting`) |
| Chuyển chương / màn chương | một nốt nhạc ngân khoảng 1 giây, khi lời nói chưa vào | Sang Huỳnh 07/11 (12:38, mở "Cách 3") | chưa |
| Nối bố cục (người thu nhỏ vào ô, thẻ bay vào) | tiếng lướt nhẹ, ngắn (kiểu `tua`), nhỏ hơn tiếng thẻ | Sang Huỳnh 07/11 | chưa (highlight có `tua`) |
| Suốt video kiến thức | nhạc nền rất nhỏ, đều, không có nhịp mạnh; lời nói là chính | Sang Huỳnh 07/11 | có (tuyến `kien_thuc`, khối 09) |

Khi làm code, người làm thêm vào danh sách `hieu-ung-am-thanh` trong `dung-video-theo-phong-cach/scripts/xem-truoc-ban-dung.py` theo `type: 'bocuc'` (mốc `start` của cảnh, mốc
`at` của dòng có `to: true`). Tiếng mới thì đặt ở `assets/hieu-ung-am-thanh/` và ghi nguồn, giấy phép.
