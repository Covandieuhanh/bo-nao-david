# Khối 17-dung-kiem-tra: Dựng + kiểm tra: chụp thử từng cảnh, render, ghép bản cuối, soát khung / âm lượng / tiếng rè

**Dùng trong:** cả 4
**Đầu vào:** dự án đã có kịch bản
**Đầu ra:** video-final.mp4 + check/{stills,sheet}.jpg
**Tham số hồ sơ:** —
**Sửa khối này → chạy lại:** —

**File thật (code, một bản duy nhất):**
- `video-style-edit/scripts/{safe_guide.py,composite_stills.sh,check_frames.sh,render_preview.py}`
- `…/remotion-template/{preview.mjs,render.mjs}`
- `…/montage-template/{stills.mjs,render-show.mjs}`
- `video-style-edit/references/gotchas.md`

## Cách làm (chuyển nguyên văn từ SKILL.md cũ — ngày 2026-11-04)

### 7. Dựng & kiểm tra từng cảnh (trước khi render thật)

```bash
cd "$P/motion" && node preview.mjs <id>@<giây> phu-de@<giây> <id>@<giây> phu-de@<giây> ...
```
(chụp `phu-de` cùng mốc với mỗi cảnh → composite_stills ghép phụ đề lên cảnh đó để thấy chồng lấn, nếu có)
Chụp mỗi cảnh ở khoảnh khắc "đầy nhất" (cuối cảnh, khi mọi phần tử đã hiện). Ghép lên khung video gốc + khung an toàn
bằng `python3 $SKILL/scripts/safe_guide.py "$P"` (một lần) và `zsh $SKILL/scripts/composite_stills.sh "$P"` → xem `check/stills.jpg`: chữ có tràn/xuống dòng xấu, dấu tiếng Việt
có bị cắt, **hai dòng chữ có chồng nhau / chữ có chạm khung ảnh không** (soi chữ có Ố Ễ Ỗ), **ô hiệu ứng có bị cắt ở đáy hoặc chạm phụ đề không**
(lớp phủ bị chặn cứng ở đỉnh dải phụ đề — thấy bị cắt thì rút nội dung), có gì lọt vùng đỏ, **lớp phủ có đè lên mặt/đầu người nói không** (script dò mặt theo khung 0,5 s — cử động
nhanh vẫn có thể lọt; thấy đè thì đặt tay `place`), chữ có đọc được trên nền, cảnh có khớp lời nói không. Sửa rồi chụp lại tới khi sạch.
Đây là bước tiết kiệm nhất — sửa ở đây rẻ hơn nhiều so với sau khi render.
Khung ngang (pillar): trước khi chụp, dựng nền ngang một lần —
`node render.mjs hai-ben` (~1 phút / phút video) rồi `python3 -I $SKILL/scripts/pillar_base.py "$P"` → `nen_ngang.mp4`;
composite_stills tự dùng nền này. Chụp thêm `hai-ben@<giây>` ở vài mốc để kiểm chữ hai bên (tràn, xuống dòng xấu).
Đổi `SIDES` hoặc mốc cảnh → render lại `hai-ben` + `pillar_base.py`.

### 8. Render, đóng gói, xuất bản cuối

```bash
cd "$P/motion" && node render.mjs                                  # chạy nền; ~10–40 s mỗi cảnh
python3 -I $SKILL/scripts/pillar_base.py "$P"                      # chỉ khi xuất ngang từ gốc dọc (sau khi render hai-ben)
python3 -I $SKILL/scripts/credits_card.py "$P"                     # chỉ khi có dùng ảnh → nguon-anh.txt (dán vào mô tả)
python3 -I $SKILL/scripts/render_preview.py "$P"                   # chạy nền → video-final.mp4
```

### 9. Kiểm tra bản cuối

```bash
zsh $SKILL/scripts/check_frames.sh "$P" "$P/video-final.mp4" <các mốc giây: giữa & cuối mỗi cảnh, vài chỗ không có cảnh, màn hình nguồn>
```
Xem `check/sheet.jpg`: cảnh đúng chỗ, không gì lọt vùng an toàn, không lớp phủ nào che mặt, không nháy/đen. So âm lượng với bản gốc
(`ffmpeg -i ... -af volumedetect -f null -`, chênh ≤ 0,5 dB) và tiếng rè (`-af highpass=f=12000,astats` — mức RMS bản cuối
chênh bản gốc ≤ 1 dB; cao hơn hẳn = âm thanh bị hạ bit ở đâu đó, xem gotchas) và thời lượng (= bản sạch; video KHÔNG có màn hình nguồn ảnh ở cuối).
Lỗi thì sửa cảnh đó → `node render.mjs <id>` → render_preview lại.

