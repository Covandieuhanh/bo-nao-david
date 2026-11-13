# Danh mục bố cục

Đây là kho để chọn, không phải công thức. Giữ chữ ký nhận diện (`thu-vien-hinh/nhan-dien-chung.md` mục 0); ngoài đó tự do (10/11/2026). Chữ trong thẻ là nguyên văn lời người nói.
Cột "Code": **có** = viết được ngay trong `scenes.js` · **chưa** = mới học ý, cần làm code khi có video cần.

## Người là chính

| Kiểu | Hợp khi | Ngang / dọc | Code |
|---|---|---|---|
| Người + phụ đề | kể chuyện, cảm xúc, lời mời, câu tâm tình | cả hai | có (mặc định) |
| Điểm nhấn trên người (`nhan`, không zoom): làm tối viền, chữ / biểu tượng cạnh mặt | câu đắt, cú chốt | cả hai | có (khối 07) |
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

## Mục lục, nền, chữ nhấn (học Ali Abdaal + Joseph Video Editing, 10/11/2026 — `nguon-hoc/ali-joseph-2026-11-10.md`)

| Kiểu | Hợp khi | Ngang / dọc | Code |
|---|---|---|---|
| **Mục lục tích luỹ** (`bocuc` · `muc-luc`): người vào ô, danh sách đánh số hiện dần, mục đang nói sáng, mục cũ mờ | "trong video này", nhắc lại các ý đã qua | cả hai | có |
| **Thanh tiến trình ý** (`bocuc` · `tien-trinh`): đường nối nút 1…n, chạy tới ý hiện tại, tên ý dưới nút | video theo danh sách (ý 1, 2, 3…), thay màn chương | cả hai | có |
| **Mạch hình cạnh người** (`bocuc` · `canh-nguoi`): người giữ khung, hình vẽ thẳng vào khoảng trống sát người, không thẻ nền (như bảng phấn) | giải thích dài mà vẫn muốn thấy người; nhiều cảnh vẽ tiếp một mạch | ngang (cần khoảng trống ≥ 26 % bề ngang); thiếu chỗ tự thành `o-nguoi` | có |
| **Nền người mờ** (`phong: 'nguoi-mo'` ở cảnh toàn màn hình): nền = chính video người nói làm mờ + tối | cảnh toàn màn hình mà không muốn đứt khỏi người (giữa câu chuyện) | cả hai | có (FullShell, Illus, Diagram, BoCuc) |
| **Nền hạt** (`phong: 'hat'`): nền tối + hạt nhiễu như giấy ảnh | cảnh trích câu, lắng | cả hai | có |
| **Một từ nhấn kiểu khác** (`*từ*` trong chữ): font phụ có chân, nghiêng, màu cam | một từ mang nghĩa chính trong cụm; tối đa một chỗ mỗi cụm | cả hai | có (mọi chữ đi qua `ChuHien`) |
| Hàng nhãn viên thuốc có biểu tượng (Linux · Cameras · Security) bật quanh người | kể tên nhiều thứ ngắn, công cụ, kỹ năng | cả hai | chưa (gần `nhan` icon) |
| Cảnh đời thường toàn khung + người nói ở ô nhỏ góc, chữ trích dưới trái | có cảnh quay thêm minh hoạ lời kể | ngang | chưa (cần cảnh quay thêm; hợp vlog) |
| Một đường kẻ nối xuyên nhiều cảnh (đường chạy từ cảnh này sang cảnh sau) | mạch ý dài, "nét riêng" của một video | cả hai | chưa (làm bằng cảnh tự vẽ `ve` + `mach.js`) |
| Ảnh tài liệu / bài báo, tô màu dòng đang nói | minh chứng, trích nghiên cứu | ngang | chưa (gần `card` ảnh) |
| Trước / sau hai khung cạnh nhau | so sánh kết quả | cả hai | chưa (gần `card` `vs`) |
| Người làm mờ phía sau, chữ / vật nổi giữa khung (không cắt sang nền tối) | câu chốt giữa đoạn nói | cả hai | = `phong: 'nguoi-mo'` cho cảnh toàn màn hình |

## Nền và lớp thông tin (11/11/2026 — chọn theo `tu-chon.md`)

| Kiểu | Hợp khi | Ngang / dọc | Code |
|---|---|---|---|
| **Khung chủ thể** (`khung_chu_the.py`): chủ thể tách thành khung bo góc trên nền kênh | quay màn hình điện thoại / laptop, vật, người nhỏ giữa nhiều rác | ngang (dọc: chưa thử) | có |
| **Bảng ghi chú chạy** (`GHI_CHU` trong scenes.js): tên phần + ý nguyên văn cộng dồn, luôn hiện ở phần khung trống, cảnh hiện thì nhường | video dày thông tin, cuộc gọi, bài giảng, người nói không nhìn camera | ngang (dọc: chưa thử) | có |

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

```js
// mục lục tích luỹ · thanh tiến trình ý · mạch hình cạnh người
{id: 'l1', type: 'bocuc', start: 56, end: 70, props: {kieu: 'muc-luc', tieu_de: '5 nguyên tắc', muc: [{text: 'Tiền phải tiết kiệm', at: 57}, …]}},
{id: 't2', type: 'bocuc', start: 250.9, end: 254.5, props: {kieu: 'tien-trinh', so: 2, tong: 5, nhan: 'Nguyên tắc 2', ten: 'Đầu tư vào *bản thân*'}},
{id: 'k1', type: 'bocuc', start: 338.9, end: 353.1, props: {kieu: 'canh-nguoi', noi_dung: {type: 'illus', props: {mode: 'flow', items: [...]}}}},
// cảnh toàn màn hình trên nền người mờ
{id: 'm1', type: 'illus', start: 132.6, end: 137.7, props: {mode: 'count', …, phong: 'nguoi-mo'}},
```

