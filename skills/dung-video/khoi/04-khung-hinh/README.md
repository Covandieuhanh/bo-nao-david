# Khối 04-khung-hinh: Khung hình: đổi khung (ngang↔dọc), nâng khung khi người nằm thấp

**Dùng trong:** làm video, ghép vlog, highlight người nói (podcast: khung xuất riêng)
**Đầu vào:** davinci/media/video_goc.mp4
**Đầu ra:** video_goc.mp4 đổi khung / nâng (bản trước giữ lại) · lift.js (ghép)
**Tham số hồ sơ:** —
**Sửa khối này → chạy lại:** 05 (dò mặt lại trên bản đã nâng), 17

**File thật (code, một bản duy nhất):**
- `video-style-edit/scripts/reframe_analyze.sh`
- `video-style-edit/scripts/reframe_plan.py`
- `video-style-edit/scripts/set_output.py`
- `video-style-edit/scripts/pillar_base.py`
- `video-style-edit/scripts/lift.py`
- `video-style-edit/scripts/faces.swift`

## Cách làm (chuyển nguyên văn từ SKILL.md cũ — ngày 2026-11-04)

**3b. Đổi khung** (chỉ khi khung xuất khác khung gốc — xem bảng ở "Đầu vào"):

*Ngang → dọc* — sau 3a, trên bản sạch:
```bash
zsh $SKILL/scripts/reframe_analyze.sh "$P"           # chạy nền; lần đầu biên dịch bộ dò mặt ~2 phút
```
Dò mặt bằng Vision của macOS (không cài gì thêm), gom thành người A, B… (từ trái sang), đoán người nói từng câu
theo độ cử động miệng. Xem `check/reframe/tracks.jpg` (ô màu = ai là ai), `plan.md` (shot, người, ✓/?),
`shots.jpg` (khung vàng = phần giữ lại). Sửa `plan.json` khi cần: shot `?` → đọc câu nói để biết ai nói;
người bị khung cắt nửa mặt → đặt `cx` (0–1); slide/cảnh rộng/vật cần thấy → `target: "wide"`; người đi lại → `follow: true`.
Sau khi sửa: `python3 -I $SKILL/scripts/reframe_plan.py "$P" sheet` để xem lại. Rồi:
```bash
python3 -I $SKILL/scripts/reframe_plan.py "$P" apply  # → video_goc.mp4 dọc 1080×1920; bản ngang giữ là video_goc_ngang.mp4
```
Từ đây dự án là dự án dọc bình thường (vùng an toàn Reels/TikTok, lớp phủ dưới mặt). Video ngang 1080p chỉ còn
~608 px chiều ngang sau khi cắt → hình mềm hơn; báo người dùng (quay 4K sẽ nét).

*Dọc → ngang*:
```bash
python3 -I $SKILL/scripts/set_output.py "$P" pillar   # ghi motion/src/output.js
```
Thiết kế cảnh vẫn trên khung dọc như mọi khi (component không đổi); `layout.js` tự đặt vào khung ngang.
Thêm `SIDES` vào scenes.js ở bước 5.

**3b'. Nâng khung** — khung dọc 1080×1920 (gốc dọc, hoặc sau ngang → dọc), luôn chạy:
```bash
python3 -I $SKILL/scripts/lift.py "$P"           # chỉ in kế hoạch → check/faces/lift.md (mức nâng theo từng cửa sổ 4 s)
python3 -I $SKILL/scripts/lift.py "$P" apply     # nung vào video_goc.mp4 (bản trước giữ là video_goc_truoc_nang.mp4)
```
Mặt nằm thấp (tâm > ~900 px hoặc cằm lọt dải phụ đề) → đẩy hình lên theo bậc 100 px, tối đa 400, đổi mức trượt 0,6 s; đáy
hở là chính hình đó làm mờ. Toàn bảng 0 → "không cần nâng", bỏ qua. Xem 1–2 khung sau khi nung (mặt không chạm đỉnh vùng an
toàn). Chạy lại sau khi sửa cuts → tự tính từ bản chưa nâng. Phải chạy TRƯỚC 3c và `face_place.sh` (mặt dò lại trên bản đã nâng).

## Khung xuất

| Nguồn | Xuất mặc định |
|---|---|
| Chỉ có tiếng | Dọc 1080×1920 |
| Video dọc | Dọc 1080×1920 |
| Video ngang | **Ngang 1920×1080** |

**Khung ngang là thiết kế toàn khung 16:9** (người dùng chốt) — sân khấu, lớp phủ, cảnh toàn màn hình đều vẽ cho khung ngang;
KHÔNG chia 3 cột kiểu pillar của skill gốc, KHÔNG dùng `set_output.py`/`SIDES`/`hai-ben`. Người dùng muốn khung khác nguồn →
tham số 3 của new_podcast.sh (`doc` | `ngang`). Đổi khung sau khi đã làm → sửa `width/height` trong `motion/src/project.js`
(1080×1920 ↔ 1920×1080), chụp thử lại, render lại tất cả. Hình học hai khung ở `motion/src/podframe.js`.
Khung ngang có bản riêng cho `montage`, `gens`, `build` (FullScreenLand.jsx); `recap`, `converge`, `master` chỉ có bản dọc →
không dùng ở khung ngang. Thẻ/chữ to/hook vẽ trên dải 830×435 như cũ, `Place` phóng 1,25× đặt canh trái phía trên.

