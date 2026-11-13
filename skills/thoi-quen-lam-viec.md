# Thói quen làm việc chung — mọi skill đọc file này trước

Mục tiêu: làm đúng quy trình, ra đúng ý ngay lần đầu, không tốn token vô ích.
File này giữ các thói quen **dùng chung cho mọi skill**. Luật riêng của từng việc nằm trong skill đó; luật riêng của video nằm ở
`dung-video/luat-chung.md`. Sáu luật không được phá ở `AGENTS.md`. Mỗi luật chỉ nằm một chỗ; chỗ khác chỉ trỏ về.

## 0. Khi hai điều ngược nhau
1. **Chất lượng thắng tiết kiệm** ("kết quả hơn tốc độ"). Chỉ tiết kiệm ở chỗ không đổi kết quả.
2. **Khi các nguồn mâu thuẫn: lời David mới nhất > bản luật (`nao/David.md`, skill) > ghi nhớ `nao/bo-nho/`.** Hai bản luật lệch
   nhau thì bên có ngày chốt mới hơn (theo sổ: changelog, git) thắng. Chỗ lệch thường do một chỗ chưa được cập nhật, không phải ý David.
3. Luật còn mơ hồ → xem **sản phẩm mới nhất David đã duyệt** làm chứng cứ, rồi hỏi nếu vẫn chưa rõ.

**Phần AI làm thì sáng tạo hết sức:** khung (bước, luật, tiêu chí đạt) và nhận diện lớn là cố định; bên trong mỗi bước cần phán đoán
thì sáng tạo cho hợp nội dung đang làm, không dập khuôn, không lặp cách cũ. Danh mục có sẵn là công cụ, không phải khuôn.
Luật nội dung (nguyên văn lời David, giọng David, lằn ranh) không phải khuôn — vẫn giữ.

## 1. Đầu việc: đọc đúng phần cần
- Đặt **Mục tiêu** và **Xong khi** cho việc (mục 5).
- Đi theo đường: bảng chọn skill trong `AGENTS.md` → `SKILL.md` → chỉ những khối, hồ sơ mà bước đang làm cần.
- Không đọc cả repo. Không đọc `references/`, `changelog`, `hoc-tu-*` trừ khi đang cân nhắc đổi luật hoặc đang gỡ lỗi.
  `gotchas.md` của skill đọc một lần ở đầu phiên.
- File dài: tìm (`grep`) rồi đọc đúng đoạn. Đã đọc trong phiên thì không đọc lại.

## 2. Mặc định là tự làm, hỏi là ngoại lệ
Mục tiêu của David: **đưa tài nguyên vào, nhận kết quả**. Các lần làm thật là để chỉnh phần giữa, không phải để trả lời câu hỏi.
- **Skill / hồ sơ đã định → làm đúng như vậy**, không hỏi, không đề xuất khác. Đề xuất của Claude không bao giờ trái mặc định của
  skill; thấy cần khác mặc định thì đó là tín hiệu 2 (mâu thuẫn) — dừng hỏi, không tự đổi.
- **Skill chưa định → Claude tự chọn** phương án tốt nhất theo tiêu chí của skill, làm luôn, ghi "đã chọn X vì Y" trong báo cáo cuối
  để David sửa ở bản cuối.
- **Yêu cầu của David làm được trong mặc định → giữ mặc định**, không đổi thứ khác để đáp ứng (vd. "tập trung vào điện thoại" ≠ đổi khung).
- **Câu David không trả lời, "làm đi", "theo skill"** = theo mặc định của skill, phần chưa định thì theo đề xuất của Claude.
- **Chỉ dừng hỏi khi:** đăng / gửi / xoá trên mạng xã hội / mật khẩu (`AGENTS.md` luật 4) · tín hiệu nặng của `hoi-chuyen-gia` (mâu thuẫn luật, khó đảo
  ngược, thiếu file / nguồn hỏng, hiểu được nhiều cách làm đổi hẳn kết quả) · sửa thông tin trực tiếp về David, màu chủ đạo, chữ ký
  nhận diện (diễn giải + chờ "ok"). Skill, giọng văn, luật kênh: tự cải tiến theo `skills/tu-hoc`, báo một dòng.
- Phần cứng của video: `dung-video/luat-chung.md` mục 8.

## 3. Trong lúc làm
- **Lệnh theo lô:** các lệnh không phụ thuộc nhau gộp vào một lần gọi. Lệnh > 2 phút chạy nền, không thăm dò.
- **Agent phụ** chỉ khi David cho phép.
- **Bước nhẹ:** skill ghi rõ bước nào nhẹ (chép, đổi tên, chạy lệnh có sẵn). Tới đó nhắc một dòng "bước này nhẹ, bạn có thể đổi
  mô hình rẻ hơn" — không tự đổi.
- **Việc của David là của David:** việc David tự tạo hoặc tự bấm (một việc dựng, render đang chạy) thì không tự bấm Chạy tiếp, Duyệt,
  Làm lại hay chạy lệnh thay, kể cả khi Claude vừa vô tình làm ngắt nó; chỉ báo tình trạng và chờ lệnh. Việc thử của Claude đặt tên riêng
  (`thu-…`) và chỉ thao tác trên việc đó. Trước khi tắt hay chạy lại thứ dùng chung (render, tiến trình nền), kiểm có việc của David
  hoặc phiên khác đang chạy không; có thì hỏi trước.
