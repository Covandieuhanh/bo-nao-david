---
name: podcast-style-edit
description: Biến một podcast (file tiếng mp3/m4a/wav, hoặc video podcast — chỉ lấy tiếng, bỏ hình) thành video đăng được ngay mà TOÀN BỘ khung hình là motion graphics, cùng phong cách video-style-edit. Sân khấu nền chạy suốt video (ý đang bàn, sóng âm đổi màu theo người nói 1–2 người, thanh thời gian còn lại), phụ đề đầy đủ, cảnh minh hoạ nối tiếp theo lời, màn chốt nguyên văn; chỉ dùng nội dung gốc, giữ trọn không cắt. Khung xuất theo nguồn (ngang → 16:9, dọc hoặc chỉ tiếng → dọc) trừ khi được yêu cầu khác; kết bằng phát hành (tiêu đề, chương, teaser, thumbnail không mặt khi ngang). Dùng khi người dùng nói "podcast", "làm video từ file ghi âm", "video toàn animation", "không có hình gốc", "audiogram", "biến bài nói/tập podcast thành video", hoặc đưa file tiếng (hay video podcast) muốn có hiệu ứng thay hình quay — kể cả khi chỉ gửi file mà không nói rõ.
---
# Podcast thành video toàn motion graphics

**Đọc trước:** `../../thoi-quen-lam-viec.md` · `../luat-chung.md` · hồ sơ `../ho-so/podcast.md` — **con số lấy ở hồ sơ, không ghi cứng**.
`$BASE/references/gotchas.md` + `references/gotchas.md` đọc một lần ở đầu phiên. File khác chỉ đọc ở đúng bước cần (cột "Khối").
Skill này là **CÔNG THỨC**: thứ tự khối + quyết định riêng của loại + tiêu chí đạt. Sửa cách làm → sửa khối, không sửa công thức.

David đưa **một tập podcast** (file tiếng, hoặc video không muốn dùng hình). Mục tiêu: video **đăng được ngay**, mọi khung hình
là đồ hoạ chuyển động theo lời. Không có hình người → **sân khấu nền** (`Stage.jsx`) chạy suốt video lấp khoảng trống, các cảnh đặt lên trên.

Dùng chung template Remotion và gần hết script của skill gốc — `$BASE=~/.claude/skills/video-style-edit`, `$SKILL` = thư mục này.
Luật nội dung của skill gốc vẫn áp dụng. Lệnh > 2 phút chạy nền. Giữ task list theo các bước.

**Hỏi một lần + cổng chụp thử** (`hoi-chuyen-gia`): sau khi chép lời, hỏi một lần gộp mọi điểm cần chọn — chữ
thumbnail, tên các phần (TOPICS), nền lắng hay lưới tối — mỗi điểm 2–3 gợi ý. Trước khi render, chụp thử mọi cảnh mới cho David chốt.
Sau đó chạy một mạch tới bản cuối; giữa chừng chỉ dừng khi gặp một trong 6 tín hiệu.

## Luật riêng (kiểm lại trước khi giao)

Luật chung video ở `../luat-chung.md` (chữ nguyên văn, không cắt video dài, hình, nhận diện, phát hành, số liệu). Luật RIÊNG podcast:

- **Chỉ nội dung gốc**: không ghép thêm lời, không giọng đọc máy, không tự đặt nhãn người nói ("Người dẫn", "Khách mời"…). Tên
  người nói chỉ khi có trong lời hoặc David đưa; tên chương trình chỉ khi David đưa.
- **Không cắt gì** (luat-chung mục 2): giữ cả khoảng lặng, ngập ngừng, nói lại, đầu/cuối. Lằn ranh chỉ cảnh báo ở phiếu lọc, David
  quyết. Highlight podcast thì cắt sạch (skill cat-highlight-video, `new_podcast.sh … cat-thua`).
