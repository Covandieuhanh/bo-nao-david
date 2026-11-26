---
description: "Nhật ký thay đổi skill cắt đoạn nổi bật: quyết định của David và lý do."
---

# Nhật ký thay đổi — cat-doan-noi-bat (quyết định của người dùng và lý do)

## 18/11/2026 — Bản dọc cùng ý, cùng intro
- David: "làm thêm 1 video highlight gồm có cả itro nhưng mà bản dọc nhé", nên Claude thêm mục "Cùng ý, thêm bản dọc từ nguồn ngang" dưới Highlight ngang: đổi khung nguồn bám người nói, giữ mốc; chữ nhấn trên đầu (`y`); thẻ tiêu đề intro `keep: true`.
- Claude sửa `ke-hoach-doi-khung.py` (`probe`): file DJI in thêm dòng thì lấy dòng đầu.

## 17/11/2026 — Highlight ngang có intro ghép
- David: "từ 2 video này, tạo ra 1 video highlight trọn 1 ý đặc sắc nhất, có intro ở đầu được ghép từ các cảnh trong 2 video gốc này. video highlight ngang nhé", nên luật 1 thành "mặc định dọc, ngang khi David yêu cầu"; Claude thêm mục "Highlight ngang" (khung, intro, nguồn nhiều video dài). Mẫu ghép: màn chốt ngang (ô 50 %), `pow.x`.
- Claude sửa lỗi `TS()` trong `danh-sach-cat-doan-noi-bat.py`: câu đặt khác thứ tự nguồn làm mọi lớp phủ dồn về câu đầu, nay script tìm đúng đoạn chứa mốc.

## Tái bản 3 — 14/11/2026: bản luật viết lại từ bảng du-an/nang-cap/tai-ban-3-video.md
- Claude bỏ dấu ngày, lời kể, chỗ ngược luật khỏi bản luật; mục "Nhật ký" cuối SKILL.md chuyển về đây:
- 2026-11-10 · David chốt: clip dọc bỏ thanh thời gian và thẻ cuối, màn chốt trên hình (quy-tac-chung 5); `danh-sach-cat-doan-noi-bat.py` vẫn ghi ENDCARD nhưng mẫu tự bỏ (`nganDoc`).
- 2026-11-08 · chuẩn hoá (`du-an/chuan-hoa-ky-nang.md` bước 3): mọi chữ nguyên văn, tít là cụm then chốt nhất, bỏ "tít báo" (N3); màn chốt một luật cả hai nhánh, không có câu kêu gọi thì không dừng (N13); thẻ cuối "Bản đầy đủ trên kênh …", không nút phát, bỏ câu gợi tò mò Claude viết (N14); phụ đề cụm 5–8 chữ (N5); bỏ số nhịp/mật độ (N6); "kho nhạc kênh" (N7); gộp mẫu podcast dọc vào kịch bản 7B; đọc trước 3 file; bước nhẹ 0–1; sửa link tài liệu; rút mô tả; thêm "Xong khi". Chi tiết các quyết định trước: `references/nhat-ky-thay-doi.md`.

## Tái bản 2 — 10/11/2026: bản luật viết lại từ bảng du-an/nang-cap/tai-cau-truc-2-video.md
- Nguồn luật bỏ phóng xen kẽ ở điểm cắt là quy-tac-chung mục 2 (kèm lý do); khối 02, ho-so-thuong-hieu/doan-noi-bat.md, cat-highlight luật 8 trỏ về đó. quy-tac-chung mục 8 trỏ thói quen chung (hỏi, lệnh nền, mật khẩu, báo cáo), chỉ giữ phần riêng video. Claude bỏ câu chép ở gotchas, phan-phoi-da-kenh; sửa đường trỏ "hình của chính video" về khối 14; viết lại 6 câu mà công cụ đo khớp nhầm ("thay cho", "THAY", tên file có ngày).

