# Khối 13-chon-khoanh-khac: Chọn khoảnh khắc highlight: bản đồ cả video, tự chọn ý theo 4 câu, chọn câu, bố trí lời kêu gọi, cắt + kiểm lời

**Dùng trong:** highlight
**Đầu vào:** video dài / dự án gốc
**Đầu ra:** phuong-an.json, cat/<id>.mp4 + map + kiểm lời, ke-hoach-cat.md
**Tham số hồ sơ:** highlight: *
**Sửa khối này → chạy lại:** 11 (hl_edl.py viết lại edl.js) → 05 → 17

**File thật (code, một bản duy nhất):**
- `cat-highlight-video/scripts/{new_highlight.sh,loud_check.py,cut_highlight.py,pauses.py,hl_edl.py,hl_apply.py}`

## Cách làm (chuyển nguyên văn từ SKILL.md cũ — ngày 2026-11-04)

### 0. Nhận loại video gốc (quyết định cách dựng)
| Video gốc | Nhận ra | Highlight ra | Dựng bằng |
|---|---|---|---|
| **Tự quay có người nói** (talking-head, ngang hoặc dọc) | thấy người trong hình; chưa có chữ/phụ đề đốt sẵn | hình người nói, khung dọc bám người nói, phủ hiệu ứng như skill gốc | bước 7A — `video-style-edit` |
| **Podcast / video toàn đồ hoạ** (sân khấu, sóng âm, thẻ — vd. bản dựng của `podcast-style-edit`) | không có người; đồ hoạ, phụ đề, thanh thời gian đốt sẵn | podcast đồ hoạ **dọc** dựng lại từ tiếng gốc, cùng phong cách + tên tập (`STAGE`) + người nói của bản gốc | bước 7B — `podcast-style-edit` |
| **Video đã dựng có người nói** (bản `video-style-edit` đã phủ chữ/phụ đề) | có người + chữ/phụ đề đốt sẵn | như hàng 1, nhưng dựng từ **bản sạch** `davinci/media/video_goc.mp4` của dự án gốc (không chồng 2 lớp chữ) | bước 7A |
| Không rõ / đã đốt chữ mà không tìm được dự án gốc | — | **hỏi người dùng** bản thô hoặc thư mục dự án; không phủ thêm phụ đề lên phụ đề | — |

Cắt thẳng hình đồ hoạ ngang rồi đặt vào khung dọc là **không đạt** (chữ nhỏ, bố cục ngang vỡ, thanh thời gian hiện thời lượng
bản dài) — luôn dựng lại.

### 1. Môi trường + dự án
```bash
zsh $BASE/scripts/check_env.sh
zsh $SKILL/scripts/new_highlight.sh "<thư mục dự án gốc | video dài>" <tên-ngắn> ["<phụ đề .srt/.vtt>"]   # chạy nền; dòng cuối = $P
```
→ `~/Movies/tap-<tên>/3-highlight/`: `nguon.<ext>`, `loai.txt` (podcast · tu-quay · chua-ro), `check/goc/`: `transcript.srt`, `words.srt`,
`loud05.txt` (độ lớn tiếng mỗi 0,05 s), `contact.jpg`; từ dự án gốc thêm `captions-goc.js` (lời đã sửa chính tả — nguồn chữ chính),
`scenes-goc.js` (tên tập, người nói, kịch bản gốc), `du-an-goc.txt`. Đưa file video → chép lời bằng whisper.cpp + `large-v3-turbo`
(không dùng faster-whisper/pip); `loai.txt = chua-ro` → xem `contact.jpg` rồi quyết theo bảng bước 0.
Whisper bịa câu ở đoạn không lời ("Hãy subscribe cho kênh…") — bỏ, không dùng làm câu chọn.

