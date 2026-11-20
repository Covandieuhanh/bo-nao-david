---
description: "Thói quen làm việc chung mọi skill đọc trước: khi hai điều ngược nhau, đọc đúng phần, khi nào hỏi, trong lúc làm, cuối việc, giữ phiên gọn."
---

# Thói quen làm việc chung — mọi skill đọc file này trước

Mục tiêu: làm đúng quy trình, ra đúng ý ngay lần đầu, không tốn token vô ích.
File này giữ các thói quen **dùng chung cho mọi skill**. Luật riêng của từng việc nằm trong skill đó; luật riêng của video nằm ở
`san-xuat-video/quy-tac-chung.md`. Sáu luật không được phá ở `AGENTS.md`. Mỗi luật chỉ nằm một chỗ; chỗ khác chỉ trỏ về.

## 0. Khi hai điều ngược nhau
1. **Chất lượng thắng tiết kiệm** ("kết quả hơn tốc độ"). Chỉ tiết kiệm ở chỗ không đổi kết quả.
2. **Khi các nguồn mâu thuẫn: lời David mới nhất > bản luật (`co-so-tri-thuc/david.md`, skill) > ghi nhớ `co-so-tri-thuc/bo-nho/`.** Hai bản luật lệch
   nhau thì bên có ngày chốt mới hơn (theo sổ: changelog, git) thắng. Chỗ lệch thường do một chỗ chưa được cập nhật, không phải ý David.
3. Luật còn mơ hồ → xem **sản phẩm mới nhất David đã duyệt** làm chứng cứ, rồi hỏi nếu vẫn chưa rõ.

**Phần AI làm thì sáng tạo hết sức:** khung (bước, luật, tiêu chí đạt) và nhận diện lớn là cố định; bên trong mỗi bước cần phán đoán
thì sáng tạo cho hợp nội dung đang làm, không dập khuôn, không lặp cách cũ. Danh mục có sẵn là công cụ, không phải khuôn.
Luật nội dung (nguyên văn lời David, giọng David, lằn ranh) không phải khuôn — vẫn giữ.

**Nội dung là của David:** David tự xây nội dung, nói tự do và có cảm xúc. AI không viết khuôn lời, không đặt kịch bản thu âm, không đề xuất
đổi lời David; AI lo phần hình và cách trình bày (thẩm mỹ, nhịp), lấy người xem làm trung tâm. Chi tiết cho video: `san-xuat-video/quy-tac-chung.md` mục 0–1.

## 1. Đầu việc: đọc đúng phần cần
- Đặt **Mục tiêu** và **Xong khi** cho việc (mục 5).
- Đi theo đường: bảng chọn skill trong `AGENTS.md` → `SKILL.md` → chỉ những khối, hồ sơ mà bước đang làm cần.
- Không đọc cả repo. Không đọc `references/`, `changelog`, `hoc-tu-*` trừ khi đang cân nhắc đổi luật hoặc đang gỡ lỗi.
  `loi-thuong-gap.md` của skill đọc một lần ở đầu phiên.
- File dài: tìm (`grep`) rồi đọc đúng đoạn. Đã đọc trong phiên thì không đọc lại.

