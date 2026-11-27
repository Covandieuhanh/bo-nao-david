---
name: cat-doan-noi-bat
description: Cắt một video dài (bản YouTube 5–60 phút) thành các clip nổi bật cùng khung với video gốc (gốc ngang ra ngang, gốc dọc ra dọc; chỉ đổi khung khi David yêu cầu) cho Facebook, Reels, TikTok, Shorts. Claude tự chọn ý theo bốn câu (bối cảnh, ý trọn, mang về, chừa lại): mỗi clip một ý trọn, hiểu được khi xem riêng, số clip và độ dài theo ý. Mọi chữ trên clip là nguyên văn lời người nói — kể cả thẻ tiêu đề (cụm then chốt nhất) và màn chốt; phụ đề cụm 5–8 chữ; cắt cứng giấu điểm nối, rút khoảng lặng; hai tông sôi động / lắng với nhạc từ kho kênh; clip dọc không thanh thời gian, mọi clip không thẻ cuối — dẫn về bản đầy đủ ở caption và bình luận ghim. Đoạn nổi bật ra ĐÚNG LOẠI video gốc — nguồn người nói thì dùng khung ghép của dung-video-theo-phong-cach; nguồn podcast hoặc đồ hoạ thì dựng podcast đồ hoạ cùng khung nguồn (dung-podcast). Kèm lịch đăng, mô tả, bình luận ghim. Dùng khi người dùng nói "cắt highlight", "làm video highlight", "cắt clip ngắn từ video dài", "làm Reels/TikTok/Shorts từ video YouTube/podcast", "cắt đoạn hay", "/cat-doan-noi-bat", hoặc đưa một video dài (kể cả podcast đã dựng) muốn ra clip ngắn — kể cả khi chỉ gửi file mà không nói rõ.
---
# Cắt đoạn nổi bật cho mọi mục video ngắn

**Chọn hiệu ứng và thẩm mỹ trước khi viết cảnh.** Áp dụng [hướng dẫn dùng chung](../thiet-ke-bo-cuc/huong-dan-lua-chon.md) bước 2b và 4d cho đầu vào này. Đối chiếu hai hướng thẩm mỹ, so ứng viên cho từng ý cần hình và ghi phương án khớp mã cảnh. Nếu mẫu thiếu công cụ, chuyển thể hoặc ghi lý do chọn ứng viên khác. Xem các cảnh liên tiếp trên video thử để xác nhận bố cục, nhịp và vùng an toàn.

**Đọc trước:** `../quy-tac-chung.md` (mục 8) · hồ sơ `../ho-so-thuong-hieu/doan-noi-bat.md`. Lỗi thường gặp: đọc của `$BASE`, thêm của `$POD` khi nguồn là podcast.

`$BASE=~/.claude/skills/dung-video-theo-phong-cach`, `$POD=~/.claude/skills/dung-podcast`, `$SKILL` là thư mục này. Skill này đảm nhận **nhận loại
video gốc, hiểu cả video, chọn khoảnh khắc, cắt câu, bố trí lời kêu gọi hành động**; phần dựng dùng quy trình của skill tương ứng.

Mục tiêu: từ một video gốc, Claude **tự chọn ý** rồi ra các clip ngắn **cùng loại với video gốc**. Mỗi clip là **một ý trọn vẹn** và đạt cùng lúc **hai mục tiêu**:
1. Người xem không sang video dài vẫn **mang về được một sự chuyển hoá** từ chính clip.
2. Người xem **muốn mở bản đầy đủ** vì bản dài còn những điều khác.

Clip đẹp mà xem xong không hiểu gì, hoặc hiểu mà không mang về được gì, là clip hỏng.


## Bốn câu chọn ý (luật gốc của skill, đứng trên mọi luật khác của skill khi trái nhau)
Claude **tự chọn ý, không hỏi David chọn đoạn**. Claude đọc nối lời như người xem mới chưa xem bản dài, trả lời đủ 4 câu cho từng clip và ghi vào `chon_y` trong `phuong-an.json`. Thiếu một câu thì chọn lại ý, không giao.
| Khoá | Câu hỏi | Đạt khi |
|---|---|---|
| `boi_canh` | Ngay đầu clip, người xem mới có biết ai đang nói, chuyện gì, vì sao nói không? | Nói được bằng chính lời trong clip; thiếu thì thêm câu nguyên văn nêu hoàn cảnh |
| `y_tron` | Có đủ từ vấn đề hoặc câu hỏi đến lời giải hoặc điều nhận ra, và kết thúc được không? | Không dừng giữa mạch, không chỉ kể chuyện hay chỉ nêu cảm xúc |
| `mang_ve` | Không xem video dài, họ mang về điều gì? | Một câu rõ: cách nghĩ mới, câu tự hỏi hoặc việc làm, có trong lời người nói; không bắt buộc câu giao việc |
| `chua_lai` | Bản dài còn thêm gì ngoài ý đã trọn này? | Một chuyện khác hoặc ý mở rộng; không được chừa phần kết của ý trong clip |

