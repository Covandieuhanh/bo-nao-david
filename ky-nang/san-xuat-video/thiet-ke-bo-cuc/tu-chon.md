---
description: "Tự chọn cách trình bày: chẩn đoán video rồi chọn bố cục, hiệu ứng trong kho."
---

# Tự chọn cách trình bày — chẩn đoán video rồi chọn trong kho

Học nhiều thì phải **dùng được**. Kho (`bo-cuc.md`, khối 07, `thu-vien-tai-nguyen/`) là thực đơn. File này là
**cách gọi món**: từ dấu hiệu của video ra bố cục, lớp thông tin, kiểu cảnh. Claude tự chọn, không hỏi, ghi "đã chọn X vì Y" vào
`ke-hoach-canh.md` (mục **Chẩn đoán**) để David sửa ở bản cuối.

Áp cho mọi skill dựng (`dung-video-theo-phong-cach`, `dung-podcast`, `cat-doan-noi-bat`) và **mọi khuôn** (1 video, ghép, podcast). Bước này chạy **ngay sau chép lời + làm sạch,
trước kế hoạch cảnh**.

## Bước 0 — Nguyên tắc: mọi lựa chọn tự setup theo nội dung nguồn

David chốt 19/11/2026: *"mọi thứ cần phát huy tối đa được sức mạnh của AI, mọi lựa chọn đều phải được tự động setup phù hợp với nội
dung của tài nguyên nguồn"*. Vì vậy:
- **Không chép kịch bản, kiểu trình bày của tập trước** làm điểm xuất phát. Mỗi tài nguyên đi lại từ bước 1. Chép được phần kỹ thuật
  (khuôn, hàm, chữ ký nhận diện), không chép lựa chọn (kiểu cảnh, nền, nhịp, nhạc).
- Mọi thứ trong kho (bố cục, motion graphics, thẩm mỹ, chuyển cảnh, nhạc) là ứng viên cho mọi video. Chọn theo **dấu hiệu** ở các bảng
  dưới, ghi "đã chọn X vì Y".
- **Máy chặn trước render** (`soat-canh.mjs`, chạy tự động trong `xuat-video.mjs` và `xuat-chuong-trinh.mjs`): thiếu mục
  `## Chẩn đoán` trong `ke-hoach-canh.md` → P0, không render · cả video chỉ một kiểu lớp phủ nội dung → P0, trừ khi ghi
  `Một kiểu có chủ đích: <lý do>` · thiếu dòng `Thẩm mỹ:` → P1.
- **Khuôn nào có gì** (19/11/2026: tập dựng bằng khuôn ghép chỉ ra chữ nhấn + tít vì khuôn này thiếu nửa kho):

| Khuôn | Dùng cho | Có sẵn |
|---|---|---|
| **1 video** (`khuon-remotion`) | mọi video người nói — **kể cả nhiều file của cùng một buổi nói / cùng cảnh** (nối file trước) · bản dài, bản theo hướng | đủ kho: `nhan`, `bocuc` (the-canh, canh-nguoi, o-nguoi, chuong, muc-luc, tien-trinh), `GHI_CHU`, `CHAPTERS`, `illus`, `diagram`, `ve`, `phong` |
| **ghép** (`khuon-dung-ghep`) | vlog nhiều cảnh khác nhau, sự kiện · clip ngắn highlight người nói | `illus`, `diagram`, `chips`, `callout`, `action`, `pointer`, `pow`, `nameCard`, `location`, `scene`; nền `phong: 'hat'` |
| **podcast** | chỉ có tiếng | sân khấu + kho cảnh của khuôn 1 video |

## Bước 1 — Đo (máy) + nhìn (Claude)

