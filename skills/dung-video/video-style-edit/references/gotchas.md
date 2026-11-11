# Lỗi đã gặp và cách tránh

## Công cụ
- **ffmpeg của Homebrew không có `drawtext`** (không có freetype) → không viết chữ bằng ffmpeg; mọi chữ làm trong
  Remotion hoặc Pillow.
- **`python3 -I` tắt thư mục user-site** → Pillow (cài `--user`) không import được. Script cần Pillow
  (`credits_card.py --card`, `safe_guide.py`) chạy bằng `python3` thường; script khác chạy `-I` cho an toàn.
- `timeout` không có trên macOS — đừng dùng.
- Lệnh `rm` với biến: luôn `"${VAR:?}"` để không bao giờ xoá nhầm khi biến rỗng (Claude Code chặn dạng `rm -f "$X/$Y"`).
- npm báo `allow-scripts` cho esbuild → `npm approve-scripts esbuild` (new_project.sh đã làm).

## Video gốc lạ
- iPhone đã cắt khung (vd. 770×1368) hoặc 720p: component vẽ theo 1080×1920 → `clean_apply.py` tự phóng về khung
  chuẩn (tỉ lệ ≈ 9:16 thì đúng 1080×1920). Luôn chạy bước làm sạch, kể cả khi không cắt gì.
- Quay ngoài trời / micro điện thoại: lời nói chỉ to hơn nền ồn ~8–10 dB → ngưỡng cố định "nền + 12 dB" coi cả video
  là im lặng ("Không thấy lời nói thật"). Ngưỡng giờ lấy min(nền + 12, điểm giữa nền và lời nói).

## Remotion
- Cảnh chiếu lại video gốc (`bocuc` o-nguoi, `cta`) đọc khung từ file gốc lớn (1,6 GB) → quá hạn chờ 28 s khi máy bận. render.mjs
  đã đặt `timeoutInMilliseconds: 240000`, 2 luồng cho cảnh có video; lỗi giữa chừng thì `TIEP=1 node render.mjs` chạy tiếp. Render
  mỗi lúc MỘT dự án (8 GB RAM).
- Không đặt `"type": "module"` trong package.json — import không đuôi (`./scenes`) sẽ hỏng.
- `defaultProps` phải là dữ liệu thuần (JSON) — truyền tên loại cảnh (`type`), không truyền component/hàm.
- Chữ trong khung `overflow: hidden` (hiệu ứng trồi lên) **cắt mất dấu dưới** (ạ, ợ) → thêm `paddingBottom` + `marginBottom` âm.
- Chờ font bằng `delayRender` + `document.fonts.load` (đã có trong Root.jsx); thiếu thì khung đầu dùng font dự phòng.
- 8 GB RAM: `concurrency: 4`. Lần đầu chạy tải Chrome headless (~100 MB).
- Chữ to (kinetic, hook) tự co cỡ theo dòng dài nhất (≈ 0,46 em/ký tự với Barlow Condensed in hoa có dấu) → không xuống
  hàng lẻ; đổi font thì đo lại hệ số.
- Chữ dài tự xuống dòng → đè lên phần tử bên dưới. Component nên tự giảm cỡ chữ theo độ dài; luôn kiểm tra bằng ảnh chụp.

## Ảnh (Openverse / Wikimedia)
- Openverse chậm, hay timeout 30 s → timeout 90 s, thử lại, tuần tự.
- Openverse có lúc sập hẳn (mọi lượt quá giờ) → `openverse.py` tự chuyển sang API Wikimedia Commons (lọc bỏ NC/ND,
  ảnh < 1000 px); từ khoá nên cụ thể, có tên địa danh ("Tokyo street pedestrians" ra ảnh, "walking shoes" trả rỗng).
