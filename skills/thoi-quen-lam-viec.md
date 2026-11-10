# Thói quen làm việc chung — mọi skill đọc file này trước

Mục tiêu: làm đúng quy trình, ra đúng ý ngay lần đầu, không tốn token vô ích.
File này giữ các thói quen **dùng chung cho mọi skill**. Luật riêng của từng việc nằm trong skill đó; luật riêng của video nằm ở
`dung-video/luat-chung.md`. Sáu luật không được phá ở `AGENTS.md`. Mỗi luật chỉ nằm một chỗ; chỗ khác chỉ trỏ về.

## 0. Khi hai điều ngược nhau
1. **Chất lượng thắng tiết kiệm** ("kết quả hơn tốc độ"). Chỉ tiết kiệm ở chỗ không đổi kết quả.
2. **Lời David vừa nói > bên có ngày chốt gần nhất > bên cũ hơn.** Chỗ lệch giữa các file thường do một chỗ chưa được cập nhật,
   không phải ý David.
3. Khi các nguồn mâu thuẫn: lời David vừa nói > `nao/David.md` > bộ nhớ ngày mới hơn > bộ nhớ cũ.
4. Luật còn mơ hồ → xem **sản phẩm mới nhất David đã duyệt** làm chứng cứ, rồi hỏi nếu vẫn chưa rõ.

**Phần AI làm thì sáng tạo hết sức:** khung (bước, luật, tiêu chí đạt) và nhận diện lớn là cố định; bên trong mỗi bước cần phán đoán
thì sáng tạo cho hợp nội dung đang làm, không dập khuôn, không lặp cách cũ. Danh mục có sẵn là công cụ, không phải khuôn.
Luật nội dung (nguyên văn lời David, giọng David, lằn ranh) không phải khuôn — vẫn giữ.

## 1. Đầu việc: đọc đúng phần cần
- Đặt **Mục tiêu** và **Xong khi** cho việc (mục 5).
- Đi theo đường: bảng chọn skill trong `AGENTS.md` → `SKILL.md` → chỉ những khối, hồ sơ mà bước đang làm cần.
- Không đọc cả repo. Không đọc `references/`, `changelog`, `hoc-tu-*` trừ khi đang cân nhắc đổi luật hoặc đang gỡ lỗi.
  `gotchas.md` của skill đọc một lần ở đầu phiên.
- File dài: tìm (`grep`) rồi đọc đúng đoạn. Đã đọc trong phiên thì không đọc lại.
- Sự thật tra được (file, bộ nhớ, công cụ, web) thì tự tra, không hỏi David.

## 2. Hỏi: một lần, gộp, có đề xuất
- Cách hỏi theo skill `hoi-chuyen-gia`. Thói quen chung:
- **Hỏi một lần ở đầu**, gộp mọi điểm cần David chọn (chữ bìa, câu chốt, cảnh, nền tảng, phạm vi…). Mỗi câu có một đề xuất đứng
  đầu, để David chỉ cần "đồng ý". Không hỏi điều đã có trong file, bộ nhớ, skill.
- David "ok" → chạy trọn một mạch. "Làm đi" chỉ cho phép làm việc được giao, **không phải chốt các lựa chọn** bên trong nó.
- Giữa chừng chỉ dừng khi gặp một trong 6 tín hiệu của `hoi-chuyen-gia`; phần không bị ảnh hưởng vẫn làm tiếp.
- Ngoại lệ được tự chọn, không hỏi trước: cắt highlight, làm lại video cũ. Vẫn báo rõ đã chọn gì để David sửa.
- **Phần cứng không hỏi, không đổi:** những gì quy trình mặc định đã định (nhận diện, dấu góc, màn chốt, thẻ cuối, nhạc theo tuyến,
  mức motion graphics, phụ đề, chuẩn âm lượng, nơi giao file, tên riêng chưa chắc → dùng cách Whisper nghe và nêu ở báo cáo) thì cứ
  làm đúng mặc định, kể cả với bản "riêng", bản thử. Không đưa thành câu hỏi, không đề xuất bỏ hay giảm. Chỉ hỏi điều quy trình chưa định.

## 3. Trong lúc làm
- **Lệnh theo lô:** các lệnh không phụ thuộc nhau gộp vào một lần gọi. Lệnh > 2 phút chạy nền, không thăm dò; render nối tiếp, không song song.
- **Chụp kiểm có giới hạn:** chụp đúng mốc dễ lỗi (khung mới lần đầu, chỗ chồng lớp, mối cắt, màn chốt, thẻ cuối, chỗ David góp ý),
  không chụp từng cảnh. Xem bố cục thì dùng ảnh thu nhỏ.
