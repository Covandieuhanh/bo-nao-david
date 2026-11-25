---
name: tai-cau-truc
description: Dọn luật — bước 4 của vòng NÂNG CẤP bộ não (hoc-lien-tuc Việc 4). Gom luật hiện hành của cả bộ não (mọi bộ skill + ghi nhớ, một đợt) rồi viết lại bản sạch: mỗi luật một nguồn duy nhất, không ngày, không "thay luật cũ", không câu trùng hay tự mâu thuẫn; lịch sử về sổ quyết định. Có công cụ đo chồng chéo (do-chong-cheo.py): chỉ kêu vì trùng / rối, không vì bộ não dài ra. Dùng khi đang ở bước Dọn của một đợt nâng cấp, khi David nói "gom luật", "luật bị chồng chéo", "viết lại toàn bộ luật", "/tai-cau-truc"; David nói "nâng cấp" hay "tái bản" thì bắt đầu từ hoc-lien-tuc Việc 4.
---

# Dọn luật (bước 4 của Nâng cấp)

**Đọc trước:** `../../co-so-tri-thuc/truc-tri-thuc.md` (mục 2: mỗi ý một nguồn duy nhất ở tầng 1–2) · `../chuan-muc-lam-viec.md` (mục 4 "sửa thẳng, không chồng câu" — dọn là bước định kỳ của luật đó) · vòng nâng cấp:
`../hoc-lien-tuc/SKILL.md` Việc 4 (mốc, thước đo trước / sau, chưng cất, cắt giảm, ra bản nằm ở đó).

**Mục tiêu:** gom các bản trùng, ý trùng viết theo nhiều cách về một nguồn duy nhất, gỡ chỗ rối — không phải làm bộ não ngắn đi. Dù đã học, sửa
bao nhiêu lớp, lúc làm việc AI chỉ đọc **một bản luật hiện hành**, đọc một lần là làm đúng, không phải tự đoán câu nào còn hiệu lực.

## Ba loại file (định nghĩa từng bộ ở `bo.json`)
| Loại | Chứa | Lúc làm việc |
|---|---|---|
| **Bản luật** | chỉ luật đang dùng, viết như mới: không ngày, không "thay luật cũ / bổ sung 09/11", không lời kể lịch sử | đọc |
| **Sổ quyết định** | ngày · lời David nguyên văn · lý do · luật nào bị thay | không đọc (chỉ khi cân nhắc đổi luật, gỡ lỗi) |
| **Kho** | thực đơn để chọn (bố cục, nguồn học, hình mẫu) — không phải luật | chỉ khi cần chọn |

Bộ: `video` (ky-nang/san-xuat-video) · `hoi` (thu-thap-yeu-cau) · `nao` (truc-tri-thuc, AGENTS, CLAUDE, chi-dan-toan-cuc, david.md, chuan-muc-lam-viec). Ghi nhớ `co-so-tri-thuc/bo-nho/`
là sổ, không đo ở đây, nhưng **dọn cùng đợt** bằng skill `consolidate-memory`. Dọn luôn là **cả bộ não một đợt**: học tài nguyên mới thường
kéo theo đổi luật ở nhiều bộ cùng lúc, dọn lẻ một bộ thì bộ khác vẫn giữ lớp cũ.

## Công cụ đo chồng chéo
```bash
python3 -I ky-nang/tai-cau-truc/do-chong-cheo.py [--chi-tiet]
```
- Chỉ kêu vì **trùng hoặc rối**: dấu ngày trong luật (`dau_ngay`), câu ghi đè (`ghi_de`), câu giống hệt ở hai file (`trung`), dòng gần
  trùng ở hai file — cùng ý viết lại theo cách khác (`gan_trung`). Số dòng chỉ in ra để biết độ lớn; số lần sửa (`sua`) chỉ nhắc nhẹ.
- **Một bộ bất kỳ vượt ngưỡng** thì in "NÊN NÂNG CẤP" một dòng thì Claude nhắc David **một dòng**, David quyết (hoc-lien-tuc Việc 4).
- Chạy cuối mỗi việc có sửa bản luật (`chuan-muc-lam-viec.md` mục 4).

## Quy trình dọn (trong một đợt nâng cấp `nang-cap-<n>`)
1. **Chia phiên** (khi việc lớn): một phiên con cho mỗi bộ (video · hoi · nao) và một phiên dọn ghi nhớ, chạy cùng lúc; mỗi phiên ghi
   `du-an/nang-cap-<n>-<bộ>.md`, chỉ sửa file của bộ mình, không commit, không chạy `dong-bo.sh` — phiên điều phối đẩy một lần.
   Bộ vừa sạch (công cụ đo gần 0) vẫn làm bước 2 để tìm luật lệch với bộ khác. Việc nhỏ (vài cặp trùng) làm trong một phiên.
2. **Bảng luật hiện hành** (file của bộ): đọc bản luật + sổ quyết định + ghi nhớ liên quan, mỗi luật một dòng:
   `luật · nguồn nên ở · nguồn hiện tại (file:dòng, có thể nhiều) · ngày chốt gần nhất · trạng thái (sống / trùng / ngược / cũ)`.
   Bắt đầu từ các cặp `gan_trung` của công cụ đo (`--chi-tiet`). Luật ngược nhau: theo `chuan-muc-lam-viec.md` mục 0 (lời David vừa nói >
   ngày chốt gần nhất > cũ); chỗ vẫn không rõ thì gom lại **hỏi David một lần** (thu-thap-yeu-cau), có đề xuất. Không tự bỏ luật nào
   David đã chốt mà không có luật mới hơn thay. Luật xung đột với bộ khác thì ghi mục "Chéo bộ"; phiên điều phối chốt nguồn duy nhất.