- **Wikimedia trả 429 cho urllib của Python** và cho tải song song → dùng curl, tuần tự, nghỉ 0,4–0,5 s.
- Wikimedia chỉ cho độ rộng thu nhỏ chuẩn (500, 960, 1280); độ rộng lạ trả 400.
- Không đưa email/tên người dùng vào User-Agent.
- Ảnh có người nổi tiếng dễ nhận ra (vd. vận động viên hút xì gà) → bỏ. Clip-art giữa ảnh chụp → lạc tông, bỏ.
- Ảnh CC BY / BY-SA bắt buộc ghi nguồn → `nguon-anh.txt` để dán vào mô tả bài đăng (video không có màn nguồn ảnh cuối).
  Cách ghi nguồn này hợp lệ khi video đăng kèm mô tả; nhắc người dùng dán vào mỗi lần đăng.

## ffmpeg ghép video
- `split` một ảnh lặp vô hạn ra nhiều nhánh → bộ nhớ phình to → làm sẵn ảnh có alpha thay vì ghép mask lúc chạy.
- Clip ProRes 4444 alpha: `yuva444p10le`; overlay bằng `setpts=PTS-STARTPTS+<giây>/TB` + `eof_action=pass`.
- Âm thanh gốc 44,1 kHz + đoạn câm 48 kHz → `aresample=48000` trước `concat`.
- **`anullsrc` mặc định là u8 (8-bit)** → `concat` với tiếng gốc hạ CẢ bài xuống 8-bit + dither → tiếng rè/xì suốt video
  (dải > 12 kHz tăng ~11 dB; rõ nhất ở bản thu nhỏ tiếng). Luôn `aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo`
  cho MỌI nhánh audio trước `concat`/`amix`. Kiểm: năng lượng `highpass=f=12000` của bản cuối ≈ bản gốc (±1 dB).
- Mốc thời gian luôn làm tròn về khung (`round(sec * fps)`) ở mọi nơi (scenes, timeline, preview) để khớp nhau.
- 17 clip ProRes ≈ 2 GB — báo người dùng về dung lượng.

## Làm sạch video gốc (chế độ 1 video)
- **Video cũ của kênh cũ**: hay có **chữ / viền in cứng vào hình** — dải tên tập + ngày + website ở đáy
  (từ dòng ~902/1080), viền trắng bo góc sát mép (~40 px). Luôn xem 1 khung ở giữa video **cỡ lớn** trước khi dựng; có thì cắt
  khung 16:9 bên trong rồi phóng lại 1920×1080 (`crop=1592:896:200:0` cho dải đáy; `crop=1808:1017:56:31` cho viền), làm TRƯỚC face_place.
  Màn tít mở đầu cũ ("PODCAST TẬP 4…") + lời chào/giới thiệu kênh cũ → cắt (luat-chung mục 2, làm lại video cũ).
- **Whisper chép ảo** cả bài một câu ("Hãy subscribe cho kênh Ghiền Mì Gõ…") ở video có tiếng trầm/nhạc mở đầu → clean_analyze.sh tự
  chép lại với tiếng đã lọc (`highpass=f=120,dynaudnorm`); còn ảo thì thêm `-mc 0` (tắt ngữ cảnh) và chép riêng đoạn đầu rồi ghép.
- Chỉ cắt vài đoạn (lời chào) ở video dài → **không chép lại** bản sạch: `doi_moc_loi.py "$P"` dời lời bản thô sang mốc bản sạch.
  Đặt mốc cắt ở khoảng lặng thật (đo RMS 50 ms), không theo mốc từ của Whisper (lệch ~0,3–0,5 s → lẹm chữ "Đò").
- Bản thô đổi tên thành `video_goc_raw.<ext>` TRƯỚC khi ghi `video_goc.mp4` — macOS coi `video_goc.MP4` và
  `video_goc.mp4` là một file, ghi thẳng sẽ đè mất bản gốc đang đọc.
- Mốc trong `cuts.json` luôn là mốc **bản thô**; mốc trong scenes.js là mốc **bản sạch** — quy đổi qua `segments.json`.
- Whisper kéo dài mốc cuối từ vào khoảng lặng → tìm khoảng lặng bằng `silencedetect` (ngưỡng = nền ồn + 12 dB),
  không bằng khoảng cách giữa các từ.
