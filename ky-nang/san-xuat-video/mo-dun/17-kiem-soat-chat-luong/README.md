---
description: "Khối 17 dựng và kiểm tra chất lượng: chụp thử từng cảnh, render, soát lỗi."
---

# Khối 17-kiem-soat-chat-luong: Dựng + kiểm tra: chụp thử từng cảnh, render, ghép bản cuối, soát khung / âm lượng / tiếng rè

**Dùng trong:** cả 4
**Đầu vào:** dự án đã có kịch bản
**Đầu ra:** video-hoan-chinh.mp4 + kiem-tra/{stills,sheet}.jpg
**Tham số hồ sơ:** —
**Sửa khối này → chạy lại:** —

**File thật (code, một bản duy nhất):**
- `dung-video-theo-phong-cach/scripts/{vung-an-toan.py,ghep-anh-tinh.sh,kiem-khung-hinh.sh,xem-truoc-ban-dung.py,don-tap.py,luu-drive.sh}`
- `…/khuon-remotion/{xem-truoc.mjs,xuat-video.mjs}`
- `…/khuon-dung-ghep/{anh-tinh.mjs,xuat-chuong-trinh.mjs}`
- `dung-video-theo-phong-cach/references/loi-thuong-gap.md`

## Cách làm

### Chụp thử từng cảnh (trước khi render thật)

```bash
cd "$P/chuyen-dong" && node xem-truoc.mjs <id>@<giây> phu-de@<giây> <id>@<giây> phu-de@<giây> ...
```
(chụp `phu-de` cùng mốc với mỗi cảnh → composite_stills ghép phụ đề lên cảnh đó để thấy chồng lấn, nếu có)
Chụp mỗi cảnh ở khoảnh khắc "đầy nhất" (cuối cảnh, khi mọi phần tử đã hiện). Ghép lên khung video gốc + khung an toàn
bằng `python3 $SKILL/scripts/vung-an-toan.py "$P"` (một lần) và `zsh $SKILL/scripts/ghep-anh-tinh.sh "$P"` → xem `kiem-tra/anh-tinh.jpg`: chữ có tràn/xuống dòng xấu, dấu tiếng Việt
có bị cắt, **hai dòng chữ có chồng nhau / chữ có chạm khung ảnh không** (soi chữ có Ố Ễ Ỗ), **ô hiệu ứng có bị cắt ở đáy hoặc chạm phụ đề không**
(lớp phủ bị chặn cứng ở đỉnh dải phụ đề — thấy bị cắt thì rút nội dung), có gì lọt vùng đỏ, **lớp phủ có đè lên mặt/đầu người nói không** (script dò mặt theo khung 0,5 s — cử động
nhanh vẫn có thể lọt; thấy đè thì đặt tay `place`), chữ có đọc được trên nền, cảnh có khớp lời nói không. Sửa rồi chụp lại tới khi sạch.
Chụp đúng mốc dễ lỗi (`quy-tac-chung.md` mục 8), không chụp thừa. Đây là bước tiết kiệm nhất — sửa ở đây rẻ hơn nhiều so với sau khi render.
Khung ngang (pillar): trước khi chụp, dựng nền ngang một lần —
`node xuat-video.mjs hai-ben` (khoảng 1 phút / phút video) rồi `python3 -I $SKILL/scripts/nen-cot.py "$P"` → `nen-ngang.mp4`;
composite_stills tự dùng nền này. Chụp thêm `hai-ben@<giây>` ở vài mốc để kiểm chữ hai bên (tràn, xuống dòng xấu).
Đổi `SIDES` hoặc mốc cảnh → render lại `hai-ben` + `nen-cot.py`.

### Render, đóng gói, xuất bản cuối

```bash
cd "$P/chuyen-dong" && node xuat-video.mjs                                  # chạy nền; ~10–40 s mỗi cảnh
python3 -I $SKILL/scripts/nen-cot.py "$P"                      # chỉ khi xuất ngang từ gốc dọc (sau khi render hai-ben)
python3 -I $SKILL/scripts/the-ghi-cong.py "$P"                     # chỉ khi có dùng ảnh → nguon-anh.txt (dán vào mô tả)
python3 -I $SKILL/scripts/xem-truoc-ban-dung.py "$P"                   # chạy nền → video-hoan-chinh.mp4
```

