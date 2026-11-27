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
4. **Ghép hiệu ứng với đoạn:** đọc lời, mỗi hiệu ứng chọn một đoạn có đúng dấu hiệu (ví dụ "không phải A mà là B" cho thẻ gạch chữ, đếm "thứ nhất…"
   ít nhất 3 mục cho số thứ tự to, hai con số cùng đơn vị cho cột). Bỏ đoạn chạm lằn ranh (`david.md` mục 4.7). Ghi vào
   `ke-hoach-ghep-hieu-ung.md` của tập: hiệu ứng · nguồn · mốc · lời · vì sao khớp. Hiệu ứng không có đoạn đủ điều kiện thì ghi rõ "chưa có cảnh".
5. **Viết code cho cách còn thiếu:** đo mẫu (bảng khung 0,67 giây ở đúng mốc, mã gốc của tác giả nếu có), thêm vào `rieng/` (một file mẫu
   dùng lại, đăng ký trong `diem-vao.js`), kiểm cú pháp bằng `esbuild`.
6. **Ghép nguồn thành một video gốc:** viết `doan.json` (thứ tự theo nhóm của `bo-cuc.md`), chạy
   `python3 -I $SKILL/scripts/ghep-doan-kho-hieu-ung.py doan.json <thư mục>` (thêm `--doc` cho nhóm chỉ dùng khung dọc). Ra `video-goc.mp4`,
   `bang-moc.json`, `bang-moc.md`.
7. **Dựng như một video thường:** `tao-du-an.sh <video-goc.mp4> "" kho-hieu-ung-<ngày>` → `phan-tich-video.sh` → `phu-de.py` → `canh.js`
   (mỗi đoạn một cảnh, mốc = mốc lời trong video ghép) → `ke-hoach-canh.md` (Chẩn đoán đủ dòng) → `vi-tri-khuon-mat.sh` → `xem-truoc.mjs`
   (chụp đầu / giữa / cuối từng cảnh mới) → `xuat-video.mjs` → `xem-truoc-ban-dung.py`. Không có thẻ tiêu đề hay chữ ghi chú trên hình;
   tên hiệu ứng nằm ở `bang-moc.md` và chương.
8. **Giao:** bản dựng + `bang-moc.md` (hiệu ứng · nguồn · mốc gốc · mốc trong bản xem) + danh sách hiệu ứng chưa có cảnh hoặc chưa có code.
   Đây là bản nội bộ để David xem, không đăng; lưu trên máy và Drive `thanh-pham/tap-kho-hieu-ung-<ngày>/`.

## Điểm duyệt
Không có Đ1 (đã có lá). Đ3 khi một hiệu ứng mới đụng màu chủ đạo hay chữ ký nhận diện của kênh (bản tái dựng giữ màu mẫu, không đổi nhận diện kênh).

## Xong khi
- Mọi kiểu có code trong kho có một cảnh trong bản xem, hoặc có dòng "chưa có cảnh đủ điều kiện" kèm lý do.
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
- Đoạn lặp lại trong bản ghép (cùng một nguồn dùng cho nhiều hiệu ứng) làm `soat-khop-tieng.py` báo lệch giả hơn 3 giây ở chỗ lời trùng: đối chiếu với `bang-moc.md` trước khi sửa.
- Mẫu `DuongMay` (thẻ lật, gạch thay, câu đắt) có chữ nhỏ khi xem khung ngang toàn màn hình: chấp nhận cho bản xem; dựng thật thì chọn kiểu khác nếu chữ không đọc kịp.
- Lỗi khung dựng còn mở (27/11/2026): `diagram` `xay-tang`, `moc`, `tu-thanh`, `chuyen-giao` đặt trong `bocuc` `o-nguoi` khung ngang bị tràn mép phải (sơ đồ tính bề ngang theo cả khung, không theo phần còn lại cạnh ô người). Bản xem để các kiểu này toàn khung kèm `soLieuToanKhung`; cần sửa `thanh-phan/bo-cuc.jsx` / `thu-vien/so-do.jsx` trước khi dùng trong video thật.
- Dấu góc ● DAVID khung ngang nằm ở mép trên vùng an toàn (54–118 px): dòng chữ trên cùng của cảnh tự vẽ và vùng `o` của `DuongMay` / `NhanTram` phải bắt đầu dưới `BRAND_BOT` (`o.y` ít nhất khoảng 0,13).
- Nguồn kênh cũ (Cường Kể Chuyện) có sẵn thanh tên tập in cứng ở đáy hình, chồng lên phụ đề và thanh thời gian: chỉ dùng cho bản xem, video thật cần cắt khung hoặc chọn nguồn khác.

