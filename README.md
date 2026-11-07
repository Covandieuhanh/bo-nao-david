# David.Claude — bộ não dùng chung của David Trần

Repo riêng tư. AI nào, tài khoản nào đọc xong cũng nhận đúng vai, đúng cách làm việc với David và biết việc đang dở.

**GitHub là bản gốc của bộ não.** Có gì mới cho skill hoặc não thì đẩy lên ngay. Repo chỉ giữ não, mẫu và form; sản phẩm (video, bài đăng, tài liệu đã xong) ở lại máy và tài khoản làm ra nó.

**AI đọc [AGENTS.md](AGENTS.md) trước.** Cài trên máy mới: xem [SETUP.md](SETUP.md).

## Câu mở đầu dán cho AI mới

> Đọc file AGENTS.md trong repo Covandieuhanh/David.Claude rồi đọc tiếp theo đúng thứ tự trong đó. Xong thì tóm tắt 3 dòng: tôi là ai, bạn sẽ làm việc với tôi thế nào, việc đang dở là gì.

## Muốn tìm… → mở…

| Muốn tìm | Mở |
|---|---|
| David là ai, định hướng nghề, lằn ranh | [nao/David.md](nao/David.md) |
| Tính cách, điểm mạnh, động cơ | [nao/ho-so-thau-hieu.md](nao/ho-so-thau-hieu.md) |
| Luật chung cho mọi phiên Claude | [nao/CLAUDE-toan-cuc.md](nao/CLAUDE-toan-cuc.md) |
| Các quyết định, bài học đã chốt | [nao/bo-nho/MEMORY.md](nao/bo-nho/MEMORY.md) (chia nhóm: luật, não, video) |
| Đang làm dở gì, câu hỏi còn mở | [TRANG-THAI-HIEN-TAI.md](TRANG-THAI-HIEN-TAI.md) |
| Trạng thái từng video, tài nguyên | [dang-lam/danh-muc.md](dang-lam/danh-muc.md) |
| Hỏi trước khi làm | [skills/hoi-chuyen-gia/SKILL.md](skills/hoi-chuyen-gia/SKILL.md) |
| Toàn bộ hệ dựng video | [skills/dung-video/GIOI-THIEU.md](skills/dung-video/GIOI-THIEU.md), [luat-chung.md](skills/dung-video/luat-chung.md) |
| Lọc nội dung có đáng làm không | [skills/dung-video/khoi/00-loc-noi-dung/](skills/dung-video/khoi/00-loc-noi-dung/) |
| Giọng văn David | [skills/dung-video/ho-so/giong-van-david.md](skills/dung-video/ho-so/giong-van-david.md) |
| Thông số từng loại video (hồ sơ tham số) | [skills/dung-video/ho-so/](skills/dung-video/ho-so/) |
| Video mẫu chuẩn đã chốt | [skills/dung-video/mau-chuan/](skills/dung-video/mau-chuan/) |
| Form kế hoạch đăng bài | [skills/dung-video/khoi/19-dang-bai/](skills/dung-video/khoi/19-dang-bai/) |
| Form ghi số liệu sau đăng | [skills/dung-video/khoi/16-so-lieu/mau-so-lieu.md](skills/dung-video/khoi/16-so-lieu/mau-so-lieu.md) |
| Nghiên cứu kênh, video mẫu | [nghien-cuu/](nghien-cuu/) |
| Bản cũ đã thay, đã bỏ (không làm theo) | [luu-tru/](luu-tru/) |
| Cài máy mới, đổi tài khoản | [SETUP.md](SETUP.md) |

## Cấu trúc

| Thư mục | Nội dung |
|---|---|
| `AGENTS.md` | Điểm vào cho mọi AI |
| `CLAUDE.md` | Điểm vào cho Claude Code khi mở repo này |
| `TRANG-THAI-HIEN-TAI.md` | Đang làm gì, việc tiếp theo |
| `nao/` | Hồ sơ David, luật toàn cục, bộ nhớ (`bo-nho/`) |
| `skills/` | Toàn bộ skill: dựng video, đăng đa kênh, hỏi chuyên gia, trình duyệt; mẫu và form nằm trong skill |
| `dang-lam/` | Việc đang dở: sổ danh mục, kho 100 video, rà soát video cũ |
| `nghien-cuu/` | Nguyên liệu đã tra cứu, có ngày ở tên file |
| `luu-tru/` | Bản cũ, đã bỏ |
| `scripts/` | Cài vào máy, đồng bộ 2 chiều, hook, quét bí mật |

## Đồng bộ

Trên Mac đã chạy `scripts/install.sh`, các file não trong `~/.claude` là lối tắt vào repo này, nên máy và repo là một bản. Hook tự kéo về đầu phiên, đẩy lên cuối phiên. Đồng bộ tay (nói với Claude Code **"cập nhật não"**, hoặc tự chạy):

```bash
bash scripts/sync.sh
```
