---
name: dung-podcast
description: Biến một podcast (file âm thanh mp3/m4a/wav, hoặc video podcast — skill chỉ lấy phần âm thanh, bỏ phần hình) thành video đăng được ngay, trong đó TOÀN BỘ khung hình là motion graphics, cùng phong cách dung-video-theo-phong-cach. Sân khấu nền chạy suốt video (ý đang bàn, sóng âm đổi màu theo người nói, 1–2 người, thanh thời gian còn lại), phụ đề đầy đủ, cảnh minh hoạ nối tiếp theo lời nói, màn chốt nguyên văn; skill chỉ dùng nội dung gốc, giữ trọn, không cắt. Khung xuất theo nguồn (nguồn ngang thì xuất 16:9; nguồn dọc hoặc chỉ có âm thanh thì xuất dọc) trừ khi người dùng yêu cầu khác; skill kết thúc bằng bước phát hành (tiêu đề, chương, teaser, thumbnail không có khuôn mặt khi xuất ngang). Dùng khi người dùng nói "podcast", "làm video từ file ghi âm", "video toàn animation", "không có hình gốc", "audiogram", "biến bài nói/tập podcast thành video", hoặc đưa file âm thanh (hay video podcast) và muốn có hiệu ứng thay cho hình quay — kể cả khi chỉ gửi file mà không nói rõ.
---
# Podcast thành video toàn motion graphics

**Đọc trước:** `../quy-tac-chung.md` (mục 8) · hồ sơ `../ho-so-thuong-hieu/podcast.md`. Lỗi thường gặp: đọc phần của `$BASE` và phần của skill này.

David đưa **một tập podcast** (file âm thanh, hoặc video mà David không muốn dùng hình). Mục tiêu: video **đăng được ngay**, mọi khung hình
là đồ hoạ chuyển động theo lời nói. Vì không có hình người, skill dùng **sân khấu nền** (`san-khau.jsx`) chạy suốt video để lấp khoảng trống, các cảnh đặt lên trên.

Skill này dùng chung template Remotion và phần lớn script của skill gốc — `$BASE=~/.claude/skills/dung-video-theo-phong-cach`, `$SKILL` = thư mục này.
Luật nội dung của skill gốc vẫn áp dụng. Lệnh chạy quá 2 phút thì chạy nền. Claude giữ task list theo các bước.

**Không hỏi** (`../../chuan-muc-lam-viec.md` mục 2): chữ thumbnail, tên các phần (TOPICS), nền lắng hay lưới tối do Claude tự chọn
theo khối. Claude chạy liên tục tới bản cuối, không trình 4 phần (đã có quy trình): chụp thử mọi cảnh mới để Claude
tự rà soát (khối 17) rồi render, không chờ David chốt. Luật về dừng giữa chừng và báo cáo cuối có "đã chọn X vì Y": `../quy-tac-chung.md` mục 8.


## Luật riêng (kiểm lại trước khi bàn giao)

Luật chung về video ở `../quy-tac-chung.md` (chữ nguyên văn, không cắt video dài, hình, nhận diện, phát hành, số liệu). Luật RIÊNG của podcast:

- **Chỉ nội dung gốc**: Claude không ghép thêm lời, không dùng giọng đọc máy, không tự đặt nhãn người nói ("Người dẫn", "Khách mời"…). Tên
  người nói chỉ ghi khi có trong lời nói hoặc do David cung cấp; tên chương trình chỉ ghi khi David cung cấp.
- **Không cắt gì** (quy-tac-chung mục 2): giữ cả khoảng lặng, ngập ngừng, câu nói lại, phần đầu và phần cuối. Nội dung chạm lằn ranh chỉ được cảnh báo ở phiếu lọc, David
  quyết định. Riêng highlight podcast thì cắt sạch (skill cat-doan-noi-bat, `tao-podcast.sh … cat-thua`).
- **Kích thước vừa phải** (không phóng to lại): lớp phủ 1,08× (ngang) / 0,88× (dọc), cảnh toàn màn hình 0,88×, chữ lớn tối đa 120 px,
  ý đang bàn tối đa 118 (ngang) / 104 (dọc). **Phụ đề:** ngang 36 px; dọc cụm 5–8 chữ cỡ 58 (quy-tac-chung mục 3). Chữ lớn dùng `VN` (khung-podcast.js), không dùng `lineHeight: 1`.