**Không có con số cố định** cho độ dài hay số clip: ý cần bao lâu thì clip dài bấy lâu, video có bao nhiêu ý đạt thì ra bấy nhiêu clip. Clip dài mà còn giữ được người xem thì giữ; có đoạn thừa thì bỏ đoạn thừa, không cắt vào ý cho vừa số giây. Claude được ghép hai đoạn xa nhau khi đúng mạch ý của người nói, nhưng phải báo rõ các mốc trong báo cáo giao bản. Báo cáo giao bản ghi đủ 4 câu và lời đọc nối; David duyệt ở bản cuối.

## Luật riêng của đoạn nổi bật (kiểm lại trước khi giao)

Vị trí và thành phần cố định theo bộ nhận diện chung `../thu-vien-tai-nguyen/nhan-dien-chung.md`. Clip nổi bật khung dọc: không có thanh
thời gian, không có thẻ cuối, màn chốt trên hình, kết ở chữ cuối để tự lặp (clip khung ngang: mục "Highlight ngang"). Mọi clip: dẫn về bản đầy đủ nằm ở caption và bình luận ghim (khối 15).

1. **Cùng loại với video gốc**: nguồn người nói ra clip người nói, nguồn đồ hoạ ra clip đồ hoạ; giữ phong cách cùng tên tập, tên người nói của bản gốc (khối 13, bước 0).
   **Khung clip bằng khung video gốc** (`../quy-tac-chung.md` mục 4): gốc ngang thì làm theo mục "Highlight ngang" dưới bước 7A; chỉ đổi khung khi David yêu cầu rõ. Khi David yêu cầu đổi sang dọc: không cắt thẳng hình đồ hoạ ngang vào khung dọc mà phải dựng lại.
2. **Số clip theo số ý đạt 4 câu**: mỗi clip một ý KHÁC NHAU, không trùng câu chính; không thêm clip đệm cho đủ số. David yêu cầu một số clip cụ thể thì chọn các ý mạnh nhất cho đủ số đó. Clip A là ý mạnh nhất (đăng đầu tiên).
3. **Mọi chữ là nguyên văn** (thẻ tiêu đề, phụ đề, chữ to, màn hành động, ý đang bàn, màn chốt) — quy-tac-chung mục 1: chỉ chọn câu,
   bỏ bớt chữ ở đầu/cuối câu, sửa chính tả Whisper. Không có ngoại lệ. Mô tả bài đăng theo giọng David (khối 15).
4. **Màn chốt — một luật cho cả hai nhánh**: người nói có câu mệnh lệnh/giao việc hay câu mời bình luận nguyên văn ("Hãy chọn…",
   "thử làm…") thì màn chốt dùng câu đó. Không có thì clip kết ở câu chốt ý; **không dừng lại để báo David**, không ghép
   câu kêu gọi hành động từ chỗ khác; clip vẫn phải đạt `mang_ve`. "Vấn đề / Kết quả" để ở mô tả và bình luận ghim.
5. **Ý của cả video**: luôn làm bước 2 (bản đồ cả video) trước khi chọn. Mỗi clip phục vụ lời hứa cốt lõi hoặc một ý lớn của video. **Người xem clip là người xem độc lập**: mỗi clip phải qua đủ bốn câu chọn ý và tự đạt câu hỏi gốc của bộ lọc (làm chủ bản thân hoặc công việc); chỉ nói cảm xúc hoặc chỉ kể chuyện thì không đạt.
6. **Không thứ tự cố định**: vị trí lời kêu gọi hành động do Claude tự bố trí theo mạch (khối 13, bước 4); đổi thứ tự không được làm sai nghĩa. Độ dài theo ý.
7. **Thẻ tiêu đề mở đầu** (chuẩn DOAC/Mel Robbins): **cụm nguyên văn then chốt nhất của clip**, Claude tự chọn, ngắn, 2 dòng, nửa trên khung; nêu
   điều được mất, kết quả hoặc mâu thuẫn của clip nếu lời nói có. Câu hook (câu chạm) vẫn là lời thật ngay giây 0. Ghi tiêu đề và mốc câu gốc vào ke-hoach-cat.md.
8. **Nhịp kênh lớn**: **cắt cứng** giữa các câu, không phóng to xen kẽ ở điểm cắt (quy-tac-chung mục 2); khoảng lặng ít nhất 0,45 s **trong** câu và
   > 0,6 s **giữa** câu rút còn khoảng 0,24 s; phụ đề **cụm trọn ý 5–8 chữ, cỡ bằng chữ thẻ, ẩn khi lớp chữ motion graphic hiện** (quy-tac-chung mục 3). Giữ 1 s lặng sau câu hỏi kêu gọi. Kiểu cũ có chip tua chỉ khi David yêu cầu: `--tua` cho `cat-doan-noi-bat.py` + `danh-sach-cat-doan-noi-bat.py`.
