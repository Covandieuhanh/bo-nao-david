---
name: cat-highlight-video
description: Cắt một video dài (bản YouTube 5–60 phút của người dùng) thành các clip highlight DỌC 9:16 (1080×1920), tự chọn ý: mỗi clip một ý trọn vẹn, tự đứng được, số clip và độ dài theo đúng ý cần truyền tải — dùng chung cho Reels, TikTok, Shorts, Facebook Reels, theo chuẩn đội cắt clip của kênh lớn (DOAC, Jay Shetty, Hormozi): thẻ tít mở đầu viết như tít báo đúng ý người nói, phụ đề 1–3 chữ to mỗi nhịp, cắt cứng giấu mối + cắt sạch khoảng lặng, nhịp hai tông (sôi động / lắng, nhạc nền cố định của kênh). Highlight ra ĐÚNG LOẠI của video gốc — video tự quay có người nói → hình người nói (khung dựng của skill video-style-edit); podcast/video toàn đồ hoạ → podcast đồ hoạ dọc cùng phong cách, cùng tên tập (skill podcast-style-edit). Lời trong clip chỉ là nguyên văn lời người nói (không viết thêm, không đổi chữ), mỗi clip có lời kêu gọi hành động, tự soát điểm cắt theo độ lớn tiếng và chép lời lại bản cắt để kiểm; kèm lịch đăng, mô tả bài đăng, bình luận ghim. Dùng khi người dùng nói "cắt highlight", "làm video highlight", "cắt clip ngắn từ video dài", "làm Reels/TikTok/Shorts từ video YouTube/podcast", "cắt đoạn hay", "/cat-highlight-video", hoặc đưa một video dài (kể cả video podcast đã dựng, kèm hoặc không kèm phụ đề, dàn ý) và muốn ra clip ngắn — kể cả khi chỉ gửi file mà không nói rõ.
---
# Cắt video highlight cho mọi mục video ngắn

Mục tiêu: từ một video gốc, **tự chọn ý** rồi ra các clip ngắn **cùng loại với video gốc**. Mỗi clip là **một ý trọn vẹn** và đạt cùng lúc **hai mục tiêu** (David chốt 2026-11-07):
1. Người xem không sang video dài vẫn **mang về được một sự chuyển hoá** từ chính clip.
2. Người xem **muốn mở bản đầy đủ** vì bản dài còn những điều khác.

Clip đẹp mà xem xong không hiểu gì, hoặc hiểu mà không mang về được gì, là clip hỏng.

## Bốn câu chọn ý (luật gốc của skill, thắng mọi luật khác khi trái nhau)
Claude **tự chọn ý, không hỏi David chọn đoạn**. Đọc nối lời như người lạ chưa xem bản dài, trả lời đủ 4 câu cho từng clip và ghi vào `chon_y` trong `phuong-an.json`. Thiếu một câu thì chọn lại ý, không nộp.
| Khoá | Câu hỏi | Đạt khi |
|---|---|---|
| `boi_canh` | Ngay đầu clip, người lạ có biết ai đang nói, chuyện gì, vì sao nói không? | Nói được bằng chính lời trong clip; thiếu thì thêm câu nguyên văn nêu hoàn cảnh |
| `y_tron` | Có đủ từ vấn đề hoặc câu hỏi đến lời giải hoặc điều nhận ra, và kết thúc được không? | Không dừng giữa mạch, không chỉ kể chuyện hay chỉ nêu cảm xúc |
| `mang_ve` | Không xem video dài, họ mang về điều gì? | Một câu rõ: cách nghĩ mới, câu tự hỏi hoặc việc làm, có trong lời người nói; không bắt buộc câu giao việc |
| `chua_lai` | Bản dài còn thêm gì ngoài ý đã trọn này? | Một chuyện khác hoặc ý mở rộng; không được chừa phần kết của ý trong clip |

