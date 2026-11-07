---
name: github-chi-giu-nao
description: "GitHub David.Claude là bản gốc của bộ não — có gì mới cho skill/não thì ĐẨY NGAY (bắt buộc); chỉ giữ mẫu, form, luật, hồ sơ; sản phẩm ở lại máy/tài khoản làm ra nó"
metadata:
  node_type: memory
  type: feedback
  originSessionId: a3db5b56-cfbd-4990-a23d-3d0562a49e99
  modified: 2026-11-07T15:40:01.698Z
---

David chốt 07/11/2026: GitHub là bộ não để dùng với bất kỳ tài khoản Claude hay AI nào, làm ra cùng một chuẩn.

**Luật bắt buộc (07/11/2026, tối):** có gì mới cho skill hoặc bộ não (luật, quyết định, ghi nhớ, hồ sơ, việc dở, mẫu, form, khuôn, script) thì đẩy lên GitHub ngay khi xong thay đổi đó (`bash scripts/sync.sh --push`), không chờ David nói "cập nhật não". Lưới an toàn: hook `SessionEnd` trong `~/.claude/settings.json` tự chạy sync khi phiên kết thúc (do `install.sh` cài). Repo phải xếp gọn, phần nào ra phần đó, tìm bằng tay được ngay.

Chỉ đưa lên: hồ sơ, luật, bộ nhớ, skill, việc đang dở (TRANG-THAI, sổ danh mục, kho 100 video, rà soát), và **mẫu/form** (đặt trong skill, ví dụ `skills/dung-video/mau-chuan/`, `khoi/19-dang-bai/mau-ke-hoach-dang.md`). Không đưa: dự án video, bài đăng, kịch bản từng dự án, tài liệu đã làm xong, dữ liệu khách, hồ sơ cá nhân (ví dụ `~/Documents/2-ca-nhan/`). Lịch sử git cũ giữ nguyên.

**Why:** máy nào gắn với thư mục máy đó; GitHub là nơi duy nhất mọi tài khoản cùng đọc, nên não phải luôn mới nhất ở đó.
**How to apply:** sửa skill/não xong là sync --push trong cùng lượt. Muốn đưa gì lên repo thì hỏi "đây là não/mẫu hay sản phẩm?". Sản phẩm để `~/Movies` và Drive; trong TRANG-THAI chỉ ghi đường dẫn trên máy. Sửa hồ sơ thì sửa `~/.claude/David.md` (sync chép từ đó đè lên `nao/David.md`). Liên quan [[david-claude-brain-repo]], [[dat-ten-khong-dau]].