### 2. Bản đồ cả video (bắt buộc, trước khi chọn câu)
Đọc HẾT lời (ưu tiên `captions-goc.js`, không có thì transcript; sửa chính tả bằng `youtube.srt`), ghép thành câu hoàn chỉnh,
rồi ghi đầu `$P/ke-hoach-cat.md`:
- **Nỗi đau** video giải quyết và **lời hứa cốt lõi** — mỗi thứ một câu nguyên văn kèm mốc.
- **Lời kêu gọi**: liệt kê MỌI câu kêu gọi kèm mốc, xếp theo độ mạnh; đánh dấu **lời kêu gọi chính** (việc người nói muốn người xem
  làm NHẤT) và câu **mạnh nhất về cảm xúc** (thường khác nhau — dùng cả hai được). Ghi rõ video có câu "Vấn đề:/Kết quả:" không.
- **Các ý lớn** theo thứ tự video (mốc bắt đầu, 1 câu nguyên văn tiêu biểu). · **Lằn ranh**: câu nào bị loại (bước 5).

Gán vai cho từng câu:
- **CHAM** — câu mở mạnh, có xung đột, nghịch lý hoặc chạm nỗi đau, đứng riêng vẫn hiểu.
- **DAUHIEU** — tình huống người xem nhận ra mình. · **GOCRE** — giải thích vì sao kẹt / điều nghịch lý cốt lõi.
- **BUOC** — một bước trong cách làm. · **HANHDONG** — lời giao việc cụ thể ("dừng video, viết ra…", "trong 48 giờ…").
- **KEUGOI** — mời bình luận/làm theo, câu hỏi kết, "Vấn đề:" / "Kết quả:". · **KETQUA** — điều thay đổi khi làm được.
- **CHUYEN** — kể chuyện cá nhân. · **THUA** — chào hỏi, lặp ý, "như mình nói ở trên", chuyển đoạn, ậm ừ.

### 3. Tự chọn ý theo 4 câu, rồi chọn câu cho từng clip
**Không hỏi David chọn đoạn.** Bốn câu `boi_canh`, `y_tron`, `mang_ve`, `chua_lai` ở đầu `cat-highlight-video/SKILL.md` là thước chọn; số clip và độ dài theo ý, không có số cố định.
Từ bản đồ bước 2, liệt kê các **khoảnh khắc ứng viên** (một chuyện kể, một nghịch lý, một con số gây sốc, một lời khuyên làm được
ngay…) kèm mốc; chấm theo 4 câu trước, rồi theo câu mở (mục 6 dưới). Giữ các ý đạt đủ 4 câu, khác nhau rõ
(luật 2), đặt tên clip A (mạnh nhất), B, C… Với **mỗi clip**, chọn câu phục vụ lời hứa cốt lõi hoặc ý lớn của khoảnh khắc đó:
1. Một câu CHAM mạnh nhất (lấy từ đâu cũng được).
2. 1–2 câu DAUHIEU / GOCRE nối tự nhiên với câu chạm — là ý chính của cả video, không phải chi tiết phụ.
3. Đúng **một** việc HANHDONG — ưu tiên việc làm được ngay khi đang xem; là việc lời kêu gọi chính nhắm tới. Bỏ nhãn "bước 1"
   nếu clip không có các bước kia (bắt đầu câu ở chữ sau nhãn).
4. **Lời kêu gọi chính** — bắt buộc; thêm câu mạnh nhất về cảm xúc + KETQUA nếu chúng làm cú chốt mạnh hơn.
5. Chỉ thêm CHUYEN/BUOC khi thiếu nó thì hành động không hiểu được, và vẫn trong giới hạn thời gian.