- **Không thẻ tiêu đề mở đầu, không bìa ghép trước video**: thẻ tiêu đề chỉ dùng khi David yêu cầu, chữ nguyên văn. Ảnh bìa là **thumbnail** ở bước
  phát hành, chỉ khi xuất ngang VÀ đăng YouTube; video dọc chọn khung bìa khi đăng. `COVER` chỉ bật khi David yêu cầu.
- **Không ghi số tập, ngày ghi âm hay bất kỳ thông tin phát hành nào lên video** — Claude không đặt `STAGE.episode`, không hỏi; dải đáy chỉ có thanh thời gian.
- **Thanh thời gian** nằm ở đáy vùng an toàn (thời gian đã chạy · "còn m:ss") suốt video, trên mọi cảnh — trừ podcast dọc trích ngắn: không có thanh thời gian, không có thẻ cuối (`thu-vien-tai-nguyen/nhan-dien-chung.md` mục 1).
- **Màn chốt** `cta` cuối video: ô câu chốt giữa sân khấu là **nguyên văn câu David nói cuối tập** (quy-tac-chung 1). "Vấn đề / Kết quả"
  chỉ dùng ở bài đăng; "gỡ" chỉ đưa lên video khi David nói trong tập.
- Claude không làm bản cho app chỉnh sửa (CapCut/DaVinci); sau khi David chốt: bản cuối vào `~/Movies/cho-dang/<tập>/` + `cho-dang.sh gui <tập>`, dọn file tạm rồi đưa dự án lên Drive (`don-tap.py` rồi `luu-drive.sh`, khối 17).
- **Học nhịp từ 50 video Hieu Nguyen** (`references/hoc-tu-hieu-nguyen-50.md` — học nhịp và cách trình bày; lời là của David, không
  thêm lời, không dùng lời mẫu):
  - **Mật độ hình:** hình phủ **khoảng 30% thời lượng** (`phu_hinh_muc_tieu`), không cố định: đoạn khó hiểu hoặc quan trọng thì dày
    hơn, đoạn nhẹ thì thưa hơn; không để trống lâu ở phần đầu; không phủ kín. Đoạn chạm lằn ranh không vẽ hình.
  - **Loại cảnh:** ưu tiên **sơ đồ nói thay lời** (`diagram`, khối 07) cho câu có cấu trúc, hoặc **ảnh thật trong khung bo góc** (`diagram` mode
    `anh`) khi lời nói nhắc tới người / nơi / tổ chức có thật. `illus` cho câu ngắn không có cấu trúc. Giữa các cảnh: sân khấu + phụ đề.
  - **Bản đồ chương tích luỹ** (tự bật khi có ít nhất 3 TOPICS và tập dài): mỗi phần thêm thẻ số + tên phần; trước màn chốt, sân khấu hiện cả bản đồ làm phần tóm tắt.
  - **Mô tả**: 2–3 đoạn tóm tắt (ý của David) + chương + liên kết tới tập liên quan + liên kết tài nguyên do David cung cấp.
  - **Mục tiêu cuối**: để người xem *thấy hành động*, câu giao việc cụ thể nhất của tập có màn `action`.
- **Học từ 20 podcast Việt** (`references/hoc-tu-20-podcast-vn.md`):
  - **Thẻ chương**: sân khấu tự hiện "PHẦN n" ở đầu mỗi `TOPICS` (khi có ít nhất 2 TOPICS); `chuong.py` ghi chương YouTube từ TOPICS.
  - **Teaser** cho tập đủ dài (Claude tự quyết định): sau render, Claude chạy `doan-gioi-thieu.py` với 2–3 câu then chốt (trọn câu, nguyên văn); độ dài theo hồ sơ.
  - **Thumbnail theo mẫu cố định** cho mọi tập, không có số tập, không có khuôn mặt — mẫu ở khối 14.
  - **Nền "lắng"** cho tập tâm sự / thiền: `STAGE.bg = [{at: 0, src: 'nen-1.jpg'}, …]` (ảnh hoặc tranh do David cung cấp hoặc có giấy phép, trong
    `chuyen-dong/public/`) — chuyển động rất chậm, phủ tối; nếu không có thì dùng lưới tối mặc định.
  - Tập rất dài được giảm mật độ cảnh trong mức 30%: sân khấu + thẻ chương + TOPICS là đủ.
  - Tài liệu podcast QUAY NGƯỜI để dùng sau này: `references/podcast-quay-nguoi.md`.

