---
name: podcast-style-edit
description: Biến một podcast (file tiếng mp3/m4a/wav, hoặc video podcast — chỉ lấy tiếng, bỏ hình) thành video đăng được ngay mà TOÀN BỘ khung hình là motion graphics, cùng phong cách với skill video-style-edit (nền tối, nhấn cam, chữ cô đặc in hoa, thẻ, chữ to, cảnh sơ đồ, biểu tượng vẽ thay ảnh). Có sân khấu nền chạy suốt video — tên tập, ý đang bàn, sóng âm theo giọng đổi màu theo người nói (tự nhận 1–2 người), thanh thời gian còn lại ở đáy — cộng mở đầu 3 giây, phụ đề đầy đủ, bước phát hành (3 tiêu đề + mốc khung bìa; thumbnail khi video ngang đăng YouTube), các cảnh hiệu ứng nối tiếp theo lời; chỉ dùng nguyên nội dung gốc. Khung xuất theo nguồn (video ngang → ngang 16:9 thiết kế toàn khung, video dọc hoặc chỉ có tiếng → dọc) trừ khi người dùng yêu cầu khác; tuỳ chọn xuất dự án CapCut. Dùng khi người dùng nói "podcast", "làm video từ file ghi âm", "video toàn animation", "không có hình gốc", "audiogram", "biến bài nói/tập podcast thành video", hoặc đưa file tiếng (hay video podcast) và muốn video có hiệu ứng thay cho hình quay — kể cả khi chỉ gửi file mà không nói rõ.
---
# Podcast thành video toàn motion graphics

Người dùng đưa **một tập podcast** (file tiếng, hoặc video mà họ không muốn dùng hình). Mục tiêu: một video **đăng được
ngay**, mọi khung hình là đồ hoạ chuyển động theo lời nói, cùng phong cách skill gốc `video-style-edit`.
Không có hình người → không còn chỗ "nghỉ mắt": **sân khấu nền** (`Stage.jsx`) chạy suốt video lấp mọi khoảng trống, các cảnh
hiệu ứng đặt lên trên nó.

Skill này **dùng chung** template Remotion và gần hết script của skill gốc — đặt `$BASE=~/.claude/skills/video-style-edit`,
`$SKILL` = thư mục chứa file này. Đọc `$BASE/references/gotchas.md` + `references/gotchas.md` (của skill này) trước khi bắt đầu.
Mọi luật nội dung của skill gốc vẫn áp dụng (xem dưới). Chạy trọn một mạch, không dừng hỏi duyệt từng bước; mọi lệnh
dài (>2 phút) chạy nền. Giữ task list theo các bước.

## Đọc trước (lần đầu trong phiên)
`../nguyen-tac.md` (7 điểm chung của hình mẫu) · `../luat-chung.md` (luật nền) · `../nhan-dien.md` (chọn loại) · hồ sơ `../ho-so/podcast.md`
(hình mẫu chính + tham số — **con số lấy ở đây, không ghi cứng**) · `../khoi/README.md` (kho khối). Skill này là **CÔNG THỨC**: thứ tự
khối + quyết định riêng của loại + tiêu chí đạt. Cách làm từng bước nằm trong README của khối; sửa cách làm → sửa khối, không sửa công thức.

## Luật (kiểm lại trước khi giao)

**Đọc `../luat-chung.md` trước** (nội dung không bịa, lằn ranh, phụ đề, hình, nhận diện, phát hành, số liệu). Luật RIÊNG podcast:

- **Chỉ nội dung gốc**: không ghép thêm lời, không giọng đọc máy, không tự đặt nhãn người nói ("Người dẫn", "Khách mời"…). Tên
  người nói chỉ khi có trong lời hoặc David đưa; tên chương trình chỉ khi David đưa.
- **Không cắt gì** (David chốt 2026-11-05, luat-chung 2): podcast để nguyên, cả khoảng lặng, ngập ngừng, nói lại, đầu/cuối. Lằn ranh chỉ cảnh báo
  ở phiếu lọc, David quyết. Highlight podcast thì cắt sạch (skill cat-highlight-video, `new_podcast.sh … cat-thua`).
