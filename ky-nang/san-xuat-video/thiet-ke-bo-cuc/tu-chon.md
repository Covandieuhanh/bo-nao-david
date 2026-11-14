---
description: "Tự chọn cách trình bày: chẩn đoán video rồi chọn bố cục, hiệu ứng trong kho."
---

# Tự chọn cách trình bày — chẩn đoán video rồi chọn trong kho

David chốt 11/11/2026: "học rất nhiều" thì phải **dùng được**. Kho (`bo-cuc.md`, khối 07, `thu-vien-tai-nguyen/`) là thực đơn. File này là
**cách gọi món**: từ dấu hiệu của video ra bố cục, lớp thông tin, kiểu cảnh. Claude tự chọn, không hỏi, ghi "đã chọn X vì Y" vào
`ke-hoach-canh.md` (mục **Chẩn đoán**) để David sửa ở bản cuối.

Áp cho mọi skill dựng (`dung-video-theo-phong-cach`, `dung-podcast`, `cat-doan-noi-bat`). Bước này chạy **ngay sau chép lời + làm sạch,
trước kế hoạch cảnh**.

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

**Không dùng "cắt khung 16:9 rồi phóng" để bỏ rác** — rác vẫn còn quanh chủ thể (lỗi 11/11/2026). Cắt-phóng chỉ để nắn mép khung.

## Bước 3 — Chọn lớp thông tin (nội dung → người xem theo dõi bằng gì)

| Dấu hiệu nội dung (chan-doan.md) | Lớp thông tin | Code |
|---|---|---|
| **Dày thông tin**: ≥ 3 phút và (mật độ ≥ 140 chữ/phút **hoặc** ≥ 6 chỗ liệt kê / bước / con số), hoặc người nói chính không nhìn camera (cuộc gọi, quay màn hình, bài giảng), hoặc video chia sẻ kiến thức đã chọn khung chủ thể quanh người. Máy báo DÀY THÔNG TIN thì dùng bảng, không tự bỏ vì "nghe như kể chuyện" | **Bảng ghi chú chạy**: tên phần + ý chính nguyên văn cộng dồn, luôn hiện ở phần khung trống | `GHI_CHU` trong canh.js (phu-de.jsx) |
| Video dài > 6 phút, có các phần rõ | Chương: `CHAPTERS` + màn chương (`bocuc chuong`) hoặc thanh tiến trình ý (`bocuc tien-trinh`) khi video theo danh sách | có |
| Mở đầu nói "trong video này…" / nhắc lại các ý đã qua | mục lục tích luỹ (`bocuc muc-luc`) | có |
| Kể chuyện, cảm xúc, ít ý | không thêm lớp — người + phụ đề + điểm nhấn | có |

Bảng ghi chú: mỗi phần = một mục `CHAPTERS` (tên phần nguyên văn); ý = cụm **nguyên văn** 3–10 chữ của câu chốt / câu liệt kê /
con số, `at` = lúc nói. Mỗi phút ~2–4 ý. **Lằn ranh** (số tiền, chuyện người khác, pháp lý…) không đưa vào bảng.

## Bước 4 — Chọn kiểu cảnh (từng ý → kiểu)

Đi hết kho cho từng ý, không dừng ở 3–4 kiểu quen. Mỗi dòng dưới = dấu hiệu trong lời → kiểu.

| Câu nói có dạng | Kiểu | Nơi (khi có khung chủ thể / bảng) |
|---|---|---|
| một vật / việc / khái niệm | `illus single` · chữ nhấn `nhan` | cạnh chủ thể (`canh-nguoi`) |
| nhân quả, các bước 2–3 | `illus flow` | cạnh chủ thể (`canh-nguoi`) |
| quy trình nhiều bước, vẽ tiếp qua nhiều cảnh | `canh-nguoi` + `tu_buoc` / `mach.js` | cạnh chủ thể |
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
| câu đắt, cú chốt, đỉnh cảm xúc | `nhan` zoom / làm tối / chữ cạnh mặt · `the-canh` chữ to | trên người / cạnh |
| giải thích dài vẫn cần thấy người | `o-nguoi` (người vào ô) | — |
| ý riêng không kiểu nào khớp | cảnh tự vẽ `ve` (khối 07 mục 1) | tuỳ |

**Có khung chủ thể + bảng ghi chú:** ưu tiên cảnh **cạnh chủ thể** (thay chỗ bảng trong vài giây) để chủ thể luôn thấy; toàn màn hình chỉ
cho đỉnh và ý cần nhìn rõ. **Không có kiểu nào trong bảng mà lời có dạng rõ** → xem `bo-cuc.md` cột "chưa code"; hợp thì ghi vào
`can-code.md` (hàng đợi làm code), dùng kiểu gần nhất cho video này.

## Bước 5 — Kiểu nào lỗi ở khung nào (máy soát chặn trước)

`soat-canh.mjs` báo P0: `kinetic`, `action` ở khung ngang · cảnh minh hoạ trống > 1,2 s đầu cảnh · phần tử ngoài cảnh. P1: thẻ > 4 dòng
ở khung ngang. Gặp P0 → đổi kiểu theo bảng bước 4, không thử render.

## Ghi vào ke-hoach-canh.md

```
## Chẩn đoán (thiet-ke-bo-cuc/tu-chon.md)
Hình: <4 câu trả lời> → bố cục nền: <X> vì <Y>
Nội dung: <số đo> → lớp thông tin: <X> vì <Y>
Kiểu cảnh dùng: <danh sách> · kiểu hợp mà chưa code: <…> (đã ghi can-code.md)
```

## Học thêm thì thêm dòng ở đây

Mỗi điều học mới (`phan-tich-video-mau`, `thiet-ke-bo-cuc/README.md` mục 4) phải thêm **dấu hiệu nhận ra** vào bảng bước 2, 3 hoặc 4. Học mà không
có dòng ở đây thì sẽ không bao giờ được chọn.
