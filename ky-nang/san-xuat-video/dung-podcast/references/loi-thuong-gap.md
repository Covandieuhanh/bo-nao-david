---
description: "Lỗi thường gặp riêng khi dựng podcast và cách tránh."
---

# Lỗi đã gặp (riêng podcast) — đọc cùng `$BASE/references/loi-thuong-gap.md`

## Lời nói
- **Mốc thời gian từng từ của Whisper bị lệch qua khoảng lặng ở chỗ đổi người nói** (thử nghiệm: "Cảm ơn anh" của người dẫn bị đặt sớm khoảng 1,6 s, nằm trong
  lượt của khách) nên tach-luot-nguoi-noi.py dời ranh giới đổi người nói vào khoảng lặng thật dài nhất trong ±2,5 s; phụ đề quanh chỗ đổi người nói phải
  được dời thủ công theo `nguoi-noi.js`.
- Whisper nghe nhầm giống như ở skill gốc ("con nhà" thành "căn nhà", "cái đá" thành "cái đã", "Cô đang" thành "Còn đang") — Claude đối chiếu kết quả của 2 lần chạy.

## Người nói
- **tach-luot-nguoi-noi.py dùng pyannote** (`tach-luot-nguoi-noi-pyannote.py`, venv `~/.venvs/pyannote`, mô hình speaker-diarization-3.1 đã tải, chạy offline trên MPS): công cụ tự đếm số người nói, độ tin cậy là tỉ lệ thời gian trùng. Thử nghiệm: podcast 1 người dài 9 phút cho kết quả 1 người (chạy khoảng 3 phút); cuộc họp Zoom 4 phút tách được 2 người. torch từ bản 2.6 trở lên chặn việc nạp mô hình nên tach-luot-nguoi-noi-pyannote.py cho phép đúng 4 lớp siêu dữ liệu (TorchVersion, Specifications, Problem, Resolution), không tắt kiểm tra. Claude vẫn đọc `kiem-tra/nguoi-noi.md` để đối chiếu theo nội dung.
- Dự phòng (khi pyannote lỗi hoặc không có venv): ước đoán theo giọng (cao độ + phổ mel + kênh trái/phải), k-means, mặc định 2 nhóm. Giọng nam và giọng nữ tách tốt (thử nghiệm:
  với giọng nam thật + giọng nữ đọc máy: đúng 8/8 đoạn, độ tin cậy 0,6–0,9 — chưa thử với 2 người thật). Hai giọng cùng giới, cùng âm sắc dễ lẫn nên Claude luôn đọc `kiem-tra/nguoi-noi.md` để đối chiếu theo nội dung.
- Khi thu stereo mỗi người một kênh, kênh trái/phải được dùng làm dấu hiệu mạnh (tự bật khi lệch kênh > 1,5 log-năng lượng).
- Khi cần numpy, `cai-python.sh` cài vào `~/.cache/dung-video-theo-phong-cach/podcast-venv` (python của hệ thống không có numpy).

## Render
- Sân khấu `nen` render mất khoảng 1,5× thời lượng (60 s thành 93 s). Đổi TOPICS/STAGE/speakers thì phải
  render lại `nen` (tốn nhiều thời gian) nên Claude chốt kỹ ở bước chụp thử.
- Khung ngang ban đầu được làm theo kiểu pillar (sân khấu dọc ở giữa + chữ hai bên) thì David không muốn: **khung ngang là thiết kế toàn khung**.
  Hiện tại du-an.js dùng 1920×1080, `chu-de.js` giữ SAFE dọc (dải lớp phủ 830×435) khi `podcast`, `khung-podcast.js` cung cấp hình học của khung thật.
- Dải lớp phủ căn giữa khung ngang thì chạm vòng micro bên phải; căn giữa khung dọc thì lệch sang cột nút (vùng an toàn dọc không cân:
  lề phải 180), nên dải lớp phủ căn trái theo vùng an toàn ở cả hai khung.
- Cảnh toàn màn hình của bản dọc vẽ theo toạ độ 1080×1920 thì bị vỡ ở khung ngang. Mỗi loại cảnh cần bản ngang riêng (toan-man-hinh-ngang.jsx).
- Khung ngang: tên người nói đặt dưới ý đang bàn (y 600) bị thẻ hoặc chữ lớn đè lên, nên tên được đặt dưới vòng micro bên phải (lớp phủ căn trái không chạm tới).
- `xuat-video.mjs` không có tham số thì render cả `nen`; `xuat-video.mjs <id>` chỉ render cảnh đó.
- Khi chụp thử cảnh có `start` sau mốc chụp, bản xem trước lấy khung 0 (trống) — mốc chụp phải nằm trong cảnh.

## Chữ tiếng Việt
- Dấu chồng, dấu bị cắt ở chữ lớn: `$BASE/references/loi-thuong-gap.md` mục "Chữ tiếng Việt". Riêng podcast còn gặp lỗi dấu nặng của dòng
  nhấn tràn ra khỏi ô màu ("LỰC").
- Ô màu của hook cao thêm khi chừa chỗ cho dấu nên chạm sóng âm ở cỡ 150, vì vậy cỡ chữ lớn của podcast giới hạn tối đa 118–120.

## Nội dung
- **Chỉ nội dung gốc** (luật riêng podcast). Lần thử đầu ghép giọng đọc máy làm "người dẫn" và đặt nhãn "Người dẫn / Khách mời" thì 
  bị loại bỏ. Claude không thêm lời, không tự đặt tên hoặc vai trò người nói; thử nghiệm cũng chỉ dùng đoạn trích nguyên văn từ bản ghi thật.
