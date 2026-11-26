---
description: "Lớp trình bày video: tiêu chí gốc để học mọi loại video mới, giữ chữ ký nhận diện."
---

# Lớp trình bày — khung gốc để học mọi loại video mới

File này là **tiêu chí gốc**: dù học thêm loại video nào, mọi thứ học được đều đi qua đây, để kiến thức ngày càng phong phú trong khi người xem
vẫn nhận ra video của David.

## 1. Chữ ký giữ, còn lại học và thêm vào kho

| Lớp | Gồm | Ở đâu | Khi học video mẫu |
|---|---|---|---|
| **Chữ ký nhận diện** | màu nhấn cam, hai font chính, thành phần cố định (dấu góc, phụ đề, thanh thời gian, màn chốt, thẻ cuối), nhạc kênh | `thu-vien-tai-nguyen/nhan-dien-chung.md` mục 0, `bien-thiet-ke.js`, `thuong-hieu.json` | **Không đổi** |
| **Phần sáng tạo** (học được) | bố cục, thứ tự thông tin hiện ra, cách nối cảnh, nhịp, chỗ đặt hiệu ứng âm thanh, nền, kết cấu, kiểu hình, chữ nhấn phụ, chuyển động | thư mục này + `bo-cuc.jsx`, `thu-vien-tai-nguyen/` | **Chỉ thêm.** Mỗi điều học được là một mục mới trong kho |

Học càng nhiều thì càng có nhiều tài nguyên để chọn; khi dựng, Claude chỉ chọn vài kiểu hợp nội dung (`quy-tac-chung.md` mục 0, hiểu hơn cầu kì).

## 2. Thước đo duy nhất: hợp nội dung, người xem dễ nhận

- **Không có con số bắt buộc** về bố cục, ví dụ độ dài cảnh, tỷ lệ mặt / đồ hoạ, số cảnh, số chữ nhãn. Mỗi đoạn, Claude tự hỏi:
  1. Đoạn này người xem cần **thấy người** (cảm xúc, chuyện kể, lời mời) hay cần **thấy ý** (giải thích, bước, so sánh, con số)?
  2. Ý này **dài hay ngắn**? Nếu dài và nhiều bước, nội dung cần chiếm chỗ lâu hơn.
  3. Khung này **còn chỗ** không? Ngang có nhiều chỗ; dọc thì xem trên điện thoại.
  4. **Ngay trước và ngay sau** là gì? Tránh lặp một bố cục quá lâu, và nối cảnh cho liền mạch.
- **Video ngang:** tự do bố trí, nhiều chỗ để người và nội dung cùng hiện.
- **Video dọc:** người xem dùng điện thoại, nên **mỗi lúc chỉ hiện ít thứ**. Mỗi lúc một điểm nhìn chính và chữ to vừa đọc kịp.
- Con số còn trong hồ sơ là **thẩm mỹ** (nhịp hiện / ẩn, cỡ phụ đề) và **kỹ thuật** (âm lượng −14 LUFS, nhạc thấp hơn giọng khoảng 23 dB,
  màn kết YouTube). Đây không phải luật bố cục.

## 3. Luật bắt buộc vẫn giữ (không phải con số)

- Không che mặt người nói. Thu người vào ô bo góc không tính là che.
- Chữ trên màn hình là **nguyên văn lời David** (`quy-tac-chung.md` mục 1): không tự rút tiêu đề, không bỏ chữ làm đổi nghĩa.
- Phụ đề luôn chạy. Không ghi chú kỹ thuật trên hình.
- Chuẩn âm lượng chung (khối 09).
- Với vài video đầu tiên dùng bố cục mới, Claude chụp đủ lớp để tự rà soát kỹ trước khi render (`kiem-tra/anh-tinh.jpg`).

## 4. Quy trình học một video mẫu mới

Học là **bổ sung** (`quy-tac-hoc-la-bo-sung`; trục `co-so-tri-thuc/truc-tri-thuc.md`: nguồn mới vào kho / tầng 3 trước): không xoá, không sửa nghĩa phần đã có. Skill `phan-tich-video-mau` tự kích hoạt khi David gửi video
và nói "học cái này"; skill đó chỉ trỏ về đây.

Bước nhẹ (1–3): khi tới các bước đó, Claude nhắc một dòng để David tự đổi sang mô hình chi phí thấp hơn; Claude không tự đổi.

1. **Lấy mẫu** *(bước nhẹ)*: khi David gửi file thì dùng file đó. Khi chỉ có link thì tải bản 720p **chỉ để học** vào thư mục tạm (không đưa
   lên repo, **học xong thì xoá**), đọc mô tả và danh sách chương (`yt-dlp --dump-json`).
2. **Cắt khung** *(bước nhẹ)*: bảng khung theo nhịp 1,5–3 s (`ffmpeg … fps=1/2,scale=480:-1,tile=4x4`) ở đoạn mở đầu và đoạn đúng loại cần học.
3. **Nghe** *(bước nhẹ)*: vẽ phổ âm (`showspectrumpic`) để thấy chỗ có tiếng hiệu ứng, nhạc nền, nốt chuyển chương.
4. **Rút ra nguyên lý trước, món sau:** trả lời "vì sao mẫu này dễ hiểu / giữ người xem" bằng **tên nguyên lý ở `nhu-cau-nguoi-xem.md`**
   (Đúng lúc, Chia đoạn, Báo hiệu, Tinh gọn…; nếu không gắn được vào khó khăn nào của người xem thì không học), rồi xác định mỗi nguyên lý nâng cấp **thành phần đang có** nào. Claude chỉ thêm kiểu mới khi không thành phần
   nào làm được. Kỹ thuật chỉ để trang trí (không giúp hiểu thêm) thì ghi vào "Không lấy". Không thay đổi chữ ký nhận diện (mục 1).
   Học để tự áp dụng và cải tiến phần đang có: motion graphics rõ nghĩa hơn nhưng tinh gọn (`huong-dan-lua-chon.md` bước 4a).
