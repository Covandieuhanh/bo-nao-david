---
description: "Tự chọn cách trình bày: yêu cầu người dùng → đo → loại nội dung → bố cục nền, thẩm mỹ, lớp thông tin → từng đoạn: cái khó → nguyên lý → cách thể hiện trong kho."
---

# Tự chọn cách trình bày — lập luận từ nội dung rồi chọn trong kho

**Đọc trước:** [nguoi-xem-can-gi.md](nguoi-xem-can-gi.md) (cách nghĩ: loại nội dung → cái khó → nguyên lý). File này là các bước làm
và **kho cách thể hiện** xếp theo nguyên lý. Kho (`bo-cuc.md`, khối 07, `thu-vien-tai-nguyen/`) là thực đơn; người dựng (AI nào cũng
được) tự chọn, không hỏi, ghi lý do vào `ke-hoach-canh.md` (mục **Chẩn đoán**) để David sửa ở bản cuối.

Áp cho mọi skill dựng (`dung-video-theo-phong-cach`, `dung-podcast`, `cat-doan-noi-bat`) và **mọi khuôn** (1 video, ghép, podcast). Chạy
**ngay sau chép lời + làm sạch, trước kế hoạch cảnh**.

## Bước 0 — Nguyên tắc: mọi lựa chọn tự setup theo nội dung nguồn

- **Không chép kịch bản, kiểu trình bày của tập trước** làm điểm xuất phát. Mỗi tài nguyên đi lại từ đầu. Chép được phần kỹ thuật
  (khuôn, hàm, chữ ký nhận diện), không chép lựa chọn (kiểu cảnh, nền, nhịp, nhạc).
- Mọi thứ trong kho (bố cục, motion graphics, thẩm mỹ, chuyển cảnh, nhạc) là ứng viên cho mọi video; chọn bằng lập luận ở
  `nguoi-xem-can-gi.md`, ghi lý do.
- **Máy chặn trước render** (`soat-canh.mjs`, chạy tự động trong `xuat-video.mjs` và `xuat-chuong-trinh.mjs`), chi tiết ở bước 5.
- **Khuôn nào có gì** (khuôn thiếu kiểu thì video nghèo hình — chọn khuôn đúng trước):

| Khuôn | Dùng cho | Có sẵn |
|---|---|---|
| **1 video** (`khuon-remotion`) | mọi video người nói — **kể cả nhiều file của cùng một buổi nói / cùng cảnh** (nối file trước), phỏng vấn · bản dài, bản theo hướng | đủ kho: `nhan`, `bocuc` (the-canh, canh-nguoi, o-nguoi, chuong, muc-luc, tien-trinh, dung-hay, tren-duoi, o-tron, cau-hoi), `GHI_CHU`, `CHAPTERS`, `illus`, `diagram`, `ve`, `phong` |
| **ghép** (`khuon-dung-ghep`) | vlog nhiều cảnh khác nhau, sự kiện · clip ngắn highlight người nói | `illus`, `diagram`, `chips`, `callout`, `action`, `pointer`, `pow`, `nameCard`, `location`, `scene`; nền `phong: 'hat'` |
| **podcast** | chỉ có tiếng | sân khấu + kho cảnh của khuôn 1 video |

## Bước 0b — Yêu cầu của người dùng (`yeu-cau.md`, `them-anh/`)

Thư mục dự án có sẵn (tạo bởi `tao-du-an.sh`, `tao-dung-ghep.sh`):
- **`yeu-cau.md`** — người dùng viết / dán lời nói tự do: muốn hiệu ứng gì, đoạn nào, giống video nào, bỏ gì.
- **`them-anh/`** — ảnh bỏ vào: tên bắt đầu `mau-` = **ảnh mẫu** (kiểu muốn bắt chước); còn lại = **ảnh chèn** vào video.

Cách làm:
1. **Thứ tự ưu tiên:** luật cứng (`nguoi-xem-can-gi.md` mục 0) > yêu cầu người dùng > tự chọn. Yêu cầu trái luật cứng → không làm, ghi lý do.
2. **Ảnh mẫu:** xem ảnh, gọi tên nó giải cái khó nào (nguyên lý), rồi chọn cách thể hiện gần nhất trong kho; không có thì tự vẽ (`ve`)
   và ghi `can-code.md`. Không chép màu, font của ảnh mẫu (chữ ký nhận diện giữ nguyên).
