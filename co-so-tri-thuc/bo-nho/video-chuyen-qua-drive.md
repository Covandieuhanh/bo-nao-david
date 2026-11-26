---
name: video-chuyen-qua-drive
description: "~/Movies sắp xếp theo tập; Drive covandieuhanh chỉ lưu bộ não, video gốc và thành quả video; Mac chỉ lưu việc đang làm (07/11, 08/11, 11/11; gộp 15/11)"
metadata:
  node_type: memory
  type: reference
  originSessionId: 8485f85b-5487-4ff8-8491-137cb6e9e7d2
  modified: 2026-11-11T11:00:00.000Z
---

**Drive chỉ lưu dữ liệu công việc của David:** bộ não (luật, ghi nhớ, skill, tài liệu làm việc với Claude), video gốc của từng video đang làm, thành quả
video (bản cuối dù đạt hay chưa đạt, kịch bản, phụ đề, bài đăng). File tải về, dữ liệu ứng dụng và dữ liệu cá nhân không đồng bộ lên Drive.
**Mac chỉ lưu việc đang làm và bản cuối chưa đăng** (20/11/2026, David: "những kết quả cuối cùng mà tôi chưa đăng thì vẫn cần phải có trong mac để có khi đăng"; "tôi chỉ quan tâm đến các kết quả cuối thôi"): bản cuối nằm ở `~/Movies/cho-dang/<tập>/`; sau khi đăng xong, chạy `cho-dang.sh xong` thì bản cuối mới được xoá; trang kiểm tra `localhost:8765/mac`. Từ 26/11/2026 (David): làm ra kết quả là lên Drive ngay; sửa thì tải bản mới nhất lên, xoá bản cũ; David chốt bản cuối thì xoá bản gốc theo quy trình (`ky-nang/san-xuat-video/quy-tac-chung.md` mục 8), vì đủ kết quả ba hướng, nhật ký và ý tưởng thì không cần bản gốc nữa.
**Việc đang làm:** khi bắt đầu một video, Claude chép tệp gốc lên `tu-lieu-goc/<tập>/` (nếu David gửi qua chat hoặc Downloads); khi xong tập, Claude chạy `don-tap.py --xoa` rồi `luu-drive.sh` để tải dự án (bỏ file tạm, bỏ tệp gốc đã có) lên
`sao-luu-mac/video/<tập>/`, kiểm tra dữ liệu đã lên đám mây, xoá trên Mac và ghi loại vào [kho-drive.md](../../du-an/kho-drive.md).
**Xoá:** với dữ liệu công việc của David, Claude chép lên Drive và kiểm tra dữ liệu đã lên đám mây trước; với dữ liệu khác (ứng dụng, dữ liệu ứng dụng, file tải về, dữ liệu cá nhân), Claude liệt kê
và hỏi David trước khi xoá vĩnh viễn; Claude chỉ xoá trực tiếp bộ nhớ đệm và file tạm có thể tạo lại được.
Sổ 11/11/2026: (1) David: "máy mac này chỉ còn đóng mỗi vai trò là khi đang thực thi cái gì thì có dữ liệu và tài nguyên của cái đó thôi";
lý do là Mac 228 GB đã đầy, còn Drive có 400 GB. (2) Dữ liệu Codex đã bị xoá trực tiếp theo lời "codex xoá hết"; sau đó David cần lại dữ liệu đó nhưng không khôi phục được.
(3) David: "không cần đồng bộ tất cả… chỉ khi nào liên quan đến bộ não… và khi làm video thì mới tải video gốc lên… và các thứ liên quan
đến thành quả của video thôi", vì việc đồng bộ mọi file tải về tốn thời gian.

David điều khiển Mac từ điện thoại bằng Remote Control; David không dùng iCloud Drive.
**Drive dùng chung là tài khoản `covandieuhanh@gmail.com`** (David chốt 08/11/2026); Drive `trainer.davidtran@gmail.com` không còn được dùng.
Video gốc David gửi lên: `~/Library/CloudStorage/GoogleDrive-covandieuhanh@gmail.com/Drive của tôi/tu-lieu-goc/`
Thành phẩm trả về: `.../Drive của tôi/thanh-pham/`, **mỗi tập một thư mục, trùng tên với `~/Movies`** (David chốt 08/11/2026): `tap-<ten>/ban-dai/<ten>.mp4` và `tap-<ten>/highlight/clip-a.mp4`, `clip-b.mp4`…; tập chỉ có bản dài vẫn tạo thư mục `ban-dai/`. Vlog lưu vào `vlog/<ten>.mp4`, video tự quay lưu vào `video-tu-quay/<ten>.mp4`. Claude có thể gửi clip ngắn trực tiếp vào chat bằng SendUserFile.
Kho dự án và bộ não: `.../Drive của tôi/sao-luu-mac/` (Movies, Downloads, Documents, bo-nao). Bản sao lưu đợt chuyển tài khoản: `.../Drive của tôi/sao-luu-claude-2026-11-07/` gồm `tai-lieu-claude-ai` và `du-an-video` (âm thanh gốc, kịch bản; không gồm file render).
Liên quan (mục gộp bên dưới), [[co-so-tri-thuc-github-ban-goc]].

Nguồn của luật: `ky-nang/chuan-muc-lam-viec.md` mục 4 ("Giữ dung lượng Mac thấp") và [kho-drive.md](../../du-an/kho-drive.md). Ghi nhớ này lưu ngày, lời David và lý do.

## Gộp từ `video-chuyen-qua-drive` (15/11/2026, vòng tự học hằng tuần: giảm số ghi nhớ xuống 40)

Ngày 07/11/2026 David chốt: video và tài liệu cùng nội dung phải nằm gần nhau. ~/Movies được sắp xếp theo tập:
`tap-<tên>/1-goc`, `2-ban-day-du`, `3-doan-noi-bat/` (kế hoạch cắt) và `3-doan-noi-bat/clip-<id>/`, `9-luu-cu`; vlog nằm ở `~/Movies/vlog/<tên>/`; video tự quay cũ nằm ở `video-tu-quay/`.
Sổ ghi việc chuyển file: `~/Movies/_danh-muc-noi-dung/so-chuyen-file-2026-11-07.tsv`.

**Why:** trước đó tệp gốc, bản dài và clip highlight của cùng một tập nằm ở 4–5 thư mục khác nhau, nên David không tìm được.
**How to apply:** khi dựng, bản dài và highlight của một tập dùng CÙNG một `<tên>`; các script new_*.sh lấy vị trí lưu từ `ky-nang/san-xuat-video/dung-video-theo-phong-cach/scripts/noi-luu.sh`. Thư mục `~/Movies/vlog/_cho-xac-nhan/` còn chờ David xác nhận từng file thuộc vlog nào.

Gốc: khối 1 (Bóc tách) của tu-duy-goc.md — mỗi loại dữ liệu có đúng một nơi giữ: GitHub giữ bộ não, Drive giữ bản gốc và thành phẩm, thiết bị chỉ giữ việc đang làm và bản cuối chưa đăng.
