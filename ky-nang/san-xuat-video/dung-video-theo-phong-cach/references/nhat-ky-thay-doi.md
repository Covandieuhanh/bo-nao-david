---
description: "Nhật ký thay đổi skill dựng video theo phong cách: quyết định của David và lý do."
---

# Nhật ký thay đổi — dung-video-theo-phong-cach (quyết định của người dùng và lý do)

## 22/11/2026 (khuya, sau): điểm duyệt rõ ở từng lá, chế độ tự chạy, không lệch quy trình
- David: *"Phần nào đến bước duyệt thì vẫn phải chờ duyệt … tự động làm video cho đến khi ra kết quả luôn và bỏ qua các bước duyệt thì mới
  bỏ qua thôi, chứ còn không có trường hợp nào mà chạy lệch quy trình cả"*.
- `quy-trinh.md` mục 1: Đ1 / Đ2 / Đ3, chế độ tự chạy, không lệch; cột "Điểm duyệt" cho 22 lá; công cụ kiểm tra chặn lá thiếu điểm duyệt.
- Skill này: bước 12 sửa thành "giao ngay khi xong, David chốt rồi mới dọn (Đ2)"; nhờ đó không còn lệch với `phan-phoi-da-kenh` ("không cổng duyệt nào
  trước khi xong"); `tach-theo-huong.md`, `doan-thu.md` có mục "Điểm duyệt"; `tao-du-an.sh` chỉ thêm đường dẫn Homebrew khi máy có.

## 22/11/2026 (khuya): việc gì cũng có quy trình — cây quy trình của bộ não
- David: *"Tất cả phần chung phải có quy trình. Quy trình từ gốc rồi đến các phần khác đều phải có. Luôn đi từ gốc phát triển lên"*
  (sổ chung: `co-so-tri-thuc/bo-nho/quy-tac-viec-gi-cung-co-quy-trinh.md`).
- Skill này: thêm lá B5 `references/doan-thu.md` (đoạn thử trước khi dựng cả video); `tach-theo-huong.md` viết lại theo khung lá (thứ tự
  với 4 phần, lằn ranh mặc định giữ lời, `$SKILL`, clip ngắn, giao theo lá A6); SKILL.md định nghĩa `$SKILL`.
- Phiên thử chỉ đọc GitHub đã tự đi đúng từ gốc tới lá B4, B2, B3; các chỗ mơ hồ phiên đó chỉ ra đã được sửa, phần còn lại ghi ở báo cáo cho David.

## 22/11/2026 (đêm): GitHub luôn dựng lại được kết quả mới nhất
- David: *"luôn luôn ở các phiên mới hoặc ai mới hay thiết bị mới hoàn toàn khi đọc được github là có thể làm ra ngay được kết quả như
  những trao đổi mới nhất. Luôn luôn như vậy"*.
- Lỗ hổng phát hiện: script tách video, chụp ảnh kiểm tra, xuất chỉ nằm ở thư mục tạm của phiên; 6 script ghi cố định `h264_videotoolbox` (chỉ chạy trên Mac)
  nên máy Windows / Linux bị lỗi ở các bước làm sạch, đổi khung, nâng lớp, highlight; phiếu `phan-huong.md` và nhật ký nội dung (khối 00) chưa làm cho buổi này.
- Sửa: `scripts/tach-video.py` (cắt, tạo dự án, phụ đề dời mốc, `canh.js` khung có `g()`), `scripts/anh-kiem-canh.sh`,
  `references/tach-theo-huong.md` (nối khối 00), `references/vi-du-tach-video.json`; `_chung.py` `ma_hoa_h264()` tự chọn videotoolbox /
  nvenc / libx264, thay thế ở 6 script; SKILL.md bảng chế độ thêm dòng tách theo hướng. Luật: `AGENTS.md` luật 6 và `chuan-muc-lam-viec.md` mục 4 (5).
- Kiểm tra: chạy lại `tach-video.py` với kế hoạch hôm nay thì ra 3 video cùng thời lượng (330,6 · 259,4 · 139,1 s), phụ đề giống từng chữ; khung
  `canh.js` chạy được; dự án thử đã xoá. Đã ghi `~/Movies/tap-dji0022-2111/phan-huong.md` và nhật ký nội dung hướng 2, 3.

## 22/11/2026 (tối): tách buổi gặp dài thành nhiều video theo hướng công việc
- David: *"làm lại cả toàn bộ video đi. Cắt những đoạn thừa và phân ra thành các đoạn video theo các hướng công việc"*; áp duyệt mặc định
  (cắt giá / phí / hoa hồng, công dụng sản phẩm sức khoẻ, xem số theo ngày sinh; giữ lời "Chữa Lành Doanh Nhân", "tự do tài chính" nhưng
  không làm hình, quyết định trước khi đăng).
- Cách làm (dùng lại được): đọc lời cả buổi theo khối 20 giây, rồi gán mỗi đoạn vào một hướng (`david.md` mục 1: tài chính · trainer con
  người · giải pháp công nghệ AI; buổi này không có tài chính), rồi cắt theo mốc phụ đề đã soát, đệm 0,12 s, fade âm 50 ms, mỗi video là một dự án,
  phụ đề dời theo đoạn cắt (không chép lời lại); `canh.js` viết mốc theo video gốc, hàm `g()` đổi sang mốc đã cắt.
  Kết quả ra 3 video: `tap-may-do-giai-phap` 5:31 · `tap-ket-noi-doanh-nhan` 4:19 · `tap-hanh-trinh-david` 2:19.
- Kho bổ sung 5 dạng trong `rieng/duong-may.jsx` (mỗi dạng ghi nguồn): câu then chốt (The Diary Of A CEO trường hợp 1), lời nhắc gửi AI dạng bong bóng
  (Sang Huỳnh #5), khuôn áo và mảnh ghép (vẽ đúng vật — Ali Abdaal trường hợp 13), thẻ tên và vai trò (The Diary Of A CEO trường hợp 10).

## 22/11/2026 (chiều): không có luật bắt buộc — tận dụng tối đa kho, kho hình mẫu là thực đơn mở ra mỗi lần chọn hình
- David: *"không cần tạo ra những cái luật cố định … nguyên tắc là khi đang hiển thị nội dung, con người đang trao đổi, thì không che nội
  dung chính … motion graphics có thể tuỳ biến tự do"*; rồi *"kiểm tra trong kho dữ liệu … skill tự học được rất nhiều từ các kênh là các
  hình mẫu thành công cho từng thể loại"*; duyệt làm lại đoạn thử: *"tận dụng được tối đa toàn bộ các thẩm mỹ ở trong kho học, nhưng phải
  đưa vào cho phù hợp với nội dung, chứ không phải nhét thật nhiều … đơn giản và tinh gọn … gây ấn tượng cho người xem một cách nhẹ nhàng"*.
- Nguyên nhân: bản thử đầu chỉ dùng một kiểu (chuỗi nút) và hiệu ứng tự nghĩ ra, không mở `truong-hop-da-giai.md` (8 kênh, 19 trường hợp) và `nguon-tham-khao/`
  (Ali Abdaal và Joseph, MagentX, Sang Huỳnh, Cường Mê AI); kho có sẵn nhưng quy trình không bắt buộc mở ra.
- Sửa: `quy-tac-chung.md` mục 0 (chỉ giữ một điều: không che nội dung chính; mở kho hình mẫu mỗi lần chọn hình) · `huong-dan-lua-chon.md` bước 4d
  (thực đơn kho, cách đổi kiểu theo loại ý, dòng `Nguồn kho:`) · `soat-canh.mjs` nhắc khi thiếu `Nguồn kho:` hoặc có ít nhất 4 cảnh hình mà chỉ một nguồn ·
  `rieng/duong-may.jsx` thêm chương lớn (Sang Huỳnh #4), gạch thay (#1), thẻ lật (#6), số mốc (MagentX C và thanh tiến trình của Ali) ·
  `rieng/hieu-ung.jsx` vào / ra đổi qua cảnh (trượt, lật 3D, xoay 3D, mở màn, phóng, nhoè) và vệt sáng · `xem-truoc-ban-dung.py` đọc
  `props.tieng` (tiếng nhẹ lúc thẻ hiện / nối cảnh — Sang Huỳnh).
- Đoạn thử lần 2: `tap-thu-tham-my` (1:50), 6 cảnh, 5 nguồn kho, không che ai. Video đầy đủ 38 phút chờ David duyệt đoạn thử.

## 22/11/2026: không che, không làm mờ người đang nói; khung nhiều người giữ mọi người; thẩm mỹ đã học phải được dùng
- Tập buổi gặp đối tác (tap-dji0022-2111, 37 phút, ba người) được dựng bằng màn toàn khung nền người mờ và "người vào ô". David: *"Học nhiều
  kiểu thẩm mỹ trong skill mà không thấy được ứng dụng nhỉ. Đều là các motion graphics rất cũ. Màn hình mờ lại còn che nhân vật là hoàn
  toàn không đúng. Tôi đang nói với các đối tác trong video thì có nên chỉ hiện một mình tôi không? … Sự tự động chọn thẩm mỹ ở đâu rồi
  nhỉ?"*; đây là lần thứ hai David góp ý về màn mờ (lần đầu 21/11, tập tham quan, chỉ được ghi ở kế hoạch tập nên chưa thành luật).
- Sửa luật: `quy-tac-chung.md` mục 4 (ba gạch đầu dòng mới), khối 05 (không có chỗ thì vẽ vào chỗ trống thật, không tự chuyển sang toàn màn hình),
  khối 07 (`phong` chỉ khi không có người trên hình), `huong-dan-lua-chon.md` bước 2b + 4c (cột "toàn màn hình" chỉ khi không có người; dòng `Kiểu mới:`).
- Công cụ soát (`soat-canh.mjs`) chặn: cảnh toàn khung / nền người mờ / màn chương toàn khung khi người còn trên hình (trừ `khong_nguoi: true`);
  `o-nguoi`, `o-tron` khi `mat.js` có từ 2 người; `lower` ở khung ngang; ít hơn 2 kiểu mới so với 3 tập gần nhất. Cảnh tự vẽ tính kiểu theo
  tên component + `props.kieu`.
- Bộ mẫu Remotion thêm mẫu cảnh tự vẽ dùng lại được: `rieng/nhan-tram.jsx` (nhãn ở chỗ trống, David duyệt 21/11) và `rieng/duong-may.jsx` (dải chương
  mỏng, mạch "đường may" vẽ tiếp, bộ vét khâu dần; tấm tối có hạt, không làm mờ hình).
- David: *"render ra 1 đoạn ngắn cho tôi xem có áp dụng được thẩm mỹ mới nào không thôi chứ đừng render lại cả video vội"*; Claude làm đoạn thử
  `tap-thu-tham-my` (11:11–13:01).

## Tái bản 4 — 20/11/2026: gom ý trùng giữa các file, bảng du-an/nang-cap/nang-cap-4.md
- Ngày và lời David trong bản luật chuyển về đây (luật giữ nguyên nghĩa):
  - 19/11/2026 · `quy-tac-chung.md` mục 0 "Mọi lựa chọn tự setup theo nội dung nguồn" — David: *"mọi thứ cần phát huy tối đa được sức mạnh của AI, mọi lựa chọn đều phải được tự động setup phù hợp với nội dung của tài nguyên nguồn"*.
  - 19/11/2026 · công thức "Nhiều file của cùng một buổi nói thì nối thành một video gốc" (mẫu 1 video có đủ kho).
  - 19/11/2026 · khối 17: công cụ soát cảnh tự chạy trong `xuat-video.mjs`, `xuat-chuong-trinh.mjs`.
  - 19/11/2026 · khối 01 (chép lại đoạn ở nơi ồn), khối 02 (điểm cắt theo chỗ ngắt tiếng), khối 03 (khớp tiếng: tập marketing lệch 14 s, phát hiện sau render 54 phút), khối 04 (hai người ngồi xa máy: đoán bằng miệng và pyannote đều sai nhiều).
  - 19/11/2026 · khối 00 mục 0b phân hướng từng đoạn, ghép bản theo hướng.

## 18/11/2026: bản dài từ nhiều file của một buổi, cắt theo ý
- David: "làm 1 video dài từ 2 video gốc, cắt đi những ý liên quan đến công thức, ở phần gần cuối nếu là ý chưa trọn vẹn thì cũng cắt đi, để trở thành 1 cuộc nói chuyện giữa 2 người nhé. Cũng có làm intro cho video dài này" nên Claude sửa `references/nhieu-doan-video.md` mục 11 (chọn đoạn theo ý, một nguồn ghép, phụ đề từ bản lời theo câu và soát hết, nhạc luân phiên, màn kết YouTube).
- Mẫu ghép: `bundle-nhe.mjs` (không chép video vào thư mục tạm, vì bundle chép 4,7 GB làm đầy ổ đĩa); thẻ nhận diện cuối đặt đúng ở khung ngang (`top` theo K.V).
- `loi-ao-giac.py`: khi chép lại phân đoạn bị ảo giác, thử thêm cửa sổ lùi 4 s / 12 s (5 phân đoạn chép từ đúng đầu phân đoạn vẫn bị ảo giác).

## 14/11/2026: phạm vi luật không zoom
- David trả lời câu hỏi tái bản 3, chọn đề xuất "Chỉ cấm hình quay": luật "không zoom vào / zoom ra" chỉ áp dụng cho hình quay (video người nói); ảnh minh hoạ (Ken Burns trôi chậm) và chuyển động bên trong motion graphic (đẩy khung) vẫn được dùng. Lý do: luật 13/11 nhắm vào hiệu ứng zoom trên người nói, không nhắm vào đồ hoạ. Nguồn luật: quy-tac-chung mục 2; khối 07 mục 4, thiet-ke-canh trỏ về đó. Đã xoá dòng gotchas "chụp thử nhan không thấy zoom" (nhan.jsx đã bỏ zoom).

## Tái bản 3 — 14/11/2026: bản luật viết lại từ bảng du-an/nang-cap/tai-ban-3-video.md
- Đã bỏ dấu ngày, lời kể, chỗ mâu thuẫn với luật khỏi bản luật; mục "Nhật ký" ở cuối SKILL.md chuyển về đây:
- 2026-11-11 · David: "học rất nhiều… các skill phải tự động chọn ra được cách nào phù hợp với nội dung"; video cuộc gọi mất 4–5 giờ, "tập trung vào điện thoại" mà vẫn còn phần thừa. Claude thêm bước 6b chẩn đoán rồi tự chọn (`thiet-ke-bo-cuc/huong-dan-lua-chon.md`, `chan-doan.py`), khung chủ thể (`khung-chu-the.py`), bảng ghi chú chạy (`GHI_CHU`), mục Nhịp làm; sửa chuẩn âm, khoá render, soát cảnh chặn kiểu lỗi khung ngang và màn trống đầu cảnh.
- 2026-11-11 · David: "mục tiêu cuối cùng của tôi luôn là đưa tài nguyên vào và chờ kết quả là xong". Claude bỏ "hỏi một lần ở đầu"; khung xuất chỉ đổi khi David nói rõ khung (Claude đã tự đổi từ ngang sang dọc vì "tập trung vào khu vực điện thoại").
- 2026-11-09 · David chốt: motion graphic kể chuyện, tự do sáng tạo (luật 1 mới, khối 07); thêm cảnh tự vẽ `ve` + thư mục `chuyen-dong/src/rieng/` + mạch hình `thu-vien/mach.js`; chuyển động dùng chung `thu-vien/chuyen-dong.js`.
- 2026-11-08 · chuẩn hoá (`du-an/chuan-hoa-ky-nang.md` bước 3): hỏi một lần đầu thay "chạy một mạch không hỏi" (N1); bỏ con số cố định (N6), thẻ tiêu đề mặc định (N2), chữ "2 trạng thái" (C3), ví dụ cũ hướng sức khoẻ; màn chốt nguyên văn, không tự đặt câu kêu gọi (N4); đọc trước 3 file, luật chung trỏ `quy-tac-chung`; đánh dấu bước nhẹ 1·2·5; rút gọn mô tả; thêm "Xong khi"; video mẫu chỉ có link thì được tải 720p chỉ để học, học xong thì xoá (khớp `thiet-ke-bo-cuc`). Chi tiết các quyết định trước: `references/nhat-ky-thay-doi.md`.


## 11/11/2026: tự chọn theo nội dung + khung chủ thể + bảng ghi chú chạy
- David: "cái quan trọng nhất là học rất nhiều, tôi cần các skill phải tự động chọn ra được cách nào phù hợp với nội dung của video"; video cuộc gọi mất 4–5 giờ, "tập trung vào điện thoại" mà vẫn còn phần thừa, video nhiều nội dung cần hiện nhiều thông tin hơn. Claude thêm `thiet-ke-bo-cuc/huong-dan-lua-chon.md` và `chan-doan.py` (bước 6b), `khung-chu-the.py` (kèm `--thu`), `bang-ghi-chu.jsx` (`GHI_CHU`), `khung.js`; sửa `chuan-am.py`, khoá render, `soat-canh.mjs`, `xem-truoc.mjs`, `vi-tri-nhan.py`; mục Nhịp làm; bảng lỗi ở gotchas.

## 11/11/2026: xong tập thì đưa lên Drive, xoá trên Mac
- David: "máy mac này chỉ còn đóng mỗi vai trò là khi đang thực thi cái gì thì có dữ liệu và tài nguyên của cái đó thôi"; "nhớ lưu lại để lần sau tự động làm việc cho gọn và nhẹ máy mac". Lý do: ổ Mac 228 GB đã đầy. `don-tap.py --xoa` xoá hẳn file tạm (bỏ Thùng rác), rồi `luu-drive.sh` (mới, kèm `kiem-tai-len-drive.swift`, `giai-phong-drive.swift`) đưa tập lên Drive `sao-luu-mac/video`, chờ lên mây, so khớp, giải phóng cache Drive, xoá trên Mac. Đã sửa SKILL bước 12 và Xong khi 8, khối 17, quy-tac-chung 8, cat-highlight, podcast, tong-quan.
## Tái bản 2 — 10/11/2026: bản luật viết lại từ bảng du-an/nang-cap/tai-cau-truc-2-video.md
- Nguồn luật bỏ phóng xen kẽ ở điểm cắt là quy-tac-chung mục 2 (kèm lý do); khối 02, ho-so-thuong-hieu/doan-noi-bat.md, cat-highlight luật 8 trỏ về đó. quy-tac-chung mục 8 trỏ về thói quen chung (hỏi, lệnh nền, mật khẩu, báo cáo), chỉ giữ phần riêng của video. Đã bỏ câu sao chép ở gotchas, phan-phoi-da-kenh; sửa đường trỏ "hình của chính video" về khối 14. Đã viết lại 6 câu bị công cụ đo phát hiện nhầm ("thay cho", "THAY", tên file có ngày).

## 10/11/2026 — Bỏ phóng xen kẽ 1,08× ở điểm cắt
- David xem đoạn thử tap-thu-tai-ban-video-1: "tôi không thích mấy đoạn zoom giật ra giật vào" rồi chốt "bỏ 1 giữ 2": bỏ mặc định phóng xen kẽ 1,08× ở mỗi điểm cắt (mọi loại video), giữ zoom dồn chậm vào mặt ở câu then chốt (`nhan` zoom, câu `"zoom": true`). Sửa: quy-tac-chung §2, khối 02, `ap-dung-lam-sach.py` + `de-xuat-lam-sach.py` mặc định `zoom: "none"`.

## Tái bản 1 — 10/11/2026: bản luật viết lại từ bảng du-an/nang-cap/tai-cau-truc-video-1.md
- Gom bản luật cả bộ video: mỗi luật một nguồn duy nhất, bỏ dấu ngày và câu "thay luật cũ"; luật cũ đã bị thay (hook mặc định, câu chốt tự viết, con số mật độ, nhạc 20/30 LU, chép màu/font từ mẫu, nút phát ở thẻ cuối) bỏ hẳn khỏi bản luật.
- David trả lời 5 câu: "Đồng ý cả 5", nên: (1) mọi video có điểm nhấn nhưng chỉ vài kiểu hợp nội dung, bỏ "trộn nhiều loại" và ví dụ "khoảng 3 illus + khoảng 4 nhan"; (3) vlog: thẻ tiêu đề chỉ tên chương trình / tên nơi / lời nguyên văn, bỏ "TẬP NÀY CÓ GÌ?" và lời mời tự viết ở kết; (4) phan-tich-video-mau "Xong khi" 2 là chữ ký nhận diện không đổi; (5) việc thật được chấm bằng một đoạn ngắn từ tap-5-nguyen-tac-tien.
- Claude tự phân xử theo ngày / mẫu đã duyệt: hashtag 2–3; bình luận ghim theo kiểu dẫn dắt (bỏ mẫu "Làm thử trong 48 giờ"); không hỏi câu chốt ở lần hỏi đầu.

## 2026-11-01
- Skill được tạo từ dự án DJI (12 nghề). Phong cách mặc định: nền tối, nhấn cam, Barlow Condensed in hoa và Be Vietnam Pro; phong cách này đã được duyệt.
- Làm sạch: cắt phần thừa đầu/cuối và câu nói lại; KHÔNG cắt ngập ngừng/khoảng lặng ("muốn video thực tế nhất").
- Đổi khung: dọc sang ngang là video ở giữa và chữ hai bên (pillar); ngang sang dọc là khung bám người nói, nhảy cắt.
- Bỏ màn hình nguồn ảnh 5 s ở cuối, thay bằng `nguon-anh.txt`. Bỏ nhãn kỹ thuật (×1,6, slow-mo).
- Phụ đề đầy đủ ở đáy vùng an toàn; lớp phủ thu 78% ngay trên phụ đề. Chữ hiệu ứng chỉ trích, không diễn đạt lại ("Haruku").

## 2026-11-02
- **Lớp phủ không được che người nói**, vị trí không cố định nên dùng `vi-tri-khuon-mat.sh` (dò mặt Vision, neo đáy/đỉnh). Nguyên nhân: video
  IMG_0499 quay trong xe, thẻ ở đáy che cằm/miệng.
- **Dự án CapCut** khi được yêu cầu thì dùng `build_capcut.py` (pycapcut). CapCut Mac đọc `draft_info.json` + đường dẫn kiểu
  `/Users/<tên>/Movies/CapCut/...`; phụ đề là chữ CapCut, font Be Vietnam Pro (người dùng thích font này). Dự án đã mở được.
- Template thêm kiểu cảnh: card `vs`, `ages`, `quote`; `steps` có nhãn `n`; montage `kicker`; toàn màn hình `gens`, `build`.
- Template dùng chung với skill mới **dung-podcast** (Stage, Timeline, podframe, FullScreenLand); chỉ bật khi `project.podcast`.
- **Chữ to tiếng Việt đủ dấu, không chồng dòng** (`VN` trong khung-podcast.js) bật cho cả skill gốc: giãn dòng 1,14, chừa chỗ dấu
  theo cỡ chữ, chữ to tối đa 120 px, hook tối đa 118 px. Đã thử trên IMG_0499: vẫn gọn trong dải lớp phủ.
- `xem-truoc-ban-dung.py` ghép `bia.mp4` (nếu có) trước video; dùng cho bìa podcast (`COVER`, `anh-bia.jsx`).
- **Chữ to sau một dòng khác chừa chỗ dấu** (`aboveGap` = 0,4 cỡ chữ) và chữ không đặt sát khung ảnh; người dùng chỉ ra
  "GỐC RỄ" đè dòng "Phải nuôi đến cả năm trời", dòng đó chạm ảnh. Áp dụng cho montage (dọc + ngang), tên người nói, "BƯỚC n".
- **Lớp phủ không bao giờ đè/nằm dưới phụ đề**: mép chặn bắt buộc ở đỉnh dải phụ đề trong `Place` (người dùng chỉ ra ô bị phụ đề đè).
- **GIỮ Ô CHỮ HIGHLIGHT** (thẻ, chữ to); Claude đã thử thay toàn bộ ô chữ tóm ý bằng hình động (biểu tượng + mũi tên + ✓/✗, chữ chỉ còn
  tên riêng và số; bản thử `~/Movies/edit-img3196-hinh-dong`). Người dùng xem và **không thích bằng bản ô chữ**: "vẫn nên để ô
  highlight chữ thì đẹp hơn". Vì vậy Claude KHÔNG đề xuất lại kiểu chỉ-hình-động; biểu tượng vẽ chỉ dùng thay ẢNH trong thẻ/montage.
- **Thẻ là màn hình toàn cảnh** (sau khi giữ ô chữ): người dùng muốn mọi ô thẻ thành một màn toàn cảnh có hình động (giống tinh
  thần cảnh "cái quả", không học theo y hệt); chỉ áp dụng cho ô thẻ; chữ to không nền, hook, tên người nói vẫn trên video. Chữ trên màn
  toàn cảnh là **nguyên văn đầy đủ** câu nói ("không được tự tóm tắt hay nói ý khác") vì toàn cảnh dễ đọc. Mỗi cảnh 4–8 s (người
  dùng chọn rút ngắn để mặt vẫn hiện khoảng 60%). Code: `the-toan-man.jsx` (dùng lại variant thẻ, `CardInline`), `card` trong `FULL`.
- **Tinh gọn** (người dùng: "tối giản và tinh gọn nhất nhưng vẫn thể hiện được ý chính"): phụ đề ẩn khi thẻ toàn cảnh hiện câu
  nguyên văn (không đọc 2 lần); khung thẻ có quote chỉ giữ hình động + nhãn; khoảng 1 hiệu ứng / 15–20 s, chữ to tối đa 3–4 lần, nghỉ ít nhất 5 s
  giữa hai cảnh chữ; podcast: ý đang bàn đổi 40–90 s. Lý do: bản Haruku có 22 cảnh / 4:28, cộng thêm phụ đề và câu trích, nên có quá nhiều chữ.
- Khe giữa 2 dòng chữ to nới 0,1 thành 0,24 cỡ chữ (dấu dòng trên/dưới chạm nhau ở "ý đang bàn" podcast); áp dụng cho sân khấu, chữ to,
  bìa, nhãn tự xuống dòng; ô màu hook giữ khe nhỏ.
- **Một chuẩn hiển thị cho mọi chế độ**: phụ đề chế độ ghép trước đây là chữ rời không nền, các dòng sát vào nhau; nay đọc chung
  `kieu-phu-de.js` với chế độ 1 video/podcast (hộp nền tối, giãn 1,28, đáy vùng an toàn); chữ to ở chế độ ghép (Rise, chữ nổ,
  lời kết, tiêu đề) dùng cùng chuẩn chừa dấu/giãn dòng. Khung trích dẫn clip giữ nguyên (người dùng khen chuẩn).
- **Minh hoạ mặc định là biểu tượng vẽ** (`bieu-tuong.jsx`, khoảng 45 hình) thay ảnh; người dùng so sánh 2 bản DJI và chọn bản không ảnh. Ảnh
  thật chỉ cho: địa danh cụ thể, nhân vật có thật/lịch sử, tư liệu quá khứ, minh chứng xác thực, sản phẩm cụ thể. Số liệu
  luôn bằng hiệu ứng, đúng con số người nói.
- **Nâng khung** (dự án ghép 9515): nhiều đoạn nhân vật tụt xuống nửa dưới, nửa trên trống, phụ đề/thanh nút che mất hình chính, nên
  đẩy hình lên tối đa 400 px và lấp đáy bằng hình mờ (phóng tối đa 1,25× khi cần hơn). `scripts/nang-khung.py` tự tính theo mặt; chế độ ghép thì dùng `nang-lop.js`
  (đặt thủ công `lift` trong danh-sach-cat.js cho đoạn đồ vật), chế độ 1 video thì ghi cố định vào video-goc.mp4 sau bước làm sạch (3b').
- **Mục tiêu video là hiểu và làm theo** (người dùng chốt): câu hành động trong lời thì màn `action` tự sinh (biểu tượng, dấu tick và nguyên
  văn câu); MỌI video kết bằng màn chốt `cta` khoảng 4 s ("David rất mong có được sự góp ý của bạn tại phần bình luận!", keu-goi-hanh-dong.js); hình
  lùi vào khung để vẫn thấy vẫy tay/like. Lý do: đánh giá cho thấy video giúp hiểu nhưng chưa thúc đẩy người xem hành động.
- **Câu màn chốt không cố định** (người dùng chốt): Claude tự sáng tạo câu chốt phù hợp với từng video sau khi nắm nội dung — một hành động (bình luận/lưu/theo dõi/chia sẻ, biểu tượng theo kiểu), giọng David, không bịa đặt; câu cố định trong keu-goi-hanh-dong.js chỉ còn là dự phòng.
- **Tick + "ting" ở màn chốt** (người dùng yêu cầu): câu chốt hiện xong thì dấu tick nhỏ bật nảy ở góc biểu tượng, kèm tiếng chuông ting (assets/hieu-ung-am-thanh/ting.wav, tự tổng hợp, không bản quyền) để kích thích người xem hành động.

## 2026-11-03 — ghép nhiều clip: thời lượng theo nội dung
- Người dùng chốt: thời lượng video ghép **tự cân theo nội dung**, không cắt theo tỉ lệ/con số mặc định; có khi chỉ giữ 50%
  (quay trong túi, tối đen, cảnh không rõ), có khi giữ 100% (cảnh nào cũng rõ, không trùng). Ghép khác highlight: không tự rút
  thành bản 3–5 phút hay video ngắn. Bỏ trùng lặp theo bước 2b sẵn có.
- **Tiêu chí giữ/bỏ cảnh** (Claude đề xuất, người dùng chốt 5 điểm) được ghi vào nhieu-doan-video.md mục 2c: ưu tiên cảm xúc > câu chuyện >
  nhịp > hình đẹp; người khác trong khung giữ hết ("vlog không chỉ một mình mình"); đoạn trầm quá thì tua (video cần nhịp);
  quay lại cùng câu/cảnh thì Claude tự chọn lần tốt nhất; có cảm xúc là giữ dù rung; cảnh tâm linh giữ, **tông bắt buộc khớp cảnh**.

## 2026-11-03 (học từ 10 Shorts top lượt xem — xem cat-doan-noi-bat/references/hoc-tu-video-dan-dau.md)
- Chế độ ghép clip: nhịp cắt mục tiêu, cảnh phản ứng, viền ô phụ đề theo người nói (`who` trong `SUB`), bằng chứng thật cho
  kết quả/con số (nhieu-doan-video.md mục 2c, 4). Thẻ cuối `ENDCARD` cho highlight (mục 10). Vị trí phụ đề KHÔNG đổi (người dùng chốt).

## 2026-11-04 (vlog leo núi — người dùng chỉ ra sau khi xem bản render)
- Thẻ địa điểm đè phụ đề 2 dòng (Location top 1060 cố định). Montage chuong-trinh.jsx: thêm `CAP_H = 140` / `CAP_TOP` / `LOW_Y` (như
  CAP_H chế độ 1 video); Location, NameCard, Replay canh ĐÁY vào `LOW_Y`; Chips mặc định tính từ `LOW_Y`.
- 4:15–4:33 (c13 119,5 s đến hết): giữ vì có lời hỏi đường, nhưng hình còn trong túi rồi lật ngang/lộn ngược nên phải cắt.
  khung-loi.py: ngưỡng TÚI/CHE 30 thành 60 (clip thường không khung nào < 60), gộp khoảng cách < 1 s. danh-sach-cat-vlog.py: cảnh báo ⚠ khi đoạn giữ trùng với
  khung-loi.txt, kèm tờ soát `kiem-tra/cac-doan/` 1 khung/giây, xem hết trước khi render. Luật: hình hỏng thì bỏ kể cả có lời.

## 2026-11-04 (khung vlog theo kênh Jessie Luong — người dùng chọn làm chuẩn)
- Học 13 vlog của kênh (2021 đến 2026), theo kiểu GẦN ĐÂY: mở đầu là đoạn ghép 9–20 s gồm các cảnh ấn tượng nhất cả chuyến và thẻ tiêu đề trên đoạn
  ghép, rồi chào + bối cảnh, hành trình theo thời gian, kết bằng lời tổng kết của người quay. Claude tự chọn kiểu 1/2 theo nội dung.
  nhieu-doan-video.md 2d; danh-sach-cat-vlog.py `intro` (cảnh m1…, `voice`, `{"montage": true}` cho kiểu 2), tiêu đề `over` (nền mỏng) tự nằm ở dải
  cảnh câm. Luật: đoạn ghép đa dạng, tối đa 2 cảnh mặt cận (lần chạy thử đầu ra 6/9 cảnh selfie giống nhau).
- danh-sach-cat-vlog.py: biến `n` (đếm đoạn) bị ghi đè khi chia dòng phụ đề, dẫn tới trùng id đoạn (c12_2, c20_3…), nên phụ đề/thẻ của đoạn trùng có thể
  lệch giờ (bản vlog leo núi đã render mắc lỗi này). Đã đổi tên thành `nl`; id đánh số liên tục theo clip (clip tách hai mục vẫn không trùng).
- Nhạc đoạn ghép mở đầu vlog: 2 bài riêng `intro-soi` (Upbeat — alex-morgan) / `intro-lang` (Inspiring Documentary — AtlasAudio), Claude
  chọn theo nội dung (`intro.music`). Cảnh câm mặc định dài 2 phách, điểm vào bài canh cho điểm cắt rơi đúng phách; nhạc to hơn ở dải
  cảnh câm (loudRanges). Không lấy nhạc của kênh mẫu (bản quyền / Content ID + luật không tải từ YouTube).
- xuat-chuong-trinh.mjs: `node xuat-chuong-trinh.mjs <từ s> <đến s> <tên.mp4>` render riêng một đoạn để xem thử.
- Tiêu đề trên đoạn ghép (`over`): một dòng gọn tối đa 130 px, canh đáy vào LOW_Y, bỏ nền lưới; khi chạy thử 3 video Haruku (toàn selfie,
  mặt ở nửa trên khung) thì tiêu đề 2 dòng 250 px che mặt. Vlog toàn cảnh tự quay mặt: đa dạng bằng nền / trang phục / cử chỉ.
- Độ dài intro không cố định (người dùng chốt): theo chất liệu và cảm xúc; chỉ dùng cảnh thật sự khác nhau; video tự quay mặt nói khoảng 5–8 s
  (1 câu then chốt và tiêu đề trên 1–2 cảnh). Intro Haruku 16,7 s theo luật này còn khoảng 7 s.
- danh-sach-cat-vlog.py phụ đề (vlog Haruku 2026-11-04): (1) mốc TỪNG CHỮ khớp moc-tung-tu.srt bằng difflib, chữ ngoài đoạn giữ bị bỏ; trước đó
  câu nối dài làm tràn chữ của đoạn đã cắt ("…tốt lành thật ra", "David xin chào…"); (2) nối dòng Whisper: chữ hoa không phải tên
  riêng (PROPER = chữ hoa giữa dòng) thì câu mới ". "; (3) ngắt dòng ưu tiên khoảng ngừng giọng nói, cấm kết dòng bằng từ đệm/nối
  (END_BAD) và cấm tách cặp chữ lặp ít nhất 2 lần / chữ trong `fix` (COMPOUND: bí mật, đi bộ, phạm trù…). Từ ghép chỉ xuất hiện 1 lần vẫn
  có thể bị tách ("giải / trình"), nên cần soát bằng mắt.
- Âm lượng vlog ghép (người dùng chỉ ra 2026-11-04, Haruku): (1) tao-dung-ghep.sh cân GIỌNG từng clip về −20 LUFS (gain tuyến
  tính + alimiter, tối đa +18 dB), vì 3 clip gốc −17 / −34 / −23 LUFS nghe chỗ to chỗ nhỏ; (2) danh-sach-cat-vlog.py đo giọng thật rồi đặt
  mức nhạc khi có lời thấp hơn giọng 20 LU (duck), chỗ ngừng nói ×1,6 (×2,5 nghe lên xuống thất thường). Intro giữ mức `loud` 0,3.
- Hiệu ứng trong vlog ghép (người dùng chỉ ra: "không thấy hiệu ứng, animation"): ke-hoach.json `fx` — pow (chữ to trích lời, tự canh
  đáy LOW_Y), chips (danh sách hiện theo lời), action (thẻ câu hành động), zoom (dồn rồi tự nhả sau `hold` 2,5 s); khoảng 1 / 20–30 s.

## 2026-11-04 — BỘ NHẬN DIỆN DAVID (người dùng chốt: "xem bất kỳ thể loại nào cũng nhận ra cùng một người làm")
- thuong-hieu.json (mau-remotion/src, nguồn duy nhất; tao-dung-ghep.sh chép sang dự án ghép). Dấu góc ● DAVID │ chủ đề: BrandMark
  (lop-phu.jsx cho Captions 1 video, Stage podcast) + Hud (chế độ ghép, highlight người nói). Hook đổi sang mẫu tiêu đề chung (dòng
  nhỏ cam + gạch cam + chữ trắng/cam, bỏ ô nền màu). Tiếng ký hiệu sting.wav ở tiêu đề mở đầu (xem-truoc-ban-dung.py · danh-sach-cat-vlog.py · danh-sach-cat-doan-noi-bat.py).
- Video 1 người / podcast: nhạc kênh rất nhỏ (thấp hơn giọng 22 LU, `project.music` đổi bài / '' tắt) và loudnorm −14 LUFS bản cuối.
- Thẻ cuối nhận diện (chủ đề + DAVID, không nút phát) cho mọi video có chủ đề (man-ket.js ENDCARD_ON); highlight giữ thẻ dẫn bản đầy đủ.
- Chế độ ghép: cảnh minh hoạ VẼ `scene` (bieu-tuong.jsx dùng chung, sed import sang thuong-hieu.js) — 3–4 cảnh / video, câu nguyên văn sáng dần.
- Chống chữ đè phụ đề TẬN GỐC ở chế độ ghép (người dùng: "bị rất nhiều lần rồi mà vẫn chưa khắc phục"): Chips neo đáy + tự thu cỡ một
  dòng; chuong-trinh.jsx cắt mọi lớp không toàn màn hình ở CAP_TOP; phụ đề ẩn dưới mọi lớp toàn màn hình (FULLSCREEN); danh-sach-cat-vlog.py in lệnh chụp
  soát ở cuối từng lớp chữ. Chế độ 1 video (bo-cuc.js Clip) và podcast (PF.contentBottom) đã có chặn bắt buộc từ trước.

## 2026-11-04 — NGƯỜI XEM LÀ TRUNG TÂM (David: "các kênh lớn là hình mẫu thành công đã đạt được điều này rồi thì sao chép luôn")
Sau bản đánh giá đối chiếu với kênh lớn (thể loại nói trước camera, highlight, vlog, podcast), David duyệt kế hoạch 5 pha:
- `quy-tac-chung.md` (thư mục san-xuat-video): nguồn duy nhất của luật chung; SKILL.md chỉ giữ luật riêng. `so-lieu-mau.md`: vòng số liệu sau 7 ngày.
- **Phát hành** mọi video: 3 tiêu đề và 2 thumbnail 1280×720 (`scripts/anh-thu-nho.sh`, `assets/mau-anh-thu-nho/`: mặt có cảm xúc, tối đa 4
  chữ, nhận diện David; nguồn quay dọc tự thành khung một bên). Video ngắn không ghép bìa trước video.
- **Phụ đề video ngắn** 1–3 chữ to mỗi nhịp ngang ngực (`kieu-phu-de.js` `ShortLine`, chuẩn Hormozi/DOAC), thay quyết định cũ "giữ
  phụ đề đáy" (bỏ đề xuất K ngày 03/11) vì David đổi nguyên tắc định hướng. Video dài / vlog / podcast giữ hộp tối.
- **Làm sạch cắt khoảng lặng ít nhất 0,45 s và tiếng đệm "ờ/ừm"** mặc định (`de-xuat-lam-sach.py`, `am-luong-05.txt` trong phan-tich-lam-sach.sh),
  thay luật cũ "không cắt ngập ngừng" (2026-11-01, "muốn video thực tế nhất"). Bản tự nhiên: `phan-tich-lam-sach.sh <dự án> tu-nhien`.
  Vlog ghép giữ nhịp tự nhiên. Thử trên IMG3196 (46,7 s): 8 khoảng lặng 0,5–0,8 s được cắt.
- Montage (highlight): `SHORT` trong danh-sach-cat.js bật phụ đề nhịp chữ, bỏ chớp trắng ở điểm cắt; `HL.bar = false` tắt thanh tập gốc.
- **Thumbnail chỉ khi video xuất NGANG và đăng YouTube** (David chốt cùng ngày: "chỉ có đăng video youtube thì mới cần ảnh bìa ngang, mà còn phải là video ngang"). Video xuất ngang thì hỏi "có đăng YouTube không?" lúc đầu; video dọc chỉ có mốc khung bìa.

## 2026-11-04 (học 80 video Việt)
- Học 20 video nói trước camera + 20 vlog Việt (David duyệt ưu tiên 1+2): màn kết YouTube 15–20 s (`man-ket-youtube.jsx`, `project.ytEnd`, ke-hoach.json `ytEnd`, nhạc kênh nhỏ trong xem-truoc-ban-dung.py / chuong-trinh.jsx); thumbnail kiểu Việt (`THUMB_L3`, `THUMB_NUM`, `THUMB_BADGE`); nhãn số `listItem`; màu theo nghĩa `+`/`-` trong hl (kieu-phu-de.js); thẻ tóm tắt để lưu; `CHAPTERS` + `chuong.py`; `doan-gioi-thieu.py`; vlog: kiểu mở 3 "nhiệm vụ", thẻ vòng chỉ cho vlog thử thách, flycam mở nơi mới, nhãn giá/con số, tách phần > 25 phút. Cảnh câm intro 2 phách khoảng 1,06 s đã đúng nhịp video Việt nên giữ. Chưa áp dụng TH-1 (cắt khoảng lặng nhẹ hơn cho video dài), chờ David.
- Đã áp dụng TH-1 (David duyệt): video dài hơn 3 phút chỉ cắt khoảng lặng từ 1,2 s trở lên, rút còn 0,5 s, giữ tiếng đệm (de-xuat-lam-sach.py); tối đa 3 phút giữ 0,45 s. PO-6: lịch phát `project.schedule` / ke-hoach.json `schedule` trên thẻ cuối + màn kết YouTube.
- Sửa sau khi dựng tờ mẫu (2026-11-04): phụ đề nhịp chữ giữ liền cụm từ khoá trong `hl` (không tách "TỎ / RÕ"), không gộp nhịp quá 16 ký tự (không còn rớt dòng).
- **Che mặt / thân trên thì toàn màn hình** (David chốt 2026-11-04): vi-tri-khuon-mat.py coi đầu, cổ, vai, ngực là vùng cấm; không có chỗ trống thì `full: true` + `end` tối đa 4 s trong vi-tri.js (bo-cuc.js Place vẽ nền + phóng giữa, goc.jsx rút thời lượng). Chế độ ghép: `bao-ve-lop-phu.py` ghi vào bao-ve.js (chuong-trinh.jsx `FullOv`), tiêu đề ghim che đầu thì ẩn. Thử trên Haruku: thẻ hook 1 video và thẻ tiêu đề highlight chuyển thành toàn màn hình, tiêu đề ghim ẩn (che đầu 86/95 mốc).

## 2026-11-04 — TÁI CẤU TRÚC (David: "tách nhỏ để sửa một chỗ")
- Kiến trúc 5 lớp: nguyen-tac · nhan-dien · ho-so (tham số từ hình mẫu, script + khung dựng đọc) · khoi (18 khối, nội dung SKILL.md cũ chuyển nguyên văn vào) · thu-vien-tai-nguyen (một bộ thành phần hình) + mau-chuan (kiem-mau.py). SKILL.md trở thành công thức gọn (thứ tự khối, bảng phụ thuộc, tiêu chí đạt).
- 2 TRẠNG THÁI: cảnh `illus` (single/flow/vs/count/list, nhãn tối đa 3 chữ) ở cả 2 khung dựng; lớp chữ đè người tự vẽ toàn màn hình tối đa 4 s; thẻ/hành động bỏ câu trích dài; tiêu đề ghim tắt (hồ sơ highlight `tit_ghim: false`). Thêm 11 biểu tượng. Sao lưu trước tái cấu trúc: `~/.claude/skills/san-xuat-video.bak-2026-11-04b`.

## 2026-11-05
- **Thumbnail / ảnh bìa chỉ dùng hình của CHÍNH video đang làm** (David chỉ ra: thumbnail podcast "Mục tiêu và sứ mệnh" lấy mặt từ vlog Miếu Bà Cam nên sai). Podcast không mặt thì nền là khung đồ hoạ của chính podcast; ảnh người nói chỉ khi David gửi riêng cho tập đó. Không đưa "lấy ảnh từ video cũ" thành lựa chọn khi hỏi. Luật ghi ở quy-tac-chung 7, khối 14, podcast SKILL, anh-thu-nho.sh.
- **Nhạc nền theo tuyến nội dung + nhạc nhỏ khi nói** (David: "nhạc nền hơi to… tông chưa phù hợp… phải tự chọn được nhạc theo tuyến nội dung"). Hồ sơ chung `nhac`: bảng tuyến ứng với bài, `project.tuyen` bắt buộc (render_preview dừng nếu thiếu — bỏ mặc định soi-1); nén theo giọng tương đối (ngưỡng giọng − 14 dB, tỉ lệ 20, nhả 1,5 s): nhạc khi nói 17 thành 30–33 LU dưới giọng. Tuyến kiến thức chờ David tải 1 bài ambient.

## 2026-11-06
- **Podcast: hình phủ khoảng 30% thời lượng**, cân theo nội dung (David, sau khi xem video dài chỉ phủ 12%). Mẫu: `~/Movies/podcast-dji-20261105`, 30 cảnh, 34%.
- **Chuẩn âm lượng chung mọi đầu ra** (David): mức của 3 clip Đi trainer thành hồ sơ chung, thêm `chuan-am.py` chạy cuối mỗi lần xuất (khối 09). Màn kết YouTube đổi từ mức nhạc cố định sang mức tính theo giọng.
- `project.sting: false` bỏ tiếng ký hiệu đầu video khi lời vào ngay giây đầu (David chọn cho video dài "Đi trainer").
- **Mẫu ảnh bìa podcast không mặt** (David duyệt sau khi xem 3 bản): nền hoạ tiết, một hình vẽ, tiêu đề ngắn, "DAVID · PODCAST". Bỏ bản micro vì chỉ nói định dạng; bỏ bản liệt kê 3 bước vì lộ giải pháp. `anh-thu-nho.sh` thêm nguồn `-`, `THUMB_HINH`, `THUMB_TAG`.
- **Học từ HyperFrames + Motion Studio, không cài** (David duyệt): bỏ lơ lửng, vòng xoay, quầng nhấp nháy; hiệu ứng ra ngắn hơn hiệu ứng vào; kiểu vào theo ý câu (khối 07). Thêm sơ đồ `xay-tang`, `doi-trang-thai`, `chuyen-giao`. Thêm `scripts/soat-canh.mjs` (khối 17) và `scripts/chu-tren-man.mjs` (khối 03). Bản trước: `~/.claude/skills/san-xuat-video.bak-2026-11-06-hoc-motion`.

## 2026-11-07
- **Điểm nhấn trên người** (David: "mọi video đều phải có motion graphics, nhiều loại, không chỉ toàn màn hình"): cảnh `nhan` (thanh-phan/nhan.jsx) — zoom dồn vào mặt (xem-truoc-ban-dung.py, zoompan theo `mat.js`), làm tối viền, chữ nhấn / biểu tượng cạnh mặt. `vi-tri-nhan.py` tính vị trí mặt (chạy trong vi-tri-khuon-mat.sh, cả khung ngang). Nới luật 2 trạng thái: `nhan` thuộc TWO_KEEP. soat_canh kiểm cảnh `nhan`. Vlog / highlight: dùng `zoom` + `pow` sẵn có của khung ghép (đặt `keep: true` để không bị đổi toàn màn hình).
- `ap-dung-lam-sach.py`: file DJI có luồng phụ làm ffprobe in thêm dòng thì lấy dòng đầu.
- Màn chốt `cta` có bản khung ngang (hanh-dong.jsx): ô video 16:9 rộng 56% giữa trên + câu chốt bên dưới (bản dọc làm câu chốt rơi khỏi khung ngang).
- **Chữ trên video là nguyên văn lời David** (David: "không được sáng tạo sai lời chính xác của tôi"): bỏ thẻ tiêu đề mặc định, màn chốt dùng câu David nói cuối video, không số chạy, không bỏ chữ đổi nghĩa. quy-tac-chung 1, khối 06, 08.

## 2026-11-08 · nhạc (vlog The View Vũng Tàu)
- David: "đã tải rất nhiều nhạc để phù hợp với từng nội dung… sao không tự đánh giá để tự ghép nhạc phù hợp". Claude tự chọn nhạc theo tuyến, không hỏi, bỏ câu "nhạc nghe điện tử" (nhieu-doan-video.md 8).
- Kho nhạc thêm 5 bài từ `~/Music/nhac-nen`: du-lich-1/2, kham-pha-1/2, ngam-canh-1; tuyến mới du_lich, kham_pha, ngam_canh (`ho-so-thuong-hieu/chung.json`).
- Mức cân từng bài gom về nguồn duy nhất `nhac.muc` (vlog_edl, render_preview, hl_edl, hl_apply); chuong-trinh.jsx ghép tự lấy khi edl không ghi gain; nguyên nhân gốc: edl viết thủ công thiếu gain thì nhạc to gấp đôi.
- danh-sach-cat-vlog.py: ke-hoach.json `tuyen` chọn bài đoạn sôi, `nhac: {soi, lang}` chỉ định thủ công.

## 2026-11-08 · dọn file tạm
- David: "cập nhật vào quy trình dọn để lần sau không cần hỏi lại tôi nữa trừ khi vướng vào file đang làm dở của phiên khác". David chốt nên `don-tap.py --xoa` chạy trực tiếp.
- don-tap.py nhận cả `~/Movies/vlog/<tên>`; tự bỏ qua (⏸, hỏi David) khi có tiến trình chạy trong dự án, kịch bản sửa sau bản cuối, hoặc chưa có bản cuối.

## 2026-11-08 · nhiều người trong khung + người đang nói (David: "tất cả motion graphics không có gì cố định, bố trí tự động cho phù hợp nhất")
- `vi-tri-nhan.py` viết lại: mọi người trong khung (k-means chỗ ngồi, người quay nghiêng vẫn được tính) + người đang nói (pyannote tự chạy
  khi ít nhất 2 người, ghép giọng với miệng). Khoá cũ cx/cy/w/h/l/r chỉ vị trí người đang nói, nên zoom dồn đúng người nói.
- `src/thu-vien/cho.js` (mới): khoảng trống quanh mọi người; chọn chỗ sát người đang nói, chữ nhỏ lại trước khi phải rời người đó.
- nhan.jsx: bỏ chọn phía theo một mặt; thêm `bam`. bo-cuc.jsx: `o-nguoi` tỉ lệ tự do, không cắt ngang mặt, ô ở phía người ngồi;
  `the-canh` co theo khoảng trống, hết chỗ thì thành `o-nguoi`. doan-gioi-thieu.py không còn tràn bộ nhớ.
- Nguyên nhân: video phỏng vấn "5 nguyên tắc": thẻ đè mặt khách, ô thu nhỏ cắt mặt khách. David duyệt 7 cảnh mẫu trước khi sửa skill.


## 2026-11-09 · thẻ cạnh mặt xuống dòng cân (app dựng video, bản thử "Sự tập trung")
- Lỗi: chữ trong thẻ `bocuc` (the-canh / ô người + thẻ) tự ngắt ở chỗ vô nghĩa, để một chữ đứng lẻ ("LUYỆN TẬP LẠI THÓI / QUEN").
- Sửa `thanh-phan/bo-cuc.jsx`: `textWrap: 'balance'` (dòng đều nhau) và `whiteSpace: 'pre-line'` (kịch bản đặt `\n` theo cụm nghĩa).
  Dự án cũ muốn áp dụng thì bấm "Cập nhật khung dựng" trong app (hoặc chép lại bo-cuc.jsx) rồi render lại cảnh bocuc.

## 2026-11-09 · khung ghép clip (highlight người nói, vlog) — lớp phủ toàn màn hình căn giữa, màn chốt theo luật 4
- Lỗi (app dựng video, thử 2 đoạn ngắn; Claude tự duyệt hình chỉ ra): lớp phủ bị overlay_guard đổi sang toàn màn hình chỉ bị đẩy lên và
  phóng 1,12 nên chữ/biểu tượng sát mép trái, chữ dài tràn khung; pow chia theo từ, không theo cụm; dấu góc highlight lấy tên tập dài
  ("…ĐẾN MỨC KHÔN…"); danh-sach-cat-doan-noi-bat.py luôn lấy câu cuối làm màn chốt (mâu thuẫn với luật 4).
- Sửa: `mau-dung-ghep/src/chuong-trinh.jsx` thêm CHẾ ĐỘ GIỮA (GiuaCtx) cho pow · chips · nameCard · location khi toàn màn hình — căn giữa trong
  vùng an toàn, không phóng; pow nhận `\n` theo cụm nghĩa và cỡ chữ tự co theo dòng dài nhất; location tự co + textWrap balance.
  `danh-sach-cat-doan-noi-bat.py`: màn chốt chỉ khi có câu `cta` / KEUGOI nguyên văn (không có thì CTA = null, kết ở câu chốt ý và thẻ cuối); dấu góc dùng
  `topic` ngắn của phương án (tối đa 3 chữ) trước tên tập.

## 2026-11-10 · Chữ nhấn dưới cằm đè miệng khi mặt nằm thấp
- Lỗi: video vòng đồng xu (mặt thấp, khung dọc hẹp) — `nhan.jsx` kẹp ô "dưới cằm" lên trên dải phụ đề thì ô chữ đè miệng/cằm.
- Sửa: `mau-remotion/src/thanh-phan/nhan.jsx`: khi ô dưới cằm bị kẹp lên quá cằm, đưa ô lên **trên đầu** (dưới dấu góc);
  không đủ chỗ trên đầu thì giữ cách cũ.
- 2026-11-10 · David chốt: video dọc ngắn bỏ thanh thời gian và thẻ cuối, màn chốt trên hình (quy-tac-chung 5); thêm `nganDoc()` (nhan-dien-thuong-hieu.js), `NGAN_DOC` (thanh.js), Cta dọc ngắn trong hanh-dong.jsx / chuong-trinh.jsx.

## 2026-11-10 · Học từ thiet-ke-trang-cuon: đường cảm xúc, không lặp kiểu cảnh, kiểm cảm nhận (David chốt)
- Lý do: video dễ giống nhau và thiếu một khoảnh khắc người xem nhớ; bộ skill mới kiểm kỹ thuật, chưa kiểm cảm nhận.
- `quy-tac-chung.md` mục 2: **đường cảm xúc và một đỉnh** cho mọi loại video (video dài vẫn không cắt; vlog ghép bỏ đoạn trùng cảm xúc liền nhau; highlight giữ 4 câu).
- Khối 07: cách viết đường cảm xúc trong `ke-hoach-canh.md`; **không hai cảnh cùng kiểu liền nhau**, không con số tối thiểu, ngoại lệ vẽ tiếp `tu_buoc`.
- Khối 17: **kiểm cảm nhận** (Claude tự làm, xem với góc nhìn mới rồi so đường dự định, lệch thì sửa cảnh), ghi `kiem-tra/cam-nhan.md`.
- `soat-canh.mjs`: thêm P2 "cùng kiểu với cảnh liền trước". Thử trên tap-5-nguyen-tac-tien (4), tap-di-trainer (16), vlog the-view-vung-tau (1); công cụ báo đúng.
- Không lấy: tạo ảnh AI, phỏng vấn 8 câu, con số "ít nhất 4 kiểu" (mâu thuẫn với "bố cục tự cân").

## 2026-11-10 · Thẩm mỹ chỉ giữ chữ ký nhận diện + học Ali Abdaal / Joseph Video Editing (David chốt)
- David: thẩm mỹ chỉ cần người xem nhận ra mọi video là của cùng một người; sáng tạo theo nội dung thì thoải mái; học càng nhiều tài nguyên càng tốt.
  Vì vậy ý này được ghi vào `thu-vien-tai-nguyen/nhan-dien-chung.md` mục 0 "Chữ ký nhận diện" (bộ nhận diện chung, cam nhấn, HEAD/BODY); sửa quy-tac-chung §0, khối 07, thiet-ke-bo-cuc README, phan-tich-video-mau, BoCuc, rieng.
- Thành phần mới (có code): `chusau` (chữ sau người, `bong` bóng người) + `scripts/tach_nguoi.{swift,py}` (Vision tách người từng khung thì public/nguoi/<id>/, src/nguoi.js);
  `bocuc` `muc-luc`, `tien-trinh`, `canh-nguoi`; `phong: 'nguoi-mo'|'hat'` (lib/phong.jsx, FullShell/Illus/Diagram); `*từ*` font phụ NHAN = Playfair Display nghiêng (file font trong thu-vien-tai-nguyen/font, lib/phong-chu-nhan.css — không cần cài gói; kiểm mẫu chuẩn bắt lỗi khi còn dùng gói npm).
- Place / TWO_KEEP / face_place / nhan_place nhận 'chusau'; soat_canh: P0 chưa tách người / thiếu khung, P1 chữ sau người > 6 chữ, bỏ dấu * khi đếm chữ.
- Lỗi đã gặp khi thử: lớp chusau bị Place thu nhỏ như lớp phủ nên người nhân đôi lệch; sửa bằng cách để nguyên khung. Chữ dòng 2 bị thân người che nên đáy khối chữ ngang mắt, thêm `cao`.
- Kiểm tra không làm hỏng phần cũ: 10 cảnh cũ ngang + dọc trùng từng điểm ảnh với skill trước khi sửa. Phiếu: `thiet-ke-bo-cuc/nguon-tham-khao/ali-joseph-2026-11-10.md`.

## 2026-11-10 · Gỡ chữ sau người + bóng người; luật "hiểu hơn cầu kì" (David chốt)
- David xem ảnh thử: "hiệu ứng chữ sau người là không cần, nhiều hiệu ứng quá là bị rối, nhìn ảnh toàn lỗi". Claude gỡ `ChuSau.jsx`, `tach_nguoi.{swift,py}`,
  `nguoi.js` và mọi chỗ nhắc (layout, Root, face_place, nhan_place, soat_canh, bo-cuc, khối 07/17, nhan-dien-chung). Giữ: muc-luc, tien-trinh, canh-nguoi, phong, `*từ*`.
- David: "học nhiều là để ứng dụng cho phù hợp với tuỳ mỗi loại nội dung chứ không cần nhét hết vào cùng 1 video… quan trọng nhất là truyền tải cho người xem hiểu chứ không phải cầu kì".
  Vì vậy thêm quy-tac-chung §0 "Hiểu hơn cầu kì"; khối 07 nới luật không lặp (giữ cùng kiểu được khi giúp dễ theo); khối 17 thêm câu soát "video có rối không".

## 2026-11-10 · Sửa 2 lỗi code lộ khi dựng đoạn thử tái bản 1 (David chọn cách sửa)
- `xuat-video.mjs` dừng ở bước thẻ cuối trên Node 24: `man-ket.js` kéo `thanh.js`, file này nạp `ho-so.json` không có `with {type: 'json'}` (ERR_IMPORT_ATTRIBUTE_MISSING) và nạp `./khung-podcast` thiếu đuôi `.js`.
  Chỉ sửa `thanh.js` (file duy nhất Node dùng tới; các `.jsx` nạp json chỉ chạy trong bundle nên giữ nguyên). Đã thử: `with` chạy được cả Node lẫn webpack của Remotion.
- `chuan-am.py` ra −14,8 LUFS khi render_preview tự gọi: bộ chặn đỉnh làm bài nhỏ đi sau khi kéo mức. Nay công cụ đo lại bản ra, bù phần thiếu, xuất lại TỪ BẢN TRƯỚC KHI CHỈNH (không nén AAC chồng), tối đa 3 lượt.
- Thử trên `tap-thu-tai-ban-video-1/2-ban-day-du`: xuat-video.mjs chạy trọn (có the-cuoi), bản cuối từ −17,2 lên −14,2 LUFS, đỉnh −1,5 dBTP, 2 lượt, ngay lần đầu.
- 2026-11-12 · David góp ý video giao dịch hàng hoá: "nhân vật chiếm rất ít không gian, đây là video chia sẻ thông tin kiến thức… nên đưa nhân vật vào khung và phần còn lại để bảng hiển thị nội dung thông tin và các hình ảnh"; "bạn vẫn chưa chọn được thể loại phù hợp với nội dung". Claude đã giữ khung gốc dù công cụ báo DÀY THÔNG TIN (215 chữ/phút). Claude sửa `thiet-ke-bo-cuc/huong-dan-lua-chon.md` bước 2–3 (video kiến thức có người chiếm dưới khoảng 50 % khung thì dùng khung chủ thể quanh người kèm bảng; công cụ báo dày thì không tự bỏ bảng) và gợi ý trong `chan-doan.py`. Cùng lần: bỏ mọi nền đen mờ sau chữ (thẻ cạnh người, chữ nhấn `nhan`, phụ đề, thanh thời gian, dải tối sau lớp phủ) nên dùng nền sẫm đặc `C.card` / `C.nen`; dấu góc DAVID có ô nền sẫm đặc (David: "chữ trắng trên nền sáng thì đâu có thấy").
- 2026-11-13 · David xem bản render 2 tap-giao-dich-hang-hoa: "bỏ hiệu ứng zoom ra zoom vào, không thẩm mỹ" nên bỏ zoom ở mọi loại video (xem-truoc-ban-dung.py, nhan.jsx, danh-sach-cat-vlog.py, montage chuong-trinh.jsx, danh-sach-cat-doan-noi-bat.py, cat-doan-noi-bat.py; tài liệu khối 07, scene-design, bo-cuc, quy-tac-chung, cat-highlight). "Ảnh vuông mà khung chữ nhật thừa ra ngoài" nên màn chốt (Cta, hanh-dong.jsx) có khung chủ thể thì chỉ cắt đúng ô người, cùng tỉ lệ, ô trượt từ chỗ cũ vào giữa.
- 2026-11-13 · David: "nhiều hình ảnh để mô tả hơn, chỉ lấy tại Việt Nam, liên quan người Việt Nam" nên Claude sửa quy-tac-chung (ảnh thật nhiều hơn, chỉ ảnh Việt Nam, không có thì biểu tượng vẽ); `kho-anh-openverse.py` tự thêm "Vietnam" vào từ khoá; thêm biểu tượng `thoi` (thỏi kim loại); bỏ zoom chậm trên ảnh (Diagram `kb`). Bỏ cổng 1, cổng 2: làm liên tục tới hết, có góp ý thì render lại toàn bộ; trang xem kết quả `tu-dong-hoa/xem-ket-qua.py` (localhost:8765, chỉ đọc Drive thanh-pham). `cat-doan-noi-bat.py` tự tạo thư mục `cat/`.
- 2026-11-19 · David: video nào cũng một kiểu thẩm mỹ, bố cục; "mọi lựa chọn đều phải được tự động setup phù hợp với nội dung của tài nguyên nguồn" (duyệt đường A) nên chọn mẫu theo nguồn (nhiều file cùng buổi nói thì nối, mẫu 1 video); huong-dan-lua-chon.md bước 0 và 2b (thẩm mỹ); cổng chặn render trong xuat-video.mjs / xuat-chuong-trinh.mjs (soat-canh: chưa chẩn đoán, chỉ một kiểu thì là P0); chan-doan.py đọc mẫu ghép + tín hiệu so sánh, nhân quả, thẩm mỹ; danh-sach-cat-doan-noi-bat.py ghi goi-y-kieu.md; mẫu ghép có nền `phong: 'hat'`; sửa soat-canh tính sai độ dài mẫu ghép (chia FPS hai lần).
- 2026-11-19 · Lỗi đợt marketing: phụ đề lệch tới 14 s nên dùng `soat-khop-tieng.py` trước render (khối 03, 17) · whisper ảo giác ở quán ồn nên chép theo phân đoạn, bản gốc trước (khối 01) · điểm cắt theo mốc từ cụt chữ nên dùng `diem-ngat.py` (khối 02, 13) · đoán người nói sai khi hai người ngồi xa nên dùng khung cố định + follow (khối 04) · `trim=` trên nguồn dài chậm nên dùng `-ss` từng đoạn (khối 02) · anh-tinh.mjs lỗi để lại thư mục tạm nên dùng try/finally, bỏ mốc quá độ dài · bảng thời gian render thật (khối 17).
- 2026-11-20 · Học kênh MagentX (David duyệt "đồng ý hết"): `bocuc` thêm `dung-hay`, `tren-duoi`, `o-tron`, `cau-hoi`, `the-canh` `so`; phụ đề dọc ngắn `hl` "^" là từ khoá to; `soat-canh.mjs` báo P1 khi kiểu học mới thiếu dấu hiệu trong Chẩn đoán. Kiểm tra: phần cũ SSIM 1,000 (10/10) cả hai khung.
- 2026-11-20 · David: học phải thành "tư duy logic về việc xây dựng video chứ không phải áp dụng code máy móc"; "khi không có claude mà chỉ cần dựa vào các file thì máy nào cũng có thể dùng bất kì ai nào để làm ra được video" (máy Windows chỉ có GitHub). Phỏng vấn `du-an/phong-van/2026-11-20-tu-duy-dung-video.md`, đợt 1: tầng `thiet-ke-bo-cuc/nhu-cau-nguoi-xem.md` (loại nội dung, 12 nguyên lý Mayer và 4 nguyên lý ngoài Mayer), `huong-dan-lua-chon.md` viết lại theo nguyên lý (bỏ các câu trích, ngày trong bản luật: lời 19/11 "mọi lựa chọn đều phải được tự động setup…" và 20/11 "motion graphics ngày càng thể hiện rõ… tinh gọn" ghi ở đây), `soat-canh.mjs` chặn khi thiếu `Loại:` / `Cần:` (dự án cũ không có `yeu-cau.md` chỉ nhắc), `yeu-cau.md` và `them-anh/` tạo sẵn trong dự án mới, ảnh mẫu từng kiểu.
- 2026-11-20 · Đợt 2 tư duy dựng video. David: "không cần dựa trên những nội dung tôi nói, mà hãy dựa trên những hình mẫu đã rất thành công của cùng thể loại" nên Claude đo 23 kênh, David đồng ý 8 hình mẫu, rồi Claude viết `thiet-ke-bo-cuc/truong-hop-da-giai.md` (19 trường hợp) và `thiet-ke-bo-cuc/bai-kiem/` (10 đoạn, `cham.py`, đạt ít nhất 8/10).
- 2026-11-24 · Rà soát để máy mới (Windows qua WSL) làm đúng chỉ từ GitHub (David duyệt 4 phần): tên script cũ trong tài liệu và ghi chú đổi sang tên thật (render_preview → xem-truoc-ban-dung.py, clean_apply → ap-dung-lam-sach.py, rekhung-* → phan-tich-doi-khung.sh + ke-hoach-doi-khung.py…); teaser một ngưỡng > 10 phút; đỉnh âm −1,5 dB; mẫu canh.js bỏ chữ "thẻ tít bắt buộc"; ghép vlog ghi rõ bước chan-doan.py; khối 05 ghi rõ code vẫn tự chuyển toàn màn hình (chưa đổi code, chờ David quyết định trên Mac); drive-chung.sh dò thêm Drive kiểu phản chiếu + câu hướng dẫn khi thiếu Drive; kiem-moi-truong.sh cảnh báo thiếu Drive.
- 2026-11-26 · David góp ý trên thẻ liệt kê (tập AI sản xuất video): "các dòng như thế này cần có khoảng cách trên dưới giữa các ý, chữ đầu cần viết hoa, gạch đầu dòng để rõ ý khi trình bày" nên thêm luật ở `quy-tac-chung.md` mục 4, sửa mẫu `bo-cuc.jsx` (thẻ chữ) và `rieng/nhan-tram.jsx`. Cùng ngày: `loi-ao-giac.py` tự bỏ câu bịa ở đuôi không lời (tối đa 1,5 s) thay vì dừng quy trình.
- 2026-11-26 · David hay làm việc từ xa, cần máy Windows đưa đủ kết quả lên Drive; duyệt đường tải lên bằng `rclone` (quyền `drive.file`, thư mục `thanh-pham-may-windows/`), thêm `ket-noi-drive.sh`. `luu-drive.sh` dùng `${1:a}` vì dự án trên máy này là đường dẫn tắt sang ổ D.
- 2026-11-26 · David: không đồng bộ Drive vào ổ G trên máy Windows; Drive chỉ để tải video gốc về hoặc tải lên. `drive-chung.sh` ngoài Mac không tự tìm ổ Drive nữa, `cho-dang.sh` giữ kết quả trên máy; luật ở `du-an/kho-drive.md` mục "Máy Windows". Việc mở lại ứng dụng Google Drive ghi ở dòng dưới là làm sai, không lặp lại.
- 2026-11-26 · Video cho xem màn hình máy tính lộ link thư mục Drive và tên phiên làm việc nên thêm `lam-mo-vung-rieng.py` và mục làm mờ ở khối 05. Ổ Drive trong WSL mất kết nối giữa việc (ứng dụng Google Drive tắt): mở lại ứng dụng, đóng gói trong WSL rồi chép bằng `robocopy` từ phía Windows (thư mục thật của `~/Movies/cho-dang` là ổ D), so khớp từng tệp, không cần khởi động lại WSL.