- **Agent phụ** chỉ khi David cho phép.
- **Bước nhẹ:** skill ghi rõ bước nào nhẹ (chép, đổi tên, chạy lệnh có sẵn). Tới đó nhắc một dòng "bước này nhẹ, bạn có thể đổi
  mô hình rẻ hơn" — không tự đổi.
- **Không tự render lại** sau góp ý: chỉ sửa skill, kịch bản; render khi David nói "render".
- Đăng, gửi, xoá, mật khẩu: `AGENTS.md` luật 5.

## 4. Cuối việc
- **Báo cáo ngắn, tiếng Việt:** đã làm gì · đã kiểm gì · chưa kiểm gì · điều cần David xác nhận.
- **Góp ý của David ghi đúng một chỗ:** sửa skill hoặc khối bị ảnh hưởng + một dòng nhật ký (`changelog` của skill, hoặc mục "Nhật ký").
  Chỉ luật dùng chung cho nhiều skill mới vào `nao/bo-nho/`; đã có ghi nhớ gần giống thì sửa ghi nhớ đó, không tạo cái mới.
- **Sửa thẳng, không chồng câu:** đổi một luật (góp ý, học mẫu, quyết định mới) thì **viết lại chính câu luật đó** thành trạng thái mới
  và xoá câu cũ. Trong bản luật không ghi ngày, không "(David chốt …)", không lời kể đã thay hay thêm câu nào, không "ngoại lệ mới"; ngày, lời
  David nguyên văn và lý do ghi vào sổ quyết định (changelog / Nhật ký). Luật mới đụng luật ở nơi khác → sửa luôn nơi đó, không để hai
  câu cãi nhau. Ba loại file (bản luật · sổ · kho) và định nghĩa từng bộ: skill `tai-ban`.
- **Đo chồng chéo** sau mỗi việc có sửa bản luật: `python3 -I skills/tai-ban/do_chong_cheo.py`. Báo "NÊN TÁI BẢN TOÀN BỘ" → nhắc
  David một dòng; David đồng ý thì tái bản cả bộ não một đợt (skill `tai-ban`).
- **Video đã chốt hoặc đã đăng:** dọn file tạm luôn bằng `don_tap.py --xoa` (khối 17), không hỏi lại David.
  Chỉ hỏi khi script báo ⏸ (việc đang dở, có thể của phiên khác). File vào Thùng rác, David tự đổ.
- **Cập nhật file theo dõi** (`dang-lam/…`, `TRANG-THAI-HIEN-TAI.md`) khi xong một đợt việc.
- **Đẩy GitHub ngay** khi có thay đổi về skill hoặc não: `bash scripts/sync.sh --push` (`AGENTS.md` luật 6).

## 5. Luôn đi tới mục tiêu, giữ phiên gọn
**Mục tiêu và "Xong khi":** mọi việc, trừ câu hỏi nhanh.
- **Đầu việc:** trong lần hỏi đầu, ghi một dòng **Mục tiêu** và 2–4 dòng **Xong khi**. Skill đã có "Xong khi" thì lấy từ đó. David "ok" là chốt.
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
| Tin nhắn thiếu một trong ba điều: việc gì, file nào, muốn ra cái gì | Hỏi gộp một lần, có đề xuất (mục 2) |
| David dán log hoặc văn bản dài | Vẫn làm; cuối việc nhắc lần sau chỉ cần đưa đường dẫn file |
| Tới bước nhẹ | Nhắc đổi mô hình rẻ hơn (mục 3) |
| Buổi nhìn lại cuối tuần, hoặc `nao/bo-nho/` quá 40 ghi nhớ | Đề nghị "dọn bộ nhớ" (skill `consolidate-memory`) |
| Máy đo chồng chéo báo "NÊN TÁI BẢN" | Nhắc một dòng (mục 4) |
| David hỏi phiên tốn vào đâu | Chạy "giải thích mức dùng" (skill `explain-usage`) |

**Thói quen của David** (để Claude biết mà nhắc): mỗi việc một phiên · xong thì "cập nhật não" rồi đóng · làm liền một mạch ·
nói đủ việc, file, kết quả trong một tin nhắn · gộp việc nhỏ · vòng hỏi trả lời gộp ("đồng ý cả 5", chỉ nêu câu muốn đổi) ·
đưa đường dẫn thay vì dán · nói "chỉ chụp 2–3 khung" khi muốn kiểm nhanh.
