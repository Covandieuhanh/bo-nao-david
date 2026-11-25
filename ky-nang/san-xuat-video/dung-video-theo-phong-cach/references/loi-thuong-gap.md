---
description: "Lỗi thường gặp khi dựng video (ffmpeg, Remotion, Whisper…) và cách tránh."
---

# Lỗi đã gặp và cách tránh

## Công cụ
- **ffmpeg của Homebrew không có `drawtext`** (không có freetype) nên không viết chữ bằng ffmpeg; mọi chữ làm trong
  Remotion hoặc Pillow.
- **`python3 -I` tắt thư mục user-site** nên Pillow (cài `--user`) không import được. Script cần Pillow
  (`the-ghi-cong.py --card`, `vung-an-toan.py`) chạy bằng `python3` thường; script khác chạy `-I` cho an toàn.
- `timeout` không có trên macOS — đừng dùng.
- **Whisper ở chỗ ồn** bịa "Hãy subscribe cho kênh…" và lặp câu hàng chục lần ở bản chép dài; mốc từng từ lệch 0,5–2 s thì điểm cắt dùng
  `diem-ngat.py`, mốc phụ đề kiểm bằng `soat-khop-tieng.py` (khối 01–03).
- **Chép kịch bản tập trước** = nhân bản kiểu trình bày thì mỗi tài nguyên chẩn đoán lại (`thiet-ke-bo-cuc/tu-chon.md` bước 0); render bị chặn nếu thiếu.
- Lệnh `rm` với biến: luôn `"${VAR:?}"` để không bao giờ xoá nhầm khi biến rỗng (Claude Code chặn dạng `rm -f "$X/$Y"`).
- npm báo `allow-scripts` cho esbuild thì chạy `npm approve-scripts esbuild` (tao-du-an.sh đã làm).

## Video gốc lạ
- iPhone đã cắt khung (ví dụ: 770×1368) hoặc 720p: component vẽ theo 1080×1920 nên `ap-dung-lam-sach.py` tự phóng về khung
  chuẩn (tỉ lệ ≈ 9:16 thì đúng 1080×1920). Luôn chạy bước làm sạch, kể cả khi không cắt gì.
- Quay ngoài trời / micro điện thoại: lời nói chỉ to hơn nền ồn khoảng 8–10 dB thì ngưỡng cố định "nền + 12 dB" coi cả video
  là im lặng ("Không thấy lời nói thật"). Ngưỡng giờ lấy min(nền + 12, điểm giữa nền và lời nói).

## Remotion
- Cảnh chiếu lại video gốc (`bocuc` o-nguoi, `cta`) đọc khung từ file gốc lớn (1,6 GB) thì quá hạn chờ 28 s khi máy bận. xuat-video.mjs
  đã đặt `timeoutInMilliseconds: 240000`, 2 luồng cho cảnh có video; lỗi giữa chừng thì `TIEP=1 node xuat-video.mjs` chạy tiếp. Render
  mỗi lúc MỘT dự án (8 GB RAM).
- Không đặt `"type": "module"` trong package.json — import không đuôi (`./canh`) sẽ hỏng.
- `defaultProps` phải là dữ liệu thuần (JSON) — truyền tên loại cảnh (`type`), không truyền component/hàm.
- Chữ trong khung `overflow: hidden` (hiệu ứng trồi lên) **cắt mất dấu dưới** (ạ, ợ) nên thêm `paddingBottom` + `marginBottom` âm.
- Chờ font bằng `delayRender` + `document.fonts.load` (đã có trong goc.jsx); thiếu thì khung đầu dùng font dự phòng.
- 8 GB RAM: `concurrency: 4`. Lần đầu chạy tải Chrome headless (khoảng 100 MB).
- Chữ to (kinetic, hook) tự co cỡ theo dòng dài nhất (≈ 0,46 em/ký tự với Barlow Condensed in hoa có dấu) thì không xuống
  hàng lẻ; đổi font thì đo lại hệ số.
- Chữ dài tự xuống dòng thì đè lên phần tử bên dưới. Component nên tự giảm cỡ chữ theo độ dài; luôn kiểm tra bằng ảnh chụp.

## Ảnh (Openverse / Wikimedia)
- Openverse chậm, hay timeout 30 s thì timeout 90 s, thử lại, tuần tự.
- Openverse có lúc sập hẳn (mọi lượt quá giờ) nên `kho-anh-openverse.py` tự chuyển sang API Wikimedia Commons (lọc bỏ NC/ND,
  ảnh < 1000 px); từ khoá nên cụ thể, có tên địa danh ("Tokyo street pedestrians" ra ảnh, "walking shoes" trả rỗng).