- **Cỡ vừa phải** (đừng phóng to lại): lớp phủ 1,08× (ngang) / 0,88× (dọc), cảnh toàn màn hình 0,88×, chữ to ≤ 120 px,
  ý đang bàn ≤ 118 (ngang) / 104 (dọc). **Phụ đề:** ngang 36 px; dọc cụm 5–8 chữ cỡ 58 (luat-chung mục 3). Chữ to dùng `VN` (podframe.js), đừng `lineHeight: 1`.
- **Không thẻ tít mở đầu, không bìa ghép trước video**: thẻ tít chỉ khi David yêu cầu, chữ nguyên văn. Ảnh bìa = **thumbnail** ở bước
  phát hành, chỉ khi xuất ngang VÀ đăng YouTube; video dọc chọn khung bìa khi đăng. `COVER` chỉ bật khi David yêu cầu.
- **Không ghi số tập, ngày ghi âm hay thông tin phát hành nào lên video** — không đặt `STAGE.episode`, không hỏi; dải đáy chỉ có thanh thời gian.
- **Thanh thời gian** ở đáy vùng an toàn (đã chạy · "còn m:ss") suốt video, trên mọi cảnh — trừ podcast dọc trích ngắn: không thanh, không thẻ cuối (`thu-vien-hinh/nhan-dien-chung.md` mục 1).
- **Màn chốt** `cta` cuối video: ô câu chốt giữa sân khấu = **nguyên văn câu David nói cuối tập** (luat-chung 1). "Vấn đề / Kết quả"
  chỉ ở bài đăng; "gỡ" chỉ lên video khi David nói trong tập.
- Không làm bản cho app chỉnh sửa (CapCut/DaVinci); dọn file tạm sau khi David chốt (`don_tap.py`, khối 17).
- **Học nhịp từ 50 video Hieu Nguyen** (`references/hoc-tu-hieu-nguyen-50.md` — học nhịp & cách trình bày; lời là của David, không
  thêm/khuôn lời):
  - **Mật độ hình:** hình phủ **khoảng 30% thời lượng** (`phu_hinh_muc_tieu`), không cố định: đoạn khó hiểu hoặc quan trọng dày
    hơn, đoạn nhẹ thưa hơn; không để trống lâu ở đầu; không phủ kín. Đoạn chạm lằn ranh không vẽ hình.
  - **Loại cảnh:** ưu tiên **sơ đồ nói thay lời** (`diagram`, khối 07) cho câu có cấu trúc, hoặc **ảnh thật khung bo góc** (`diagram` mode
    `anh`) khi nhắc người / nơi / tổ chức có thật. `illus` cho câu ngắn không có cấu trúc. Giữa các cảnh: sân khấu + phụ đề.
  - **Bản đồ chương tích luỹ** (tự bật khi ≥ 3 TOPICS và tập dài): mỗi phần thêm thẻ số + tên phần; trước màn chốt hiện cả bản đồ làm tóm tắt.
  - **Mô tả**: 2–3 đoạn tóm tắt (ý của David) + chương + liên kết tập liên quan + link tài nguyên David đưa.
  - **Mục tiêu cuối**: người xem *thấy hành động* → câu giao việc cụ thể nhất của tập có màn `action`.
- **Học từ 20 podcast Việt** (`references/hoc-tu-20-podcast-vn.md`):
  - **Thẻ chương**: sân khấu tự hiện "PHẦN n" đầu mỗi `TOPICS` (khi ≥ 2 TOPICS); `chapters.py` ghi chương YouTube từ TOPICS.
  - **Teaser** cho tập > 10 phút: sau render, `teaser.py` với 2–3 câu đắt nhất (trọn câu, nguyên văn); độ dài theo hồ sơ.
  - **Thumbnail khuôn cố định** mọi tập, không số tập, không mặt — mẫu ở khối 14.
  - **Nền "lắng"** cho tập tâm sự/thiền: `STAGE.bg = [{at: 0, src: 'nen-1.jpg'}, …]` (ảnh/tranh David đưa hoặc có giấy phép, trong
    `motion/public/`) — chuyển động rất chậm, phủ tối; không có thì lưới tối mặc định.
  - Tập rất dài được thưa cảnh hơn trong mức 30%: sân khấu + thẻ chương + TOPICS đủ.
  - Tài liệu podcast QUAY NGƯỜI cho sau này: `references/podcast-quay-nguoi.md`.

