# Luật chung — bộ skill dựng video của David (một nguồn cho cả 3 skill, 4 loại video)

Đọc file này trước mọi skill dựng video. Mỗi SKILL.md chỉ ghi luật RIÊNG của nó; trùng ý thì file này thắng, trừ khi SKILL.md
ghi rõ "ngoại lệ". Sổ quyết định + lý do: `<skill>/references/changelog.md`.

## 0. Kim chỉ nam (David chốt 2026-11-04)
**Người xem là trung tâm.** Kênh lớn đã chứng minh cách nào giữ người xem (DOAC, Hormozi, MrBeast, Ali Abdaal, Jay Shetty, Mel
Robbins…) thì **sao chép luôn chuẩn đó** — không cần thử A/B. Luật dựa trên gu riêng mà trái chuẩn kênh lớn → nghiêng về chuẩn
kênh lớn, ghi lý do vào changelog. Mục tiêu mỗi video: người xem **ở lại → HIỂU ý chính → LÀM theo**. Đo lại bằng số thật (mục 9).

## 1. Nội dung
- **Không bịa.** Phụ đề, chữ to, thẻ, màn hành động = **trích / bỏ bớt lời người nói**, không diễn đạt lại. Tên riêng, con số, vế
  đối lập, từ phủ định giữ nguyên. Tên chưa chắc chính tả → dùng cách Whisper nghe, hỏi trong báo cáo.
- **CHỮ TRÊN VIDEO = NGUYÊN VĂN LỜI DAVID** (David chốt 2026-11-07 — THAY các ngoại lệ (a), (b) dưới cho chữ nằm TRÊN video):
  motion graphics loại nào cũng được nhưng không sáng tạo sai lời. Không thẻ tít mở đầu mặc định (tít tự rút ý có thể lệch điều David muốn
  truyền tải). Màn chốt dùng câu David nói ở cuối video. Chữ = cụm nguyên văn liền mạch, được tách mảnh, không bỏ chữ làm đổi nghĩa
  ("không **muốn** làm một mình"). Không số chạy hiện số David không nói. Câu Claude tự viết (tiêu đề, mô tả, câu hỏi bình luận) chỉ ở bài đăng.
- **Ngoại lệ được viết lời** (chỉ hai chỗ — (a), (b) không còn áp cho chữ TRÊN video, xem dòng trên): (a) **câu màn chốt** của video thường (làm video / vlog / podcast) — Claude tự viết, giọng
  David, ≤ 55 ký tự, một hành động; (b) **tiêu đề, thumbnail, thẻ tít mở đầu highlight** — viết như tít báo, ĐÚNG Ý người nói,
  không thêm thông tin/lời hứa ngoài video, không giật tít sai sự thật (chuẩn DOAC: "A PATIENT ON MY FLIGHT HAD 5 MINUTES TO LIVE!");
  (c) **nhãn cố định của khung** (David duyệt 2026-11-04): "XEM BẢN ĐẦY ĐỦ" trên thẻ cuối highlight, và **lịch phát do David đưa**
  ("Tập mới mỗi thứ 6") trên thẻ cuối / màn kết — `project.schedule` (1 video), `STAGE.schedule` (podcast), plan.json `"schedule"`
  (vlog), `"endcard": {"schedule"}` (highlight). Không tự đặt lịch.
- **Lằn ranh** (loại khỏi mọi chữ/clip): huyền học, thần số học, phong thuỷ, lá số · "chữa lành", công dụng sức khoẻ của sản phẩm ·
  tư vấn thuế/pháp lý · tên thật/nơi làm/chi tiết lộ danh tính khách, học viên, nhân viên · giá, tên gói dịch vụ. Câu chủ chốt dính
  lằn ranh → báo David, không tự sửa lời.
- Whisper bịa câu ở đoạn không lời ("Hãy subscribe cho kênh…", "Cảm ơn các bạn đã xem") → bỏ.

