---
description: "Nguồn học Cường Mê AI (20/11): nguyên lý làm motion graphics dễ hiểu — hình theo nhịp lời, một hình lớn dần, một chỗ sáng, ít chữ."
---

# Cường Mê AI — "Bí kíp tự build xưởng phim motion graphics" (học 20/11/2026)

David duyệt hướng học: *"học để tự động áp dụng chứ không phải áp dụng máy móc y chang… học để cải tiến trên chính những gì mình
đang có… motion graphics ngày càng thể hiện rõ sự mô tả các nội dung đang được nói đến… nhưng vẫn tinh gọn, đơn giản, không cầu kỳ,
loè loẹt gây phân tán sự chú ý"*. Vì vậy lần này **học nguyên lý, nâng cấp thành phần có sẵn**, không thêm món mới.

## 1. Nguồn
- Facebook reel, kênh Cường Mê AI, 1:47, dọc 9:16, người nói + motion graphics. Đã xem cả bài bằng bảng khung 1,5 s.
- File tải về đã xoá sau khi cắt khung. Chưa phân tích kỹ âm thanh.

## 2. Vì sao dễ hiểu (nguyên lý — đã đưa vào `tu-chon.md` bước 4a)
| # | Nguyên lý | Thấy ở |
|---|---|---|
| 1 | **Hình đi đúng nhịp lời**: nói tới thứ gì thứ đó mới hiện | Câu lệnh → Viết code → Chụp frame → Ghép MP4 hiện từng nút |
| 2 | **Một hình lớn dần** thay vì nhiều hình rời: cùng sơ đồ thêm nút theo lời | sơ đồ Node · FFmpeg · Playwright → Claude, dải khung 001–006 |
| 3 | **Chỉ một chỗ sáng**: phần đang nói viền cam, phần đã qua mờ | danh sách bước, dải khung |
| 4 | **Hình đúng loại ý**: quy trình → chuỗi nút; so sánh → hai cột; liệt kê → xếp chồng | cột trước/sau, danh sách 01–05 |
| 5 | **Ít chữ, nền yên**: mỗi nút 1–3 chữ, nền tối đồng nhất | mọi cảnh |
| 6 | Dọc: **hình nửa trên, người nửa dưới** khi giải thích dài, không mất mặt người nói | phần giữa video |

## 3. Nâng cấp vào hệ có sẵn
| Có sẵn | Nâng cấp | File | Code |
|---|---|---|---|
| `diagram` | kiểu `chuoi` (chuỗi bước nối dây, chấm chạy chỉ hướng, bước đang nói sáng, bước cũ mờ) · `mot_diem: true` cho `tang`, `cot` (sáng đúng mục đang nói thay vì mục cố định) | `thu-vien/so-do.jsx` | có |
| `o-nguoi` | `nguoi_duoi: true` ở khung dọc: người xuống nửa dưới, hình nửa trên | `thanh-phan/bo-cuc.jsx` | có |
| `tu-chon.md` | bước 4a: chỉ dựng hình khi ý khó hiểu nếu chỉ nghe; dòng `Tiết chế:` trong chẩn đoán | `thiet-ke-bo-cuc/tu-chon.md` | — |
| `soat-canh.mjs` | soát: nhãn > 4 chữ · hình phủ > 45 % thời lượng · thiếu dòng `Tiết chế:` | `scripts/soat-canh.mjs` | có |

## 4. Không lấy
Màu, font, kiểu vẽ của nguồn · đồng hồ điểm chạy số (trái luật chữ nguyên văn, không số chạy) · khung điện thoại kêu gọi, nút
"Following" giả · đường cong chuyển động, đồng xu 3D, poster chữ lặp tiếng Anh (món trang trí, không giúp hiểu thêm) · ảnh AI người
nước ngoài (chỉ ảnh Việt Nam) · nhãn tự đặt kiểu "NGUYÊN LÝ" (chữ phải nguyên văn) · phụ đề chữ nhỏ viết thường (kênh giữ cụm 5–8 chữ, cỡ 58).

## 5. Ý về quy trình (để đợt riêng)
Nguồn cho Claude tự xem lại từng khung và chấm điểm, đạt 8/10 mới cho qua. Hệ David đã có `soat-canh.mjs` + xem ảnh tĩnh; chấm điểm
theo thang có thể thêm sau nếu David muốn.

## 6. Kiểm không phá
Thành phần cũ không đổi khi không bật cờ mới (`mot_diem`, `nguoi_duoi` mặc định tắt; `chuoi` là kiểu mới). Kết quả chụp thử: mục 7.

## 7. Kết quả kiểm (20/11/2026)
- Dự án thử tạm (dọc 1080×1920 + ngang 1920×1080, khuôn 1 video), vì các dự án mẫu chuẩn (`mau-chuan/mau.json`) đã chuyển lên Drive.
- **Phần cũ y nguyên:** `diagram tang`, `diagram cot`, `bocuc o-nguoi` (thẻ), `bocuc muc-luc`, chụp trước và sau khi sửa ở cả hai khung thì SSIM 1,000 (8/8 ảnh).
- **Phần mới đã xem ảnh:** `chuoi` dọc (cột) và ngang (hàng), đang chạy dây và đủ bước · `tang` + `mot_diem` · `o-nguoi` + `nguoi_duoi`
  (dọc: hình trên, người dưới; ngang: cờ bị bỏ qua, `chuoi` lồng trong ô tự xếp cột, không tràn vào ô người — đã sửa sau lần chụp đầu).
- **Máy soát:** thử đúng 3 báo mới (nhãn 7 chữ thì P1 · thiếu `Tiết chế:` thì P1 · hình phủ 63 % thì P1) và gợi ý `mot_diem` (P2).
- **Chưa kiểm:** video người nói dọc thật có dữ liệu khuôn mặt (ô người ở `nguoi_duoi` sẽ theo khung người thật) · render video trọn ·
  khuôn ghép và podcast (dùng chung `so-do.jsx` nên có `chuoi`, chưa chụp) · `kiem-mau.py` (dự án mẫu không còn trên Mac).