5. **Phiếu học cho David duyệt** (mẫu ở `phieu-hoc-mau.md`): học được gì, dùng cho loại video nào, thêm thành phần nào, mỗi thành
   phần đối chiếu với các quy tắc chặn đã có thế nào. Đây là **cổng hỏi duy nhất**: gộp mọi điểm cần chọn, mỗi điểm 2–3 gợi ý.
   **Chờ David "ok" rồi mới sửa skill.**
6. **Ghi vào kho** (kho là thực đơn, không phải luật). Khi điều học được làm **đổi luật**, Claude sửa trực tiếp câu luật đó, ghi lý do vào sổ (thoi-quen mục 4), không thêm câu chồng lên.
   **Cách ghi kho:** một file `nguon-tham-khao/<ten-nguon>-<ngay>.md` kể học gì từ đâu. Mỗi cách mới thêm một dòng ở `bo-cuc.md` hoặc `am-thanh.md`,
   ghi rõ "đã có code" hay "chưa có code", **thêm vào dòng "Đã học" của nguyên lý ở `nhu-cau-nguoi-xem.md` và một dòng "dạng câu / hình thì cách thể hiện" dưới đúng nguyên lý
   ở bảng 4c của `huong-dan-lua-chon.md`** (cách nào không có dòng ở đó thì không bao giờ được chọn). Không xoá, không sửa nghĩa dòng cũ.
7. **Viết code khi cần:** thêm `kieu` mới trong `dung-video-theo-phong-cach/assets/mau-remotion/src/thanh-phan/bo-cuc.jsx` (màu nhấn và
   font lấy từ `C`, `HEAD`, `BODY`; hình động dùng `ease`, `pop`, `Illus`, `Diagram`, `Icon` hoặc `thu-vien-tai-nguyen/chuyen-dong.js`). Vị trí lấy từ hằng số chung (`SAFE`, `BRAND_TOP`/`BRAND_BOT`,
   `PF`, `CAP_H`), **không viết số vị trí riêng**.
8. **Kiểm tra không làm hỏng phần cũ** (bắt buộc trước khi dùng vào video thật):
   - Thành phần mới phải qua đủ các quy tắc chặn đã có: không che mặt · không đè phụ đề · nằm dưới dấu góc · trên thanh thời gian · trong vùng an
     toàn · chữ tiếng Việt đủ dấu, không chồng dòng · chữ nguyên văn.
   - Chụp thử **đủ lớp** (cảnh + `phu-de@<giây>` có dấu góc, phụ đề, thanh thời gian) ở **cả khung ngang lẫn dọc**, trên ít nhất
     một dự án cũ đã duyệt. So với ảnh trước khi thêm: phần cũ phải giữ nguyên.
   - Chạy `soat-canh.mjs` và `python3 -I ../mau-chuan/kiem-mau.py` (mẫu chuẩn); nếu có lệch thì sửa thành phần mới, không sửa phần cũ cho vừa.
9. **Xoá file mẫu đã tải**, **đẩy lên GitHub** và báo David: thêm gì, đã kiểm gì, chưa kiểm gì.
10. **Không chép công cụ của nguồn** (HyperFrames…): giữ Remotion, chỉ học ý (`video-bo-ung-dung`).

## 5. Dùng khi dựng

- Trước khi viết kịch bản cảnh: lập luận theo **`nhu-cau-nguoi-xem.md`** rồi làm các bước của **`huong-dan-lua-chon.md`** (`chan-doan.py`), kết hợp 4 câu hỏi ở mục 2.
  Mỗi cảnh một dòng `Cần · Vì · Làm` trong `ke-hoach-canh.md` của dự án.
- Danh mục là **kho để chọn**, không phải công thức. Một video có thể chỉ dùng hai kiểu, cũng có thể dùng năm kiểu, tuỳ nội dung.

## Các file

| File | Nội dung |
|---|---|
| [nhu-cau-nguoi-xem.md](nhu-cau-nguoi-xem.md) | **điểm vào tư duy**: loại nội dung → cái khó của người xem → nguyên lý (12 nguyên lý Mayer + 4 ngoài Mayer) |
| [nguyen-ly.json](nguyen-ly.json) | tên loại / nguyên lý hợp lệ (công cụ kiểm tra đọc) |
| [truong-hop-da-giai.md](truong-hop-da-giai.md) | 19 trường hợp giải từ 8 hình mẫu thành công cùng thể loại (số liệu đo) |
| [bai-kiem/](bai-kiem/README.md) | bài kiểm suy luận 10 đoạn + công cụ chấm, chạy khi có thiết bị mới / đổi luật |
| [huong-dan-lua-chon.md](huong-dan-lua-chon.md) | **các bước tự chọn** + kho cách thể hiện xếp theo nguyên lý |
| [bo-cuc.md](bo-cuc.md) | danh mục bố cục: dùng khi nào, viết thế nào, có code chưa |
| [am-thanh.md](am-thanh.md) | cách đặt tiếng hiệu ứng / nhạc theo bố cục |
| [nguon-tham-khao/](nguon-tham-khao/) | mỗi nguồn đã học một file: học gì, ở phút nào |
| [phieu-hoc-mau.md](phieu-hoc-mau.md) | mẫu phiếu học đưa David duyệt trước khi sửa skill |