**Thời gian render thật** (đo 18–19/11/2026, Mac này, 1080p, `concurrency: 3`; báo David theo bảng này, không đoán):
| Khuôn / khung | Tốc độ | Ví dụ |
|---|---|---|
| ghép ngang 1920×1080 | khoảng 4–5,7 × độ dài | 11:45 → 44–60 phút (chạy cùng render khác: 60) · 54:30 → 5,2 giờ |
| ghép dọc 1080×1920 clip ngắn | khoảng 6–7 × độ dài | 1:19 → khoảng 8 phút |
Ổ trống cần ít nhất 2 × file ra + 5 GB (thư mục tạm `remotion-*` của Remotion); render dài làm SAU khi đã soát khớp tiếng (khối 03) và
chụp thử đủ lớp, để không phải render lại.

### Kiểm tra bản cuối

```bash
zsh $SKILL/scripts/kiem-khung-hinh.sh "$P" "$P/video-hoan-chinh.mp4" <các mốc giây: giữa & cuối mỗi cảnh, vài chỗ không có cảnh, màn hình nguồn>
```
Xem `kiem-tra/bang-anh.jpg`: cảnh đúng chỗ, không gì lọt vùng an toàn, không lớp phủ nào che mặt, không nháy/đen. Âm thanh
(cả bài −14 LUFS, đỉnh tối đa −1,5 dB — `ebur128=peak=true`; KHÔNG so dB thô với nguồn vì giọng nhỏ được kéo lên — khối 09) và tiếng rè so với giọng (`-af highpass=f=12000,astats` — mức RMS bản cuối
chênh bản gốc tối đa 1 dB; cao hơn hẳn = âm thanh bị hạ bit ở đâu đó, xem gotchas) và thời lượng (= bản sạch; video KHÔNG có màn hình nguồn ảnh ở cuối).
Lỗi thì sửa cảnh đó → `node xuat-video.mjs <id>` → render_preview lại.

## Soát cảnh tự động
Chạy **trước bước chụp thử** và sau mỗi lần sửa mốc / chữ:
```bash
node $SKILL/scripts/soat-canh.mjs "$P"     # in ra + ghi kiem-tra/soat.md; có P0 thì mã thoát 1. Không sửa gì, không render
```
Đọc từ `canh.js` hoặc `danh-sach-cat.js`, báo mỗi lỗi một dòng `t=… · cảnh · vấn đề → cách sửa`:
- **P0 (phải sửa):** kiểu cảnh / biểu tượng không tồn tại, phần tử hiện ngoài cảnh, mốc sai · **chưa chẩn đoán** (thiếu
  `ke-hoach-canh.md` mục `## Chẩn đoán`) · **cả video một kiểu lớp phủ nội dung** (trừ khi ghi `Một kiểu có chủ đích: …`). Render đầy
  đủ (`xuat-video.mjs`, `xuat-chuong-trinh.mjs`) tự chạy soát này và dừng khi còn P0 (`thiet-ke-bo-cuc/tu-chon.md` bước 5).
- **P1 (nên sửa):** nhãn không đủ đọc (0,5 s + 0,3 s mỗi từ), nhãn `illus` quá số chữ hồ sơ, hai cảnh toàn màn hình chồng nhau.
- **P2 (tinh chỉnh, giữ có chủ đích được):** hình đứng yên quá 3 s sau khi đọc xong, thẻ tít / màn chốt thiếu hẳn thời gian đọc, hai cảnh cùng kiểu liền nhau (trừ cảnh vẽ tiếp `tu_buoc`, khối 07).
Giới hạn: chỉ bắt lỗi đo được. Chữ tràn, che mặt, xấu vẫn soi bằng `kiem-tra/anh-tinh.jpg`. **Xem tờ ảnh ở đúng cỡ (mỗi khung 240–270 px, nhỏ hơn màn điện thoại): chữ cần đọc mà không đọc được = P0.**
Câu hỏi khi soi tờ ảnh: **video có rối không** — đếm số kiểu hiệu ứng cả video, kiểu nào không giúp hiểu thì bỏ (quy-tac-chung §0, hiểu hơn cầu kì) · **mỗi khung có đúng một tiêu điểm không** (nheo mắt vẫn biết nhìn vào đâu) · cam có còn là màu nhấn (khoảng 10 % khung), không phủ cả khung. Che chữ đi, hình còn nói được ý không? Thấy mọi cảnh giống nhau thì đổi kiểu vào (khối 07). Video rối → bỏ bớt khoảng một phần ba chuyển động, giữ cái dẫn mắt.

