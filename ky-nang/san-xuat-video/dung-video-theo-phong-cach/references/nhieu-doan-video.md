---
description: "Chế độ ghép nhiều clip thành vlog kiểu chương trình (teaser, chia vòng, phụ đề)."
---

# Chế độ GHÉP NHIỀU CLIP — vlog kiểu game show / chương trình thực tế

*Luật chung cả bộ: `../../quy-tac-chung.md` (đọc trước). Vlog giữ nhịp tự nhiên + phụ đề hộp tối (không cắt khoảng lặng kiểu jump cut).*

## Công thức — Ghép vlog · hồ sơ `../../ho-so-thuong-hieu/ghep-vlog` (hình mẫu chính: Khoai Lang Thang + Jessie Luong)
File này là chi tiết của **khối 11** (`../../mo-dun/11-dung-ghep`). Thứ tự khối:
| # | Bước | Khối |
|---|---|---|
| 1 | Môi trường + `tao-dung-ghep.sh` (cân giọng −20 LUFS) | 01 · 09 |
| 2–2d | Hiểu từng clip · bản đồ + liên kết · giữ/bỏ · khung mở đầu–chào–hành trình–kết | 11 · 01 · 06 (mở đầu) |
| 3–6 | Cấu trúc · điểm nhấn (bố cục tự cân, khối 07) · phong cách · danh-sach-cat.js / ke-hoach.json | 07 · 10 · 11 · 03 |
| 6b | Nâng khung → tránh che người: `nang-lop.py` → `bao-ve-lop-phu.py` | 04 · 05 |
| 7–8 | Ảnh tĩnh → Claude tự soát kế hoạch → render | 17 · 09 |
| 9 | Phát hành: màn kết (`ytEnd`), chương, thumbnail (ngang), tách phần, số liệu | 08 · 15 · 14 · 16 |

Sửa thì chạy lại: ke-hoach.json → danh-sach-cat-vlog.py → nang-lop.py → bao-ve-lop-phu.py → stills → xuat-chuong-trinh.mjs · danh-sach-cat.js sửa thủ công → bao-ve-lop-phu.py → stills → render.

Dùng khi người dùng đưa **từ 2 video gốc trở lên** (hoặc 1 clip không phải nói trước camera mà là cảnh quay sự kiện)
và muốn ghép thành một video hoàn chỉnh có điểm nhấn. Khác chế độ 1 video ở chỗ: **hình gốc bị cắt, sắp lại, đổi tốc độ**,
và **toàn bộ video render trong Remotion một lần (có tiếng)**, không phải lớp phủ trong suốt ghép lên video gốc.

Ví dụ thật đã duyệt: dự án `~/Movies/edit-vlog-nhan-xe` (3 clip iPhone đi nhận xe VF3 thành 56 s), kịch bản ở
`references/vi-du-danh-sach-cat.js`. Đọc nó trước khi viết kịch bản mới để lấy cảm giác về nhịp.

## Quy trình

### 1. Môi trường + khởi tạo
```bash
zsh $SKILL/scripts/kiem-moi-truong.sh
zsh $SKILL/scripts/tao-dung-ghep.sh <tên-ngắn> <clip1> <clip2> ... [--ref <video mẫu>] [--style-from <dự án cũ>]   # chạy nền
```
Clip được đặt tên `c1, c2, …` theo **thứ tự người dùng đưa** (xem `clips.tsv`). Template đã có sẵn file âm thanh
(`public/hieu-ung-am-thanh/`: whoosh, boom, pop, ding1–4, shutter, rewind, sting, tada, music) — tự tổng hợp nên không vướng bản quyền.

### 2. Hiểu từng clip (quan trọng nhất — quyết định chất lượng)
Với mỗi `kiem-tra/cN/`:
- `am-luong.txt` trước: chỗ nào có tiếng thật (> −25 dB thường là có người nói/cười). **Whisper bịa đặt câu khi không có lời**
  — dấu hiệu: "Hãy subscribe cho kênh…", "Cảm ơn các bạn đã xem", một câu lặp suốt clip. Gặp thì cắt đoạn ồn ra và
  chạy lại với `-mc 0` (`whisper-cli … -mc 0 -ml 1 -sow`), cộng lại độ lệch thời gian.
- `moc-tung-tu.srt`: mốc từng từ để cắt đúng giữa hai từ và gắn hiệu ứng đúng lúc từ khoá được nói.
- Cảnh chọn nhanh hơn: dải 1 khung/giây cho một khoảng `ffmpeg -ss <t> -t <n> -i cN.mp4 -vf "fps=1,scale=150:-2,tile=<n>x1" -frames:v 1 x.jpg`.
- `python3 -I $SKILL/scripts/khung-loi.py "$P"` → `kiem-tra/cN/khung-loi.txt`: đoạn TÚI/CHE (khung một màu) và TỐI — gợi ý bỏ, đối chiếu lời trước.
  **Hình hỏng thì bỏ kể cả có lời** (trong túi, che ống kính, vừa rút máy ra thì hình lật ngang/lộn ngược/quay loạn): người xem
  không theo được, lời hay cũng không cứu được (David chỉ ra ở c13 vlog leo núi).