**Không có con số cố định** cho độ dài hay số clip: ý cần bao lâu thì clip dài bấy lâu, video có bao nhiêu ý đạt thì ra bấy nhiêu clip. Dài mà còn giữ được người xem thì giữ; có đoạn thừa thì bỏ đoạn thừa, không cắt vào ý cho vừa số giây. Được ghép hai đoạn xa nhau khi đúng mạch ý của người nói, phải báo rõ các mốc trong báo cáo giao bản. Báo cáo giao bản ghi đủ 4 câu và lời đọc nối; David duyệt ở bản cuối.

Skill này lo phần **nhận loại video gốc, hiểu cả video, chọn khoảnh khắc, cắt câu, bố trí lời kêu gọi**. Phần dựng dùng quy
trình của skill tương ứng — `$BASE=~/.claude/skills/video-style-edit`, `$POD=~/.claude/skills/podcast-style-edit`, `$SKILL` = thư
mục chứa file này. **Đọc `$SKILL/../luat-chung.md` trước** (luật chung cả bộ), rồi `$BASE/references/gotchas.md`
(+ `$POD/references/gotchas.md` khi nguồn là podcast) và `references/changelog.md`.

## Đọc trước (lần đầu trong phiên)
`../nguyen-tac.md` (7 điểm chung của hình mẫu) · `../luat-chung.md` (luật nền) · `../nhan-dien.md` (chọn loại) · hồ sơ `../ho-so/highlight.md`
(hình mẫu chính + tham số — **con số lấy ở đây, không ghi cứng**) · `../khoi/README.md` (kho khối). Skill này là **CÔNG THỨC**: thứ tự
khối + quyết định riêng của loại + tiêu chí đạt. Cách làm từng bước nằm trong README của khối; sửa cách làm → sửa khối, không sửa công thức.

## Luật riêng của highlight (kiểm lại trước khi giao)

1. **Cùng loại với video gốc**: người nói ↔ người nói, đồ hoạ ↔ đồ hoạ; giữ phong cách + tên tập/tên người nói của bản gốc (khối 13, bước 0).
   Luôn **dọc 9:16, 1080×1920**. Không cắt thẳng hình đồ hoạ ngang vào khung dọc — dựng lại.
2. **Số clip theo số ý đạt 4 câu** (David chốt 2026-11-07, thay luật 3–5 clip): mỗi clip một ý KHÁC NHAU, không trùng câu chính; không độn. David yêu cầu một số clip cụ thể thì chọn các ý mạnh nhất đủ số đó. Clip A = mạnh nhất (đăng đầu).
3. **Lời = nguyên văn** (phụ đề, chữ to, màn hành động, ý đang bàn, câu màn chốt, mô tả bài đăng): chỉ chọn câu, bỏ bớt chữ ở
   đầu/cuối câu, sửa chính tả Whisper. **Ngoại lệ duy nhất: thẻ tít mở đầu** (luật 7) viết như tít báo.
4. **Mỗi clip bắt buộc có lời kêu gọi** = câu mệnh lệnh/giao việc nguyên văn của người nói ("Hãy chọn…", "thử làm…"). Câu mời
   bình luận chỉ dùng khi người nói có nói; còn lại để ở bình luận ghim. Không có câu nào dùng được → dừng, báo David.
5. **Ý của cả video**: luôn làm bước 2 (bản đồ cả video) trước khi chọn. Mỗi clip phục vụ lời hứa cốt lõi hoặc một ý lớn của video. **Người xem clip là người xem độc lập** (David chốt 2026-11-06): mỗi clip qua đủ bốn câu chọn ý ở đầu file và tự đạt câu hỏi gốc của bộ lọc (làm chủ bản thân / công việc); chỉ nói cảm xúc hoặc chỉ kể chuyện thì không đạt.
6. **Không thứ tự cố định**: vị trí lời kêu gọi tự bố trí theo mạch (khối 13, bước 4); đổi thứ tự không được làm sai nghĩa.
   **Độ dài theo ý** (không có số cố định): xem bốn câu chọn ý.