9. **Hai tông** theo cảm xúc lời nói, được đổi giữa chừng (mỗi lần đổi tông là một điểm nhấn cảm xúc):
   | | **Sôi động** `soi` (mẹo, tin vui, kết quả, lời mời) | **Lắng** `lang` (tâm sự, nỗi đau, mất mát, câu hỏi day dứt) |
   |---|---|---|
   | Nhạc | bài vui `soi-*` | bài trầm `lang-*` (piano/dây) |
   | Chữ to | bật nảy, gạch cam | hiện chậm, nét mảnh, không gạch |
   | Hình | dồn khung | màu dịu |
   Nhạc lấy từ **kho nhạc kênh** (`$SKILL/assets/nhac/`), Claude tự chọn theo tuyến nội dung (khối 09). Mức nhạc
   theo chuẩn âm lượng chung (thấp hơn giọng khoảng 23 dB). Không có nhãn kỹ thuật, không có thẻ "TẬP NÀY CÓ GÌ?" hay tên vòng.
10. **Chừa cho bản đầy đủ đúng chỗ**: chừa một chuyện khác hoặc ý mở rộng; ý trong clip phải đi đến hết. Câu mở đầu ưu tiên điều bất ngờ, kết quả lớn hoặc điều được mất hơn lời than chung chung.
11. **Không thẻ cuối; clip dọc không thanh thời gian, clip ngang có thanh thời gian** (video dọc ngắn: `nhan-dien-chung.md` mục 1). `danh-sach-cat-doan-noi-bat.py` vẫn ghi `ENDCARD` từ
    `"endcard"` trong phuong-an.json (tên tập gốc, người nói) nhưng mẫu tự bỏ ở video dọc ngắn; ghi đủ để dùng khi David cần bản dọc dài.
    Không có tên tập gốc thì tra sổ danh mục nội dung; vẫn không có thì ghi chỗ trống trong báo cáo (`../nhan-dien-thuong-hieu.md`).
12. **Tự chọn, không hỏi** (`chuan-muc-lam-viec.md` mục 2): nhận yêu cầu cắt là Claude tự chọn ý, tiêu đề, câu màn chốt rồi dựng trọn
    một mạch. Chỉ dừng lại hỏi khi không ý nào đạt 4 câu hoặc câu chủ chốt xung đột với lằn ranh. Luôn ghi rõ đã chọn gì trong báo cáo để David sửa ở bản cuối.
13. **Học từ 20 đoạn nổi bật Việt** (`references/hoc-tu-20-doan-noi-bat-vn.md`):
    - **Tiêu đề ghim** (mặc định tắt, hồ sơ `tit_ghim: false`, vì khung dọc mỗi lúc ít thành phần): ghi `"tit"` vào từng option của phuong-an.json
      (`danh-sach-cat-doan-noi-bat.py` tự viết `pow` mở đầu); `"pin": true` để tiêu đề thu nhỏ thành dải dưới dấu kênh suốt clip tới màn chốt (`pinTitle`).
      Nhánh podcast: `STAGE.title` là tiêu đề.
    - **Khung bìa ở 0,3 s** (thẻ tiêu đề và mặt người nói rõ) — ghi mốc này vào dang-bai.md.
    - **Cảnh phản ứng**: nguồn có khán giả hoặc người dẫn thì piece thêm `"react": {"at": <giây nguồn ngay sau cụm đắt>, "from": <giây
      nguồn có mặt người nghe>, "len": 0.8–1.5}` — hình người nghe, tiếng người nói vẫn chạy.
    - **Danh sách đếm / hướng dẫn từng bước**: giữ đủ các ý trong danh sách để ý được trọn.

## Đầu vào

1. **Video gốc** (mp4/mov…; file chỉ có tiếng thì dựng podcast trước bằng `dung-podcast`, rồi cắt từ `video-hoan-chinh.mp4` — script cắt cần hình) — hoặc **thư mục dự án** đã dựng nó (`~/Movies/tap-<tên>/2-ban-day-du`, dự án Codex dạng `…/work/podcast-<tên>`):
   thư mục dự án là tốt nhất, vì có lời đã sửa chính tả, tiếng sạch, kịch bản, tên tập. Chỉ có video-hoan-chinh thì tìm thư mục dự án cạnh nó (
   `outputs/` và `work/` nằm cùng thư mục cha, hoặc `~/Movies/*/video-hoan-chinh.mp4`). Không tải video từ YouTube/TikTok mà nhờ David gửi file.
