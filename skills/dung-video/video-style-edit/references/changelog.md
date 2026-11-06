# Sổ thay đổi — video-style-edit (quyết định của người dùng + lý do)

## 2026-11-01
- Skill tạo từ dự án DJI (12 nghề). Phong cách mặc định: nền tối, nhấn cam, Barlow Condensed in hoa + Be Vietnam Pro — đã duyệt.
- Làm sạch: cắt thừa đầu/cuối + câu nói lại; KHÔNG cắt ngập ngừng/khoảng lặng ("muốn video thực tế nhất").
- Đổi khung: dọc→ngang = video giữa + chữ hai bên (pillar); ngang→dọc = khung bám người nói, nhảy cắt.
- Bỏ màn hình nguồn ảnh 5 s cuối → `nguon-anh.txt`. Bỏ nhãn kỹ thuật (×1,6, slow-mo).
- Phụ đề đầy đủ ở đáy vùng an toàn; lớp phủ thu 78% ngay trên phụ đề. Chữ hiệu ứng chỉ trích, không diễn đạt lại ("Haruku").

## 2026-11-02
- **Lớp phủ không được che người nói**, vị trí không cố định → `face_place.sh` (dò mặt Vision, neo đáy/đỉnh). Nguyên nhân: video
  IMG_0499 quay trong xe, thẻ ở đáy che cằm/miệng.
- **Dự án CapCut** khi được yêu cầu → `build_capcut.py` (pycapcut). CapCut Mac đọc `draft_info.json` + đường dẫn kiểu
  `/Users/<tên>/Movies/CapCut/...`; phụ đề là chữ CapCut, font Be Vietnam Pro (người dùng thích font này). Đã mở được.
- Template thêm kiểu cảnh: card `vs`, `ages`, `quote`; `steps` có nhãn `n`; montage `kicker`; toàn màn hình `gens`, `build`.
- Template dùng chung với skill mới **podcast-style-edit** (Stage, Timeline, podframe, FullScreenLand) — chỉ bật khi `project.podcast`.
- **Chữ to tiếng Việt đủ dấu, không chồng dòng** (`VN` trong podframe.js) bật cho cả skill gốc: giãn dòng 1,14, chừa chỗ dấu
  theo cỡ chữ, chữ to ≤ 120 px, hook ≤ 118 px. Đã thử trên IMG_0499: vẫn gọn trong dải lớp phủ.
- `render_preview.py` ghép `bia.mp4` (nếu có) trước video — dùng cho bìa podcast (`COVER`, `Cover.jsx`).
- **Chữ to sau một dòng khác chừa chỗ dấu** (`aboveGap` = 0,4 cỡ chữ) và chữ không đặt sát khung ảnh — người dùng chỉ ra
  "GỐC RỄ" đè dòng "Phải nuôi đến cả năm trời", dòng đó chạm ảnh. Áp cho montage (dọc + ngang), tên người nói, "BƯỚC n".
- **Lớp phủ không bao giờ đè/chui dưới phụ đề**: mép chặn cứng ở đỉnh dải phụ đề trong `Place` (người dùng chỉ ra ô bị phụ đề đè).
- **GIỮ Ô CHỮ HIGHLIGHT** (thẻ, chữ to) — đã thử thay toàn bộ ô chữ tóm ý bằng hình động (biểu tượng + mũi tên + ✓/✗, chữ chỉ còn
  tên riêng và số; bản thử `~/Movies/edit-img3196-hinh-dong`). Người dùng xem và **không ưng bằng bản ô chữ**: "vẫn nên để ô
  highlight chữ thì đẹp hơn". → KHÔNG đề xuất lại kiểu chỉ-hình-động; biểu tượng vẽ chỉ dùng thay ẢNH trong thẻ/montage.
- **Thẻ = màn hình toàn cảnh** (sau khi giữ ô chữ): người dùng muốn mọi ô thẻ thành một màn toàn cảnh có hình động (giống tinh
  thần cảnh "cái quả", không bắt chước y hệt) — chỉ ô thẻ; chữ to không nền, hook, tên người nói vẫn trên video. Chữ trên màn
  toàn cảnh = **nguyên văn đầy đủ** câu nói ("không được tự tóm tắt hay nói ý khác") vì toàn cảnh dễ đọc. Mỗi cảnh 4–8 s (người
  dùng chọn rút ngắn để mặt vẫn hiện ~60%). Code: `CardFull.jsx` (dùng lại variant thẻ, `CardInline`), `card` trong `FULL`.
