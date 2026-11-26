---
description: "Hồ sơ tham số chung cả 4 loại video: khoá, ý nghĩa, nguồn."
---

# Hồ sơ chung (cả 4 loại)

| Khoá | Ý nghĩa | Nguồn |
|---|---|---|
| `hai_trang_thai` | **false** = bố cục tự cân theo `thiet-ke-bo-cuc/` (không chế độ 2 trạng thái) | David |
| `phu_de.*` | video ngắn (tối đa `ngan_max_s`): cụm tối đa `ngan_max_chu` chữ (đẹp nhất 5–8), cỡ `ngan_co` = 58 bằng chữ thẻ, tối đa `ngan_max_ky_tu` ký tự (2 dòng) | David |
| `canh_minh_hoa.*` | nhịp hiện / ẩn (thẩm mỹ): giữ ít nhất `giu_sau_s` sau khi phần tử cuối hiện xong (+`giu_moi_chu_s`/chữ vượt 3) — thư viện `giu.js`. Không trần độ dài cảnh, không giới hạn số chữ nhãn | Mayer (thừa chữ), Pháp Hoà; Kurzgesagt, Vox, phụ đề Netflix |
| `nhac.*` | bảng tuyến nội dung → bài (bắt buộc `project.tuyen`), mức cân từng bài `nhac.muc`, chuẩn âm lượng chung (nhạc khoảng 23 dB dưới giọng, cả bài −14 LUFS — khối 09) | David; Hieu Nguyen, Have A Sip, 3 clip "Đi trainer" |
| `youtube.*` | video > 180 s đăng YouTube: màn kết 20 s; > 600 s: teaser 15–25 s | 11/30 video dài Việt có màn kết |
| `thumbnail.*` | tối đa 8 chữ, tối đa 3 tầng | 10/10 video dài Việt |

Các khoá giới hạn tối đa bắt buộc về bố cục (`toan_man_max_s`, `mat_hien_min`, `mat_do_canh_s`) không dùng: code thiếu khoá thì không chặn.