2. **Phụ đề** .srt/.vtt nếu có (trong YouTube Studio, vào mục Phụ đề rồi chọn Tải xuống): để sửa chính tả; mốc cắt vẫn lấy từ `moc-tung-tu.srt`.
3. **Dàn ý** (Vấn đề · Giải pháp · Thực thi), đoạn đã đánh dấu "highlight" nếu có thì ưu tiên.

Chỉ có phụ đề, không có video thì làm bước 2–5, trả bảng cắt, mô tả và bình luận ghim để cắt bằng công cụ khác.

## Công thức — Đoạn nổi bật · hồ sơ `doan-noi-bat`
| # | Bước | Khối |
|---|---|---|
| 0–1 | Nhận loại nguồn · tạo dự án *(bước nhẹ)* | [13](../mo-dun/13-chon-doan-noi-bat/README.md) · [01](../mo-dun/01-chep-loi/README.md) |
| 2–6 | Bản đồ cả video · tự chọn ý theo 4 câu · chọn câu · bố trí lời kêu gọi hành động · kiểm hiểu được khi xem riêng + lằn ranh · cắt + kiểm lời | [13](../mo-dun/13-chon-doan-noi-bat/README.md) (chi tiết từng bước) · [02](../mo-dun/02-lam-sach/README.md) (khoang-lang.py) · [01](../mo-dun/01-chep-loi/README.md) |
| 7A | Chẩn đoán → tự chọn ([huong-dan-lua-chon](../thiet-ke-bo-cuc/huong-dan-lua-chon.md)) · dựng nguồn có người nói (mục dưới) | [11](../mo-dun/11-dung-ghep/README.md) · [04](../mo-dun/04-khung-hinh/README.md) · [05](../mo-dun/05-tranh-che-chu-the/README.md) · [06](../mo-dun/06-phan-mo-dau/README.md) · [07](../mo-dun/07-canh-minh-hoa/README.md) · [08](../mo-dun/08-phan-ket/README.md) · [03](../mo-dun/03-phu-de/README.md) · [09](../mo-dun/09-am-thanh/README.md) · [17](../mo-dun/17-kiem-soat-chat-luong/README.md) |
| 7B | Chẩn đoán → tự chọn · dựng nguồn podcast / đồ hoạ (mục dưới) | [12](../mo-dun/12-san-khau-podcast/README.md) · [07](../mo-dun/07-canh-minh-hoa/README.md) · [08](../mo-dun/08-phan-ket/README.md) · [17](../mo-dun/17-kiem-soat-chat-luong/README.md) |
| 8 | Phát hành: lịch đăng, khung bìa, mô tả, bình luận ghim, số liệu | [15](../mo-dun/15-xuat-ban/README.md) · [16](../mo-dun/16-phan-tich-so-lieu/README.md) |

### 7A. Dựng — nguồn có người nói (`dung-video-theo-phong-cach` chế độ ghép clip, `references/nhieu-doan-video.md`)
Hai lệnh `nang-khung.py` và `bao-ve-lop-phu.py` dưới đây **chỉ dùng cho khung dọc**; khung ngang theo mục "Highlight ngang".
Làm lần lượt cho từng clip `<id>` (A, B…). `cat/<id>.mp4` của bước 6 chỉ để **kiểm lời**; bản dựng đọc trực tiếp video gốc theo mốc trong phuong-an.json (mỗi câu thêm
`"tone": "lang"|"soi"`, câu dùng cho màn chốt thêm `"cta": true`):
```bash
LOI_SAN="$P/kiem-tra/goc" zsh $BASE/scripts/tao-dung-ghep.sh hl-<tên>-<id> "$P/nguon.<ext>"   # chạy nền → ~/Movies/tap-<tên>/3-doan-noi-bat/clip-<id> = $E (c1 = video gốc; LOI_SAN = dùng lại lời đã chép, không chép lại cả video cho mỗi clip)
python3 -I $SKILL/scripts/danh-sach-cat-doan-noi-bat.py "$P" "$E" <id>                   # → $E/chuyen-dong/src/danh-sach-cat.js viết sẵn
cp $SKILL/assets/nhac/*.mp3 "$E/chuyen-dong/public/hieu-ung-am-thanh/"                 # kho nhạc kênh (soi-*, lang-*)
```
`danh-sach-cat-doan-noi-bat.py` viết: các câu `p1…pN` **cắt cứng**, khoảng lặng trong câu đã rút (đoạn con `p2b`, `p2c`…), không phóng to xen kẽ;
`SUBS` (giây timeline, chữ đúng câu nguyên văn — hiện cụm 5–8 chữ nhờ `SHORT = true`); `TS(src)` đổi giây video gốc thành giây
timeline cho lớp phủ; `TONE` và `MUSIC.tracks`; `CTA` là câu kêu gọi hành động nguyên văn (nếu có); `HL = {…, bar: false}` (không có thanh tập gốc).
Claude chỉnh tiếp trong danh-sach-cat.js:
- **Phụ đề**: sửa chính tả, đánh dấu từ khoá bằng `hl` (từ trong `hl` hiện màu cam khi tới nhịp của nó).
- **Chẩn đoán trước** (bắt buộc, render bị chặn nếu thiếu): chạy `python3 -I $BASE/scripts/chan-doan.py "$E"` rồi đọc `$E/kiem-tra/goi-y-kieu.md`
  (công cụ dò dạng từng câu) rồi ghi `$E/ke-hoach-canh.md` mục `## Chẩn đoán` (mẫu, thẩm mỹ, bảng ý ứng với kiểu) theo `../thiet-ke-bo-cuc/huong-dan-lua-chon.md`.
  Không chép lớp phủ của clip hay tập trước.
