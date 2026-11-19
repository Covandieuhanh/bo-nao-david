---
name: cat-doan-noi-bat
description: Cắt một video dài (bản YouTube 5–60 phút) thành các clip highlight DỌC 9:16 (1080×1920) cho Reels, TikTok, Shorts, Facebook Reels. Claude tự chọn ý theo bốn câu (bối cảnh, ý trọn, mang về, chừa lại): mỗi clip một ý trọn, tự đứng được, số clip và độ dài theo ý. Mọi chữ trên clip là nguyên văn lời người nói — kể cả thẻ tít (cụm đắt nhất) và màn chốt; phụ đề cụm 5–8 chữ; cắt cứng giấu mối, rút khoảng lặng; hai tông sôi động / lắng với nhạc từ kho kênh; không thanh thời gian, không thẻ cuối — dẫn về bản đầy đủ ở caption + bình luận ghim. Highlight ra ĐÚNG LOẠI video gốc — người nói → khung ghép của dung-video-theo-phong-cach; podcast/đồ hoạ → podcast đồ hoạ dọc (dung-podcast). Kèm lịch đăng, mô tả, bình luận ghim. Dùng khi người dùng nói "cắt highlight", "làm video highlight", "cắt clip ngắn từ video dài", "làm Reels/TikTok/Shorts từ video YouTube/podcast", "cắt đoạn hay", "/cat-doan-noi-bat", hoặc đưa một video dài (kể cả podcast đã dựng) muốn ra clip ngắn — kể cả khi chỉ gửi file mà không nói rõ.
---
# Cắt video highlight cho mọi mục video ngắn

**Đọc trước:** `../../chuan-muc-lam-viec.md` · `../quy-tac-chung.md` · hồ sơ `../ho-so-thuong-hieu/doan-noi-bat.md` — **con số lấy ở hồ sơ, không ghi cứng**.
`$BASE/references/loi-thuong-gap.md` (+ `$POD/references/loi-thuong-gap.md` khi nguồn là podcast) đọc một lần ở đầu phiên. File khác chỉ đọc ở
đúng bước cần (cột "Khối"). Skill này là **CÔNG THỨC**: thứ tự khối + quyết định riêng của loại + tiêu chí đạt; sửa cách làm → sửa khối.

`$BASE=~/.claude/skills/dung-video-theo-phong-cach`, `$POD=~/.claude/skills/dung-podcast`, `$SKILL` = thư mục này. Skill này lo **nhận loại
video gốc, hiểu cả video, chọn khoảnh khắc, cắt câu, bố trí lời kêu gọi**; phần dựng dùng quy trình của skill tương ứng.

Mục tiêu: từ một video gốc, **tự chọn ý** rồi ra các clip ngắn **cùng loại với video gốc**. Mỗi clip là **một ý trọn vẹn** và đạt cùng lúc **hai mục tiêu**:
1. Người xem không sang video dài vẫn **mang về được một sự chuyển hoá** từ chính clip.
2. Người xem **muốn mở bản đầy đủ** vì bản dài còn những điều khác.

Clip đẹp mà xem xong không hiểu gì, hoặc hiểu mà không mang về được gì, là clip hỏng.


## Bốn câu chọn ý (luật gốc của skill, đứng trên mọi luật khác của skill khi trái nhau)
Claude **tự chọn ý, không hỏi David chọn đoạn**. Đọc nối lời như người lạ chưa xem bản dài, trả lời đủ 4 câu cho từng clip và ghi vào `chon_y` trong `phuong-an.json`. Thiếu một câu thì chọn lại ý, không nộp.
| Khoá | Câu hỏi | Đạt khi |
|---|---|---|
| `boi_canh` | Ngay đầu clip, người lạ có biết ai đang nói, chuyện gì, vì sao nói không? | Nói được bằng chính lời trong clip; thiếu thì thêm câu nguyên văn nêu hoàn cảnh |
| `y_tron` | Có đủ từ vấn đề hoặc câu hỏi đến lời giải hoặc điều nhận ra, và kết thúc được không? | Không dừng giữa mạch, không chỉ kể chuyện hay chỉ nêu cảm xúc |
| `mang_ve` | Không xem video dài, họ mang về điều gì? | Một câu rõ: cách nghĩ mới, câu tự hỏi hoặc việc làm, có trong lời người nói; không bắt buộc câu giao việc |
| `chua_lai` | Bản dài còn thêm gì ngoài ý đã trọn này? | Một chuyện khác hoặc ý mở rộng; không được chừa phần kết của ý trong clip |