```bash
python3 -I $SKILL/scripts/chan-doan.py "$P"    # → kiem-tra/chan-doan.md (số đo + gợi ý) + kiem-tra/chan-doan.jpg (6 khung gốc)
```
Script đo: khung, độ dài, **mật độ lời** (chữ/phút), **số chỗ liệt kê / bước / con số**, số câu hỏi, tỉ lệ lặng. Claude **xem
`chan-doan.jpg`** và trả lời 4 câu: (1) có thấy rõ mặt người nói không, mặt chiếm bao nhiêu khung; (2) chủ thể cần xem là gì (người,
màn hình điện thoại / laptop, bảng, sản phẩm, cảnh); (3) quanh chủ thể có **rác** không (bàn, tường, đồ vật, mép khung lộn xộn);
(4) máy quay đứng yên hay dịch.

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

Chữ ký nhận diện giữ nguyên (cam, hai font, dấu góc, phụ đề, màn chốt). Phần còn lại chọn theo nội dung, máy đo ở `chan-doan.md`
mục "Tín hiệu thẩm mỹ", Claude quyết.

| Dấu hiệu | Nền cảnh toàn màn hình | Kiểu hình | Chuyển cảnh | Nhạc (khối 09) |
|---|---|---|---|---|
| Kiến thức, giải thích, dày thông tin | tối mặc định (mặc định kênh) | sơ đồ, biểu tượng nét, bảng ghi chú | đổi trên cùng nền, vật lớn dần thành cảnh sau | `kien_thuc` |
| Hướng 3 công nghệ, quy trình, hệ thống | tối + `phong: 'nguoi-mo'` khi cần giữ mạch người nói | `diagram` chuyen-giao / tu-thanh, `illus flow`, mạch vẽ tiếp (`mach.js`) | màu tràn nền ở đổi phần | `kien_thuc` |
| Kể chuyện đời, cảm xúc, tâm sự (nhiều câu cảm xúc, nhịp chậm) | `phong: 'hat'` (giấy ảnh) hoặc người mờ | ít hình, chữ nhấn cạnh mặt, cảnh tự vẽ `ve` mềm | tối dần, không chớp trắng (`TONE 'lang'`) | `tam_su` / `y_nghia` |
| Trò chuyện 1:1, hội thoại | giữ người là chính, nền tối khi cần thấy ý | `the-canh` cạnh người, `illus vs` khi hai góc nhìn | cắt cứng giấu mối + tối nhẹ | theo cảm xúc chủ đạo |
| Vui, năng lượng, mẹo nhanh | tối + điểm sáng cam | `illus single/list`, `chips`, `pow` | chớp, đẩy nhanh (`TONE 'soi'`) | `vui` |
| Video dọc ngắn | như dòng nội dung + mỗi lúc một điểm nhìn | hình to, ít chữ | ngắn, ít kiểu | như dòng nội dung |

Ghi một dòng `Thẩm mỹ: nền … · kiểu hình … · chuyển cảnh … · nhạc … vì …` vào `ke-hoach-canh.md` (mục Chẩn đoán).

## Bước 3 — Chọn lớp thông tin (nội dung → người xem theo dõi bằng gì)

| Dấu hiệu nội dung (chan-doan.md) | Lớp thông tin | Code |
|---|---|---|
| **Dày thông tin**: ≥ 3 phút và (mật độ ≥ 140 chữ/phút **hoặc** ≥ 6 chỗ liệt kê / bước / con số), hoặc người nói chính không nhìn camera (cuộc gọi, quay màn hình, bài giảng), hoặc video chia sẻ kiến thức đã chọn khung chủ thể quanh người. Máy báo DÀY THÔNG TIN thì dùng bảng, không tự bỏ vì "nghe như kể chuyện" | **Bảng ghi chú chạy**: tên phần + ý chính nguyên văn cộng dồn, luôn hiện ở phần khung trống | `GHI_CHU` trong canh.js (phu-de.jsx) |
| Video dài > 6 phút, có các phần rõ | Chương: `CHAPTERS` + màn chương (`bocuc chuong`) hoặc thanh tiến trình ý (`bocuc tien-trinh`) khi video theo danh sách | có |
| Mở đầu nói "trong video này…" / nhắc lại các ý đã qua | mục lục tích luỹ (`bocuc muc-luc`) | có |
| Kể chuyện, cảm xúc, ít ý | không thêm lớp — người + phụ đề + điểm nhấn | có |