7. **Thẻ tít mở đầu 0 → ~2,5 s** (chuẩn DOAC/Mel Robbins): ≤ 8 chữ, 2 dòng, ở nửa trên khung — **viết như tít báo** nêu tiền cược /
   kết quả / mâu thuẫn của clip, ĐÚNG Ý người nói, không thêm thông tin hay lời hứa ngoài clip (luat-chung 1b). Câu chạm vẫn là
   lời thật ngay giây 0. Ghi tít + câu gốc làm căn cứ vào ke-hoach-cat.md.
8. **Nhịp kênh lớn** (David chốt 2026-11-04 — trước đây có chip ⏩ + thanh tập gốc, đã bỏ): **cắt cứng** giữa các câu, đoạn xen kẽ
   phóng 1,08× để giấu mối; khoảng lặng ≥ 0,45 s **trong** câu và > 0,6 s **giữa** câu rút còn ~0,24 s; phụ đề **1–3 chữ to mỗi
   nhịp** (luat-chung 3). Giữ 1 s lặng sau câu hỏi kêu gọi. Kiểu cũ có chip tua chỉ khi David yêu cầu: `--tua` cho `cut_highlight.py` + `hl_edl.py`.
9. **Hai tông** theo cảm xúc lời nói, đổi giữa chừng được (cú đổi tông là cú cảm xúc):
   | | **Sôi động** `soi` (mẹo, tin vui, kết quả, lời mời) | **Lắng** `lang` (tâm sự, nỗi đau, mất mát, câu hỏi day dứt) |
   |---|---|---|
   | Nhạc | bài vui `soi-*` | bài trầm `lang-*` (piano/dây) |
   | Chữ to | bật nảy, gạch cam | hiện chậm, nét mảnh, không gạch |
   | Hình | dồn khung | màu dịu |
   Nhạc chỉ các bài cố định trong `$SKILL/assets/music/` — không tự thêm bài. Không nhãn kỹ thuật, không thẻ "TẬP NÀY CÓ GÌ?"/tên vòng.
10. **Chừa cho bản đầy đủ đúng chỗ**: chừa một chuyện khác hoặc ý mở rộng; ý trong clip phải đi đến hết. Câu mở ưu tiên bất ngờ / kết quả lớn / tiền cược hơn lời than chung chung.
11. **Thẻ cuối dẫn về bản đầy đủ ~1,8 s** sau màn chốt (kiểu Have A Sip): ảnh đứng hình người nói + nút phát + nhãn cố định
    **"XEM BẢN ĐẦY ĐỦ"** (HL-5, David duyệt 2026-11-04) + **tên tập gốc** + tên người nói gốc (+ lịch phát nếu David đưa: `"schedule"`). Ghi `"endcard": {"title": "<tên tập gốc>", "speaker": "<tên người nói>"}` vào
    `phuong-an.json` (nguồn podcast: `{}` là đủ). Không có tên tập → hỏi David. Kiểu vòng lặp → bỏ thẻ cuối.
12. **Tự chọn, không hỏi** (David chốt 2026-11-07): nhận yêu cầu cắt là tự chọn ý, tít, câu màn cuối rồi dựng trọn một mạch. Chỉ dừng hỏi khi không ý nào đạt 4 câu hoặc câu chủ chốt dính lằn ranh. Luôn ghi rõ đã chọn gì trong báo cáo để David sửa ở bản cuối.
13. **Học từ 20 highlight Việt** (`references/hoc-tu-20-highlight-vn.md`, David duyệt 2026-11-04):
    - **Tít ghim**: sau thẻ tít mở đầu, tít thu nhỏ thành dải dưới dấu kênh suốt clip tới màn chốt — ghi `"tit"` vào từng option của
      phuong-an.json (`hl_edl.py` tự viết `pow` 0–2,5 s + `pinTitle`); `"pin": false` để tắt. Nhánh podcast: `STAGE.title` = tít.
    - **Khung bìa = 0,3 s** (thẻ tít + mặt người nói rõ) — ghi mốc này vào dang-bai.md.
    - **Cảnh phản ứng**: nguồn có khán giả / người dẫn → piece thêm `"react": {"at": <giây nguồn ngay sau cụm đắt>, "from": <giây
      nguồn có mặt người nghe>, "len": 0.8–1.5}` — hình người nghe, tiếng người nói vẫn chạy.
    - **Danh sách đếm / hướng dẫn từng bước**: giữ đủ các ý trong danh sách để ý được trọn.