**Không có con số cố định** cho độ dài hay số clip: ý cần bao lâu thì clip dài bấy lâu, video có bao nhiêu ý đạt thì ra bấy nhiêu clip. Dài mà còn giữ được người xem thì giữ; có đoạn thừa thì bỏ đoạn thừa, không cắt vào ý cho vừa số giây. Được ghép hai đoạn xa nhau khi đúng mạch ý của người nói, phải báo rõ các mốc trong báo cáo giao bản. Báo cáo giao bản ghi đủ 4 câu và lời đọc nối; David duyệt ở bản cuối.

## Luật riêng của highlight (kiểm lại trước khi giao)

Vị trí và thành phần cố định theo bộ nhận diện chung `../thu-vien-tai-nguyen/nhan-dien-chung.md`. Clip highlight là video dọc ngắn: không thanh
thời gian, không thẻ cuối, màn chốt trên hình, kết ở chữ cuối để tự lặp; dẫn về bản đầy đủ nằm ở caption + bình luận ghim (khối 15).

1. **Cùng loại với video gốc**: người nói ↔ người nói, đồ hoạ ↔ đồ hoạ; giữ phong cách + tên tập/tên người nói của bản gốc (khối 13, bước 0).
   Mặc định **dọc 9:16, 1080×1920**; David yêu cầu ngang thì ra **ngang 1920×1080** (mục "Highlight ngang" dưới bước 7A). Không cắt thẳng hình đồ hoạ ngang vào khung dọc — dựng lại.
2. **Số clip theo số ý đạt 4 câu**: mỗi clip một ý KHÁC NHAU, không trùng câu chính; không độn. David yêu cầu một số clip cụ thể thì chọn các ý mạnh nhất đủ số đó. Clip A = mạnh nhất (đăng đầu).
3. **Mọi chữ = nguyên văn** (thẻ tít, phụ đề, chữ to, màn hành động, ý đang bàn, màn chốt) — quy-tac-chung mục 1: chỉ chọn câu,
   bỏ bớt chữ ở đầu/cuối câu, sửa chính tả Whisper. Không có ngoại lệ. Mô tả bài đăng theo giọng David (khối 15).
4. **Màn chốt — một luật cho cả hai nhánh**: người nói có câu mệnh lệnh/giao việc hay câu mời bình luận nguyên văn ("Hãy chọn…",
   "thử làm…") → màn chốt bằng câu đó. Không có → clip kết ở câu chốt ý; **không dừng báo David**, không ghép
   câu kêu gọi từ chỗ khác; clip vẫn phải đạt `mang_ve`. "Vấn đề / Kết quả" để ở mô tả và bình luận ghim.
5. **Ý của cả video**: luôn làm bước 2 (bản đồ cả video) trước khi chọn. Mỗi clip phục vụ lời hứa cốt lõi hoặc một ý lớn của video. **Người xem clip là người xem độc lập**: mỗi clip qua đủ bốn câu chọn ý và tự đạt câu hỏi gốc của bộ lọc (làm chủ bản thân / công việc); chỉ nói cảm xúc hoặc chỉ kể chuyện thì không đạt.
6. **Không thứ tự cố định**: vị trí lời kêu gọi tự bố trí theo mạch (khối 13, bước 4); đổi thứ tự không được làm sai nghĩa. Độ dài theo ý.
7. **Thẻ tít mở đầu** (chuẩn DOAC/Mel Robbins): **cụm nguyên văn đắt nhất của clip**, Claude tự chọn, ngắn, 2 dòng, nửa trên khung; nêu
   tiền cược / kết quả / mâu thuẫn của clip nếu lời có. Câu chạm vẫn là lời thật ngay giây 0. Ghi tít + mốc câu gốc vào ke-hoach-cat.md.