## 10/11/2026 — Bỏ phóng xen kẽ 1,08× ở điểm cắt
- David xem đoạn thử tap-thu-tai-ban-video-1: "tôi không thích mấy đoạn zoom giật ra giật vào", nên chốt "bỏ 1 giữ 2": bỏ mặc định phóng xen kẽ 1,08× ở mỗi điểm cắt (mọi loại video), giữ zoom dồn chậm vào mặt ở câu then chốt (`nhan` zoom, câu `"zoom": true`). Claude sửa: luật 8, bước 7A, `ho-so-thuong-hieu/doan-noi-bat.json` `phong_xen_ke: 1.0`, `danh-sach-cat-doan-noi-bat.py` chỉ phóng khi > 1.

## Tái bản 1 — 10/11/2026: bản luật viết lại từ bảng du-an/nang-cap/tai-cau-truc-video-1.md
- Luật 11 chỉ còn "không thẻ cuối, không thanh thời gian"; tiêu đề ghim mặc định tắt (`tit_ghim: false`, bật `"pin": true`); không có câu kêu gọi thì không dừng (khối 13 sửa theo luật 4); ghim theo kiểu dẫn dắt + link bản đầy đủ.
- David "Đồng ý cả 5", câu 2: mẫu 7B bỏ "hình dày theo từng cụm lời", hình theo ý cần hiểu; 3 clip Đi trainer vẫn là mẫu về cách dựng.

## 2026-11-03
- Skill được tạo từ bản người dùng viết trong Claude Chat (4 vai Chạm · Ý chính · Hành động · Kêu gọi "Vấn đề:/Kết quả:", lằn ranh nội
  dung, mô tả + bình luận ghim). Claude viết lại phần dựng cho máy này: whisper.cpp thay faster-whisper/pip; dựng qua skill gốc thay vì
  ffmpeg `subtitles=` (ffmpeg Homebrew không có libass) và cắt giữa khung cố định. Bản cũ trong Cowork đã xoá.
- **Luôn dọc 9:16 (1080×1920)**, một bản cho mọi mục video ngắn.
- **Chỉ nguyên văn lời video, tuyệt đối không viết thêm hay đổi chữ** — "vì vậy mới gọi là highlight": xem highlight rồi xem bản
  gốc không lệch nội dung. Luật này áp dụng cả cho câu màn chốt (khác skill gốc, nơi Claude tự viết câu chốt) và mô tả bài đăng. Claude chỉ bỏ bớt chữ ở
  đầu/cuối câu; không có câu kêu gọi thì báo, không thêm chữ.
- **Ý chính + lời kêu gọi chính của TOÀN BỘ video** (không phải đoạn hay cục bộ), nên bước bản đồ cả video là bắt buộc.
- **Không thứ tự cố định**: lời kêu gọi đặt ở chỗ hợp mạch (4 kiểu bố trí), vì người xem video ngắn bị giữ/mất ở vài giây đầu;
  điểm chốt cảm xúc được làm mạnh bằng dựng (chữ to đúng lúc nói, dồn khung vào mặt, 1 s lặng sau câu hỏi), không bằng chữ thêm.
- **Độ dài 30–60 s, Claude tự cân theo nội dung** (tối đa 90 s khi bỏ bớt gãy ý).
- **Highlight cùng loại với video gốc** ("video gốc là gì thì phải ra highlight tương ứng"): podcast đồ hoạ thì podcast đồ hoạ dọc
  dựng lại từ tiếng gốc, cùng phong cách + tên tập; người nói thì người nói. Lần đầu (podcast "năng lực" 7:32) cắt thẳng hình ngang
  bị loại vì chữ nhỏ, bố cục hỏng, thanh thời gian sai; người dùng chọn dựng lại đồ hoạ dọc, không bìa, dựng 1 phương án.