- Mỗi đoạn có fade âm 15–30 ms ở hai đầu, không thì mối cắt kêu "tách".
- ffmpeg 8 bỏ `-filter_complex_script` → dùng `-/filter_complex <file>`.
- libx264 1080×1920 trên máy 8 GB mất ~18 phút cho 3,5 phút video; `h264_videotoolbox -b:v 20M` chỉ ~1,5 phút.
- Câu "giống câu trước" chưa chắc là nói lại: "master… → siêu cao thủ…" là người nói giải thích lại có chủ ý → giữ.

## Đổi khung (dọc ↔ ngang)
- Component luôn vẽ trên toạ độ khung dọc 1080×1920; khung ngang chỉ do `layout.js` (Place) thu/đặt lại → đừng sửa
  toạ độ trong component cho khung ngang. Loại cảnh toàn màn hình mới phải thêm vào `FULL` trong layout.js.
- Pillar: `Scrim` tự tắt (nền hai bên đã tối); `hai-ben` render H.264 đặc (không alpha) ~1,3× thời lượng video.
- Dò mặt: Vision (`faces.swift`) — biên dịch lần đầu ~2 phút, lưu ở `~/.cache/video-style-edit/faces`.
- Khung cắt dọc đổi vị trí bằng `sendcmd` + `crop@rf x` (crop nhận lệnh x); đường dẫn file lệnh không được có dấu `:`.
- Người nói đoán theo độ cử động miệng (độ lệch chuẩn của độ mở môi trong câu) — hai người cùng cười/nói chen nhau
  dễ sai → shot `?` trong plan.md phải đọc câu nói để quyết.
- `check_frames.sh` với mốc vượt thời lượng video → lỗi "Could not open encoder" và giữ sheet CŨ; mốc phải < thời lượng.

## Nội dung chữ
- Né tên riêng chưa chắc chính tả bằng cụm chung chung (viết "ĐI BỘ MỖI NGÀY" chứ không "HARUKU") → người dùng thấy minh hoạ
  sai ý. Hiện đúng tên theo Whisper + hỏi chính tả trong báo cáo.

## Vị trí lớp phủ (không che người nói)
- Dải lớp phủ cố định ở đáy che cằm/miệng khi quay selfie trong xe, cầm máy thấp (mặt nằm ở y ~860–1170 trên 1920) →
  người dùng chốt: hiệu ứng không toàn màn hình **không được che nhân vật**, vị trí không cố định. `face_place.sh` dò mặt
  (Vision, 2 khung/giây) → `placement.js`; ưu tiên 2 điểm neo (đáy/đỉnh) để các cảnh không nhảy vị trí lung tung.
- Vision cho khung mặt không gồm tóc/cổ → script nới lên 0,4 chiều cao mặt và xuống 0,25; lấy phân vị 5–95% của cả cảnh
  (đầu lắc qua lại). Đoạn không thấy mặt (quay màn hình xe, cảnh đường) → giữ vị trí mặc định.
- Selfie vừa đi vừa quay (IMG_3196): mặt to (cao ~440 px) và nhún liên tục → đệm cổ 0,25 mặt + phân vị 95% làm mọi cảnh
  báo "che mặt". Khung Vision kết thúc ≈ cằm → giờ đệm 0,06 mặt, phân vị 93%, cho thu tới 55%. Thẻ ở 55–60% chữ khá nhỏ —
  cảnh nhiều chữ nhỏ nên đổi sang chữ to/biểu tượng hoặc cảnh toàn màn hình.
- `face_place.py` đọc `FULL` trong layout.js: dòng FULL có nhánh điều kiện (`...(project.podcast ? [] : ['card'])`) → phải lấy
  mọi tên trong cả dòng (đã sửa); đọc thiếu thì thẻ toàn cảnh bị coi là lớp phủ và báo "che mặt" sai.
