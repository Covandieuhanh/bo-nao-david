# Hồ sơ chung (cả 4 loại)

| Khoá | Ý nghĩa | Nguồn |
|---|---|---|
| `hai_trang_thai` | true = chỉ 2 trạng thái: người + phụ đề / cảnh minh hoạ toàn màn hình + phụ đề (không chữ to đè người); ngoại lệ thẻ tít, màn chốt, điểm nhấn trên người `nhan` (07/11/2026) | David 2026-11-04; Wynn Trần, Pháp Hoà, Hành trình kỷ luật |
| `toan_man_max_s` | cảnh toàn màn hình chuyển từ lớp phủ dài tối đa (s) | giữ mặt ≥ 60% |
| `mat_hien_min` | tỉ lệ thời lượng mặt người nói phải hiện | luật 02/11 |
| `phu_de.*` | video ngắn (≤ `ngan_max_s`): 1–3 chữ/nhịp, cỡ `ngan_co`, ≤ `ngan_max_ky_tu` ký tự | Hormozi, DOAC, Sao Việt 24H |
| `canh_minh_hoa.*` | cảnh minh hoạ 3–5 s, nhãn ≤ 3 chữ; giữ ≥ `giu_sau_s` sau khi phần tử cuối hiện xong (+`giu_moi_chu_s`/chữ vượt 3), tối đa `dai_max_s` — thư viện `giu.js` | Mayer (thừa chữ), Pháp Hoà; Kurzgesagt, Vox, phụ đề Netflix (David 2026-11-05) |
| `nhac.*` | bảng tuyến nội dung → bài (bắt buộc `project.tuyen`) + mức nhạc: khoảng trống −20 LU, khi nói nén theo giọng → −30…−33 LU | David 2026-11-05; Hieu Nguyen, Have A Sip |
| `youtube.*` | video > 180 s đăng YouTube: màn kết 20 s; > 600 s: teaser 15–25 s | 11/30 video dài Việt có màn kết |
| `thumbnail.*` | ≤ 8 chữ, ≤ 3 tầng | 10/10 video dài Việt |

## Nhật ký
- 2026-11-04 · tạo hồ sơ từ giá trị đang dùng sau đợt học 80 video.
- 2026-11-05 · thêm `canh_minh_hoa.giu_sau_s` 1,2 s (+0,3 s/chữ vượt 3, tối đa 6 s): David thấy hình tắt ngay khi dứt lời, không kịp đọc.
- 2026-11-05 · thêm `nhac` (tuyến → bài, mức nhạc khi nói): David thấy nhạc to + sai tông ở podcast tâm sự.