8. **Nhịp kênh lớn**: **cắt cứng** giữa các câu, không phóng xen kẽ ở mối cắt (quy-tac-chung mục 2); khoảng lặng ≥ 0,45 s **trong** câu và
   > 0,6 s **giữa** câu rút còn ~0,24 s; phụ đề **cụm trọn ý 5–8 chữ, cỡ bằng chữ thẻ, ẩn khi lớp chữ motion graphic hiện** (quy-tac-chung mục 3). Giữ 1 s lặng sau câu hỏi kêu gọi. Kiểu cũ có chip tua chỉ khi David yêu cầu: `--tua` cho `cat-doan-noi-bat.py` + `danh-sach-cat-doan-noi-bat.py`.
9. **Hai tông** theo cảm xúc lời nói, đổi giữa chừng được (cú đổi tông là cú cảm xúc):
   | | **Sôi động** `soi` (mẹo, tin vui, kết quả, lời mời) | **Lắng** `lang` (tâm sự, nỗi đau, mất mát, câu hỏi day dứt) |
   |---|---|---|
   | Nhạc | bài vui `soi-*` | bài trầm `lang-*` (piano/dây) |
   | Chữ to | bật nảy, gạch cam | hiện chậm, nét mảnh, không gạch |
   | Hình | dồn khung | màu dịu |
   Nhạc lấy từ **kho nhạc kênh** (`$SKILL/assets/nhac/`), Claude tự chọn theo tuyến nội dung (khối 09). Mức nhạc
   theo chuẩn âm lượng chung (thấp hơn giọng ~23 dB). Không nhãn kỹ thuật, không thẻ "TẬP NÀY CÓ GÌ?"/tên vòng.
10. **Chừa cho bản đầy đủ đúng chỗ**: chừa một chuyện khác hoặc ý mở rộng; ý trong clip phải đi đến hết. Câu mở ưu tiên bất ngờ / kết quả lớn / tiền cược hơn lời than chung chung.
11. **Không thẻ cuối, không thanh thời gian** (video dọc ngắn, `nhan-dien-chung.md` mục 1). `danh-sach-cat-doan-noi-bat.py` vẫn ghi `ENDCARD` từ
    `"endcard"` trong phuong-an.json (tên tập gốc, người nói) nhưng khuôn tự bỏ ở video dọc ngắn; ghi đủ để dùng khi David cần bản dọc dài.
    Không có tên tập gốc → hỏi trong 4 phần lúc đầu (`../nhan-dien-thuong-hieu.md`).
12. **Tự chọn, không hỏi** (`chuan-muc-lam-viec.md` mục 2): nhận yêu cầu cắt là tự chọn ý, tít, câu màn chốt rồi dựng trọn
    một mạch. Chỉ dừng hỏi khi không ý nào đạt 4 câu hoặc câu chủ chốt dính lằn ranh. Luôn ghi rõ đã chọn gì trong báo cáo để David sửa ở bản cuối.
13. **Học từ 20 highlight Việt** (`references/hoc-tu-20-doan-noi-bat-vn.md`):
    - **Tít ghim** (mặc định tắt, hồ sơ `tit_ghim: false`, vì dọc mỗi lúc ít thứ): ghi `"tit"` vào từng option của phuong-an.json
      (`danh-sach-cat-doan-noi-bat.py` tự viết `pow` mở đầu); `"pin": true` để tít thu nhỏ thành dải dưới dấu kênh suốt clip tới màn chốt (`pinTitle`).
      Nhánh podcast: `STAGE.title` = tít.
    - **Khung bìa = 0,3 s** (thẻ tít + mặt người nói rõ) — ghi mốc này vào dang-bai.md.
    - **Cảnh phản ứng**: nguồn có khán giả / người dẫn → piece thêm `"react": {"at": <giây nguồn ngay sau cụm đắt>, "from": <giây
      nguồn có mặt người nghe>, "len": 0.8–1.5}` — hình người nghe, tiếng người nói vẫn chạy.
    - **Danh sách đếm / hướng dẫn từng bước**: giữ đủ các ý trong danh sách để ý được trọn.

## Đầu vào

1. **Video gốc** (mp4/mov…) — hoặc **thư mục dự án** đã dựng nó (`~/Movies/tap-<tên>/2-ban-day-du`, dự án Codex dạng `…/work/podcast-<tên>`):
   tốt nhất, vì có lời đã sửa chính tả, tiếng sạch, kịch bản, tên tập. Chỉ có video-hoan-chinh → tìm thư mục dự án cạnh nó (cùng cha
   `outputs/` ↔ `work/`, hoặc `~/Movies/*/video-hoan-chinh.mp4`). Không tải video từ YouTube/TikTok — nhờ gửi file.