- Đổi mốc cảnh mà quên chạy lại `face_place.py` → cảnh mới không có trong placement.js → về vị trí mặc định (có thể che mặt).

## Chữ tiếng Việt (chữ to)
- Barlow Condensed in hoa, `lineHeight` ~1 + khung `overflow: hidden` chừa cố định 34/30 px → ở cỡ 140–150 px dấu chồng dòng dưới
  chạm dòng trên ("NGẪU", "NHIỀU"), dấu nặng bị cắt ("BỊ" → "BI"). Đã sửa cho CẢ HAI skill bằng `VN` (podframe.js: giãn 1,14, chừa
  0,5 em trên / 0,32 em dưới; chữ to ≤ 120, hook ≤ 118). Component chữ to mới phải dùng `VN`. Luôn soi ảnh chụp phóng to Ầ Ễ Ỗ Ị Ự.

- **Hai dòng chữ to xếp chồng** cần khe `VN.gap` = 0,24 cỡ chữ (trước 0,1): dấu nặng dòng trên + dấu chồng dòng dưới chạm nhau
  ("MỘT NGÀY" / "RẤT LÀ ĐẶC BIỆT" — dấu dưới Ộ chạm dấu Ấ, người dùng chỉ ra). Nhãn có thể tự xuống dòng dùng
  `lineHeight: VN.lh + VN.gap`. Ngoại lệ: dòng nằm trong ô màu (hook) đã có đệm riêng → khe 0,06 (khe lớn đẩy ô lấn sóng âm).
- **Chữ to đứng ngay sau một dòng/khối khác** (kicker, vạch màu, "BƯỚC n", khung ảnh) phải chừa phía trên `aboveGap(size)` =
  0,4 cỡ chữ cho dấu chồng — đã gặp (IMG_3196, cảnh "cái cây"): "GỐC RỄ" đè lên dòng "Phải nuôi đến cả năm trời", và dòng đó
  lại chạm mép dưới khung ảnh (chữ đặt sát mép ảnh). Montage dọc giờ: ảnh y 440–1010, chữ bắt đầu 1044 (cách ảnh 34 px), chữ to
  ≤ 120. Viết component mới: không xếp chữ to ngay dưới chữ khác bằng margin cố định nhỏ; luôn chụp thử khung có Ố Ễ Ỗ.

- **Lớp phủ tràn xuống dải phụ đề**: ô có nội dung cao hơn dải lớp phủ (435 px trong toạ độ component) → khi đặt sát trên phụ đề,
  phần thừa nằm dưới phụ đề (người dùng chỉ ra: "10 TRIỆU" bị phụ đề đè). `Place` giờ có mép chặn cứng (`Clip`) ở đỉnh dải phụ
  đề (dọc tự quay y 1280; podcast `PF.contentBottom`). Mép chặn chỉ là lưới an toàn: phần tràn sẽ bị CẮT — component phải tự
  vừa dải (CardShell có maxHeight); chụp thử thấy chữ/hình bị cắt ở đáy → rút nội dung hoặc giảm cỡ.

## Template dùng chung với podcast
- `podframe.js`, `Stage.jsx`, `Timeline.jsx`, `FullScreenLand.jsx`, `Icons.jsx`, composition `nen` thuộc skill podcast-style-edit;
  mọi nhánh podcast chỉ bật khi `project.podcast`. Sửa template → chụp thử cả một dự án tự quay (vd. edit-img0499) lẫn một
  dự án podcast (dọc + ngang) trước khi coi là xong.
- `theme.js`: SAFE dọc cố định (bottom 1420, rộng 830) — đúng cho mọi dự án dọc 1080×1920 (clean_apply luôn đưa về khung này).

## Phụ đề
- Lần chạy Whisper theo từ (`-ml 1`) và theo câu cho kết quả khác nhau; cả hai đều có thể đè câu bịa lên câu thật cuối
  video ("Hãy subscribe cho kênh Ghiền Mì Gõ…" ở chỗ David nói "Xin chào") → đối chiếu lần chạy ở `check/clean/`.