## 2. Duyệt 4 phần trước, duyệt rồi tự làm trọn
**Mọi việc** (kể cả khi David chỉ gửi video/ghi âm không kèm lời, sửa skill, sửa bộ não, dựng hệ thống, thông tin trực tiếp về David: hồ sơ, màu chủ đạo, chữ ký nhận diện, mạng xã hội): trước khi tạo/sửa bất kỳ file nào, trình đủ
**4 phần** — **Mục tiêu** (kết quả, đo bằng gì) · **Kế hoạch** (làm gì, ở đâu, chọn gì vì sao) · **Quy trình** (từng bước) · **Thực thi** (checklist nhỏ nhất,
có mốc làm ngay) — kèm các điểm cần chốt (mỗi điểm có đề xuất đứng đầu), rồi **dừng chờ David "duyệt"**. Duyệt (hoặc sửa phần nào thì trình lại phần đó) →
**tự làm trọn một mạch**, tự thử thật tới khi chắc dùng được, không xin phép từng bước, không dừng giữa chừng trừ tín hiệu nặng; xong báo kết quả. Phiên giao
qua Telegram gửi 4 phần bằng `bao-cao.sh "#N ❓ Chờ anh duyệt 4 phần: …"`.
**Miễn 4 phần:** câu hỏi nhanh, tra cứu, giải thích (trả lời thẳng) · bot Sổ nhớ ghi nhớ, tra sổ · lịch tự chạy David đã duyệt (`tu-dong-hoa/lich/lich-chay.md`,
`[TU-HOC]`): chạy theo lời giao đã duyệt, không trình lại mỗi lần.
**Việc tự chạy phải nhìn thấy được:** lịch và việc giao qua Telegram mở thành phiên hiện trong app Claude (Remote Control) để David xem, kiểm và gõ tiếp,
không chạy ngầm; cách làm: `tu-dong-hoa/lich/lich-chay.md`, `tu-dong-hoa/so-tay/README.md`.
Trong 4 phần, cách chọn từng điểm:
- **Skill / hồ sơ đã định → làm đúng như vậy**, không đề xuất khác. Đề xuất của Claude không bao giờ trái mặc định của
  skill; thấy cần khác mặc định thì đó là tín hiệu 2 (mâu thuẫn) — dừng hỏi, không tự đổi.
- **Skill chưa định → Claude tự chọn** phương án tốt nhất theo tiêu chí của skill, ghi "chọn X vì Y" ngay trong phần Kế hoạch để David duyệt.
- **Yêu cầu của David làm được trong mặc định → giữ mặc định**, không đổi thứ khác để đáp ứng (vd. "tập trung vào điện thoại" ≠ đổi khung).
- **Câu David không trả lời, "làm đi", "theo skill"** = theo mặc định của skill, phần chưa định thì theo đề xuất của Claude.
- **Sau khi duyệt, chỉ dừng hỏi khi:** đăng / gửi / xoá trên mạng xã hội / mật khẩu (`AGENTS.md` luật 4) · tín hiệu nặng của `thu-thap-yeu-cau` (mâu thuẫn luật, khó đảo
  ngược, thiếu file / nguồn hỏng, hiểu được nhiều cách làm đổi hẳn kết quả) · sửa thông tin trực tiếp về David, màu chủ đạo, chữ ký
  nhận diện (trình lại, chờ "duyệt").
- **Tự học:** skill, giọng văn, luật kênh tự học liên tục theo hình mẫu có số liệu (`ky-nang/hoc-lien-tuc/SKILL.md`); phân tích tự chạy, phần sửa
  đề xuất trong 4 phần của buổi nhìn lại tuần.
- Phần cứng của video: `san-xuat-video/quy-tac-chung.md` mục 8.

## 3. Trong lúc làm
- **Lệnh theo lô:** các lệnh không phụ thuộc nhau gộp vào một lần gọi. Lệnh > 2 phút chạy nền, không thăm dò.
- **Agent phụ** chỉ khi David cho phép. Việc chỉ đọc, tìm, tóm tắt nhiều thì dùng agent `nghien-cuu` (mô hình nhỏ Haiku, `tac-tu/nghien-cuu.md`): nhanh, tốn ít hạn mức; phần suy nghĩ và quyết định giữ ở phiên chính.
- **Bước nhẹ:** skill ghi rõ bước nào nhẹ (chép, đổi tên, chạy lệnh có sẵn). Tới đó nhắc một dòng "bước này nhẹ, bạn có thể đổi
  mô hình rẻ hơn" — không tự đổi.