- **OVERLAYS** theo bảng ý ứng với kiểu (mốc bằng `TS(<giây>)`; mọi chữ nguyên văn): liệt kê hoặc các bước dùng `illus list` · `chips` · `diagram tang` ·
  so sánh, đổi ý dùng `illus vs` · `diagram tu-thanh` · con số người nói dùng `illus count` · nhân quả dùng `illus flow` · `diagram chuyen-giao` ·
  giao việc dùng `action` (`quote` nguyên văn) · câu hỏi then chốt dùng `callout` · điểm chốt dùng `pow` (tối đa 14 ký tự/dòng). **pow không phải mặc định.**
  Nền cảnh `phong: 'hat'` cho đoạn lắng. Mật độ theo nội dung: dày hơn ở `soi`, thưa hơn ở `lang`.
- **Hình**: không zoom vào / ra (quy-tac-chung mục 2); có thể `replay` khoảnh khắc then chốt.
- `CTA.kind` theo việc được kêu gọi (lưu dùng `save`, bình luận dùng `comment`…); không có câu kêu gọi hành động thì không đặt `CTA` (luật 4).
- **Thẻ tiêu đề mở đầu** (luật 7): `{type: 'pow', start: 0, end: 2.5, text: '<TÍT nguyên văn>', y: 300}` — nửa trên khung, tách khỏi phụ đề.
  `ENDCARD` do `danh-sach-cat-doan-noi-bat.py` ghi (luật 11), mẫu tự bỏ ở video dọc ngắn.
Rồi làm như nhieu-doan-video.md: chạy `python3 -I $BASE/scripts/nang-khung.py "$E"`, rồi `python3 -I $BASE/scripts/bao-ve-lop-phu.py "$E"` (lớp phủ che mặt hoặc thân trên thì
chuyển thành toàn màn hình; tiêu đề ghim che đầu thì ẩn), rồi `node anh-tinh.mjs <mốc>` (chụp: thẻ tiêu đề, mỗi pow/action lúc đầy nhất, 2–3 mốc thấy phụ đề,
ngay sau 1–2 điểm cắt, cuối clip thấy màn chốt), sửa tới khi không còn lỗi, rồi `node xuat-chuong-trinh.mjs` (chạy nền; render các clip nối tiếp,
không chạy song song vì tốn RAM). Không có bước duyệt kế hoạch ghép của chế độ ghép nhiều clip (luật 12).

### Highlight ngang (video gốc ngang) — nguồn người nói, mẫu ghép
- `danh-sach-cat.js`: `W = 1920`, `H = 1080`; `THE_CUOI = false` (kết ở màn chốt); thanh thời gian tự có (khung ngang). Bỏ `nang-khung.py` và
  `bao-ve-lop-phu.py` (chỉ tính cho khung dọc) — tự rà soát bằng ảnh chụp thử: `pow` đặt `x` (tâm khối chữ, px) vào vùng trống cạnh người nói.
- Nguồn nhiều video dài (ổ đĩa không đủ dung lượng để chép bản gốc): chép lời trên bản dung lượng nhỏ ghép các video, chọn ý, rồi cắt các cửa sổ cần dùng từ file gốc
  (1920×1080, 30 fps) ghép thành `nguon.mp4` mới và chép lời lại — mốc trong `phuong-an.json` theo nguồn mới.
- **Đoạn ghép mở đầu (intro)** khi David yêu cầu: thêm vào đầu `RAW` các đoạn `m1…` (câu then chốt giữ tiếng ≈ 3 s, rồi cảnh câm thật sự khác nhau
  2 phách bài `intro-soi`/`intro-lang`), `D = segStart('p1')`; phụ đề phần chính cộng `D`, `TS()` bỏ qua đoạn `m`; thẻ `title` `over` trên dải
  cảnh câm, chữ nguyên văn; nhạc `tracks` gồm bài intro và bài phần chính, `loudRanges` là dải cảnh câm. Luật chọn cảnh ở `nhieu-doan-video.md` mục 2d.1.
  Mẫu: `~/Movies/tap-marketing-noi-dau-nhu-cau/3-doan-noi-bat/clip-A`.