- **Wikimedia trả 429 cho urllib của Python** và cho tải song song thì dùng curl, tuần tự, nghỉ 0,4–0,5 s.
- Wikimedia chỉ cho độ rộng thu nhỏ chuẩn (500, 960, 1280); độ rộng lạ trả 400.
- Không đưa email/tên người dùng vào User-Agent.
- Ảnh có người nổi tiếng dễ nhận ra (ví dụ: vận động viên hút xì gà) thì bỏ. Clip-art giữa ảnh chụp thì lạc tông, bỏ.
- Ảnh CC BY / BY-SA bắt buộc ghi nguồn nên ghi vào `nguon-anh.txt` để dán vào mô tả bài đăng (video không có màn nguồn ảnh cuối).
  Cách ghi nguồn này hợp lệ khi video đăng kèm mô tả; nhắc người dùng dán vào mỗi lần đăng.

## ffmpeg ghép video
- `split` một ảnh lặp vô hạn ra nhiều nhánh nên bộ nhớ phình to nên làm sẵn ảnh có alpha thay vì ghép mask lúc chạy.
- Clip ProRes 4444 alpha: `yuva444p10le`; overlay bằng `setpts=PTS-STARTPTS+<giây>/TB` + `eof_action=pass`.
- Âm thanh gốc 44,1 kHz + đoạn câm 48 kHz thì dùng `aresample=48000` trước `concat`.
- **`anullsrc` mặc định là u8 (8-bit)** nên `concat` với tiếng gốc hạ CẢ bài xuống 8-bit + dither nên tiếng rè/xì suốt video
  (dải > 12 kHz tăng khoảng 11 dB; rõ nhất ở bản thu nhỏ tiếng). Luôn `aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo`
  cho MỌI nhánh audio trước `concat`/`amix`. Kiểm: năng lượng `highpass=f=12000` của bản cuối ≈ bản gốc (±1 dB).
- Mốc thời gian luôn làm tròn về khung (`round(sec * fps)`) ở mọi nơi (scenes, timeline, preview) để khớp nhau.
- 17 clip ProRes ≈ 2 GB — báo người dùng về dung lượng.

## Làm sạch video gốc (chế độ 1 video)
- **Video cũ của kênh cũ**: hay có **chữ / viền in cứng vào hình** — dải tên tập + ngày + website ở đáy
  (từ dòng khoảng 902/1080), viền trắng bo góc sát mép (khoảng 40 px). Luôn xem 1 khung ở giữa video **cỡ lớn** trước khi dựng; có thì cắt
  khung 16:9 bên trong rồi phóng lại 1920×1080 (`crop=1592:896:200:0` cho dải đáy; `crop=1808:1017:56:31` cho viền), làm TRƯỚC vi-tri-khuon-mat.sh.
  Màn tít mở đầu cũ ("PODCAST TẬP 4…") + lời chào/giới thiệu kênh cũ thì cắt (quy-tac-chung mục 2, làm lại video cũ).
- **Whisper chép ảo** cả bài một câu ("Hãy subscribe cho kênh Ghiền Mì Gõ…") ở video có tiếng trầm/nhạc mở đầu nên phan-tich-lam-sach.sh tự
  chép lại với tiếng đã lọc (`highpass=f=120,dynaudnorm`); còn ảo thì thêm `-mc 0` (tắt ngữ cảnh) và chép riêng đoạn đầu rồi ghép.
- Chỉ cắt vài đoạn (lời chào) ở video dài thì **không chép lại** bản sạch: `doi-moc-loi.py "$P"` dời lời bản thô sang mốc bản sạch.
  Đặt mốc cắt ở khoảng lặng thật (đo RMS 50 ms), không theo mốc từ của Whisper (lệch khoảng 0,3–0,5 s thì lẹm chữ "Đò").
- Bản thô đổi tên thành `video-goc-tho.<ext>` TRƯỚC khi ghi `video-goc.mp4` — macOS coi `video-goc.MP4` và
  `video-goc.mp4` là một file, ghi thẳng sẽ đè mất bản gốc đang đọc.
- Mốc trong `diem-cat.json` luôn là mốc **bản thô**; mốc trong canh.js là mốc **bản sạch** — quy đổi qua `cac-doan.json`.
- Whisper kéo dài mốc cuối từ vào khoảng lặng nên tìm khoảng lặng bằng `silencedetect` (ngưỡng = nền ồn + 12 dB),
  không bằng khoảng cách giữa các từ.
