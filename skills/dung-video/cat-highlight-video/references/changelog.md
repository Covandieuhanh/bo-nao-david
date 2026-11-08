# Sổ thay đổi — cat-highlight-video (quyết định của người dùng + lý do)

## 2026-11-03
- Skill tạo từ bản người dùng viết trong Claude Chat (4 vai Chạm · Ý chính · Hành động · Kêu gọi "Vấn đề:/Kết quả:", lằn ranh nội
  dung, mô tả + bình luận ghim). Viết lại phần dựng cho máy này: whisper.cpp thay faster-whisper/pip; dựng qua skill gốc thay vì
  ffmpeg `subtitles=` (ffmpeg Homebrew không có libass) và cắt giữa khung cố định. Bản cũ trong Cowork đã xoá.
- **Luôn dọc 9:16 (1080×1920)**, một bản cho mọi mục video ngắn.
- **Chỉ nguyên văn lời video, tuyệt đối không viết thêm hay đổi chữ** — "vì vậy mới gọi là highlight": xem highlight rồi xem bản
  gốc không lệch nội dung. Áp cả câu màn chốt (khác skill gốc, nơi Claude tự viết câu chốt) và mô tả bài đăng. Chỉ bỏ bớt chữ ở
  đầu/cuối câu; không có câu kêu gọi → báo, không thêm chữ.
- **Ý chính + lời kêu gọi chính của TOÀN BỘ video** (không phải đoạn hay cục bộ) → bước bản đồ cả video bắt buộc.
- **Không thứ tự cố định**: lời kêu gọi đặt ở chỗ hợp mạch (4 kiểu bố trí), vì người xem video ngắn bị giữ/mất ở vài giây đầu;
  cú chốt cảm xúc mạnh bằng dựng (chữ to đúng lúc nói, dồn khung vào mặt, 1 s lặng sau câu hỏi), không bằng chữ thêm.
- **Độ dài 30–60 s, Claude tự cân theo nội dung** (≤ 90 s khi bỏ bớt gãy ý).
- **Highlight cùng loại với video gốc** ("video gốc là gì thì phải ra highlight tương ứng"): podcast đồ hoạ → podcast đồ hoạ dọc
  dựng lại từ tiếng gốc, cùng phong cách + tên tập; người nói → người nói. Lần đầu (podcast "năng lực" 7:32) cắt thẳng hình ngang
  bị loại vì chữ nhỏ, bố cục vỡ, thanh thời gian sai; người dùng chọn dựng lại đồ hoạ dọc, không bìa, dựng 1 phương án.
- Lỗi gặp ở lần đầu → sửa script:
  - Mốc từ Whisper lệch tới 1,6 s ở chỗ ngắt câu ("Không" bị kéo về 2,96 s, thật ở 4,6 s) → `loud_check.py` soát theo độ lớn
    tiếng. Lấy khoảng lặng dài nhất cho mốc cuối từng chọn nhầm chỗ ngập ngừng giữa câu ("…nhìn nhận được ‖ mình là ai") → chỉ lấy
    khoảng lặng sát sau chữ cuối, không có thì cảnh báo.
  - Giữ 1 s sau câu kêu gọi bằng tiếng nguồn lọt chữ câu kế ("…ở bên dưới nhé | Mình sẽ gặp lại") → chèn lặng thật.
  - Tự kiểm: `cut_highlight.py` chép lời lại bản cắt, so với lời đã chọn (bản A khớp 100%).
  - Chữ to dòng dài ("MÃI MÃI KHÔNG THỂ HIỂU ĐƯỢC") co nhỏ mất lực → chỉ lấy cụm ngắn đúng lúc nói.
  - Thêm biểu tượng `write` (viết ra giấy) vào template chung.
