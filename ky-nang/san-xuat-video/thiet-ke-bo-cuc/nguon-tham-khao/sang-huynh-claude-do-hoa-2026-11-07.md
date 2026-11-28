---
description: "Nguồn học Sang Huỳnh: Claude làm motion graphics trong video (07/11)."
---

# Sang Huỳnh — "Claude Làm Hết Motion Graphics Trong Video Này" (học 07/11/2026)

- Nguồn: https://www.youtube.com/watch?v=zmnjXAlCPEU · 18:56 · ngang 16:9 · làm bằng HyperFrames (không cài, chỉ học ý).
- Đoạn đã xem: 0:00–0:42 (mở đầu, quay mặt và đồ hoạ), 12:38–17:35 (phần video quay mặt).
- Hiệu ứng học từ nguồn này giữ trọn thẩm mỹ của mẫu: màu kem, đỏ cam, font, tỉ lệ, nhịp (`thu-vien-tai-nguyen/nhan-dien-chung.md` mục 0, David 28/11/2026) — mã `rieng/mau-sang-huynh.jsx`, bảng màu `M`.

## Tài nguyên trực tiếp của tác giả

- [Prompt của video](https://aislop.vn/prompt/3-kieu-video-bang-claude-hyperframes/) và [kho hiệu ứng](https://aislop.vn/bo-hieu-ung/).
- [Echo number](https://aislop.vn/bo-hieu-ung/echo-number/): thẻ trắng, lớp chữ viền lặp, nền xám sáng và số chính xanh lam. Hợp đoạn có con số quan trọng và người nói.
- [Spotlight magnifier](https://aislop.vn/bo-hieu-ung/spotlight-magnifier/): giảm sáng vùng ngoài điểm nhìn, viền phát sáng vẽ quanh phần cần xem, ô chú thích và đường dẫn. Hợp đoạn quay thao tác trên màn hình.
- [Flowchart highlight](https://aislop.vn/bo-hieu-ung/flowchart-highlight/): sơ đồ nhánh, vùng quét đánh dấu và camera tiến vào cụm ý. Hợp đoạn có đầu vào, cơ chế, các nhánh song song và kết quả.

Mỗi trang có clip đối chiếu, đặc tả và liên kết mã nguồn. Khi dựng theo đúng mẫu, giữ cấu hình thẩm mỹ của template, thay nội dung và mốc theo tài nguyên.

## Bố cục học được

1. **Thẻ cạnh mặt:** người giữ nguyên khung, một thẻ cao bo góc chiếm khoảng một phần ba ở phía nền trống, chữ xây dần theo lời:
   gạch chữ cũ thì hiện chữ mới ("không cần biết CODE · chẳng cần dựng video · chỉ cần PROMPT"), danh sách hiện từng dòng, lưới
   ảnh nhỏ hiện dần. Thẻ sáng hoặc tối tuỳ đoạn. → `the-canh`.
2. **Người vào ô bo góc:** video quay mặt thu thành ô nhỏ ở góc trên, nền đồ hoạ chiếm phần lớn ("Cách 3 · Video quay mặt"). → `o-nguoi`.
3. **Người nằm trong thẻ:** thẻ "Bước 2 · Quay" chứa chính video quay mặt, nằm giữa chuỗi 3 bước. → `ve` · `NguoiTrongThe`.
4. **Màn chương:** số to mờ "03" phía sau, nhãn nhỏ "CÁCH 3", tên phần to, dòng cuối màu nhấn. → `chuong`.
5. **Màn hình máy trong khung, chú thích đánh số** ở góc dưới trái ("① Chọn thư mục · nơi AI làm việc"); thẻ lời nhắc phóng to đè lên. → `ve` · `GoLenh` (thẻ gõ lệnh) và `SoiSang` (soi vùng màn hình).
6. **Tổng quan:** tít nhỏ trên + tít to giữa + hàng 3 thẻ; thẻ đang nói sáng lên, thẻ khác mờ đi; nhãn "làm từ…" dưới mỗi thẻ. → `ve` · `HangThe`.
7. **Vòng lặp:** vòng tròn "V1 · Xem lại → Góp ý → Sửa" và đếm vòng ở góc. → gần `diagram` `vong`.
8. Phụ đề nhỏ ở góc dưới trái khi người toàn khung (không dùng: kênh giữ phụ đề của mình).

## Nhịp

- Phần quay mặt: người toàn khung xen thẻ cạnh mặt dài cả chục giây; các đoạn toàn đồ hoạ kéo dài hàng phút khi đang hướng dẫn.
  Tức là không có trần cứng, độ dài theo nội dung.
- Chữ xây theo đúng lúc nói; thẻ ở lại suốt ý, không bật tắt liên tục.

## Âm thanh (đọc phổ âm)

- Nhạc nền nhỏ chạy suốt dưới lời.
- Tiếng sáng, cao, ngắn đúng lúc thẻ / chữ lớn hiện (0:01, 0:10, 0:15–0:17, 0:25).
- Mở chương "Cách 3" (12:38): nốt nhạc ngân khoảng 1,3 giây trước khi lời vào.
- Tiếng lướt / click nhỏ ở chỗ nối cảnh.

## Đối chiếu trực tiếp để tái dựng theo mẫu (27/11/2026)

Rà toàn tập bằng bảng khung ba giây và mở lại các đoạn dưới đây ở mốc chọn. Đọc theo [quy trình tái dựng theo đúng video mẫu](../README.md#4a-tái-dựng-theo-đúng-video-mẫu). Cột mốc dẫn tới trạng thái dễ nhìn trong mẫu. Khi cần dựng chính xác, mở hai phía của mốc để xác định khung vào và khung kết.

| Mốc mẫu | Cách trình bày quan sát được | Chọn khi nguồn có | Dấu hiệu để đặt động tác |
|---|---|---|---|
| 00:10–00:18 | Thẻ viền sáng trên nền tối, làm rõ thẻ đang được nói, nhãn nhỏ đi với hình của từng thẻ | Các hạng mục độc lập, có tư liệu thật cho từng hạng mục | Tên hạng mục xác định thẻ sáng, lời nói về nguồn xác định nhãn dưới thẻ |
| 00:21–00:27 | Thẻ dọc sáng cạnh người, gạch chữ cũ rồi hiện chữ thay thế | Một câu nói bác bỏ cách cũ và nêu cách thay | Gạch khi cụm phủ định hoàn chỉnh, hiện chữ mới khi người nói xác nhận phương án thay |
| 00:28–00:40 | Thẻ dọc tối, từng hình thu nhỏ và nhãn tăng dần | Giới thiệu các ví dụ có hình tương ứng | Mỗi hình và nhãn bám một ví dụ vừa được gọi tên |
| 00:52–00:57, 12:47–12:53 | Thẻ nổi sáng trên nền kem, có ô chờ, số, hình rồi nhãn | Liệt kê các mục cùng cấp hoặc quy trình có bước rõ | Đợi đến khi tên mục đủ nghĩa mới mở thẻ tương ứng |
| 00:59–01:05 | Một bảng số lớn kèm thanh ngang | Một đại lượng có đơn vị và mức so sánh xác định | Số và thanh dùng cùng mốc số liệu, đối chiếu giá trị và đơn vị với tiếng gốc |
| 01:36–01:41 | Hai nguồn hội tụ vào công cụ, sau đó đi xuống đầu ra | Hai đầu vào cùng tạo một kết quả | Hiện riêng từng đầu vào, vẽ đường hội tụ khi quan hệ rõ, mở đầu ra khi được nhắc đến |
| 02:45–02:54 | Màn hình trong khung sáng, nhãn dưới, phóng lớp câu lệnh ở trung tâm | Có cảnh giao diện thật và đúng câu lệnh, nút hoặc đối tượng đang được giải thích | Chờ thao tác chỉ hoặc cụm tên đối tượng, để vùng đang giải thích nhìn rõ |
| 05:00–05:10 | Điểm sáng cam, nhiều đường mảnh toả ra, nét đậm cho đường được chọn, chú thích hệ quả | Một điểm xuất phát dẫn tới nhiều lựa chọn hoặc hướng chú ý | Mỗi hướng mở theo cụm lời riêng, chú thích hệ quả chỉ xuất hiện khi lời đã nêu hệ quả |
| 12:39–12:46 | Chữ số chìm trên nền tối, nhãn rồi tiêu đề trắng và cam, hình minh họa ở nửa phải | Bước sang phần mới có tên và trật tự xác nhận được | Mở ở chỗ đổi phần, chữ và hình lần lượt dẫn người xem vào phần mới |
| 15:50–15:56 | Hai thẻ trắng cạnh nhau trên nền kem, lần lượt tiết lộ cách làm | Hai cách hoặc hai thời kỳ có chung một việc để đối chiếu | Giữ vế đầu khi vế thứ hai vào, điền điểm khác biệt được nói ra |
| 18:49–18:55 | Thẻ sáng bo góc, lời chào chữ đậm hai tầng đặt cạnh người | Câu chào hay câu hẹn được nói thật ở cuối đoạn | Dùng đúng lời chào, hiện cụm sau khi người nói sang vế sau |

## Đo để dựng (27/11/2026, bảng khung 0,67 giây ở đúng mốc; mã gốc của tác giả cho 3 hiệu ứng aislop)

Mã: `dung-video-theo-phong-cach/assets/mau-remotion/src/rieng/mau-sang-huynh.jsx`. Vị trí ghi theo phần khung (0–1).

| Mốc mẫu | Cảnh `ve` | Đo được |
|---|---|---|
| 05:00–05:10 | `ToaNhanh` | nền tối chuyển sắc; điểm cam tại (0,17; 0,56) nảy vào; 6 nhánh mảnh vẽ lần lượt khoảng 0,7 giây mỗi nhánh tới x 0,62, nhãn chữ đơn cách; khi chọn: nhánh cũ mờ còn khoảng 30 %, nét đỏ cam vẽ khoảng 1 giây xuống dưới, chấm ✕ + nhãn; nét trắng lên trên, chấm ✓; đường đứt dọc nối hai đầu + chữ to màu nhấn |
| 01:36–01:41 | `HoiTu` | hai thẻ chip ở y 0,2; dây hội tụ vẽ khoảng 0,6 giây vào chip giữa y 0,44; đường cam dọc + nhãn; thẻ trắng kết quả nảy, dấu ✓ xanh khoảng 0,7 giây sau; chip phụ gạch ngang mờ bên phải |
| 00:59–01:05 | `SoVang` (+ thanh) | mã tác giả echo-number 3,8 giây: thẻ trượt 40 px và phóng 0,96 thành 1 (0,8 giây, expo), số nảy 0,8 thành 1 (0,6 giây, back 1,6), 6 lớp chữ viền vang ra ±112/224/336 px; mẫu video thêm thanh tiến trình đổi theo số |
| 02:45–02:54 | `GoLenh` · `SoiSang` | màn hình làm tối, thẻ lệnh giữa (0,12–0,88 bề ngang) gõ khoảng 12–14 chữ mỗi giây; nhãn viên thuốc góc dưới trái; mã tác giả spotlight-magnifier 10 giây: làm mờ 7 px + giảm sáng 50 % trong 0,6 giây, viền vàng vẽ 0,45 giây, phóng vùng 1,3 lần, nhãn từng chữ, đường chỉ 0,5 giây, chấm 0,3 giây |
| 00:10–00:18 | `HangThe` | hàng 3 thẻ 16:9 giữa khung trên nền tối; thẻ đang nói viền cam, thẻ khác mờ còn khoảng 45 %; nhãn viên thuốc dưới thẻ; tít to hai màu hiện từng chữ |
| 15:50–15:56 | `HaiThe` | nền kem; dòng tiêu đề có biểu tượng đồng hồ hiện từng chữ, từ cuối màu nhấn, rồi lên trên; thẻ trắng 1 trượt lên, thẻ 2 vào khoảng 1,3 giây sau; số màu nhấn |
| 18:49–18:55 | `TheChao` | hai thẻ kem bên phải (x 0,66–0,96): thẻ trên nhãn nhỏ + nút đỏ cam nảy lần lượt; thẻ dưới chữ đậm tầng 1, dòng nhỏ, tầng 2 hiện từng chữ với từ cuối màu nhấn; cả cảnh mờ dần cuối |
| 00:28–00:40 | `TheDocToi` | thẻ dọc tối x 0,655–0,965, y 0,05–0,95, mở từ trên xuống khoảng 0,4 giây; tít to có số màu nhấn; từng hình thu nhỏ + số thứ tự + nhãn sáng lên đúng lúc nói; nút cuối thẻ |
| bố cục 3 | `NguoiTrongThe` | chuỗi thẻ trắng nối bằng dây đứt cam; thẻ bước có hình chứa chính video người nói |

Ví dụ dùng từng cảnh trên tư liệu thật: `~/Movies/tap-kho-hieu-ung-2711/ghep/doan.json` (bản xem đủ kho hiệu ứng, lá B15).

## Giao diện đo (28/11/2026, từ khung hình gốc 12:38–17:35)

Dùng qua `GIAO_DIEN` trong `thu-vien/bien-thiet-ke.js`; bảng `MAU_CUA` gắn mỗi loại cảnh với giao diện mẫu của nó (David 28/11/2026: hiệu ứng học
từ mẫu giữ trọn thẩm mỹ của mẫu, `thu-vien-tai-nguyen/nhan-dien-chung.md` mục 0).

| Giao diện | Dùng cho | Số đo |
|---|---|---|
| `sang-huynh-sang` | màn đồ hoạ có người trong ô (`bocuc o-nguoi`, sơ đồ và minh hoạ đặt trong ô người) | nền giấy sáng giữa #FAF7F6, mép #EEEBE8 → #E5E1DB, lưới chấm rất mờ; thẻ trắng #FFFFFF bóng mềm nâu; chữ đen than; nhãn nhỏ in hoa giãn chữ màu nhấn; chip đen #201D1A; dấu tích xanh #49725D; khung người viền trắng dày khoảng 5 px |
| `sang-huynh-the` | thẻ đè lên video (`bocuc the-canh`, `cau-hoi`, `DuongMay` gạch thay, thẻ lật, lời nhắc; cảnh tự vẽ đè video mượn giao diện này) | thẻ trắng #FFFFFF bóng mềm nâu, chữ đen than #1C1B1A, nhãn nhỏ in hoa màu nhấn #B5604A |
| `sang-huynh-toi` | chương lớn và màn chương | thẻ #30302D, nhãn xám #B0B0AB in hoa, chữ kem #F4F2EE, cụm nhấn màu nhấn; màn chương nền #111111, số to mờ, dòng 2 màu nhấn |

Thẻ cạnh mặt (đo khung 0:21–0:30, 28/11/2026): thẻ cao x 0,63–0,97, y 0,06–0,94, nền kem #F3F1EE hơi trong; chữ dẫn nhỏ xám (khoảng 3 % chiều cao khung) → từ bị gạch chữ hẹp đậm in hoa xám có vạch đỏ (khoảng 8 %) → **từ khoá chính rất to** chữ hẹp đậm in hoa đen (khoảng 12 %) gạch chân màu nhấn → dòng liệt kê nhỏ có biểu tượng nhỏ (khoảng 3 %). Trong `bocuc the-canh`: dòng thường = chữ nhỏ, `to: true` = từ khoá chính, `gach` = từ bị gạch; chỉ một từ khoá chính cho mỗi thẻ.

Màu nhấn đỏ đất của mẫu giữ nguyên: #B5604A trên nền sáng, #E79377 trên nền tối (David 28/11/2026: lấy chính xác từ mẫu, không phối lại).
Font tiêu đề của mẫu là chữ hẹp đậm giống Barlow Condensed, chữ thường giống Be Vietnam Pro, nên giữ hai font chính.