## Công thức — Podcast · hồ sơ `podcast`
| # | Bước | Khối |
|---|---|---|
| 1 | Môi trường + dự án (mục dưới) · khung xuất *(bước nhẹ)* | [01](../mo-dun/01-phien-am/README.md) · [04](../mo-dun/04-khung-hinh/README.md) |
| 2 | Chép lời + phụ đề *(chép lời là bước nhẹ)* | [01](../mo-dun/01-phien-am/README.md) · [03](../mo-dun/03-phu-de/README.md) |
| 2b | Thumbnail (ngang + YouTube): mẫu không có khuôn mặt gồm nền hoạ tiết + một hình theo ý của tập + tiêu đề ngắn + "DAVID · PODCAST", không lộ các bước giải pháp | [14](../mo-dun/14-anh-thu-nho/README.md) |
| 3 | Tách lượt người nói (`PY=$(zsh $SKILL/scripts/cai-python.sh)` → `$PY $SKILL/scripts/nguoi-noi.py "$P" [số người]` — **podcast 1 người ghi `1`**, nếu không ghi thì cách dự phòng mặc định là 2 người) · sóng âm (`$PY $SKILL/scripts/duong-bao-am.py "$P"`) · sân khấu, TOPICS, PHẦN n, nền lắng | [12](../mo-dun/12-san-khau-podcast/README.md) |
| 4 | Phong cách · **tuyến nội dung → nhạc nền** (`project.tuyen`, bắt buộc) | [10](../mo-dun/10-nhan-dien-thuong-hieu/README.md) · [09](../mo-dun/09-am-thanh/README.md) |
| 5–6 | Chẩn đoán (`python3 -I $BASE/scripts/chan-doan.py "$P"` + mục `## Chẩn đoán` trong `ke-hoach-canh.md`, thiếu thì công cụ chặn render) → tự chọn lớp thông tin, kiểu cảnh ([huong-dan-lua-chon](../thiet-ke-bo-cuc/huong-dan-lua-chon.md)) · cảnh minh hoạ (bố cục tự cân) · màn chốt nguyên văn | [07](../mo-dun/07-canh-minh-hoa/README.md) · [08](../mo-dun/08-phan-ket/README.md) |
| 7–9 | Chụp thử → Claude tự rà soát → render → kiểm (mục dưới) | [17](../mo-dun/17-kiem-soat-chat-luong/README.md) · [09](../mo-dun/09-am-thanh/README.md) |
| 10 | Phát hành: teaser khi tập đủ dài, chương, màn kết, số liệu | [15](../mo-dun/15-xuat-ban/README.md) · [16](../mo-dun/16-phan-tich-so-lieu/README.md) |

### 1. Môi trường + dự án
```bash
zsh $BASE/scripts/kiem-moi-truong.sh
zsh $SKILL/scripts/tao-podcast.sh "<file tiếng hoặc video>" <tên-ngắn> [doc|ngang]   # → ~/Movies/tap-<tên>/2-ban-day-du (gốc vào tap-<tên>/1-goc), dòng cuối = $P
```
Script lấy phần âm thanh (bỏ hình), giữ nguyên toàn bộ (`cat-thua` ở tham số 4 mới cắt khoảng lặng đầu/cuối, chỉ dùng cho clip highlight; ghi `kiem-tra/cat-goc.txt`),
tạo `tu-lieu/am-thanh.wav` + `audio.m4a`, chép template của skill gốc, `du-an.js` có `podcast: true`, khung theo nguồn (hoặc theo tham số 3).

### 2. Lời nói + phụ đề
```bash
zsh $SKILL/scripts/phien-am.sh "$P"                    # chạy nền; ~1 phút / 5 phút tiếng
python3 -I $BASE/scripts/phu-de.py "$P"               # → chuyen-dong/src/phu-de.js (nháp)
```
Claude sửa TỪNG dòng theo khối 03: chính tả, câu bịa đặt ("Hãy subscribe…" — đối chiếu `ban-chep-loi.srt` với `moc-tung-tu.srt`), chỗ ngắt dòng.
**Riêng podcast**: ở chỗ đổi người nói, mốc thời gian từ Whisper thường lệch 1–2 s nên dòng phụ đề có thể bắt đầu trong lượt của người kia. Claude đối chiếu
`nguoi-noi.js` (bước 3) và dời mốc.