- **Tinh gọn** (người dùng: "tối giản và tinh gọn nhất nhưng vẫn thể hiện được ý chính"): phụ đề ẩn khi thẻ toàn cảnh hiện câu
  nguyên văn (không đọc 2 lần); khung thẻ có quote chỉ giữ hình động + nhãn; ~1 hiệu ứng / 15–20 s, chữ to ≤ 3–4 lần, nghỉ ≥ 5 s
  giữa hai cảnh chữ; podcast: ý đang bàn đổi 40–90 s. Lý do: bản Haruku 22 cảnh / 4:28 + phụ đề + câu trích = quá nhiều chữ.
- Khe giữa 2 dòng chữ to nới 0,1 → 0,24 cỡ chữ (dấu dòng trên/dưới chạm nhau ở "ý đang bàn" podcast); áp cho sân khấu, chữ to,
  bìa, nhãn tự xuống dòng; ô màu hook giữ khe nhỏ.
- **Một chuẩn hiển thị cho mọi chế độ**: phụ đề chế độ ghép trước là chữ rời không nền, các dòng dính nhau → giờ đọc chung
  `subStyle.js` với chế độ 1 video/podcast (hộp nền tối, giãn 1,28, đáy vùng an toàn); chữ to ở chế độ ghép (Rise, chữ nổ,
  lời kết, tiêu đề) dùng cùng chuẩn chừa dấu/giãn dòng. Khung trích dẫn clip giữ nguyên (người dùng khen chuẩn).
- **Minh hoạ mặc định = biểu tượng vẽ** (`Icons.jsx`, ~45 hình) thay ảnh; người dùng so sánh 2 bản DJI và chọn bản không ảnh. Ảnh
  thật chỉ cho: địa danh cụ thể, nhân vật có thật/lịch sử, tư liệu quá khứ, minh chứng xác thực, sản phẩm cụ thể. Số liệu
  luôn bằng hiệu ứng, đúng con số người nói.