- Khung chữ phụ đề rộng ~37 ký tự ở cỡ 42 px; dòng dài hơn thì `textWrap: 'balance'` chia đều 2 dòng, tránh rơi 1 chữ.

## Giao tiếp
- Người dùng không xem được video trong khung chat → gửi file bằng SendUserFile và mô tả cảnh theo mốc thời gian.
- Mật khẩu, tải video từ mạng: `../../luat-chung.md` mục 8.

## Chế độ ghép nhiều clip
- **macOS không phân biệt hoa/thường tên file**: `Show.jsx` và `show.js` là MỘT file → import nhầm, lỗi
  "A value of `undefined` was passed to the `component` prop". Đặt tên khác hẳn (Show.jsx + edl.js).
- **Whisper bịa câu khi không có lời** ("Hãy subscribe cho kênh Ghiền Mì Gõ…" lặp cả clip) → so với `loud.txt`,
  cắt đoạn có tiếng rồi chạy lại với `-mc 0`.
- Clip iPhone có metadata xoay (−90°): ffmpeg tự áp khi chuẩn hoá (new_montage.sh) → luôn dùng `public/clips/cN.mp4`,
  không đưa .MOV gốc vào Remotion.
- Đoạn máy cầm ngang: xoay riêng bằng `transpose=2` (mặt đất bên trái → xuống dưới) hoặc `transpose=1`, kiểm bằng 1 khung.
- Remotion 4.0.5xx: `startFrom` đã đổi tên thành `trimBefore` (OffthreadVideo, Audio).
- Hiệu ứng + nhạc + tiếng gốc dễ chạm 0 dB → render-show.mjs tự loudnorm (−14 LUFS, đỉnh −1,5 dB).
- zsh KHÔNG tách biến chưa trích dẫn thành nhiều đối số: `node preview.mjs $ARGS` truyền cả chuỗi làm 1 đối số → dùng `${=ARGS}`.
- zsh: `$n:l…` trong chuỗi bị hiểu là modifier (`:l` = chữ thường) → viết `${n}` khi ngay sau là dấu `:`.
- `glob` của ffmpeg sắp chữ cái (11.8 trước 2.3) → ghép sheet bằng `ls | sort -n`.
- Toạ độ ước từ ảnh thu nhỏ dễ sai; lấy bằng khung có lưới `drawgrid` ở đúng mốc giây trong clip.
- `node stills.mjs` đôi khi báo "Timed out … connect to the browser" lần đầu (Chrome headless khởi động chậm) → chạy lại là được.
- Contact sheet 24 khung của clip ngắn (8 s) có bước 0,34 s — đừng ước mốc theo số thứ tự khung như clip dài; tính lại `t = i * DUR/24`.
- Render cả video lỗi "delayRender … Fetching …/proxy?src=…cN.mp4 … not cleared after 28000ms" / "ECONNRESET": bộ trích
  khung quá tải với clip dài + concurrency 4 → render-show.mjs dùng concurrency 3, timeoutInMilliseconds 120000,
  offthreadVideoThreads 2 (đã sửa trong template).

## Nâng khung (lift.py)
- Mốc mặt dò 2 khung/giây; người đi nhanh có thể lệch — luôn xem 1–2 khung sau khi nâng. Mặt gần đỉnh (đỉnh đầu < 230) thì
  script tự giảm mức nâng; nếu cả hai đầu đều chật (mặt to chiếm cả khung) → không nâng được, để nguyên.
- edl.js đọc bằng `node --input-type=module` — lỗi cú pháp edl.js (thiếu dấu phẩy sau chú thích cuối dòng) làm lift.py báo
  CalledProcessError; chạy `node -e "import('file://…/edl.js')"` để thấy dòng lỗi.
- `cite` có `{label: undefined}` → JSON thành `{}`: kiểm `'cite' in s`, đừng `s.get('cite')`.