### 4. Phong cách
Không có mẫu thì skill dùng phong cách mặc định của template. Có video hoặc ảnh mẫu thì theo khối 10.

### 6. Minh hoạ
Theo khối 07 + `../quy-tac-chung.md` mục 4: lời nói nhắc tới nơi, người, vật, việc cụ thể thì dùng **ảnh thật** (chỉ ảnh Việt Nam, `$BASE/scripts/kho-anh-openverse.py`);
ý trừu tượng thì dùng **biểu tượng vẽ** hoặc sơ đồ (`icon` trong `montage`/`card job`, xem `$BASE/references/thiet-ke-canh.md`). Số liệu thể hiện bằng hiệu ứng, đúng con số người nói. David nói "không dùng ảnh" / "thêm ảnh" thì Claude làm theo.

### 7. Chụp thử (trước khi render — Claude tự rà soát)
```bash
zsh $SKILL/scripts/anh-tinh-podcast.sh "$P" nen@<giây> <id>@<giây> ...     # sân khấu + cảnh + phụ đề cùng mốc → kiem-tra/anh-tinh.jpg
```
Claude chụp mỗi cảnh ở khoảnh khắc nhiều nội dung nhất + vài mốc chỉ có sân khấu (`nen@…`) ở các TOPICS và lúc đổi người nói. Kiểm: chữ tràn, dấu bị
cắt, hai dòng chữ chồng nhau hoặc chạm khung ảnh/biểu tượng (chữ lớn đặt sau dòng khác thì chừa `aboveGap`), màu sóng âm đúng người nói, ý
đang bàn khớp lời nói, lớp phủ không chạm sóng âm/vòng micro (ngang), thanh thời gian và phụ đề không bị che, không có gì tràn vùng đỏ.
Claude sửa tới khi đạt rồi render ngay.

### 8. Render + xuất
```bash
cd "$P/chuyen-dong" && node xuat-video.mjs                          # chạy nền: cảnh + phụ đề + sân khấu (~1,5× thời lượng)
python3 $SKILL/scripts/nen-podcast.py "$P"                # sân khấu + tiếng → tu-lieu/video-goc.mp4
python3 -I $BASE/scripts/the-ghi-cong.py "$P"              # chỉ khi có ảnh → nguon-anh.txt
python3 -I $BASE/scripts/xem-truoc-ban-dung.py "$P"            # chạy nền → video-hoan-chinh.mp4
```
Podcast 15 phút: sân khấu mất khoảng 25 phút, phụ đề khoảng 10 phút, bước ghép cuối khoảng 10 phút — Claude báo trước thời gian chờ.

### 9. Kiểm tra bản cuối
`zsh $BASE/scripts/kiem-khung-hinh.sh "$P" "$P/video-hoan-chinh.mp4" <mốc giữa & cuối mỗi cảnh, vài mốc chỉ sân khấu>` rồi xem `kiem-tra/bang-anh.jpg`.
Âm thanh được kiểm như khối 17 (chuẩn khối 09; nguồn để so sánh tiếng rè là `am-thanh.wav`), thời lượng bằng `am-thanh.wav` (+ thẻ cuối nếu có).

### 10. Phát hành + bàn giao
Phát hành theo `../quy-tac-chung.md` mục 7. Thumbnail podcast (khi có):
`THUMB_HINH=<hình> THUMB_TAG=PODCAST zsh $BASE/scripts/anh-thu-nho.sh "$P" - "<DÒNG 1>" "<DÒNG 2>" 1|2` (khối 14, chữ do Claude tự chọn).
Chép `san-xuat-video/mo-dun/16-phan-tich-so-lieu/mau-so-lieu.md` sang `$P/so-lieu.md`.
Claude gửi `video-hoan-chinh.mp4` (+ thumbnail nếu có) (SendUserFile). Báo cáo tiếng Việt: người nói (tên/vai trò, tỉ lệ, chỗ chưa chắc chắn), danh sách
cảnh + TOPICS theo mốc, `nguon-anh.txt` nếu có ảnh, đã kiểm gì / chưa kiểm gì, tên riêng cần xác nhận chính tả.