6. **Câu mở đầu** chấm theo: bất ngờ / kết quả lớn ("họ sống thọ… không bị bệnh tật nhiều") = **tiền cược** (sinh mạng, tiền,
   "còn 5 phút để sống") = **kết quả trước, quá khứ sau** ("3 năm sau khi bị chê… gọi vốn 5 triệu USD") = **câu đố cho người
   xem** ("bạn đoán được…?") > câu khiêu khích / con số danh sách ("3 bài học…") > câu hỏi day dứt ("tại sao… không phải thuốc
   thang") > nỗi đau cụ thể > lời than chung. Câu mở có thể là một vế ngắn 2–4 s đặt trước câu chạm.
7. **Chừa cho bản đầy đủ** (luật 10): ghi trong ke-hoach-cat.md chuyện hoặc ý mở rộng nào được để dành; không chừa phần kết của ý trong clip.

8. **Thẻ tít mở đầu** (luật 7): viết 1 tít ≤ 8 chữ cho từng clip, ghi kèm câu gốc làm căn cứ.

Các clip không dùng chung câu chính; một câu kêu gọi mạnh có thể dùng lại ở 2 clip khi mỗi clip có chạm + ý khác nhau.
Ghi ngắn trong ke-hoach-cat.md vì sao chọn các khoảnh khắc này và bỏ các ứng viên khác.

### 4. Bố trí lời kêu gọi (tự chọn cho từng video)
Người xem video ngắn quyết định ở lại trong vài giây đầu và nhiều người không xem tới cuối → lời kêu gọi không mặc định nằm
cuối. Chọn MỘT kiểu hợp mạch nội dung (ghi kiểu + lý do vào ke-hoach-cat.md):

| Kiểu | Bố trí | Hợp khi |
|---|---|---|
| **Thách thức mở đầu** | Câu kêu gọi/việc cần làm LÀ câu chạm (0–3 s) → ý chính giải thích vì sao → chốt lại bằng kết quả | Câu kêu gọi tự nó gây tò mò hoặc thách thức ("Trong 48 giờ, hãy viết ra…") |
| **Giao việc sớm, chốt cuối** | Chạm → ý chính → giao việc sớm (~8–15 s) → kết quả → các câu kêu gọi dồn thành cao trào cuối | Mặc định cho video dạy cách làm: người rời sớm vẫn kịp nhận việc, người ở lại nhận lời mời bình luận |
| **Cao trào cuối** | Chạm → dấu hiệu → gốc rễ dồn nén → hành động + kêu gọi ở đỉnh cảm xúc cuối | Video kể chuyện, cảm xúc tăng dần; câu chạm đã đủ giữ người xem |
| **Vòng lặp** | Câu cuối nối ngược về câu chạm (câu hỏi cuối được câu đầu trả lời, hoặc câu cuối lặp ý câu đầu — Tony Robbins "3 chữ P", Hormozi) | **Mặc định khi clip ≤ 35 s và có cặp câu như vậy**; nền tảng tự phát lại — tăng lượt xem lại. Thẻ cuối (luật 11) bỏ ở kiểu này để vòng lặp liền |

Bất kể kiểu nào:
- **Câu kêu gọi chính có thể xuất hiện 2 lần** — lời nói một lần ở vị trí đã chọn, và **chữ nguyên văn** của nó ở màn chốt 4 s
  cuối. Không lặp lời nói hai lần trừ khi chính người nói đã nhắc lại trong video.
- **Cú chốt cảm xúc** ở câu mạnh nhất (bằng dựng, không bằng chữ thêm): chữ to đúng cụm đắt nhất **đúng lúc nói cụm đó**
  (ngắn để chữ đạt cỡ lớn — ≤ ~14 ký tự/dòng, vd. "MÃI MÃI / KHÔNG THỂ HIỂU"); nguồn có người nói thêm khung dồn chậm vào mặt
  (`zoom: true`, bước 6); 1 s lặng sau câu hỏi để người xem kịp nghĩ.
- Kiểu nào cũng phải đạt bước 5 (tự đứng được) — đổi chỗ mà câu mất nghĩa thì chọn kiểu khác.

### 5. Kiểm clip tự đứng được + lằn ranh nội dung
Đọc nối các câu theo thứ tự đã bố trí như người chưa xem bản đầy đủ. **Người xem clip là người xem độc lập (David chốt 2026-11-06):** xem một mình phải biết hoàn cảnh là gì và clip nói gì; thiếu hoàn cảnh thì thêm câu nguyên văn nêu hoàn cảnh, không có thì bỏ clip. **Chấm riêng từng clip** theo câu hỏi gốc của khối 00: giúp làm chủ bản thân hoặc làm chủ công việc thêm một bước; đoạn chỉ nói về cảm xúc thì không đạt, dù câu nghe đắt. Loại/thay câu khi:
- Có từ trỏ chỗ khác: "ở trên", "như mình vừa nói", "bước 2" mà không có bước 1, "cái này"/"phương pháp này" chưa nói là gì.
- Hành động không làm được nếu không xem bản đầy đủ; câu cắt giữa chừng, mất chủ ngữ hoặc mất ý; đổi chỗ làm lệch nghĩa.

Loại mọi câu dính **lằn ranh** (`../luat-chung.md` mục 1). Câu bị loại mà là câu chủ chốt → báo David, **không tự sửa lời**.
Video không có câu HANHDONG hoặc KEUGOI dùng được → **dừng, báo người dùng** (gợi ý đoạn gần nhất); không thêm chữ thay lời.

### 6. Cắt ghép + tự kiểm
Viết `$P/phuong-an.json` — mỗi clip một mục trong `options` (A, B, C…), câu **theo thứ tự phát trong clip**; mốc `start`/`end` = chữ đầu / chữ cuối của câu (tra `check/goc/words.srt`),
`text` = nguyên văn câu (từ captions-goc.js nếu có):
```json
{"options": [
  {"id": "A", "layout": "Giao việc sớm, chốt cuối", "chon_y": {"boi_canh": "…", "y_tron": "…", "mang_ve": "…", "chua_lai": "…"}, "pieces": [
    {"start": 4.60, "end": 8.30, "role": "CHAM", "text": "…nguyên văn…"},
    {"start": 263.35, "end": 269.28, "role": "HANHDONG", "text": "…"},
    {"start": 379.12, "end": 384.72, "role": "KEUGOI", "text": "…", "zoom": true}]},
  {"id": "B", "layout": "Vòng lặp", "pieces": [ … ]}
],
 "endcard": {"title": "<tên tập gốc>", "speaker": "<tên người nói>"}}
```
**Soát mốc theo độ lớn tiếng** (mốc từ Whisper hay lệch 0,5–1,6 s ở chỗ ngắt câu: chữ đầu bị kéo sớm vào khoảng lặng — cắt theo
đó lọt đuôi chữ câu trước; chữ cuối kéo dài vào câu sau):
```bash
python3 -I $SKILL/scripts/loud_check.py "$P"           # dải █/▁ quanh từng mốc + mốc đề xuất
```
Theo mốc đề xuất (sửa phuong-an.json). "⚠ lệch > 1 s" → nhìn dải xác nhận; "⚠ nói liền" → giữ mốc Whisper, hoặc lấy luôn chữ
nối ("Nhưng…") nếu câu vẫn đúng nghĩa, rồi để bước kiểm lời quyết. Rồi:
```bash
python3 -I $SKILL/scripts/cut_highlight.py "$P"          # cắt bản kiểm lời cat/A.mp4, cat/B.mp4… (chạy nền)
```
→ `cat/<id>.mp4` (khung như nguồn) + `cat/<id>.md` (4 câu, lời đọc nối, mốc đoạn ghép, bảng cắt, tổng thời lượng, **kiểm lời**) + `cat/<id>-map.json`
+ `cat/<id>-kiem.txt`. Thiếu `chon_y` thì script dừng. Script tự: lùi 0,15 s / thêm 0,25 s · gộp câu liền nhau (≤ 0,6 s) · cắt lặng > 0,6 s giữa câu · **chèn** 1 s lặng
(giữ khung cuối) sau KEUGOI kết bằng "?" và sau KEUGOI cuối clip — không lấy tiếng nguồn phía sau vì câu kế có thể nói liền ·
`zoom: true` dồn 1,0 → 1,12× · **cắt cứng** ở mỗi mối nhảy + **rút khoảng lặng ≥ 0,45 s trong câu** (`pauses.py`, trừ câu
`zoom`) · fade âm ở mối · tiếng fltp 48 kHz stereo · **chép lời lại bản cắt** và so với `text`.
**Kiểm lời phải khớp**: chữ thừa ở mối = lọt đuôi câu bên cạnh → thu mốc; chữ thiếu = bị cụt → nới mốc; lệch kiểu "nhé/nhá" là
Whisper nghe khác (bỏ qua). Cắt lại tới khi sạch.
Ghi tiếp vào `ke-hoach-cat.md`: kiểu bố trí + lý do, tông từng câu, ý chừa cho bản đầy đủ, bảng cắt.