## Đầu vào

1. **Video gốc** (mp4/mov…) của người dùng — hoặc **thư mục dự án** đã dựng nó (`~/Movies/tap-<tên>/2-ban-dai`,
   dự án Codex dạng `…/work/podcast-<tên>`): tốt nhất, vì có lời đã sửa chính tả, tiếng sạch, kịch bản, tên tập. Người dùng chỉ
   đưa video-final của một dự án → tìm thư mục dự án cạnh nó (cùng cha `outputs/` ↔ `work/`, hoặc `~/Movies/*/video-final.mp4`).
   Không tải video từ YouTube/TikTok — nhờ người dùng gửi file.
2. **Phụ đề** .srt/.vtt nếu có (YouTube Studio → Phụ đề → Tải xuống): để sửa chính tả; mốc cắt vẫn lấy từ `words.srt`.
3. **Dàn ý** (Vấn đề · Giải pháp · Thực thi), đoạn đã đánh dấu "highlight" nếu có → ưu tiên.

Chỉ có phụ đề, không có video → làm bước 2–5, trả bảng cắt + mô tả + bình luận ghim để người dùng cắt bằng công cụ khác.

## Công thức — Highlight · hồ sơ `highlight`
| # | Bước | Khối |
|---|---|---|
| 0–6 | Nhận loại nguồn · dự án · bản đồ cả video · tự chọn ý theo 4 câu · chọn câu · bố trí lời kêu gọi · kiểm tự đứng được + lằn ranh · cắt + kiểm lời | [13](../khoi/13-chon-khoanh-khac/README.md) (chi tiết từng bước) · [02](../khoi/02-lam-sach/README.md) (pauses.py) · [01](../khoi/01-chep-loi/README.md) |
| 7A | Dựng nguồn có người nói (mục dưới) | [11](../khoi/11-ghep-canh/README.md) · [04](../khoi/04-khung-hinh/README.md) · [05](../khoi/05-tranh-che-nguoi/README.md) · [06](../khoi/06-mo-dau/README.md) · [07](../khoi/07-canh-minh-hoa/README.md) · [08](../khoi/08-ket-thuc/README.md) · [03](../khoi/03-phu-de/README.md) · [09](../khoi/09-am-thanh/README.md) · [17](../khoi/17-dung-kiem-tra/README.md) |
| 7B | Dựng nguồn podcast / đồ hoạ (mục dưới) | [12](../khoi/12-san-khau-podcast/README.md) · [07](../khoi/07-canh-minh-hoa/README.md) · [08](../khoi/08-ket-thuc/README.md) · [17](../khoi/17-dung-kiem-tra/README.md) |
| 8 | Phát hành: lịch đăng, khung bìa, mô tả, bình luận ghim, số liệu | [15](../khoi/15-phat-hanh/README.md) · [16](../khoi/16-so-lieu/README.md) |