- **Thêm bản dọc từ nguồn ngang (chỉ khi David yêu cầu)**: không cắt thẳng mà đổi khung `nguon.mp4` bám theo người nói (`phan-tich-doi-khung.sh` và `ke-hoach-doi-khung.py`
  trong dự án phụ `clip-<id>-doc/rekhung`, `tu-lieu/video-goc.mp4` là liên kết cứng tới c1; mọi câu bám người đang nói, cảnh intro đặt `cx` riêng,
  cảnh có người đi ngang hoặc thấy cả quán thì dùng `wide`), rồi chép `chuyen-dong` của bản ngang, c1 là bản dọc (cùng thời lượng nên giữ nguyên mốc),
  `W = 1080`, `H = 1920`, bỏ `pow.x`; người ngồi cả thân lấp giữa khung thì `pow` đặt `y` vào dải trống trên đầu (đỉnh đầu khoảng 650 px thì đặt `y: 300`);
  thẻ `title` trên intro thêm `keep: true` để không thành toàn màn hình che hết cảnh câm. Rồi chạy `nang-khung.py`, rồi `bao-ve-lop-phu.py`, rồi chụp thử như 7A.
  Mẫu: `~/Movies/tap-marketing-noi-dau-nhu-cau/3-doan-noi-bat/clip-B-doc`.

### Nguồn đã làm sạch từ video tối đa 3 phút — dựng bằng mẫu 1 video
Bản sạch của video tối đa 3 phút đã rút khoảng lặng rồi, nên **không rút lặng lần hai** (lần hai dễ cắt mất chữ nói nhỏ): ghép các đoạn trọn
câu bằng `ffmpeg` (`trim` + `concat`, mờ tiếng 15–30 ms ở mỗi đầu) thành `tu-lieu/video-goc.mp4`, chép `chuyen-dong` của bản đầy đủ, dời mốc
`phu-de.js` và các cảnh nằm trong những đoạn đó, rồi chụp thử và render như bản đầy đủ. Khung theo video gốc.

### 7B. Dựng — nguồn podcast / toàn đồ hoạ (`dung-podcast`; khung theo nguồn, lệnh dưới là ví dụ khung dọc)
```bash
zsh $POD/scripts/tao-podcast.sh "$P/cat/<id>.mp4" hl-<tên>-<id> "" cat-thua   # mỗi clip → ~/Movies/tap-<tên>/3-doan-noi-bat/clip-<id> = $E (chỉ lấy tiếng)
zsh $POD/scripts/chep-loi.sh "$E"
python3 -I $BASE/scripts/phu-de.py "$E"                         # rồi sửa chữ theo captions-goc.js của $P (đã sửa chính tả)
PY=$(zsh $POD/scripts/cai-python.sh); $PY $POD/scripts/tach-luot-nguoi-noi.py "$E"; $PY $POD/scripts/duong-bao-am.py "$E"
```
- `tao-podcast.sh … cat-thua` còn 0,4 s lặng cuối thì đệm thêm cho đủ 1 s lặng, cập nhật `project.duration`, chạy lại `duong-bao-am.py`.
- **Tông, nhạc, thẻ cuối**: chạy `python3 -I $SKILL/scripts/ap-dung-doan-noi-bat.py "$P" <id> "$E"` để ghi `chuyen-dong/src/doan-noi-bat.js` (cắt cứng: `bar: false`,
  không có chip tua; tự trừ phần cắt đầu ghi trong `kiem-tra/cat-goc.txt`).
- Số người nói (1|2) và `STAGE` lấy từ `scenes-goc.js`: `title` là tên tập gốc, `speakers` là tên người nói gốc, `show` giữ như gốc.
  `chu-de.js`/`phong-chu.js` khác mặc định thì chép sang. Biểu tượng vẽ thêm trong dự án gốc thì chép `bieu-tuong.jsx` nếu cảnh cần.
- **Không bìa** (`COVER = null`) trừ khi David muốn — video ngắn vào thẳng câu hook (câu chạm).
- `"endcard": {}` trong phuong-an.json là đủ (để trống thì lấy `STAGE.title` và người nói của `STAGE`); mẫu tự bỏ thẻ cuối ở video dọc ngắn.
- `TOPICS` 2–3 mục cho cả clip (mốc là lúc bắt đầu ý), chữ trích lời, không lặp chữ của cảnh đang hiện.
- **Tông và nhạc**: ghi `tone` cho từng câu như 7A; `ap-dung-doan-noi-bat.py` chép vào `doan-noi-bat.js` (`nhac`), rồi `xem-truoc-ban-dung.py` trộn nhạc
  kho kênh dưới tiếng nói (khoá `nhac_chu_chinh` trong `ho-so-thuong-hieu/doan-noi-bat.json`), không có tiếng ký hiệu đầu clip; chuyển cảnh `lang` không có tiếng vút.
