---
description: "Lớp trình bày video: tiêu chí gốc để học mọi loại video mới, giữ chữ ký nhận diện."
---

# Lớp trình bày — khung gốc để học mọi loại video mới

File này là **tiêu chí gốc**: dù học thêm loại video nào, mọi thứ học được đều đi qua đây, để kiến thức ngày càng phong phú trong khi người xem
vẫn nhận ra video của David.

## 1. Tài nguyên nhận diện và tài nguyên sáng tạo

| Lớp | Gồm | Ở đâu | Khi học video mẫu |
|---|---|---|---|
| **Chữ ký nhận diện** | thành phần cố định (dấu góc, phụ đề, thanh thời gian, màn chốt, thẻ cuối) với hai font chính, nhạc kênh; màu không phải nhận diện; hiệu ứng học từ mẫu lấy chính xác thẩm mỹ của mẫu, kể cả màu nhấn | `thu-vien-tai-nguyen/nhan-dien-chung.md` mục 0, `bien-thiet-ke.js`, `thuong-hieu.json` | Cân nhắc khi tạo phong cách từng video |
| **Phần sáng tạo** (học được) | bố cục, thứ tự thông tin hiện ra, cách nối cảnh, nhịp, chỗ đặt hiệu ứng âm thanh, nền, kết cấu, kiểu hình, chữ nhấn phụ, chuyển động | thư mục này + `bo-cuc.jsx`, `thu-vien-tai-nguyen/` | **Chỉ thêm.** Mỗi điều học được là một mục mới trong kho |

Học càng nhiều thì càng có nhiều tài nguyên để chọn; khi dựng, người dựng chọn các cách thể hiện theo nội dung (`quy-tac-chung.md` mục 0, hiểu hơn cầu kì).

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
4. **Rút ra cách kể và thẩm mỹ:** xem hình mẫu tổ chức cả khung, hướng mắt, thay đổi nhịp và tạo cảm xúc như thế nào. Ghi nguồn,
   điều kiện dùng và một cách chuyển thể sang tư liệu của David. Đưa cả nguyên lý và kỹ thuật có tác dụng thẩm mỹ vào kho.
5. **Phiếu học** (Claude điền, báo David) (mẫu ở `phieu-hoc-mau.md`): học được gì, dùng cho loại video nào, thêm thành phần nào, mỗi thành
   phần đối chiếu với các quy tắc chặn đã có thế nào. Đây là **cổng hỏi duy nhất**: gộp mọi điểm cần chọn, mỗi điểm 2–3 gợi ý.
   **Claude sửa skill luôn, báo David; đụng màu chủ đạo, chữ ký nhận diện thì chờ "duyệt" (Đ3).**
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

## 4a. Tái dựng theo đúng video mẫu

Dùng chế độ này khi David yêu cầu bản gốc bám sát mẫu hoặc muốn xem đủ những hiệu ứng đã học. Bản thử lấy thẩm mỹ của từng mẫu làm chuẩn. Góp ý cho các cảnh cụ thể được áp dụng vào lần chỉnh cảnh sau khi có bản đối chiếu. Chế độ này áp dụng cho bản tái dựng được yêu cầu, độc lập với thiết lập nhận diện dùng khi dựng thông thường.

