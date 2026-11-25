---
description: "Khối 04 khung hình: đổi khung ngang ↔ dọc, bám người nói, nâng khung."
---

# Khối 04-khung-hinh: Khung hình: đổi khung (ngang↔dọc), nâng khung khi người nằm thấp

**Dùng trong:** làm video, ghép vlog, highlight người nói (podcast: khung xuất riêng)
**Đầu vào:** tu-lieu/video-goc.mp4
**Đầu ra:** video-goc.mp4 đổi khung / nâng (bản trước giữ lại) · nang-lop.js (ghép)
**Tham số hồ sơ:** —
**Sửa khối này thì chạy lại:** 05 (dò mặt lại trên bản đã nâng), 17

**File thật (code, một bản duy nhất):**
- `dung-video-theo-phong-cach/scripts/phan-tich-doi-khung.sh`
- `dung-video-theo-phong-cach/scripts/ke-hoach-doi-khung.py`
- `dung-video-theo-phong-cach/scripts/dat-dau-ra.py`
- `dung-video-theo-phong-cach/scripts/nen-cot.py`
- `dung-video-theo-phong-cach/scripts/nang-lop.py`
- `dung-video-theo-phong-cach/scripts/nhan-dien-khuon-mat.swift`

## Cách làm

**Đổi khung** (chỉ khi khung xuất khác khung gốc — bảng "Khung xuất" dưới, hoặc David yêu cầu):

*Ngang thì dọc* — sau làm sạch, trên bản sạch:
```bash
zsh $SKILL/scripts/phan-tich-doi-khung.sh "$P"           # chạy nền; lần đầu biên dịch bộ dò mặt ~2 phút
```
Dò mặt bằng `do-mat.sh` (Mac: Vision, không cài gì thêm; máy khác: YuNet + MediaPipe quy đổi theo thước Vision), gom thành người A, B… (từ trái sang), đoán người nói từng câu
theo độ cử động miệng. **Hai người ngồi xa máy (mặt < khoảng 6 % khung, quán, buổi 1:1)**: đoán bằng miệng và bảng tách giọng pyannote (phân đoạn
8 s) đều sai nhiều thì khung cố định người nói chính, `follow: true` để bám khi người đó dịch chỗ, chỉ chuyển sang người
kia ở câu chắc chắn của họ (nghe lại); xem `canh-quay.jpg` trước `apply`. Xem `kiem-tra/doi-khung/vet-chu-the.jpg` (ô màu = ai là ai), `ke-hoach.md` (shot, người, ✓/?),
`canh-quay.jpg` (khung vàng = phần giữ lại). Sửa `ke-hoach.json` khi cần: shot `?` thì đọc câu nói để biết ai nói;
người bị khung cắt nửa mặt thì đặt `cx` (0–1); slide/cảnh rộng/vật cần thấy thì `target: "wide"`; người đi lại thì `follow: true`.
Sau khi sửa: `python3 -I $SKILL/scripts/ke-hoach-doi-khung.py "$P" sheet` để xem lại. Rồi:
```bash
python3 -I $SKILL/scripts/ke-hoach-doi-khung.py "$P" apply  # → video-goc.mp4 dọc 1080×1920; bản ngang giữ là video-goc-ngang.mp4
```
Từ đây dự án là dự án dọc bình thường (vùng an toàn Reels/TikTok, lớp phủ dưới mặt). Video ngang 1080p chỉ còn
khoảng 608 px chiều ngang sau khi cắt thì hình mềm hơn; báo người dùng (quay 4K sẽ nét).

*Dọc thì ngang*:
```bash
python3 -I $SKILL/scripts/dat-dau-ra.py "$P" pillar   # ghi chuyen-dong/src/dau-ra.js
```
Thiết kế cảnh vẫn trên khung dọc như mọi khi (component không đổi); `bo-cuc.js` tự đặt vào khung ngang.
Thêm `SIDES` vào canh.js ở bước 5.

