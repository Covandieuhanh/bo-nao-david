---
name: video-chuyen-qua-drive
description: Drive covandieuhanh chỉ giữ bộ não, video gốc và thành quả video (tu-lieu-goc / thanh-pham / sao-luu-mac); Mac chỉ giữ việc đang làm; đồ khác không đồng bộ (2026-11-08, 11/11)
metadata:
  node_type: memory
  type: reference
  originSessionId: 8485f85b-5487-4ff8-8491-137cb6e9e7d2
  modified: 2026-11-11T11:00:00.000Z
---

**Drive chỉ giữ việc của David:** bộ não (luật, ghi nhớ, skill, làm việc với Claude), video gốc của từng video đang làm, thành quả
video (bản cuối đạt hay không, kịch bản, phụ đề, bài đăng). File tải về, dữ liệu app, đồ cá nhân không đồng bộ lên Drive.
**Mac chỉ giữ việc đang làm:** bắt đầu một video thì chép gốc lên `tu-lieu-goc/<tập>/` (nếu David gửi qua chat/Downloads); xong tập thì `don-tap.py --xoa` → `luu-drive.sh` tải dự án (bỏ file tạm, bỏ gốc đã có) lên
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
Liên quan [[video-thu-muc-xep-theo-tap]], [[co-so-tri-thuc-github-ban-goc]].