## 2. Nhịp (chuẩn kênh lớn)
- **Mở đầu 0–3 s** nói ngay video về cái gì / đang đặt cược gì: thẻ tiêu đề chữ to ở nửa trên khung, hiện từ giây 0.
- **VIDEO DÀI KHÔNG CẮT GÌ** (David chốt 2026-11-05 — thắng mọi luật cắt cũ): video dài (> 3 phút: podcast, tâm sự, thực tế, nói trước
  camera) là BẢN GỐC, để nguyên cả khoảng lặng, tiếng "ờ/ừm", ngập ngừng, nói lại, đoạn dẫn dắt, phần đầu/cuối. Những chỗ kỹ thuật coi là
  lỗi lại là nét tự nhiên của người kể chuyện; giá trị của đoạn hay nằm trong cả câu chuyện dẫn tới nó. Không rút video dài thành đoạn hay. **Ngoại lệ (David 08/11/2026):** làm lại video cũ thì cắt màn tít + lời chào / giới thiệu kênh cũ (tên kênh cũ, nghề cũ, kinh doanh) và chữ/viền kênh cũ in trong hình — chỉ đúng các đoạn đó.
- **Lằn ranh ở video dài: CẢNH BÁO, không tự cắt.** Phiếu lọc liệt kê đoạn chạm (mốc giây + lý do + rủi ro), hỏi David cắt hay giữ; David quyết
  từng video. David chọn cắt thì chỉ cắt đúng đoạn đó. Dù giữ, chữ đồ hoạ / tiêu đề / thumbnail / mô tả / clip ngắn vẫn không lấy nội dung chạm lằn ranh.
- **Cắt chỉ dùng cho video ngắn trích từ video dài** (highlight) và video ngắn ≤ 3 phút: cắt lặng ≥ 0,45 s còn ~0,24 s + tiếng đệm
  "ờ/ừm" đứng riêng (jump cut + phóng xen kẽ 1,08×); vẫn giữ 1 s lặng sau câu hỏi kêu gọi. Clip luôn trích từ bản gốc, ưu tiên kéo người
  xem về video dài trên YouTube, không về thì vẫn cần tương tác / nhắn tin trên Facebook, TikTok. **Vlog ghép** giữ nhịp tự nhiên.
- **Không để 5–8 s trôi qua không đổi gì** ở video ngắn (nhịp chữ phụ đề, phóng, chữ to, cắt); video dài ~1 điểm nhấn / 15–20 s
  là đủ vì phụ đề + jump cut đã tạo nhịp.
- Một màn = một ý, một hình, một câu. Không chồng 2 lớp phủ.

## 3. Phụ đề (một nguồn: `video-style-edit/assets/remotion-template/src/subStyle.js`)
- **Video ngắn** (highlight; video 1 người dọc ≤ 90 s): **1–3 chữ to mỗi nhịp**, in hoa, viền đen dày, không hộp nền, từ khoá cam,
  ngang ngực/dưới cằm (`ShortLine`) — chuẩn Hormozi / DOAC / Jay Shetty. Tự bật; ép tay `project.short = true|false` (1 video)
  hoặc `SHORT` trong edl.js (ghép).
- **Video dài, vlog, podcast**: hộp tối, đầy đủ câu, đáy vùng an toàn (`SUB`).
- **Podcast đồ hoạ dọc trích ngắn** (David chốt 2026-11-06): không dải phụ đề; cả câu đang nói hiện to giữa khung làm đồ hoạ (`chu_chinh`), mỗi lúc một lớp chữ.
- **Màu theo nghĩa** (2026-11-04): trong `hl`, mục bắt đầu `+` = nên làm (xanh lá), `-` = tránh (đỏ), còn lại cam — chỉ khi lời có cặp nên/tránh.
- Luôn đầy đủ, đúng từng chữ; ẩn khi thẻ toàn cảnh đang hiện nguyên văn câu đó. Không đốt phụ đề bằng ffmpeg (không có libass).