- `anh-tinh-podcast.sh` chụp thử (mỗi cảnh lúc đầy nhất và vài mốc `nen@`), rồi `node xuat-video.mjs`, rồi `nen-podcast.py`, rồi `xem-truoc-ban-dung.py`,
  rồi `kiem-khung-hinh.sh` như bước 7–9 của `$POD/SKILL.md`.

### Kịch bản đoạn nổi bật podcast (7B) — mẫu chuẩn 3 clip "Đi trainer", MỌI chữ nguyên văn lời trong clip
Mẫu: `~/Movies/tap-di-trainer/3-doan-noi-bat/clip-{A,B,C}`, thành phẩm ở Drive `thanh-pham/tap-di-trainer/highlight/clip-a|b|c.mp4`, lời và kịch bản ở `du-an/video-di-trainer/`.
- **Chữ chính thay phụ đề** (`ap-dung-doan-noi-bat.py` tự bật `chu_chinh`): không có dải phụ đề, không có dòng chủ đề, không `kinetic`; mỗi dòng `phu-de.js` là một câu trọn ý (tối đa 3 dòng, khoảng 55 ký tự), có từ khoá `hl`. Cảnh đồ hoạ dùng `illus` `single` `compact: true`, không `label`, để chỉ có một lớp chữ.
- **Hoàn cảnh:** thiếu thì đưa câu nguyên văn nêu hoàn cảnh lên đầu clip.
- `hook` mở đầu: **thẻ tiêu đề** nguyên văn (luật 7), `eyebrow` trích lời hoặc bỏ trống.
- **Hình theo ý cần hiểu**, không lấp từng cụm lời: thêm `montage`/`card` biểu tượng (biểu tượng vẽ kèm nhãn trích lời) chỉ ở đoạn mà hình
  giúp người xem hiểu nhanh hơn (quy-tac-chung mục 0). 3 clip "Đi trainer" là mẫu về cách dựng (chữ chính, nhạc, màn chốt).
- `action` đúng lúc câu HANHDONG (`icon`, thiếu thì vẽ thêm: `write` là viết ra giấy; `quote` nguyên văn, `quoteAt`, `doneAt`).
- Điểm chốt cảm xúc: cụm ngắn nhất, then chốt nhất, `start` là lúc bắt đầu nói cụm đó (mốc từ `moc-tung-tu.srt` của `$E`). Nguồn người nói mà
  `vi-tri-khuon-mat.sh` báo "⚠ vẫn che mặt" thì đổi điểm chốt thành `card` toàn cảnh (ví dụ: `ages` cho con số: số chạy đúng lúc nói kèm `quote`
  nguyên văn; `ages` cần `pillAt` kể cả khi nhãn tự ẩn, thiếu thì lỗi "Frame NaN"), đặt sau phần dồn khung.
- Tối đa một `card` nếu ý chính có con số, so sánh, danh sách; không có thì bỏ.
- **Màn chốt** theo luật 4: có câu kêu gọi hành động nguyên văn thì `cta` `text` là câu đó (tối đa 55 ký tự; dài hơn thì chọn vế trọn ý; `**cụm**` để tô nhấn),
  `kind` theo việc được kêu gọi; báo cáo ghi mốc của câu. Không có thì kết ở câu chốt ý.
- Kiểm thêm khi chụp thử: chữ to có đủ lớn không (dòng dài làm chữ co nhỏ thì giảm sức tác động, phải rút ngắn cụm); vài mốc thấy chữ chính đọc rõ, không chạm
  sóng âm. `phu-de@…` không có trong `ghep-anh-tinh.sh` khi đứng riêng thì tự ghép lên `video-goc.mp4` cùng mốc.
- Bản cuối: cùng khung video gốc, thời lượng theo ý, âm lượng và tiếng rè bằng nguồn.

## Bảng phụ thuộc (sửa X thì chạy lại Y)
| Sửa | Chạy lại |
|---|---|
| phuong-an.json (câu, mốc, tit, react, tone) | cat-doan-noi-bat.py (kiểm lời) → danh-sach-cat-doan-noi-bat.py → nang-khung.py → bao-ve-lop-phu.py → stills → render |
| danh-sach-cat.js sửa thủ công (OVERLAYS, SUBS) | bao-ve-lop-phu.py → stills → xuat-chuong-trinh.mjs |
| 7B: cat/<id>.mp4 | tao-podcast.sh … → ap-dung-doan-noi-bat.py → xuat-video.mjs → nen-podcast.py → xem-truoc-ban-dung.py |
| hồ sơ doan-noi-bat | danh-sach-cat-doan-noi-bat.py / cat-doan-noi-bat.py chạy lại |

