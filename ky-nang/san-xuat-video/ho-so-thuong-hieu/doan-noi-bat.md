---
description: "Hồ sơ tham số loại highlight: hình mẫu chính, nhịp cắt, thẻ."
---

# Hồ sơ: Highlight

**Hình mẫu chính:** clip Have A Sip (cắt qua lại khách–người dẫn 2–3 s, chip show + lịch, thẻ "nghe bản full") + Sao Việt 24H (khung 0
= ảnh bìa, phụ đề nhịp chữ, tư liệu); quốc tế DOAC / Jay Shetty (thẻ tít tiền cược). Báo cáo: `cat-doan-noi-bat/references/hoc-tu-20-doan-noi-bat-vn.md`.

| Khoá | Ý nghĩa |
|---|---|
| `cat_lang.*` | lặng trong câu ít nhất `trong_cau_min_s` rút còn 2×`giu_s`; lùi/thêm `bien_cau_s`; gộp câu liền tối đa `gop_cau_lien_s`; lặng chèn sau câu hỏi kêu gọi |
| `phong_xen_ke` | đoạn xen kẽ phóng ở mối cắt — **1.0 = tắt** (quy-tac-chung mục 2); > 1 chỉ khi David yêu cầu |
| `tit_ghim` | dải tít ghim suốt clip — **false** (thêm chữ thứ 3 trên người, dọc mỗi lúc ít thứ); bật từng clip `"pin": true` |
| `the_cuoi_s` · `man_cuoi_s` · `man_cuoi_kenh` | thẻ cuối dẫn về bản đầy đủ — chỉ dùng khi xuất dọc dài; video dọc ngắn không thẻ cuối |
| `nhac_chu_chinh` | mức nhạc mẫu podcast đồ hoạ dọc (thấp hơn giọng khoảng 23 dB) |
| `phan_ung_s` | cảnh phản ứng người nghe |