- **Cỡ vừa phải** (David chốt): lớp phủ 1,08× (ngang) / 0,88× (dọc), cảnh toàn màn hình 0,88×, chữ to ≤ 120 px, ý đang bàn ≤ 118
  (ngang) / 104 (dọc), phụ đề 36 / 38 px. Đừng phóng to lại. Chữ to mới dùng `VN` (podframe.js), đừng `lineHeight: 1`.
- **Không bìa ghép trước video** (từ 2026-11-04 — giây đầu dành cho `hook`, chuẩn kênh lớn): ảnh bìa = **thumbnail** ở bước phát hành,
  chỉ khi xuất ngang VÀ đăng YouTube (luat-chung 7); video dọc chọn khung bìa khi đăng. `COVER` chỉ bật khi David yêu cầu.
- **Thanh thời gian** ở đáy vùng an toàn (đã chạy · "còn m:ss") suốt video, trên mọi cảnh.
- Màn chốt `cta` ~4 s cuối (ô câu chốt giữa sân khấu, câu Claude tự viết — luat-chung 1a). Không timeline CapCut trừ khi được yêu cầu.
- **Học NHỊP từ 50 video nổi bật nhất Hieu Nguyen** (`references/hoc-tu-hieu-nguyen-50.md`, David duyệt 2026-11-05 — chỉ học
  nhịp & cách trình bày đơn giản, GIỮ thẩm mỹ của bộ nhận diện; lời là của David, nói tự do — skill không thêm/khuôn lời):
  - **Mật độ hình (David chốt 2026-11-06, thay luật "ít mà sâu" ở dòng dưới):** podcast chỉ có tiếng, người xem YouTube cần hình để vừa nghe vừa xem. Hình phủ **khoảng 30% thời lượng** (`phu_hinh_muc_tieu`), không phải số cố định: đoạn khó hiểu hoặc quan trọng thì dày hơn, đoạn nhẹ thì thưa hơn; không để trống lâu ở đầu video; không phủ kín từ đầu đến cuối. Đoạn chạm lằn ranh không vẽ hình. Trước khi render, chụp thử tất cả cảnh mới cho David chốt.
  - ~~Ít mà sâu~~ (bỏ về mật độ, giữ cách dùng sơ đồ) **(tập > `it_ma_sau_khi_dai_hon_s` 300 s):** ~1 cảnh / `so_do_moi_s` 60–120 s (tập 8 phút ≈ 6–8 cảnh). Mỗi cảnh là một
    **sơ đồ nói thay lời** (`diagram`, khối 07) diễn tả trọn câu có cấu trúc, hoặc **ảnh thật khung bo góc** (`diagram` mode `anh`) khi
    nhắc người / nơi / tổ chức có thật. `illus` (biểu tượng + nhãn) chỉ còn cho câu ngắn không có cấu trúc. Giữa các cảnh: sân khấu + phụ đề.
  - **Bản đồ chương tích luỹ** (tự bật khi ≥ 3 TOPICS và tập > 5 phút): mỗi phần thêm một thẻ số + tên phần; 5,5 s trước màn chốt hiện cả bản đồ làm tóm tắt.
  - **Mở 0–3 s = thẻ tên tập** (`hook`: lines = tên tập trích lời) thay câu trích chữ to. **KHÔNG ghi số tập, ngày ghi âm hay thông tin
    phát hành nào lên video** (David chốt 2026-11-05) — không đặt `STAGE.episode`, không hỏi; dải đáy chỉ có thanh thời gian.
  - **Màn chốt theo luật kênh David** (khối 08, `ho-so/kenh.json`): Không / Gợi mở → `comment` "Vấn đề" / "Kết quả"; Mời → `moi` "nhắn mình một chữ 'gỡ'". (Thay `chot_mac_dinh` theo tuyến — 05/11/2026.)
  - **Mô tả**: 2–3 đoạn tóm tắt (ý của David) + chương + liên kết tập liên quan + link tài nguyên David đưa (phễu chuyển đổi kiểu "tài liệu miễn phí").
  - **Mục tiêu cuối (David)**: người xem *thấy hành động* và chuyển hoá bằng hành động → câu giao việc cụ thể nhất của tập luôn có màn `action`.
