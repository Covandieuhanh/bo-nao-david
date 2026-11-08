# Hồ sơ chung (cả 4 loại)

| Khoá | Ý nghĩa | Nguồn |
|---|---|---|
| `hai_trang_thai` | **false** (07/11/2026): bỏ luật 2 trạng thái, bố cục tự cân theo `trinh-bay/` | David 2026-11-07 |
| ~~`toan_man_max_s`~~ · ~~`mat_hien_min`~~ · ~~`mat_do_canh_s`~~ | **đã bỏ** 07/11/2026: không trần cứng; code thiếu khoá = không chặn | David 2026-11-07 |
| `phu_de.*` | video ngắn (≤ `ngan_max_s`): cụm ≤ `ngan_max_chu` chữ (đẹp nhất 5–8), cỡ `ngan_co` = 58 bằng chữ thẻ, ≤ `ngan_max_ky_tu` ký tự (2 dòng) | David chốt 2026-11-08 (thay 1–3 chữ cỡ 84 kiểu Hormozi/DOAC) |
| `canh_minh_hoa.*` | nhịp hiện / ẩn (thẩm mỹ): giữ ≥ `giu_sau_s` sau khi phần tử cuối hiện xong (+`giu_moi_chu_s`/chữ vượt 3) — thư viện `giu.js`. Độ dài cảnh, số chữ nhãn, trần dài: đã bỏ 07/11/2026 | Mayer (thừa chữ), Pháp Hoà; Kurzgesagt, Vox, phụ đề Netflix (David 2026-11-05) |
| `nhac.*` | bảng tuyến nội dung → bài (bắt buộc `project.tuyen`) + mức nhạc: khoảng trống −20 LU, khi nói nén theo giọng → −30…−33 LU | David 2026-11-05; Hieu Nguyen, Have A Sip |
| `youtube.*` | video > 180 s đăng YouTube: màn kết 20 s; > 600 s: teaser 15–25 s | 11/30 video dài Việt có màn kết |
| `thumbnail.*` | ≤ 8 chữ, ≤ 3 tầng | 10/10 video dài Việt |

## Nhật ký
- 2026-11-04 · tạo hồ sơ từ giá trị đang dùng sau đợt học 80 video.
- 2026-11-05 · thêm `canh_minh_hoa.giu_sau_s` 1,2 s (+0,3 s/chữ vượt 3, tối đa 6 s): David thấy hình tắt ngay khi dứt lời, không kịp đọc.
- 2026-11-05 · thêm `nhac` (tuyến → bài, mức nhạc khi nói): David thấy nhạc to + sai tông ở podcast tâm sự.
