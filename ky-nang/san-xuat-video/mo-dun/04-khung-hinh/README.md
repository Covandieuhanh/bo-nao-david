---
description: "Khối 04 khung hình: đổi khung giữa ngang và dọc, bám theo người nói, nâng khung."
---

# Khối 04-khung-hinh: Khung hình: đổi khung (ngang↔dọc), nâng khung khi người nói nằm thấp trong khung

**Dùng trong:** làm video, ghép vlog, highlight người nói (podcast có khung xuất riêng)
**Đầu vào:** tu-lieu/video-goc.mp4
**Đầu ra:** video-goc.mp4 đã đổi khung hoặc đã nâng (bản trước được giữ lại) · nang-lop.js (ghép)
**Tham số hồ sơ:** —
**Sửa khối này thì chạy lại:** 05 (phát hiện khuôn mặt lại trên bản đã nâng), 17

**File thật (mã nguồn, một bản duy nhất):**
- `dung-video-theo-phong-cach/scripts/phan-tich-doi-khung.sh`
- `dung-video-theo-phong-cach/scripts/ke-hoach-doi-khung.py`
- `dung-video-theo-phong-cach/scripts/dat-dau-ra.py`
- `dung-video-theo-phong-cach/scripts/nen-cot.py`
- `dung-video-theo-phong-cach/scripts/nang-khung.py`
- `dung-video-theo-phong-cach/scripts/nhan-dien-khuon-mat.swift`

## Cách làm

**Đổi khung** (chỉ làm khi khung xuất khác khung gốc theo bảng "Khung xuất" bên dưới, hoặc khi David yêu cầu):

*Ngang sang dọc* (làm sau bước làm sạch, trên bản đã làm sạch):
```bash
zsh $SKILL/scripts/phan-tich-doi-khung.sh "$P"           # chạy nền; lần đầu biên dịch bộ dò mặt ~2 phút
```
Phát hiện khuôn mặt bằng `do-mat.sh` (trên Mac dùng Vision, không cần cài thêm; trên thiết bị khác dùng YuNet + MediaPipe quy đổi theo thang đo của Vision), gom thành người A, B… (tính từ trái sang), đoán người nói của từng câu
theo độ cử động của miệng. **Hai người ngồi xa máy quay (mặt nhỏ hơn khoảng 6 % khung, quay ở quán, buổi 1:1)**: khi đoán bằng cử động miệng và bảng tách giọng pyannote (phân đoạn
8 s) đều sai nhiều thì đặt khung cố định vào người nói chính, dùng `follow: true` để bám theo khi người đó dịch chỗ, chỉ chuyển sang người
kia ở những câu chắc chắn là của họ (nghe lại để xác nhận); xem `canh-quay.jpg` trước khi chạy `apply`. Xem `kiem-tra/doi-khung/vet-chu-the.jpg` (ô màu cho biết ai là ai), `ke-hoach.md` (shot, người, ✓/?),
`canh-quay.jpg` (khung vàng là phần giữ lại). Sửa `ke-hoach.json` khi cần: shot đánh dấu `?` thì đọc câu nói để biết ai nói;
người bị khung cắt nửa mặt thì đặt `cx` (0–1); slide, cảnh rộng hoặc vật cần thấy thì đặt `target: "wide"`; người đi lại thì đặt `follow: true`.
Sau khi sửa, chạy `python3 -I $SKILL/scripts/ke-hoach-doi-khung.py "$P" sheet` để xem lại. Rồi chạy:
```bash
python3 -I $SKILL/scripts/ke-hoach-doi-khung.py "$P" apply  # → video-goc.mp4 dọc 1080×1920; bản ngang giữ là video-goc-ngang.mp4
```
Từ đây dự án là một dự án dọc bình thường (vùng an toàn Reels/TikTok, lớp phủ đặt dưới mặt). Video ngang 1080p chỉ còn
khoảng 608 px chiều ngang sau khi cắt nên hình kém nét hơn; Claude báo người dùng (quay 4K sẽ nét).

*Dọc sang ngang*:
```bash
python3 -I $SKILL/scripts/dat-dau-ra.py "$P" pillar   # ghi chuyen-dong/src/dau-ra.js
```
Thiết kế cảnh vẫn làm trên khung dọc như mọi khi (component không đổi); `bo-cuc.js` tự đặt cảnh vào khung ngang.
Thêm `SIDES` vào canh.js ở bước 5.

