# Khối 17-dung-kiem-tra: Dựng + kiểm tra: chụp thử từng cảnh, render, ghép bản cuối, soát khung / âm lượng / tiếng rè

**Dùng trong:** cả 4
**Đầu vào:** dự án đã có kịch bản
**Đầu ra:** video-final.mp4 + check/{stills,sheet}.jpg
**Tham số hồ sơ:** —
**Sửa khối này → chạy lại:** —

**File thật (code, một bản duy nhất):**
- `video-style-edit/scripts/{safe_guide.py,composite_stills.sh,check_frames.sh,render_preview.py,don_tap.py}`
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
Xem `check/sheet.jpg`: cảnh đúng chỗ, không gì lọt vùng an toàn, không lớp phủ nào che mặt, không nháy/đen. Âm thanh
(cả bài −14 LUFS, đỉnh ≤ −1,5 dB — `ebur128=peak=true`; KHÔNG so dB thô với nguồn vì giọng nhỏ được kéo lên, sửa 10/11/2026) và tiếng rè so với giọng (`-af highpass=f=12000,astats` — mức RMS bản cuối
chênh bản gốc ≤ 1 dB; cao hơn hẳn = âm thanh bị hạ bit ở đâu đó, xem gotchas) và thời lượng (= bản sạch; video KHÔNG có màn hình nguồn ảnh ở cuối).
Lỗi thì sửa cảnh đó → `node render.mjs <id>` → render_preview lại.

## Soát cảnh tự động (David duyệt 2026-11-06 — học từ `check` + `review.md` của HyperFrames)
Chạy **trước bước chụp thử** và sau mỗi lần sửa mốc / chữ:
```bash
node $SKILL/scripts/soat_canh.mjs "$P"     # in ra + ghi check/soat.md; có P0 thì mã thoát 1. Không sửa gì, không render
```
Đọc từ `scenes.js` hoặc `edl.js`, báo mỗi lỗi một dòng `t=… · cảnh · vấn đề → cách sửa`:
- **P0 (phải sửa):** kiểu cảnh / biểu tượng không tồn tại, phần tử hiện ngoài cảnh, mốc sai.
- **P1 (nên sửa):** nhãn không đủ đọc (0,5 s + 0,3 s mỗi từ), nhãn `illus` quá số chữ hồ sơ, hai cảnh toàn màn hình chồng nhau.
- **P2 (tinh chỉnh, giữ có chủ đích được):** hình đứng yên quá 3 s sau khi đọc xong, thẻ tít / màn chốt thiếu hẳn thời gian đọc, hai cảnh cùng kiểu liền nhau (trừ cảnh vẽ tiếp `tu_buoc`, khối 07).
Giới hạn: chỉ bắt lỗi đo được. Chữ tràn, che mặt, xấu vẫn soi bằng `check/stills.jpg`. **Xem tờ ảnh ở đúng cỡ (mỗi khung 240–270 px, nhỏ hơn màn điện thoại): chữ cần đọc mà không đọc được = P0.**
Câu hỏi khi soi tờ ảnh: che chữ đi, hình còn nói được ý không? Thấy mọi cảnh giống nhau thì đổi kiểu vào (khối 07). Video rối → bỏ bớt khoảng một phần ba chuyển động, giữ cái dẫn mắt.

## Kiểm cảm nhận (David chốt 2026-11-10 — học từ scroll-craft `feel.md` §6)
Claude tự làm, hai lần: sau bước chụp thử và sau bản cuối. Không gửi David chấm.
1. **Xem lạnh trước:** xem tờ ảnh theo thứ tự thời gian (bản cuối: thêm vài đoạn video quanh đỉnh), chưa mở `ke-hoach-canh.md`. Ghi một
   từ cho cảm xúc mỗi đoạn vào `check/cam-nhan.md`.
2. **Rồi mới so** với "Đường cảm xúc" trong `ke-hoach-canh.md` (khối 07): bảng ba cột `đoạn · dự định · cảm thấy`.
3. **Lệch thì video sai, không phải đường sai:** sửa cảnh (đổi kiểu, bỏ bớt hình, đưa lớn hình ở đỉnh) rồi chụp lại. Đồng thời soát:
   đỉnh có phải chỗ đổi hình lớn nhất không · đoạn trước đỉnh có lặng hơn không · màn cuối có khép lại (không tắt dần) không.
4. Báo cáo David chỉ thêm một dòng: "Cảm nhận: khớp N/M đoạn; đã sửa <đoạn>".

### Dọn file tạm khi David chốt bản cuối (David chốt 08/11/2026)

Không dọn ngay lúc render xong, mà dọn khi David nói "chốt" hoặc khi video đã đăng. Nếu tập còn cắt highlight thì dọn sau khi đã có clip, vì dọn xong thì không còn `davinci/media/video_goc.mp4` để cắt.
```bash
python3 -I $SKILL/scripts/don_tap.py --xoa <dự án>    # David chốt → chạy thẳng, KHÔNG gửi danh sách hỏi lại (David chốt 08/11/2026)
python3 -I $SKILL/scripts/don_tap.py <dự án>          # chỉ liệt kê, khi cần xem trước
```
`<dự án>` = `~/Movies/tap-<tên>` hoặc `~/Movies/vlog/<tên>`. Chỉ hỏi David khi script báo **⏸** — việc đang dở: tiến trình đang chạy
trong dự án (thường là phiên khác), file kịch bản sửa sau bản cuối mà chưa render lại, hoặc chưa có `video-final.mp4`. Phần ⏸ để
nguyên, phần còn lại vẫn dọn. Báo David một dòng: đã giải phóng bao nhiêu, Thùng rác ở đâu, phần nào bỏ qua và vì sao.
- **Giữ:** `1-goc/` · `video-final*.mp4` ở gốc mỗi dự án · `phat-hanh/` · mọi file chữ.
- **Xoá hẳn:** `node_modules` · `.remotion` · `.cache`.
- **Đưa vào Thùng rác** (David tự đổ): mọi file hình, tiếng, video còn lại.
- Dự án chưa có bản cuối thì script tự bỏ qua. Không có bản cho app chỉnh sửa (CapCut/DaVinci).
