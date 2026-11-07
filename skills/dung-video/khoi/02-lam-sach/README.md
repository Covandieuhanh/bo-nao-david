# Khối 02-lam-sach: Làm sạch: cắt thừa đầu/cuối, câu nói lại, khoảng lặng + tiếng đệm, sửa chiều hình

**Dùng trong:** làm video, highlight (cắt lặng trong câu)
**Đầu vào:** davinci/media/video_goc_raw.*
**Đầu ra:** davinci/media/video_goc.mp4 (bản sạch) + check/clean/{cuts.json, cuts.md, segments.json}
**Tham số hồ sơ:** lam-video: cat_lang.*, highlight: cat_lang.*
**Sửa khối này → chạy lại:** 01 (chép lời trên bản sạch), 03, 04, 05, mọi mốc cảnh (dời theo segments.json)

**File thật (code, một bản duy nhất):**
- `video-style-edit/scripts/clean_analyze.sh`
- `video-style-edit/scripts/clean_suggest.py`
- `video-style-edit/scripts/clean_apply.py`
- `cat-highlight-video/scripts/pauses.py`

## Cách làm (chuyển nguyên văn từ SKILL.md cũ — ngày 2026-11-04)

**VIDEO DÀI > 3 PHÚT KHÔNG CẮT GÌ** (David chốt 2026-11-05, luat-chung 2): `clean_suggest.py` tự để mọi cut `ok: false` (chỉ liệt kê). Chỉ sửa chiều
hình khi cần; không đổi cut nào thành `true` trừ đoạn lằn ranh David đã chọn cắt.
**Làm lại video cũ (David 08/11/2026):** được cắt màn tít + lời chào / giới thiệu kênh cũ (đặt cut tay `ok: true`, mọi cut tự động `ok: false`,
`zoom: "none"`); chữ / viền kênh cũ in trong hình → cắt khung (gotchas). Sau `clean_apply.py` dùng `doi_moc_loi.py "$P"` thay cho chép lại. Các luật cắt dưới đây chỉ cho video ≤ 3 phút.

**3a. Làm sạch** — luôn làm, kể cả khi video trông ổn (không có gì để cắt thì bản sạch chỉ là bản mã hoá lại):
```bash
zsh $SKILL/scripts/clean_analyze.sh "$P"          # chạy nền, ~2–4 phút cho video 3–4 phút
```
Đọc `check/clean/cuts.md` và xem `orient.jpg`, `head.jpg`, `tail.jpg`, rồi chỉnh `check/clean/cuts.json`:
- **Chiều hình** (`orient`): mặt đất ở trên → `["180"]`; nằm ngang → `["cw"]`/`["ccw"]` (xoay sao cho đầu người
  hướng lên); chữ trên áo/biển bị ngược như soi gương → thêm `"mirror"`. Không chắc thì để trống.
- **Đầu/cuối** (ok sẵn): kiểm `head.jpg`/`tail.jpg` — đang đi về chỗ, chỉnh máy, "ok bắt đầu nhé", "vậy thôi"
  rồi với tay tắt máy → dời `start`/`end` của cut cho gọn hơn. Câu chào mở đầu thật thì giữ;
  cười/vẫy tay chào sau câu cuối là phần kết → giữ (dời `start` của cut thừa cuối ra sau, hoặc bỏ cut).
- **Khoảng lặng: CẮT sẵn** (`ok: true`, luat-chung 2) — video ≤ 3 phút: lặng ≥ 0,45 s + tiếng đệm "ờ/ừm"; video > 3 phút: chỉ lặng ≥ 1,2 s (còn 0,5 s), giữ tiếng đệm.
  Soát `cuts.md`: lặng ngay sau câu hỏi tu từ / trước cú chốt cảm xúc mà khoảng ngừng là chủ ý → đổi `ok: false` để giữ.
  David muốn bản tự nhiên → chạy `clean_analyze.sh "$P" tu-nhien` (chỉ liệt kê lặng ≥ 3 s, không cắt).
- **Nói lại** (`ok: false`): đọc `words.srt` quanh mốc; đúng là bỏ dở rồi nói lại → giữ **lần nói sau cùng**, đặt
  `start` = đầu lần nói hỏng, `end` = ngay trước lần nói giữ lại (cắt giữa hai từ), `ok: true`. Thêm cut tay cho
  lần nói lại mà script không bắt được (câu bỏ dở giữa chừng rồi nói lại khác chữ).
  Nghi ngờ thì **giữ** — cắt mất ý người nói tệ hơn để thừa một nhịp.
```bash
python3 -I $SKILL/scripts/clean_apply.py "$P"     # chạy nền → davinci/media/video_goc.mp4 (bản sạch)
```
Bản thô giữ lại là `video_goc_raw.<ext>`; `project.js` tự trỏ sang bản sạch, mọi bước sau dùng bản sạch.
`zoom: "alt"` phóng 1,08× xen kẽ từng đoạn để mối cắt thành cú "đẩy máy" (jump cut kiểu Ali Abdaal) thay vì giật hình
(`"none"` nếu mẫu không có kiểu này). Xem 2–3 mối nối (mốc in cuối `cuts.md`) bằng `check_frames.sh` với khung
ngay trước/sau mối: mặt không bị cắt, không nháy đen. Báo cáo cuối liệt kê đã cắt gì (`cuts.md`).