- **Việc của David là của David:** việc David tự tạo hoặc tự bấm (một việc dựng, render đang chạy) thì không tự bấm Chạy tiếp, Duyệt,
  Làm lại hay chạy lệnh thay, kể cả khi Claude vừa vô tình làm ngắt nó; chỉ báo tình trạng và chờ lệnh. Việc thử của Claude đặt tên riêng
  (`thu-…`) và chỉ thao tác trên việc đó. Trước khi tắt hay chạy lại thứ dùng chung (render, tiến trình nền), kiểm có việc của David
  hoặc phiên khác đang chạy không; có thì hỏi trước.
- **Công cụ David đã cài là để nâng skill:** thấy công cụ trên máy giúp việc tốt hơn mà skill chưa dùng thì đề xuất tích hợp (diễn giải
  ngắn trước khi sửa skill), giữ cách cũ làm dự phòng khi công cụ lỗi.
- **Không dùng mod giao diện:** không cài mod, plugin vẽ bảng hay thanh tiến độ, dòng trên ô nhập; chỉ giữ plugin Telegram. Muốn mod mới thì hỏi David trước.
- **Thêm việc không phá việc cũ:** bổ sung việc, tính năng mới thì việc cũ phải chạy y như trước. Chỉ đổi phần cũ khi 4 phần đã duyệt ghi rõ. Sửa thứ dùng chung (script lịch, máy canh, hook) thì tự thử lại việc cũ trước khi báo xong. Mọi thứ phải tự động, không trông vào David bấm tay (ghi nhớ `quy-tac-them-viec-khong-pha-viec-cu`).
- Đăng, gửi, xoá, mật khẩu: `AGENTS.md` luật 4.

## 4. Cuối việc
Ghi lại gì, ở đâu, đi lên tầng nào: trục `../co-so-tri-thuc/truc-tri-thuc.md` (mục này là vòng học "mỗi việc" của trục).
- **Tự soát trước khi báo xong:** (1) kiểm theo "Xong khi" và tiêu chí của skill; (2) tự hỏi "đã xong hết chưa?" rồi quét lại một lượt
  tìm chỗ sót; (3) đổi tên, đổi cấu trúc, đổi luồng thì chạy thử trọn một quy trình thật trước khi báo, vì lỗi hay nằm ở chỗ ghép nối;
  (4) việc phức tạp, rủi ro cao: đề nghị một agent chưa tham gia việc soát lại, chỉ bắt lỗi làm sai yêu cầu (cần David cho phép, mục 3).
- **Báo cáo ngắn, tiếng Việt:** đã làm gì · đã kiểm gì · chưa kiểm gì · điều cần David xác nhận.
- **Báo lên Telegram** khi xong một việc trọn vẹn (render xong, đăng xong, sửa bộ não xong…) hoặc khi kẹt cần David quyết, không báo
  sau mỗi lượt: `bash tu-dong-hoa/so-tay/bao-cao.sh "✅ Xong: … · Ở đâu: … · Còn lại: …"` hoặc `"❓ Chờ anh: …"`, tối đa 5 dòng. Việc giao
  qua Telegram thì mở đầu bằng số việc `#N`. Máy chưa cài bot thì lệnh chỉ ghi sổ. Chi tiết: `tu-dong-hoa/so-tay/README.md` (chỉ Mac chính).
- **Nhắc lần hai thì thành luật ngay:** David phải nhắc lại một điều lần thứ hai → sửa ngay đúng nhà của luật đó, không đợi lượt nhìn lại tuần
  (skill, giọng văn, luật kênh, thông tin về David: đề xuất trong 4 phần, chờ "duyệt").
