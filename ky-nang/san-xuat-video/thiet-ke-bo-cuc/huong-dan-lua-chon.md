---
description: "Tự chọn cách trình bày: đi từ yêu cầu người dùng, số đo, loại nội dung tới bố cục nền, thẩm mỹ, lớp thông tin, rồi từng đoạn đi từ cái khó tới nguyên lý rồi cách thể hiện trong kho."
---

# Tự chọn cách trình bày — lập luận từ nội dung rồi chọn trong kho

**Đọc trước:** [nhu-cau-nguoi-xem.md](nhu-cau-nguoi-xem.md) (cách nghĩ: từ loại nội dung tới cái khó rồi tới nguyên lý). File này là các bước làm
và **kho cách thể hiện** xếp theo nguyên lý. Kho (`bo-cuc.md`, khối 07, `thu-vien-tai-nguyen/`) là danh mục lựa chọn; người dựng (AI nào cũng
được) tự chọn, không hỏi, ghi lý do vào `ke-hoach-canh.md` (mục **Chẩn đoán**) để David sửa ở bản cuối.

Hướng dẫn này áp dụng cho mọi skill dựng (`dung-video-theo-phong-cach`, `dung-podcast`, `cat-doan-noi-bat`) và **mọi mẫu** (1 video, ghép, podcast). Bước này chạy
**ngay sau chép lời và làm sạch, trước kế hoạch cảnh**.

## Bước 0 — Nguyên tắc: mọi lựa chọn tự thiết lập theo nội dung nguồn

- **Không chép kịch bản, kiểu trình bày của tập trước** làm điểm xuất phát. Mỗi tài nguyên được làm lại từ đầu. Người dựng chép được phần kỹ thuật
  (mẫu, hàm, chữ ký nhận diện), không chép lựa chọn (kiểu cảnh, nền, nhịp, nhạc).