### 7A. Dựng — nguồn có người nói (`video-style-edit` chế độ ghép clip, `references/multi-clip.md`)
Làm lần lượt cho từng clip `<id>` (A, B…). `cat/<id>.mp4` của bước 6 chỉ để **kiểm lời**; bản dựng đọc thẳng video gốc theo mốc trong phuong-an.json (mỗi câu thêm
`"tone": "lang"|"soi"`, câu dùng cho màn chốt thêm `"cta": true`):
```bash
zsh $BASE/scripts/new_montage.sh hl-<tên>-<id> "$P/nguon.<ext>"     # chạy nền → ~/Movies/tap-<tên>/3-highlight/clip-<id> = $E (c1 = video gốc)
python3 -I $SKILL/scripts/hl_edl.py "$P" "$E" <id>                   # → $E/motion/src/edl.js viết sẵn
cp $SKILL/assets/music/*.mp3 "$E/motion/public/sfx/"                 # nhạc cố định của kênh (soi-*, lang-*)
```
`hl_edl.py` viết: các câu `p1…pN` **cắt cứng**, khoảng lặng trong câu đã rút (đoạn con `p2b`, `p2c`…), đoạn xen kẽ phóng 1,08×;
`SUBS` (giây timeline, chữ đúng câu nguyên văn — hiện 1–3 chữ mỗi nhịp nhờ `SHORT = true`); `TS(src)` đổi giây video gốc → giây
timeline cho lớp phủ; `TONE` + `MUSIC.tracks`; `CTA` = câu kêu gọi nguyên văn; `HL = {…, bar: false}` (không thanh tập gốc).
Claude chỉnh tiếp trong edl.js:
- **Phụ đề**: sửa chính tả, tô `hl` từ khoá (từ trong `hl` hiện màu cam khi tới nhịp của nó).
- **OVERLAYS** (mốc bằng `TS(<giây trong words.srt>)`; chữ nguyên văn trừ thẻ tít): `pow` cụm đắt đúng lúc nói (cú chốt, ≤ 14 ký tự/dòng) · `action` khi câu HANHDONG
  (`quote` nguyên văn) · `chips` khi người nói đếm/liệt kê. Mật độ ~1 điểm nhấn / 5–8 s ở `soi`, thưa hơn ở `lang`.
- **Hình**: cú chốt `zoomIn` (hl_edl tự đặt khi `zoom: true`); phản ứng mạnh → `zoom` dồn nhanh; có thể `replay` khoảnh khắc đắt.
- `CTA.kind` theo việc được kêu gọi (lưu → `save`, bình luận → `comment`…).
- **Thẻ tít mở** (luật 7): `{type: 'pow', start: 0, end: 2.5, text: '<TÍT>', y: 300}` — nửa trên khung, tách khỏi phụ đề. **Thẻ cuối** (luật 11): `hl_edl.py` tự viết `ENDCARD` từ
  `"endcard"` trong phuong-an.json (thiếu → in ⚠); `ENDCARD.at` = giây trong clip gốc lấy làm ảnh nền (mặt người nói rõ, mắt mở).
  Kiểu vòng lặp → `ENDCARD = null`. Thời lượng bản cuối = clip + 1,8 s.
Rồi như multi-clip.md: `python3 -I $BASE/scripts/lift.py "$E"` → `python3 -I $BASE/scripts/overlay_guard.py "$E"` (che mặt/thân trên →
toàn màn hình; tít ghim che đầu → ẩn) → `node stills.mjs <mốc>` (chụp: thẻ tít lúc 1,5 s, mỗi pow/action
lúc đầy nhất, 2–3 mốc thấy phụ đề nhịp chữ, ngay sau 1–2 mối cắt, 2 s cuối thấy màn chốt, giữa thẻ cuối) → sửa tới sạch →
`node render-show.mjs` (nền; render các clip nối tiếp nhau, không chạy song song — tốn RAM).
Không có bước duyệt kế hoạch ghép của multi-clip (người dùng đã "ok" ở đầu).