## Công thức — Podcast · hồ sơ `podcast`
| # | Bước | Khối |
|---|---|---|
| 1 | Môi trường + dự án (mục dưới) · khung xuất *(bước nhẹ)* | [01](../khoi/01-chep-loi/README.md) · [04](../khoi/04-khung-hinh/README.md) |
| 2 | Chép lời + phụ đề *(chép lời là bước nhẹ)* → **hỏi một lần** | [01](../khoi/01-chep-loi/README.md) · [03](../khoi/03-phu-de/README.md) |
| 2b | Thumbnail (ngang + YouTube): mẫu không mặt = nền hoạ tiết + một hình theo ý của tập + tiêu đề ngắn + "DAVID · PODCAST", không lộ các bước giải pháp | [14](../khoi/14-thumbnail/README.md) |
| 3 | Ai đang nói · sóng âm · sân khấu, TOPICS, PHẦN n, nền lắng | [12](../khoi/12-san-khau-podcast/README.md) |
| 4 | Phong cách · **tuyến nội dung → nhạc nền** (`project.tuyen`, bắt buộc) | [10](../khoi/10-nhan-dien/README.md) · [09](../khoi/09-am-thanh/README.md) |
| 5–6 | Cảnh minh hoạ (bố cục tự cân) · màn chốt nguyên văn | [07](../khoi/07-canh-minh-hoa/README.md) · [08](../khoi/08-ket-thuc/README.md) |
| 7–9 | Chụp thử → **David chốt** → render → kiểm (mục dưới) | [17](../khoi/17-dung-kiem-tra/README.md) · [09](../khoi/09-am-thanh/README.md) |
| 10 | Phát hành: teaser > 10 phút, chương, màn kết, số liệu | [15](../khoi/15-phat-hanh/README.md) · [16](../khoi/16-so-lieu/README.md) |

Bước đánh dấu *(bước nhẹ)*: nhắc đổi mô hình rẻ hơn theo `thoi-quen-lam-viec.md` mục 3.

### 1. Môi trường + dự án
```bash
zsh $BASE/scripts/check_env.sh
zsh $SKILL/scripts/new_podcast.sh "<file tiếng hoặc video>" <tên-ngắn> [doc|ngang]   # → ~/Movies/tap-<tên>/2-ban-dai (gốc vào tap-<tên>/1-goc), dòng cuối = $P
```
Lấy tiếng (bỏ hình), giữ nguyên toàn bộ (`cat-thua` ở tham số 4 mới cắt lặng đầu/cuối, chỉ cho clip highlight; ghi `check/trim.txt`),
`davinci/media/audio.wav` + `audio.m4a`, chép template skill gốc, `project.js` có `podcast: true`, khung theo nguồn (hoặc tham số 3).

### 2. Lời nói + phụ đề
```bash
zsh $SKILL/scripts/transcribe.sh "$P"                    # chạy nền; ~1 phút / 5 phút tiếng
python3 -I $BASE/scripts/captions.py "$P"               # → motion/src/captions.js (nháp)
```
Sửa TỪNG dòng theo khối 03: chính tả, câu bịa ("Hãy subscribe…" — đối chiếu `transcript.srt` với `words.srt`), chỗ ngắt dòng.
**Riêng podcast**: ở chỗ đổi người nói, mốc từ Whisper hay trôi 1–2 s → dòng phụ đề có thể bắt đầu trong lượt người kia. Đối chiếu
`speakers.js` (bước 3) và dời mốc.

### 4. Phong cách
Không có mẫu → phong cách mặc định của template. Có video/ảnh mẫu → khối 10.

### 6. Minh hoạ
Theo khối 07: **mặc định biểu tượng vẽ** hoặc sơ đồ (`icon` trong `montage`/`card job`, xem `$BASE/references/scene-design.md`); ảnh chỉ khi hình
vẽ không thay được cái thật (địa danh, nhân vật có thật, tư liệu, minh chứng, sản phẩm cụ thể) và tìm được ảnh tốt
(`$BASE/scripts/openverse.py`). Số liệu bằng hiệu ứng, đúng con số người nói. David nói "không dùng ảnh" / "thêm ảnh" thì theo đó.