## 4. Hình
- **ĐIỂM NHẤN TRÊN NGƯỜI** (David chốt 2026-11-07, nới luật 2 trạng thái): mọi video phải có motion graphics, hiểu là điểm nhấn kéo mắt người xem — nhiều loại, không chỉ toàn màn hình. Cảnh `nhan` được đè lên người, không che mặt: zoom dồn vào mặt ở câu đắt (`zoom` 1,12–1,2), làm tối viền (`toi`), chữ nhấn ≤ 4 chữ trích lời (`text`) hoặc biểu tượng nhỏ (`icon`) bật cạnh mặt. Mỗi video trộn loại theo nội dung, không số cố định. Khối 07.
- **BỐ CỤC TỰ CÂN** (David chốt 2026-11-07, thay luật 2 trạng thái): không con số bắt buộc về độ dài cảnh, tỷ lệ mặt / đồ hoạ, số cảnh; Claude chọn bố cục từ `trinh-bay/bo-cuc.md` sao cho hợp nội dung và người xem dễ nhận. Ngang tự do; dọc mỗi lúc ít thứ. Học video mẫu mới: chỉ học trình bày (bố cục, thứ tự hiện, cách nối, âm thanh), không đổi thẩm mỹ — quy trình ở `trinh-bay/README.md`.
- **Không che người nói** (face_place / LOW_Y), **không đè phụ đề** (chặn cứng ở mọi template).
- **Che mặt / thân trên → TOÀN MÀN HÌNH** (David chốt 2026-11-04): lớp chữ/hiệu ứng không có chỗ trống tránh được mặt, đầu, vai,
  ngực người nói → tự thành cảnh toàn màn hình (nền tối + quầng cam, nội dung phóng ra giữa, phụ đề vẫn chạy), dài theo nội dung
  (không trần cứng). Chỉ chạm tay/bụng/nền → giữ lớp phủ. Tít ghim (highlight) che đầu → tự ẩn. 1 video: `face_place.sh` tự làm;
  ghép (vlog, highlight): `python3 -I video-style-edit/scripts/overlay_guard.py <dự án>` sau `lift.py` và sau mỗi lần sửa edl.js.
  Giữ lớp phủ cho một cảnh: `place: {full: false}` (1 video) hoặc `keep: true` (OVERLAYS). Người/vật chính nằm thấp → nâng khung (`lift.py`).
- Vùng an toàn dọc 1080×1920: x 70–900, y 210–1420. Chữ tiếng Việt đủ dấu, không chồng dòng (`VN`, chừa 0,5 em trên / 0,32 em dưới).
- Minh hoạ mặc định = biểu tượng vẽ (`Icons.jsx`); ảnh thật chỉ cho địa danh, nhân vật có thật, tư liệu, minh chứng, sản phẩm cụ thể.
  Số liệu luôn bằng hiệu ứng, đúng con số người nói. Kết quả/con số mà clip gốc có bằng chứng thật (ảnh giá, hoá đơn) → ưu tiên chiếu.
- Không ghi chú kỹ thuật trên video (×1,6, slow-mo…). Không màn nguồn ảnh cuối video → `nguon-anh.txt`.
- Khung xuất = khung gốc trừ khi David yêu cầu (highlight luôn dọc 9:16).

## 5. Bộ nhận diện David (một nguồn: `remotion-template/src/brand.json` + `theme.js`/`brand.js` + `subStyle.js` + `cta.js` + `Icons.jsx`)
Dấu góc ● DAVID │ chủ đề · khuôn tiêu đề (dòng nhỏ cam → gạch cam → chữ cô đặc in hoa trắng, dòng nhấn cam) · tiếng ký hiệu
`sting.wav` lúc hiện tiêu đề · nhạc kênh dưới lời (4 bài cố định ở `cat-highlight-video/assets/music`, + 2 bài intro vlog; không
tự thêm bài) · giọng −20 LUFS, bản cuối −14 LUFS · màn chốt (`cta`, ~4 s, tick + "ting") → thẻ cuối. Sửa nhận diện → giữ đồng bộ cả 4 loại.
- **BỘ NHẬN DIỆN CHUNG** (David chốt 08/11/2026): mọi loại video cùng tiêu chuẩn vị trí và thành phần cố định — vùng an toàn, dấu góc,
  thanh thời gian, phụ đề, màn chốt, thẻ cuối. Một nguồn: `thu-vien-hinh/nhan-dien-chung.md` + `nhan-dien.js`. Chỉ motion graphics là tự do theo loại, theo cảnh.