### 7B. Dựng — nguồn podcast / toàn đồ hoạ (`podcast-style-edit`, khung dọc)
```bash
zsh $POD/scripts/new_podcast.sh "$P/cat/<id>.mp4" hl-<tên>-<id> doc cat-thua   # mỗi clip → ~/Movies/tap-<tên>/3-highlight/clip-<id> = $E (chỉ lấy tiếng)
zsh $POD/scripts/transcribe.sh "$E"
python3 -I $BASE/scripts/captions.py "$E"                         # rồi sửa chữ theo captions-goc.js của $P (đã sửa chính tả)
PY=$(zsh $POD/scripts/py_setup.sh); $PY $POD/scripts/speakers.py "$E" <1|2>; $PY $POD/scripts/envelope.py "$E"
```
- `new_podcast.sh … cat-thua` cắt lặng cuối còn 0,4 s — bình thường.
- **Tông, nhạc, thẻ cuối**: `python3 -I $SKILL/scripts/hl_apply.py "$P" <id> "$E"` → `motion/src/highlight.js` (cắt cứng: `bar: false`,
  không chip tua; phụ đề 1–3 chữ mỗi nhịp tự bật; tự trừ phần cắt đầu trong `check/trim.txt`).
- Số người nói (1|2) và `STAGE` lấy từ `scenes-goc.js`: `title` = tên tập gốc, `speakers` = tên người nói gốc, `show` như gốc.
  `theme.js`/`fonts.js` khác mặc định → chép sang. Biểu tượng vẽ thêm trong dự án gốc → chép `Icons.jsx` nếu cảnh cần.
- **Không bìa** (`COVER = null`) trừ khi người dùng muốn — video ngắn vào thẳng câu chạm.
- **Thẻ cuối** (luật 11): `"endcard": {}` trong phuong-an.json (trống = lấy `STAGE.title` + người nói của `STAGE`; điền `title`/
  `speaker` khi muốn khác) → `hl_apply.py` ghi `endcard` vào `highlight.js` → `node render.mjs` dựng `the_cuoi.mp4` (composition
  `the-cuoi`: nút phát + tên tập + người nói + sóng âm lặng dần, 1,8 s) → `render_preview.py` ghép SAU video, tiếng câm. Kiểu vòng
  lặp → bỏ khoá `endcard`. Đổi endcard → chạy lại `hl_apply.py` rồi `node render.mjs the-cuoi` + `render_preview.py`.
- `TOPICS` 2–3 mục cho cả clip (mốc = lúc bắt đầu ý), chữ trích lời, không lặp chữ của cảnh đang hiện.
- **Kịch bản cảnh** — mục dưới. Màn chốt podcast là ô câu chốt cỡ đã chốt ("đừng phóng to lại") → cú chốt cảm xúc nằm ở chữ to.
- **Tông + nhạc**: ghi `tone` cho từng câu như 7A; `hl_apply.py` chép vào `highlight.js` (`music`) → `render_preview.py` trộn
  nhạc cố định của kênh dưới tiếng nói (tự hạ khi có lời), chuyển cảnh `lang` không tiếng vút.
- `pod_stills.sh` chụp thử (mỗi cảnh lúc đầy nhất + vài mốc `nen@`) → `node render.mjs` → `podcast_base.py` → `render_preview.py`
  → `check_frames.sh` như bước 7–9 của `$POD/SKILL.md`.

