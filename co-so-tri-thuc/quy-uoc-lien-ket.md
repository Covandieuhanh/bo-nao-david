---
description: Bộ quy tắc liên kết của bộ não — mô tả đầu file, liên kết giữa các file, bản đồ nội dung, chỉ mục tự sinh, ghi chú kiến thức, công cụ kiểm tra; để Claude tra cứu nhanh, tốn ít token, không bỏ sót.
---

# Quy ước liên kết

David chốt 14/11/2026: bộ não là **mạng lưới file liên kết với nhau**, không cần app Obsidian (mở thư mục bằng Obsidian chỉ để xem bản đồ tham khảo). Liên kết nằm trong chính file nên được đồng bộ theo GitHub, thiết bị nào clone về cũng dùng được ngay. Kế hoạch và chỉ số đo: [du-an/lien-ket-tri-thuc.md](../du-an/lien-ket-tri-thuc.md).

## Claude tra cứu thế nào

1. **Tìm trong chỉ mục trước**: `grep -i "<từ khoá>" co-so-tri-thuc/chi-muc.md` → vài dòng, mỗi dòng một file kèm mô tả → mở trực tiếp 1–3 file đúng. Không đọc cả chỉ mục, không grep toàn repo trừ khi chỉ mục không cho kết quả.
2. **Tra theo chủ đề** khi cần bức tranh rộng: mở trang trong [ban-do/](../ban-do/README.md) rồi đi theo các liên kết.
3. **Theo liên kết** trong file đang đọc để lấy phần liên quan, không đoán tên file.

## Năm luật cho mọi file `.md`

1. **Có mô tả đầu file**: khối `description:` một câu nói file này là gì và dùng khi nào (khoá `description` vì Claude Code đọc đúng tên này ở ghi nhớ, skill). Mô tả viết bằng từ khoá người dùng sẽ tìm. Không thêm mô tả vào file nạp mỗi phiên hay hồ sơ David (danh sách miễn ở công cụ kiểm tra); mô tả của các file đó ghi trong công cụ kiểm tra.
2. **Liên kết dùng đường dẫn tương đối** `[tên](duong/dan.md)`: mở trực tiếp được, GitHub và Obsidian đều hiểu. Ghi nhớ trong `bo-nho/` được dùng thêm `[[ten-ghi-nho]]` (định dạng bộ nhớ Claude Code). Tên file trong dấu `` ` `` chỉ là chữ, không tính là liên kết.
3. **Không có file mồ côi**: mọi file có ít nhất một file khác liên kết tới (chỉ mục không tính). Tối thiểu là trang bản đồ của chủ đề đó; tốt hơn là thêm liên kết từ file cha (skill tới tài liệu của skill, kế hoạch tới file con).
4. **Liên kết hai chiều khi thực sự liên quan**: luật ↔ ghi nhớ ghi lý do ↔ skill dùng luật ↔ dự án áp dụng. Không liên kết tràn lan; mỗi liên kết trả lời được "mở file kia để biết gì".
5. **Đổi tên, gộp, xoá file thì sửa mọi liên kết trỏ tới file đó** trong cùng lần sửa. Công cụ kiểm tra báo liên kết gãy và chặn push lên GitHub.

## Bốn lớp

| Lớp | Ở đâu | Ai giữ |
|---|---|---|
| Chỉ mục | [chi-muc.md](chi-muc.md): mỗi file một dòng (đường dẫn, mô tả, số liên kết tới) | Công cụ tự sinh mỗi lần đồng bộ, **không sửa thủ công** |
| Bản đồ nội dung | [ban-do/](../ban-do/README.md): mỗi chủ đề một trang, liên kết tới file kèm một câu giải thích lý do | Claude, khi thêm file mới thì thêm dòng vào đúng trang |
| Mô tả đầu file | khối `description:` | Claude, khi tạo hoặc đổi nội dung chính của file |
| Liên kết | trong thân file | Claude |

## Ghi chú kiến thức

Kiến thức đáng giữ từ trao đổi với David (kể cả phần Claude giải thích, công cụ, khái niệm) ghi vào [kien-thuc/](kien-thuc/README.md), **mỗi khái niệm một file nhỏ**, có mô tả, có mục "Liên quan" liên kết tới ý tưởng / dự án / skill dùng tới khái niệm đó, và một dòng trong trang bản đồ `kien-thuc`. Đã có file đúng chủ đề thì bổ sung, không tạo file trùng. Ý tưởng chưa chốt vẫn ở [du-an/danh-sach-y-tuong.md](../du-an/danh-sach-y-tuong.md); luật vẫn ở nguồn của luật. Khi nào ghi: [ky-nang/chuan-muc-lam-viec.md](../ky-nang/chuan-muc-lam-viec.md) mục 4.

## Sổ tay riêng (chỉ trên máy)

`~/Documents/2-ca-nhan/so-tay/` (danh bạ, việc, nhắc, tài chính, tin nhắn, kho gom) theo cùng quy ước nhưng **không đưa lên GitHub**, sao lưu lên Drive. Bot Sổ nhớ ghi các sổ, nên không thêm khối mô tả vào file của bot: mô tả nằm ở dòng của file đó trong `so-tay/ban-do.md` (chữ sau " — "); liên kết tới thư mục (sổ theo tháng, theo ngày) được tính là liên kết tới mọi file trong đó. Chỉ mục `so-tay/chi-muc.md` do công cụ tự sinh. Bộ não không liên kết vào sổ tay (thiết bị khác không có), chỉ ghi đường dẫn trong dấu `` ` ``. Tra: `grep -i "<từ khoá>" ~/Documents/2-ca-nhan/so-tay/chi-muc.md`.

## Công cụ kiểm tra

- `python3 tu-dong-hoa/lien-ket/kiem-tra-lien-ket.py`: báo liên kết gãy, file mồ côi, file thiếu mô tả; sinh lại `chi-muc.md`. Có liên kết gãy thì công cụ trả lỗi.
- Chạy tự động trong `tu-dong-hoa/dong-bo.sh` trước khi push lên GitHub: có liên kết gãy trong bộ não thì không push; sổ tay riêng (`--goc ~/Documents/2-ca-nhan/so-tay`) chỉ kiểm và sinh chỉ mục, không chặn.
- `python3 tu-dong-hoa/lien-ket/do-truy-xuat.py`: đo 10 câu hỏi thử (`cau-hoi-thu.json`), so sánh cách tìm toàn văn với cách tìm qua chỉ mục. Chạy lại khi kho tăng thêm nhiều để biết lúc nào cần tìm theo nghĩa.