- Mỗi đoạn có fade âm 15–30 ms ở hai đầu, không thì mối cắt kêu "tách".
- ffmpeg 8 bỏ `-filter_complex_script` nên dùng `-/filter_complex <file>`.
- libx264 1080×1920 trên máy 8 GB mất khoảng 18 phút cho 3,5 phút video; `h264_videotoolbox -b:v 20M` chỉ khoảng 1,5 phút.
- Câu "giống câu trước" chưa chắc là nói lại: "master… thành siêu cao thủ…" là người nói giải thích lại có chủ ý nên giữ.

## Đổi khung (dọc ↔ ngang)
- Component luôn vẽ trên toạ độ khung dọc 1080×1920; khung ngang chỉ do `bo-cuc.js` (Place) thu/đặt lại nên đừng sửa
  toạ độ trong component cho khung ngang. Loại cảnh toàn màn hình mới phải thêm vào `FULL` trong bo-cuc.js.
- Pillar: `Scrim` tự tắt (nền hai bên đã tối); `hai-ben` render H.264 đặc (không alpha) khoảng 1,3× thời lượng video.
- Dò mặt: Vision (`nhan-dien-khuon-mat.swift`) — biên dịch lần đầu khoảng 2 phút, lưu ở `~/.cache/dung-video-theo-phong-cach/khuon-mat`.
- Khung cắt dọc đổi vị trí bằng `sendcmd` + `crop@rf x` (crop nhận lệnh x); đường dẫn file lệnh không được có dấu `:`.
- Người nói đoán theo độ cử động miệng (độ lệch chuẩn của độ mở môi trong câu) — hai người cùng cười/nói chen nhau
  dễ sai nên shot `?` trong ke-hoach.md phải đọc câu nói để quyết.
- `kiem-khung-hinh.sh` với mốc vượt thời lượng video thì lỗi "Could not open encoder" và giữ sheet CŨ; mốc phải < thời lượng.

## Nội dung chữ
- Né tên riêng chưa chắc chính tả bằng cụm chung chung (viết "ĐI BỘ MỖI NGÀY" chứ không "HARUKU") thì người dùng thấy minh hoạ
  sai ý. Hiện đúng tên theo Whisper + hỏi chính tả trong báo cáo.

## Vị trí lớp phủ (không che người nói)
- Dải lớp phủ cố định ở đáy che cằm/miệng khi quay selfie trong xe, cầm máy thấp (mặt nằm ở y khoảng 860–1170 trên 1920) thì 
  người dùng chốt: hiệu ứng không toàn màn hình **không được che nhân vật**, vị trí không cố định. `vi-tri-khuon-mat.sh` dò mặt
  (Vision, 2 khung/giây) ghi vào `vi-tri.js`; ưu tiên 2 điểm neo (đáy/đỉnh) để các cảnh không nhảy vị trí lung tung.
- Vision cho khung mặt không gồm tóc/cổ thì script nới lên 0,4 chiều cao mặt và xuống 0,25; lấy phân vị 5–95% của cả cảnh
  (đầu lắc qua lại). Đoạn không thấy mặt (quay màn hình xe, cảnh đường) thì giữ vị trí mặc định.
- Selfie vừa đi vừa quay (IMG_3196): mặt to (cao khoảng 440 px) và nhún liên tục thì đệm cổ 0,25 mặt + phân vị 95% làm mọi cảnh
  báo "che mặt". Khung Vision kết thúc ≈ cằm thì giờ đệm 0,06 mặt, phân vị 93%, cho thu tới 55%. Thẻ ở 55–60% chữ khá nhỏ —
  cảnh nhiều chữ nhỏ nên đổi sang chữ to/biểu tượng hoặc cảnh toàn màn hình.
- `vi-tri-khuon-mat.py` đọc `FULL` trong bo-cuc.js: dòng FULL có nhánh điều kiện (`...(project.podcast ? [] : ['card'])`) nên phải lấy
  mọi tên trong cả dòng (đã sửa); đọc thiếu thì thẻ toàn cảnh bị coi là lớp phủ và báo "che mặt" sai.
- Đổi mốc cảnh mà quên chạy lại `vi-tri-khuon-mat.py` thì cảnh mới không có trong vi-tri.js nên về vị trí mặc định (có thể che mặt).