Bảng ghi chú: mỗi phần = một mục `CHAPTERS` (tên phần nguyên văn); ý = cụm **nguyên văn** 3–10 chữ của câu chốt / câu liệt kê /
con số, `at` = lúc nói. Mỗi phút ~2–4 ý. **Lằn ranh** (số tiền, chuyện người khác, pháp lý…) không đưa vào bảng.

## Bước 4a — Ý nào cần hình, hình thế nào cho dễ hiểu

David chốt 20/11/2026: *"motion graphics ngày càng thể hiện được rõ sự mô tả các nội dung đang được nói đến… giúp người xem dễ hiểu
hơn nhưng vẫn tinh gọn, đơn giản, không cầu kỳ, loè loẹt gây phân tán sự chú ý"*. Một video không cần nhiều hình; cần hình đúng chỗ.

**Chỉ dựng hình khi ý đó khó hiểu nếu chỉ nghe:** quy trình nhiều bước, quan hệ (nhân quả, tầng bậc, từ → thành), so sánh, con số,
danh sách người xem cần nhớ. Ý dễ (kể chuyện, cảm xúc, lời mời, câu ngắn tự rõ) thì để người nói + phụ đề, nhiều lắm một điểm nhấn.
Hình phủ (toàn màn hình + bố cục) quá ~45 % thời lượng là dấu hiệu dựng thừa: bỏ bớt hình ở ý dễ.

**Năm nguyên lý mỗi hình phải đạt** (học Cường Mê AI, `nguon-tham-khao/cuong-me-ai-2026-11-20.md`):
1. **Theo nhịp lời:** nói tới thứ gì thứ đó mới hiện (`at` = lúc nói), không hiện trước, không hiện hết một lúc.
2. **Một hình lớn dần:** các ý nối nhau thì giữ một hình và thêm phần (`chuoi`, `xay-tang`, `muc-luc`, `mach.js` `tu_buoc`), không
   đổi sang hình rời mỗi câu. Người xem giữ được "bản đồ".
3. **Một chỗ sáng:** phần đang nói sáng cam, phần đã qua mờ (`chuoi`, `xay-tang`, `moc`, `muc-luc` sẵn có; `tang`, `cot` bật `mot_diem: true`).
4. **Đúng loại ý:** bảng dưới (quy trình → `chuoi`, so sánh → `vs`/`tu-thanh`, liệt kê → `list`/`muc-luc`…).
5. **Ít chữ, nền yên:** mỗi nút 1–3 chữ nguyên văn (máy báo khi > 4), nền tối đồng nhất, không thêm trang trí không mang nghĩa.

Ghi vào mục Chẩn đoán một dòng `Tiết chế: <số> ý cần hình / <tổng ý> · bỏ hình ở … vì dễ hiểu khi nghe` (máy soát báo P1 khi thiếu).

## Bước 4 — Chọn kiểu cảnh (từng ý cần hình → kiểu)

Với các ý bước 4a chọn ra, đi hết kho để tìm kiểu diễn tả đúng nhất, không dừng ở 3–4 kiểu quen. Mỗi dòng dưới = dấu hiệu trong lời → kiểu.