- Lỗi gặp ở lần đầu và cách Claude sửa script:
  - Mốc từ Whisper lệch tới 1,6 s ở chỗ ngắt câu ("Không" bị kéo về 2,96 s, thật ở 4,6 s) nên `kiem-am-luong.py` soát theo độ lớn
    tiếng. Cách lấy khoảng lặng dài nhất cho mốc cuối từng chọn nhầm chỗ ngập ngừng giữa câu ("…nhìn nhận được ‖ mình là ai"), nên script chỉ lấy
    khoảng lặng sát sau chữ cuối, không có thì cảnh báo.
  - Giữ 1 s sau câu kêu gọi bằng tiếng nguồn làm tràn chữ câu kế ("…ở bên dưới nhé | Mình sẽ gặp lại"), nên script chèn khoảng lặng thật.
  - Tự kiểm: `cat-doan-noi-bat.py` chép lời lại bản cắt, so với lời đã chọn (bản A khớp 100%).
  - Chữ to dòng dài ("MÃI MÃI KHÔNG THỂ HIỂU ĐƯỢC") co nhỏ làm mất sức nhấn, nên chỉ lấy cụm ngắn đúng lúc nói.
  - Claude thêm biểu tượng `write` (viết ra giấy) vào mẫu chung.
- **Chuyển cảnh "tua" + thanh tập gốc** (người dùng xem bản đầu: "cần hiệu ứng chuyển cảnh giữa các đoạn, phải cho người xem cảm
  giác đây đúng là highlight trích từ một video dài, không phải video bình thường"). Người dùng chọn: tua nhanh ngắn (không chớp
  sáng, không cắt cứng), thanh thời gian của cả tập gốc + mốc (thay thanh "còn m:ss"), tiếng vút nhỏ, áp cho cả hai nhánh.
  Code: `cat-doan-noi-bat.py` chèn 0,4 s/điểm nhảy + `jumps` trong map · `ap-dung-doan-noi-bat.py` ghi `doan-noi-bat.js` · mẫu `tua.jsx`,
  `dong-thoi-gian.jsx` (chế độ highlight), `phu-de.jsx` (ẩn phụ đề lúc tua, phụ đề lên trên thanh) · `assets/hieu-ung-am-thanh/tua.wav` (tự tổng hợp)
  · `xem-truoc-ban-dung.py` trộn tiếng tua (và sửa lỗi chỉ số đầu vào màn nguồn ảnh khi có tiếng hiệu ứng). Claude không render lại bản cũ.
- Video thứ hai (IMG_3196, người nói, ngoài trời): chip chuyển cảnh thêm "⏪" khi nhảy lùi trong tập gốc (đoạn 3:53 về 2:22 hiện ⏩ là sai
  nghĩa); thanh tập gốc trên video người nói có nền tối mờ (nền trời sáng làm mốc khó đọc); điểm chốt đổi sang thẻ toàn cảnh `ages`
  khi chữ to sẽ che mặt (selfie mặt to + dồn khung). Điểm nói liền ngoài trời: tràn chữ "là" của câu trước, nên dời mốc vào chỗ âm lượng thấp.
  Thanh tập gốc đẩy phụ đề lên 40 px khiến ô mở đầu chạm phụ đề 2 dòng, nên dải lớp phủ dừng sớm 40 px khi có doan-noi-bat.js (bo-cuc.js + vi-tri-khuon-mat.py).