**Nâng khung** — khung dọc 1080×1920 (gốc dọc, hoặc sau ngang thì dọc), luôn chạy:
```bash
python3 -I $SKILL/scripts/nang-lop.py "$P"           # chỉ in kế hoạch → kiem-tra/khuon-mat/lift.md (mức nâng theo từng cửa sổ 4 s)
python3 -I $SKILL/scripts/nang-lop.py "$P" apply     # nung vào video-goc.mp4 (bản trước giữ là video-goc-truoc-nang.mp4)
```
Mặt nằm thấp (tâm > khoảng 900 px hoặc cằm lọt vào dải phụ đề) thì đẩy hình lên theo bậc 100 px, tối đa 400, đổi mức trượt 0,6 s; đáy
hở là chính hình đó làm mờ. Toàn bảng 0 thì "không cần nâng", bỏ qua. Xem 1–2 khung sau khi nung (mặt không chạm đỉnh vùng an
toàn). Chạy lại sau khi sửa cuts thì tự tính từ bản chưa nâng. Phải chạy TRƯỚC bước hiểu video (khối 01) và `vi-tri-khuon-mat.sh` (mặt dò lại trên bản đã nâng).

## Khung chủ thể (tập trung một vùng, bỏ rác)

Chủ thể cần xem (màn hình điện thoại / laptop, bảng, vật, người nhỏ giữa khung rộng) chiếm phần nhỏ khung hoặc quanh có rác thì tách
chủ thể thành **khung bo góc viền cam trên nền kênh**; phần khung còn lại cho phụ đề, bảng ghi chú chạy, cảnh cạnh chủ thể. Khung xuất
giữ nguyên. Chạy sau làm sạch, trước `vi-tri-khuon-mat.sh`:
```bash
python3 -I $SKILL/scripts/khung-chu-the.py "$P" luoi [giây …]   # → kiem-tra/khung/luoi.jpg (lưới 10 %) — đọc toạ độ chủ thể
# ghi kiem-tra/khung.json: {"phia": "trai", "vung": [{"tu": 0, "x": 312, "y": 45, "w": 700, "h": 990}, {"tu": 271.8, "x": 442, "y": 45}]}
python3 -I $SKILL/scripts/khung-chu-the.py "$P" apply           # → video-goc.mp4 mới (bản trước: video-goc-truoc-khung.mp4) + chuyen-dong/src/khung.js
```
Máy quay dịch thì thêm vùng theo mốc giây (cùng w, h). `vi-tri-nhan.py` đọc `khung.js`: "người" = khung chủ thể (không cần Vision dò mặt
trong màn hình). **Không cắt-phóng cả khung để bỏ rác** vì rác vẫn còn quanh chủ thể. Không tạo liên kết cứng giữa bản
nguồn và `video-goc.mp4` (ffmpeg ghi đè chính nguồn — script đã chặn).

## Khung xuất

| Nguồn | Xuất mặc định |
|---|---|
| Chỉ có tiếng | Dọc 1080×1920 |
| Video dọc | Dọc 1080×1920 |
| Video ngang | **Ngang 1920×1080** |

**Podcast: khung ngang là thiết kế toàn khung 16:9** — sân khấu, lớp phủ, cảnh toàn màn hình đều vẽ cho khung ngang;
KHÔNG chia 3 cột kiểu pillar, KHÔNG dùng `dat-dau-ra.py`/`SIDES`/`hai-ben`. David muốn khung khác nguồn thì 
tham số 3 của tao-podcast.sh (`doc` | `ngang`). Đổi khung sau khi đã làm thì sửa `width/height` trong `chuyen-dong/src/du-an.js`
(1080×1920 ↔ 1920×1080), chụp thử lại, render lại tất cả. Hình học hai khung ở `chuyen-dong/src/khung-podcast.js`.
Khung ngang có bản riêng cho `montage`, `gens`, `build` (toan-man-hinh-ngang.jsx); `recap`, `converge`, `master` chỉ có bản dọc nên
không dùng ở khung ngang. Thẻ/chữ to/hook vẽ trên dải 830×435 như cũ, `Place` phóng 1,25× đặt canh trái phía trên.