- **Nâng khung** (dự án ghép 9515): nhiều đoạn nhân vật tụt xuống nửa dưới, nửa trên trống, phụ đề/thanh nút che mất hình chính →
  đẩy hình lên ≤ 400 px + đáy lấp hình mờ (phóng ≤ 1,25× khi cần hơn). `scripts/lift.py` tự tính theo mặt; chế độ ghép → `lift.js`
  (đặt tay `lift` trong edl.js cho đoạn đồ vật), chế độ 1 video → nung vào video_goc.mp4 sau bước làm sạch (3b').
- **Mục tiêu video = hiểu + làm theo** (người dùng chốt): câu hành động trong lời → màn `action` tự sinh (biểu tượng + tick + nguyên
  văn câu); MỌI video kết bằng màn chốt `cta` ~4 s ("David rất mong có được sự góp ý của bạn tại phần bình luận!", cta.js) — hình
  lùi vào khung để vẫn thấy vẫy tay/like. Lý do: đánh giá cho thấy video giúp hiểu nhưng chưa thúc người xem hành động.
- **Câu màn chốt không cố định** (người dùng chốt): Claude tự sáng tạo câu chốt hợp từng video sau khi nắm nội dung — một hành động (bình luận/lưu/theo dõi/chia sẻ, biểu tượng theo kiểu), giọng David, không bịa; câu cố định trong cta.js chỉ còn là dự phòng.
- **Tick + "ting" ở màn chốt** (người dùng yêu cầu): câu chốt hiện xong → dấu tick nhỏ bật nảy ở góc biểu tượng + tiếng chuông ting (assets/sfx/ting.wav, tự tổng hợp, không bản quyền) để kích thích người xem hành động.

## 2026-11-03 — ghép nhiều clip: thời lượng theo nội dung
- Người dùng chốt: thời lượng video ghép **tự cân theo nội dung**, không cắt theo tỉ lệ/con số mặc định — có khi chỉ giữ 50%
  (quay trong túi, đen xì, cảnh không rõ), có khi giữ 100% (cảnh nào cũng rõ, không trùng). Ghép ≠ highlight: không tự rút
  thành bản 3–5 phút hay video ngắn. Bỏ trùng lặp theo bước 2b sẵn có.
- **Tiêu chí giữ/bỏ cảnh** (Claude đề xuất, người dùng chốt 5 điểm) → multi-clip.md mục 2c: ưu tiên cảm xúc > câu chuyện >
  nhịp > hình đẹp; người khác trong khung giữ hết ("vlog không chỉ một mình mình"); đoạn trầm quá thì tua (video cần nhịp);
  quay lại cùng câu/cảnh → Claude tự chọn lần tốt nhất; có cảm xúc là giữ dù rung; cảnh tâm linh giữ, **tông bắt buộc khớp cảnh**.

## 2026-11-03 (học từ 10 Shorts top lượt xem — xem cat-highlight-video/references/hoc-tu-top-video.md)
- Chế độ ghép clip: nhịp cắt mục tiêu, cảnh phản ứng, viền ô phụ đề theo người nói (`who` trong `SUB`), bằng chứng thật cho
  kết quả/con số (multi-clip.md mục 2c, 4). Thẻ cuối `ENDCARD` cho highlight (mục 10). Vị trí phụ đề KHÔNG đổi (người dùng chốt).

## 2026-11-04 (vlog leo núi — người dùng chỉ ra sau khi xem bản render)
- Thẻ địa điểm đè phụ đề 2 dòng (Location top 1060 cố định). Montage Show.jsx: thêm `CAP_H = 140` / `CAP_TOP` / `LOW_Y` (như
  CAP_H chế độ 1 video); Location, NameCard, Replay canh ĐÁY vào `LOW_Y`; Chips mặc định tính từ `LOW_Y`.
- 4:15–4:33 (c13 119,5 s→hết): giữ vì có lời hỏi đường, nhưng hình còn trong túi rồi lật ngang/lộn ngược → phải cắt.
  bad_frames.py: ngưỡng TÚI/CHE 30 → 60 (clip thường không khung nào < 60), gộp khoảng cách < 1 s. vlog_edl.py: ⚠ khi đoạn giữ chạm
  bad.txt + tờ soát `check/segs/` 1 khung/giây, xem hết trước render. Luật: hình hỏng thì bỏ kể cả có lời.

## 2026-11-04 (khung vlog theo kênh Jessie Luong — người dùng chọn làm chuẩn)
- Học 13 vlog của kênh (2021 → 2026), theo kiểu GẦN ĐÂY: mở đầu = đoạn ghép 9–20 s cảnh đắt nhất cả chuyến + thẻ tiêu đề trên đoạn
  ghép, rồi chào + bối cảnh, hành trình theo thời gian, kết bằng lời tổng kết của người quay. Claude tự chọn kiểu 1/2 theo nội dung.
  multi-clip.md 2d; vlog_edl.py `intro` (cảnh m1…, `voice`, `{"montage": true}` cho kiểu 2), tiêu đề `over` (nền mỏng) tự nằm ở dải
  cảnh câm. Luật: đoạn ghép đa dạng, ≤ 2 cảnh mặt cận (lần chạy thử đầu ra 6/9 cảnh selfie giống nhau).
- vlog_edl.py: biến `n` (đếm đoạn) bị ghi đè khi chia dòng phụ đề → trùng id đoạn (c12_2, c20_3…) → phụ đề/thẻ của đoạn trùng có thể
  lệch giờ (bản vlog leo núi đã render dính lỗi này). Đổi tên `nl`; id đánh số liên tục theo clip (clip tách hai mục vẫn không trùng).
- Nhạc đoạn ghép mở đầu vlog: 2 bài riêng `intro-soi` (Upbeat — alex-morgan) / `intro-lang` (Inspiring Documentary — AtlasAudio), Claude
  chọn theo nội dung (`intro.music`). Cảnh câm mặc định dài 2 phách, điểm vào bài canh cho mối cắt rơi đúng phách; nhạc to hơn ở dải
  cảnh câm (loudRanges). Không lấy nhạc của kênh mẫu (bản quyền / Content ID + luật không tải từ YouTube).
- render-show.mjs: `node render-show.mjs <từ s> <đến s> <tên.mp4>` render riêng một đoạn để xem thử.
- Tiêu đề trên đoạn ghép (`over`): một dòng gọn ≤ 130 px, canh đáy vào LOW_Y, bỏ nền lưới — chạy thử 3 video Haruku (toàn selfie,
  mặt ở nửa trên khung) thì tiêu đề 2 dòng 250 px che mặt. Vlog toàn cảnh tự quay mặt: đa dạng bằng nền / trang phục / cử chỉ.
- Độ dài intro không cố định (người dùng chốt): theo chất liệu + cảm xúc; chỉ cảnh thật sự khác nhau; video tự quay mặt nói ≈ 5–8 s
  (1 câu đắt + tiêu đề trên 1–2 cảnh). Intro Haruku 16,7 s → ~7 s.
- vlog_edl.py phụ đề (vlog Haruku 2026-11-04): (1) mốc TỪNG CHỮ khớp words.srt bằng difflib, chữ ngoài đoạn giữ bị bỏ — trước đó
  câu nối dài làm lọt chữ của đoạn đã cắt ("…tốt lành thật ra", "David xin chào…"); (2) nối dòng Whisper: chữ hoa không phải tên
  riêng (PROPER = chữ hoa giữa dòng) → câu mới ". "; (3) ngắt dòng ưu tiên khoảng ngừng giọng nói, cấm kết dòng bằng từ đệm/nối
  (END_BAD) và cấm tách cặp chữ lặp ≥ 2 lần / chữ trong `fix` (COMPOUND: bí mật, đi bộ, phạm trù…). Từ ghép chỉ xuất hiện 1 lần vẫn
  có thể bị tách ("giải / trình") — soát bằng mắt.
- Âm lượng vlog ghép (người dùng chỉ ra 2026-11-04, Haruku): (1) new_montage.sh cân GIỌNG từng clip về −20 LUFS (gain tuyến
  tính + alimiter, tối đa +18 dB) — 3 clip gốc −17 / −34 / −23 LUFS nghe đoạn to đoạn nhỏ; (2) vlog_edl.py đo giọng thật rồi đặt
  mức nhạc khi có lời thấp hơn giọng 20 LU (duck), chỗ ngừng nói ×1,6 (×2,5 nghe dập dình). Intro giữ mức `loud` 0,3.
- Hiệu ứng trong vlog ghép (người dùng chỉ ra: "không thấy hiệu ứng, animation"): plan.json `fx` — pow (chữ to trích lời, tự canh
  đáy LOW_Y), chips (danh sách hiện theo lời), action (thẻ câu hành động), zoom (dồn rồi tự nhả sau `hold` 2,5 s); ~1 / 20–30 s.

## 2026-11-04 — BỘ NHẬN DIỆN DAVID (người dùng chốt: "xem bất kỳ thể loại nào cũng nhận ra cùng một người làm")
- brand.json (remotion-template/src, một nguồn; new_montage.sh chép sang dự án ghép). Dấu góc ● DAVID │ chủ đề: BrandMark
  (Overlays.jsx → Captions 1 video, Stage podcast) + Hud (chế độ ghép, highlight người nói). Hook đổi sang khuôn tiêu đề chung (dòng
  nhỏ cam + gạch cam + chữ trắng/cam, bỏ ô nền màu). Tiếng ký hiệu sting.wav ở tiêu đề mở đầu (render_preview.py · vlog_edl.py · hl_edl.py).
- Video 1 người / podcast: nhạc kênh rất nhỏ (thấp hơn giọng 22 LU, `project.music` đổi bài / '' tắt) + loudnorm −14 LUFS bản cuối.
- Thẻ cuối nhận diện (chủ đề + DAVID, không nút phát) cho mọi video có chủ đề (endcard.js ENDCARD_ON); highlight giữ thẻ dẫn bản đầy đủ.
- Chế độ ghép: cảnh minh hoạ VẼ `scene` (Icons.jsx dùng chung, sed import → brand.js) — 3–4 cảnh / video, câu nguyên văn sáng dần.
- Chống chữ đè phụ đề TẬN GỐC ở chế độ ghép (người dùng: "bị rất nhiều lần rồi mà vẫn chưa khắc phục"): Chips neo đáy + tự thu cỡ một
  dòng; Show.jsx cắt mọi lớp không toàn màn hình ở CAP_TOP; phụ đề ẩn dưới mọi lớp toàn màn hình (FULLSCREEN); vlog_edl.py in lệnh chụp
  soát ở cuối từng lớp chữ. Chế độ 1 video (layout.js Clip) và podcast (PF.contentBottom) đã có chặn cứng từ trước.

## 2026-11-04 — NGƯỜI XEM LÀ TRUNG TÂM (David: "các kênh lớn là hình mẫu thành công đã đạt được điều này rồi thì sao chép luôn")
Sau bản đánh giá đối chiếu với kênh lớn (thể loại nói trước camera, highlight, vlog, podcast), David duyệt kế hoạch 5 pha:
- `luat-chung.md` (thư mục dung-video) — một nguồn luật chung; SKILL.md chỉ giữ luật riêng. `so-lieu-mau.md` — vòng số liệu sau 7 ngày.
- **Phát hành** mọi video: 3 tiêu đề + 2 thumbnail 1280×720 (`scripts/thumbnail.sh`, `assets/thumb-template/` — mặt có cảm xúc, ≤ 4
  chữ, nhận diện David; nguồn quay dọc tự thành khung một bên). Video ngắn không ghép bìa trước video.
- **Phụ đề video ngắn** 1–3 chữ to mỗi nhịp ngang ngực (`subStyle.js` `ShortLine`, chuẩn Hormozi/DOAC) — thay quyết định cũ "giữ
  phụ đề đáy" (bỏ đề xuất K ngày 03/11) vì David đổi kim chỉ nam. Video dài / vlog / podcast giữ hộp tối.
- **Làm sạch cắt khoảng lặng ≥ 0,45 s + tiếng đệm "ờ/ừm"** mặc định (`clean_suggest.py`, `loud05.txt` trong clean_analyze.sh) —
  thay luật cũ "không cắt ngập ngừng" (2026-11-01, "muốn video thực tế nhất"). Bản tự nhiên: `clean_analyze.sh <dự án> tu-nhien`.
  Vlog ghép giữ nhịp tự nhiên. Thử trên IMG3196 (46,7 s): 8 khoảng lặng 0,5–0,8 s được cắt.
- Montage (highlight): `SHORT` trong edl.js bật phụ đề nhịp chữ, bỏ chớp trắng ở mối cắt; `HL.bar = false` tắt thanh tập gốc.
- **Thumbnail chỉ khi video xuất NGANG và đăng YouTube** (David chốt cùng ngày: "chỉ có đăng video youtube thì mới cần ảnh bìa ngang, mà còn phải là video ngang"). Video xuất ngang → hỏi "có đăng YouTube không?" lúc đầu; video dọc chỉ có mốc khung bìa.

## 2026-11-04 (học 80 video Việt)
- Học 20 video nói trước camera + 20 vlog Việt (David duyệt ưu tiên 1+2): màn kết YouTube 15–20 s (`YtEnd.jsx`, `project.ytEnd`, plan.json `ytEnd`, nhạc kênh nhỏ trong render_preview.py / Show.jsx); thumbnail kiểu Việt (`THUMB_L3`, `THUMB_NUM`, `THUMB_BADGE`); nhãn số `listItem`; màu theo nghĩa `+`/`-` trong hl (subStyle.js); thẻ tóm tắt để lưu; `CHAPTERS` + `chapters.py`; `teaser.py`; vlog: kiểu mở 3 "nhiệm vụ", thẻ vòng chỉ cho vlog thử thách, flycam mở nơi mới, nhãn giá/con số, tách phần > 25 phút. Cảnh câm intro 2 phách ≈ 1,06 s đã đúng nhịp Việt — giữ. Chưa áp TH-1 (cắt lặng nhẹ hơn cho video dài) — chờ David.
- TH-1 áp (David duyệt): video > 3 phút chỉ cắt lặng ≥ 1,2 s còn 0,5 s, giữ tiếng đệm (clean_suggest.py); ≤ 3 phút giữ 0,45 s. PO-6: lịch phát `project.schedule` / plan.json `schedule` trên thẻ cuối + màn kết YouTube.
- Sửa sau khi dựng tờ mẫu (2026-11-04): phụ đề nhịp chữ giữ liền cụm từ khoá trong `hl` (không tách "TỎ / RÕ"), không gộp nhịp quá 16 ký tự (hết rớt dòng).
- **Che mặt / thân trên → toàn màn hình** (David chốt 2026-11-04): face_place.py coi đầu + cổ + vai + ngực là vùng cấm; không chỗ trống → `full: true` + `end` ≤ 4 s trong placement.js (layout.js Place vẽ nền + phóng giữa, Root.jsx rút thời lượng). Chế độ ghép: `overlay_guard.py` → guard.js (Show.jsx `FullOv`), tít ghim che đầu thì ẩn. Thử Haruku: thẻ hook 1 video + thẻ tít highlight thành toàn màn hình, tít ghim ẩn (che đầu 86/95 mốc).

## 2026-11-04 — TÁI CẤU TRÚC (David: "tách nhỏ để sửa một chỗ")
- Kiến trúc 5 lớp: nguyen-tac · nhan-dien · ho-so (tham số từ hình mẫu, script + khung dựng đọc) · khoi (18 khối, nội dung SKILL.md cũ chuyển nguyên văn vào) · thu-vien-hinh (một bộ thành phần hình) + mau-chuan (kiem-mau.py). SKILL.md thành công thức mỏng (thứ tự khối, bảng phụ thuộc, tiêu chí đạt).
- 2 TRẠNG THÁI: cảnh `illus` (single/flow/vs/count/list, nhãn ≤ 3 chữ) ở cả 2 khung dựng; lớp chữ đè người tự vẽ toàn màn hình ≤ 4 s; thẻ/hành động bỏ câu trích dài; tít ghim tắt (hồ sơ highlight `tit_ghim: false`). +11 biểu tượng. Sao lưu trước tái cấu trúc: `~/.claude/skills/dung-video.bak-2026-11-04b`.

## 2026-11-05
- **Thumbnail / ảnh bìa chỉ dùng hình của CHÍNH video đang làm** (David chỉ ra: thumbnail podcast "Mục tiêu và sứ mệnh" lấy mặt từ vlog Miếu Bà Cam → sai). Podcast không mặt → nền là khung đồ hoạ của chính podcast; ảnh người nói chỉ khi David gửi riêng cho tập đó. Không đưa "lấy ảnh từ video cũ" thành lựa chọn khi hỏi. Ghi ở luat-chung 7, khối 14, podcast SKILL, thumbnail.sh.
- **Nhạc nền theo tuyến nội dung + nhạc nhỏ khi nói** (David: "nhạc nền hơi to… tông chưa phù hợp… phải tự chọn được nhạc theo tuyến nội dung"). Hồ sơ chung `nhac`: bảng tuyến → bài, `project.tuyen` bắt buộc (render_preview dừng nếu thiếu — bỏ mặc định soi-1); nén theo giọng tương đối (ngưỡng giọng − 14 dB, tỉ lệ 20, nhả 1,5 s): nhạc khi nói 17 → 30–33 LU dưới giọng. Tuyến kiến thức chờ David tải 1 bài ambient.

## 2026-11-06
- **Học từ HyperFrames + Motion Studio, không cài** (David duyệt): bỏ lơ lửng, vòng xoay, quầng nhấp nháy; ra ngắn hơn vào; kiểu vào theo ý câu (khối 07). Thêm sơ đồ `xay-tang`, `doi-trang-thai`, `chuyen-giao`. Thêm `scripts/soat_canh.mjs` (khối 17) và `scripts/chu_tren_man.mjs` (khối 03). Bản trước: `~/.claude/skills/dung-video.bak-2026-11-06-hoc-motion`.