## 2026-11-03 (sau bản Haruku đầu)
- **Lời kêu gọi hành động BẮT BUỘC** — clip không có là không duyệt. **Chỉ một phương án tối ưu nhất** (bỏ phương án B: "chỉ cần
  1 phương án tối ưu nhất là được").
- Người dùng hỏi "xem riêng highlight có đủ kích thích tìm bản đầy đủ không?" câu trả lời là chưa: clip giải hết (vấn đề, rồi cách, rồi bằng chứng, rồi
  lời mời), thiếu kết quả lớn ("sống thọ… không bị bệnh tật nhiều"), câu mở là lời than chung, kết bị chùng xuống, nên luật 10 **chừa một
  ý cho bản đầy đủ** + chấm điểm câu mở (bất ngờ/kết quả lớn > câu hỏi day dứt > nỗi đau > lời than). Claude không thêm nhãn "BẢN ĐẦY ĐỦ".
- **Nhịp game show, MỘT skill hai tông** (`soi` sôi động / `lang` lắng; đổi tông giữa chừng được — "1 video có thể vừa có lúc
  truyền tải thông tin tích cực, vừa có tâm sự"). Video mẫu "Ngày nhận xe" chỉ là mẫu về nhịp, giữ mọi luật cũ; không cần tên vòng.
  Highlight người nói chuyển sang khung ghép clip của dung-video-theo-phong-cach (`mau-dung-ghep`: thêm `HL` thanh tập gốc, đoạn `jump`
  có chip tua, `TONE`, `MUSIC.tracks`) — script `danh-sach-cat-doan-noi-bat.py` viết sẵn danh-sach-cat.js từ phuong-an.json. Podcast: `ap-dung-doan-noi-bat.py` ghi tông +
  nhạc vào doan-noi-bat.js, `xem-truoc-ban-dung.py` trộn nhạc (sidechain hạ khi có lời), `tua.jsx` có kiểu lắng.
- **Nhạc nền cố định vài bài** (`assets/nhac/soi-*.mp3`, `lang-*.mp3`) — người dùng không muốn nhiều lựa chọn làm rối bản sắc
  kênh. Nguồn: Pixabay (giấy phép Pixabay Content License, không cần ghi nguồn). Pixabay chặn tải tự động (403) thì người dùng tự tải.
- Bản Haruku dựng lại: thêm câu mở "họ sống thọ…" (1:12) + câu hỏi "tại sao… không phải thuốc thang" (1:45); để dành ví dụ cái
  cây + nghĩa "Haruku" cho bản đầy đủ. Mốc từ Whisper ở 1:44 lệch khoảng 0,4 s ("bởi vì" tràn khi cắt ở 104,96), nên Claude chép thử từng mốc
  bắt đầu (104,85 / 105,08 / 105,25 / 105,35) tới khi sạch — cách kiểm khi "⚠ nói liền".

## 2026-11-03 (học từ 10 Shorts top lượt xem)
- Claude phân tích 10 Shorts lượt xem cao (7 quốc tế, 3 Việt Nam; 1,4–41 Tr), ghi ở `references/hoc-tu-video-dan-dau.md`. Người dùng đồng ý A–J,
  **bỏ K** ("giữ nguyên vị trí phụ đề") — phụ đề vẫn ở đáy vùng an toàn theo `kieu-phu-de.js`, dù 7/10 video mẫu đặt giữa khung.
- Luật 12 **thẻ tiêu đề mở 2–3 s** (nguyên văn cụm then chốt của câu chạm, nửa trên khung). Luật 13 **thẻ cuối dẫn về bản đầy đủ**
  khoảng 1,8 s (kiểu Have A Sip): chỉ tên tập gốc + người nói gốc + nút phát — người dùng cho phép thay cho luật "không nhãn BẢN ĐẦY
  ĐỦ" vì không có chữ tự viết. Code: montage-template `EndCard` + `ENDCARD` (Root cộng thời lượng), `danh-sach-cat-doan-noi-bat.py` đọc
  `"endcard"` trong phuong-an.json. Nhánh podcast (7B): `man-ket.jsx` + composition `the-cuoi` (remotion-template),
  `xuat-video.mjs` xuất `the-cuoi.mp4`, `xem-truoc-ban-dung.py` ghép sau video (như bìa ghép trước); `bo-cuc.js` coi `endcard` là toàn khung.
  Claude thử trên bản sao podcast-hl-nang-luc-A: 42,1 thành 43,9 s, tiếng phần chính giữ nguyên (−19,2 dB), thẻ không có tiếng.
- Lời kêu gọi là câu mệnh lệnh/giao việc nguyên văn (video đầu bảng gần như không có "hãy bình luận"); thang câu mở thêm "tiền cược",
  "kết quả trước, quá khứ sau", "câu đố cho người xem", "con số danh sách". Vòng lặp thành mặc định khi clip tối đa 35 s có cặp câu.
  Độ dài cho tới 120 s chỉ với câu chuyện hồi hộp có đáp án cuối.
- dung-video-theo-phong-cach (nhieu-doan-video.md): nhịp cắt mục tiêu `soi` 2,2–2,7 s / `lang` 4–6 s; cảnh phản ứng 0,8–1,5 s sau câu then chốt;
  `who: 1|2` viền ô phụ đề theo người nói (chuong-trinh.jsx `Caption`); ưu tiên bằng chứng thật khi nêu kết quả/con số.

## 2026-11-04
- Bộ nhận diện David chung 4 loại video: highlight người nói (montage) có dấu góc ● DAVID │ tên tập gốc + tiếng ký hiệu mở đầu;
  highlight podcast dùng chung BrandMark / Hook / thẻ cuối của remotion-template.

## 2026-11-04 — NGƯỜI XEM LÀ TRUNG TÂM (David: "các kênh lớn là hình mẫu thành công đã đạt được điều này rồi thì sao chép luôn")
Sau bản đánh giá đối chiếu với kênh lớn (thể loại nói trước camera, highlight, vlog, podcast), David duyệt kế hoạch 5 pha:
- `quy-tac-chung.md` (thư mục san-xuat-video) — một nguồn luật chung; SKILL.md chỉ giữ luật riêng. `so-lieu-mau.md` — vòng số liệu sau 7 ngày.
- **Phát hành** mọi video: 3 tiêu đề + 2 thumbnail 1280×720 (`scripts/anh-thu-nho.sh`, `assets/mau-anh-thu-nho/` — mặt có cảm xúc, tối đa 4
  chữ, nhận diện David; nguồn quay dọc tự thành khung một bên). Video ngắn không ghép bìa trước video.
- **Phụ đề video ngắn** 1–3 chữ to mỗi nhịp ngang ngực (`kieu-phu-de.js` `ShortLine`, chuẩn Hormozi/DOAC) — thay quyết định cũ "giữ
  phụ đề đáy" (bỏ đề xuất K ngày 03/11) vì David đổi định hướng. Video dài / vlog / podcast giữ hộp tối.
- **3–5 clip mỗi video dài** (thay "chỉ MỘT phương án" của 03/11 — David phân biệt: không làm biến thể của cùng đoạn, nhưng nhiều
  khoảnh khắc khác nhau thì có, chuẩn DOAC/Hormozi). phuong-an.json nhiều `options`; dự án dựng `edit-hl-<tên>-<id>`.
- **Thẻ tít mở đầu viết như tít báo** đúng ý người nói (ngoại lệ duy nhất của luật nguyên văn; chuẩn DOAC).
- **Bỏ chip tua ⏩ + thanh tập gốc** (luật 8 ngày 03/11): cắt cứng + phóng xen kẽ 1,08× (giấu điểm nối như clip kênh lớn); khoảng lặng
  ít nhất 0,45 s trong câu rút còn 0,24 s (`khoang-lang.py`, dùng chung cat-doan-noi-bat.py + danh-sach-cat-doan-noi-bat.py). Kiểu cũ: `--tua`.
  danh-sach-cat-doan-noi-bat.py xuất `SUBS` theo giây timeline + `TS(src)`; thử trên highlight-img3196: 8 câu thành 17 đoạn, chụp thử thấy phụ đề nhịp chữ.

## 2026-11-04 (học 80 video Việt)
- Claude học 20 highlight Việt (David duyệt ưu tiên 1+2): tiêu đề ghim `pinTitle` (chuong-trinh.jsx) + `"tit"` trong phuong-an.json; cảnh phản ứng `"react"` (danh-sach-cat-doan-noi-bat.py, đoạn hình khác + `audio` của câu đang nói); khung bìa 0,3 s; 60–120 s cho danh sách; hình dày theo lời ở nhánh podcast. Chưa áp dụng HL-5 (nhãn "Xem bản đầy đủ") — chờ David.
- HL-5 đã áp dụng (David duyệt): thẻ cuối highlight có nhãn cố định "XEM BẢN ĐẦY ĐỦ" (chuong-trinh.jsx EndCard, man-ket.jsx); lịch phát `endcard.schedule`.
- Che mặt / thân trên thì toàn màn hình (quy-tac-chung 4): chạy `bao-ve-lop-phu.py` ở 7A; tiêu đề ghim che đầu người nói thì tự ẩn (selfie mặt cao — Haruku 86/95 mốc).

## 2026-11-04 — TÁI CẤU TRÚC (David: "tách nhỏ để sửa một chỗ")
- Kiến trúc 5 lớp: nguyen-tac · nhan-dien · ho-so (tham số từ hình mẫu, script + khung dựng đọc) · khoi (18 khối, nội dung SKILL.md cũ chuyển nguyên văn vào) · thu-vien-tai-nguyen (một bộ thành phần hình) + mau-chuan (kiem-mau.py). SKILL.md thành công thức ngắn gọn (thứ tự khối, bảng phụ thuộc, tiêu chí đạt).
- 2 TRẠNG THÁI: cảnh `illus` (single/flow/vs/count/list, nhãn tối đa 3 chữ) ở cả 2 khung dựng; lớp chữ đè người tự vẽ toàn màn hình tối đa 4 s; thẻ/hành động bỏ câu trích dài; tiêu đề ghim tắt (hồ sơ highlight `tit_ghim: false`). Thêm 11 biểu tượng. Sao lưu trước tái cấu trúc: `~/.claude/skills/san-xuat-video.bak-2026-11-04b`.

## 2026-11-06 — clip DJI_16
- Nhạc + tiếng hiệu ứng highlight tính theo giọng như video dài; bỏ tiếng ký hiệu khi vào lời ngay giây 0 (đo Clip 1: lúc ngừng nói −19,5 dB, đang nói −17 dB; file thu −35 LUFS).
- Podcast đồ hoạ dọc: chữ chính thay phụ đề (phương án B, David chọn sau khi thấy phụ đề + đồ hoạ bị rối).
- 2026-11-06: Claude bỏ nút YouTube ở màn hình cuối clip dọc, ghi tên kênh thay vào. Chưa có bằng chứng chính thức về việc bị hạn chế, nhưng biểu tượng gần như không mang lại gì.
- 2026-11-06: David duyệt cả 3 clip "Đi trainer" làm mẫu cho các video sau; đã thêm vào `mau-chuan/mau.json`.
- Mẫu podcast đồ hoạ dọc: bỏ câu kêu gọi ghép và màn chốt bình luận (David thấy ép buộc, cụt cảm xúc), kết bằng màn hình cuối 3 s mời xem YouTube; nhạc thấp hơn giọng khoảng 23 dB (David nghe 2 mức, chọn mức này).
- Người xem clip là người xem độc lập; chấm riêng từng clip. David loại clip chỉ nói nỗi buồn.
- 2026-11-07: David thấy clip 39 giây xem riêng không hiểu gì. Luật gốc mới: clip đạt hai mục tiêu (chuyển hoá ngay trong clip, kéo sang bản dài) qua bốn câu `boi_canh`, `y_tron`, `mang_ve`, `chua_lai`. Claude tự chọn ý, không hỏi David chọn đoạn. Claude bỏ mọi số cố định về độ dài và số clip; Claude được ghép đoạn xa khi đúng mạch nhưng phải báo mốc. `cat-doan-noi-bat.py` dừng nếu thiếu `chon_y`.

## 2026-11-08 — clip người nói dọc đầu tiên (4 video cũ làm lại)
- Nguồn ngang có người nói cắt sang dọc: mặt chiếm gần hết nửa trên, nên `bao-ve-lop-phu.py` đổi thẻ tiêu đề `y: 300` thành màn đen toàn khung (mất mặt ngay giây 0, chữ lệch sát mép trái). Cách làm: tít `keep: true`, bỏ `y` thì neo vùng ngực ngay trên phụ đề, thấy rõ mặt.
- Chữ to `pow` giữa clip lặp đúng chữ phụ đề nhịp chữ và cũng bị đổi thành màn đen, nên Claude bỏ. Điểm nhấn giữa clip dùng minh hoạ (`illus` vs/list/count) và màn hành động (`action`), từ khoá tô cam trong phụ đề.
- Claude bỏ tiếng ký hiệu đầu clip khi vào lời ngay giây 0 (đúng quyết định 06/11); `danh-sach-cat-doan-noi-bat.py` đã sửa: không thêm `sting`, tít tự `keep: true`.
- Chưa sửa: màn `pow` toàn khung của khung ghép (lề trái khoảng 18 px thay vì 70 px, dải tối khác màu ở đỉnh). Nếu cần chữ to toàn khung, sửa `chuong-trinh.jsx` trước.
- Câu màn chốt dài (cả đoạn HANHDONG khoảng 250 ký tự) tràn đè phụ đề ở clip sự tập trung. `danh-sach-cat-doan-noi-bat.py` nay cảnh báo khi quá 55 ký tự; ghi `"cta_text"` (vế trọn ý, nguyên văn) vào câu `cta` trong phuong-an.json.

## 2026-11-08 — Phụ đề dọc cụm 5–8 chữ, mỗi lúc một chỗ chữ (David chốt)
- David: phụ đề 3–4 chữ cỡ 84 quá ngắn, quá to; đọc chữ motion graphic và phụ đề cùng lúc là rối. Claude đổi: cỡ 58 bằng chữ thẻ, chữ thường, viền mảnh, cụm trọn ý 5–8 chữ (tối đa 2 dòng).
- Mọi lớp chữ motion graphic (pow, illus, action, chips, thẻ tiêu đề, màn chốt…) đang hiện thì phụ đề nhường, hết lớp thì hiện tiếp đúng cụm (chuong-trinh.jsx `nhuong`, phu-de.jsx `LOP`).
- `danh-sach-cat-doan-noi-bat.py`: chia dòng bằng quy hoạch động (hết câu / dấu phẩy / trước từ nối; không ngắt sau "rất, của, là, những…"). Claude sửa lỗi chạy lại `danh-sach-cat-doan-noi-bat.py` làm nhân đôi khối `TS`.
- Chạy lại `danh-sach-cat-doan-noi-bat.py` sẽ ghi đè lớp phủ và `hl` sửa thủ công trong danh-sach-cat.js, nên người làm lưu bản cũ rồi chép lại sau.
- 2026-11-24 · Claude rà soát để máy mới (Windows qua WSL) làm đúng chỉ từ GitHub (David duyệt 4 phần): Claude sửa lỗi nhánh highlight từ podcast — ap-dung-doan-noi-bat.py đọc khoá "cac-doan" trong khi cat-doan-noi-bat.py ghi "segs" (lệch từ 14/11), và thông số nén nhạc bị danh sách bài ghi đè làm xem-truoc-ban-dung.py lỗi; nay tách khoá `nhac_thong_so`. Thử trên WSL: clip 16 s dựng trọn, −14,2 LUFS. Nguồn chỉ có tiếng: dựng podcast trước rồi mới cắt.
- 2026-11-26 · David: "không làm khung dọc nhé, bản gốc ở khung nào thì kết quả ra ở khung đó thôi, trừ khi tôi yêu cầu thì mới cần làm" nên bỏ mặc định highlight dọc 9:16 ở mọi nơi (quy-tac-chung mục 4, skill này, khối 00, khối 13, tổng quan, kênh); `danh-sach-cat-doan-noi-bat.py` lấy W/H theo video gốc.