## Chữ tiếng Việt (chữ to)
- Barlow Condensed in hoa, `lineHeight` khoảng 1 + khung `overflow: hidden` chừa cố định 34/30 px nên ở cỡ 140–150 px dấu chồng dòng dưới
  chạm dòng trên ("NGẪU", "NHIỀU"), dấu nặng bị cắt ("BỊ" thành "BI"). Đã sửa cho CẢ HAI skill bằng `VN` (khung-podcast.js: giãn 1,14, chừa
  0,5 em trên / 0,32 em dưới; chữ to tối đa 120, hook tối đa 118). Component chữ to mới phải dùng `VN`. Luôn soi ảnh chụp phóng to Ầ Ễ Ỗ Ị Ự.

- **Hai dòng chữ to xếp chồng** cần khe `VN.gap` = 0,24 cỡ chữ (trước 0,1): dấu nặng dòng trên + dấu chồng dòng dưới chạm nhau
  ("MỘT NGÀY" / "RẤT LÀ ĐẶC BIỆT" — dấu dưới Ộ chạm dấu Ấ, người dùng chỉ ra). Nhãn có thể tự xuống dòng dùng
  `lineHeight: VN.lh + VN.gap`. Ngoại lệ: dòng nằm trong ô màu (hook) đã có đệm riêng thì khe 0,06 (khe lớn đẩy ô lấn sóng âm).
- **Chữ to đứng ngay sau một dòng/khối khác** (kicker, vạch màu, "BƯỚC n", khung ảnh) phải chừa phía trên `aboveGap(size)` =
  0,4 cỡ chữ cho dấu chồng — đã gặp (IMG_3196, cảnh "cái cây"): "GỐC RỄ" đè lên dòng "Phải nuôi đến cả năm trời", và dòng đó
  lại chạm mép dưới khung ảnh (chữ đặt sát mép ảnh). Montage dọc giờ: ảnh y 440–1010, chữ bắt đầu 1044 (cách ảnh 34 px), chữ to
  tối đa 120. Viết component mới: không xếp chữ to ngay dưới chữ khác bằng margin cố định nhỏ; luôn chụp thử khung có Ố Ễ Ỗ.

- **Lớp phủ tràn xuống dải phụ đề**: ô có nội dung cao hơn dải lớp phủ (435 px trong toạ độ component) thì khi đặt sát trên phụ đề,
  phần thừa nằm dưới phụ đề (người dùng chỉ ra: "10 TRIỆU" bị phụ đề đè). `Place` giờ có mép chặn cứng (`Clip`) ở đỉnh dải phụ
  đề (dọc tự quay y 1280; podcast `PF.contentBottom`). Mép chặn chỉ là lưới an toàn: phần tràn sẽ bị CẮT — component phải tự
  vừa dải (CardShell có maxHeight); chụp thử thấy chữ/hình bị cắt ở đáy thì rút nội dung hoặc giảm cỡ.

## Template dùng chung với podcast
- `khung-podcast.js`, `san-khau.jsx`, `dong-thoi-gian.jsx`, `toan-man-hinh-ngang.jsx`, `bieu-tuong.jsx`, composition `nen` thuộc skill dung-podcast;
  mọi nhánh podcast chỉ bật khi `project.podcast`. Sửa template thì chụp thử cả một dự án tự quay (ví dụ: edit-img0499) lẫn một
  dự án podcast (dọc + ngang) trước khi coi là xong.
- `chu-de.js`: SAFE dọc cố định (bottom 1420, rộng 830) — đúng cho mọi dự án dọc 1080×1920 (ap-dung-lam-sach.py luôn đưa về khung này).

## Phụ đề
- Lần chạy Whisper theo từ (`-ml 1`) và theo câu cho kết quả khác nhau; cả hai đều có thể đè câu bịa lên câu thật cuối
  video ("Hãy subscribe cho kênh Ghiền Mì Gõ…" ở chỗ David nói "Xin chào") thì đối chiếu lần chạy ở `kiem-tra/lam-sach/`.
- Khung chữ phụ đề rộng khoảng 37 ký tự ở cỡ 42 px; dòng dài hơn thì `textWrap: 'balance'` chia đều 2 dòng, tránh rơi 1 chữ.

## Giao tiếp
- Người dùng không xem được video trong khung chat thì gửi file bằng SendUserFile và mô tả cảnh theo mốc thời gian.
- Mật khẩu, tải video từ mạng: `../../quy-tac-chung.md` mục 8.

## Chế độ ghép nhiều clip
- **macOS không phân biệt hoa/thường tên file**: `chuong-trinh.jsx` và `show.js` là MỘT file nên import nhầm, lỗi
  "A value of `undefined` was passed to the `component` prop". Đặt tên khác hẳn (chuong-trinh.jsx + danh-sach-cat.js).