## Highlight (dùng chung template với cat-highlight-video)
- `motion/src/highlight.js` = null ở mọi dự án thường; có dữ liệu (hl_apply.py) thì phụ đề hiện thanh tập gốc + hiệu ứng tua
  (Tua.jsx, chỉ khi bật `--tua`) và render_preview.py trộn `assets/sfx/tua.wav`. Sửa Captions/Timeline → chụp thử cả dự án thường lẫn highlight.
- render_preview.py: chỉ số đầu vào của màn nguồn ảnh phải đếm sau mọi tiếng hiệu ứng (trước đây cố định n + 1 → sai khi có ting).
- Highlight ở video người nói: phụ đề lên 40 px nhường thanh tập gốc → dải lớp phủ phải dừng sớm 40 px (CAP_H = 180 trong layout.js
  + face_place.py khi highlight.js có dữ liệu), không thì ô chữ (hook) chạm phụ đề 2 dòng (gặp ở IMG_3196). Sửa CAP_H ở một nơi → sửa cả hai.
- Highlight người nói dựng bằng montage-template: sửa `Show.jsx` phần `HL/TONE/MUSIC.tracks/jump` → chụp thử cả
  một dự án vlog thường (`edit-vlog-nhan-xe`) để chắc không đổi gì khi `HL = null`.
- Nhạc Pixabay to nhỏ rất khác nhau (−9 … −20 LUFS) → `gain` theo bài (hl_edl.py / hl_apply.py `GAIN`), đo lại khi thêm bài.
- Pixabay chặn tải bằng curl / fetch thẳng CDN (403) — nhờ người dùng bấm "Free download"; không lách.

- new_montage.sh: lưới khung mỗi 13 s — phần dư cuối < 0,6 s (clip 13,17 s) không ra khung nào → ffmpeg lỗi, cả dự án dừng (gặp ở vlog leo núi 48 clip) → bỏ phần dư đó.
- Montage: lớp chữ toạ độ cố định (thẻ địa điểm top 1060…) đè phụ đề 2 dòng → canh đáy vào `LOW_Y`.
- Hình lật ngang/lộn ngược lúc rút máy khỏi túi có độ sáng/độ tương phản/YDIF như cảnh đi bộ thường → không dò bằng signalstats;
  chỉ bắt được bằng mắt trên `check/segs/` (c13 vlog leo núi).
- Remotion `bundle()` chép CẢ `public/` (clip gốc) vào thư mục tạm mỗi lần chạy, không tự xoá → vlog 48 clip: 205 bản sót, đầy ổ,
  render kẹt/ENOSPC. Mọi script render/stills giờ `fs.rmSync(serveUrl)` ở cuối; script tự viết thêm cũng phải dọn.
- Chữ đè phụ đề lặp nhiều lần (thẻ địa điểm, danh sách `chips`): nguyên nhân chung = đặt vị trí bằng ƯỚC
  chiều cao (top cố định, n × cỡ chữ) trong khi chữ dài tự xuống dòng. Luật: lớp chữ KHÔNG BAO GIỜ đặt `top` ước lượng — neo ĐÁY
  vào LOW_Y (translateY(-100%)) để khối mọc lên; chữ một dòng thì tự thu cỡ theo mục dài nhất; Show.jsx chặn cứng mọi lớp không
  toàn màn hình ở mép trên dải phụ đề (lưới an toàn, như layout.js chế độ 1 video / PF.contentBottom podcast). Chụp soát ở CUỐI mỗi
  lớp (vlog_edl.py in sẵn mốc), không chụp lúc mới hiện.
- Sửa `thu-vien-hinh/` khi dự án ĐÃ tạo: dự án giữ bản chép thật (`cp -RL`) → chép file vừa sửa vào `<dự án>/motion/src/lib/` rồi mới chụp/render (đã gặp: Illus lưới 2 cột chưa vào dự án VF3).

