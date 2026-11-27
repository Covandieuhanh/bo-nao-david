---
description: "Khối 17 dựng và kiểm tra chất lượng: chụp thử từng cảnh, render, rà soát lỗi."
---

# Khối 17-kiem-soat-chat-luong: Dựng và kiểm tra: chụp thử từng cảnh, render, ghép bản cuối, rà soát khung / âm lượng / tiếng rè

**Dùng trong:** cả 4
**Đầu vào:** dự án đã có kịch bản
**Đầu ra:** video-hoan-chinh.mp4 + kiem-tra/{stills,sheet}.jpg
**Tham số hồ sơ:** —
**Sửa khối này thì chạy lại:** —

**File thật (code, một bản duy nhất):**
- `dung-video-theo-phong-cach/scripts/{vung-an-toan.py,ghep-anh-tinh.sh,kiem-khung-hinh.sh,xem-truoc-ban-dung.py,don-tap.py,luu-drive.sh}`
- `…/mau-remotion/{xem-truoc.mjs,xuat-video.mjs}`
- `…/mau-dung-ghep/{anh-tinh.mjs,xuat-chuong-trinh.mjs}`
- `dung-video-theo-phong-cach/references/loi-thuong-gap.md`

## Cách làm

### Chụp thử từng cảnh (trước khi render thật)

```bash
cd "$P/chuyen-dong" && node xem-truoc.mjs <id>@<giây> phu-de@<giây> <id>@<giây> phu-de@<giây> ...
```
(khi người dựng chụp `phu-de` cùng mốc với mỗi cảnh, ghep-anh-tinh.sh ghép phụ đề lên cảnh đó để thấy chồng lấn, nếu có)
Chụp mỗi cảnh ở khoảnh khắc "đầy nhất" (cuối cảnh, khi mọi phần tử đã hiện). Ghép lên khung video gốc và khung an toàn
bằng `python3 $SKILL/scripts/vung-an-toan.py "$P"` (một lần) và `zsh $SKILL/scripts/ghep-anh-tinh.sh "$P"` rồi xem `kiem-tra/anh-tinh.jpg`: chữ có tràn hoặc xuống dòng sai chỗ, dấu tiếng Việt
có bị cắt, **hai dòng chữ có chồng nhau / chữ có chạm khung ảnh không** (kiểm chữ có Ố Ễ Ỗ), **ô hiệu ứng có bị cắt ở đáy hoặc chạm phụ đề không**
(lớp phủ bị chặn bắt buộc ở đỉnh dải phụ đề; nếu thấy bị cắt thì rút gọn nội dung), có gì tràn vùng đỏ, **lớp phủ có đè lên mặt/đầu người nói không** (script dò mặt theo khung 0,5 s — cử động
nhanh vẫn có thể bị bỏ sót; nếu thấy đè thì chỉ định thủ công `place`), chữ có đọc được trên nền, cảnh có khớp lời nói không. Người dựng sửa rồi chụp lại tới khi không còn lỗi.
Chụp đúng mốc dễ lỗi (`quy-tac-chung.md` mục 8), không chụp thừa. Đây là bước tiết kiệm chi phí nhất: sửa ở đây tốn ít hơn nhiều so với sửa sau khi render.
Khung ngang (pillar): trước khi chụp, dựng nền ngang một lần —
`node xuat-video.mjs hai-ben` (khoảng 1 phút / phút video) rồi `python3 -I $SKILL/scripts/nen-cot.py "$P"` để tạo `nen-ngang.mp4`;
ghep-anh-tinh.sh tự dùng nền này. Chụp thêm `hai-ben@<giây>` ở vài mốc để kiểm chữ hai bên (tràn, xuống dòng sai chỗ).
Khi đổi `SIDES` hoặc mốc cảnh, người dựng render lại `hai-ben` và chạy lại `nen-cot.py`.

### Render, đóng gói, xuất bản cuối