- **Whisper bịa câu khi không có lời** ("Hãy subscribe cho kênh Ghiền Mì Gõ…" lặp cả clip) thì so với `am-luong.txt`,
  cắt đoạn có tiếng rồi chạy lại với `-mc 0`.
- Clip iPhone có metadata xoay (−90°): ffmpeg tự áp khi chuẩn hoá (tao-dung-ghep.sh) nên luôn dùng `public/doan-video/cN.mp4`,
  không đưa .MOV gốc vào Remotion.
- Đoạn máy cầm ngang: xoay riêng bằng `transpose=2` (mặt đất bên trái thành xuống dưới) hoặc `transpose=1`, kiểm bằng 1 khung.
- Remotion 4.0.5xx: `startFrom` đã đổi tên thành `trimBefore` (OffthreadVideo, Audio).
- Hiệu ứng + nhạc + tiếng gốc dễ chạm 0 dB nên xuat-chuong-trinh.mjs tự loudnorm (−14 LUFS, đỉnh −1,5 dB).
- zsh KHÔNG tách biến chưa trích dẫn thành nhiều đối số: `node xem-truoc.mjs $ARGS` truyền cả chuỗi làm 1 đối số nên dùng `${=ARGS}`.
- zsh: `$n:l…` trong chuỗi bị hiểu là modifier (`:l` = chữ thường) nên viết `${n}` khi ngay sau là dấu `:`.
- `glob` của ffmpeg sắp chữ cái (11.8 trước 2.3) nên ghép sheet bằng `ls | sort -n`.
- Toạ độ ước từ ảnh thu nhỏ dễ sai; lấy bằng khung có lưới `drawgrid` ở đúng mốc giây trong clip.
- `node anh-tinh.mjs` đôi khi báo "Timed out … connect to the browser" lần đầu (Chrome headless khởi động chậm) thì chạy lại là được.
- Contact sheet 24 khung của clip ngắn (8 s) có bước 0,34 s — đừng ước mốc theo số thứ tự khung như clip dài; tính lại `t = i * DUR/24`.
- Render cả video lỗi "delayRender … Fetching …/proxy?src=…cN.mp4 … not cleared after 28000ms" / "ECONNRESET": bộ trích
  khung quá tải với clip dài + concurrency 4 nên xuat-chuong-trinh.mjs dùng concurrency 3, timeoutInMilliseconds 120000,
  offthreadVideoThreads 2 (đã sửa trong template).

## Nâng khung (nang-lop.py)
- Mốc mặt dò 2 khung/giây; người đi nhanh có thể lệch — luôn xem 1–2 khung sau khi nâng. Mặt gần đỉnh (đỉnh đầu < 230) thì
  script tự giảm mức nâng; nếu cả hai đầu đều chật (mặt to chiếm cả khung) thì không nâng được, để nguyên.
- danh-sach-cat.js đọc bằng `node --input-type=module` — lỗi cú pháp danh-sach-cat.js (thiếu dấu phẩy sau chú thích cuối dòng) làm nang-lop.py báo
  CalledProcessError; chạy `node -e "import('file://…/danh-sach-cat.js')"` để thấy dòng lỗi.
- `cite` có `{label: undefined}` nên JSON thành `{}`: kiểm `'cite' in s`, đừng `s.get('cite')`.

## Highlight (dùng chung template với cat-doan-noi-bat)
- `chuyen-dong/src/doan-noi-bat.js` = null ở mọi dự án thường; có dữ liệu (ap-dung-doan-noi-bat.py) thì phụ đề hiện thanh tập gốc + hiệu ứng tua
  (tua.jsx, chỉ khi bật `--tua`) và xem-truoc-ban-dung.py trộn `assets/hieu-ung-am-thanh/tua.wav`. Sửa Captions/Timeline thì chụp thử cả dự án thường lẫn highlight.
- xem-truoc-ban-dung.py: chỉ số đầu vào của màn nguồn ảnh phải đếm sau mọi tiếng hiệu ứng (trước đây cố định n + 1 thì sai khi có ting).
- Highlight ở video người nói: phụ đề lên 40 px nhường thanh tập gốc thì dải lớp phủ phải dừng sớm 40 px (CAP_H = 180 trong bo-cuc.js
  + vi-tri-khuon-mat.py khi doan-noi-bat.js có dữ liệu), không thì ô chữ (hook) chạm phụ đề 2 dòng (gặp ở IMG_3196). Sửa CAP_H ở một nơi thì sửa cả hai.
- Highlight người nói dựng bằng montage-template: sửa `chuong-trinh.jsx` phần `HL/TONE/MUSIC.tracks/jump` thì chụp thử cả
  một dự án vlog thường (`edit-vlog-nhan-xe`) để chắc không đổi gì khi `HL = null`.