3. **Ảnh chèn:** chép vào `chuyen-dong/public/anh/`, dùng qua `photo: '<tên>'` (`diagram anh`, `dung-hay`, `tren-duoi`, `o-tron`…) đúng lúc lời nhắc tới.
4. Ghi vào Chẩn đoán: `Yêu cầu: <tóm tắt> → làm ở <cảnh> · bỏ <…> vì <…>` (yêu cầu trống thì `Yêu cầu: không`).

## Bước 1 — Đo (máy) + nhìn

```bash
python3 -I $SKILL/scripts/chan-doan.py "$P"    # → kiem-tra/chan-doan.md (số đo + gợi ý) + kiem-tra/chan-doan.jpg (6 khung gốc)
```
Script đo: khung, độ dài, **mật độ lời** (chữ/phút), **số chỗ liệt kê / bước / con số**, số câu hỏi, tỉ lệ lặng. Người dựng **xem
`chan-doan.jpg`** và trả lời 4 câu: (1) có thấy rõ mặt người nói không, mặt chiếm bao nhiêu khung; (2) chủ thể cần xem là gì (người,
màn hình điện thoại / laptop, bảng, sản phẩm, cảnh); (3) quanh chủ thể có **rác** không (bàn, tường, đồ vật, mép khung lộn xộn);
(4) máy quay đứng yên hay dịch.

## Bước 1b — Loại nội dung cả video

Đọc bản chép lời + số đo → chọn loại ở `nguoi-xem-can-gi.md` mục 1 (có thể pha hai loại). Loại quyết định người xem cần gì là chính,
mức dày hình, nhịp, nhạc cho bước 2b–4. Ghi `Loại: <tên> vì <dấu hiệu> · cần chính: <…>`.

## Bước 2 — Chọn bố cục nền (hình gốc → nền)

| Dấu hiệu hình gốc | Bố cục nền | Cách làm |
|---|---|---|
| Người nói trước camera, người **chiếm phần lớn khung** (selfie dọc, cận mặt), hoặc kể chuyện / cảm xúc | **giữ khung gốc** | — |
| **Video chia sẻ kiến thức, thông tin** (lời có lý do, liệt kê, khái niệm) mà người **chiếm < ~50 % khung** (ngồi xa máy, hai bên là tường / phòng trống) | **khung chủ thể quanh người** + phần còn lại cho **bảng thông tin** (`GHI_CHU`) và cảnh, ảnh cạnh người | `khung-chu-the.py` (vùng = người, gồm tay khi múa tay) |
| Chủ thể là **màn hình** (điện thoại, laptop, máy tính bảng), **vật**, **bảng** — chiếm < ~60 % khung, hoặc quanh có rác | **khung chủ thể**: tách chủ thể thành khung bo góc trên nền kênh; phần còn lại cho bảng ghi chú, phụ đề, cảnh | `khung-chu-the.py luoi` → đọc toạ độ → `kiem-tra/khung.json` → `apply` (khối 04) |
| Người nhỏ trong khung rộng, nền rác, nhưng cần thấy người | khung chủ thể quanh người (ô dọc hoặc ngang) | như trên, vùng = người |
| Gốc dọc, xuất ngang | pillar (`dat-dau-ra.py pillar`) + `SIDES` | khối 04 |
| Gốc ngang, xuất dọc (chỉ khi David nói rõ) | reframe bám người nói | khối 04 |
| Chỉ có tiếng | sân khấu podcast | `dung-podcast` |

**Không dùng "cắt khung 16:9 rồi phóng" để bỏ rác** — rác vẫn còn quanh chủ thể (khối 04). Cắt-phóng chỉ để nắn mép khung.

## Bước 2b — Chọn thẩm mỹ (nền, kiểu hình, chuyển cảnh, nhạc)

Chữ ký nhận diện giữ nguyên (cam, hai font, dấu góc, phụ đề, màn chốt). Phần còn lại theo loại nội dung (bước 1b) + số đo ở
`chan-doan.md` mục "Tín hiệu thẩm mỹ".

