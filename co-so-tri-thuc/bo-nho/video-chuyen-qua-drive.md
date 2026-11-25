---
name: video-chuyen-qua-drive
description: "~/Movies xếp theo tập; Drive covandieuhanh chỉ giữ bộ não, video gốc, thành quả video; Mac chỉ giữ việc đang làm (07/11, 08/11, 11/11; gộp 15/11)"
metadata:
  node_type: memory
  type: reference
  originSessionId: 8485f85b-5487-4ff8-8491-137cb6e9e7d2
  modified: 2026-11-11T11:00:00.000Z
---

**Drive chỉ giữ việc của David:** bộ não (luật, ghi nhớ, skill, làm việc với Claude), video gốc của từng video đang làm, thành quả
video (bản cuối đạt hay không, kịch bản, phụ đề, bài đăng). File tải về, dữ liệu app, đồ cá nhân không đồng bộ lên Drive.
**Mac chỉ giữ việc đang làm + bản cuối chưa đăng** (20/11/2026, David: "những kết quả cuối cùng mà tôi chưa đăng thì vẫn cần phải có trong mac để có khi đăng"; "tôi chỉ quan tâm đến các kết quả cuối thôi"): bản cuối ở `~/Movies/cho-dang/<tập>/`, đăng xong `cho-dang.sh xong` mới xoá; trang kiểm `localhost:8765/mac`.
**Việc đang làm:** bắt đầu một video thì chép gốc lên `tu-lieu-goc/<tập>/` (nếu David gửi qua chat/Downloads); xong tập thì `don-tap.py --xoa` → `luu-drive.sh` tải dự án (bỏ file tạm, bỏ gốc đã có) lên
`sao-luu-mac/video/<tập>/`, kiểm đã lên mây, xoá trên Mac, ghi loại vào [kho-drive.md](../../du-an/kho-drive.md).
**Xoá:** việc của David thì chép lên Drive và kiểm đã lên mây trước; thứ khác (app, dữ liệu app, file tải về, đồ cá nhân) thì liệt kê
và hỏi David trước khi xoá hẳn; chỉ xoá thẳng bộ nhớ đệm và file tạm dựng lại được.
Sổ 11/11/2026: (1) David: "máy mac này chỉ còn đóng mỗi vai trò là khi đang thực thi cái gì thì có dữ liệu và tài nguyên của cái đó thôi";
lý do Mac 228 GB đầy, Drive 400 GB. (2) Xoá thẳng dữ liệu Codex theo lời "codex xoá hết", sau đó David cần lại mà không khôi phục được.
(3) David: "không cần đồng bộ tất cả… chỉ khi nào liên quan đến bộ não… và khi làm video thì mới tải video gốc lên… và các thứ liên quan
đến thành quả của video thôi", vì đồng bộ mọi file tải về tốn thời gian.

David điều khiển Mac từ điện thoại bằng Remote Control; không dùng iCloud Drive.
**Drive dùng chung là tài khoản `covandieuhanh@gmail.com`** (David chốt 08/11/2026); không dùng Drive `trainer.davidtran@gmail.com` nữa.
Video gốc David gửi lên: `~/Library/CloudStorage/GoogleDrive-covandieuhanh@gmail.com/Drive của tôi/tu-lieu-goc/`
Thành phẩm trả về: `.../Drive của tôi/thanh-pham/`, **mỗi tập một thư mục, trùng tên với `~/Movies`** (David chốt 08/11/2026): `tap-<ten>/ban-dai/<ten>.mp4` và `tap-<ten>/highlight/clip-a.mp4`, `clip-b.mp4`…; tập chỉ có bản dài vẫn tạo `ban-dai/`. Vlog vào `vlog/<ten>.mp4`, video tự quay vào `video-tu-quay/<ten>.mp4`. Clip ngắn có thể gửi thẳng vào chat bằng SendUserFile.
Kho dự án và bộ não: `.../Drive của tôi/sao-luu-mac/` (Movies, Downloads, Documents, bo-nao). Sao lưu đợt chuyển tài khoản: `.../Drive của tôi/sao-luu-claude-2026-11-07/` gồm `tai-lieu-claude-ai` và `du-an-video` (âm thanh gốc, kịch bản, bỏ file render).
Liên quan (mục gộp dưới), [[co-so-tri-thuc-github-ban-goc]].

Nguồn của luật: `ky-nang/chuan-muc-lam-viec.md` mục 4 ("Giữ dung lượng Mac thấp") và [kho-drive.md](../../du-an/kho-drive.md). Ghi nhớ này giữ ngày, lời David, lý do.

## Gộp từ `video-chuyen-qua-drive` (15/11/2026, tự học tuần: giảm ghi nhớ về 40)

Ngày 07/11/2026 David chốt: video và tài liệu cùng nội dung phải nằm gần nhau. ~/Movies xếp theo tập:
`tap-<tên>/1-goc`, `2-ban-day-du`, `3-doan-noi-bat/` (kế hoạch cắt) + `3-doan-noi-bat/clip-<id>/`, `9-luu-cu`; vlog ở `~/Movies/vlog/<tên>/`; video tự quay cũ ở `video-tu-quay/`.
Sổ chuyển file: `~/Movies/_danh-muc-noi-dung/so-chuyen-file-2026-11-07.tsv`.

**Why:** trước đó gốc, bản dài, clip highlight của cùng một tập nằm ở 4–5 thư mục, David không tìm được.
**How to apply:** khi dựng, bản dài và highlight của một tập dùng CÙNG một `<tên>`; các script new_*.sh lấy chỗ lưu từ `ky-nang/san-xuat-video/dung-video-theo-phong-cach/scripts/noi-luu.sh`. Còn `~/Movies/vlog/_cho-xac-nhan/` chờ David nói từng file thuộc vlog nào.