- **Học từ 20 podcast Việt** (`references/hoc-tu-20-podcast-vn.md`, David duyệt 2026-11-04):
  - **Thẻ chương**: sân khấu tự hiện "PHẦN n" 3 s đầu mỗi `TOPICS` (khi ≥ 2 TOPICS); `chapters.py` ghi chương YouTube từ TOPICS.
  - **Teaser 15–25 s** cho tập > 10 phút: sau render, `teaser.py` với 2–3 câu đắt nhất (trọn câu, nguyên văn).
  - **Thumbnail khuôn cố định**: câu hỏi/câu trích 2–3 tầng, giữ khuôn mọi tập — không số tập (David 2026-11-05).
  - **Nền "lắng"** cho tập tâm sự/thiền: `STAGE.bg = [{at: 0, src: 'nen-1.jpg'}, …]` (ảnh/tranh David đưa hoặc có giấy phép, đặt
    trong `motion/public/`) — chuyển động rất chậm, phủ tối; không có thì lưới tối mặc định.
  - **Tập > 20 phút được thưa cảnh** (~1 cảnh / 40–60 s): sân khấu + thẻ chương + TOPICS đủ (Hieu Nguyen, VOV, Fonos đổi hình rất ít).
  - Tài liệu podcast QUAY NGƯỜI cho sau này: `references/podcast-quay-nguoi.md`.

## Công thức — Podcast · hồ sơ `podcast`
| # | Bước | Khối |
|---|---|---|
| 1 | Môi trường + dự án (mục dưới) · khung xuất | [01](../khoi/01-chep-loi/README.md) · [04](../khoi/04-khung-hinh/README.md) |
| 2 | Chép lời + phụ đề | [01](../khoi/01-chep-loi/README.md) · [03](../khoi/03-phu-de/README.md) |
| 2b | Thumbnail (ngang + YouTube): mẫu podcast không mặt = nền hoạ tiết + một hình theo ý của tập + tiêu đề ngắn + "DAVID · PODCAST", không lộ các bước giải pháp | [14](../khoi/14-thumbnail/README.md) |
| 3 | Ai đang nói · sóng âm · sân khấu, TOPICS, PHẦN n, nền lắng | [12](../khoi/12-san-khau-podcast/README.md) |
| 4 | Phong cách · **tuyến nội dung → nhạc nền** (`project.tuyen`, bắt buộc) | [10](../khoi/10-nhan-dien/README.md) · [09](../khoi/09-am-thanh/README.md) |
| 5–6 | Cảnh minh hoạ 2 trạng thái · màn chốt | [07](../khoi/07-canh-minh-hoa/README.md) · [08](../khoi/08-ket-thuc/README.md) |
| 7–9 | Chụp thử → render → kiểm (mục dưới) | [17](../khoi/17-dung-kiem-tra/README.md) · [09](../khoi/09-am-thanh/README.md) |
| 10 | Phát hành: teaser > 10 phút, chương, màn kết, số liệu | [15](../khoi/15-phat-hanh/README.md) · [16](../khoi/16-so-lieu/README.md) |

### 1. Môi trường + dự án
```bash
zsh $BASE/scripts/check_env.sh
zsh $SKILL/scripts/new_podcast.sh "<file tiếng hoặc video>" <tên-ngắn> [doc|ngang]   # → ~/Movies/tap-<tên>/2-ban-dai (gốc vào tap-<tên>/1-goc), dòng cuối = $P
```
Lấy tiếng (bỏ hình), giữ nguyên toàn bộ (`cat-thua` ở tham số 4 mới cắt lặng đầu/cuối, chỉ dùng cho clip highlight; ghi `check/trim.txt`), `davinci/media/audio.wav` + `audio.m4a`,
chép template của skill gốc, `project.js` có `podcast: true`, khung theo nguồn (hoặc tham số 3 `doc`|`ngang`).