| Dấu hiệu | Nền cảnh toàn màn hình | Kiểu hình | Chuyển cảnh | Nhạc (khối 09) |
|---|---|---|---|---|
| Kiến thức, giải thích, dày thông tin | tối mặc định (mặc định kênh) | sơ đồ, biểu tượng nét, bảng ghi chú | đổi trên cùng nền, vật lớn dần thành cảnh sau | `kien_thuc` |
| Hướng 3 công nghệ, quy trình, hệ thống | tối + `phong: 'nguoi-mo'` khi cần giữ mạch người nói | `diagram` chuyen-giao / tu-thanh, `illus flow`, mạch vẽ tiếp (`mach.js`) | màu tràn nền ở đổi phần | `kien_thuc` |
| Kể chuyện đời, cảm xúc, tâm sự (nhiều câu cảm xúc, nhịp chậm) | `phong: 'hat'` (giấy ảnh) hoặc người mờ | ít hình, chữ nhấn cạnh mặt, cảnh tự vẽ `ve` mềm | tối dần, không chớp trắng (`TONE 'lang'`) | `tam_su` / `y_nghia` |
| Trò chuyện 1:1, hội thoại | giữ người là chính, nền tối khi cần thấy ý | `the-canh` cạnh người, `illus vs` khi hai góc nhìn | cắt cứng giấu mối + tối nhẹ | theo cảm xúc chủ đạo |
| Vui, năng lượng, mẹo nhanh | tối + điểm sáng cam | `illus single/list`, `chips`, `pow` | chớp, đẩy nhanh (`TONE 'soi'`) | `vui` |
| Video dọc ngắn | như dòng nội dung + mỗi lúc một điểm nhìn | hình to, ít chữ | ngắn, ít kiểu | như dòng nội dung |

Ghi `Thẩm mỹ: nền … · kiểu hình … · chuyển cảnh … · nhạc … vì …`.

## Bước 3 — Chọn lớp thông tin (người xem theo dõi cả video bằng gì)

| Dấu hiệu nội dung (chan-doan.md) | Lớp thông tin | Code |
|---|---|---|
| **Dày thông tin**: ≥ 3 phút và (mật độ ≥ 140 chữ/phút **hoặc** ≥ 6 chỗ liệt kê / bước / con số), hoặc người nói chính không nhìn camera (cuộc gọi, quay màn hình, bài giảng), hoặc video chia sẻ kiến thức đã chọn khung chủ thể quanh người. Máy báo DÀY THÔNG TIN thì dùng bảng, không tự bỏ vì "nghe như kể chuyện" | **Bảng ghi chú chạy**: tên phần + ý chính nguyên văn cộng dồn, luôn hiện ở phần khung trống | `GHI_CHU` trong canh.js (phu-de.jsx) |
| Video dài > 6 phút, có các phần rõ | Chương: `CHAPTERS` + màn chương (`bocuc chuong`) hoặc thanh tiến trình ý (`bocuc tien-trinh`) khi video theo danh sách | có |
| Mở đầu nói "trong video này…" / nhắc lại các ý đã qua | mục lục tích luỹ (`bocuc muc-luc`) | có |
| Kể chuyện, cảm xúc, ít ý | không thêm lớp — người + phụ đề + điểm nhấn | có |

Bảng ghi chú: mỗi phần = một mục `CHAPTERS` (tên phần nguyên văn); ý = cụm **nguyên văn** 3–10 chữ của câu chốt / câu liệt kê /
con số, `at` = lúc nói. Mỗi phút ~2–4 ý. **Lằn ranh** (số tiền, chuyện người khác, pháp lý…) không đưa vào bảng.

## Bước 4 — Từng đoạn: cái khó → nguyên lý → cách thể hiện

**4a. Đoạn nào cần hình (Tinh gọn):** chỉ dựng hình khi ý đó khó hiểu nếu chỉ nghe — quy trình nhiều bước, quan hệ (nhân quả, tầng bậc,
từ → thành), so sánh, con số, danh sách cần nhớ. Ý dễ (kể chuyện, cảm xúc, lời mời, câu ngắn tự rõ) → người nói + phụ đề, nhiều lắm
một điểm nhấn. Hình phủ (toàn màn hình + bố cục) quá ~45 % thời lượng là dựng thừa. Ghi `Tiết chế: <số> ý cần hình / <tổng ý> · bỏ hình ở … vì dễ hiểu khi nghe`.

