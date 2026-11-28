---
description: "Quy trình lá B15: dựng bản xem đủ kho hiệu ứng — mỗi hiệu ứng trong bộ não ghép với một đoạn nội dung phù hợp trong các video gốc của David."
---

# Bản xem đủ kho hiệu ứng từ video gốc (cây quy trình lá B15)

**Khi nào dùng:** David muốn "thấy được hết mọi hiệu ứng đang có trong bộ não", "lấy từ các video gốc từng đoạn phù hợp với từng hiệu ứng",
"kiểm kho hiệu ứng đã học đúng chưa". Đây là trường hợp riêng của [tái dựng theo đúng video mẫu](README.md#4a-tái-dựng-theo-đúng-video-mẫu).

**Đầu vào:** kho hiệu ứng (`bo-cuc.md`, bảng 4c của `huong-dan-lua-chon.md`, `nguon-tham-khao/`, `rieng/` của khung Remotion) và các video gốc
David được phép dùng (trên máy và Drive `sao-luu-mac/video/<tập>/1-goc/`, `tu-lieu-goc/`).

## Các bước

1. **Kiểm kê kho:** liệt kê mọi kiểu có code (`bocuc` các `kieu`, `diagram`/`illus` các `mode`, `nhan`, `phong`, `rieng/` mọi cảnh trong
   `diem-vao.js`) và mọi cách "chưa code" ở `bo-cuc.md`. Mỗi kiểu ghi dấu hiệu bắt buộc lấy từ bảng 4c.
2. **Gom nguồn:** chép video gốc về `~/Movies/tap-kho-hieu-ung-<ngày>/1-goc/` (lá B2). Ưu tiên video David nói một mình, có liệt kê, con số,
   so sánh, quy trình. Ổ Drive chưa tải tệp về thì đọc bằng `cat <tệp> > <đích>` có thử lại (lệnh `cp` dễ hết thời gian chờ với tệp lớn).
3. **Chép lời** từng nguồn chưa có lời: `zsh $SKILL/scripts/phan-tich-video.sh <video> ~/Movies/tap-kho-hieu-ung-<ngày>/loi/<tên>`.
4. **Nội dung chọn hiệu ứng, không phải hiệu ứng đi tìm đoạn** (David 28/11/2026: điều quan trọng nhất là nhận diện được nội dung này nên dùng
   hiệu ứng nào cho hợp lý; bản đầu đặt tám hiệu ứng lên cùng một đoạn lời nên phần lớn là gượng).
   - Đọc lời từng nguồn theo mạch, cắt thành các ý trọn. Với mỗi ý, hỏi như khi dựng video thật (`huong-dan-lua-chon.md` bước 4): cái khó của người xem
     là gì, nguyên lý nào giải, rồi chọn cách thể hiện hợp nhất trong bảng 4c. Ý không cần hình thì để người và phụ đề.
   - Thước đo là độ hợp, không phải số lần dùng. Một đoạn được dùng lại cho hiệu ứng khác chỉ khi nội dung đó cũng thật sự hợp với hiệu ứng ấy
     (ví dụ một ý vừa là "hai thời kỳ" vừa có con số quyết định); ghi rõ vì sao hợp cho từng lần. Script ghép in cảnh báo khi hai đoạn cùng nguồn
     chồng nhau để người dựng xem lại.
   - Hiệu ứng phải khớp đúng dấu hiệu của ý (ví dụ "không phải A mà là B" cho thẻ gạch chữ, đếm "thứ nhất…" ít nhất 3 mục cho số thứ tự to, hai con số
     cùng đơn vị cho cột) và đúng vai trò của nó trong hình mẫu gốc (`nguon-tham-khao/`). Khớp gượng ("gần giống", phải đổi lời, phải chế chữ) thì không dùng.
   - Sau khi đi hết các nguồn, hiệu ứng nào chưa có ý nào chọn nó thì tìm thêm nguồn (Drive `sao-luu-mac/video/`); vẫn không có thì ghi
     "chưa có cảnh đủ điều kiện" kèm dấu hiệu cần tìm. Một bản xem thiếu vài hiệu ứng mà cảnh nào cũng đúng tốt hơn bản đủ mà có cảnh gượng.
   - Bỏ đoạn chạm lằn ranh (`david.md` mục 4.7). Ghi vào `ke-hoach-ghep-hieu-ung.md` của tập: ý · nguồn · mốc · lời · cái khó · hiệu ứng chọn ·
     ứng viên đã loại và vì sao.
5. **Viết code cho cách còn thiếu:** đo mẫu (bảng khung 0,67 giây ở đúng mốc, mã gốc của tác giả nếu có), thêm vào `rieng/` (một file mẫu
   dùng lại, đăng ký trong `diem-vao.js`), kiểm cú pháp bằng `esbuild`.
6. **Ghép nguồn thành một video gốc:** viết `doan.json` (thứ tự theo nhóm của `bo-cuc.md`; cảnh của từng đoạn ở khoá `canh`, mốc theo nguồn).
   `doan.json` là nguồn duy nhất của cảnh: sửa cảnh thì sửa ở đây rồi chạy lại, không sửa tay `canh.js`. Chạy
   `python3 -I $SKILL/scripts/ghep-doan-kho-hieu-ung.py doan.json <thư mục> --chep-loi --canh-js <dự án>/chuyen-dong/src/canh.js`
   (thêm `--doc` cho nhóm chỉ dùng khung dọc). Script cắt và nối đoạn, chép lời **từng đoạn** (mốc từ đúng; chép một lượt cả video ghép dài
   làm mốc trôi hơn 1 giây), ghi cảnh và chương vào `canh.js`, chạy `khop-chu-voi-loi.py --sua` để mọi chữ trên hình hiện đúng lúc nói,
   rồi ghi mốc đã khớp ngược về `doan.json`. Ra `video-goc.mp4`, `bang-moc.json`, `bang-moc.md`, `loi/`.
7. **Dựng như một video thường:** `tao-du-an.sh <video-goc.mp4> "" kho-hieu-ung-<ngày>` → chép `<thư mục>/loi/*.srt` vào
   `kiem-tra/goc/` (thay bản `phan-tich-video.sh`) → `phu-de.py` → `ke-hoach-canh.md` (Chẩn đoán đủ dòng) → `vi-tri-khuon-mat.sh` →
   `xem-truoc.mjs` (chụp đầu / giữa / cuối từng cảnh mới) → `xuat-video.mjs` → `xem-truoc-ban-dung.py`. Không có thẻ tiêu đề hay chữ ghi chú
   trên hình; tên hiệu ứng nằm ở `bang-moc.md` và chương. Trước khi xuất, `khop-chu-voi-loi.py <canh.js> kiem-tra/goc/moc-tung-tu.srt` phải
   báo 0 mục lệch, 0 mục không thấy trong lời.
8. **Giao:** bản dựng + `bang-moc.md` (hiệu ứng · nguồn · mốc gốc · mốc trong bản xem) + danh sách hiệu ứng chưa có cảnh hoặc chưa có code.
   Đây là bản nội bộ để David xem, không đăng; lưu trên máy và Drive `thanh-pham/tap-kho-hieu-ung-<ngày>/`.

## Điểm duyệt
Không có Đ1 (đã có lá). Đ3 khi một hiệu ứng mới đụng màu chủ đạo hay chữ ký nhận diện của kênh (bản tái dựng giữ màu mẫu, không đổi nhận diện kênh).

## Xong khi
- Mọi kiểu có code trong kho có một cảnh trong bản xem, hoặc có dòng "chưa có cảnh đủ điều kiện" kèm lý do.
- Mỗi cảnh có dòng cái khó → nguyên lý → hiệu ứng; đọc lại thấy hiệu ứng sinh ra từ ý, không phải ngược lại. Đoạn dùng lại có lý do hợp riêng cho từng hiệu ứng.
- `bang-moc.md` ghi đủ mốc, đã xem đủ đầu / giữa / cuối từng cảnh mới ở kích thước phát hành, không che mặt, chữ đúng nguyên văn.
- Code mới, script, lá này nằm trong repo và đã đẩy GitHub.

## Kiểm gì
- Chữ trên hình là nguyên văn lời người nói (luật 3); lời chép sai thì sửa theo tiếng, không đoán.
- Đoạn có người khác hiện hình chỉ dùng nội bộ; không đưa vào bài đăng.

## Lỗi hay gặp
- Tệp gốc trên Drive có thể đã bị dọn theo luật xoá tệp gốc (`du-an/kho-drive.md`) giữa lúc đang chép: chọn nguồn khác có cùng dấu hiệu, ghi vào báo cáo.
- Video điện thoại có góc xoay: script ghép tự xoay; nguồn dọc trong bản ngang được thu vừa khung, nên đưa hiệu ứng chỉ dọc vào bản `--doc` riêng.
- Kiểu cũ `lower`, `kinetic`, `converge`, `action` chỉ viết cho khung dọc (vị trí cố định 1040–1150 px): trên khung ngang chữ nằm ngoài khung hoặc bộ soát chặn.
  `converge` còn có tiêu đề cố định "TẤT CẢ NHỮNG NGHỀ ĐÃ LÀM" (không phải lời người nói). Bản ngang dùng mẫu riêng tương đương (`DuongMay` thẻ tên, câu đắt;
  `NhanTram` thẻ ý; `bocuc` the-canh); `kinetic` đưa vào bản dọc.
- Luật giữ hình gốc (`quy-tac-chung.md` mục 4): bộ soát chặn `illus` / `diagram` toàn khung. Đặt chúng trong `bocuc` `o-nguoi` (`noi_dung`); kiểu vốn toàn khung
  (màn chương, thanh tiến trình, thẻ các bước, nền người mờ, nền hạt) ghi lý do ở `props.soLieuToanKhung`.
- Bản đầu (27/11/2026) có chữ hiện sớm hơn lời 1–5 giây ở gần mọi cảnh: mốc lấy theo đầu câu trong bản chép lời cả câu, và bản chép lời của
  nguồn đã làm sạch lệch 1 giây so với tệp thật. Đo bằng khoảng lặng (`ffmpeg silencedetect`) mới biết bản nào đúng; nay dùng lời chép
  từng đoạn và `khop-chu-voi-loi.py`.
- Đoạn lặp lại trong bản ghép (cùng một nguồn dùng cho nhiều hiệu ứng) làm `soat-khop-tieng.py` báo lệch giả hơn 3 giây ở chỗ lời trùng: đối chiếu với `bang-moc.md` trước khi sửa.
- Mẫu `DuongMay` (thẻ lật, gạch thay, câu đắt) từng có chữ 14–24 px ở khung ngang vì cỡ chữ tính như cả câu trên một dòng. Đã sửa 28/11/2026: `coChu()` trong `rieng/duong-may.jsx` cho xuống tối đa 2–4 dòng khi ô đủ cao. Vẫn xem bảng khung ở kích thước phát hành; chữ chính dưới khoảng 36 px ở khung 1080 thì nới ô `o`.
- Sơ đồ và minh hoạ đặt trong `o-nguoi` hay `canh-nguoi` khung ngang từng tràn mép phải vì khung co theo vùng 60% bề ngang, trong khi sơ đồ vẽ 86%. Đã sửa 28/11/2026: `vungNoi()` trong `thanh-phan/bo-cuc.jsx` co theo vùng vẽ thật của từng loại. Thêm loại nội dung lồng mới thì khai vùng vẽ của nó trong `VUNG_NOI`.
- Bản 27/11/2026 phối lại hiệu ứng học từ mẫu sang màu kênh nên lỗi thẩm mỹ và che mặt (David 28/11/2026). Luật hiện hành: lấy chính xác màu, font, tỉ lệ của mẫu, kể cả màu nhấn; màu không phải nhận diện. Nay mỗi loại cảnh mang giao diện của mẫu
  gốc qua `MAU_CUA` / `GIAO_DIEN` (`thu-vien/bien-thiet-ke.js`); loại học từ mẫu mà chưa đo giao diện thì ghi vào báo cáo "chưa đo mẫu", không tự phối màu.
- Kiểm che mặt bằng công cụ trước khi xuất: `kiem-che-mat.py <dự án> chup` → `node xem-truoc.mjs …` → `kiem-che-mat.py <dự án> kiem` phải báo 0.
- Dấu góc ● DAVID khung ngang nằm ở mép trên vùng an toàn (54–118 px): dòng chữ trên cùng của cảnh tự vẽ và vùng `o` của `DuongMay` / `NhanTram` phải bắt đầu dưới `BRAND_BOT` (`o.y` ít nhất khoảng 0,13).
- Nguồn kênh cũ (Cường Kể Chuyện) có sẵn thanh tên tập in cứng ở đáy hình, chồng lên phụ đề và thanh thời gian: chỉ dùng cho bản xem, video thật cần cắt khung hoặc chọn nguồn khác.
- Ổ đĩa: lớp hiệu ứng ProRes 4444 của bản ngang 11 phút chiếm khoảng 16 GB; bước ghép cần thêm vài GB. 28/11/2026 ổ còn 1,2 GB nên bước chuẩn âm lượng lỗi và mất bản ghép cũ. Trước khi xuất, kiểm `df -h /` còn ít nhất 25 GB; giao xong thì xoá `tu-lieu/*.mov` (dựng lại được bằng `xuat-video.mjs`). Chạy xuất dài kèm `caffeinate -i` để máy không ngủ giữa chừng.