## Tiêu chí đạt
- Mỗi clip đạt đủ bốn câu chọn ý (`chon_y`), báo cáo ghi 4 câu, lời đọc nối và mốc đoạn ghép
- Thẻ tiêu đề nguyên văn; bố cục tự cân (dọc: mỗi lúc ít thành phần, `../thiet-ke-bo-cuc/`); màn chốt theo luật 4; không thẻ cuối, không thanh thời gian; kiểm lời khớp
- dang-bai.md: lịch đăng, mốc bìa 0,3 s, mô tả, bình luận ghim · so-lieu.md

## Điều không làm
- Không viết thêm, không đổi chữ của người nói trên clip; không ghép câu tạo ra ý người nói không nói.
- Không đổi khung so với video gốc khi David không yêu cầu.
- Không đổi loại video (podcast không thành người nói, người nói không thành toàn đồ hoạ); không cắt thẳng hình đồ hoạ ngang vào khung dọc.
- Không dùng giọng đọc AI thay người nói; không thêm lời bán hàng vào clip; giá chỉ hiện khi chính người nói nêu và là sản phẩm công nghệ (hướng 3), bài về con người không nói giá, không nói gói.
- Không ghi cứng phụ đề vào hình bằng ffmpeg (`subtitles=`/`drawtext` — ffmpeg Homebrew không có libass/freetype); phụ đề luôn qua Remotion
  theo chuẩn chung `kieu-phu-de.js`; không phủ phụ đề lên video đã có phụ đề ghi cứng sẵn.

## Cấu trúc
```
~/Movies/tap-<tên>/3-doan-noi-bat/   (<tên> = đúng tên tập của bản dài)
├── nguon.<ext> · loai.txt          # video nguồn (bản không bìa nếu lấy từ dự án) · loại video gốc
├── kiem-tra/goc/                      # ban-chep-loi.srt · moc-tung-tu.srt · am-luong-05.txt · bang-khung-hinh.jpg · captions-goc.js · scenes-goc.js · phu-de-youtube.srt
├── phuong-an.json                  # các clip (A, B, C…), chon_y + câu theo thứ tự phát (Claude viết)
├── cat/<id>.mp4 · <id>.md · <id>-map.json · <id>-kiem.txt
├── ke-hoach-cat.md · dang-bai.md · so-lieu.md
~/Movies/tap-<tên>/3-doan-noi-bat/clip-<id>/   → video-hoan-chinh.mp4 (BẢN CUỐI mỗi clip, cùng khung video gốc)
$SKILL/assets/nhac/               # soi-*.mp3 · lang-*.mp3 — kho nhạc kênh
```

## Xong khi
1. Mỗi clip đạt đủ bốn câu chọn ý; báo cáo ghi 4 câu và lời đọc nối.
2. Clip cùng loại và **cùng khung** video gốc (khác khung chỉ khi David yêu cầu).
3. Mọi chữ trên clip nguyên văn (cả tiêu đề, màn chốt).
4. Không cắt vào giữa ý; lời bản cắt đã chép lại đối chiếu khớp.
5. Phụ đề cụm khoảng 5–8 chữ (tối đa theo hồ sơ `phu_de.ngan_max_chu`) không chồng chữ motion graphic; không thẻ cuối; clip dọc không thanh thời gian.
6. Nhạc từ kho kênh, thấp hơn giọng khoảng 23 dB.
7. Có dang-bai.md (lịch đăng, mốc bìa, mô tả, bình luận ghim) và so-lieu.md; David không phải sửa lại vì trái luật đã chốt.
8. David chốt cả tập thì clip cuối vào `~/Movies/cho-dang/<tập>/highlight/` và chạy `cho-dang.sh gui <tập>`, rồi dọn file tạm ngay bằng `don-tap.py --xoa` rồi `luu-drive.sh` lên Drive (khối 17), không hỏi lại; chỉ hỏi phần ⏸ đang làm chưa xong.

## Tài liệu kèm (chỉ đọc khi bước cần, cân nhắc đổi luật hoặc gỡ lỗi)
- `references/nhat-ky-thay-doi.md` — quyết định theo ngày kèm lý do.
- `references/hoc-tu-20-doan-noi-bat-vn.md` — 20 đoạn nổi bật Việt đã phân tích (nguồn của luật 13).
- Ví dụ thật (bản chuẩn): `~/Movies/tap-di-trainer/3-doan-noi-bat/clip-A|B|C`. Nguồn có người nói chưa có ví dụ đang giữ trên máy.