2. **Phụ đề** .srt/.vtt nếu có (YouTube Studio → Phụ đề → Tải xuống): để sửa chính tả; mốc cắt vẫn lấy từ `moc-tung-tu.srt`.
3. **Dàn ý** (Vấn đề · Giải pháp · Thực thi), đoạn đã đánh dấu "highlight" nếu có → ưu tiên.

Chỉ có phụ đề, không có video → làm bước 2–5, trả bảng cắt + mô tả + bình luận ghim để cắt bằng công cụ khác.

## Công thức — Highlight · hồ sơ `doan-noi-bat`
| # | Bước | Khối |
|---|---|---|
| 0–1 | Nhận loại nguồn · tạo dự án *(bước nhẹ)* | [13](../mo-dun/13-chon-doan-noi-bat/README.md) · [01](../mo-dun/01-phien-am/README.md) |
| 2–6 | Bản đồ cả video · tự chọn ý theo 4 câu · chọn câu · bố trí lời kêu gọi · kiểm tự đứng được + lằn ranh · cắt + kiểm lời | [13](../mo-dun/13-chon-doan-noi-bat/README.md) (chi tiết từng bước) · [02](../mo-dun/02-lam-sach/README.md) (khoang-lang.py) · [01](../mo-dun/01-phien-am/README.md) |
| 7A | Chẩn đoán → tự chọn ([tu-chon](../thiet-ke-bo-cuc/tu-chon.md)) · dựng nguồn có người nói (mục dưới) | [11](../mo-dun/11-dung-ghep/README.md) · [04](../mo-dun/04-khung-hinh/README.md) · [05](../mo-dun/05-tranh-che-chu-the/README.md) · [06](../mo-dun/06-phan-mo-dau/README.md) · [07](../mo-dun/07-canh-minh-hoa/README.md) · [08](../mo-dun/08-phan-ket/README.md) · [03](../mo-dun/03-phu-de/README.md) · [09](../mo-dun/09-am-thanh/README.md) · [17](../mo-dun/17-kiem-soat-chat-luong/README.md) |
| 7B | Chẩn đoán → tự chọn · dựng nguồn podcast / đồ hoạ (mục dưới) | [12](../mo-dun/12-san-khau-podcast/README.md) · [07](../mo-dun/07-canh-minh-hoa/README.md) · [08](../mo-dun/08-phan-ket/README.md) · [17](../mo-dun/17-kiem-soat-chat-luong/README.md) |
| 8 | Phát hành: lịch đăng, khung bìa, mô tả, bình luận ghim, số liệu | [15](../mo-dun/15-xuat-ban/README.md) · [16](../mo-dun/16-phan-tich-so-lieu/README.md) |

Bước đánh dấu *(bước nhẹ)*: nhắc đổi mô hình rẻ hơn theo `chuan-muc-lam-viec.md` mục 3.