- **Chỉ chọn hiệu ứng có hình mẫu, dùng đúng như mẫu** (David 28/11/2026: "đã học từ hình mẫu thì mọi thứ chuẩn đúng theo hình mẫu ở cả
  hiệu ứng và cả motion graphics … đừng sáng tạo và thêm linh tinh nữa"). Hiệu ứng tự chế nằm ở `hieu-ung-luu-tru.json`, không chọn.
  Giá trị của người dựng là phân tích nội dung rồi chọn hiệu ứng mẫu hợp nhất (lập luận ở `nhu-cau-nguoi-xem.md`, ghi lý do); nội dung không
  có hiệu ứng mẫu hợp thì giữ người và phụ đề. Bảng chọn nhanh theo dạng nội dung:
  danh sách ý → thẻ cạnh mặt hiện từng dòng (đoạn dài: người vào ô + thẻ chữ) · ý cũ đổi thành ý mới → thẻ cạnh mặt gạch chữ ·
  một con số → số vang · hai vế đối chiếu có hình → hai thẻ lần lượt tiết lộ · liệt kê có đánh số hoặc "trong video này" → mục lục tích luỹ ·
  các ý theo thứ tự → thanh tiến trình · câu trích đắt → câu đắt hộp trắng · tự giới thiệu tên → thẻ tên · lời chào cuối → thẻ chào.
- **Công cụ chặn trước render** (`soat-canh.mjs`, chạy tự động trong `xuat-video.mjs` và `xuat-chuong-trinh.mjs`), chi tiết ở bước 5.
- **Mỗi mẫu có gì** (mẫu thiếu kiểu thì video ít hình, nên chọn mẫu đúng trước):

| Mẫu | Dùng cho | Có sẵn |
|---|---|---|
| **1 video** (`mau-remotion`) | mọi video người nói — **kể cả nhiều file của cùng một buổi nói / cùng cảnh** (nối file trước), phỏng vấn · bản dài, bản theo hướng | đủ kho: `nhan`, `bocuc` (the-canh, canh-nguoi, o-nguoi, chuong, muc-luc, tien-trinh, dung-hay, tren-duoi, o-tron, cau-hoi), `GHI_CHU`, `CHAPTERS`, `illus`, `diagram`, `ve`, `phong` |
| **ghép** (`mau-dung-ghep`) | vlog nhiều cảnh khác nhau, sự kiện · clip ngắn highlight người nói | `illus`, `diagram`, `chips`, `callout`, `action`, `pointer`, `pow`, `nameCard`, `location`, `scene`; nền `phong: 'hat'` |
| **podcast** | chỉ có tiếng | sân khấu và kho cảnh của mẫu 1 video |

## Bước 0b — Yêu cầu của người dùng (`yeu-cau.md`, `them-anh/`)

Thư mục dự án có sẵn (tạo bởi `tao-du-an.sh`, `tao-dung-ghep.sh`):
- **`yeu-cau.md`** — người dùng viết hoặc dán lời nói tự do: muốn hiệu ứng gì, đoạn nào, giống video nào, bỏ gì.
- **`them-anh/`** — ảnh người dùng đặt vào: tên bắt đầu `mau-` là **ảnh mẫu** (kiểu muốn học theo); còn lại là **ảnh chèn** vào video.

Cách làm:
1. **Thứ tự ưu tiên:** luật bắt buộc (`nhu-cau-nguoi-xem.md` mục 0) > yêu cầu người dùng > tự chọn. Yêu cầu trái luật bắt buộc thì người dựng không làm và ghi lý do.
2. **Ảnh mẫu:** người dựng xem ảnh, gọi tên cái khó mà ảnh đó giải (nguyên lý), rồi chọn cách thể hiện gần nhất trong kho; kho không có thì tự vẽ (`ve`)
   và ghi `can-code.md`. Hiệu ứng học từ ảnh mẫu giữ trọn thẩm mỹ của mẫu (màu, font, tỉ lệ, khoảng trống); phần cố định của kênh giữ nguyên (`thu-vien-tai-nguyen/nhan-dien-chung.md` mục 0).
3. **Ảnh chèn:** người dựng chép vào `chuyen-dong/public/anh/`, dùng qua `photo: '<tên>'` (`diagram anh`, `dung-hay`, `tren-duoi`, `o-tron`…) đúng lúc lời nói nhắc tới.
4. Người dựng ghi vào Chẩn đoán: `Yêu cầu: <tóm tắt> → làm ở <cảnh> · bỏ <…> vì <…>` (yêu cầu trống thì `Yêu cầu: không`).

## Bước 1 — Đo (bằng công cụ) và nhìn

```bash
python3 -I $SKILL/scripts/chan-doan.py "$P"    # → kiem-tra/chan-doan.md (số đo + gợi ý) + kiem-tra/chan-doan.jpg (6 khung gốc)
```
Script đo: khung, độ dài, **mật độ lời** (chữ/phút), **số chỗ liệt kê / bước / con số**, số câu hỏi, tỉ lệ lặng. Người dựng **xem
`chan-doan.jpg`** và trả lời 4 câu: (1) có thấy rõ mặt người nói không, mặt chiếm bao nhiêu khung; (2) chủ thể cần xem là gì (người,
màn hình điện thoại / laptop, bảng, sản phẩm, cảnh); (3) quanh chủ thể có **chi tiết thừa** không (bàn, tường, đồ vật, mép khung lộn xộn);
(4) máy quay đứng yên hay di chuyển.

## Bước 1b — Loại nội dung cả video

Người dựng đọc bản chép lời và số đo rồi chọn loại ở `nhu-cau-nguoi-xem.md` mục 1 (có thể kết hợp hai loại). Loại quyết định người xem cần gì là chính,
mức dày hình, nhịp, nhạc cho bước 2b–4. Người dựng ghi `Loại: <tên> vì <dấu hiệu> · cần chính: <…>`.

## Bước 2 — Chọn bố cục nền (hình gốc quyết định nền)

| Dấu hiệu hình gốc | Bố cục nền | Cách làm |
|---|---|---|
| Người nói trước camera, người **chiếm phần lớn khung** (selfie dọc, cận mặt), hoặc kể chuyện / cảm xúc | **giữ khung gốc** | — |
| **Video chia sẻ kiến thức, thông tin** (lời có lý do, liệt kê, khái niệm) mà người **chiếm < khoảng 50 % khung (ngưỡng riêng cho người)** (ngồi xa máy quay, hai bên là tường / phòng trống) | **khung chủ thể quanh người** và phần còn lại cho **bảng thông tin** (`GHI_CHU`) và cảnh, ảnh cạnh người | `khung-chu-the.py` (vùng là người, gồm cả tay khi người nói cử động tay) |
| Chủ thể là **màn hình** (điện thoại, laptop, máy tính bảng), **vật**, **bảng** — chiếm < khoảng 60 % khung (ngưỡng riêng cho màn hình, vật, bảng; khác ngưỡng của người ở hàng trên), hoặc quanh có chi tiết thừa | **khung chủ thể**: tách chủ thể thành khung bo góc trên nền kênh; phần còn lại cho bảng ghi chú, phụ đề, cảnh | `khung-chu-the.py luoi` → đọc toạ độ → `kiem-tra/khung.json` → `apply` (khối 04) |
| Người nhỏ trong khung rộng, nền có chi tiết thừa, nhưng cần thấy người | khung chủ thể quanh người (ô dọc hoặc ngang) | như trên, vùng là người |
| Gốc dọc, xuất ngang | pillar (`dat-dau-ra.py pillar`) + `SIDES` | khối 04 |
| Gốc ngang, xuất dọc (chỉ khi David nói rõ) | reframe bám người nói | khối 04 |
| Chỉ có tiếng | sân khấu podcast | `dung-podcast` |

**Không dùng "cắt khung 16:9 rồi phóng" để bỏ chi tiết thừa**: chi tiết thừa vẫn còn quanh chủ thể (khối 04). Cắt rồi phóng chỉ để chỉnh mép khung.

## Bước 2b — Chọn thẩm mỹ (nền, kiểu hình, chuyển cảnh, nhạc)

Nhận diện, nền, chữ, hình, chuyển cảnh và nhạc được chọn phù hợp với ngữ cảnh. Tham khảo loại nội dung (bước 1b) và số đo ở
`chan-doan.md` mục "Tín hiệu thẩm mỹ".

| Dấu hiệu | Nền cảnh toàn màn hình | Kiểu hình | Chuyển cảnh | Nhạc (khối 09) |
|---|---|---|---|---|
| Kiến thức, giải thích, dày thông tin | tối mặc định (mặc định kênh) | sơ đồ, biểu tượng nét, bảng ghi chú | đổi trên cùng nền, vật lớn dần thành cảnh sau | `kien_thuc` |
| Hướng 3 công nghệ, quy trình, hệ thống | người còn trên hình: vẽ ở chỗ trống thật (`ve`), không nền mờ; tối chỉ khi không có người trên hình | `diagram` chuyen-giao / tu-thanh, `illus flow`, mạch vẽ tiếp (`mach.js`) | màu tràn nền ở đổi phần | `kien_thuc` |
| Kể chuyện đời, cảm xúc, tâm sự (nhiều câu cảm xúc, nhịp chậm) | `phong: 'hat'` (giấy ảnh) hoặc người mờ | ít hình, chữ nhấn cạnh mặt, cảnh tự vẽ `ve` mềm | tối dần, không chớp trắng (`TONE 'lang'`) | `tam_su` / `y_nghia` |
| Trò chuyện 1:1, hội thoại | giữ người là chính, nền tối khi cần thấy ý | `the-canh` cạnh người, `illus vs` khi hai góc nhìn | cắt cứng giấu điểm nối, thêm tối nhẹ | theo cảm xúc chủ đạo |
| Vui, năng lượng, mẹo nhanh | tối và điểm sáng cam | `illus single/list`, `chips`, `pow` | chớp, đẩy nhanh (`TONE 'soi'`) | `vui` |
| Video dọc ngắn | như dòng nội dung, thêm mỗi lúc một điểm nhìn | hình to, ít chữ | ngắn, ít kiểu | như dòng nội dung |

Người dựng có thể đối chiếu nhiều hướng khi điều đó giúp tìm cách kể phù hợp. So nền, ngôn ngữ hình, nhịp/chuyển cảnh và âm thanh (kể cả giữ tiếng gốc nếu phù hợp). Chọn theo dấu hiệu nhìn hoặc nghe được trong nguồn, và ghi lựa chọn vào mục Chẩn đoán. Dòng đối chiếu dùng khi cần:

- `Thẩm mỹ: nền … · kiểu hình … · chuyển cảnh … · nhạc … vì …`
- `Đối chiếu thẩm mỹ: <hướng còn lại> · Chọn: <hướng thực hiện> · Vì: <dấu hiệu trong nguồn và tác dụng>`

## Bước 3 — Chọn lớp thông tin (người xem theo dõi cả video bằng gì)

| Dấu hiệu nội dung (chan-doan.md) | Lớp thông tin | Code |
|---|---|---|
| **Dày thông tin**: ít nhất 3 phút và (mật độ ít nhất 140 chữ/phút **hoặc** ít nhất 6 chỗ liệt kê / bước / con số), hoặc người nói chính không nhìn camera (cuộc gọi, quay màn hình, bài giảng), hoặc video chia sẻ kiến thức đã chọn khung chủ thể quanh người. Công cụ đo báo DÀY THÔNG TIN thì dùng bảng, không tự bỏ vì "nghe như kể chuyện" | **Bảng ghi chú chạy**: tên phần và ý chính nguyên văn cộng dồn, luôn hiện ở phần khung trống | `GHI_CHU` trong canh.js (phu-de.jsx) |
| Video dài > 6 phút, có các phần rõ | Chương: `CHAPTERS` và màn chương (`bocuc chuong`) hoặc thanh tiến trình ý (`bocuc tien-trinh`) khi video theo danh sách | có |
| Mở đầu nói "trong video này…" / nhắc lại các ý đã qua | mục lục tích luỹ (`bocuc muc-luc`) | có |
| Kể chuyện, cảm xúc, ít ý | không thêm lớp: chỉ người nói, phụ đề và điểm nhấn | có |

Bảng ghi chú: mỗi phần là một mục `CHAPTERS` (tên phần nguyên văn); ý là cụm **nguyên văn** 3–10 chữ của câu chốt / câu liệt kê /
con số, `at` là lúc nói. Mỗi phút khoảng 2–4 ý. **Lằn ranh** (số tiền, chuyện người khác, pháp lý…) không đưa vào bảng.

## Bước 4 — Từng đoạn: cái khó → nguyên lý → cách thể hiện

**4a. Đoạn nào cần hình:** đọc cả mạch và xác định hiệu ứng có thể giúp người xem hiểu, cảm nhận hoặc nhớ gì. Chọn mật độ và thời lượng
  theo lời, hình gốc và nhịp. Video có thể giữ một ngôn ngữ hình xuyên suốt hoặc đổi bố cục theo các điểm chuyển ý.

**4b. Mỗi hình phải đạt:** Đúng lúc (`at` là lúc nói, không hiện hết một lúc) · Chia đoạn (ý nối nhau thì giữ một hình lớn dần: `chuoi`,
`xay-tang`, `muc-luc`, `mach.js` `tu_buoc`) · Báo hiệu (một chỗ sáng cam, phần đã qua mờ; `tang`, `cot` bật `mot_diem: true`) · Lời kèm hình
(hình đúng cấu trúc câu, bảng dưới) · Tinh gọn (mỗi nút 1–3 chữ nguyên văn, công cụ kiểm báo khi > 4; nền yên).

**4c. Kho cách thể hiện, xếp theo nguyên lý.** Người dựng gọi tên cái khó, tìm nguyên lý, rồi đi hết các dòng của nguyên lý đó, không dừng ở 3–4 kiểu quen thuộc.
Người dựng ghi mỗi cảnh một dòng `- <id> · Cần: <nguyên lý> · Vì: <cái khó> · Làm: <cách>` (`nhu-cau-nguoi-xem.md` mục 4).
Cột "Nơi" gợi ý vị trí, có thể chuyển thể theo hình gốc. Nếu giữ hình người đang nói, kiểm tra rõ mặt trong cả cảnh.

**4d. Kho hình mẫu là danh mục lựa chọn, mở ra mỗi lần chọn hình** (22/11/2026 — David: *"tận dụng được tối đa toàn bộ các thẩm mỹ ở trong kho học,
nhưng phải đưa vào cho phù hợp với nội dung, chứ không phải nhét thật nhiều … đơn giản và tinh gọn … gây ấn tượng cho người xem một cách
nhẹ nhàng"*). Với mỗi ý đã qua 4a (cần hình), người dựng đọc lại các cách đã học và chọn cách **hợp với ý đó nhất**:
- `truong-hop-da-giai.md` — 19 trường hợp của 8 kênh hình mẫu (mở đầu, chia đoạn, báo hiệu, lời kèm hình, tin, khi nào không dựng gì).
- `nguon-tham-khao/` — Ali Abdaal và Joseph (14 cách), MagentX (A–G, có dấu hiệu nhận ra), Sang Huỳnh (8 bố cục, nhịp, âm thanh),
  Cường Mê AI (6 nguyên lý); `dung-podcast/references/hoc-tu-hieu-nguyen-50.md` cho podcast.
- Mẫu khung nhiều người, chỗ trống thật (`rieng/duong-may.jsx`): chương lớn, gạch thay, chuỗi nút, thẻ lật, số mốc, câu then chốt, lời nhắc gửi
  AI, thẻ tên và vai trò, vẽ đúng vật (bộ vét, khuôn áo, mảnh ghép).

**Hiệu ứng sinh ra từ ý, thước đo là độ hợp.** Nhận diện nội dung trước rồi mới chọn hiệu ứng hợp nhất; không chọn hiệu ứng trước rồi đi tìm câu
cho nó. Ý khớp gượng (phải đổi lời, chế chữ, "gần giống" dấu hiệu) thì chọn cách khác hoặc để người và phụ đề (David 28/11/2026).

**Yêu cầu bám đúng mẫu hoặc dựng đủ kho hiệu ứng:** dùng [quy trình tái dựng theo đúng video mẫu](README.md#4a-tái-dựng-theo-đúng-video-mẫu) để chọn cảnh, dựng và kiểm đủ. Điều kiện áp dụng dựa trên lời và hình bằng chứng tại mốc của nguồn, cùng vai trò của hiệu ứng trong mẫu.

**So cách tổ chức cả khung hình, rồi chọn hiệu ứng.** Rút từ hình mẫu điều làm cảnh dễ hiểu: mắt nhìn vào đâu trước, quan hệ giữa hình và vật thật, cách điểm nhìn đổi theo lời và lúc nào bố cục chuyển. Các ứng viên có thể là hình gốc với dấu chỉ bám vật, sơ đồ nét vẽ trực tiếp, người và tư liệu được bố trí lại, hoặc cắt sang hình thật phục vụ lời dẫn. Thử cách trình bày khác khi nó có thể làm ý rõ hoặc ấn tượng hơn. Chọn thẻ có nền khi văn bản cần tương phản hoặc các mục cần được phân nhóm. Nếu cỡ chữ chỉ đọc được khi phóng ảnh, đổi bố cục hoặc rút nội dung hình.

Trong bản thử, xem đầu, giữa và cuối từng cảnh ở kích thước phát hành. Đặt các cảnh gần nhau để phát hiện tình trạng đổi biểu tượng hoặc hoạt ảnh trong cùng một ô. Nếu những ý khác nhau vẫn có cùng điểm nhìn, kích thước và cách tổ chức hình, quay lại hình mẫu và dựng lại các cảnh đại diện. Một nhóm ý giống nhau có thể dùng một bố cục xuyên suốt khi bố cục đó giúp người xem theo dõi. Đối chiếu cấu trúc của ý, nhịp nói, vùng trống, khả năng đọc và công cụ của mẫu hiện tại. Có thể giữ hình gốc và phụ đề khi đồ họa không đóng góp gì. Nếu mẫu thiếu cách phù hợp nhất, chuyển cách thể hiện sang công cụ sẵn có hoặc triển khai cảnh tự vẽ theo giao diện của mẫu. Khi chưa thể thực hiện an toàn, ghi giới hạn và chọn ứng viên kế tiếp.

Mỗi cảnh nội dung đã chọn cần một dòng trong mục Chẩn đoán:

```text
- kenh-lien-he · Lựa chọn: DuongMay:the · Ứng viên khác: hai nút nối · Vì sao chọn: hai kênh độc lập, mỗi kênh xuất hiện đúng khi được nhắc
```

`Lựa chọn` là mã thực tế trong phần **Cách thể hiện trong mã** của `kiem-tra/soat.md` (ví dụ `nhan:text`, `bocuc:the-canh`, `DuongMay:the`). Khi đổi cảnh phải cập nhật lý do và nguồn. Bộ soát đối chiếu mã khi kế hoạch đã ghi lựa chọn cụ thể. Xem bản thử ở tỷ lệ phát hành để xác nhận các lựa chọn có thật trên hình, đúng lời, có một điểm nhìn và không che chủ thể. Chỉ đánh giá lịch sử các tập trước khi người dùng yêu cầu đối chiếu.

Tiếng nhẹ (`props.tieng`: `ting` lúc thẻ / chữ lớn hiện, `tua` lúc nối cảnh) chỉ ở
chỗ hình thật sự đổi. Người dựng ghi ở Chẩn đoán dòng `Nguồn kho: <cảnh> ← <nguồn, mã ca>; …` và thêm nguồn vào chú thích từng cảnh trong `canh.js`.
Trước khi xuất, xem liên tiếp các đoạn nhấn ở kích thước phát hành. Nhãn chữ, nhãn biểu tượng và thẻ cạnh người có cùng bố cục phải được xem như cùng một nhóm. Nếu một nhóm chiếm phần lớn cảnh nhấn, tìm một ý có thể kể bằng cách khác trong kho và thử trên đúng khung gốc. Không đổi cảnh chỉ để đủ số. Cách đã học mà kho chưa có code thì người dựng viết thêm vào `rieng/` (mẫu dùng lại), không thay bằng kiểu quen thuộc.

| Nguyên lý | Câu nói / hình có dạng | Cách thể hiện có sẵn | Nơi (khi có khung chủ thể / bảng) |
|---|---|---|---|
| Lời kèm hình | một vật / việc / khái niệm | `illus single` · chữ nhấn `nhan` | cạnh chủ thể (`canh-nguoi`) |
| Lời kèm hình | nhân quả, các bước 2–3 | `illus flow` | cạnh chủ thể (`canh-nguoi`) |
| Lời kèm hình | một con số người nói | `illus count` | thẻ số cạnh người hoặc vật |
| Lời kèm hình | tầng bậc / cấp | `diagram tang` · `xay-tang` (tầng sau cần tầng trước) | cạnh hình gốc hoặc chia khung |
| Lời kèm hình | trong → ngoài | `diagram vong` | cạnh hình gốc hoặc chia khung |
| Lời kèm hình | mốc thời gian | `diagram moc` | cạnh hình gốc hoặc chia khung |
| Lời kèm hình | so độ lớn nhiều con số | `diagram cot` | cạnh hình gốc hoặc chia khung |
| Lời kèm hình | phần trên tổng, khi người xem cần thấy tỉ lệ (chỉ cần nhớ con số thì thẻ chữ, nguyên lý Báo hiệu, trường hợp 9 của `truong-hop-da-giai.md`) | `diagram luoi` | cạnh hình gốc hoặc chia khung |
| Lời kèm hình | từ … thành … | `diagram tu-thanh` · `doi-trang-thai` | cạnh hình gốc hoặc chia khung |
| Lời kèm hình | việc đi từ người này sang người kia | `diagram chuyen-giao` | cạnh hình gốc hoặc chia khung |
| Chia đoạn | quy trình 3–6 bước kể liền một mạch ("đầu tiên… rồi… cuối cùng") | `diagram chuoi` (bước hiện theo lời, dây có chấm chạy, bước đang nói sáng) | cạnh hình gốc; dọc giải thích dài → `o-nguoi` `nguoi_duoi` + `chuoi` |
| Chia đoạn | quy trình nhiều bước, vẽ tiếp qua nhiều cảnh | `canh-nguoi` + `tu_buoc` / `mach.js` | cạnh chủ thể |
| Chia đoạn | liệt kê 3–5 thứ | `illus list` · `the-canh` (giữ người) · thêm vào bảng ghi chú | cạnh chủ thể |
| Chia đoạn | ít nhất 2 cặp "đừng… hãy…" / "sai… đúng…" / "thay vì… thì…" nối nhau | `bocuc dung-hay` (một cặp lẻ → `illus vs`) | dọc: khung trên, người dưới · ngang: cạnh người |
| Báo hiệu | lời đếm "thứ nhất / yếu tố 1…" ít nhất 3 mục, mỗi mục ít nhất khoảng 5 s | `the-canh` + `so` (hoặc `tien-trinh`) | cạnh người |
| Báo hiệu | cụm phụ đề có con số / một chữ quyết định nghĩa (video dọc ngắn) | `hl: ['^từ']` — tối đa một chỗ mỗi dòng | phụ đề |
| Báo hiệu | đổi ý ("không phải A, mà là B") | `the-canh` có gạch chữ | cạnh chủ thể |
| Báo hiệu | phỏng vấn / lời chứng, có người hỏi | `bocuc cau-hoi` + `lower` tên · vai trò | dưới mặt |
| Báo hiệu · Cảm xúc | câu then chốt, điểm chốt cảm xúc, đỉnh cảm xúc | `nhan` làm tối / chữ cạnh mặt · `the-canh` chữ to | trên người / cạnh |
| Gần chỗ | so sánh nên / không nên, trước / sau | `illus vs` · trước/sau | cạnh hình gốc hoặc chia khung |
| Gần chỗ | có hai nguồn hình cùng lúc (ảnh trước và video sau, bản gốc và kết quả) | `bocuc tren-duoi` (`giuPhuDe: true`) | toàn màn hình |
| Mặt người nói | giải thích dài vẫn cần thấy người | `o-nguoi` (người vào ô); khung dọc: `nguoi_duoi: true` (hình nửa trên, người nửa dưới) | — |
| Mặt người nói · Lời kèm hình | lời tả chi tiết một thứ cần nhìn kỹ (một bộ phận, sản phẩm, màn hình) ít nhất khoảng 4 s, có ảnh / hình vẽ đúng thứ đó | `bocuc o-tron` | toàn màn hình, người ô tròn |
| Tin | người / nơi / tổ chức có thật | `diagram anh` | cạnh hoặc toàn |
| Giữ chú ý | video giới thiệu một thành quả có bản gốc / quá trình | **kết quả trước, cách làm sau**: cảnh thành quả lên đầu, hiện bản gốc sau | thứ tự cảnh |
| Lời kèm hình | một điểm xuất phát, nhiều hướng, rồi chọn một ("ngó bên này, bên kia… người chọn lúc đầu") | `ve` `ToaNhanh` | toàn màn hình |
| Lời kèm hình | hai đầu vào cùng tạo một kết quả | `ve` `HoiTu` · `ve` `NguoiTrongThe` (khi một bước là chính hình người nói) | toàn màn hình |
| Báo hiệu | một con số quyết định nghĩa, có người nói ("thiếu mất 0,4 điểm") | `ve` `SoVang` | thẻ trái, người nửa phải |
| Báo hiệu · Đúng lúc | quay màn hình, nói đúng nút / đường dẫn đang hiện; đọc câu lệnh gửi AI | `ve` `SoiSang` · `ve` `GoLenh` | trên hình màn hình |
| Chia đoạn | 3 mục cùng cấp, mỗi mục có hình thật | `ve` `HangThe` (toàn màn hình) · `ve` `TheDocToi` (giữ người) | toàn màn hình / cạnh người |
| Gần chỗ | hai cách / hai thời kỳ cùng một việc ("ngày trước… ngày hôm nay…") | `ve` `HaiThe` | toàn màn hình |
| Giọng trò chuyện | câu chào, câu hẹn gặp lại cuối video | `ve` `TheChao` | cạnh người |
| bất kỳ | ý riêng không kiểu nào khớp | cảnh tự vẽ `ve` theo đúng nguyên lý (khối 07 mục 1) | tuỳ |

**Có khung chủ thể và bảng ghi chú:** người dựng ưu tiên cảnh **cạnh chủ thể** (thay chỗ bảng trong vài giây) để chủ thể luôn được thấy; toàn màn hình chỉ
cho đỉnh và ý cần nhìn rõ. **Lời có dạng rõ mà không kiểu nào khớp** thì xem `bo-cuc.md` cột "chưa code"; hợp thì ghi vào `can-code.md`
(hàng đợi làm code), video này dùng `ve` hoặc kiểu gần nhất. Ảnh từng kiểu: `bo-cuc.md` mục "Ảnh mẫu".

### Gắn chuyển động với lời và hình

**Nhịp xuất hiện mặc định:** dùng fade-in ngắn và easing để hình, chữ hoặc viền đi vào nhẹ. Giữ mốc kích hoạt của lời hoặc sự kiện, rồi tăng độ rõ trong phần đầu chuyển động. Có thể chọn nhịp nhanh hơn khi cần dứt khoát, hoặc giữ mềm hơn khi lời lắng. Các lớp bắt đầu ở mốc riêng. Kiểm bản thử để chắc rằng lớp cũ đứng ổn định, phần mới đọc được đúng lúc và chuyển động không làm nhòe hình quay.

Khi chọn kiểu trong kho, đọc hàng cấu tạo của phiếu học và thiết lập từng chi tiết phù hợp với cảnh. Gắn mỗi thay đổi có ý nghĩa với một cụm lời, một động tác hoặc một điểm cắt. Hiệu ứng có nhiều nhịp, như thu hình rồi hiện hai con số, dùng mốc riêng cho từng nhịp.

Với nhịp theo lời, dùng bản SRT từng từ thuộc chính video đã làm sạch. Khi nguồn hình và bản chép lời có thể thuộc hai bản cắt khác nhau, trích tiếng từ chính tệp sẽ ghép, cùng điểm vào và điểm ra, rồi chép lại đoạn đó. So các cụm đầu, giữa và cuối với tiếng sẽ xuất trước khi dùng SRT cũ. Giữ hình gốc toàn khung ở câu giới thiệu toàn cảnh. Khi lời chuyển sang chi tiết mới khoanh hoặc phóng chi tiết. Giữ sơ đồ ở góc nhìn rộng khi cần theo dõi nhiều nhánh cùng lúc. Nghe đối chiếu cụm quan trọng với tiếng gốc. Chạy `node moc-theo-loi.mjs moc-tung-tu.srt yeu-cau-moc.json` từ thư mục script. JSON có `fps` và mảng `moc`, mỗi mục ghi `cum`, `tuGiay`, `denGiay`, tùy chọn `canh` là `dau` hoặc `cuoi`, và `goc` nếu dựng trích đoạn. Dùng `at` từ kết quả trong mã hiệu ứng. Cụm trùng hoặc không thấy phải được phân giải bằng đoạn hẹp hơn hoặc kiểm lại lời.

Trước khi xuất, chạy `python3 -I scripts/khop-chu-voi-loi.py chuyen-dong/src/canh.js kiem-tra/lam-sach/moc-tung-tu.srt` (thêm `--sua` để dời
mốc về lúc nói): công cụ dò mọi chữ trên hình có `at`, báo chữ hiện sớm hoặc trễ so với lời và chữ không nguyên văn. Mốc theo cử chỉ hay hình
thì khai `"khop": false` ở mục đó. Cảnh có thể khai báo thêm `mocLoi` ở cấp cảnh với cùng dữ liệu và trường `truong` trỏ tới mốc dùng thật, ví dụ `props.items.0.at`. Bộ soát đối chiếu với `kiem-tra/lam-sach/moc-tung-tu.srt` và chặn nếu lệch khung. Nhịp theo cử chỉ hoặc hình dùng mốc khung từ video. Sau khi ghép, xem điểm kích hoạt và nghe lại ở tốc độ thường. Độ khớp với tiếng phụ thuộc vào độ đúng của bản mốc từ, nên kiểm cụm quan trọng bằng tai.

## Bước 5 — Công cụ kiểm chặn trước render (`soat-canh.mjs`)

- **Hiệu ứng có mẫu:** `python3 -I scripts/kiem-hieu-ung-co-mau.py <canh.js>` phải báo 0 hiệu ứng không có mẫu.

- **P0:** lỗi triển khai như phần tử nằm ngoài cảnh, ảnh được gọi bị thiếu, kiểu đã biết lỗi ở khung đang xuất, hoặc mã cảnh lệch lựa chọn đã ghi.
- **P1/P2:** gợi ý rà soát bản thử, gồm khả năng đọc và cảnh tác động lên hình gốc. Số kiểu, mật độ hiệu ứng và số phương án thẩm mỹ do người dựng quyết định theo nội dung.

Gặp P0 thì người dựng sửa kế hoạch hoặc đổi kiểu theo bước 4, không thử render.

## Ghi vào ke-hoach-canh.md (thư mục dự án, cạnh `chuyen-dong/`)

```
## Chẩn đoán (thiet-ke-bo-cuc/huong-dan-lua-chon.md)
Yêu cầu: <tóm tắt yeu-cau.md + them-anh/ → làm ở đâu · bỏ gì vì sao> | không
Khuôn: <1 video / ghép / podcast> vì <Y>
Loại: <tên> vì <dấu hiệu> · cần chính: <hiểu / nhớ / tin / cảm>
Hình: <4 câu trả lời> → bố cục nền: <X> vì <Y>
Nội dung: <số đo> → lớp thông tin: <X> vì <Y>
Thẩm mỹ: nền … · kiểu hình … · chuyển cảnh … · nhạc … vì …
Tiết chế: <số> ý cần hình / <tổng ý> · bỏ hình ở … vì dễ hiểu khi nghe
<kiểu học mới>: <dấu hiệu>      (dung-hay / tren-duoi / o-tron / cau-hoi / so — khi dùng)

- <id cảnh> · Cần: <nguyên lý> · Vì: <cái khó của người xem> · Làm: <cách thể hiện>
```
Bảng ý và cảnh tương ứng (mốc · câu nguyên văn · dạng câu · cảnh) đặt ngay dưới, là nguồn để viết `canh.js` / `danh-sach-cat.js`.

## Học thêm thì thêm ở đây

Việc học thêm làm theo `README.md` mục 4: mỗi cách mới thêm một dòng vào bảng 4c dưới đúng nguyên lý. Cách không có dòng ở bảng 4c thì không bao giờ được chọn.
