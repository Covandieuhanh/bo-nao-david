---
name: co-so-tri-thuc-github-ban-goc
description: "GitHub bo-nao-david là bản gốc của bộ não — có gì mới cho skill/não thì ĐẨY NGAY (bắt buộc); chỉ giữ mẫu, form, luật, hồ sơ; sản phẩm ở lại máy/tài khoản làm ra nó"
metadata:
  node_type: memory
  type: feedback
  originSessionId: a3db5b56-cfbd-4990-a23d-3d0562a49e99
  modified: 2026-11-07T15:40:01.698Z
---

David chốt 07/11/2026: GitHub là bộ não để dùng với bất kỳ tài khoản Claude hay AI nào, làm ra cùng một chuẩn.

**Luật bắt buộc (07/11/2026, tối):** có gì mới cho skill hoặc bộ não (luật, quyết định, ghi nhớ, hồ sơ, việc dở, mẫu, form, khuôn, script) thì đẩy lên GitHub ngay khi xong thay đổi đó (`bash tu-dong-hoa/dong-bo.sh --push`), không chờ David nói "cập nhật não". **Đồng bộ 2 chiều (07/11/2026):** trên Mac chính, `~/.claude/david.md`, `CLAUDE.md`, các skill, thư mục bộ nhớ và `~/Movies/_danh-muc-noi-dung/danh-muc-noi-dung.md` là lối tắt trỏ vào repo, nên máy và repo là một bản. Hook trong `~/.claude/settings.json` (do `cai-dat-bo-nao.sh` cài): `SessionStart` kéo từ GitHub về (`dong-bo.sh --keo`), `SessionEnd` đẩy lên. Mac và GitHub phải luôn giống nhau. Repo phải xếp gọn, phần nào ra phần đó, tìm bằng tay được ngay.

**Bộ não = đủ mọi dữ liệu dùng chung** (David nói rõ 07/11/2026, tối): ai, máy nào, tài khoản Claude hay AI code nào dùng bộ não cũng phải có đủ dữ liệu. Gồm: hồ sơ, luật, bộ nhớ, skill, **tài liệu tham chiếu** (`tai-lieu-tham-khao/`, ví dụ hồ sơ CCL làm hình mẫu chuẩn), nghiên cứu, việc đang dở (bao-cao-trang-thai, sổ danh mục, kho 100 video, rà soát), và **mẫu/form** (đặt trong skill, ví dụ `ky-nang/san-xuat-video/mau-chuan/`, `ky-nang/san-xuat-video/mo-dun/19-dang-bai/mau-ke-hoach-dang.md`). Chỉ **sản phẩm** làm ra từ bộ não (dự án video, bài viết, bài đăng, kịch bản từng dự án) mới ở lại máy và tài khoản làm ra nó; cộng dữ liệu khách và giấy tờ cá nhân (`~/Documents/2-ca-nhan/`). Lịch sử git cũ giữ nguyên.

**Why:** máy nào gắn với thư mục máy đó; GitHub là nơi duy nhất mọi tài khoản cùng đọc, nên não phải luôn mới nhất ở đó.
**How to apply:** sửa skill/não xong là sync --push trong cùng lượt. Muốn đưa gì lên repo thì hỏi "đây là dữ liệu dùng chung hay sản phẩm?"; dùng chung thì đưa lên. Sản phẩm để `~/Movies` và Drive; trong bao-cao-trang-thai chỉ ghi đường dẫn trên máy. Sửa hồ sơ ở đâu cũng được: `~/.claude/david.md` và `co-so-tri-thuc/david.md` là cùng một file. Liên quan [[co-so-tri-thuc-quy-uoc-dat-ten]].

**Repo và lệnh (gộp từ ghi nhớ `co-so-tri-thuc-repo-david-claude`, 08/11/2026):** https://github.com/Covandieuhanh/bo-nao-david (**công khai**: David chốt 20/11/2026 "cứ để công khai đi vì cũng không có mật khẩu hay token nào trên đó"; quét lại cả lịch sử git không thấy bí mật), bản trên máy `~/Documents/bo-nao-david`, lập 05/11/2026. David nói **"cập nhật não"** → sửa `bao-cao-trang-thai.md` nếu trạng thái đổi, rồi `bash tu-dong-hoa/dong-bo.sh --push` (quét bí mật, commit, kéo về rồi đẩy lên). Hồ sơ thấu hiểu `co-so-tri-thuc/ho-so-ca-nhan.md` là bản bỏ số nợ và khoản chi; bản có số chỉ ở Drive `sao-luu-claude-2026-11-07/`. Đổi tài khoản Claude: `huong-dan-cai-dat.md` mục 1. **Không đưa lên:** lịch sử chat thô, cookie, `.claude.json`, `~/Documents/mk.csv`, video.

Nhà của luật: `AGENTS.md` luật 6 và `huong-dan-cai-dat.md`. Ghi nhớ này giữ ngày, lời David, lý do.

**Hai repo (David 20/11/2026: "trên github chỉ còn những cái có thể dùng chung thôi chứ những cái riêng như là bot telegram ở máy này thì không cần đưa lên github nữa để tránh loạn"; chọn "Repo riêng tư mới"):** phần chỉ Mac chính (`tu-dong-hoa/phan-rieng-mac.txt`) lên repo riêng tư https://github.com/Covandieuhanh/bo-nao-david-mac, cùng thư mục `~/Documents/bo-nao-david` (git dir `.git-mac`), đường dẫn giữ nguyên nên bot, lịch không cài lại. `dong-bo.sh` đẩy cả hai; máy khác chỉ có repo công khai. Phần riêng cũ vẫn còn trong lịch sử repo công khai (không có bí mật nên không viết lại lịch sử). Liên quan [[co-so-tri-thuc-nhieu-may]].