- **Góp ý của David ghi đúng một chỗ:** sửa skill hoặc khối bị ảnh hưởng + một dòng nhật ký (`changelog` của skill, hoặc mục "Nhật ký");
  lỗi David phải sửa thì thêm một câu kiểm vào bộ kiểm của bộ đó (trục mục 4).
  Chỉ luật dùng chung cho nhiều skill mới vào `co-so-tri-thuc/bo-nho/`; đã có ghi nhớ gần giống thì sửa ghi nhớ đó, không tạo cái mới.
  `co-so-tri-thuc/david.md` chỉ ghi điều cố định đã chốt, vì mọi AI đọc nó như định hướng; ý tưởng, góp ý đang cân nhắc ghi
  `du-an/danh-sach-y-tuong.md` (hoặc file `du-an/` phù hợp), David chốt rồi mới đưa vào `david.md` qua 4 phần.
- **Sửa thẳng, không chồng câu:** đổi một luật (góp ý, học mẫu, quyết định mới) thì **viết lại chính câu luật đó** thành trạng thái mới
  và xoá câu cũ. Trong bản luật không ghi ngày, không "(David chốt …)", không lời kể đã thay hay thêm câu nào, không "ngoại lệ mới"; ngày, lời
  David nguyên văn và lý do ghi vào sổ quyết định (changelog / Nhật ký). Luật mới đụng luật ở nơi khác → sửa luôn nơi đó, không để hai
  câu cãi nhau. Ba loại file (bản luật · sổ · kho) và định nghĩa từng bộ: skill `tai-cau-truc`.
- **Đo chồng chéo** sau mỗi việc có sửa bản luật: `python3 -I ky-nang/tai-cau-truc/do-chong-cheo.py`. Báo "NÊN NÂNG CẤP" → nhắc
  David một dòng; David đồng ý thì nâng cấp cả bộ não một đợt (`hoc-lien-tuc` Việc 4).
- **Cập nhật file theo dõi** (`du-an/…`, `bao-cao-trang-thai.md`) khi xong một đợt việc.
- **Giữ mạng lưới liên kết** ([co-so-tri-thuc/quy-uoc-lien-ket.md](../co-so-tri-thuc/quy-uoc-lien-ket.md)): file mới có mô tả đầu file và
  một dòng ở trang [ban-do/](../ban-do/README.md) đúng chủ đề; đổi tên, gộp, xoá file thì sửa mọi nối tới nó. Trao đổi có **kiến thức đáng giữ**
  (công cụ, khái niệm, phần Claude giải thích mà David thấy hay) thì ghi hoặc bổ sung ghi chú trong `co-so-tri-thuc/kien-thuc/`, nối tới
  ý tưởng / dự án / skill liên quan. Máy kiểm tự chạy khi đồng bộ.
- **Giữ Mac nhẹ:** Mac chỉ giữ việc đang làm. Xong việc thì đưa việc của David (video gốc, thành quả video) lên Drive rồi xoá trên Mac
  (video: `don-tap.py --xoa` → `luu-drive.sh`); file tải về, dữ liệu app, đồ cá nhân không đồng bộ, muốn xoá thì hỏi trước. Ghi nhớ `video-chuyen-qua-drive`.
  Xoá video trên Mac chỉ bằng `luu-drive.sh` (chép cả tập → lên mây → so khớp → mới xoá), không tự lọc file bằng `find … -delete`
  (`-delete` làm mất tác dụng `-prune`, ngày 20/11/2026 đã xoá mất gốc DJI_0030 của tập máy đo giải pháp AI).
  **Video: Mac chỉ giữ bản cuối chưa đăng** ở `~/Movies/cho-dang/<tập>/` (David 20/11/2026: "tôi chỉ quan tâm đến các kết quả cuối thôi");
  bản gốc + dự án dựng chỉ ở Drive. Render xong → `cho-dang.sh gui`; đăng xong → `cho-dang.sh xong` (kiểm Drive rồi mới xoá).
  Kiểm nhanh: trang `localhost:8765/mac` (Chờ đăng + dự án còn trên Mac) hoặc `python3 tu-dong-hoa/kiem-video-mac.py` (chỉ đọc).
  David nói "kiểm video" → chạy lệnh này; "dọn Mac" → `luu-drive.sh` cho các dự án ✅; "đã đăng <tập>" → `cho-dang.sh xong`.
