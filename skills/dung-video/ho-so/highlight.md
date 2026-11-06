# Hồ sơ: Highlight

**Hình mẫu chính:** clip Have A Sip (cắt qua lại khách–người dẫn 2–3 s, chip show + lịch, thẻ "nghe bản full") + Sao Việt 24H (khung 0
= ảnh bìa, phụ đề nhịp chữ, tư liệu); quốc tế DOAC / Jay Shetty (thẻ tít tiền cược). Báo cáo: `cat-highlight-video/references/hoc-tu-20-highlight-vn.md`.

| Khoá | Ý nghĩa |
|---|---|
| `cat_lang.*` | lặng trong câu ≥ `trong_cau_min_s` rút còn 2×`giu_s`; lùi/thêm `bien_cau_s`; gộp câu liền ≤ `gop_cau_lien_s`; lặng chèn sau câu hỏi kêu gọi |
| `phong_xen_ke` | đoạn xen kẽ phóng (jump cut) |
| `tit_ghim` | dải tít ghim suốt clip — **false** theo 2 trạng thái (thêm chữ thứ 3 trên người); bật lại từng clip `"pin": true` |
| `the_cuoi_s` | thẻ cuối dẫn về bản đầy đủ |
| `phan_ung_s` | cảnh phản ứng người nghe |

## Nhật ký
- 2026-11-06 · thêm `man_cuoi_kenh`: màn hình cuối clip dọc ghi tên kênh, không logo nền tảng.
- 2026-11-06 · thêm `nhac_chu_chinh`, `man_cuoi_s` (khuôn podcast đồ hoạ dọc, David chọn bản nhạc thấp hơn giọng khoảng 23 dB).
- 2026-11-04 · `tit_ghim` true → false (David chốt 2 trạng thái: người + phụ đề / minh hoạ toàn màn hình).