**4b. Mỗi hình phải đạt:** Đúng lúc (`at` = lúc nói, không hiện hết một lúc) · Chia đoạn (ý nối nhau thì giữ một hình lớn dần: `chuoi`,
`xay-tang`, `muc-luc`, `mach.js` `tu_buoc`) · Báo hiệu (một chỗ sáng cam, phần đã qua mờ; `tang`, `cot` bật `mot_diem: true`) · Lời kèm hình
(hình đúng cấu trúc câu, bảng dưới) · Tinh gọn (mỗi nút 1–3 chữ nguyên văn, máy báo khi > 4; nền yên).

**4c. Kho cách thể hiện, xếp theo nguyên lý.** Gọi tên cái khó → tìm nguyên lý → đi hết các dòng của nguyên lý đó, không dừng ở 3–4 kiểu
quen. Ghi mỗi cảnh một dòng `- <id> · Cần: <nguyên lý> · Vì: <cái khó> · Làm: <cách>` (`nguoi-xem-can-gi.md` mục 4).

| Nguyên lý | Câu nói / hình có dạng | Cách thể hiện có sẵn | Nơi (khi có khung chủ thể / bảng) |
|---|---|---|---|
| Lời kèm hình | một vật / việc / khái niệm | `illus single` · chữ nhấn `nhan` | cạnh chủ thể (`canh-nguoi`) |
| Lời kèm hình | nhân quả, các bước 2–3 | `illus flow` | cạnh chủ thể (`canh-nguoi`) |
| Lời kèm hình | một con số người nói | `illus count` | toàn màn hình (ngắn) |
| Lời kèm hình | tầng bậc / cấp | `diagram tang` · `xay-tang` (tầng sau cần tầng trước) | toàn màn hình |
| Lời kèm hình | trong → ngoài | `diagram vong` | toàn màn hình |
| Lời kèm hình | mốc thời gian | `diagram moc` | toàn màn hình |
| Lời kèm hình | so độ lớn nhiều con số | `diagram cot` | toàn màn hình |
| Lời kèm hình | phần trên tổng | `diagram luoi` | toàn màn hình |
| Lời kèm hình | từ … thành … | `diagram tu-thanh` · `doi-trang-thai` | toàn màn hình |
| Lời kèm hình | việc đi từ người này sang người kia | `diagram chuyen-giao` | toàn màn hình |
| Chia đoạn | quy trình 3–6 bước kể liền một mạch ("đầu tiên… rồi… cuối cùng") | `diagram chuoi` (bước hiện theo lời, dây có chấm chạy, bước đang nói sáng) | toàn màn hình; dọc giải thích dài → `o-nguoi` `nguoi_duoi` + `chuoi` |
| Chia đoạn | quy trình nhiều bước, vẽ tiếp qua nhiều cảnh | `canh-nguoi` + `tu_buoc` / `mach.js` | cạnh chủ thể |
| Chia đoạn | liệt kê 3–5 thứ | `illus list` · `the-canh` (giữ người) · thêm vào bảng ghi chú | cạnh chủ thể |
| Chia đoạn | ≥ 2 cặp "đừng… hãy…" / "sai… đúng…" / "thay vì… thì…" nối nhau | `bocuc dung-hay` (một cặp lẻ → `illus vs`) | dọc: khung trên, người dưới · ngang: cạnh người |
| Báo hiệu | lời đếm "thứ nhất / yếu tố 1…" ≥ 3 mục, mỗi mục ≥ ~5 s | `the-canh` + `so` (hoặc `tien-trinh`) | cạnh người |
| Báo hiệu | cụm phụ đề có con số / một chữ quyết định nghĩa (video dọc ngắn) | `hl: ['^từ']` — tối đa một chỗ mỗi dòng | phụ đề |
| Báo hiệu | đổi ý ("không phải A, mà là B") | `the-canh` có gạch chữ | cạnh chủ thể |
| Báo hiệu | phỏng vấn / lời chứng, có người hỏi | `bocuc cau-hoi` + `lower` tên · vai trò | dưới mặt |
| Báo hiệu · Cảm xúc | câu đắt, cú chốt, đỉnh cảm xúc | `nhan` làm tối / chữ cạnh mặt · `the-canh` chữ to | trên người / cạnh |
| Gần chỗ | so sánh nên / không nên, trước / sau | `illus vs` · trước/sau | toàn màn hình hoặc cạnh |
| Gần chỗ | có hai nguồn hình cùng lúc (ảnh trước + video sau, bản gốc + kết quả) | `bocuc tren-duoi` (`giuPhuDe: true`) | toàn màn hình |
| Mặt người nói | giải thích dài vẫn cần thấy người | `o-nguoi` (người vào ô); khung dọc: `nguoi_duoi: true` (hình nửa trên, người nửa dưới) | — |
| Mặt người nói · Lời kèm hình | lời tả chi tiết một thứ cần nhìn kỹ (một bộ phận, sản phẩm, màn hình) ≥ ~4 s, có ảnh / hình vẽ đúng thứ đó | `bocuc o-tron` | toàn màn hình, người ô tròn |
| Tin | người / nơi / tổ chức có thật | `diagram anh` | cạnh hoặc toàn |
| Giữ chú ý | video khoe một thành quả có bản gốc / quá trình | **kết quả trước, cách làm sau**: cảnh thành quả lên đầu, lộ bản gốc sau | thứ tự cảnh |
| bất kỳ | ý riêng không kiểu nào khớp | cảnh tự vẽ `ve` theo đúng nguyên lý (khối 07 mục 1) | tuỳ |