## Điểm nhấn trên người `nhan`
- Selfie vừa đi vừa quay: mặt xê dịch 30–40% chiều ngang trong một cảnh → đặt chữ theo trung vị mặt sẽ đè mặt. `nhan_place.py` ghi
  khoảng mặt (`l`, `r` = phân vị 10/90 suốt cảnh), Nhan.jsx đặt chữ ngoài khoảng đó + chừa 0,3 bề rộng mặt.
- Khung ngang KHÔNG đặt chữ dưới cằm (đè miệng + phụ đề). Hết chỗ → chữ tự thu cỡ cho vừa; chữ dài thì ngắt 2 dòng (≤ 9 ký tự / dòng) để giữ cỡ to.
- Chụp thử `nhan` bằng preview.mjs không thấy zoom (zoom làm ở render_preview.py) → soát trên video-final.mp4 ở vài mốc trong cảnh.

- **Bố cục "người thu vào ô" (khung ngang): thẻ chữ canh giữa vùng trống bị đẩy lên đè dấu góc kênh** (BrandMark ở top 228 px) khi thẻ cao. Vùng nội dung giờ bắt đầu từ `max(SAFE.top, 320)`. Soát bằng ảnh rải đều cả video, không chỉ ảnh giữa cảnh.

### Lỗi khung ngang David chỉ ra (4 video cũ làm lại)
Gốc chung: template dựng cho khung dọc trước; các video ngang trước đó đều là podcast (dấu góc nằm trong sân khấu), nên khung ngang
người nói chưa từng chạy với dấu góc. Không do bài học video mẫu xoá gì; riêng `BoCuc.jsx` (từ bài học) đã chép số 300/320 theo giả định cũ.
- **Dấu góc thấp:** `top: 228` là số của khung dọc, dùng luôn cho khung ngang (21% chiều cao). Nay `BRAND_TOP` theo khung (`theme.js`).
- **Điểm nhấn đè dấu góc** ("TỪ 98 ĐẾN 2002"): `Nhan.jsx` chỉ tránh mặt. Nay chữ cạnh mặt không lên trên `BRAND_BOT + 24`.
- **Màn chốt ngang đè dấu góc:** ô video 56% bề ngang + dấu góc vẫn vẽ. Nay ô 50%, dấu góc ẩn trong `cta` khung ngang, thẻ kết thúc trên thanh thời gian.
- **Thiếu thanh thời gian:** từng chỉ bật cho podcast và highlight. Nay bật cho mọi video dài (`src/thanh.js`), phụ đề lên trên thanh (`CAP_H` +40).
- Soát: chụp `phu-de@<giây>` cùng cảnh để thấy dấu góc + thanh; với khung ngang luôn chụp ít nhất một cảnh điểm nhấn, một bố cục, màn chốt.

## Video nhiều người / phỏng vấn (video "5 nguyên tắc", 2 người ngồi bàn)
- Bản cũ chỉ giữ MẶT LỚN NHẤT → không biết có người thứ hai: thẻ `the-canh` đè mặt khách, ô `o-nguoi` (ô đứng, tâm theo mặt chủ) cắt
  nửa mặt khách. Nay `nhan_place.py` ghi mọi người + người đang nói; graphic đi qua `lib/cho.js`.
- Người quay nghiêng: Vision hay mất mặt → `nhan_place.py` lấy chỗ ngồi quen của người đó (`uoc: true`). Máy quay di chuyển nhiều
  (vlog đi bộ 2 người) thì cách gom chỗ ngồi theo bề ngang không còn đúng — soát kỹ khung.
- Ghép giọng với người: so cử động miệng của mỗi người với MỨC THƯỜNG của chính họ (mặt nghiêng có số đo miệng nhỏ hơn hẳn).
- Thẻ tên khách: `bam: 'trai'|'phai'` — lúc giới thiệu người đang nói là chủ, nhưng thẻ phải nằm cạnh khách.
- Khung ngang: `lower` (thẻ tên dưới) không hiện chữ, `action` đẩy câu trích ra ngoài vùng an toàn → dùng `nhan` (thẻ tên) và
  `bocuc` `o-nguoi` + `the` (câu hành động) cho tới khi hai cảnh đó được làm lại cho khung ngang.