## Bảng phụ thuộc (sửa X thì chạy lại Y)
| Sửa | Chạy lại |
|---|---|
| phu-de.js | `node xuat-video.mjs phu-de` → xem-truoc-ban-dung.py |
| STAGE / TOPICS / speakers / envelope | `node xuat-video.mjs nen` → nen-podcast.py → xem-truoc-ban-dung.py |
| một cảnh (canh.js) | `node xuat-video.mjs <id>` → xem-truoc-ban-dung.py |
| thêm / bớt / dời cảnh (canh.js): sân khấu tự ẩn chữ chủ đề theo danh sách cảnh | `node xuat-video.mjs <các id> nen` → nen-podcast.py → xem-truoc-ban-dung.py. Bỏ `nen` sẽ lộ chữ sau thẻ; ảnh chụp thử KHÔNG thấy lỗi này, phải kiểm bản cuối |
| video-hoan-chinh (teaser) | chuong.py |

## Sửa theo góp ý
- Một cảnh thì sửa `canh.js`, rồi chạy `node xuat-video.mjs <id>`, rồi `xem-truoc-ban-dung.py`.
- TOPICS / STAGE / người nói / sóng âm thì chạy `node xuat-video.mjs nen`, rồi `nen-podcast.py`, rồi `xem-truoc-ban-dung.py`.
- Phụ đề / thanh thời gian thì chạy `node xuat-video.mjs phu-de`, rồi `xem-truoc-ban-dung.py`.
- Thumbnail thì chạy lại `anh-thu-nho.sh` với chữ/ảnh mới (không cần render video).

## Cấu trúc dự án
```
~/Movies/tap-<tên>/2-ban-day-du/
├── tu-lieu/   nguon.* (file gốc) · am-thanh.wav/.m4a (tiếng giữ nguyên) · nen.mp4 (sân khấu) · video-goc.mp4 (sân khấu + tiếng)
│                    <id>.mov (cảnh, nền trong suốt) · phu-de.mov (phụ đề + thanh thời gian)
├── chuyen-dong/src/      canh.js (STAGE, TOPICS, SCENES) · phu-de.js · nguoi-noi.js · duong-bao-am.js · khung-podcast.js · chu-de.js
├── kiem-tra/           cat-goc.txt (chỉ khi cat-thua) · goc/ (transcript, words) · nguoi-noi.md · anh-tinh.jpg · bang-anh.jpg
├── phat-hanh/  phat-hanh.md · anh-thu-nho-1.jpg · anh-thu-nho-2.jpg
├── hinh-anh/ · ke-hoach-canh.md · nguon-anh.txt · so-lieu.md
└── video-hoan-chinh.mp4
```

## Xong khi
1. Claude không hỏi giữa chừng, trừ khi có tín hiệu nặng; có chụp thử để Claude tự rà soát trước khi render; báo cáo có "đã chọn X vì Y".
2. Chỉ nội dung gốc, giữ trọn tập; chữ trên video là nguyên văn; không có thẻ tiêu đề, số tập, ngày tháng.
3. Sân khấu, sóng âm, thanh thời gian chạy suốt video; màu sóng âm đúng người nói.
4. Hình phủ khoảng 30% thời lượng, dày hơn ở đoạn khó, không để trống lâu ở phần đầu.
5. Phụ đề đúng chữ, đủ dấu, khớp lượt người nói; không có gì tràn vùng đỏ.
6. Âm lượng và thời lượng khớp bản âm thanh gốc.
7. Đủ gói phát hành (tiêu đề, chương, teaser nếu tập đủ dài, thumbnail không có khuôn mặt nếu xuất ngang, mẫu số liệu).

## Tài liệu kèm (chỉ đọc khi bước cần, khi cân nhắc đổi luật hoặc gỡ lỗi)
- `references/thiet-ke-podcast.md` — cấu tạo sân khấu, chọn cảnh cho lời hội thoại, vùng giữa.
- `references/nhat-ky-thay-doi.md` — sổ quyết định theo ngày + lý do.
- `references/loi-thuong-gap.md` — lỗi riêng của podcast (mốc Whisper ở chỗ đổi người nói, nhận diện giọng, thời gian render).
- `$BASE/references/thiet-ke-canh.md` — mọi loại cảnh có sẵn + props (dùng chung).
- `san-xuat-video/mo-dun/16-phan-tich-so-lieu/mau-so-lieu.md` — mẫu số liệu sau khi đăng.