- Nhạc Pixabay to nhỏ rất khác nhau (−9 … −20 LUFS) nên đặt `gain` theo bài (danh-sach-cat-doan-noi-bat.py / ap-dung-doan-noi-bat.py `GAIN`), đo lại khi thêm bài.
- Pixabay chặn tải bằng curl / fetch thẳng CDN (403) — nhờ người dùng bấm "Free download"; không lách.

- tao-dung-ghep.sh: lưới khung mỗi 13 s — phần dư cuối < 0,6 s (clip 13,17 s) không ra khung nào nên ffmpeg lỗi, cả dự án dừng (gặp ở vlog leo núi 48 clip) nên bỏ phần dư đó.
- Montage: lớp chữ toạ độ cố định (thẻ địa điểm top 1060…) đè phụ đề 2 dòng nên canh đáy vào `LOW_Y`.
- Hình lật ngang/lộn ngược lúc rút máy khỏi túi có độ sáng/độ tương phản/YDIF như cảnh đi bộ thường thì không dò bằng signalstats;
  chỉ bắt được bằng mắt trên `kiem-tra/cac-doan/` (c13 vlog leo núi).
- Remotion `bundle()` chép CẢ `public/` (clip gốc) vào thư mục tạm mỗi lần chạy, không tự xoá thì vlog 48 clip: 205 bản sót, đầy ổ,
  render kẹt/ENOSPC. Mọi script render/stills giờ `fs.rmSync(serveUrl)` ở cuối; script tự viết thêm cũng phải dọn.
- Chữ đè phụ đề lặp nhiều lần (thẻ địa điểm, danh sách `chips`): nguyên nhân chung = đặt vị trí bằng ƯỚC
  chiều cao (top cố định, n × cỡ chữ) trong khi chữ dài tự xuống dòng. Luật: lớp chữ KHÔNG BAO GIỜ đặt `top` ước lượng — neo ĐÁY
  vào LOW_Y (translateY(-100%)) để khối mọc lên; chữ một dòng thì tự thu cỡ theo mục dài nhất; chuong-trinh.jsx chặn cứng mọi lớp không
  toàn màn hình ở mép trên dải phụ đề (lưới an toàn, như bo-cuc.js chế độ 1 video / PF.contentBottom podcast). Chụp soát ở CUỐI mỗi
  lớp (danh-sach-cat-vlog.py in sẵn mốc), không chụp lúc mới hiện.
- Sửa `thu-vien-tai-nguyen/` khi dự án ĐÃ tạo: dự án giữ bản chép thật (`cp -RL`) nên chép file vừa sửa vào `<dự án>/chuyen-dong/src/thu-vien/` rồi mới chụp/render (đã gặp: Illus lưới 2 cột chưa vào dự án VF3).

## Điểm nhấn trên người `nhan`
- Selfie vừa đi vừa quay: mặt xê dịch 30–40% chiều ngang trong một cảnh thì đặt chữ theo trung vị mặt sẽ đè mặt. `vi-tri-nhan.py` ghi
  khoảng mặt (`l`, `r` = phân vị 10/90 suốt cảnh), nhan.jsx đặt chữ ngoài khoảng đó + chừa 0,3 bề rộng mặt.
- Khung ngang KHÔNG đặt chữ dưới cằm (đè miệng + phụ đề). Hết chỗ thì chữ tự thu cỡ cho vừa; chữ dài thì ngắt 2 dòng (tối đa 9 ký tự / dòng) để giữ cỡ to.

- **Bố cục "người thu vào ô" (khung ngang): thẻ chữ canh giữa vùng trống bị đẩy lên đè dấu góc kênh** (BrandMark ở top 228 px) khi thẻ cao. Vùng nội dung giờ bắt đầu từ `max(SAFE.top, 320)`. Soát bằng ảnh rải đều cả video, không chỉ ảnh giữa cảnh.