### 7. Chụp thử (trước khi render — gửi David chốt)
```bash
zsh $SKILL/scripts/pod_stills.sh "$P" nen@<giây> <id>@<giây> ...     # sân khấu + cảnh + phụ đề cùng mốc → check/stills.jpg
```
Chụp mỗi cảnh ở khoảnh khắc đầy nhất + vài mốc chỉ có sân khấu (`nen@…`) ở các TOPICS và lúc đổi người nói. Kiểm: chữ tràn, dấu bị
cắt, hai dòng chữ chồng nhau hoặc chạm khung ảnh/biểu tượng (chữ to sau dòng khác chừa `aboveGap`), màu sóng âm đúng người nói, ý
đang bàn khớp lời, lớp phủ không chạm sóng âm/vòng micro (ngang), thanh thời gian và phụ đề không bị che, không gì lọt vùng đỏ.
Sửa tới khi sạch rồi gửi David chốt.

### 8. Render + xuất
```bash
cd "$P/motion" && node render.mjs                          # chạy nền: cảnh + phụ đề + sân khấu (~1,5× thời lượng)
python3 $SKILL/scripts/podcast_base.py "$P"                # sân khấu + tiếng → davinci/media/video_goc.mp4
python3 -I $BASE/scripts/credits_card.py "$P"              # chỉ khi có ảnh → nguon-anh.txt
python3 -I $BASE/scripts/render_preview.py "$P"            # chạy nền → video-final.mp4
```
Podcast 15 phút: sân khấu ~25 phút, phụ đề ~10 phút, ghép cuối ~10 phút — báo trước thời gian chờ.

### 9. Kiểm tra bản cuối
`zsh $BASE/scripts/check_frames.sh "$P" "$P/video-final.mp4" <mốc giữa & cuối mỗi cảnh, vài mốc chỉ sân khấu>` → xem `check/sheet.jpg`.
Âm thanh theo khối 09 (cả bài −14 LUFS ±0,5 (hồ sơ `nhac.do_to_cuoi_LUFS`), đỉnh ≤ −1,5 dB, tiếng rè (highpass 12 kHz) **so với giọng** tăng ≤ 1 dB; không so dB thô với `audio.wav` vì giọng nhỏ được kéo lên),
thời lượng = `audio.wav` (+ thẻ cuối nếu có).

### 10. Phát hành + giao
Phát hành theo `../luat-chung.md` mục 7: `phat-hanh/phat-hanh.md` (3 tiêu đề, mô tả, mốc khung bìa); xuất ngang VÀ đăng YouTube → 2 thumbnail
`THUMB_HINH=<hình> THUMB_TAG=PODCAST zsh $BASE/scripts/thumbnail.sh "$P" - "<DÒNG 1>" "<DÒNG 2>" 1|2` (khối 14, chữ đã chốt ở lần hỏi đầu).
Chép `dung-video/khoi/16-so-lieu/mau-so-lieu.md` → `$P/so-lieu.md`.
Gửi `video-final.mp4` (+ thumbnail nếu có) (SendUserFile). Báo cáo tiếng Việt: người nói (tên/vai, tỉ lệ, chỗ không chắc), danh sách
cảnh + TOPICS theo mốc, `nguon-anh.txt` nếu có ảnh, đã kiểm gì / chưa kiểm gì, tên riêng cần xác nhận chính tả.

## Bảng phụ thuộc (sửa X → chạy lại Y)
| Sửa | Chạy lại |
|---|---|
| captions.js | `node render.mjs phu-de` → render_preview.py |
| STAGE / TOPICS / speakers / envelope | `node render.mjs nen` → podcast_base.py → render_preview.py |
| một cảnh (scenes.js) | `node render.mjs <id>` → render_preview.py |
| thêm / bớt / dời cảnh (scenes.js): sân khấu tự ẩn chữ chủ đề theo danh sách cảnh | `node render.mjs <các id> nen` → podcast_base.py → render_preview.py. Bỏ `nen` sẽ lộ chữ sau thẻ; ảnh chụp thử KHÔNG thấy lỗi này, phải soi bản cuối |
| video-final (teaser) | chapters.py |