- **Dấu góc** (sửa 08/11/2026): khung dọc 228 px, khung ngang sát mép trên vùng an toàn (`BRAND_TOP` / `BRAND_BOT` trong `theme.js`).
  Mọi lớp phủ ở góc trên (thẻ, điểm nhấn, bố cục) nằm dưới `BRAND_BOT`; màn chốt ngang ẩn dấu góc. Không viết số vị trí của khung dọc vào khung ngang.
- **Thanh thời gian ở đáy** (David chốt 08/11/2026): MỌI video đều có, kể cả clip ngắn (đã chạy mm:ss · còn mm:ss). Tắt tay chỉ khi David yêu cầu.

## 6. Lời kêu gọi
- Ưu tiên **câu mệnh lệnh nằm sẵn trong lời** ("Hãy chọn…", "thử làm…") — top video gần như không có câu "hãy bình luận".
- Màn hành động (`action`) đúng lúc người nói giao một việc làm được; 1–2 lần / video.
- Màn chốt ~4 s cuối mọi video; highlight dùng nguyên văn câu kêu gọi, video thường Claude tự viết (mục 1). **Ngoại lệ podcast đồ hoạ dọc trích ngắn** (David chốt 2026-11-06): không ép hành động, kết bằng màn hình cuối mời xem bản đầy đủ.

## 7. Phát hành (bước cuối của MỌI skill — David chốt 2026-11-04, chuẩn MrBeast / Paddy Galloway)
Ghi `<dự án>/phat-hanh/phat-hanh.md`:
- **3 tiêu đề** (≤ 60 ký tự, một ý, gây tò mò nhưng đúng ý video — mục 1b) xếp theo độ mạnh; tiêu đề và thumbnail **bổ sung**, không lặp chữ.
- **Thumbnail 1280×720 CHỈ khi video xuất NGANG 16:9 VÀ đăng YouTube** (David chốt 2026-11-04). Video dọc (Reels/TikTok/Shorts) không cần thumbnail — chỉ đề xuất mốc khung bìa. Video xuất ngang → **hỏi David một câu lúc đầu** (cùng lượt hỏi `hoi-chuyen-gia`): "Video này có đăng YouTube không?" — có thì làm 2 thumbnail, không thì bỏ.
  Cách làm: `zsh video-style-edit/scripts/thumbnail.sh <dự án> <nguồn> "<DÒNG 1>" "<DÒNG 2>" <số> [left|right] [vị trí] [phóng]`.
  Chuẩn: một khuôn mặt có cảm xúc rõ (mắt mở, miệng/biểu cảm), ≤ 4 chữ, một ý. Chọn khung: xem `contact.jpg`/`half_XX.jpg`, lấy
  khoảnh khắc cảm xúc mạnh nhất. Xem `thumb-<số>@160.jpg` (cỡ điện thoại) — không đọc được chữ thì rút chữ. **CHỈ HÌNH CỦA CHÍNH VIDEO ĐANG LÀM** (David chốt 2026-11-05): thumbnail / ảnh bìa / khung bìa
  lấy từ khung của chính video này (hoặc ảnh David gửi RIÊNG cho video này) — không bao giờ lấy mặt, cảnh, ảnh từ video / dự án
  khác, kể cả khi "đẹp hơn" hay tiện tay (2026-11-05: thumbnail podcast lấy mặt từ vlog Miếu Bà Cam → sai). **Podcast không mặt** (David duyệt 2026-11-06, khối 14): không dùng mặt người, kể cả ảnh chụp riêng; bìa = nền hoạ tiết + một hình vẽ theo ý của tập + tiêu đề ngắn + góc "DAVID · PODCAST", không liệt kê các bước giải pháp. Hình vẽ theo nội dung là ngoại lệ của luật lấy khung từ video.
  Không hỏi "lấy ảnh từ video cũ" như một lựa chọn.