### 2. Lời nói + phụ đề
```bash
zsh $SKILL/scripts/transcribe.sh "$P"                    # chạy nền; ~1 phút / 5 phút tiếng
python3 -I $BASE/scripts/captions.py "$P"               # → motion/src/captions.js (nháp)
```
Sửa TỪNG dòng như skill gốc (khối 03 `../khoi/03-phu-de/README.md`): chính tả, câu bịa ("Hãy subscribe…" — đối chiếu `transcript.srt`
với `words.srt`, hai lần chạy khác nhau), chỗ ngắt dòng. **Riêng podcast**: ở mỗi chỗ đổi người nói, mốc từ của Whisper hay
trôi sớm/muộn 1–2 s → một dòng phụ đề có thể bắt đầu trong lượt của người kia. Đối chiếu với `speakers.js` (bước 3) và dời mốc.

### 4. Phong cách
Không có mẫu → phong cách mặc định của template (đã duyệt). Có video/ảnh mẫu → làm theo khối 10 (`../khoi/10-nhan-dien/README.md`).

### 6. Minh hoạ
Theo khối 07 (`../khoi/07-canh-minh-hoa/README.md`): **mặc định biểu tượng vẽ** (`icon` trong `montage`/`card job`, xem `$BASE/references/scene-design.md`),
ảnh chỉ khi hình vẽ không thay được cái thật — địa danh, nhân vật có thật, tư liệu quá khứ, minh chứng xác thực, sản phẩm cụ
thể — và tìm được ảnh tốt (`$BASE/scripts/openverse.py`). Số liệu luôn bằng hiệu ứng, đúng con số người nói. Podcast càng nên toàn
hiệu ứng — cả khung là đồ hoạ, ảnh dễ lạc tông. Người dùng nói "không dùng ảnh" / "thêm ảnh" thì theo đó.

### 7. Chụp thử (trước khi render)
```bash
zsh $SKILL/scripts/pod_stills.sh "$P" nen@<giây> <id>@<giây> ...     # sân khấu + cảnh + phụ đề cùng mốc → check/stills.jpg
```
Chụp mỗi cảnh ở khoảnh khắc đầy nhất + vài mốc chỉ có sân khấu (`nen@…`) ở các TOPICS và lúc đổi người nói. Kiểm: chữ tràn, dấu
bị cắt, hai dòng chữ chồng nhau hoặc chữ chạm khung ảnh/biểu tượng (chữ to sau dòng khác phải chừa `aboveGap`), màu sóng âm đúng người đang nói, ý đang bàn khớp lời, lớp phủ không chạm sóng âm/vòng micro (ngang), thanh thời gian và
phụ đề không bị che, không gì lọt vùng đỏ. Sửa tới khi sạch.

### 8. Render + xuất
```bash
cd "$P/motion" && node render.mjs                          # chạy nền: cảnh + phụ đề + sân khấu (~1,5× thời lượng)
python3 $SKILL/scripts/podcast_base.py "$P"                # sân khấu + tiếng → davinci/media/video_goc.mp4
python3 -I $BASE/scripts/credits_card.py "$P"              # chỉ khi có ảnh → nguon-anh.txt
python3 -I $BASE/scripts/render_preview.py "$P"            # chạy nền → video-final.mp4
```
Podcast 15 phút: sân khấu ~25 phút, phụ đề ~10 phút, ghép cuối ~10 phút — báo người dùng thời gian chờ.

### 9. Kiểm tra bản cuối
`zsh $BASE/scripts/check_frames.sh "$P" "$P/video-final.mp4" <mốc giữa & cuối mỗi cảnh, vài mốc chỉ sân khấu>` → xem `check/sheet.jpg`.
So âm lượng và tiếng rè với `davinci/media/audio.wav` (volumedetect chênh ≤ 0,5 dB; `highpass=f=12000,astats` chênh ≤ 1 dB),
thời lượng = `audio.wav` (+ thẻ cuối nếu có). Khung 0 của video-final là `hook`.