- `half_XX.jpg` (khung mỗi 0,5 s, 13 khung/hàng, khung thứ k của ảnh XX ở giây `XX*13 + k*0,5`): tìm
  **khoảnh khắc đắt** (cười to, quay sang camera, lần đầu thấy thứ quan trọng, cử chỉ chỉ trỏ) và **đoạn hỏng**
  (rung nhoè, quay vào túi/sàn/tay, máy cầm ngang, che ống kính) thì bỏ. Đoạn quay ngang nhưng đẹp: xoay lại
  (`transpose=2` = ngược chiều kim đồng hồ khi mặt đất nằm bên trái khung) và dùng `fit: 'blur'`.
- Cần toạ độ để đặt chú thích: cắt khung có lưới
  `ffmpeg -ss <t> -i c2.mp4 -frames:v 1 -vf "scale=360:640,drawgrid=w=36:h=64:t=1:c=yellow@0.6" x.png`
  (mỗi ô = 10% khung) rồi nhân ra px trên 1080×1920. Camera cầm tay luôn trôi nên lấy 3–4 mốc và cho điểm neo
  **bám theo** (`track` của callout).

### 2b. Bản đồ nội dung + liên kết giữa các clip (BẮT BUỘC)
Ghép nhiều clip KHÔNG phải nối cho đủ số lượng: dù ra game show, video giải thích hay vlog, lời nói ở clip này nhắc
tới thứ gì mà clip khác có hình thì hình đó phải xuất hiện ĐÚNG LÚC câu đó được nói.

1. **Phân loại** — David chỉ đưa clip thuộc một trong hai loại (không có clip "thừa", đừng bỏ clip):
   - **Clip chính**: có người nói / diễn biến, được ghép nối tiếp thành video dài, giữ tiếng.
   - **Clip minh hoạ**: quay vật, thao tác, nơi chốn (ví dụ quay cuốn sổ) để minh hoạ một ý ở clip chính thì luôn
     **tắt tiếng**, chèn dạng **trích dẫn** (khung bo góc trên nền theo phong cách, không toàn khung).
   Dấu hiệu clip minh hoạ: ít/không lời (`am-luong.txt`, transcript rỗng hoặc toàn câu bịa đặt), quay cận vật, ngắn.
   Không chắc thì Claude tự chọn, ghi "đã chọn X vì Y" trong kế hoạch và báo cáo cuối.
2. **Bản đồ**: mỗi clip chính — các chỗ nhắc tới thứ NHÌN THẤY ĐƯỢC (vật, việc, nơi, người; "như hôm trước…") kèm
   mốc từ `moc-tung-tu.srt`; mỗi clip minh hoạ — đoạn nào quay gì (`half_XX.jpg`), đoạn đẹp nhất.
3. **Ghép cặp**: mỗi clip minh hoạ gắn vào câu nói khớp nghĩa nhất (ví dụ: "hàng ngày mình dành khoảng 15 phút để viết"
   ↔ clip quay sổ, tay viết). Đoạn trích dài đúng câu đó (thường 2–6 s; ý kéo dài thì tới 8–10 s), lấy đoạn hình đẹp
   nhất; clip minh hoạ dài có thể chia cho nhiều câu liên quan. Chỉ nối khi khớp nghĩa thật, không bịa đặt liên hệ.
4. **Mạch câu chuyện**: TỰ sắp thứ tự clip chính theo nội dung (mở vấn đề → diễn biến/giải thích → kết), không
   theo thứ tự tên file; vlog sự kiện thì theo thời gian thật.
5. Viết `ke-hoach-ghep.md` (mẫu dưới) + `danh-sach-cat.js` đầy đủ (đoạn trích viết bằng `cite()`), chạy:
   ```bash
   cd "$P/chuyen-dong" && node anh-tinh.mjs <vài mốc lớp phủ>          # như bước 7
   python3 -I $SKILL/scripts/bang-lien-ket.py "$P"                  # → kiem-tra/lien-ket.jpg: [người nói | khung trích dẫn]
   ```
6. **Tự soát kế hoạch rồi render, không chờ** (`../../../chuan-muc-lam-viec.md` mục 2): soát `ke-hoach-ghep.md` + `kiem-tra/lien-ket.jpg`
   theo tiêu chí của mục này, sửa danh-sach-cat.js tới khi đạt rồi sang bước 8. Gửi kèm bản cuối để David góp ý.

Mẫu `ke-hoach-ghep.md`:
```markdown
# Kế hoạch ghép — <tên>
**Câu chuyện:** <1–2 câu>
## Các clip
| Clip | File | Loại | Nội dung |
|---|---|---|---|
| c1 | IMG_0501.MOV | Chính | Nói về thói quen viết mỗi sáng |
| c2 | IMG_0502.MOV | Minh hoạ | Cận cuốn sổ, tay viết |
## Thứ tự trong video
1. c3 (0:00–0:42) mở đầu: … · 2. c1 (…) … — lý do sắp như vậy
## Liên kết trích dẫn (số khớp kiem-tra/lien-ket.jpg)
| # | Mốc video | Câu nói (clip, giây) | Chèn hình (clip, giây) | Lý do |
|---|---|---|---|---|
| 1 | 0:52–0:57 | c1 0:12 "hàng ngày mình dành khoảng 15 phút để viết" | c2 0:03–0:08 cận sổ, tay viết | nói về viết ↔ cảnh viết |
## Bỏ / cắt
- …
```

Ghi `ke-hoach-dung.md` (hoặc gộp vào ke-hoach-ghep.md): câu chuyện 1 dòng, khoảnh khắc (clip, giây), đoạn bỏ và lý do.