- **Video dọc**: không ghép bìa trước video (giây đầu dành cho câu mở); ghi **mốc khung bìa đề xuất** (giây) để David chọn khi đăng.
- **Kiểu thumbnail Việt** (học 10/10 video dài Việt): mặt biểu cảm mạnh + 2–3 tầng chữ (≤ ~8 chữ), dòng cam = từ khoá to nhất,
  con số khổng lồ riêng (`THUMB_NUM`), nhãn series/số tập (`THUMB_BADGE`), dòng 3 (`THUMB_L3`).
- **Video > 3 phút đăng YouTube** (hỏi "có đăng YouTube không?" lúc đầu với MỌI video > 3 phút, ngang hay dọc):
  - **Màn kết YouTube 15–20 s**: 1 video/podcast `project.ytEnd = 20` (ghi sau bước làm sạch — clean_apply viết lại project.js);
    vlog ghép `"ytEnd": 20` trong plan.json. Khung chừa 2 ô video + nút đăng ký, nhạc kênh nhỏ; ghi vào phat-hanh.md: "gắn màn kết
    trong YouTube Studio: 2 video (trái/phải hoặc trên/dưới) + nút đăng ký (tròn giữa dưới)".
  - **Chương YouTube**: `python3 -I video-style-edit/scripts/chapters.py <dự án>` → `phat-hanh/chuong.txt` dán vào mô tả.
  - **Teaser 15–25 s** cho video > 10 phút (podcast, nói trước camera, vlog nói chuyện): sau render, chọn 2–3 câu đắt nhất (trọn câu,
    nguyên văn) → `python3 -I video-style-edit/scripts/teaser.py <dự án> <từ-đến> …` (chạy TRƯỚC chapters.py).
- Mô tả bài đăng + bình luận ghim (highlight theo mẫu cố định của skill), hashtag 3–5 tiếng Việt.
- Gửi David: video + thumbnail (SendUserFile) + tiêu đề.

## 8. Quy trình chung
- Hỏi theo `hoi-chuyen-gia` một lần đầu (diễn giải ngắn + câu thật sự thiếu); David "ok" thì chạy trọn một mạch. Ngoại lệ dừng duyệt:
  kế hoạch ghép vlog (multi-clip.md 2b).
- Lệnh dài (> 2 phút) chạy nền, không thăm dò. Không tự nhập mật khẩu máy. Không tải video từ YouTube/TikTok (nhờ David gửi file).
- Chụp thử (stills) trước khi render; kiểm bản cuối (khung, âm lượng ±0,5 dB, tiếng rè ±1 dB, thời lượng).
- Báo cáo tiếng Việt: đã làm gì, đã kiểm gì, chưa kiểm gì, tên riêng cần xác nhận.

## 9. Vòng số liệu (David chốt 2026-11-04)
Mỗi video giao kèm `<dự án>/so-lieu.md` (mẫu: `dung-video/khoi/16-so-lieu/mau-so-lieu.md`). 7 ngày sau đăng, David gửi ảnh chụp số liệu (YouTube
Studio / TikTok / Facebook) → Claude điền: lượt xem, tỉ lệ xem hết / thời lượng xem trung bình, giây người xem rời nhiều nhất,
CTR thumbnail (video ngang YouTube), lượt lưu/chia sẻ/bình luận. So với video trước → đề xuất **một** chỉnh luật kèm bằng chứng, David duyệt
rồi mới ghi changelog. Tổng hợp nhiều video ở `dung-video/so-lieu-tong.md`.