### 7A. Dựng — nguồn có người nói (`dung-video-theo-phong-cach` chế độ ghép clip, `references/nhieu-doan-video.md`)
Làm lần lượt cho từng clip `<id>` (A, B…). `cat/<id>.mp4` của bước 6 chỉ để **kiểm lời**; bản dựng đọc thẳng video gốc theo mốc trong phuong-an.json (mỗi câu thêm
`"tone": "lang"|"soi"`, câu dùng cho màn chốt thêm `"cta": true`):
```bash
LOI_SAN="$P/kiem-tra/goc" zsh $BASE/scripts/tao-dung-ghep.sh hl-<tên>-<id> "$P/nguon.<ext>"   # chạy nền → ~/Movies/tap-<tên>/3-doan-noi-bat/clip-<id> = $E (c1 = video gốc; LOI_SAN = dùng lại lời đã chép, không chép lại cả video cho mỗi clip)
python3 -I $SKILL/scripts/danh-sach-cat-doan-noi-bat.py "$P" "$E" <id>                   # → $E/chuyen-dong/src/danh-sach-cat.js viết sẵn
cp $SKILL/assets/nhac/*.mp3 "$E/chuyen-dong/public/hieu-ung-am-thanh/"                 # kho nhạc kênh (soi-*, lang-*)
```
`danh-sach-cat-doan-noi-bat.py` viết: các câu `p1…pN` **cắt cứng**, khoảng lặng trong câu đã rút (đoạn con `p2b`, `p2c`…), không phóng xen kẽ;
`SUBS` (giây timeline, chữ đúng câu nguyên văn — hiện cụm 5–8 chữ nhờ `SHORT = true`); `TS(src)` đổi giây video gốc → giây
timeline cho lớp phủ; `TONE` + `MUSIC.tracks`; `CTA` = câu kêu gọi nguyên văn (nếu có); `HL = {…, bar: false}` (không thanh tập gốc).
Claude chỉnh tiếp trong danh-sach-cat.js:
- **Phụ đề**: sửa chính tả, tô `hl` từ khoá (từ trong `hl` hiện màu cam khi tới nhịp của nó).
- **OVERLAYS** (mốc bằng `TS(<giây trong moc-tung-tu.srt>)`; mọi chữ nguyên văn): `pow` cụm đắt đúng lúc nói (cú chốt, ≤ 14 ký tự/dòng) · `action` khi câu HANHDONG
  (`quote` nguyên văn) · `chips` khi người nói đếm/liệt kê. Mật độ theo nội dung: dày hơn ở `soi`, thưa hơn ở `lang`.
- **Hình**: không zoom vào / ra (quy-tac-chung mục 2); có thể `replay` khoảnh khắc đắt.
- `CTA.kind` theo việc được kêu gọi (lưu → `save`, bình luận → `comment`…); không có câu kêu gọi → không đặt `CTA` (luật 4).
- **Thẻ tít mở** (luật 7): `{type: 'pow', start: 0, end: 2.5, text: '<TÍT nguyên văn>', y: 300}` — nửa trên khung, tách khỏi phụ đề.
  `ENDCARD` do `danh-sach-cat-doan-noi-bat.py` ghi (luật 11), khuôn tự bỏ ở video dọc ngắn.
Rồi như nhieu-doan-video.md: `python3 -I $BASE/scripts/nang-lop.py "$E"` → `python3 -I $BASE/scripts/bao-ve-lop-phu.py "$E"` (che mặt/thân trên →
toàn màn hình; tít ghim che đầu → ẩn) → `node anh-tinh.mjs <mốc>` (chụp: thẻ tít, mỗi pow/action lúc đầy nhất, 2–3 mốc thấy phụ đề,
ngay sau 1–2 mối cắt, cuối clip thấy màn chốt) → sửa tới sạch → `node xuat-chuong-trinh.mjs` (nền; render các clip nối tiếp,
không song song — tốn RAM). Không có bước duyệt kế hoạch ghép của multi-clip (luật 12).

### Highlight ngang (khi David yêu cầu) — nguồn người nói, khuôn ghép
- `danh-sach-cat.js`: `W = 1920`, `H = 1080`; `THE_CUOI = false` (kết ở màn chốt); thanh thời gian tự có (khung ngang). Bỏ `nang-lop.py` và
  `bao-ve-lop-phu.py` (chỉ tính cho khung dọc) — tự soát bằng ảnh chụp thử: `pow` đặt `x` (tâm khối chữ, px) vào vùng trống cạnh người nói.
- Nguồn nhiều video dài (ổ không đủ chép bản gốc): chép lời trên bản xem nhẹ ghép các video, chọn ý, rồi cắt các cửa sổ cần dùng từ file gốc
  (1920×1080, 30 fps) ghép thành `nguon.mp4` mới và chép lời lại — mốc trong `phuong-an.json` theo nguồn mới.
- **Đoạn ghép mở đầu (intro)** khi David yêu cầu: thêm đầu `RAW` các đoạn `m1…` (câu đắt nhất giữ tiếng ≈ 3 s, rồi cảnh câm thật sự khác nhau
  2 phách bài `intro-soi`/`intro-lang`), `D = segStart('p1')`; phụ đề phần chính cộng `D`, `TS()` bỏ qua đoạn `m`; thẻ `title` `over` trên dải
  cảnh câm, chữ nguyên văn; nhạc `tracks` intro + bài phần chính, `loudRanges` = dải cảnh câm. Luật chọn cảnh: `nhieu-doan-video.md` mục 2d.1.
  Mẫu: `~/Movies/tap-marketing-noi-dau-nhu-cau/3-doan-noi-bat/clip-A`.