### 2c. Tiêu chí giữ / bỏ cảnh
**Thứ tự ưu tiên** khi chọn hay bỏ (Walter Murch): **cảm xúc > câu chuyện > nhịp > hình đẹp**. Cảnh rung mà có khoảnh khắc thật
hơn cảnh đẹp mà trống.

**Giữ:**
- **Có cảm xúc là giữ** — cười, ngạc nhiên, lần đầu thấy, thở dốc, xúc động; kể cả rung/nhoè nhẹ (cắt khung, phóng cỡ tĩnh nhẹ `zoomIn: [a, a, …]` cho đỡ rung).
- **Mốc câu chuyện**: xuất phát, chặng khó, điểm đến, phần thưởng — thiếu một mốc là hẫng.
- Lời có ý/cảm xúc — trọn câu, không cắt giữa câu.
- Cảnh mở mỗi nơi mới 2–4 s (không lời cũng giữ) để người xem biết đang ở đâu.
- **Người khác trong khung: giữ hết** (khách, người bán, người đi cùng) — "vlog vốn không chỉ một mình mình"; không làm mờ mặt.
- **Cảnh tâm linh** (dâng hoa, khấn, tượng thờ): giữ.

**Bỏ:**
- Hỏng thật: trong túi/đen xì, che ống kính, nhoè nặng > 1 s **mà không có cảm xúc/lời**, quay sàn/tay.
- 0,5–1 s đầu/cuối clip lúc bấm quay/tắt máy (tay che, hình lắc mạnh).
- Quay lại cùng một câu / cùng một cảnh nhiều lần thì **Claude tự chọn lần tự nhiên và trọn nhất** (thường lần sau cùng); cảnh nào
  lần nào cũng hay thì ghép nhanh 2–3 s mỗi lần.
- Cùng một ý nói lặp nhiều lần thì giữ lần hay nhất.

**Nhịp (video cần nhịp điệu):**
- Đoạn **trầm quá** (đi bộ không lời, chờ, lặp cảnh) thì **tua 1,5–2×** kèm nhạc, mỗi lần còn khoảng 3–6 s — giữ cảm giác hành trình thay vì
  cắt hẳn; đoạn có lời/cảm xúc thì phát thường.
- Không để quá 20–30 s trôi qua không đổi gì (cảnh mới, nơi mới, điểm nhấn, thẻ chặng).
- **Nhịp cắt mục tiêu** (đo trên 10 Shorts top xem, `cat-doan-noi-bat/references/hoc-tu-video-dan-dau.md`): đoạn `soi` có lời
  khoảng 2,2–2,7 s/cảnh (vlog GaryVee 2,3 · tin Dat Bike 2,2 · Hormozi 2,7); đoạn `lang` 4–6 s/cảnh. Một người nói liền thì không cần
  cắt dày — nhịp đến từ phụ đề + điểm nhấn.
- Video ít nhất 5 phút chia **chặng theo nơi chốn** (thẻ `round` hoặc `location`, chữ lấy từ lời/tên nơi thật).

**Tông bắt buộc khớp cảnh** (`TONE` + `MUSIC.tracks`, xem mục 10): mỗi đoạn tông theo cảnh của nó — vui, khám phá, leo dốc
 thì `soi`; tâm linh, ngắm cảnh lặng, tâm sự thì `lang` (không pháo giấy/boom/pop, chữ hiện chậm, nhạc piano). Đổi cảnh thì đổi tông;
không áp một tông cho cả video khi cảnh không khớp.

Kế hoạch ghép ghi rõ: tổng nguồn thì tổng video, bảng đoạn bỏ (clip, giây, lý do: hỏng / trùng / đầu-cuối clip) và đoạn tua.

