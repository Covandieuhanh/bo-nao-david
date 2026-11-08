---
name: nao-github-ban-goc
description: "GitHub David.Claude là bản gốc của bộ não — có gì mới cho skill/não thì ĐẨY NGAY (bắt buộc); chỉ giữ mẫu, form, luật, hồ sơ; sản phẩm ở lại máy/tài khoản làm ra nó"
metadata:
  node_type: memory
  type: feedback
  originSessionId: a3db5b56-cfbd-4990-a23d-3d0562a49e99
  modified: 2026-11-07T15:40:01.698Z
---

David chốt 07/11/2026: GitHub là bộ não để dùng với bất kỳ tài khoản Claude hay AI nào, làm ra cùng một chuẩn.

**Luật bắt buộc (07/11/2026, tối):** có gì mới cho skill hoặc bộ não (luật, quyết định, ghi nhớ, hồ sơ, việc dở, mẫu, form, khuôn, script) thì đẩy lên GitHub ngay khi xong thay đổi đó (`bash scripts/sync.sh --push`), không chờ David nói "cập nhật não". **Đồng bộ 2 chiều (07/11/2026):** trên Mac chính, `~/.claude/David.md`, `CLAUDE.md`, các skill, thư mục bộ nhớ và `~/Movies/_so-danh-muc/danh-muc.md` là lối tắt trỏ vào repo, nên máy và repo là một bản. Hook trong `~/.claude/settings.json` (do `install.sh` cài): `SessionStart` kéo từ GitHub về (`sync.sh --keo`), `SessionEnd` đẩy lên. Mac và GitHub phải luôn giống nhau. Repo phải xếp gọn, phần nào ra phần đó, tìm bằng tay được ngay.

**Bộ não = đủ mọi dữ liệu dùng chung** (David nói rõ 07/11/2026, tối): ai, máy nào, tài khoản Claude hay AI code nào dùng bộ não cũng phải có đủ dữ liệu. Gồm: hồ sơ, luật, bộ nhớ, skill, **tài liệu tham chiếu** (`tham-chieu/`, ví dụ hồ sơ CCL làm hình mẫu chuẩn), nghiên cứu, việc đang dở (TRANG-THAI, sổ danh mục, kho 100 video, rà soát), và **mẫu/form** (đặt trong skill, ví dụ `skills/dung-video/mau-chuan/`, `khoi/19-dang-bai/mau-ke-hoach-dang.md`). Chỉ **sản phẩm** làm ra từ bộ não (dự án video, bài viết, bài đăng, kịch bản từng dự án) mới ở lại máy và tài khoản làm ra nó; cộng dữ liệu khách và giấy tờ cá nhân (`~/Documents/2-ca-nhan/`). Lịch sử git cũ giữ nguyên.

**Why:** máy nào gắn với thư mục máy đó; GitHub là nơi duy nhất mọi tài khoản cùng đọc, nên não phải luôn mới nhất ở đó.
**How to apply:** sửa skill/não xong là sync --push trong cùng lượt. Muốn đưa gì lên repo thì hỏi "đây là dữ liệu dùng chung hay sản phẩm?"; dùng chung thì đưa lên. Sản phẩm để `~/Movies` và Drive; trong TRANG-THAI chỉ ghi đường dẫn trên máy. Sửa hồ sơ ở đâu cũng được: `~/.claude/David.md` và `nao/David.md` là cùng một file. Liên quan [[nao-dat-ten-khong-dau]].

**Repo và lệnh (gộp từ ghi nhớ `nao-repo-david-claude`, 08/11/2026):** https://github.com/Covandieuhanh/David.Claude (Private), bản trên máy `~/Documents/David.Claude`, lập 05/11/2026. David nói **"cập nhật não"** → sửa `TRANG-THAI-HIEN-TAI.md` nếu trạng thái đổi, rồi `bash scripts/sync.sh --push` (quét bí mật, commit, kéo về rồi đẩy lên). Hồ sơ thấu hiểu `nao/ho-so-thau-hieu.md` là bản bỏ số nợ và khoản chi; bản có số chỉ ở Drive `Sao-luu-Claude-2026-11-07/`. Đổi tài khoản Claude: `SETUP.md` mục 1. **Không đưa lên:** lịch sử chat thô, cookie, `.claude.json`, `~/Documents/mk.csv`, video.