3. **Viết lại từ bảng, không vá:**
   - Mỗi luật **một nguồn duy nhất**; nơi khác một dòng trỏ. Luật dùng chung nhiều skill thì đặt ở `chuan-muc-lam-viec.md` / `quy-tac-chung.md`, không chép.
   - Không ngày, không "(David chốt …)", không "thay luật cũ", không "chuyển nguyên văn từ SKILL.md cũ". Lý do một luật tồn tại
     viết ngắn **trong luật** nếu giúp AI làm đúng ("vì người xem không đọc hai chỗ cùng lúc"); lịch sử thì vào sổ.
   - Giữ đúng nghĩa từng luật trong bảng; viết gọn hơn, không thêm luật mới. Nhà mới thiếu chi tiết mà nơi cũ có thì chuyển chi tiết đó
     vào nguồn mới. Code đi kèm (tên khoá, lệnh) giữ khớp. Bảng "Xong khi" của mỗi skill giữ nguyên ý.
   - Ghi nhớ: gộp trùng, bỏ cái đã lỗi thời, cập nhật `MEMORY.md`; ghi nhớ không chứa luật mà bản luật không có.
4. **Đóng sổ:** mỗi sổ quyết định bị đụng thêm một mục đầu `## Nâng cấp <n> — <ngày>: …` (ngày + lời David vừa gỡ khỏi bản luật).
   Sổ quá dài (> 400 dòng) thì chuyển phần cũ vào `luu-tru/` cạnh sổ.
5. **Kiểm dọn:** đủ luật (đi từng dòng bảng — luật "sống" nào cũng có nguồn duy nhất); công cụ đo mọi bộ "Chưa cần", dấu ngày và câu ghi đè gần 0,
   câu trùng 0, dòng gần trùng còn lại chỉ là loại đúng thiết kế (dòng trỏ, "Xong khi" từng skill, bảng công thức, giải thích tham số
   hồ sơ); `kiem-tra-lien-ket.py` không link gãy. Dọn chỉ viết lại chữ, không đổi code dựng: hình khác ở `kiem-mau.py` = có gì sai.
   Thước đo trước / sau còn lại và ra bản: hoc-lien-tuc Việc 4 bước 5.

## Không làm
- Không đổi luật, không thêm luật mới trong lúc dọn — chỉ viết lại. Thấy luật nên đổi thì ghi vào file theo dõi (bước Chưng cất / Tỉa xử lý).
- Không đụng kho (bố cục, nguồn học) ngoài việc sửa đường trỏ.
- Không dọn lẻ một bộ.

## Xong khi
1. Bảng luật hiện hành của mọi bộ có đủ, mỗi dòng có nguồn trong bản mới; ghi nhớ đã dọn.
2. Công cụ đo mọi bộ: "Chưa cần"; dấu ngày, câu ghi đè gần 0; câu trùng 0; dòng gần trùng chỉ còn loại đúng thiết kế.
3. Không link gãy; code dựng không đổi.

## Nhật ký
- 10/11/2026 · tạo skill. David: "mỗi lần học hay bổ sung hay sửa thì không bị chồng chéo… cứ một thời gian… viết lại toàn bộ… học được lớp 1, lớp 2, lớp 3 thì lại phải tổng kết lại toàn bộ để viết lại thành một skill hoàn chỉnh bao gồm cả 3 lớp". Chốt 5 điểm: sửa thẳng mỗi lần + lý do vào sổ · công cụ đo nhắc, David quyết · từng bộ một · kiểm mẫu chuẩn + việc thật · skill riêng.
- 10/11/2026 · đổi sang tái bản toàn bộ. David: "khi tái bản thì cứ tái bản hết toàn bộ mọi thứ để tối ưu nhất". Chốt: cả ba bộ + dọn ghi nhớ · một bộ vượt ngưỡng là tái bản cả đợt · một mốc chung `tai-ban-<n>`, mỗi bộ một phiên con chạy cùng lúc · đợt 2 chạy ngay. Thay luật "từng bộ một".
- 20/11/2026 · công cụ đo đo trùng / rối, không đo độ lớn. Máy báo vượt ngưỡng số dòng (4005 > 4000) sau khi thêm tầng tư duy dựng video. David: "bộ não và các phần cần học chắc chắn sẽ ngày càng tăng lên, tái bản chỉ là gom các bản trùng hay ý trùng theo nhiều cách khác nhau về một hoặc là gỡ rối, chứ yêu cầu phải 4000 dòng thì tôi thấy sẽ bị hạn chế". Chốt: bỏ `dong` khỏi chuông · thêm `gan_trung` (cặp dòng ở hai file chung > 50 % số chữ, bỏ mô tả đầu file, khối lệnh, phần `code`) · `sua` chỉ nhắc nhẹ. Đo lần đầu: video 49 cặp gần trùng.
- 20/11/2026 · đổi "tái bản" thành bước Dọn của vòng **Nâng cấp** (hoc-lien-tuc Việc 4). David: "tôi thấy nên sử dụng từ cải tiến hoặc nâng cấp thì đúng hơn. giống kiểu r&d trong kinh doanh" … "theo đề xuất triển khai luôn đi, vì quá trình học liên tục sẽ rất nhiều". Chốt theo đề xuất: tên "Nâng cấp" · gộp làm một chu trình trong hoc-lien-tuc (skill này còn lại phần dọn + công cụ đo) · thước đo chính = bài kiểm + số liệu người xem. Mốc mới `nang-cap-<n>`; mốc đóng, đo trước / sau, việc thật chuyển sang Việc 4.
