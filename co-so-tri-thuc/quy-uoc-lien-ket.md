---
description: Bộ quy tắc liên kết của bộ não — mô tả đầu file, đường nối, bản đồ nội dung, chỉ mục tự sinh, ghi chú kiến thức, máy kiểm; để Claude tra nhanh, ít token, không sót.
---

# Quy ước liên kết

David chốt 14/11/2026: bộ não là **mạng lưới file nối với nhau**, không cần app Obsidian (mở thư mục bằng Obsidian chỉ để xem bản đồ cho vui). Liên kết nằm trong chính file nên đi theo GitHub, máy nào clone về cũng dùng được ngay. Kế hoạch và số đo: [du-an/lien-ket-tri-thuc.md](../du-an/lien-ket-tri-thuc.md).

## Claude tra cứu thế nào

1. **Tìm trong chỉ mục trước**: `grep -i "<từ khoá>" co-so-tri-thuc/chi-muc.md` → vài dòng, mỗi dòng một file kèm mô tả → mở thẳng 1–3 file đúng. Không đọc cả chỉ mục, không grep toàn repo trừ khi chỉ mục không ra.
2. **Đi theo chủ đề** khi cần bức tranh rộng: mở trang trong [ban-do/](../ban-do/README.md) rồi đi theo đường nối.
3. **Theo đường nối** trong file đang đọc để lấy phần liên quan, không đoán tên file.

## Năm luật cho mọi file `.md`

1. **Có mô tả đầu file**: khối `description:` một câu nói file này là gì và dùng khi nào (khoá `description` vì Claude Code đọc đúng tên này ở ghi nhớ, skill). Viết bằng từ người ta sẽ tìm. Không thêm mô tả vào file nạp mỗi phiên hay hồ sơ David (danh sách miễn ở máy kiểm); mô tả của chúng ghi trong máy kiểm.
2. **Đường nối dùng link tương đối** `[tên](duong/dan.md)`: mở thẳng được, GitHub và Obsidian đều hiểu. Ghi nhớ trong `bo-nho/` được dùng thêm `[[ten-ghi-nho]]` (định dạng bộ nhớ Claude Code). Tên file trong dấu `` ` `` chỉ là chữ, không tính là nối.
3. **Không file mồ côi**: mọi file có ít nhất một file khác nối tới (chỉ mục không tính). Tối thiểu là trang bản đồ của chủ đề đó; tốt hơn là thêm nối từ file cha (skill → tài liệu của nó, kế hoạch → file con).
4. **Nối hai chiều khi liên quan thật**: luật ↔ ghi nhớ ghi lý do ↔ skill dùng luật ↔ dự án áp dụng. Không nối tràn lan; mỗi nối trả lời được "mở file kia để biết gì".
5. **Đổi tên, gộp, xoá file thì sửa mọi nối trỏ tới nó** trong cùng lần sửa. Máy kiểm báo link gãy và chặn đẩy GitHub.

## Bốn lớp

| Lớp | Ở đâu | Ai giữ |
|---|---|---|
| Chỉ mục | [chi-muc.md](chi-muc.md): mỗi file một dòng (đường dẫn, mô tả, số nối tới) | Máy tự sinh mỗi lần đồng bộ, **không sửa tay** |
| Bản đồ nội dung | [ban-do/](../ban-do/README.md): mỗi chủ đề một trang, nối tới file kèm một câu vì sao | Claude, khi thêm file mới thì thêm dòng vào đúng trang |
| Mô tả đầu file | khối `description:` | Claude, khi tạo hoặc đổi nội dung chính của file |
| Đường nối | trong thân file | Claude |

## Ghi chú kiến thức

Kiến thức đáng giữ từ trao đổi với David (kể cả phần Claude giải thích, công cụ, khái niệm) ghi vào [kien-thuc/](kien-thuc/README.md), **mỗi khái niệm một file nhỏ**, có mô tả, có mục "Liên quan" nối tới ý tưởng / dự án / skill dùng tới nó, và một dòng trong trang bản đồ `kien-thuc`. Đã có file đúng chủ đề thì bổ sung, không tạo file trùng. Ý tưởng chưa chốt vẫn ở [du-an/danh-sach-y-tuong.md](../du-an/danh-sach-y-tuong.md); luật vẫn ở nhà của luật. Khi nào ghi: [ky-nang/chuan-muc-lam-viec.md](../ky-nang/chuan-muc-lam-viec.md) mục 4.

## Sổ tay riêng (chỉ trên máy)

`~/Documents/2-ca-nhan/so-tay/` (danh bạ, việc, nhắc, tài chính, tin nhắn, kho gom) theo cùng quy ước nhưng **không lên GitHub**, sao lưu Drive. Bot Sổ nhớ ghi các sổ, nên không thêm khối mô tả vào file của bot: mô tả nằm ở dòng của file đó trong `so-tay/ban-do.md` (chữ sau " — "); link tới thư mục (sổ theo tháng, theo ngày) tính là nối tới mọi file trong đó. Chỉ mục `so-tay/chi-muc.md` máy sinh. Bộ não không nối link vào sổ tay (máy khác không có), chỉ ghi đường dẫn trong dấu `` ` ``. Tra: `grep -i "<từ khoá>" ~/Documents/2-ca-nhan/so-tay/chi-muc.md`.

## Máy kiểm

- `python3 tu-dong-hoa/lien-ket/kiem-tra-lien-ket.py`: báo link gãy, file mồ côi, file thiếu mô tả; sinh lại `chi-muc.md`. Link gãy thì trả lỗi.
- Chạy tự động trong `tu-dong-hoa/dong-bo.sh` trước khi đẩy GitHub: link gãy trong bộ não thì không đẩy; sổ tay riêng (`--goc ~/Documents/2-ca-nhan/so-tay`) chỉ kiểm và sinh chỉ mục, không chặn.
- `python3 tu-dong-hoa/lien-ket/do-truy-xuat.py`: đo 10 câu hỏi thử (`cau-hoi-thu.json`), so cách tìm toàn văn với tìm qua chỉ mục. Chạy lại khi kho lớn thêm nhiều để biết lúc nào cần tìm theo nghĩa.
