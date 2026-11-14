# Lỗi đã gặp (riêng podcast) — đọc cùng `$BASE/references/loi-thuong-gap.md`

## Lời nói
- **Mốc từ của Whisper trôi qua khoảng lặng ở chỗ đổi người** (thử nghiệm: "Cảm ơn anh" của người dẫn bị đặt sớm ~1,6 s, rơi vào
  lượt khách) → nguoi-noi.py dời ranh giới đổi người vào khoảng lặng thật dài nhất trong ±2,5 s; phụ đề quanh chỗ đổi người phải
  dời tay theo `nguoi-noi.js`.
- Whisper nghe nhầm như skill gốc ("con nhà" → "căn nhà", "cái đá" → "cái đã", "Cô đang" → "Còn đang") — đối chiếu 2 lần chạy.

## Người nói
- **nguoi-noi.py dùng pyannote** (`tach-nguoi-noi.py`, venv `~/.venvs/pyannote`, mô hình speaker-diarization-3.1 đã tải, chạy offline trên MPS): tự đếm số người, độ chắc = tỉ lệ thời gian trùng. Thử: podcast 1 người 9 phút → 1 người (~3 phút chạy); họp Zoom 4 phút → tách 2 người. torch ≥ 2.6 chặn nạp mô hình → tach-nguoi-noi.py cho phép đúng 4 lớp siêu dữ liệu (TorchVersion, Specifications, Problem, Resolution), không tắt kiểm tra. Vẫn đọc `check/speakers.md` theo nội dung.
- Dự phòng (pyannote lỗi / không có venv): ước đoán theo giọng (cao độ + phổ mel + kênh trái/phải), k-means, mặc định 2 nhóm. Giọng nam/nữ tách tốt (thử nghiệm:
  thử với giọng nam thật + giọng nữ đọc máy: đúng 8/8 đoạn, độ chắc 0,6–0,9 — chưa thử 2 người thật). Hai giọng cùng giới, cùng âm sắc dễ lẫn → luôn đọc `check/speakers.md` theo nội dung.
- Thu stereo mỗi người một kênh → kênh trái/phải được dùng làm dấu hiệu mạnh (tự bật khi lệch kênh > 1,5 log-năng lượng).
- Cần numpy → `cai-python.sh` cài vào `~/.cache/dung-video-theo-phong-cach/podcast-venv` (python hệ thống không có numpy).

## Render
- Sân khấu `nen` render ~1,5× thời lượng (60 s → 93 s). Đổi TOPICS/STAGE/speakers → phải
  render lại `nen` (đắt) → chốt kỹ ở bước chụp thử.
- Khung ngang ban đầu làm kiểu pillar (sân khấu dọc giữa + chữ hai bên) → David không muốn: **ngang là thiết kế toàn khung**.
  Giờ du-an.js 1920×1080, `chu-de.js` giữ SAFE dọc (dải lớp phủ 830×435) khi `podcast`, `khung-podcast.js` cho hình học khung thật.
- Dải lớp phủ căn giữa khung ngang chạm vòng micro bên phải; căn giữa khung dọc lệch sang cột nút (vùng an toàn dọc không cân:
  lề phải 180) → canh trái theo vùng an toàn ở cả hai khung.
- Cảnh toàn màn hình bản dọc vẽ theo toạ độ 1080×1920 → ở khung ngang bị vỡ. Mỗi loại cần bản ngang riêng (toan-man-hinh-ngang.jsx).
- Ngang: tên người nói đặt dưới ý đang bàn (y 600) bị thẻ/chữ to đè → đặt dưới vòng micro bên phải (lớp phủ canh trái không tới).
- `xuat-video.mjs` không tham số render cả `nen`; `xuat-video.mjs <id>` chỉ render cảnh đó.
- Chụp thử cảnh có `start` sau mốc chụp → preview lấy khung 0 (trống) — mốc chụp phải nằm trong cảnh.

## Chữ tiếng Việt
- Barlow Condensed in hoa với `lineHeight: 1` + khung `overflow: hidden` chừa cố định (34/30 px): ở cỡ 140–150 px dấu chồng của dòng
  dưới chạm dòng trên ("NGẪU", "NHIỀU", "CỦA"), dấu nặng bị cắt ("BỊ" thành "BI"), dấu nặng của dòng nhấn lòi ra khỏi ô màu
  ("LỰC"). Sửa: `VN` trong khung-podcast.js — giãn dòng + chừa chỗ theo tỉ lệ cỡ chữ. Luôn soi ảnh chụp phóng to các chữ Ầ Ễ Ỗ Ị Ự.
- Ô màu của hook cao thêm khi chừa dấu → chạm sóng âm ở cỡ 150 → giới hạn cỡ chữ to podcast ≤ 118–120.

## Nội dung
- **Chỉ nội dung gốc** (luật riêng podcast). Lần thử đầu ghép giọng đọc máy làm "người dẫn" và đặt nhãn "Người dẫn / Khách mời" →
  bị bỏ. Không thêm lời, không tự đặt tên/vai người nói; thử nghiệm cũng chỉ dùng đoạn trích nguyên từ bản ghi thật.
