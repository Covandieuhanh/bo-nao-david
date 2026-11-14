---
description: "Dự án liên kết tri thức (14/11): biến bộ não thành mạng lưới file nối nhau để Claude tra nhanh, ít token; mục tiêu, thiết kế, việc đã làm, số đo trước / sau, việc còn lại."
---

# Liên kết tri thức: bộ nhớ có liên kết cho Claude

> Lập 14/11/2026 theo lời David: "tôi sẽ trao đổi rất nhiều và dần dần sẽ cần lưu trữ và truy xuất lượng lớn thông tin. Tôi chỉ làm việc trực tiếp với Claude." Ban đầu tên "kế hoạch Obsidian"; David chốt cùng ngày: "triển khai bộ quy tắc và liên kết file đi, vậy thì không cần obsidian nữa".
> Trạng thái: **đã triển khai 14/11/2026**. Luật đang áp dụng: [co-so-tri-thuc/quy-uoc-lien-ket.md](../co-so-tri-thuc/quy-uoc-lien-ket.md). Ghi chú kiến thức về lý do: [lien-ket-tri-thuc](../co-so-tri-thuc/kien-thuc/lien-ket-tri-thuc.md).

## 1. Mục tiêu

| # | Mục tiêu | Đo bằng | Kết quả 14/11 |
|---|---|---|---|
| 1 | Tra nhanh, ít token, ít sót | 10 câu hỏi thử (`tu-dong-hoa/lien-ket/do-truy-xuat.py`) | Đọc ít hơn **48%** byte (261 KB → 138 KB), trúng **9/10** so với 7/10 |
| 2 | Không file rời rạc | Máy kiểm: mồ côi, link gãy | 239 file · gãy 0 · mồ côi 0 · thiếu mô tả 0 (lúc đầu: 21 link gãy, 66 mồ côi, 147 thiếu mô tả) |
| 3 | Giữ cả phần Claude giải thích | Ghi chú `co-so-tri-thuc/kien-thuc/` | 3 ghi chú đầu: Telegram bot, Mini App, liên kết tri thức |
| 4 | Dựng lại 100% từ GitHub | Liên kết nằm trong file, máy kiểm trong repo | Đạt: không cần app nào |
| 5 | David không phải làm gì thêm | — | Đạt: không cần mở Obsidian |

## 2. Thiết kế

- **Vault = chính thư mục bộ não**, không dời file. Không dùng app Obsidian (mở thư mục bằng Obsidian chỉ để xem cho vui).
- **Bốn lớp**: mô tả đầu file (`description:`) · chỉ mục tự sinh [chi-muc.md](../co-so-tri-thuc/chi-muc.md) · bản đồ nội dung [ban-do/](../ban-do/README.md) (6 trang) · đường nối link tương đối.
- **Máy kiểm** `tu-dong-hoa/lien-ket/kiem-tra-lien-ket.py`: link gãy (chặn đẩy GitHub), mồ côi, thiếu mô tả; sinh lại chỉ mục. Chạy trong `tu-dong-hoa/dong-bo.sh`.
- **File miễn mô tả** (mô tả ghi trong máy kiểm): file nạp mỗi phiên (AGENTS.md, CLAUDE.md, chi-dan-toan-cuc.md), hồ sơ David (david.md, ho-so-ca-nhan.md, không sửa khi chưa hỏi), MEMORY.md, README.md (trang GitHub), quy-tac-bot.md (bị chép thành lời nhắc của bot).
- **Luồng giữ mới**: `ky-nang/chuan-muc-lam-viec.md` mục 4 (file mới có mô tả + dòng bản đồ; kiến thức đáng giữ → `kien-thuc/`); AGENTS.md chỉ cách tra (grep chỉ mục trước).

## 3. Việc đã làm (14/11)

- [x] Đo trước: 10 câu hỏi thử `tu-dong-hoa/lien-ket/cau-hoi-thu.json`
- [x] Thuật ngữ mới vào `bang-thuat-ngu.md` (Bản đồ nội dung `ban-do`, Chỉ mục `chi-muc`, Ghi chú kiến thức `kien-thuc`, Quy ước liên kết, Kiểm tra liên kết, Đo truy xuất, Câu hỏi thử; khoá `description`)
- [x] Luật `co-so-tri-thuc/quy-uoc-lien-ket.md`
- [x] Máy kiểm + chỉ mục tự sinh, gắn vào `dong-bo.sh`
- [x] Sửa 21 link `[[...]]` gãy trong ghi nhớ (tên cũ trước chuẩn hoá tên 14/11)
- [x] Mô tả một câu cho 145 file
- [x] 6 trang bản đồ: gốc, hồ sơ và chiến lược, sản phẩm và đào tạo, sản xuất video, bộ não và tự động hoá, kiến thức
- [x] 3 ghi chú kiến thức đầu tiên
- [x] Luật cuối việc + AGENTS.md cách tra + ghi nhớ `co-so-tri-thuc-lien-ket-tri-thuc`
- [x] Đo sau

## 4. Còn lại

- [ ] **David chốt**: sổ tay riêng `~/Documents/2-ca-nhan/so-tay/` (danh bạ, tin nhắn, kho dữ liệu) có nối theo cùng quy ước không, chỉ trên máy, không lên GitHub. Đề xuất: có, vì phần này sẽ lớn nhanh nhất.
- [ ] Câu 4 (luật bot Sổ nhớ) vẫn trượt vì nhiều file cùng nói về bot: theo dõi, không chỉnh mô tả để "ăn" bài đo.
- [ ] Đo lại khi kho lớn thêm nhiều; khoảng 1.000 ghi chú hoặc trúng dưới 8/10 thì cân nhắc tìm theo nghĩa (script chỉ mục theo nghĩa chạy thẳng trên file).
