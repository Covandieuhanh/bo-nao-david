---
description: "Khối 02 làm sạch video: cắt thừa đầu cuối, câu nói lại, khoảng lặng."
---

# Khối 02-lam-sach: Làm sạch: cắt thừa đầu/cuối, câu nói lại, khoảng lặng + tiếng đệm, sửa chiều hình

**Dùng trong:** làm video, highlight (cắt lặng trong câu)
**Đầu vào:** tu-lieu/video-goc-tho.*
**Đầu ra:** tu-lieu/video-goc.mp4 (bản sạch) + kiem-tra/lam-sach/{diem-cat.json, diem-cat.md, cac-doan.json}
**Tham số hồ sơ:** lam-video: cat_lang.*, highlight: cat_lang.*
**Sửa khối này thì chạy lại:** 01 (chép lời trên bản sạch), 03, 04, 05, mọi mốc cảnh (dời theo cac-doan.json)

**File thật (code, một bản duy nhất):**
- `dung-video-theo-phong-cach/scripts/phan-tich-lam-sach.sh`
- `dung-video-theo-phong-cach/scripts/de-xuat-lam-sach.py`
- `dung-video-theo-phong-cach/scripts/ap-dung-lam-sach.py`
- `cat-doan-noi-bat/scripts/khoang-lang.py`

## Luật
- **Video dài > 3 phút không cắt gì** (quy-tac-chung mục 2): `de-xuat-lam-sach.py` tự để mọi cut `ok: false` (chỉ liệt kê). Chỉ sửa chiều
  hình khi cần; không đổi cut nào thành `true` trừ đoạn lằn ranh David đã chọn cắt.
- **Làm lại video cũ:** cắt màn tít + lời chào / giới thiệu kênh cũ bằng cut tay `ok: true` (mọi cut tự động `ok: false`,
  `zoom: "none"`); chữ / viền kênh cũ in trong hình thì cắt khung (gotchas). Sau `ap-dung-lam-sach.py` chạy `doi-moc-loi.py "$P"`, không chép lại.
- Các luật cắt ở mục dưới chỉ cho video tối đa 3 phút.
- **Bản ngắn chỉ giữ một ý** (David: "cắt hết đoạn thừa, chỉ tập trung một ý"): chọn đoạn từ bản chép lời cả video, cắt từng đoạn
  (`-ss -t`, mã hoá lại cùng số khung hình) rồi `concat` thành video gốc trước khi chạy `tao-du-an.sh`; điểm vào / ra dò bằng `diem-ngat.py`
  và chép lời lại đoạn đã ghép. Cảnh không lời giữ lại có chủ ý (cảnh lia phòng làm intro, cảnh minh hoạ) bị máy gợi ý cắt là "thừa đầu"
  hay "lặng": đổi cut đó thành `ok: false`. Whisper chép cả video ghép hay lệch mốc ở cảnh không lời: lấy mốc từng chữ bằng cách chép riêng
  từng đoạn nói rồi cộng giờ bắt đầu đoạn (việc #39, 22/11).
  Video ngắn mời sự kiện mà David thấy "ậm ừ làm chậm": cắt cả khoảng ngừng ngắn từ 0,15 s trong câu (chữ kéo dài "để… tổ… chức"), chừa
  khoảng 0,06 s mỗi bên, mờ tiếng 12 ms ở mối; lời nhanh 1,12 lần (`setpts` + `atempo`, giữ cao độ), cảnh không lời nhanh 1,3 lần.

## Cách làm

**Điểm cắt theo chỗ ngắt tiếng, không theo mốc từ**: `python3 -I $SKILL/scripts/diem-ngat.py <video> <giây>…` cho ra chỗ nhỏ tiếng
gần nhất trước / sau mỗi mốc + vạch năng lượng. Cắt xong, chép lời lại đoạn đã ghép (không nhạc) và đọc chữ đầu / cuối từng mối.
Cắt đoạn từ nguồn dài bằng `-ss <vào> -t <dài> -i nguồn` cho từng đoạn rồi `concat`, **không** dùng `trim=` trên cả file (giải mã từ đầu
file: 8 phút mỗi clip ở nguồn 54 phút).

**Làm sạch** — luôn làm, kể cả khi video trông ổn (không có gì để cắt thì bản sạch chỉ là bản mã hoá lại):
```bash
zsh $SKILL/scripts/phan-tich-lam-sach.sh "$P"          # chạy nền, ~2–4 phút cho video 3–4 phút
```
Đọc `kiem-tra/lam-sach/diem-cat.md` và xem `orient.jpg`, `head.jpg`, `tail.jpg`, rồi chỉnh `kiem-tra/lam-sach/diem-cat.json`:
- **Chiều hình** (`orient`): mặt đất ở trên thì `["180"]`; nằm ngang thì `["cw"]`/`["ccw"]` (xoay sao cho đầu người
  hướng lên); chữ trên áo/biển bị ngược như soi gương thì thêm `"mirror"`. Không chắc thì để trống.
- **Đầu/cuối** (ok sẵn): kiểm `head.jpg`/`tail.jpg` — đang đi về chỗ, chỉnh máy, "ok bắt đầu nhé", "vậy thôi"
  rồi với tay tắt máy thì dời `start`/`end` của cut cho gọn hơn. Câu chào mở đầu thật thì giữ;
  cười/vẫy tay chào sau câu cuối là phần kết thì giữ (dời `start` của cut thừa cuối ra sau, hoặc bỏ cut).
- **Khoảng lặng: CẮT sẵn** (`ok: true`, quy-tac-chung mục 2): lặng ít nhất 0,45 s + tiếng đệm "ờ/ừm".
  Soát `diem-cat.md`: lặng ngay sau câu hỏi tu từ / trước cú chốt cảm xúc mà khoảng ngừng là chủ ý thì đổi `ok: false` để giữ.
  David muốn bản tự nhiên thì chạy `phan-tich-lam-sach.sh "$P" tu-nhien` (chỉ liệt kê lặng ít nhất 3 s, không cắt).
- **Nói lại** (`ok: false`): đọc `moc-tung-tu.srt` quanh mốc; đúng là bỏ dở rồi nói lại thì giữ **lần nói sau cùng**, đặt
  `start` = đầu lần nói hỏng, `end` = ngay trước lần nói giữ lại (cắt giữa hai từ), `ok: true`. Thêm cut tay cho
  lần nói lại mà script không bắt được (câu bỏ dở giữa chừng rồi nói lại khác chữ).
  Nghi ngờ thì **giữ** — cắt mất ý người nói tệ hơn để thừa một nhịp.
```bash
python3 -I $SKILL/scripts/ap-dung-lam-sach.py "$P"     # chạy nền → tu-lieu/video-goc.mp4 (bản sạch)
```
Bản thô giữ lại là `video-goc-tho.<ext>`; `du-an.js` tự trỏ sang bản sạch, mọi bước sau dùng bản sạch.
`zoom: "none"` (mặc định): cắt cứng, không phóng xen kẽ ở mối cắt (`quy-tac-chung.md` mục 2). `"alt"` (phóng 1,08× xen kẽ)
chỉ khi David yêu cầu. Xem 2–3 mối nối (mốc in cuối `diem-cat.md`) bằng `kiem-khung-hinh.sh` với khung
ngay trước/sau mối: mặt không bị cắt, không nháy đen. Báo cáo cuối liệt kê đã cắt gì (`diem-cat.md`).