- **Cùng ý, thêm bản dọc từ nguồn ngang**: không cắt thẳng — đổi khung `nguon.mp4` bám người nói (`phan-tich-doi-khung.sh` + `ke-hoach-doi-khung.py`
  trong dự án phụ `clip-<id>-doc/rekhung`, `tu-lieu/video-goc.mp4` = nối cứng tới c1; mọi câu bám người đang nói, cảnh intro đặt `cx` riêng,
  cảnh có người đi ngang / thấy cả quán → `wide`) → chép `chuyen-dong` của bản ngang, c1 = bản dọc (cùng thời lượng nên giữ nguyên mốc),
  `W = 1080`, `H = 1920`, bỏ `pow.x`; người ngồi cả thân lấp giữa khung → `pow` đặt `y` vào dải trống trên đầu (đỉnh đầu ~650 px → `y: 300`);
  thẻ `title` trên intro thêm `keep: true` để không thành toàn màn hình che hết cảnh câm. Rồi `nang-lop.py` → `bao-ve-lop-phu.py` → chụp thử như 7A.
  Mẫu: `~/Movies/tap-marketing-noi-dau-nhu-cau/3-doan-noi-bat/clip-B-doc`.

### 7B. Dựng — nguồn podcast / toàn đồ hoạ (`dung-podcast`, khung dọc)
```bash
zsh $POD/scripts/tao-podcast.sh "$P/cat/<id>.mp4" hl-<tên>-<id> doc cat-thua   # mỗi clip → ~/Movies/tap-<tên>/3-doan-noi-bat/clip-<id> = $E (chỉ lấy tiếng)
zsh $POD/scripts/phien-am.sh "$E"
python3 -I $BASE/scripts/phu-de.py "$E"                         # rồi sửa chữ theo captions-goc.js của $P (đã sửa chính tả)
PY=$(zsh $POD/scripts/cai-python.sh); $PY $POD/scripts/nguoi-noi.py "$E"; $PY $POD/scripts/duong-bao-am.py "$E"
```
- `tao-podcast.sh … cat-thua` còn 0,4 s lặng cuối → đệm đủ 1 s lặng, cập nhật `project.duration`, chạy lại `duong-bao-am.py`.
- **Tông, nhạc, thẻ cuối**: `python3 -I $SKILL/scripts/ap-dung-doan-noi-bat.py "$P" <id> "$E"` → `chuyen-dong/src/doan-noi-bat.js` (cắt cứng: `bar: false`,
  không chip tua; tự trừ phần cắt đầu trong `kiem-tra/cat-goc.txt`).
- Số người nói (1|2) và `STAGE` lấy từ `scenes-goc.js`: `title` = tên tập gốc, `speakers` = tên người nói gốc, `show` như gốc.
  `chu-de.js`/`phong-chu.js` khác mặc định → chép sang. Biểu tượng vẽ thêm trong dự án gốc → chép `bieu-tuong.jsx` nếu cảnh cần.
- **Không bìa** (`COVER = null`) trừ khi David muốn — video ngắn vào thẳng câu chạm.
- `"endcard": {}` trong phuong-an.json là đủ (trống = lấy `STAGE.title` + người nói của `STAGE`); khuôn tự bỏ thẻ cuối ở video dọc ngắn.
- `TOPICS` 2–3 mục cho cả clip (mốc = lúc bắt đầu ý), chữ trích lời, không lặp chữ của cảnh đang hiện.
- **Tông + nhạc**: ghi `tone` cho từng câu như 7A; `ap-dung-doan-noi-bat.py` chép vào `doan-noi-bat.js` (`nhac`) → `xem-truoc-ban-dung.py` trộn nhạc
  kho kênh dưới tiếng nói (`ho-so-thuong-hieu/doan-noi-bat.json` → `nhac_chu_chinh`), không tiếng ký hiệu đầu clip; chuyển cảnh `lang` không tiếng vút.