### 10. Phát hành + giao
Phát hành theo `../luat-chung.md` mục 7: `phat-hanh/phat-hanh.md` (3 tiêu đề, mô tả, mốc khung bìa); xuất ngang VÀ đăng YouTube → 2 thumbnail
`THUMB_HINH=<hình> THUMB_TAG=PODCAST zsh $BASE/scripts/thumbnail.sh "$P" - "<DÒNG 1>" "<DÒNG 2>" 1|2` (khối 14) (chữ từ bước 2b). Chép `dung-video/khoi/16-so-lieu/mau-so-lieu.md` → `$P/so-lieu.md`.
Gửi `video-final.mp4` (+ thumbnail nếu có) (SendUserFile). Báo cáo tiếng Việt: đã cắt gì (`check/trim.txt`), người nói (tên/vai, tỉ lệ, chỗ không
chắc), danh sách cảnh + TOPICS theo mốc, nội dung `nguon-anh.txt` nếu có ảnh, đã kiểm tra gì / chưa kiểm tra gì, tên riêng cần
xác nhận chính tả.

## Bảng phụ thuộc (sửa X → chạy lại Y)
| Sửa | Chạy lại |
|---|---|
| captions.js | `node render.mjs phu-de` → render_preview.py |
| STAGE / TOPICS / speakers / envelope | `node render.mjs nen` → podcast_base.py → render_preview.py |
| một cảnh (scenes.js) | `node render.mjs <id>` → render_preview.py |
| thêm / bớt / dời cảnh (scenes.js): sân khấu tự ẩn chữ chủ đề theo danh sách cảnh | `node render.mjs <các id> nen` → podcast_base.py → render_preview.py. Bỏ `nen` sẽ lộ chữ sau thẻ; ảnh chụp thử KHÔNG thấy lỗi này, phải soi bản cuối (2026-11-06) |
| video-final (teaser) | chapters.py |

## Sửa theo góp ý
- Một cảnh → sửa `scenes.js` → `node render.mjs <id>` → `render_preview.py`.
- TOPICS / STAGE / người nói / sóng âm (thứ vẽ trên sân khấu) → `node render.mjs nen` → `podcast_base.py` → `render_preview.py`.
- Phụ đề / thanh thời gian → `node render.mjs phu-de` → `render_preview.py`.
- Thumbnail → chạy lại `thumbnail.sh` với chữ/ảnh mới (không cần render video).
- **CapCut** (khi được yêu cầu): giống skill gốc — `PY=$(zsh $BASE/scripts/capcut_setup.sh); $PY $BASE/scripts/build_capcut.py "$P"`.
  Track chính là sân khấu + tiếng (video_goc.mp4), track "Hieu ung" là từng cảnh, phụ đề là chữ CapCut cùng font.

## Cấu trúc dự án
```
~/Movies/tap-<tên>/2-ban-dai/
├── davinci/media/   nguon.* (file gốc) · audio.wav/.m4a (đã cắt đầu/cuối) · nen.mp4 (sân khấu) · video_goc.mp4 (sân khấu + tiếng)
│                    <id>.mov (cảnh, nền trong suốt) · phu_de.mov (phụ đề + thanh thời gian)
├── motion/src/      scenes.js (STAGE, TOPICS, SCENES) · captions.js · speakers.js · envelope.js · podframe.js · theme.js
├── check/           trim.txt · goc/ (transcript, words) · speakers.md · stills.jpg · sheet.jpg
├── phat-hanh/  phat-hanh.md · thumb-1.jpg · thumb-2.jpg
├── images/ · ke-hoach-canh.md · nguon-anh.txt · so-lieu.md
└── video-final.mp4
```

## Tài liệu kèm
- `../luat-chung.md` — luật chung cả bộ (đọc trước); `dung-video/khoi/16-so-lieu/mau-so-lieu.md` — mẫu số liệu sau đăng.
- `references/podcast-design.md` — giải phẫu sân khấu, chọn cảnh cho lời hội thoại, mật độ, vùng giữa.
- `references/changelog.md` — sổ quyết định của người dùng theo ngày + lý do.
- `references/gotchas.md` — lỗi riêng của podcast (mốc Whisper ở chỗ đổi người, nhận giọng, thời gian render).
- `$BASE/references/scene-design.md` — mọi loại cảnh có sẵn + props (dùng chung).