### Lỗi khung ngang David chỉ ra (4 video cũ làm lại)
Gốc chung: template dựng cho khung dọc trước; các video ngang trước đó đều là podcast (dấu góc nằm trong sân khấu), nên khung ngang
người nói chưa từng chạy với dấu góc. Không do bài học video mẫu xoá gì; riêng `bo-cuc.jsx` (từ bài học) đã chép số 300/320 theo giả định cũ.
- **Dấu góc thấp:** `top: 228` là số của khung dọc, dùng luôn cho khung ngang (21% chiều cao). Nay `BRAND_TOP` theo khung (`chu-de.js`).
- **Điểm nhấn đè dấu góc** ("TỪ 98 ĐẾN 2002"): `nhan.jsx` chỉ tránh mặt. Nay chữ cạnh mặt không lên trên `BRAND_BOT + 24`.
- **Màn chốt ngang đè dấu góc:** ô video 56% bề ngang + dấu góc vẫn vẽ. Nay ô 50%, dấu góc ẩn trong `cta` khung ngang, thẻ kết thúc trên thanh thời gian.
- **Thiếu thanh thời gian:** từng chỉ bật cho podcast và highlight. Nay bật cho mọi video dài (`src/thanh.js`), phụ đề lên trên thanh (`CAP_H` +40).
- Soát: chụp `phu-de@<giây>` cùng cảnh để thấy dấu góc + thanh; với khung ngang luôn chụp ít nhất một cảnh điểm nhấn, một bố cục, màn chốt.

## Video nhiều người / phỏng vấn (video "5 nguyên tắc", 2 người ngồi bàn)
- Bản cũ chỉ giữ MẶT LỚN NHẤT thì không biết có người thứ hai: thẻ `the-canh` đè mặt khách, ô `o-nguoi` (ô đứng, tâm theo mặt chủ) cắt
  nửa mặt khách. Nay `vi-tri-nhan.py` ghi mọi người + người đang nói; graphic đi qua `thu-vien/cho.js`.
- Người quay nghiêng: Vision hay mất mặt nên `vi-tri-nhan.py` lấy chỗ ngồi quen của người đó (`uoc: true`). Máy quay di chuyển nhiều
  (vlog đi bộ 2 người) thì cách gom chỗ ngồi theo bề ngang không còn đúng — soát kỹ khung.
- Ghép giọng với người: so cử động miệng của mỗi người với MỨC THƯỜNG của chính họ (mặt nghiêng có số đo miệng nhỏ hơn hẳn).
- Thẻ tên khách: `bam: 'trai'|'phai'` — lúc giới thiệu người đang nói là chủ, nhưng thẻ phải nằm cạnh khách.
- Khung ngang: `lower` (thẻ tên dưới) không hiện chữ, `action` đẩy câu trích ra ngoài vùng an toàn nên dùng `nhan` (thẻ tên) và
  `bocuc` `o-nguoi` + `the` (câu hành động) cho tới khi hai cảnh đó được làm lại cho khung ngang.
- doan-gioi-thieu.py: mỗi đoạn một đầu vào riêng; dùng chung một đầu vào cho nhiều nhánh thì ffmpeg giữ cả video trong bộ nhớ, video 14 phút bị SIGKILL.

## Video cuộc gọi hợp tác (mất 4–5 giờ thay vì khoảng 1 giờ) — đã chặn
| Lỗi | Hậu quả | Chặn ở đâu |
|---|---|---|
| Tự đổi khung sang dọc khi David chỉ nói "tập trung vào điện thoại" | làm lại từ đầu (khoảng 2 giờ) | SKILL "Đầu vào": khung chỉ đổi khi David nói rõ khung |
| "Tập trung vào một vùng" làm bằng cắt-phóng cả khung | rác (bàn, sổ, tường) vẫn còn quanh điện thoại | `tu-chon.md` bước 2 → khung chủ thể `khung-chu-the.py` |
| Chỉ dùng vài kiểu cảnh quen, video dày ý mà giữa các cảnh chỉ còn phụ đề | người xem khó theo dõi | `tu-chon.md` + `chan-doan.py` → bảng ghi chú chạy `GHI_CHU` |
| Thử kiểu cảnh bằng chụp/render: `kinetic`, `action`, `card` > 4 dòng lỗi ở khung ngang | khoảng 45 phút đổi kiểu nhiều vòng | `soat-canh.mjs` P0/P1 theo khung |
| Cảnh `illus` bắt đầu 4 s trước phần tử đầu | 4 s nền tối che người, không chữ (lọt tới bản cuối) | `soat-canh.mjs` P0 "màn trống đầu cảnh" |
| Vision không dò mặt trong màn hình điện thoại → đặt hình sai phía | chỉnh tay mat.js | `vi-tri-nhan.py` đọc `khung.js` |
| Ghép bản cuối khi `xuat-video.mjs` còn render thẻ cuối | bản cuối mất màn kết YouTube 20 s, ghép lại 30 phút | khoá `.dang-render` + `xem-truoc-ban-dung.py` kiểm đủ lớp |
| `chuan-am.py` chặn đỉnh −2,0 dB mà AAC đẩy lên −1,0 | 3 lượt không đạt; mổ xẻ giữa chừng khoảng 40 phút | hạ ngưỡng theo phần vượt, tối đa 6 lượt; SKILL "Nhịp làm": lỗi skill ghi `kiem-tra/loi-ky-nang.md`, làm tiếp |
| `renderStill` màn chốt quá hạn 28 s (đọc khung từ video gốc 1,6 GB) | chụp thử hỏng | `xem-truoc.mjs` timeout 240 s |
| Tạo liên kết cứng giữa bản nguồn và `video-goc.mp4` rồi ffmpeg ghi ra `video-goc.mp4` | ffmpeg cắt rỗng chính nguồn, mất bản sạch (dựng lại từ bản thô) | `khung-chu-the.py` xoá đích trùng nguồn; **không bao giờ `ln` file nguồn vào tên file đích** |
| Ảnh tĩnh `-loop 1` làm đầu vào mà không `-t` | ffmpeg chạy mãi, file 7 GB, mất 1 giờ | `khung-chu-the.py` có `-t`; mọi lệnh có `-loop 1` phải có `-t` hoặc `shortest` ở MỌI nhánh |
| Theo dõi việc nền bằng cỡ file thay vì thời gian dự kiến | không thấy lệnh chạy quá lâu | quá 1,5 lần dự kiến → kiểm ngay (SKILL "Nhịp làm") |
| `loi-ao.py` báo nhầm câu chen 0,4 s không có trong moc-tung-tu.srt | phải chạy tay phần sau của phan-tich-lam-sach.sh | **chưa sửa** — gặp lại thì bỏ dòng đó, ghi `kiem-tra/loi-ky-nang.md` |