- `anh-tinh-podcast.sh` chụp thử (mỗi cảnh lúc đầy nhất + vài mốc `nen@`) → `node xuat-video.mjs` → `nen-podcast.py` → `xem-truoc-ban-dung.py`
  → `kiem-khung-hinh.sh` như bước 7–9 của `$POD/SKILL.md`.

### Kịch bản highlight podcast (7B) — mẫu chuẩn 3 clip "Đi trainer", MỌI chữ nguyên văn lời trong clip
Mẫu: `~/Movies/tap-di-trainer/3-doan-noi-bat/clip-{A,B,C}`, thành phẩm ở Drive `thanh-pham/tap-di-trainer/highlight/clip-a|b|c.mp4`, lời và kịch bản ở `du-an/video-di-trainer/`.
- **Chữ chính thay phụ đề** (`ap-dung-doan-noi-bat.py` tự bật `chu_chinh`): không dải phụ đề, không dòng chủ đề, không `kinetic`; mỗi dòng `phu-de.js` là một câu trọn ý (≤ 3 dòng, ~55 ký tự), có `hl` từ khoá. Cảnh đồ hoạ dùng `illus` `single` `compact: true`, không `label`, để chỉ có một lớp chữ.
- **Hoàn cảnh:** thiếu thì đưa câu nguyên văn nêu hoàn cảnh lên đầu clip.
- `hook` mở đầu: **thẻ tít** nguyên văn (luật 7), `eyebrow` trích lời hoặc bỏ trống.
- **Hình theo ý cần hiểu**, không lấp từng cụm lời: thêm `montage`/`card` biểu tượng (biểu tượng vẽ + nhãn trích lời) chỉ ở đoạn mà hình
  giúp người xem hiểu nhanh hơn (quy-tac-chung mục 0). 3 clip "Đi trainer" là mẫu về khuôn (chữ chính, nhạc, màn chốt).
- `action` đúng lúc câu HANHDONG (`icon` — thiếu thì vẽ thêm: `write` = viết ra giấy; `quote` nguyên văn, `quoteAt`, `doneAt`).
- Cú chốt cảm xúc: cụm ngắn nhất, đắt nhất, `start` = lúc bắt đầu nói cụm đó (mốc từ `moc-tung-tu.srt` của `$E`). Nguồn người nói mà
  `vi-tri-khuon-mat.sh` báo "⚠ vẫn che mặt" → đổi cú chốt thành `card` toàn cảnh (vd. `ages` cho con số: số chạy đúng lúc nói + `quote`
  nguyên văn; `ages` cần `pillAt` kể cả khi nhãn tự ẩn, thiếu thì lỗi "Frame NaN"), đặt sau phần dồn khung.
- Tối đa một `card` nếu ý chính có con số, so sánh, danh sách — không thì bỏ.
- **Màn chốt** theo luật 4: có câu kêu gọi nguyên văn → `cta` `text` = câu đó (≤ 55 ký tự; dài hơn → chọn vế trọn ý; `**cụm**` tô nhấn),
  `kind` theo việc được kêu gọi; báo cáo ghi mốc của câu. Không có → kết ở câu chốt ý.
- Kiểm thêm khi chụp thử: chữ to có đủ lớn không (dòng dài làm chữ co nhỏ → mất lực, rút cụm); vài mốc thấy chữ chính đọc rõ, không chạm
  sóng âm. `phu-de@…` không có trong `ghep-anh-tinh.sh` khi đứng riêng → tự ghép lên `video-goc.mp4` cùng mốc.
- Bản cuối: 1080×1920, thời lượng theo ý, âm lượng/tiếng rè bằng nguồn.

## Bảng phụ thuộc (sửa X → chạy lại Y)
| Sửa | Chạy lại |
|---|---|
| phuong-an.json (câu, mốc, tit, react, tone) | cat-doan-noi-bat.py (kiểm lời) → danh-sach-cat-doan-noi-bat.py → nang-lop.py → bao-ve-lop-phu.py → stills → render |
| danh-sach-cat.js sửa tay (OVERLAYS, SUBS) | bao-ve-lop-phu.py → stills → xuat-chuong-trinh.mjs |
| 7B: cat/<id>.mp4 | tao-podcast.sh … → ap-dung-doan-noi-bat.py → xuat-video.mjs → nen-podcast.py → xem-truoc-ban-dung.py |
| hồ sơ doan-noi-bat | danh-sach-cat-doan-noi-bat.py / cat-doan-noi-bat.py chạy lại |