- teaser.py: mỗi đoạn một đầu vào riêng; dùng chung một đầu vào cho nhiều nhánh → ffmpeg giữ cả video trong bộ nhớ, video 14 phút bị SIGKILL.

## Video cuộc gọi hợp tác 11/11/2026 (mất 4–5 giờ thay vì ~1 giờ) — đã chặn
| Lỗi | Hậu quả | Chặn ở đâu |
|---|---|---|
| Tự đổi khung sang dọc khi David chỉ nói "tập trung vào điện thoại" | làm lại từ đầu (~2 giờ) | SKILL "Đầu vào": khung chỉ đổi khi David nói rõ khung |
| "Tập trung vào một vùng" làm bằng cắt-phóng cả khung | rác (bàn, sổ, tường) vẫn còn quanh điện thoại | `tu-chon.md` bước 2 → khung chủ thể `khung_chu_the.py` |
| Chỉ dùng vài kiểu cảnh quen, video dày ý mà giữa các cảnh chỉ còn phụ đề | người xem khó theo dõi | `tu-chon.md` + `chan_doan.py` → bảng ghi chú chạy `GHI_CHU` |
| Thử kiểu cảnh bằng chụp/render: `kinetic`, `action`, `card` > 4 dòng lỗi ở khung ngang | ~45 phút đổi kiểu nhiều vòng | `soat_canh.mjs` P0/P1 theo khung |
| Cảnh `illus` bắt đầu 4 s trước phần tử đầu | 4 s nền tối che người, không chữ (lọt tới bản cuối) | `soat_canh.mjs` P0 "màn trống đầu cảnh" |
| Vision không dò mặt trong màn hình điện thoại → đặt hình sai phía | chỉnh tay mat.js | `nhan_place.py` đọc `khung.js` |
| Ghép bản cuối khi `render.mjs` còn render thẻ cuối | bản cuối mất màn kết YouTube 20 s, ghép lại 30 phút | khoá `.dang-render` + `render_preview.py` kiểm đủ lớp |
| `chuan_am.py` chặn đỉnh −2,0 dB mà AAC đẩy lên −1,0 | 3 lượt không đạt; mổ xẻ giữa chừng ~40 phút | hạ ngưỡng theo phần vượt, tối đa 6 lượt; SKILL "Nhịp làm": lỗi skill ghi `check/loi-skill.md`, làm tiếp |
| `renderStill` màn chốt quá hạn 28 s (đọc khung từ video gốc 1,6 GB) | chụp thử hỏng | `preview.mjs` timeout 240 s |
| Tạo liên kết cứng giữa bản nguồn và `video_goc.mp4` rồi ffmpeg ghi ra `video_goc.mp4` | ffmpeg cắt rỗng chính nguồn, mất bản sạch (dựng lại từ bản thô) | `khung_chu_the.py` xoá đích trùng nguồn; **không bao giờ `ln` file nguồn vào tên file đích** |
| Ảnh tĩnh `-loop 1` làm đầu vào mà không `-t` | ffmpeg chạy mãi, file 7 GB, mất 1 giờ | `khung_chu_the.py` có `-t`; mọi lệnh có `-loop 1` phải có `-t` hoặc `shortest` ở MỌI nhánh |
| Theo dõi việc nền bằng cỡ file thay vì thời gian dự kiến | không thấy lệnh chạy quá lâu | quá 1,5 lần dự kiến → kiểm ngay (SKILL "Nhịp làm") |
| `loi_ao.py` báo nhầm câu chen 0,4 s không có trong words.srt | phải chạy tay phần sau của clean_analyze | **chưa sửa** — gặp lại thì bỏ dòng đó, ghi `check/loi-skill.md` |