## Khung chủ thể (khung.js) + cảnh có sẵn
- `nhan` có chữ / biểu tượng: nhan.jsx đặt cạnh mặt trong khung gốc thì với khung chủ thể chữ rơi vào khe giữa khung và cột, bị cắt
  (tap-ban-ca-ngay). `bocuc the-canh` không có chỗ thì tự chuyển `o-nguoi` với thẻ trống. Dùng cảnh tự vẽ đặt vào cột trống: chữ nhấn
  `rieng/chu-cot.jsx`, ảnh thật `rieng/anh-canh.jsx` (cùng công thức bangO) — mẫu ở `~/Movies/tap-ban-ca-ngay/2-ban-day-du/chuyen-dong/src/rieng/`.
- `montage` khung ngang (MontageL) tràn ảnh xuống vùng phụ đề / vùng đỏ, mất nhãn thì không dùng; nhiều ảnh nối nhau dùng `AnhCanh` (items).
- Máy soát báo P2 "cùng kiểu ve liền nhau" cả khi hai component khác nhau (ảnh / chữ) — ghi lý do ở ke-hoach-canh.md.

## Ảnh khi Openverse sập
- Wikimedia tìm theo tên file: từ khoá đời thường dài ("man working on computer late at night") hay rỗng / 429; dùng cụm ngắn kiểu tên
  file ("alarm clock", "stack of books", "wall calendar", "brain anatomy model") và chạy lại riêng các key lỗi.
- Soát lại tên ảnh trong ghi-cong.tsv sau khi tải (ví dụ: "office dog…" — ảnh tối có con chó) và logo hãng ở chính giữa (vô-lăng Mercedes) thì đổi.

## Nhạc ép tay không ăn (25/11/2026, buổi DJI_0031)
- **Hiện tượng:** chọn ba bài cho ba video nhưng cả ba ra cùng một bài (bài đầu tuyến `kien_thuc`).
- **Nguyên nhân gốc:** tài liệu khối 09 và chú thích trong `xem-truoc-ban-dung.py` ghi khoá `music`, còn code đọc khoá `nhac` → tài liệu lệch code; script gặp khoá lạ thì bỏ qua im lặng; quy trình không có bước đối chiếu "nhạc đã áp" với kế hoạch, chỉ thấy nhờ tình cờ đọc nhật ký ghép.
- **Loại:** cách làm (học một vòng): kế hoạch chọn nhạc đúng, công cụ và tài liệu sai.
- **Đã chặn:** sửa tài liệu khối 09 và chú thích; script dừng hẳn khi thấy khoá `music`; sau ghép đối chiếu dòng "nhạc nền: …" với `ke-hoach-canh.md`.
- **Bài học chung:** tài liệu nói một đằng, code làm một nẻo thì tin code và sửa tài liệu ngay; công cụ không được bỏ qua im lặng điều nó không hiểu.