- **Đẩy GitHub ngay** khi có thay đổi về skill hoặc não: `bash tu-dong-hoa/dong-bo.sh --push` (`AGENTS.md` luật 6).

## 5. Luôn đi tới mục tiêu, giữ phiên gọn
**Mục tiêu và "Xong khi":** mọi việc, trừ câu hỏi nhanh.
- **Đầu việc:** ghi một dòng **Mục tiêu** và 2–4 dòng **Xong khi** ngay tin nhắn đầu (việc cần hỏi: trong lần hỏi). Skill đã có "Xong khi" thì lấy từ đó.
- **Trong lúc làm:** trước mỗi bước, tự hỏi bước đó có đưa tới "Xong khi" không. Không thì bỏ, hoặc hỏi David.
  David đổi ý giữa chừng → viết lại mục tiêu một dòng, chờ "ok".
- **Cuối việc:** đối chiếu từng dòng "Xong khi": **đạt / chưa đạt / chưa kiểm**.
  Còn dòng chưa đạt thì không báo "xong": nói rõ dòng nào, ghi bước tiếp vào file theo dõi.

**Nhắc hoặc hỏi lại David:** chỉ một dòng, mỗi chuyện nhắc một lần. David nói "cứ làm" thì làm tiếp, không nhắc lại.

| Khi | Claude làm |
|---|---|
| Việc tiếp theo lớn, hoặc David đưa việc mới khác hẳn việc đang làm | Đề nghị mở phiên mới, ghi sẵn bước tiếp ở file theo dõi |
| Phiên đã dài, hoặc đã tự tóm tắt mà việc chưa xong | Viết lời bàn giao trong một khung để dán vào phiên mới: đã xong · còn lại theo thứ tự · file ở đâu · đã chốt kèm lý do |
| Việc chính của phiên đã xong hoàn chỉnh (đã lưu file, đã đẩy GitHub) | Hỏi David một dòng "Xong rồi, đóng phiên này nhé?"; David đồng ý thì đóng (việc `#N`: `giao-viec.sh --dung N`). Phiên đã tự tóm tắt mà việc chưa xong: dòng bàn giao ở trên |
| David quay lại phiên cũ sau nhiều giờ để làm việc mới | Đề nghị phiên mới, vì phiên cũ nạp lại tốn hơn |
| Tin nhắn thiếu một trong ba điều: việc gì, file nào, muốn ra cái gì | Tự suy từ tài nguyên và skill (mục 2); chỉ hỏi khi không đoán được việc gì |
| David dán log hoặc văn bản dài | Vẫn làm; cuối việc nhắc lần sau chỉ cần đưa đường dẫn file |
| Tới bước nhẹ | Nhắc đổi mô hình rẻ hơn (mục 3) |
| Buổi nhìn lại cuối tuần, hoặc `co-so-tri-thuc/bo-nho/` quá 40 ghi nhớ | Đề nghị "dọn bộ nhớ" (skill `consolidate-memory`) |
| Máy đo chồng chéo báo "NÊN NÂNG CẤP", hoặc đã có ≥ 10 video có số liệu từ lần nâng cấp trước | Nhắc một dòng (mục 4) |
| David hỏi phiên tốn vào đâu | Chạy "giải thích mức dùng" (skill `explain-usage`) |

**Thói quen của David** (để Claude biết mà nhắc): mỗi việc một phiên · xong thì "cập nhật não" rồi đóng · làm liền một mạch ·
nói đủ việc, file, kết quả trong một tin nhắn · gộp việc nhỏ · vòng hỏi trả lời gộp ("đồng ý cả 5", chỉ nêu câu muốn đổi) ·
đưa đường dẫn thay vì dán · nói "chỉ chụp 2–3 khung" khi muốn kiểm nhanh.