```bash
cd "$P/chuyen-dong" && node xuat-video.mjs                                  # chạy nền; ~10–40 s mỗi cảnh
python3 -I $SKILL/scripts/nen-cot.py "$P"                      # chỉ khi xuất ngang từ gốc dọc (sau khi render hai-ben)
python3 -I $SKILL/scripts/the-ghi-cong.py "$P"                     # chỉ khi có dùng ảnh → nguon-anh.txt (dán vào mô tả)
python3 -I $SKILL/scripts/xem-truoc-ban-dung.py "$P"                   # chạy nền → video-hoan-chinh.mp4
```

**Thời gian render thật** (đo 18–19/11/2026, Mac này, 1080p, `concurrency: 3`; báo David theo bảng này, không đoán):
| Mẫu / khung | Tốc độ | Ví dụ |
|---|---|---|
| ghép ngang 1920×1080 | khoảng 4–5,7 × độ dài | 11:45 → 44–60 phút (chạy cùng render khác: 60) · 54:30 → 5,2 giờ |
| ghép dọc 1080×1920 clip ngắn | khoảng 6–7 × độ dài | 1:19 → khoảng 8 phút |
Ổ đĩa cần còn trống ít nhất 2 × dung lượng file xuất ra cộng 5 GB (thư mục tạm `remotion-*` của Remotion); người dựng chỉ render bản dài sau khi đã rà soát khớp tiếng (khối 03) và
chụp thử đủ lớp, để không phải render lại.

### Kiểm tra bản cuối

```bash
zsh $SKILL/scripts/kiem-khung-hinh.sh "$P" "$P/video-hoan-chinh.mp4" <các mốc giây: giữa & cuối mỗi cảnh, vài chỗ không có cảnh, màn hình nguồn>
```
Xem `kiem-tra/bang-anh.jpg`: cảnh đúng chỗ, không gì tràn vùng an toàn, không lớp phủ nào che mặt, không nhấp nháy hoặc màn hình đen. Âm thanh
(cả bài −14 LUFS, đỉnh tối đa −1,5 dB — `ebur128=peak=true`; không so dB thô với nguồn vì giọng nhỏ đã được tăng âm lượng — khối 09) và tiếng rè so với giọng (`-af highpass=f=12000,astats` — mức RMS bản cuối
chênh bản gốc tối đa 1 dB; nếu cao hơn hẳn thì âm thanh đã bị hạ bit ở một khâu nào đó, xem gotchas) và thời lượng (bằng bản sạch; video không có màn hình nguồn ảnh ở cuối).
Khi có lỗi, người dựng sửa cảnh đó, chạy `node xuat-video.mjs <id>` rồi chạy lại xem-truoc-ban-dung.py.

## Rà soát cảnh tự động
Chạy **trước bước chụp thử** và sau mỗi lần sửa mốc / chữ:
```bash
node $SKILL/scripts/soat-canh.mjs "$P"     # in ra + ghi kiem-tra/soat.md; có P0 thì mã thoát 1. Không sửa gì, không render
```
Công cụ đọc từ `canh.js` hoặc `danh-sach-cat.js` và báo mỗi lỗi một dòng `t=… · cảnh · vấn đề → cách sửa`:
- **P0 (phải sửa):** kiểu cảnh hoặc biểu tượng không tồn tại, phần tử hiện ngoài cảnh, mốc sai hoặc tài nguyên thiếu. Render đầy đủ tự chạy bước soát và dừng khi còn P0.
- Chẩn đoán là tài liệu để so lựa chọn với bản thử. Xem đủ chuyển động ở kích thước phát hành để đánh giá mặt người nói, điểm nhìn, nhịp và khả năng đọc.
- **P1 (nên sửa):** nhãn không đủ đọc (0,5 s + 0,3 s mỗi từ), nhãn `illus` quá số chữ hồ sơ, hai cảnh toàn màn hình chồng nhau.
- **P2 (tinh chỉnh, giữ có chủ đích được):** hình đứng yên quá 3 s sau khi đọc xong, thẻ tiêu đề / màn chốt thiếu hẳn thời gian đọc, hai cảnh cùng kiểu liền nhau (trừ cảnh vẽ tiếp `tu_buoc`, khối 07).
Giới hạn: công cụ chỉ bắt lỗi đo được. Lỗi chữ tràn, che mặt, thẩm mỹ kém vẫn được xét bằng `kiem-tra/anh-tinh.jpg`. **Xem tờ ảnh ở đúng cỡ (mỗi khung 240–270 px, nhỏ hơn màn điện thoại): chữ cần đọc mà không đọc được thì tính là P0.**
Khi xem bản thử, kiểm xem chuyển động có hướng mắt tới đúng ý, chữ có đọc được và mặt người nói có rõ ở cả điểm chuyển cảnh hay không.

