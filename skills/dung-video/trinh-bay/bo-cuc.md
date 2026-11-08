# Danh mục bố cục

Đây là kho để chọn, không phải công thức. Màu, chữ, chuyển động luôn lấy từ `thu-vien-hinh/`. Chữ trong thẻ là nguyên văn lời người nói.
Cột "Code": **có** = viết được ngay trong `scenes.js` · **chưa** = mới học ý, cần làm code khi có video cần.

## Người là chính

| Kiểu | Hợp khi | Ngang / dọc | Code |
|---|---|---|---|
| Người + phụ đề | kể chuyện, cảm xúc, lời mời, câu tâm tình | cả hai | có (mặc định) |
| Điểm nhấn trên người (`nhan`): zoom dồn, làm tối viền, chữ / biểu tượng cạnh mặt | câu đắt, cú chốt | cả hai | có (khối 07) |
| **Thẻ cạnh mặt** (`bocuc` · `the-canh`): người giữ nguyên, thẻ ở phía trống, chữ hiện dần theo lời, có thể gạch chữ | liệt kê ngắn, đổi ý ("không cần A, chỉ cần B"), nêu 2–4 điểm mà vẫn muốn thấy người | ngang tốt nhất; dọc: thẻ dưới cằm, ít dòng | có |

## Người và nội dung cùng hiện

| Kiểu | Hợp khi | Ngang / dọc | Code |
|---|---|---|---|
| **Người vào ô bo góc** (`bocuc` · `o-nguoi`): người co từ toàn khung vào ô, phần còn lại là nội dung (`illus`, `diagram` hoặc thẻ chữ), hết cảnh nở lại toàn khung | giải thích dài, nhiều bước, so sánh, khung giờ / con số cần nhìn lâu mà vẫn giữ người | ngang: ô cột phải; dọc: ô nửa trên, nội dung nửa dưới | có |
| Người nằm trong một thẻ giữa chuỗi thẻ (thẻ "Bước 2" chứa chính video quay mặt) | người nói là một bước của quy trình đang kể | ngang | chưa |
| Màn hình máy / ảnh chụp trong khung + chú thích đánh số ở góc dưới ("① Chọn thư mục") | hướng dẫn thao tác, cho xem tài liệu | ngang; dọc thì phóng vào phần chính | chưa |

## Nội dung là chính

| Kiểu | Hợp khi | Ngang / dọc | Code |
|---|---|---|---|
| Minh hoạ toàn màn hình (`illus`, `diagram`) | một ý cần hình rõ, người không cần hiện | cả hai | có (khối 07) |
| **Màn chương** (`bocuc` · `chuong`): số to mờ + nhãn nhỏ + tên phần | video dài chuyển sang phần mới | cả hai | có |
| Tít nhỏ trên + tít to + hàng thẻ bên dưới (thẻ hiện lần lượt, thẻ đang nói sáng lên, thẻ cũ mờ đi) | tổng quan nhiều mục, kết quả, "trong video này" | ngang | chưa (gần `illus` list) |
| Vòng lặp / chu trình (V1 → góp ý → sửa → V2) | quy trình lặp | cả hai | gần `diagram` `vong` |

## Cách nối giữa bố cục

| Cách | Hợp khi | Code |
|---|---|---|
| Người co vào ô rồi nở lại (liền một hình, không cắt) | vào và ra `o-nguoi` | có |
| Thẻ trượt vào từ phía trống | vào `the-canh` | có |
| Video thu nhỏ bay vào thẻ / thẻ phóng ra thành toàn khung | từ màn chương sang người, từ tổng quan sang chi tiết | chưa |

## Viết trong `scenes.js` (video 1 người)

```js
// thẻ cạnh mặt
{id: 'b1', type: 'bocuc', start: 89.3, end: 101.0, props: {kieu: 'the-canh', tieu_de: 'Đi cùng những ai',
  dong: [{text: 'sức khỏe đang bị nền tảng kém', at: 94.2}, {text: 'MÌNH XUẤT HIỆN', at: 100.2, to: true}]}},
// người vào ô + minh hoạ
{id: 'b2', type: 'bocuc', start: 127.6, end: 138.6, props: {kieu: 'o-nguoi', noi_dung: {type: 'illus', props: {mode: 'flow', items: [...]}}}},
// người vào ô + thẻ chữ (gach = giây bắt đầu gạch)
{id: 'b4', type: 'bocuc', start: 154.1, end: 206.3, props: {kieu: 'o-nguoi', noi_dung: {type: 'the', props: {tieu_de: 'Chọn giờ nắng',
  dong: [{text: '10 GIỜ SÁNG', at: 161.6, to: true, gach: 165.4}, {text: '7 GIỜ ĐẾN 9 GIỜ SÁNG', at: 198.2, to: true}]}}}},
// màn chương
{id: 'c2', type: 'bocuc', start: 143.8, end: 147.5, props: {kieu: 'chuong', so: 2, nhan: 'hằng ngày', ten: 'ĐI BỘ\nNGOÀI NẮNG'}},
```

- **Không có gì cố định (David chốt 08/11/2026):** vị trí, cỡ, tỉ lệ ô, phía đặt thẻ đều tự tính theo người trong khung và nội dung.
  `o-nguoi`: tỉ lệ ô tự do theo khung cắt quanh người đang nói, ô nằm đúng phía người đó ngồi, không cắt ngang mặt ai (`khung: 'ca-hai'`
  khi muốn ô chứa mọi người). `the-canh`: thẻ vào khoảng trống sát người đang nói, co theo khoảng trống, hết chỗ thì tự thành `o-nguoi`.
  `bam: 'trai'|'phai'` khi graphic nói về một người cụ thể (thẻ tên khách). `o: {x, y, w, h}` chỉ khi thật cần ép tay.
- Vị trí người lấy từ `mat.js`, do `face_place.sh` → `nhan_place.py` tự ghi cho mọi cảnh `nhan` và `bocuc`: **mọi người** trong khung
  (kể cả người quay nghiêng máy không thấy rõ mặt) + **người đang nói** (pyannote + cử động miệng). Graphic đặt qua `src/lib/cho.js`:
  không đè, không làm mờ bất kỳ ai.
- Ô người dùng video gốc (`public/goc.mp4`, render.mjs tự nối), nên cảnh `o-nguoi` / `chuong` là lớp đặc, ghép đè được như cảnh toàn màn hình.
- Chưa làm cho podcast (không có mặt) và vlog ghép (`montage-template`). Khi cần thì thêm cùng kiểu.