- **Chuyển cảnh "tua" + thanh tập gốc** (người dùng xem bản đầu: "cần hiệu ứng chuyển cảnh giữa các đoạn, phải cho người xem cảm
  giác đây đúng là highlight trích từ một video dài, không phải video bình thường"). Người dùng chọn: tua nhanh ngắn (không chớp
  sáng, không cắt cứng), thanh thời gian của cả tập gốc + mốc (thay thanh "còn m:ss"), tiếng vút nhỏ, áp cho cả hai nhánh.
  Code: `cut_highlight.py` chèn 0,4 s/mối nhảy + `jumps` trong map · `hl_apply.py` → `highlight.js` · template `Tua.jsx`,
  `Timeline.jsx` (chế độ highlight), `Captions.jsx` (ẩn phụ đề lúc tua, phụ đề lên trên thanh) · `assets/sfx/tua.wav` (tự tổng hợp)
  · `render_preview.py` trộn tiếng tua (và sửa lỗi chỉ số đầu vào màn nguồn ảnh khi có tiếng hiệu ứng). Không render lại bản cũ.
- Video thứ hai (IMG_3196, người nói, ngoài trời): chip chuyển cảnh thêm "⏪" khi nhảy lùi trong tập gốc (đoạn 3:53 → 2:22 hiện ⏩ là sai
  nghĩa); thanh tập gốc trên video người nói có nền tối mờ (nền trời sáng làm mốc khó đọc); cú chốt đổi sang thẻ toàn cảnh `ages`
  khi chữ to sẽ che mặt (selfie mặt to + dồn khung). Mối nói liền ngoài trời: lọt chữ "là" của câu trước → dời mốc vào chỗ tiếng trũng.
  Thanh tập gốc đẩy phụ đề lên 40 px → ô mở đầu chạm phụ đề 2 dòng → dải lớp phủ dừng sớm 40 px khi có highlight.js (layout.js + face_place.py).