### Khuôn podcast đồ hoạ dọc (7B, David duyệt 2026-11-06. Mẫu cho mọi video sau: 3 clip `~/Movies/tap-di-trainer/3-highlight/clip-{A,B,C}`, thành phẩm ở Drive `Video-xong/Di-trainer-clip-1|2|3.mp4`, lời và kịch bản ở repo David.Claude `dang-lam/video-di-trainer/`) — thắng các luật khác trong skill này khi trái nhau
- **Không ép hành động trong lời:** bỏ luật 4 và màn chốt `cta` ở nhánh này. Không ghép câu kêu gọi từ chỗ khác, nhưng clip vẫn phải đạt câu `mang_ve` bằng lời đã có. Clip kết ở câu chốt được ý, lặng 1 s (nhạc nổi lên), rồi sang màn hình cuối.
- **Màn hình cuối 3 s, không lời:** `"tease"` trong option của phuong-an.json = một câu gợi tò mò (Claude viết, David duyệt, chỉ gợi điều có thật trong video dài) + gạch nhận diện + "Bản đầy đủ trên kênh <`man_cuoi_kenh`>" + tên tập. **Không logo nền tảng nào** (David chốt 2026-11-06: video đăng Reels và TikTok, nút không bấm được mà có thể bị hạn chế phân phối). Câu hỏi "Vấn đề" / "Kết quả" để ở mô tả và bình luận ghim.
- **Nhạc:** `ho-so/highlight.json` → `nhac_chu_chinh` (thấp hơn giọng khoảng 23 dB lúc nói, nén nhẹ), chạy liền qua màn hình cuối, không tiếng ký hiệu đầu clip.
- **Hoàn cảnh:** thiếu hoàn cảnh thì đưa câu nguyên văn nêu hoàn cảnh lên đầu clip.
- **Sau khi cắt:** `new_podcast.sh … cat-thua` còn 0,4 s lặng cuối → đệm đủ 1 s lặng, cập nhật `project.duration`, chạy lại `envelope.py`.

### Kịch bản highlight podcast (7B) — tối giản ~3–4 cảnh, MỌI chữ nguyên văn lời trong clip
- **Chữ chính thay phụ đề** (David chốt 2026-11-06, `hl_apply.py` tự bật `chu_chinh`): không dải phụ đề, không dòng chủ đề, không `kinetic`; mỗi dòng `captions.js` là một câu trọn ý (≤ 3 dòng, ~55 ký tự), có `hl` từ khoá. Cảnh đồ hoạ dùng `illus` `single` `compact: true`, không `label`, để chỉ có một lớp chữ. Video ngang và video có người nói không đổi. Các mục `kinetic`, phụ đề nhịp chữ dưới đây không áp dụng cho nhánh này.
- `hook` 0 → ~2,5–3 s: **thẻ tít** (luật 7, ≤ 8 chữ, 2 dòng, viết như tít báo đúng ý), `eyebrow` trích lời hoặc bỏ trống.
- **Hình dày theo lời** (học Pháp Hoà 1,65 Tr): ngoài 3–4 cảnh chính, `montage`/`card` biểu tượng đổi theo từng cụm lời ~1,5–2,5 s ở các đoạn không có cảnh (mỗi cụm một biểu tượng vẽ + nhãn trích lời).
- `action` đúng lúc câu HANHDONG (`icon` — thiếu thì vẽ thêm: `write` = viết ra giấy; `quote` nguyên văn, `quoteAt`, `doneAt`).
- `kinetic` cú chốt cảm xúc: cụm ngắn nhất, đắt nhất, `start` = lúc bắt đầu nói cụm đó (mốc từ `words.srt` của `$E`).
  Nguồn người nói mà `face_place.sh` báo "⚠ vẫn che mặt" (mặt to + đang dồn khung) → đổi cú chốt thành `card` toàn cảnh (vd.
  `ages` cho con số: số chạy đúng lúc nói + `quote` nguyên văn; `ages` cần `pillAt` kể cả khi nhãn tự ẩn, thiếu thì lỗi "Frame NaN"),
  đặt sau phần dồn khung để người xem vẫn thấy mặt lúc dồn.
- Tối đa một `card` nếu ý chính có con số, so sánh, danh sách — không thì bỏ.
- `cta` 4 s cuối: `text` = **nguyên văn câu kêu gọi** (≤ 55 ký tự; dài hơn → chọn vế trọn ý, chỉ bỏ bớt chữ; `**cụm**` tô nhấn),
  `kind` theo việc được kêu gọi (bình luận → `comment`, lưu → `save`…). Báo cáo ghi câu này lấy ở mốc nào của video gốc.
- Kiểm thêm khi chụp thử: chữ to có đủ lớn không (dòng dài làm chữ co nhỏ → mất lực, rút cụm); `phu-de@<vài mốc>` thấy nhịp
  1–3 chữ đọc rõ, không chạm sóng âm. `phu-de@…` không có trong `composite_stills.sh` khi đứng riêng → tự ghép lên `video_goc.mp4` cùng mốc.