## Kiểm cảm nhận
Claude tự làm, hai lần: sau bước chụp thử và sau bản cuối. Không gửi David chấm.
1. **Xem như người xem mới trước:** xem tờ ảnh theo thứ tự thời gian (bản cuối: thêm vài đoạn video quanh đỉnh), chưa mở `ke-hoach-canh.md`. Ghi một
   từ cho cảm xúc mỗi đoạn vào `kiem-tra/cam-nhan.md`.
2. **Rồi mới so** với "Đường cảm xúc" trong `ke-hoach-canh.md` (khối 07): bảng ba cột `đoạn · dự định · cảm thấy`.
3. **Khi lệch thì video sai, không phải đường cảm xúc sai:** Claude sửa cảnh (đổi kiểu, bỏ bớt hình, phóng lớn hình ở đỉnh) rồi chụp lại. Đồng thời rà soát:
   đỉnh có phải chỗ đổi hình lớn nhất không · đoạn trước đỉnh có lặng hơn không · màn cuối có khép lại (không tắt dần) không.
4. Báo cáo David chỉ thêm một dòng: "Cảm nhận: khớp N/M đoạn; đã sửa <đoạn>".

## Dọn file tạm và đưa tập lên Drive khi David chốt bản cuối

Claude không dọn ngay lúc render xong, mà dọn khi David nói "chốt" hoặc khi video đã đăng, không hỏi lại David. Nếu tập còn cắt highlight thì dọn sau khi đã có clip, vì dọn xong thì không còn `tu-lieu/video-goc.mp4` để cắt.
```bash
python3 -I $SKILL/scripts/don-tap.py --xoa <dự án>    # David chốt → chạy thẳng, KHÔNG gửi danh sách hỏi lại
python3 -I $SKILL/scripts/don-tap.py <dự án>          # chỉ liệt kê, khi cần xem trước
zsh $SKILL/scripts/luu-drive.sh <dự án>               # chạy nền: lên Drive sao-luu-mac/video/<tập>, kiểm khớp, xoá trên Mac
```
`<dự án>` = `~/Movies/tap-<tên>` hoặc `~/Movies/vlog/<tên>`. Chỉ hỏi David khi script báo **⏸** — việc làm chưa xong: tiến trình đang chạy
trong dự án (thường là phiên khác), file kịch bản sửa sau bản cuối mà chưa render lại, hoặc chưa có `video-hoan-chinh.mp4`. Phần ⏸ để
nguyên, phần còn lại vẫn dọn; tập có ⏸ chưa đưa lên Drive. Claude báo David một dòng: đã giải phóng bao nhiêu dung lượng, đã lên Drive chưa, phần nào bỏ qua và vì sao.
- **Giữ (và đưa lên Drive):** `1-goc/` · `video-hoan-chinh*.mp4` ở gốc mỗi dự án · `phat-hanh/` · mọi file chữ.
- **Xoá hẳn:** `node_modules` · `.remotion` · `.cache` · mọi file hình, tiếng, video tạm còn lại (dựng lại được từ gốc + kịch bản).
- `luu-drive.sh` chỉ xoá tập trên Mac khi mọi file đã lên Drive và khớp; khi có lỗi thì giữ bản trên Mac. Khi xong, Claude ghi loại tập (đạt · chờ duyệt ·
  không đạt · thử) vào `du-an/kho-drive.md`.
- Dự án chưa có bản cuối thì script tự bỏ qua. Không có bản cho app chỉnh sửa (CapCut/DaVinci).
