# Lớp trình bày — khung gốc để học mọi loại video mới

David chốt ngày 07/11/2026. File này là **tiêu chí gốc**: dù học thêm loại video nào, mọi thứ học được đều đi qua đây. Mục đích là để
kiến thức ngày càng dày mà không đụng vào thẩm mỹ của kênh.

## 1. Hai lớp, không trộn

| Lớp | Gồm | Ở đâu | Khi học video mẫu |
|---|---|---|---|
| **Thẩm mỹ** (gốc của David) | màu, font, nét vẽ biểu tượng, kiểu chuyển động, nhạc kênh, tiếng ký hiệu | `thu-vien-hinh/` (tokens, Icons, Illus, Diagram…), `brand.json` | **Không đổi.** Không chép màu, font, kiểu chuyển động của người khác |
| **Trình bày** (học được) | bố cục (người ở đâu, nội dung ở đâu), thứ tự thông tin hiện ra, cách nối cảnh, nhịp, chỗ đặt hiệu ứng âm thanh | thư mục này + `BoCuc.jsx` | **Chỉ thêm.** Mỗi điều học được là một mục mới trong danh mục |

Kiểu bố cục mới chỉ mô tả cách sắp xếp, còn hình vẽ thì lấy từ lớp thẩm mỹ. Vì vậy học thêm không làm lệch gốc và không phải sửa lại.

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

## 3. Luật cứng vẫn giữ (không phải con số)

- Không che mặt người nói. Thu người vào ô bo góc không tính là che.
- Chữ trên màn hình là **nguyên văn lời David** (`video-chu-nguyen-van`): không tự rút tít, không bỏ chữ làm đổi nghĩa.
- Phụ đề luôn chạy. Không ghi chú kỹ thuật trên hình.
- Chuẩn âm lượng chung (khối 09).
- Mấy video đầu dùng bố cục mới: chụp vài khung cho David xem trước khi render (`check/stills.jpg`).

## 4. Quy trình học một video mẫu mới

Học là **bổ sung**, không thay thế (David chốt 08/11/2026, `luat-hoc-la-bo-sung`). Skill `hoc-video-mau` tự bật khi David gửi video
và nói "học cái này"; skill đó chỉ trỏ về đây.

Bước nhẹ (1–3): tới đó nhắc một dòng để David tự đổi mô hình rẻ hơn, không tự đổi.

1. **Lấy mẫu** *(bước nhẹ)*: David gửi file thì dùng file đó. Chỉ có link → tải bản 720p **chỉ để học** vào thư mục tạm (không đưa
   lên repo, **học xong xoá**; David chốt 08/11), đọc mô tả và danh sách chương (`yt-dlp --dump-json`).
2. **Cắt khung** *(bước nhẹ)*: bảng khung theo nhịp 1,5–3 s (`ffmpeg … fps=1/2,scale=480:-1,tile=4x4`) ở đoạn mở đầu và đoạn đúng loại cần học.
3. **Nghe** *(bước nhẹ)*: vẽ phổ âm (`showspectrumpic`) để thấy chỗ có tiếng hiệu ứng, nhạc nền, nốt chuyển chương.
4. **Rút ra, chỉ phần trình bày:** bố cục · thứ tự hiện · cách nối · nhịp · âm thanh. Không ghi màu, font, kiểu vẽ.
5. **Phiếu học cho David duyệt** (mẫu ở `phieu-hoc-mau.md`): học được gì, dùng cho loại video nào, thêm thành phần nào, mỗi thành
   phần đối chiếu với các chặn cũ thế nào. Đây là **cổng hỏi duy nhất**: gộp mọi điểm cần chọn, mỗi điểm 2–3 gợi ý.
   **Chờ David "ok" rồi mới sửa skill.**
6. **Ghi vào kho:** một file `nguon-hoc/<ten-nguon>-<ngay>.md` kể học gì từ đâu. Mỗi cách mới thêm một dòng ở `bo-cuc.md` hoặc `am-thanh.md`,
   ghi rõ "đã có code" hay "chưa có code". Không xoá, không sửa nghĩa dòng cũ.
7. **Làm code khi cần:** thêm `kieu` mới trong `video-style-edit/assets/remotion-template/src/components/BoCuc.jsx` (chỉ dùng
   `C`, `HEAD`, `BODY`, `ease`, `pop`, `Illus`, `Diagram`, `Icon` sẵn có). Vị trí lấy từ hằng số chung (`SAFE`, `BRAND_TOP`/`BRAND_BOT`,
   `PF`, `CAP_H`), **không viết số vị trí riêng**.
8. **Kiểm không phá** (bắt buộc trước khi dùng vào video thật):
   - Thành phần mới đi qua đủ các chặn cũ: không che mặt · không đè phụ đề · nằm dưới dấu góc · trên thanh thời gian · trong vùng an
     toàn · chữ tiếng Việt đủ dấu, không chồng dòng · chữ nguyên văn.
   - Chụp thử **đủ lớp** (cảnh + `phu-de@<giây>` có dấu góc, phụ đề, thanh thời gian) ở **cả khung ngang lẫn dọc**, trên ít nhất
     một dự án cũ đã duyệt. So với ảnh trước khi thêm: phần cũ phải y nguyên.
   - Chạy `soat_canh.mjs` và `python3 -I ../mau-chuan/kiem-mau.py` (mẫu chuẩn); có lệch thì sửa thành phần mới, không sửa cái cũ cho vừa.
9. **Xoá file mẫu đã tải**, **đẩy GitHub** và báo David: thêm gì, đã kiểm gì, chưa kiểm gì.
10. **Không chép công cụ của nguồn** (HyperFrames…): giữ Remotion, chỉ học ý (`video-khong-cai-hyperframes`).

## 5. Dùng khi dựng

- Khi lên kịch bản cảnh (khối 07), đọc `bo-cuc.md` và chọn kiểu theo 4 câu hỏi ở mục 2. Ghi lý do một dòng cho mỗi cảnh vào
  `ke-hoach-canh.md` của dự án.
- Danh mục là **kho để chọn**, không phải công thức. Một video có thể chỉ dùng hai kiểu, cũng có thể dùng năm kiểu, tuỳ nội dung.

## Các file

| File | Nội dung |
|---|---|
| [bo-cuc.md](bo-cuc.md) | danh mục bố cục: dùng khi nào, viết thế nào, có code chưa |
| [am-thanh.md](am-thanh.md) | cách đặt tiếng hiệu ứng / nhạc theo bố cục |
| [nguon-hoc/](nguon-hoc/) | mỗi nguồn đã học một file: học gì, ở phút nào |
| [phieu-hoc-mau.md](phieu-hoc-mau.md) | mẫu phiếu học đưa David duyệt trước khi sửa skill |