**Có khung chủ thể + bảng ghi chú:** ưu tiên cảnh **cạnh chủ thể** (thay chỗ bảng trong vài giây) để chủ thể luôn thấy; toàn màn hình chỉ
cho đỉnh và ý cần nhìn rõ. **Lời có dạng rõ mà không kiểu nào khớp** → xem `bo-cuc.md` cột "chưa code"; hợp thì ghi vào `can-code.md`
(hàng đợi làm code), video này dùng `ve` hoặc kiểu gần nhất. Ảnh từng kiểu: `bo-cuc.md` mục "Ảnh mẫu".

## Bước 5 — Máy soát chặn trước render (`soat-canh.mjs`)

- **P0 (không render):** thiếu mục `## Chẩn đoán` · thiếu dòng `Loại:` · có cảnh nội dung mà không dòng `Cần:` nào · cả video chỉ một kiểu
  lớp phủ nội dung (trừ khi ghi `Một kiểu có chủ đích: <lý do>`) · `kinetic`, `action` ở khung ngang · cảnh minh hoạ trống > 1,2 s đầu cảnh ·
  phần tử ngoài cảnh · ảnh `photo` không có trong `public/anh`.
- **P1:** thiếu dòng `Thẩm mỹ:`, `Tiết chế:`, `Yêu cầu:` (khi `yeu-cau.md` có nội dung) · cảnh nội dung thiếu dòng `Cần:` · tên loại / nguyên lý
  không có trong `nguyen-ly.json` · hình phủ > 45 % thời lượng · thẻ > 4 dòng ở khung ngang · nhãn > 4 chữ · `dung-hay`, `tren-duoi`, `o-tron`,
  `cau-hoi` thiếu dòng dấu hiệu `<kiểu>: …` · `dung-hay` < 2 cặp · dòng phụ đề > 1 mục `^`.
- **P2:** `so` thiếu dòng `so:` · hai cảnh liền nhau cùng kiểu.
- Dự án tạo trước khi có dòng `Loại:` / `Cần:` (kế hoạch cảnh cũ): hai P0 mới hạ thành P1, để dựng lại bản cũ không bị chặn.

Gặp P0 → sửa kế hoạch / đổi kiểu theo bước 4, không thử render.

## Ghi vào ke-hoach-canh.md (thư mục dự án, cạnh `chuyen-dong/`)

```
## Chẩn đoán (thiet-ke-bo-cuc/tu-chon.md)
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
Bảng ý → cảnh (mốc · câu nguyên văn · dạng câu · cảnh) đi ngay dưới, là nguồn để viết `canh.js` / `danh-sach-cat.js`.

## Học thêm thì thêm ở đây

Học thêm theo `README.md` mục 4: mỗi cách mới thêm một dòng vào bảng 4c dưới đúng nguyên lý. Không có dòng ở bảng 4c thì không bao giờ được chọn.
