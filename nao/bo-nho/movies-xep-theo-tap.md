---
name: movies-xep-theo-tap
description: "~/Movies của David xếp theo tập (gốc → bản dài → highlight chung một thư mục), skill dựng video đã sửa theo"
metadata:
  node_type: memory
  type: project
  originSessionId: f5d8cbca-e68e-4851-9ff5-2b8071eab6ce
  modified: 2026-11-07T03:11:43.928Z
---

Ngày 07/11/2026 David chốt: video và tài liệu cùng nội dung phải nằm gần nhau. ~/Movies xếp theo tập:
`tap-<tên>/1-goc`, `2-ban-dai`, `3-highlight/` (kế hoạch cắt) + `3-highlight/clip-<id>/`, `9-luu-cu`; vlog ở `~/Movies/vlog/<tên>/`; video tự quay cũ ở `video-tu-quay/`.
Sổ chuyển file: `~/Movies/_so-danh-muc/so-chuyen-file-2026-11-07.tsv`.

**Why:** trước đó gốc, bản dài, clip highlight của cùng một tập nằm ở 4–5 thư mục, David không tìm được.
**How to apply:** khi dựng, bản dài và highlight của một tập dùng CÙNG một `<tên>`; các script new_*.sh lấy chỗ lưu từ `~/.claude/skills/dung-video/video-style-edit/scripts/noi_luu.sh`. Còn `~/Movies/vlog/_cho-xac-nhan/` chờ David nói từng file thuộc vlog nào.