## Sửa theo góp ý
- Một cảnh → sửa `scenes.js` → `node render.mjs <id>` → `render_preview.py`.
- TOPICS / STAGE / người nói / sóng âm → `node render.mjs nen` → `podcast_base.py` → `render_preview.py`.
- Phụ đề / thanh thời gian → `node render.mjs phu-de` → `render_preview.py`.
- Thumbnail → chạy lại `thumbnail.sh` với chữ/ảnh mới (không cần render video).
- Ghi góp ý đúng một chỗ: khối/skill bị ảnh hưởng + một dòng `references/changelog.md`.

## Cấu trúc dự án
```
~/Movies/tap-<tên>/2-ban-dai/
├── davinci/media/   nguon.* (file gốc) · audio.wav/.m4a (tiếng giữ nguyên) · nen.mp4 (sân khấu) · video_goc.mp4 (sân khấu + tiếng)
│                    <id>.mov (cảnh, nền trong suốt) · phu_de.mov (phụ đề + thanh thời gian)
├── motion/src/      scenes.js (STAGE, TOPICS, SCENES) · captions.js · speakers.js · envelope.js · podframe.js · theme.js
├── check/           trim.txt (chỉ khi cat-thua) · goc/ (transcript, words) · speakers.md · stills.jpg · sheet.jpg
├── phat-hanh/  phat-hanh.md · thumb-1.jpg · thumb-2.jpg
├── images/ · ke-hoach-canh.md · nguon-anh.txt · so-lieu.md
└── video-final.mp4
```

## Xong khi
1. Đã hỏi một lần ở đầu; có chụp thử cho David chốt trước khi render.
2. Chỉ nội dung gốc, giữ trọn tập; chữ trên video nguyên văn; không thẻ tít, số tập, ngày tháng.
3. Sân khấu, sóng âm, thanh thời gian chạy suốt video; màu sóng âm đúng người nói.
4. Hình phủ khoảng 30% thời lượng, dày ở đoạn khó, không trống lâu ở đầu.
5. Phụ đề đúng chữ, đủ dấu, khớp lượt người nói; không gì lọt vùng đỏ.
6. Âm lượng và thời lượng khớp bản tiếng gốc.
7. Đủ gói phát hành (tiêu đề, chương, teaser nếu > 10 phút, thumbnail không mặt nếu ngang, mẫu số liệu).

## Tài liệu kèm (chỉ đọc khi bước cần, cân nhắc đổi luật hoặc gỡ lỗi)
- `references/podcast-design.md` — giải phẫu sân khấu, chọn cảnh cho lời hội thoại, vùng giữa.
- `references/changelog.md` — sổ quyết định theo ngày + lý do.
- `references/gotchas.md` — lỗi riêng podcast (mốc Whisper ở chỗ đổi người, nhận giọng, thời gian render).
- `$BASE/references/scene-design.md` — mọi loại cảnh có sẵn + props (dùng chung).
- `dung-video/khoi/16-so-lieu/mau-so-lieu.md` — mẫu số liệu sau đăng.

## Nhật ký
- 2026-11-08 · chuẩn hoá (`dang-lam/chuan-hoa-skill.md` bước 3): hỏi một lần đầu + giữ cổng chụp thử trước render (06/11) thay "chạy một mạch không hỏi"; bỏ thẻ tên tập mở đầu (N2); màn chốt nguyên văn (N4); bỏ con số nhịp 60–120 s, 40–60 s (N6), giữ cỡ chữ đã chốt; phụ đề dọc cụm 5–8 chữ cỡ 58 (08/11); "bố cục tự cân" thay "2 trạng thái" (C3); sửa chữ "đã cắt"; đọc trước 3 file; bước nhẹ 1·2; rút mô tả; thêm "Xong khi". Chi tiết các quyết định trước: `references/changelog.md`.