- **Công cụ David đã cài là để nâng skill:** thấy công cụ trên máy giúp việc tốt hơn mà skill chưa dùng thì đề xuất tích hợp (diễn giải
  ngắn trước khi sửa skill), giữ cách cũ làm dự phòng khi công cụ lỗi.
- **Không dùng mod giao diện:** David gỡ hết 13/11/2026; không tự cài lại mod, plugin vẽ bảng hay thanh tiến độ.
- Đăng, gửi, xoá, mật khẩu: `AGENTS.md` luật 5.

## 4. Cuối việc
- **Báo cáo ngắn, tiếng Việt:** đã làm gì · đã kiểm gì · chưa kiểm gì · điều cần David xác nhận.
- **Báo lên Telegram** khi xong một việc trọn vẹn (render xong, đăng xong, sửa bộ não xong…) hoặc khi kẹt cần David quyết, không báo
  sau mỗi lượt: `bash scripts/so-nho/bao-cao.sh "✅ Xong: … · Ở đâu: … · Còn lại: …"` hoặc `"❓ Chờ anh: …"`, tối đa 5 dòng. Việc giao
  qua Telegram thì mở đầu bằng số việc `#N`. Máy chưa cài bot thì lệnh chỉ ghi sổ. Chi tiết: [scripts/so-nho/README.md](../scripts/so-nho/README.md).
- **Góp ý của David ghi đúng một chỗ:** sửa skill hoặc khối bị ảnh hưởng + một dòng nhật ký (`changelog` của skill, hoặc mục "Nhật ký").
  Chỉ luật dùng chung cho nhiều skill mới vào `nao/bo-nho/`; đã có ghi nhớ gần giống thì sửa ghi nhớ đó, không tạo cái mới.
- **Sửa thẳng, không chồng câu:** đổi một luật (góp ý, học mẫu, quyết định mới) thì **viết lại chính câu luật đó** thành trạng thái mới
  và xoá câu cũ. Trong bản luật không ghi ngày, không "(David chốt …)", không lời kể đã thay hay thêm câu nào, không "ngoại lệ mới"; ngày, lời
  David nguyên văn và lý do ghi vào sổ quyết định (changelog / Nhật ký). Luật mới đụng luật ở nơi khác → sửa luôn nơi đó, không để hai
  câu cãi nhau. Ba loại file (bản luật · sổ · kho) và định nghĩa từng bộ: skill `tai-ban`.
- **Đo chồng chéo** sau mỗi việc có sửa bản luật: `python3 -I skills/tai-ban/do_chong_cheo.py`. Báo "NÊN TÁI BẢN TOÀN BỘ" → nhắc
  David một dòng; David đồng ý thì tái bản cả bộ não một đợt (skill `tai-ban`).
- **Cập nhật file theo dõi** (`dang-lam/…`, `TRANG-THAI-HIEN-TAI.md`) khi xong một đợt việc.
- **Giữ Mac nhẹ:** Mac chỉ giữ việc đang làm. Xong việc thì đưa việc của David (video gốc, thành quả video) lên Drive rồi xoá trên Mac
  (video: `don_tap.py --xoa` → `luu_drive.sh`); file tải về, dữ liệu app, đồ cá nhân không đồng bộ, muốn xoá thì hỏi trước. Ghi nhớ `video-chuyen-qua-drive`.
- **Đẩy GitHub ngay** khi có thay đổi về skill hoặc não: `bash scripts/sync.sh --push` (`AGENTS.md` luật 6).

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
| Việc chính của phiên đã xong, hoặc phiên đã tự tóm tắt hội thoại | Nhắc "cập nhật não" rồi đóng phiên |
| David quay lại phiên cũ sau nhiều giờ để làm việc mới | Đề nghị phiên mới, vì phiên cũ nạp lại tốn hơn |
| Tin nhắn thiếu một trong ba điều: việc gì, file nào, muốn ra cái gì | Tự suy từ tài nguyên và skill (mục 2); chỉ hỏi khi không đoán được việc gì |
| David dán log hoặc văn bản dài | Vẫn làm; cuối việc nhắc lần sau chỉ cần đưa đường dẫn file |
| Tới bước nhẹ | Nhắc đổi mô hình rẻ hơn (mục 3) |
| Buổi nhìn lại cuối tuần, hoặc `nao/bo-nho/` quá 40 ghi nhớ | Đề nghị "dọn bộ nhớ" (skill `consolidate-memory`) |
| Máy đo chồng chéo báo "NÊN TÁI BẢN TOÀN BỘ" | Nhắc một dòng (mục 4) |
| David hỏi phiên tốn vào đâu | Chạy "giải thích mức dùng" (skill `explain-usage`) |

**Thói quen của David** (để Claude biết mà nhắc): mỗi việc một phiên · xong thì "cập nhật não" rồi đóng · làm liền một mạch ·
nói đủ việc, file, kết quả trong một tin nhắn · gộp việc nhỏ · vòng hỏi trả lời gộp ("đồng ý cả 5", chỉ nêu câu muốn đổi) ·
đưa đường dẫn thay vì dán · nói "chỉ chụp 2–3 khung" khi muốn kiểm nhanh.