## Tiêu chí đạt
- Mỗi clip đạt đủ bốn câu chọn ý (`chon_y`), báo cáo ghi 4 câu + lời đọc nối + mốc đoạn ghép
- Thẻ tít nguyên văn; bố cục tự cân (dọc: mỗi lúc ít thứ, `../thiet-ke-bo-cuc/`); màn chốt theo luật 4; không thẻ cuối, không thanh thời gian; kiểm lời khớp
- dang-bai.md: lịch đăng, mốc bìa 0,3 s, mô tả, bình luận ghim · so-lieu.md

## Điều không làm
- Không viết thêm, không đổi chữ của người nói trên clip; không ghép câu tạo ra ý người nói không nói.
- Không đổi loại video (podcast không thành người nói, người nói không thành toàn đồ hoạ); không cắt thẳng hình đồ hoạ ngang vào khung dọc.
- Không giọng đọc AI thay người nói; không thêm lời bán hàng vào clip; giá chỉ hiện khi chính người nói nêu và là sản phẩm công nghệ (hướng 3), bài con người không nói giá, không gói.
- Không đốt phụ đề bằng ffmpeg (`subtitles=`/`drawtext` — ffmpeg Homebrew không có libass/freetype); phụ đề luôn qua Remotion
  theo chuẩn chung `kieu-phu-de.js`; không phủ phụ đề lên video đã có phụ đề đốt sẵn.

## Cấu trúc
```
~/Movies/tap-<tên>/3-doan-noi-bat/   (<tên> = đúng tên tập của bản dài)
├── nguon.<ext> · loai.txt          # video nguồn (bản không bìa nếu lấy từ dự án) · loại video gốc
├── kiem-tra/goc/                      # ban-chep-loi.srt · moc-tung-tu.srt · am-luong-05.txt · bang-khung-hinh.jpg · captions-goc.js · scenes-goc.js · phu-de-youtube.srt
├── phuong-an.json                  # các clip (A, B, C…), chon_y + câu theo thứ tự phát (Claude viết)
├── cat/<id>.mp4 · <id>.md · <id>-map.json · <id>-kiem.txt
├── ke-hoach-cat.md · dang-bai.md · so-lieu.md
~/Movies/tap-<tên>/3-doan-noi-bat/clip-<id>/   → video-hoan-chinh.mp4 (BẢN CUỐI mỗi clip, 1080×1920)
$SKILL/assets/nhac/               # soi-*.mp3 · lang-*.mp3 — kho nhạc kênh
```

## Xong khi
1. Mỗi clip đạt đủ bốn câu chọn ý; báo cáo ghi 4 câu + lời đọc nối.
2. Clip cùng loại video gốc, dọc 1080×1920 (ngang 1920×1080 khi David yêu cầu).
3. Mọi chữ trên clip nguyên văn (cả tít, màn chốt).
4. Không cắt vào giữa ý; lời bản cắt đã chép lại đối chiếu khớp.
5. Phụ đề cụm ~5–8 chữ (tối đa theo hồ sơ `phu_de.ngan_max_chu`) không chồng chữ motion graphic; không thanh thời gian, không thẻ cuối.
6. Nhạc từ kho kênh, thấp hơn giọng ~23 dB.
7. Có dang-bai.md (lịch đăng, mốc bìa, mô tả, bình luận ghim) + so-lieu.md; David không phải sửa lại vì trái luật đã chốt.
8. David chốt cả tập → dọn file tạm luôn bằng `don-tap.py --xoa` rồi `luu-drive.sh` lên Drive (khối 17), không hỏi lại; chỉ hỏi phần ⏸ đang dở.

## Tài liệu kèm (chỉ đọc khi bước cần, cân nhắc đổi luật hoặc gỡ lỗi)
- `references/nhat-ky-thay-doi.md` — quyết định theo ngày + lý do.
- `references/hoc-tu-20-doan-noi-bat-vn.md` — 20 highlight Việt đã phân tích (nguồn của luật 13).
- Ví dụ thật (bản chuẩn): `~/Movies/tap-di-trainer/3-doan-noi-bat/clip-A|B|C`. Nguồn có người nói chưa có ví dụ đang giữ trên máy.