- Bản cuối: 1080×1920, thời lượng theo ý, âm lượng/tiếng rè bằng nguồn.

## Bảng phụ thuộc (sửa X → chạy lại Y)
| Sửa | Chạy lại |
|---|---|
| phuong-an.json (câu, mốc, tit, react, tone) | cut_highlight.py (kiểm lời) → hl_edl.py → lift.py → overlay_guard.py → stills → render |
| edl.js sửa tay (OVERLAYS, SUBS) | overlay_guard.py → stills → render-show.mjs |
| 7B: cat/<id>.mp4 | new_podcast.sh … → hl_apply.py → render.mjs → podcast_base.py → render_preview.py |
| hồ sơ highlight | hl_edl.py / cut_highlight.py chạy lại |

## Tiêu chí đạt
- Mỗi clip: đạt đủ bốn câu chọn ý (`chon_y` trong phuong-an.json), báo cáo ghi lại 4 câu + lời đọc nối + mốc đoạn ghép; có lời kêu gọi nguyên văn trừ nhánh podcast đồ hoạ dọc
- 0–2,5 s thẻ tít; sau đó chỉ 2 trạng thái; thẻ cuối "XEM BẢN ĐẦY ĐỦ" + tên tập gốc; kiểm lời khớp
- dang-bai.md: lịch đăng, mốc bìa 0,3 s, mô tả, bình luận ghim · so-lieu.md

## Điều không làm
- Không viết thêm, không đổi chữ của người nói (trừ thẻ tít, luật 7); không ghép câu tạo ra ý người nói không nói.
- Không đổi loại video (podcast không thành người nói, người nói không thành toàn đồ hoạ); không cắt thẳng hình đồ hoạ ngang vào khung dọc.
- Không giọng đọc AI thay người nói; không đưa giá, gói dịch vụ, lời bán hàng vào clip.
- Không đốt phụ đề bằng ffmpeg (`subtitles=`/`drawtext` — ffmpeg Homebrew không có libass/freetype); phụ đề luôn qua Remotion
  theo chuẩn chung `subStyle.js`; không phủ phụ đề lên video đã có phụ đề đốt sẵn.

## Cấu trúc
```
~/Movies/tap-<tên>/3-highlight/   (<tên> = đúng tên tập của bản dài)
├── nguon.<ext> · loai.txt          # video nguồn (bản không bìa nếu lấy từ dự án) · loại video gốc
├── check/goc/                      # transcript.srt · words.srt · loud05.txt · contact.jpg · captions-goc.js · scenes-goc.js · youtube.srt
├── phuong-an.json                  # các clip (A, B, C…), chon_y + câu theo thứ tự phát (Claude viết)
├── cat/<id>.mp4 · <id>.md · <id>-map.json · <id>-kiem.txt
├── ke-hoach-cat.md · dang-bai.md · so-lieu.md
~/Movies/tap-<tên>/3-highlight/clip-<id>/   → video-final.mp4 (BẢN CUỐI mỗi clip, 1080×1920)
$SKILL/assets/music/               # soi-*.mp3 · lang-*.mp3 — nhạc cố định của kênh
```

## Tài liệu kèm
- `references/changelog.md` — quyết định của người dùng theo ngày + lý do.
- `../luat-chung.md` — luật chung cả bộ (đọc trước).
- `references/hoc-tu-top-video.md` — 10 Shorts lượt xem cao đã phân tích (nhịp, cảm xúc, bố cục, mạch) — nguồn của luật 7, 11
  và thang câu mở.
- Ví dụ thật (bản chuẩn David chốt 2026-11-06): `~/Movies/tap-di-trainer/3-highlight/clip-A|B|C`, kế hoạch ở `~/Movies/tap-di-trainer/3-highlight`. Nguồn có người nói chưa có ví dụ đang giữ trên máy.