## 2026-11-03 (sau bản Haruku đầu)
- **Lời kêu gọi hành động BẮT BUỘC** — clip không có là không duyệt. **Chỉ một phương án tối ưu nhất** (bỏ phương án B: "chỉ cần
  1 phương án tối ưu nhất là được").
- Người dùng hỏi "xem riêng highlight có đủ kích thích tìm bản đầy đủ không?" → chưa: clip giải hết (vấn đề → cách → bằng chứng →
  lời mời), thiếu kết quả lớn ("sống thọ… không bị bệnh tật nhiều"), câu mở là lời than chung, kết bị chùng. → luật 10 **chừa một
  ý cho bản đầy đủ** + chấm điểm câu mở (bất ngờ/kết quả lớn > câu hỏi day dứt > nỗi đau > lời than). Không thêm nhãn "BẢN ĐẦY ĐỦ".
- **Nhịp game show, MỘT skill hai tông** (`soi` sôi động / `lang` lắng; đổi tông giữa chừng được — "1 video có thể vừa có lúc
  truyền tải thông tin tích cực, vừa có tâm sự"). Video mẫu "Ngày nhận xe" chỉ là mẫu về nhịp, giữ mọi luật cũ; không cần tên vòng.
  Highlight người nói chuyển sang khung ghép clip của video-style-edit (`montage-template`: thêm `HL` thanh tập gốc, đoạn `jump`
  có chip tua, `TONE`, `MUSIC.tracks`) — script `hl_edl.py` viết sẵn edl.js từ phuong-an.json. Podcast: `hl_apply.py` ghi tông +
  nhạc vào highlight.js, `render_preview.py` trộn nhạc (sidechain hạ khi có lời), `Tua.jsx` có kiểu lắng.
- **Nhạc nền cố định vài bài** (`assets/music/soi-*.mp3`, `lang-*.mp3`) — người dùng không muốn nhiều lựa chọn làm loạn bản sắc
  kênh. Nguồn: Pixabay (giấy phép Pixabay Content License, không cần ghi nguồn). Pixabay chặn tải tự động (403) → người dùng tự tải.
- Bản Haruku dựng lại: thêm câu mở "họ sống thọ…" (1:12) + câu hỏi "tại sao… không phải thuốc thang" (1:45); để dành ví dụ cái
  cây + nghĩa "Haruku" cho bản đầy đủ. Mốc từ Whisper ở 1:44 lệch ~0,4 s ("bởi vì" lọt khi cắt ở 104,96) → chép thử từng mốc
  bắt đầu (104,85 / 105,08 / 105,25 / 105,35) tới khi sạch — cách soát khi "⚠ nói liền".

## 2026-11-03 (học từ 10 Shorts top lượt xem)
- Phân tích 10 Shorts lượt xem cao (7 quốc tế, 3 VN; 1,4–41 Tr) → `references/hoc-tu-top-video.md`. Người dùng đồng ý A–J,
  **bỏ K** ("giữ nguyên vị trí phụ đề") — phụ đề vẫn ở đáy vùng an toàn theo `subStyle.js`, dù 7/10 video mẫu đặt giữa khung.
- Luật 12 **thẻ tiêu đề mở 2–3 s** (nguyên văn cụm đắt của câu chạm, nửa trên khung). Luật 13 **thẻ cuối dẫn về bản đầy đủ**
  ~1,8 s (kiểu Have A Sip): chỉ tên tập gốc + người nói gốc + nút phát — người dùng cho phép thay cho luật "không nhãn BẢN ĐẦY
  ĐỦ" vì không có chữ tự viết. Code: montage-template `EndCard` + `ENDCARD` (Root cộng thời lượng), `hl_edl.py` đọc
  `"endcard"` trong phuong-an.json. Nhánh podcast (7B): `EndCard.jsx` + composition `the-cuoi` (remotion-template),
  `render.mjs` → `the_cuoi.mp4`, `render_preview.py` ghép sau video (như bìa ghép trước); `layout.js` coi `endcard` là toàn khung.
  Thử trên bản sao podcast-hl-nang-luc-A: 42,1 → 43,9 s, tiếng phần chính giữ nguyên (−19,2 dB), thẻ câm.
- Lời kêu gọi = câu mệnh lệnh/giao việc nguyên văn (top video gần như không có "hãy bình luận"); thang câu mở thêm "tiền cược",
  "kết quả trước, quá khứ sau", "câu đố cho người xem", "con số danh sách". Vòng lặp thành mặc định khi clip ≤ 35 s có cặp câu.
  Độ dài cho tới 120 s chỉ với câu chuyện hồi hộp có đáp án cuối.
- video-style-edit (multi-clip.md): nhịp cắt mục tiêu `soi` 2,2–2,7 s / `lang` 4–6 s; cảnh phản ứng 0,8–1,5 s sau câu đắt;
  `who: 1|2` viền ô phụ đề theo người nói (Show.jsx `Caption`); ưu tiên bằng chứng thật khi nêu kết quả/con số.

## 2026-11-04
- Bộ nhận diện David chung 4 loại video: highlight người nói (montage) có dấu góc ● DAVID │ tên tập gốc + tiếng ký hiệu mở đầu;
  highlight podcast dùng chung BrandMark / Hook / thẻ cuối của remotion-template.

## 2026-11-04 — NGƯỜI XEM LÀ TRUNG TÂM (David: "các kênh lớn là hình mẫu thành công đã đạt được điều này rồi thì sao chép luôn")
Sau bản đánh giá đối chiếu với kênh lớn (thể loại nói trước camera, highlight, vlog, podcast), David duyệt kế hoạch 5 pha:
- `luat-chung.md` (thư mục dung-video) — một nguồn luật chung; SKILL.md chỉ giữ luật riêng. `so-lieu-mau.md` — vòng số liệu sau 7 ngày.
- **Phát hành** mọi video: 3 tiêu đề + 2 thumbnail 1280×720 (`scripts/thumbnail.sh`, `assets/thumb-template/` — mặt có cảm xúc, ≤ 4
  chữ, nhận diện David; nguồn quay dọc tự thành khung một bên). Video ngắn không ghép bìa trước video.
- **Phụ đề video ngắn** 1–3 chữ to mỗi nhịp ngang ngực (`subStyle.js` `ShortLine`, chuẩn Hormozi/DOAC) — thay quyết định cũ "giữ
  phụ đề đáy" (bỏ đề xuất K ngày 03/11) vì David đổi kim chỉ nam. Video dài / vlog / podcast giữ hộp tối.
- **3–5 clip mỗi video dài** (thay "chỉ MỘT phương án" của 03/11 — David phân biệt: không làm biến thể của cùng đoạn, nhưng nhiều
  khoảnh khắc khác nhau thì có, chuẩn DOAC/Hormozi). phuong-an.json nhiều `options`; dự án dựng `edit-hl-<tên>-<id>`.
- **Thẻ tít mở đầu viết như tít báo** đúng ý người nói (ngoại lệ duy nhất của luật nguyên văn; chuẩn DOAC).
- **Bỏ chip tua ⏩ + thanh tập gốc** (luật 8 ngày 03/11): cắt cứng + phóng xen kẽ 1,08× (giấu mối như clip kênh lớn); khoảng lặng
  ≥ 0,45 s trong câu rút còn 0,24 s (`pauses.py`, dùng chung cut_highlight.py + hl_edl.py). Kiểu cũ: `--tua`.
  hl_edl.py xuất `SUBS` theo giây timeline + `TS(src)`; thử trên highlight-img3196: 8 câu → 17 đoạn, chụp thử thấy phụ đề nhịp chữ.

## 2026-11-04 (học 80 video Việt)
- Học 20 highlight Việt (David duyệt ưu tiên 1+2): tít ghim `pinTitle` (Show.jsx) + `"tit"` trong phuong-an.json; cảnh phản ứng `"react"` (hl_edl.py, đoạn hình khác + `audio` của câu đang nói); khung bìa 0,3 s; 60–120 s cho danh sách; hình dày theo lời ở nhánh podcast. Chưa áp HL-5 (nhãn "Xem bản đầy đủ") — chờ David.
- HL-5 áp (David duyệt): thẻ cuối highlight có nhãn cố định "XEM BẢN ĐẦY ĐỦ" (Show.jsx EndCard, EndCard.jsx); lịch phát `endcard.schedule`.
- Che mặt / thân trên → toàn màn hình (luat-chung 4): chạy `overlay_guard.py` ở 7A; tít ghim che đầu người nói thì tự ẩn (selfie mặt cao — Haruku 86/95 mốc).

## 2026-11-04 — TÁI CẤU TRÚC (David: "tách nhỏ để sửa một chỗ")
- Kiến trúc 5 lớp: nguyen-tac · nhan-dien · ho-so (tham số từ hình mẫu, script + khung dựng đọc) · khoi (18 khối, nội dung SKILL.md cũ chuyển nguyên văn vào) · thu-vien-hinh (một bộ thành phần hình) + mau-chuan (kiem-mau.py). SKILL.md thành công thức mỏng (thứ tự khối, bảng phụ thuộc, tiêu chí đạt).
- 2 TRẠNG THÁI: cảnh `illus` (single/flow/vs/count/list, nhãn ≤ 3 chữ) ở cả 2 khung dựng; lớp chữ đè người tự vẽ toàn màn hình ≤ 4 s; thẻ/hành động bỏ câu trích dài; tít ghim tắt (hồ sơ highlight `tit_ghim: false`). +11 biểu tượng. Sao lưu trước tái cấu trúc: `~/.claude/skills/dung-video.bak-2026-11-04b`.

## 2026-11-06 — clip DJI_16
- Nhạc + tiếng hiệu ứng highlight tính theo giọng như video dài; bỏ tiếng ký hiệu khi vào lời ngay giây 0 (đo Clip 1: lúc ngừng nói −19,5 dB, đang nói −17 dB; file thu −35 LUFS).
- Podcast đồ hoạ dọc: chữ chính thay phụ đề (phương án B, David chọn sau khi thấy phụ đề + đồ hoạ bị rối).
- 2026-11-06: bỏ nút YouTube ở màn hình cuối clip dọc, ghi tên kênh thay vào. Chưa có bằng chứng chính thức về việc bị hạn chế, nhưng icon gần như không mang lại gì.
- 2026-11-06: David duyệt cả 3 clip "Đi trainer" làm mẫu cho các video sau; đã thêm vào `mau-chuan/mau.json`.
- Khuôn podcast đồ hoạ dọc: bỏ câu kêu gọi ghép và màn chốt bình luận (David thấy ép buộc, cụt cảm xúc), kết bằng màn hình cuối 3 s mời xem YouTube; nhạc thấp hơn giọng khoảng 23 dB (David nghe 2 mức, chọn mức này).
- Người xem clip là người xem độc lập; chấm riêng từng clip. David loại clip chỉ nói nỗi buồn.
- 2026-11-07: David thấy clip 39 giây xem riêng không hiểu gì. Luật gốc mới: clip đạt hai mục tiêu (chuyển hoá ngay trong clip, kéo sang bản dài) qua bốn câu `boi_canh`, `y_tron`, `mang_ve`, `chua_lai`. Claude tự chọn ý, không hỏi David chọn đoạn. Bỏ mọi số cố định về độ dài và số clip. Được ghép đoạn xa khi đúng mạch, phải báo mốc. `cut_highlight.py` dừng nếu thiếu `chon_y`.

## 2026-11-08 — clip người nói dọc đầu tiên (4 video cũ làm lại)
- Nguồn ngang có người nói cắt sang dọc: mặt chiếm gần hết nửa trên, nên `overlay_guard.py` đổi thẻ tít `y: 300` thành màn đen toàn khung (mất mặt ngay giây 0, chữ lệch sát mép trái). Cách làm: tít `keep: true`, bỏ `y` → neo vùng ngực ngay trên phụ đề, thấy rõ mặt.
- Chữ to `pow` giữa clip lặp đúng chữ phụ đề nhịp chữ và cũng bị đổi thành màn đen → bỏ. Điểm nhấn giữa clip dùng minh hoạ (`illus` vs/list/count) và màn hành động (`action`), từ khoá tô cam trong phụ đề.
- Bỏ tiếng ký hiệu đầu clip khi vào lời ngay giây 0 (đúng quyết định 06/11); `hl_edl.py` đã sửa: không thêm `sting`, tít tự `keep: true`.
- Chưa sửa: màn `pow` toàn khung của khung ghép (lề trái ~18 px thay vì 70 px, dải tối khác màu ở đỉnh). Nếu cần chữ to toàn khung, sửa `Show.jsx` trước.
- Câu màn chốt dài (cả đoạn HANHDONG ~250 ký tự) tràn đè phụ đề ở clip sự tập trung. `hl_edl.py` giờ cảnh báo khi > 55 ký tự; ghi `"cta_text"` (vế trọn ý, nguyên văn) vào câu `cta` trong phuong-an.json.

## 2026-11-08 — Phụ đề dọc cụm 5–8 chữ, mỗi lúc một chỗ chữ (David chốt)
- David: phụ đề 3–4 chữ cỡ 84 quá ngắn, quá to; đọc chữ motion graphic và phụ đề cùng lúc là rối. Đổi: cỡ 58 bằng chữ thẻ, chữ thường, viền mảnh, cụm trọn ý 5–8 chữ (≤ 2 dòng).
- Mọi lớp chữ motion graphic (pow, illus, action, chips, thẻ tít, màn chốt…) đang hiện → phụ đề nhường, hết lớp thì hiện tiếp đúng cụm (Show.jsx `nhuong`, Captions.jsx `LOP`).
- `hl_edl.py`: chia dòng bằng quy hoạch động (hết câu / dấu phẩy / trước từ nối; không ngắt sau "rất, của, là, những…"). Sửa lỗi chạy lại `hl_edl.py` nhân đôi khối `TS`.
- Chạy lại `hl_edl.py` sẽ ghi đè lớp phủ và `hl` sửa tay trong edl.js → lưu bản cũ, chép lại sau.