1. **Kiểm kê từ video mẫu.** Mở toàn bộ phạm vi video đã xác định, ghi từng kiểu chuyển động riêng theo liên kết hoặc file, mốc vào, mốc chính và mốc ra. Lần lặp dùng chung mã nếu cấu tạo và cách dùng giống nhau. Khi thay đổi kết cấu, hành vi hoặc tình huống dùng thì ghi biến thể riêng. Ghi rõ phạm vi chưa xem. Các mục chỉ thấy trong phiếu cũ hoặc bộ template cần nối lại đúng mốc trong video mẫu trước khi tính là đã đối chiếu.
2. **Đo những gì cần dựng.** Đo vị trí theo tỷ lệ khung, điểm neo, tỷ lệ và vùng cắt, thứ tự lớp, bo góc, viền, bóng, màu, chữ, độ mờ, quỹ đạo, tốc độ và mốc tiếng. Ghi trạng thái trước, giữa và sau chuyển động. Dùng mã gốc do tác giả cung cấp nếu khớp với đoạn mẫu và chạy được. Nếu tự dựng, giữ các đặc điểm quan sát được và khai báo chi tiết nào chưa xác định hoặc thay thế do tiếng Việt, tư liệu và tỷ lệ khung khác.
3. **Chọn cảnh từ tư liệu gốc.** Rà các video được phép dùng theo lời và hình. Với mỗi hiệu ứng, lưu điều kiện bắt buộc, dấu hiệu trong lời hoặc hình, trường hợp loại, và thời điểm bắt đầu hiệu ứng so với dấu hiệu trong mẫu. Chọn cảnh đáp ứng đầy đủ, lấy mốc từ âm thanh và hình của đúng file sẽ ghép. Ví dụ, phóng một đường dẫn khi đường dẫn thật đang hiện và được nhắc đến. Mở sơ đồ theo nhánh khi lời thực sự phân các ý cùng cấp. Thu người vào khung khi thông tin chính đã chuyển sang đồ họa và hình thu vẫn đọc được. Thẻ đối chiếu cần hai vế có quan hệ rõ ràng. Nếu hiệu ứng cần đối tượng hay dữ kiện không có, tiếp tục tìm ở nguồn khác được phép dùng.
4. **Dựng bản thử có hình và tiếng nguồn.** Dùng nguyên tắc giữ hình ở [quy tắc chung, mục 4](../quy-tac-chung.md#4-hình). Giữ chữ, màu, nhịp và chuyển động riêng của mẫu. Nếu mẫu dùng đồ họa toàn màn hình, chuyển đồ họa sang vùng riêng có đủ diện tích để hình gốc vẫn chạy. Giữ toàn khung đồ họa khi đoạn số liệu khó hiểu cần thêm diện tích đọc. Đưa ảnh, video và nội dung thật của cảnh vào đúng vai trò của mẫu. Khi lời hoặc hình của nguồn kích hoạt hiệu ứng, giữ quan hệ trước, cùng lúc hoặc sau như đã đo ở mẫu. Cảnh có nhiều nhánh thì neo từng nhánh vào cụm lời riêng. Lưu đường dẫn gốc, đoạn chọn và mốc kích hoạt vào kế hoạch cảnh.
5. **Kiểm bản xuất và độ phủ.** Xem đoạn mẫu và bản xuất từ khung trước chuyển động đến lúc ra, kiểm tiếng Việt, mạch lời, khả năng nhìn chủ thể và độ đọc. Với mỗi mục kho, ghi mốc trong video bàn giao nếu đã ghép và kiểm. Mục còn thiếu ghi cụ thể là chưa lấy được mẫu, chưa tìm thấy cảnh đủ điều kiện, chưa dựng hay chưa kiểm. Chỉ kết luận đã đủ khi phạm vi mẫu đã được xem hết và mọi hiệu ứng trong phạm vi đó có cảnh ghép phù hợp đã kiểm trên bản xuất. Khi người dùng chỉ yêu cầu video trên máy, lưu video và bảng mốc cục bộ.

6. **Khóa bản dựng để chạy lại.** Lưu mã cảnh, mốc, thứ tự chương, tỉ lệ, tài nguyên và phiên bản công cụ cùng một lệnh xuất. Cùng nguồn thì dùng lại chính mã dựng và phông đã khóa. Đối chiếu vân tay của luồng hình và tiếng đã giải mã trên một lần kết xuất mới. Nếu khác môi trường mã hóa, kiểm cả mốc và các khung đại diện trước khi xác nhận hai bản khớp. Xem [cách mở lại trên Claude Code](../../../huong-dan-cai-dat.md#dựng-lại-một-bản-đối-chiếu-motion-graphics).

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
| [phieu-hoc-mau.md](phieu-hoc-mau.md) | mẫu phiếu học Claude điền trước khi sửa skill |
| [kho-hieu-ung-tu-video-goc.md](kho-hieu-ung-tu-video-goc.md) | lá B15: bản xem đủ kho hiệu ứng, mỗi hiệu ứng một đoạn video gốc phù hợp |