### 2d. Khung vlog: mở đầu · chào · hành trình · kết
Chuẩn tham khảo: kênh Jessie Luong (youtube.com/@jessieluongchannel), học từ 13 vlog, theo các video **gần đây nhất**
(2023–2026: không có thẻ nhận diện kênh, đoạn ghép ngắn, nhanh). Chỉ học cấu trúc và nhịp — không chép hình, nhạc, thẻ của kênh.
1. **Mở đầu = đoạn GHÉP** (`ke-hoach.json` → `intro`): cảnh đắt nhất **cả chuyến**, mỗi cảnh câm 2 phách nhạc.
   **Độ dài KHÔNG cố định — do chất liệu và cảm xúc quyết định** (intro Haruku 16,7 s toàn cảnh selfie giống nhau là ví dụ sai): chỉ nhận cảnh THẬT SỰ khác (khác nơi / người / hành động); cảnh gần giống cảnh đã có thì bỏ dù intro rất
   ngắn. Câu nói là xương sống: 1 câu then chốt, câu thứ 2 chỉ khi nó tăng cảm xúc. Thước đo: bỏ cảnh nào mà intro không yếu
   đi thì bỏ. Gợi ý: chất liệu chủ yếu tự quay mặt nói thì 1 câu + tiêu đề trên 1–2 cảnh ≈ 5–8 s; vlog nhiều nơi, nhiều người ≈ 10–20 s.
   Thẻ tiêu đề nằm ngay trên đoạn ghép, ở dải cảnh câm (danh-sach-cat-vlog.py tự đặt, không chồng phụ đề) — chỉ ghi tên chương trình / tên nơi
   hoặc lời nguyên văn, không câu Claude tự viết. 1–2 cảnh `voice` giữ tiếng
   thật + phụ đề nguyên văn: câu then chốt làm cảnh đầu (≈ 3 s), câu cảm xúc làm cảnh cuối. Nhạc riêng cho intro: `intro.music` =
   `intro-soi` (chuyến vui) | `intro-lang` (hành hương, từ thiện, ý nghĩa); cảnh câm tự dài 2 phách, cắt đúng nhịp. Claude **tự chọn kiểu theo nội dung**:
   - kiểu 1 (mặc định, đa số): ghép TRƯỚC thì lời chào;
   - kiểu 2: lời chào có câu chốt rõ ("Let's go", "vlog xin được bắt đầu") thì chào TRƯỚC, đoạn ghép chen ngay sau câu chốt.
   **Đa dạng là bắt buộc:** cảnh nơi chốn / toàn cảnh, người trong đoàn, hành động cao trào, biểu tượng của nơi đến (tượng, rồng,
   bảng tên điện), cảm xúc — KHÔNG quá 2 cảnh mặt người quay cận (vlog tự quay toàn selfie dễ ra 9 cảnh giống nhau). Chọn từ
   `kiem-tra/cac-doan/` hoặc tờ 1 khung/giây của clip; mỗi cảnh vẫn xuất hiện lại ở đúng chỗ trong video. Chụp `anh-tinh.mjs` từng cảnh để soát.
   - kiểu 3 (7 trên 20 vlog Việt đã học — Lâm Vlog, Bắp Sam, SAM, Thương Lê): video có câu nêu NHIỆM VỤ / THỬ THÁCH / LỜI HỨA ("hôm nay
     mình sẽ…", "24 giờ…", luật + phần thưởng) thì câu đó lên đầu (0–5 s) + `pow` tiền cược nguyên văn (thời gian, số lượng, giải), rồi mới hành trình.
   Cảnh câm đoạn ghép: 2 phách bài intro ≈ 1,06 s — đúng nhịp 1,0–1,9 s của vlog Việt top (Khoai Lang Thang, Quang Linh, Kẻ Du Mục).
   **Flycam / cảnh rộng nhất** của chuyến ưu tiên làm cảnh đầu đoạn ghép và cảnh mở mỗi nơi mới (Khoai Lang Thang Cao Bằng, Quang Linh).
2. **Chào + bối cảnh** ngay sau mở đầu: câu chào / giới thiệu chuyến của người quay — đang ở đâu, mấy giờ, đi với ai, vì sao, hôm
   nay làm gì. Không có câu chào thì dùng câu nói bối cảnh rõ nhất. Không viết thêm lời.
3. **Hành trình theo thời gian:** mỗi điểm = tới nơi → gọi tên (lời + thẻ địa điểm) → xem/thử → phản ứng; đoạn đi đường không lời
   tua thành đoạn chuyển chạy nhạc (danh-sach-cat-vlog.py tự làm); giữ đoạn đùa với người trong đoàn.
3b. **Hiệu ứng theo lời (`fx`, bắt buộc với vlog nói chuyện nhiều):** chữ to `pow` trích nguyên văn cụm đắt (tối đa 4–5 chữ), `chips`
   khi lời liệt kê, một `action` ở câu kêu gọi làm theo. Mật độ theo nội dung (bố cục tự cân), vài
   kiểu hợp nhất; chữ không che mặt, không đè phụ đề (tự canh LOW_Y). Chụp `anh-tinh.mjs` từng hiệu ứng trước render.
   **Âm lượng:** giọng mỗi clip đã cân về −20 LUFS lúc tạo dự án; nhạc theo chuẩn âm lượng chung (khối 09) — không chỉnh tay.
4. **Kết bằng lời của chính người quay** (20–40 s): tổng kết chuyến → cảm xúc / lời khuyên → hẹn lần sau → chào; cảnh toàn đẹp
   nhất của nơi đến ở cuối, rồi mới tới màn chốt CTA. Xếp clip có câu tổng kết xuống cuối `doan-video` (theo thời gian nếu nó ở cuối);
   không có thì kết bằng cảnh toàn đẹp nhất — không viết lời tổng kết thay.

### 3. Cấu trúc chương trình
**Thời lượng do nội dung quyết định** — không có tỉ lệ hay con số mặc định. Giữ MỌI cảnh rõ nét, có nội dung,
không trùng; chỉ bỏ đoạn hỏng (quay trong túi/đen xì, rung nhoè, quay sàn/tay, cảnh không rõ gì), đoạn trùng (cùng cảnh/cùng lời
quay lại), chờ đợi thừa. Kết quả có thể chỉ còn 50% tổng nguồn (nhiều cảnh hỏng) hoặc gần 100% (cảnh nào cũng rõ, không trùng).
Đây là GHÉP, không phải highlight: không rút gọn thành clip ngắn trừ khi người dùng yêu cầu. Ghi trong kế hoạch tổng nguồn thì 
tổng video và lý do bỏ từng phần.
Mạch (chọn phần hợp với độ dài và nội dung):
1. **Teaser 3–4 s**: khoảnh khắc đắt nhất (thường là cảm xúc + câu nói hay) + chữ nhấn nguyên văn. Không thẻ "TẬP NÀY CÓ GÌ?".
2. **Tiêu đề 2,5–3 s**: nền là một clip làm mờ (`grade: 'title'`), tên chương trình + 1 dòng phụ trích lời hoặc tên nơi. whoosh + boom + sting.
3. **2–4 "vòng" — CHỈ vlog THỬ THÁCH/game** (0/12 vlog du lịch Việt top có thẻ vòng; vlog du lịch dùng nhãn địa điểm `location`
   + chương YouTube `chuong.py`), mỗi vòng mở bằng thẻ `round` (số viền 01/03 + tên vòng) — chia theo diễn biến thật
   (đến nơi → gặp nhân vật → khoảnh khắc chính → …), không bịa đặt sự kiện.
4. **Replay** khoảnh khắc cảm xúc nhất: phát chậm 0,4×, tắt tiếng gốc, `grade: 'replay'`, tiếng rewind.
5. **Kết**: lời tổng kết của chính người quay (mục 2d.4) thì màn chốt nguyên văn; pháo giấy, tada khi tông vui. Không lời mời do Claude viết.

Đoạn đi lại/chờ đợi: tua 1,5–1,8×. Đoạn không lời mà cần nối: tua nhanh, tắt tiếng, whoosh.

**Không hiện ghi chú kỹ thuật lên video** (quy-tac-chung mục 4): không nhãn tốc độ ("×1,6", "TUA NHANH", "×0,5"),
không "SLOW-MO"/"Xem chậm", không thông số máy quay/khung hình. Tua nhanh, phát chậm cứ làm — người xem tự cảm nhận;
chữ trên màn hình chỉ dành cho nội dung (lời nói, cảm xúc, tên, địa điểm). Thẻ REPLAY giữ được vì là yếu tố chương trình.

### 4. Điểm nhấn — "hộp đồ nghề" và khi nào dùng
| Khoảnh khắc | Hiệu ứng (EDL / OVERLAYS / SFX) |
|---|---|
| Cười to, phản ứng mạnh | `pow` chữ nhấn + pop/ding (không zoom — quy-tac-chung mục 2) |
| **Câu then chốt khi có người thứ hai** (bạn đồng hành, khán giả, người dẫn, người bán…) | **cảnh phản ứng 0,8–1,5 s**: cắt sang mặt người nghe ngay SAU câu then chốt (cười, gật, sững) — tiếng người nói vẫn chạy (`audio` của clip chính) — chất keo cảm xúc của Jay Shetty, Rap Việt, Have A Sip. Không có cảnh phản ứng thật thì bỏ, không lấy mặt người khác ngữ cảnh |
| **Hội thoại 2 người** (mặc cả, phỏng vấn) | `who: 1 \| 2` ở dòng `SUB` → viền ô phụ đề theo người nói (cam / xanh, kiểu GaryVee); vị trí + cỡ phụ đề giữ chuẩn |
| **Người nói nêu kết quả, con số, giá** | ưu tiên **bằng chứng thật** có trong clip gốc (ảnh chụp màn hình giá, hoá đơn, giấy chứng nhận, cảnh vật thật) đúng lúc nói — `cite` khung bo góc; không có thì `chips`/số chạy với đúng con số người nói |
| **Người nói nêu giá, độ cao, số lượng** ("1,7 tỷ", "100 m", "500 bao") | `pointer`/`chips` với ĐÚNG con số người nói (học Ngô Đức Duy, Sang Vlog) |
| Giới thiệu nhân vật | đoạn `freeze` 1,8–2 s (khung đẹp nhất, có thể lấy khung trước đó) + `nameCard` + shutter |
| Đếm/liệt kê theo lời ("1 năm, 2 năm, 3 năm") | `chips` — mỗi dòng hiện đúng mốc từ, ding cao dần (ding1→3) |
| Câu chốt cảm xúc | `pow` + boom |
| Lần đầu thấy vật quan trọng | `pointer` (nhãn + mũi tên) |
| Soi chi tiết | `callout` bám theo vật (`track` 3–4 mốc) |
| Mọi lời nói nghe rõ | phụ đề `SUB`, từ khoá tô màu nhấn (cụm nhiều chữ được); đúng chính tả; câu không nghe rõ thì **bỏ**, không đoán. **Kiểu phụ đề = chuẩn chung `kieu-phu-de.js`** (giống hệt chế độ 1 video: hộp nền tối, đáy vùng an toàn, giãn dòng 1,28) — không tự viết kiểu riêng |
| Chuyển đoạn | chớp trắng tự động + whoosh ở chuyển cảnh lớn |

Mật độ theo nội dung, vài kiểu hợp nhất (quy-tac-chung mục 0); không để 2 chữ to chồng nhau; chữ to và thẻ vòng không đè logo góc (`hud`
ở y≈228, ẩn khi có replay). Mọi chữ trong vùng an toàn x 70–900, y 210–1420.

### 4b. Chuẩn chung với chế độ 1 video ("khớp 100%")
- Phụ đề: `src/kieu-phu-de.js` (tao-dung-ghep.sh chép từ khuon-remotion — MỘT nguồn; sửa kiểu phụ đề chỉ ở đó).
- Chữ to nhiều dòng: chừa chỗ dấu theo cỡ chữ (`Rise`: 0,5 em trên / 0,32 em dưới), giãn dòng 1,12–1,14, khe giữa dòng 0,24 em.
- Chỉ những điểm nhấn có nội dung (tiêu đề, địa điểm, trích dẫn) — bố cục tự cân như chế độ 1 video.
- **Màn hành động + màn chốt** (như chế độ 1 video): lớp phủ `{type: 'action', start, end, quote, doneAt}` khi người nói nêu việc
  người xem làm được (phụ đề tự ẩn trong cảnh đó); màn chốt TỰ có ở 4 s cuối (cả hình lùi vào khung) — câu = nguyên văn câu người quay
  nói ở cuối (khối 08), ghi vào `CTA = {text, kind}` trong danh-sach-cat.js. Lớp `outro` kiểu game show nếu dùng phải kết thúc trước màn chốt.
- Trích dẫn clip minh hoạ trong khung bo góc (`cite()`) — David đã khen chuẩn, giữ nguyên.
- **Nâng khung**: đoạn có người/vật chính nằm nửa dưới thì đẩy hình lên, đáy lấp hình mờ, mép chuyển mềm
  (`chuong-trinh.jsx` → `Clip`). Sau khi viết danh-sach-cat.js chạy `python3 -I $SKILL/scripts/nang-lop.py "$P"` → `src/nang-lop.js`, rồi **`python3 -I $SKILL/scripts/bao-ve-lop-phu.py "$P"`**
  → `src/bao-ve.js` (lớp chữ che mặt/thân trên tự thành toàn màn hình, dài theo nội dung; tít ghim che đầu tự ẩn — khối 05; chạy lại sau mỗi lần sửa danh-sach-cat.js) (tự tính theo mặt, đọc
  bảng `kiem-tra/khuon-mat/lift.md`). Đoạn không có mặt (quay đồ vật, cầu thang, khay đồ uống…) mà vật chính thấp thì đặt tay
  `lift: {y: 150–250}` trong đoạn ở danh-sach-cat.js (đặt tay thắng tự tính). Không nâng: đoạn tiêu đề, `fit: 'blur'`, trích dẫn.

### 5. Phong cách
- Chữ ký nhận diện (nhấn cam #FF7A45, Barlow Condensed + Be Vietnam Pro, thành phần cố định) giữ ở mọi vlog.
- Có `--style-from <dự án cũ>`: đọc `chuyen-dong/src/chu-de.js` (+ fonts, components) của dự án đó thì chép phần ngoài chữ ký (nền, màu phụ,
  kiểu chuyển động) vào `C` trong `chuong-trinh.jsx` và `phong-chu.js`, để các video "cùng một nguồn duy nhất sản xuất".
- Có `--ref <video mẫu>`: phân tích như `phan-tich-phong-cach.md` rồi áp vào cùng chỗ.
- Không có gì: giữ mặc định của template (thẻ tối).
  Phong cách game show sặc sỡ (vàng/hồng, chữ viền đen, emoji) đã thử và bị thay bằng bộ mặc định cho đồng bộ.
- Không dùng emoji trong chữ khi phong cách mẫu không dùng.

### 6. Viết `chuyen-dong/src/danh-sach-cat.js`
**Trước khi viết (bắt buộc, khối 11):** `python3 -I $SKILL/scripts/chan-doan.py "$P"` rồi ghi `$P/ke-hoach-canh.md` có mục `## Chẩn đoán`
(dòng `Loại:`, mỗi cảnh `Cần · Vì · Làm` — `../../thiet-ke-bo-cuc/tu-chon.md`). Thiếu thì `soat-canh.mjs` chặn render ở `xuat-chuong-trinh.mjs`.
**Vlog dài nhiều clip (≳ 15 clip / ≳ 5 phút)**: đừng viết tay — viết `ke-hoach.json` (giữ/bỏ từng clip, tông, thẻ địa điểm, sửa chính
tả `fix`, bỏ dòng nghe không rõ `drop_sub`, mở đầu, tiêu đề, CTA; mẫu ở đầu script) rồi
`python3 -I $SKILL/scripts/danh-sach-cat-vlog.py "$P"` → danh-sach-cat.js (tự tua đoạn không lời ít nhất 4 s, phụ đề theo câu, TONE + nhạc) + `kiem-tra/cat-vlog.md`.
Sửa theo góp ý = sửa ke-hoach.json rồi chạy lại.
Soát hết phụ đề trước khi render: in `SUBS` ra, câu Whisper nghe sai rõ thì `fix`; câu không rõ thì `drop_sub` (không đoán).
**Soát hình trước khi render (bắt buộc):** danh-sach-cat-vlog.py in ⚠ khi đoạn giữ chạm đoạn hỏng trong khung-loi.txt, và ghi `kiem-tra/cac-doan/*.jpg`
(1 khung/giây mỗi đoạn giữ) thì xem HẾT, bắt hình lật/xoay/quay loạn (độ sáng không dò được), sửa ke-hoach.json (`from`/`to`/`drop`/`skip`).
**Lớp chữ không đè phụ đề (chặn cứng ở chuong-trinh.jsx, nhưng cắt chữ = lỗi):** không đặt `top` ước lượng — neo đáy; chụp ở CUỐI mỗi lớp theo lệnh danh-sach-cat-vlog.py in ra. Đáy mọi lớp chữ tối đa `LOW_Y` (chuong-trinh.jsx: đỉnh dải phụ đề 2 dòng − 20 px). Thẻ địa điểm/tên/replay tự canh
đáy vào đó; `pow` (`y`), `pointer`, `chips` (`top`) đặt tay thì tự giữ luật này — chụp `anh-tinh.mjs` đúng lúc thẻ + phụ đề cùng hiện.

Ba phần: `RAW` (đoạn hình), `SUB` (phụ đề), `OVERLAYS` + `SFX` + `MUSIC`. Mọi mốc là **giây trong clip gốc**, quy
đổi bằng `T(id, src)`, `segStart/segEnd` — sửa một đoạn thì mọi thứ phía sau tự dời theo. Cắt đúng ranh giới từ
(lấy từ moc-tung-tu.srt). Kiểm nhanh timeline:
```bash
cd "$P/chuyen-dong" && node -e "import('./src/danh-sach-cat.js').then(m=>{console.log(m.TOTAL);m.SEGS.forEach(s=>console.log(s.id,s.start.toFixed(2),s.dur.toFixed(2)))})"
```
Loại lớp phủ có sẵn (chuong-trinh.jsx): `teaserTag, title, hud, round, pow, pointer, nameCard, chips, callout, replay, location, outro`.
Chữ truyền qua props: `title {eyebrow, l1, l2, sub}` · `hud {name, tag}` · `round {n, of, text}` · `chips {items, top}` (dòng bắt đầu bằng số thì số viền cam; 4–5 dòng tự thu nhỏ) · `replay {eyebrow, text}` · `location {eyebrow, place, sub}` · `outro {eyebrow, lines[], cta}`.
Ví dụ thứ hai: `~/Movies/edit-vlog-0693/chuyen-dong/src/danh-sach-cat.js` (4 clip quán cà phê thành 117 s, có thẻ địa điểm, danh sách 5 nước).
Cần loại mới thì viết component cùng ngôn ngữ thiết kế rồi đăng ký vào `TYPES`.

### 7. Kiểm tra bằng ảnh tĩnh (rẻ nhất)
```bash
cd "$P/chuyen-dong" && node anh-tinh.mjs <giây timeline> ...     # → kiem-tra/anh-tinh/<giây>.jpg
```
Chụp mỗi lớp phủ ở lúc "đầy nhất", ghép sheet xem: chữ tràn/xuống dòng lẻ, dấu bị cắt, chồng lớp, chú thích lệch vật,
chữ khó đọc trên nền sáng, **người/vật chính bị phụ đề che hoặc nằm dưới nửa khung** ( thì nâng khung). Sửa tới khi sạch.

### 8. Render + kiểm tra cuối (sau khi tự soát kế hoạch ở 2b)
```bash
cd "$P/chuyen-dong" && node xuat-chuong-trinh.mjs        # chạy nền, ~3–9 phút/phút video; tự loudnorm → video-hoan-chinh.mp4
```
Sau đó: cắt 12–15 khung trải đều thành dải xem lại; `ffmpeg -i video-hoan-chinh.mp4 -af ebur128=peak=true -vn -f null -`
(I ≈ −14…−15 LUFS, đỉnh tối đa −1,5 dB). Nhạc lấy từ kho nhạc kênh theo tuyến nội dung (khối 09: ke-hoach.json/edl `tuyen`, bài + mức cân ở hồ sơ chung `nhac`) — Claude tự chọn,
không hỏi David; mức nhạc theo khối 09.

### 9. Phát hành, giao + sửa theo góp ý
Vlog đăng YouTube > 3 phút: `"ytEnd": 20` trong ke-hoach.json (màn kết YouTube 15–20 s sau thẻ nhận diện) + `chuong.py` (chương theo
nhãn địa điểm). Chuyến > 25 phút: đề xuất tách phần P1/P2 (mỗi phần một video, thẻ kết "Hết phần 1" bằng `outro` ngắn — chữ là
tên phần, không tự viết lời) — nêu trong 4 phần lúc đầu.
Phát hành theo `../../quy-tac-chung.md` mục 7. Thumbnail vlog (khi có):
`zsh $SKILL/scripts/anh-thu-nho.sh "$P" c<N>@<giây> "<DÒNG 1>" "<DÒNG 2>" 1|2` (khung cảm xúc mạnh nhất cả chuyến, mặt rõ — thường
là cảnh đắt nhất của đoạn ghép mở đầu); chép `san-xuat-video/mo-dun/16-phan-tich-so-lieu/mau-so-lieu.md` → `$P/so-lieu.md`.
Gửi `video-hoan-chinh.mp4` (+ thumbnail nếu có) (SendUserFile), bảng mạch chương trình theo mốc thời gian, các đoạn bỏ và lý do, chỗ tiếng bị
ghép từ nơi khác. Góp ý kiểu "bỏ đoạn 0:13–0:16" thì tra mốc timeline ra `id` đoạn trong `SEGS`, xoá đoạn đó cùng
phụ đề/lớp phủ/SFX gắn với nó, render lại.

### 10. Dùng cho HIGHLIGHT (skill cat-doan-noi-bat, nguồn có người nói)
Một clip duy nhất `c1` = video gốc dài; `cat-doan-noi-bat/scripts/danh-sach-cat-doan-noi-bat.py` viết sẵn cả `danh-sach-cat.js`. Các phần thêm (vlog thường
để `HL = null`, `TONE = []` nên không đổi gì):
- Đoạn `jump` `{id, clip, from, freeze: 0.4, vol: 0, jump: {from, to}}` giữa hai câu trích không liền nhau: đứng hình + chip
  ⏩/⏪ mốc phút trong tập gốc (`Tua` trong chuong-trinh.jsx), tiếng `tua.wav` (trừ tông lắng). Không chớp trắng quanh đoạn jump.
- `HL = {src_duration}` → `SrcBar`: thanh của CẢ tập gốc ngay trên đáy vùng an toàn (nền tối mờ), phụ đề nhích lên 56 px.
- `TONE = [[từ, đến, 'lang'|'soi']]`: `lang` thì không chớp trắng, `pow` hiện chậm nét mảnh không gạch, chuyển cảnh tối dần
  chip viền cam; đoạn hình `grade: 'lang'` (màu dịu). `soi` = như vlog game show.
- `MUSIC.tracks = [{f, a, b, gain, from?}]`: mỗi bài (`public/hieu-ung-am-thanh/<f>.mp3`, lặp nếu ngắn) chạy một khoảng, chồng mờ 0,8 s ở mối,
  vẫn hạ khi có phụ đề theo `base/duck/loud`. Không có `tracks` → `nhac.wav` như cũ.
- `CTA.text` = câu kêu gọi NGUYÊN VĂN (luật highlight).
- `ENDCARD = {title, speaker, clip, at, len}` → `EndCard`: khoảng 1,8 s **nối thêm sau** `TOTAL` (Root cộng vào thời lượng): ảnh đứng
  hình người nói (giây `at` của `clip`) làm tối + "Bản đầy đủ trên kênh …" + tên tập gốc + tên người nói; không nút phát. Mẫu tự
  bỏ ở video dọc ngắn (`THE_CUOI`, nhan-dien-chung mục 1). `null` (vlog thường) thì không có.
- Không dùng `teaserTag`, `title`, `round`, `hud`, `outro` (chữ tự viết) trong highlight.


### 11. Bản dài từ nhiều file của MỘT buổi nói chuyện (máy quay tách file)
Khi các file gốc là một buổi liền (máy quay tự tách file, cùng góc máy) và David muốn bản dài **bỏ một số ý** ("cắt ý X", "ý chưa trọn thì cắt"):
- **Chọn đoạn theo ý, không theo câu then chốt**: đọc lời cả buổi (trục ghép các file), đánh dấu ý phải bỏ theo yêu cầu + lằn ranh kênh, giữ phần còn lại
  theo thứ tự buổi nói. Trong mỗi đoạn giữ nguyên — không cắt lặng, "ờ/ừm" (quy-tac-chung 2). Mối cắt bắt vào chỗ lặng gần nhất (±0,6 s).
- Lời cả buổi chép trên bản xem nhẹ có **câu ảo che lời thật** ("Hãy subscribe…" = mất 30 s lời, không phải chỗ lặng) thì chép lại riêng phân đoạn đó
  (`loi-ao.py`) trước khi quyết cắt/giữ phân đoạn ấy.
- Cắt các đoạn từ file gốc ghép thành **một nguồn** `nguon-dai.mp4` (ffmpeg `-hwaccel videotoolbox`, 1080p30, 10 Mbps, fade tiếng 40 ms ở mỗi mối)
  → `c1`; chép lời lại trên nguồn mới (`phan-tich-video.sh`). Cảnh câm cho intro lấy từ nguồn khác (`c2`) nếu nằm ở phần đã cắt.
- `RAW`: intro (câu chạm giữ tiếng + đáp lời người kia nếu có, rồi cảnh câm 2 phách) + **một đoạn `p1` = cả `c1`**; `TS(src) = D + src`.
- **Phụ đề**: chữ lấy từ `ban-chep-loi.srt` (bản theo câu, đúng thứ tự chữ hơn), tách cụm tối đa 10 chữ / 52 ký tự theo dấu câu, mốc bám
  `moc-tung-tu.srt`; `SHORT = false` (hộp tối). Soát HẾT phụ đề: sửa chữ Whisper nghe sai rõ, bỏ câu không rõ (không đoán); ghi bảng sửa theo
  chỉ số dòng và in đối chiếu "gốc => sửa" để bắt lệch dòng. Gộp dòng dài < 0,35 s vào dòng kế (Sequence 0 khung làm render dừng).
- Nhận người nói bằng giọng (`dung-podcast/scripts/nguoi-noi.py`, pyannote) hay lẫn giữa câu ở quán ồn thì không tô viền phụ đề theo người khi chưa
  nghe lại được.
- Nhạc: bài intro ở intro; phần chính luân phiên 2 bài cùng tuyến (`MUSIC.tracks` nối tiếp theo độ dài bài) — không lặp một bài cả tiếng.
- Video dài YouTube: `THE_CUOI = true`, `ENDCARD = {…, play: false, yt: 21.6, len: 21.6}` (thẻ nhận diện 1,6 s + màn kết YouTube 20 s).
- Render tốn ổ: mẫu dùng `bundle-nhe.mjs` (video > 50 MB nối cứng vào bản bundle, không chép). Bản thô + bản cuối ≈ 2 × (9 Mbps × thời lượng)
  — đo trước bằng render thử 40 s (`node xuat-chuong-trinh.mjs 0 40 thu.mp4`), thiếu chỗ thì nén thêm (crf 20). M1 8 GB: khoảng 3,3× thời lượng.
- Mẫu: `~/Movies/tap-marketing-noi-dau-nhu-cau/2-ban-day-du` (`ke-hoach-cat.md`, `kiem-tra/dung-phu-de.py`).