**Nâng khung** — áp cho khung dọc 1080×1920 (gốc dọc, hoặc sau khi đổi ngang sang dọc), luôn chạy:
```bash
python3 -I $SKILL/scripts/nang-khung.py "$P"           # chỉ in kế hoạch → kiem-tra/khuon-mat/lift.md (mức nâng theo từng cửa sổ 4 s)
python3 -I $SKILL/scripts/nang-khung.py "$P" apply     # nung vào video-goc.mp4 (bản trước giữ là video-goc-truoc-nang.mp4)
```
Mặt nằm thấp (tâm nằm dưới mốc khoảng 900 px hoặc cằm tràn vào dải phụ đề) thì script đẩy hình lên theo bậc 100 px, tối đa 400, đổi mức bằng trượt 0,6 s; đáy
hở được lấp bằng chính hình đó làm mờ. Toàn bảng bằng 0 thì script báo "không cần nâng", bỏ qua bước này. Xem 1–2 khung sau khi ghi cố định vào video (mặt không chạm đỉnh vùng an
toàn). Chạy lại sau khi sửa cuts thì script tự tính từ bản chưa nâng. Phải chạy TRƯỚC bước hiểu video (khối 01) và trước `vi-tri-khuon-mat.sh` (khuôn mặt được nhận diện lại trên bản đã nâng).

## Khung chủ thể (tập trung một vùng, bỏ chi tiết thừa)

Khi chủ thể cần xem (màn hình điện thoại hoặc laptop, bảng, vật, người nhỏ giữa khung rộng) chỉ chiếm phần nhỏ của khung hoặc quanh nó có chi tiết thừa thì tách
chủ thể thành **khung bo góc viền cam trên nền kênh**; phần khung còn lại dành cho phụ đề, bảng ghi chú chạy, cảnh đặt cạnh chủ thể. Khung xuất
giữ nguyên. Chạy sau bước làm sạch, trước `vi-tri-khuon-mat.sh`:
```bash
python3 -I $SKILL/scripts/khung-chu-the.py "$P" luoi [giây …]   # → kiem-tra/khung/luoi.jpg (lưới 10 %) — đọc toạ độ chủ thể
# ghi kiem-tra/khung.json: {"phia": "trai", "vung": [{"tu": 0, "x": 312, "y": 45, "w": 700, "h": 990}, {"tu": 271.8, "x": 442, "y": 45}]}
python3 -I $SKILL/scripts/khung-chu-the.py "$P" apply           # → video-goc.mp4 mới (bản trước: video-goc-truoc-khung.mp4) + chuyen-dong/src/khung.js
```
Máy quay dịch chỗ thì thêm vùng theo mốc giây (cùng w, h). `vi-tri-nhan.py` đọc `khung.js`: "người" chính là khung chủ thể (không cần Vision phát hiện khuôn mặt
trong màn hình). **Không cắt và phóng cả khung để bỏ chi tiết thừa** vì chi tiết thừa vẫn còn quanh chủ thể. Không tạo liên kết cứng giữa bản
nguồn và `video-goc.mp4` (ffmpeg sẽ ghi đè lên chính file nguồn; script đã chặn trường hợp này).

## Khung xuất

| Nguồn | Xuất mặc định |
|---|---|
| Chỉ có tiếng | Dọc 1080×1920 |
| Video dọc | Dọc 1080×1920 |
| Video ngang | **Ngang 1920×1080** |

**Podcast: khung ngang là thiết kế toàn khung 16:9** — sân khấu, lớp phủ, cảnh toàn màn hình đều được vẽ cho khung ngang;
KHÔNG chia 3 cột kiểu pillar, KHÔNG dùng `dat-dau-ra.py`/`SIDES`/`hai-ben`. David muốn khung khác khung nguồn thì dùng
tham số thứ 3 của tao-podcast.sh (`doc` | `ngang`). Đổi khung sau khi đã dựng thì sửa `width/height` trong `chuyen-dong/src/du-an.js`
(1080×1920 ↔ 1920×1080), chụp thử lại, render lại tất cả. Hình học của hai khung nằm ở `chuyen-dong/src/khung-podcast.js`.
Khung ngang có bản riêng cho `montage`, `gens`, `build` (toan-man-hinh-ngang.jsx); `recap`, `converge`, `master` chỉ có bản dọc nên
không dùng ở khung ngang. Thẻ, chữ to, hook vẫn vẽ trên dải 830×435 như cũ; `Place` phóng 1,25× và đặt canh trái phía trên.