## Kiểm cảm nhận
Claude tự làm, hai lần: sau bước chụp thử và sau bản cuối. Không gửi David chấm.
1. **Xem lạnh trước:** xem tờ ảnh theo thứ tự thời gian (bản cuối: thêm vài đoạn video quanh đỉnh), chưa mở `ke-hoach-canh.md`. Ghi một
   từ cho cảm xúc mỗi đoạn vào `kiem-tra/cam-nhan.md`.
2. **Rồi mới so** với "Đường cảm xúc" trong `ke-hoach-canh.md` (khối 07): bảng ba cột `đoạn · dự định · cảm thấy`.
3. **Lệch thì video sai, không phải đường sai:** sửa cảnh (đổi kiểu, bỏ bớt hình, đưa lớn hình ở đỉnh) rồi chụp lại. Đồng thời soát:
   đỉnh có phải chỗ đổi hình lớn nhất không · đoạn trước đỉnh có lặng hơn không · màn cuối có khép lại (không tắt dần) không.
4. Báo cáo David chỉ thêm một dòng: "Cảm nhận: khớp N/M đoạn; đã sửa <đoạn>".

## Dọn file tạm và đưa tập lên Drive khi David chốt bản cuối

Không dọn ngay lúc render xong, mà dọn khi David nói "chốt" hoặc khi video đã đăng, không hỏi lại David. Nếu tập còn cắt highlight thì dọn sau khi đã có clip, vì dọn xong thì không còn `tu-lieu/video-goc.mp4` để cắt.
```bash
python3 -I $SKILL/scripts/don-tap.py --xoa <dự án>    # David chốt → chạy thẳng, KHÔNG gửi danh sách hỏi lại
python3 -I $SKILL/scripts/don-tap.py <dự án>          # chỉ liệt kê, khi cần xem trước
zsh $SKILL/scripts/luu-drive.sh <dự án>               # chạy nền: lên Drive sao-luu-mac/video/<tập>, kiểm khớp, xoá trên Mac
```
`<dự án>` = `~/Movies/tap-<tên>` hoặc `~/Movies/vlog/<tên>`. Chỉ hỏi David khi script báo **⏸** — việc đang dở: tiến trình đang chạy
trong dự án (thường là phiên khác), file kịch bản sửa sau bản cuối mà chưa render lại, hoặc chưa có `video-hoan-chinh.mp4`. Phần ⏸ để
nguyên, phần còn lại vẫn dọn; tập có ⏸ chưa đưa lên Drive. Báo David một dòng: đã giải phóng bao nhiêu, đã lên Drive chưa, phần nào bỏ qua và vì sao.
- **Giữ (và đưa lên Drive):** `1-goc/` · `video-hoan-chinh*.mp4` ở gốc mỗi dự án · `phat-hanh/` · mọi file chữ.
- **Xoá hẳn:** `node_modules` · `.remotion` · `.cache` · mọi file hình, tiếng, video tạm còn lại (dựng lại được từ gốc + kịch bản).
- `luu-drive.sh` chỉ xoá tập trên Mac khi mọi file đã lên mây và khớp; lỗi thì giữ bản Mac. Xong thì ghi loại tập (đạt · chờ duyệt ·
  không đạt · thử) vào `du-an/kho-drive.md`.
- Dự án chưa có bản cuối thì script tự bỏ qua. Không có bản cho app chỉnh sửa (CapCut/DaVinci).