| Câu nói có dạng | Kiểu | Nơi (khi có khung chủ thể / bảng) |
|---|---|---|
| một vật / việc / khái niệm | `illus single` · chữ nhấn `nhan` | cạnh chủ thể (`canh-nguoi`) |
| nhân quả, các bước 2–3 | `illus flow` | cạnh chủ thể (`canh-nguoi`) |
| quy trình nhiều bước, vẽ tiếp qua nhiều cảnh | `canh-nguoi` + `tu_buoc` / `mach.js` | cạnh chủ thể |
| quy trình 3–6 bước kể liền một mạch ("đầu tiên… rồi… cuối cùng") | `diagram chuoi` (bước hiện theo lời, dây có chấm chạy, bước đang nói sáng) | toàn màn hình; dọc giải thích dài → `o-nguoi` `nguoi_duoi` + `chuoi` |
| so sánh nên / không nên, trước / sau | `illus vs` · trước/sau | toàn màn hình hoặc cạnh |
| một con số người nói | `illus count` | toàn màn hình (ngắn) |
| liệt kê 3–5 thứ | `illus list` · `the-canh` (giữ người) · thêm vào bảng ghi chú | cạnh chủ thể |
| tầng bậc / cấp | `diagram tang` · `xay-tang` (tầng sau cần tầng trước) | toàn màn hình |
| trong → ngoài | `diagram vong` | toàn màn hình |
| mốc thời gian | `diagram moc` | toàn màn hình |
| so độ lớn nhiều con số | `diagram cot` | toàn màn hình |
| phần trên tổng | `diagram luoi` | toàn màn hình |
| từ … thành … | `diagram tu-thanh` · `doi-trang-thai` | toàn màn hình |
| việc đi từ người này sang người kia | `diagram chuyen-giao` | toàn màn hình |
| người / nơi / tổ chức có thật | `diagram anh` | cạnh hoặc toàn |
| đổi ý ("không phải A, mà là B") | `the-canh` có gạch chữ | cạnh chủ thể |
| câu đắt, cú chốt, đỉnh cảm xúc | `nhan` làm tối / chữ cạnh mặt · `the-canh` chữ to | trên người / cạnh |
| giải thích dài vẫn cần thấy người | `o-nguoi` (người vào ô); khung dọc: `nguoi_duoi: true` (hình nửa trên, người nửa dưới) | — |
| ý riêng không kiểu nào khớp | cảnh tự vẽ `ve` (khối 07 mục 1) | tuỳ |

**Có khung chủ thể + bảng ghi chú:** ưu tiên cảnh **cạnh chủ thể** (thay chỗ bảng trong vài giây) để chủ thể luôn thấy; toàn màn hình chỉ
cho đỉnh và ý cần nhìn rõ. **Không có kiểu nào trong bảng mà lời có dạng rõ** → xem `bo-cuc.md` cột "chưa code"; hợp thì ghi vào
`can-code.md` (hàng đợi làm code), dùng kiểu gần nhất cho video này.

## Bước 5 — Kiểu nào lỗi ở khung nào (máy soát chặn trước)

`soat-canh.mjs` báo P0: `kinetic`, `action` ở khung ngang · cảnh minh hoạ trống > 1,2 s đầu cảnh · phần tử ngoài cảnh. P1: thẻ > 4 dòng
ở khung ngang. Gặp P0 → đổi kiểu theo bảng bước 4, không thử render.

## Ghi vào ke-hoach-canh.md (thư mục dự án, cạnh `chuyen-dong/`)

```
## Chẩn đoán (thiet-ke-bo-cuc/tu-chon.md)
Khuôn: <1 video / ghép / podcast> vì <Y>
Hình: <4 câu trả lời> → bố cục nền: <X> vì <Y>
Nội dung: <số đo> → lớp thông tin: <X> vì <Y>
Thẩm mỹ: nền … · kiểu hình … · chuyển cảnh … · nhạc … vì …
Tiết chế: <số> ý cần hình / <tổng ý> · bỏ hình ở … vì dễ hiểu khi nghe
Kiểu cảnh dùng: <danh sách> · kiểu hợp mà chưa code: <…> (đã ghi can-code.md)
```
Bảng ý → kiểu (mỗi ý chính một dòng: mốc · câu nguyên văn · dạng câu · kiểu chọn) đi ngay dưới, là nguồn để viết `canh.js` /
`danh-sach-cat.js`.

## Học thêm thì thêm dòng ở đây

Mỗi điều học mới (`phan-tich-video-mau`, `thiet-ke-bo-cuc/README.md` mục 4) phải thêm **dấu hiệu nhận ra** vào bảng bước 2, 3 hoặc 4. Học mà không
có dòng ở đây thì sẽ không bao giờ được chọn.
