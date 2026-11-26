---
description: "Quy trình vận hành chung (tầng 2, cách làm từng bước cho mọi skill), cùng số mục với chuẩn mực làm việc: đầu việc, mẫu bốn phần (việc chưa có quy trình) và câu báo, trong lúc làm (lệnh theo lô, tệp lệnh trên Windows, agent phụ, bước nhẹ), cuối việc (soát, ghi sổ, báo cáo, Telegram, dọn thiết bị, đẩy GitHub), giữ phiên gọn."
---

# Quy trình vận hành chung (cách làm từng bước)

Nguyên lý ở [chuan-muc-lam-viec.md](chuan-muc-lam-viec.md), cùng số mục. File này là tầng 2: đổi theo góp ý có dẫn chứng; mỗi bước có lệnh hoặc mẫu cụ thể. Phần ghi "Mac chính" là của bộ tự động hoá trên Mac chính (repo riêng tư); máy khác bỏ qua.

## 1. Đầu việc

Khi thuật ngữ ảnh hưởng tới yêu cầu, quyết định hay tiêu chí nghiệm thu, đối chiếu [hệ thuật ngữ](../co-so-tri-thuc/bang-thuat-ngu.md) ngay khi đọc yêu cầu và dùng cùng nghĩa trong báo cáo bàn giao.
1. Với nhiệm vụ cần đầu ra, xác định mục tiêu trước rồi bóc tách công việc. Ghi một dòng **Mục tiêu** và hai tới bốn dòng **Xong khi** (tiêu chí hoàn thành) ngay tin nhắn đầu; skill đã có "Xong khi" thì lấy từ đó. Nêu rõ đầu ra bắt buộc, cách kiểm và quyết định AI được tự chọn nếu có.
2. Tra cây quy trình `quy-trinh.md`: gốc, rồi lá đúng việc, rồi file quy trình của lá, rồi chỉ những khối và hồ sơ mà bước đang làm cần.
3. Việc có tài nguyên: tra sổ danh mục `~/Movies/_danh-muc-noi-dung/danh-muc-noi-dung.md` (trong repo: `du-an/danh-muc-noi-dung.md`) trước tiên.
4. Tra hình mẫu: mở `co-so-tri-thuc/hinh-mau/README.md`, tìm mục nhỏ của việc; chưa đủ hình mẫu thì nghiên cứu theo lá A8.
5. Không đọc cả repo; không đọc `references/`, nhật ký thay đổi, `hoc-tu-*` trừ khi cân nhắc đổi luật hoặc gỡ lỗi. `loi-thuong-gap.md` của skill đọc một lần ở đầu phiên. File dài: tìm bằng `grep` rồi đọc đúng đoạn; đã đọc trong phiên thì không đọc lại.

### Tiếp quản công việc đang dở

1. Xác định đúng việc qua yêu cầu và báo cáo trạng thái; mở nguồn được chỉ định cho việc đó (với video là sổ danh mục) và đối chiếu đầu ra thực tế nếu truy cập được.
2. Xác nhận quyết định mới nhất, phần đã duyệt, phần còn mở và bước có thể làm ngay. Khi các nguồn lệch nhau, áp dụng thứ tự ưu tiên trong [chuẩn mực](chuan-muc-lam-viec.md) mục 0. Ghi rõ nguồn và mốc của quyết định dùng để tiếp tục.
3. Làm tiếp bước được phép và cập nhật đúng nguồn trạng thái của việc. Chỉ hỏi khi tới điểm duyệt hoặc gặp điều kiện phải dừng theo chuẩn mực. Khi báo, nêu phần vừa hoàn thành và phần còn chờ.

## 2. Bốn phần và câu báo

Trao đổi để làm rõ thông tin được trình bày tự nhiên. Khi nhiệm vụ lớn có việc nhỏ, ghi mục tiêu và tiêu chí nghiệm thu của việc nhỏ tại đúng bước Thực thi của việc lớn.
- **Bốn phần** (khi David yêu cầu bản kế hoạch hoặc khi cần duyệt Đ1, theo [luật 2](../AGENTS.md#sáu-luật-không-được-phá)): Mục tiêu (kết quả, đo bằng gì) · Kế hoạch (làm gì, ở đâu, chọn gì vì sao) · Quy trình (từng bước) · Thực thi (danh sách kiểm nhỏ nhất, có mốc làm ngay). Kèm các điểm cần chốt, mỗi điểm có đề xuất đứng đầu. Trước khi gửi bản kế hoạch, rà đủ bốn đề mục theo thứ tự, tiêu chí nghiệm thu và trạng thái thực thi. Sửa phần nào thì trình lại phần đó.
- **Phiên giao qua Telegram** (Mac chính): việc đã có quy trình thì làm trọn rồi báo `bao-cao.sh "#N ✅ …"`; việc chưa có quy trình thì gửi bốn phần bằng `bao-cao.sh "#N ❓ Chờ anh duyệt 4 phần: …"`.
- **Lịch tự chạy đã duyệt** (Mac chính, `tu-dong-hoa/lich/lich-chay.md`, `[TU-HOC]`): chạy theo lời giao đã duyệt, không trình lại mỗi lần.
- **Phiên tự chạy nhìn thấy được** (Mac chính): lịch và việc giao qua Telegram mở thành phiên hiện trong ứng dụng Claude (Remote Control); cách làm: `tu-dong-hoa/lich/lich-chay.md`, `tu-dong-hoa/so-tay/README.md`.
- **Tự học của skill:** skill, giọng văn, luật kênh tự học theo hình mẫu có số liệu (`ky-nang/hoc-lien-tuc/SKILL.md`); phân tích và sửa đều tự chạy trong buổi nhìn lại tuần, báo David sau.
- Phần cứng của video: `san-xuat-video/quy-tac-chung.md` mục 8.

### 2a. Lập bảng giao việc

1. **Mục tiêu.** Đọc tài liệu nguồn và yêu cầu mới nhất của David. Ghi điều cần đạt, cách đo, mốc đo và các điều kiện đã chốt. Khi thiếu thông tin làm đổi mục tiêu, phạm vi hoặc cách làm, dùng [thu thập yêu cầu](thu-thap-yeu-cau/SKILL.md). Ghi rõ mốc đề xuất. Biến quyết định chưa chốt thành việc cần duyệt trước khi thực hiện việc phụ thuộc.
2. **Kế hoạch.** Chọn các nhóm việc đủ để đạt mục tiêu. Xếp theo giai đoạn thật của công việc. Hội thảo dùng trước, trong và sau sự kiện.
3. **Quy trình.** Trong từng nhóm, nêu các bước theo quan hệ phụ thuộc. Tách các bước soạn, kiểm tra, duyệt, bàn giao, thực hiện và theo dõi khi mỗi bước có đầu ra hoặc ban chịu trách nhiệm riêng.
4. **Thực thi.** Mỗi dòng ghi một hành động có đối tượng cụ thể, một ban chịu trách nhiệm, một hạn xong và một đầu ra kiểm được. Xếp theo trình tự thực hiện và giữ tên hoặc số bước để tìm về quy trình. Bảng chỉ giao cho Vận hành, Đối tác hoặc Marketing, theo phạm vi tại [mô hình kinh doanh, mục 2](../co-so-tri-thuc/mo-hinh-kinh-doanh.md#2-ba-phần-của-doanh-nghiệp). Người đã được chỉ định làm một thao tác cụ thể có thể xuất hiện trong nội dung việc. Cột giao việc chỉ ghi ban. Mỗi việc có một hạng mục chính trong Tiền, Thị trường, Con người. Trong Excel dùng màu nhất quán cho hạng mục và hiện tên ban.
5. **Kết quả** và **Vấn đề** là hai cột ghi nhận sau thực thi. Để cả hai trống khi giao bảng. Khi làm, ghi đầu ra thực tế hoặc nguyên nhân cản trở. Nếu vướng do giả định của kế hoạch sai, quay lại Kế hoạch theo [vòng hành động gốc](../co-so-tri-thuc/tu-duy-goc.md#2-khối-hành-động--vòng-kết-quả-hoặc-vấn-đề).

**Xong khi:** người nhận đọc một dòng và biết làm gì, ban nào làm, bao giờ xong và kiểm đầu ra bằng gì. Soát các mốc bàn giao, phân ban theo mô hình gốc, đối chiếu dữ kiện đã chốt và mở lại tệp xuất để kiểm hai cột ghi nhận. [Trường hợp hội thảo và phép thử dùng lại](../du-an/hoc-lien-tuc/2026-11-26.md#trường-hợp-lập-bảng-giao-việc-hội-thảo).

## 3. Trong lúc làm
- **Lệnh theo lô:** các lệnh không phụ thuộc nhau gộp vào một lần gọi; lệnh quá 2 phút chạy nền, không thăm dò.
- **Trên Windows:** lệnh dài hoặc có đường dẫn tiếng Việt, khoảng trắng thì viết thành tệp lệnh (.sh hoặc .py, mã hoá UTF-8) rồi chạy bằng một lệnh ngắn trong WSL; không gõ chuỗi dài qua PowerShell. Đầu phiên: `bash tu-dong-hoa/dong-bo.sh --keo` rồi `kiem-moi-truong.sh`; máy mới chạy `tu-dong-hoa/thiet-bi-khac/kiem-tra-thiet-bi.sh`. Bản bộ não để làm việc trên Windows là bản trong WSL (`~/Documents/bo-nao-david`); bản ở thư mục Windows chỉ để đọc. Python trên Windows mặc định in chữ bằng bảng mã cp1258 nên dừng đột ngột khi gặp chữ Việt: máy Windows đặt biến người dùng `PYTHONUTF8=1` (`cai-cong-cu-video.sh` tự đặt, `kiem-tra-thiet-bi.sh` tự kiểm); chạy Python phía Windows với cờ `-I` thì thêm `-X utf8` (`python -I -X utf8 …`), vì `-I` bỏ qua mọi biến môi trường (đã thử 26/11/2026); script tự ghi file thì luôn ghi rõ `encoding='utf-8'`.
- **Thiết bị nào cũng một quy trình:** khi nhận nhiệm vụ, áp dụng [kiểm tra khả năng thực thi](../huong-dan-cai-dat.md#kiểm-tra-khả-năng-thực-thi). luật, ghi nhớ, cách làm học được trên thiết bị nào cũng ghi vào bộ não (`co-so-tri-thuc/bo-nho/`, skill) rồi đẩy GitHub, không để ở ghi nhớ riêng của thiết bị; thiết bị thiếu công cụ (Drive, trình duyệt, gói phần mềm) thì Claude tự cài hoặc dùng cách khác có sẵn để làm trọn việc, chỉ nhờ David phần chỉ David làm được (đăng nhập, mật khẩu, cấp quyền).
- **Agent phụ** chỉ khi David cho phép; việc chỉ đọc, tìm, tóm tắt nhiều thì dùng agent `nghien-cuu` (mô hình nhỏ, `tac-tu/nghien-cuu.md`); phần suy nghĩ và quyết định vẫn ở phiên chính.
- **Bước nhẹ:** skill ghi rõ bước nào nhẹ (chép, đổi tên, chạy lệnh có sẵn); tới đó nhắc một dòng "bước này nhẹ, bạn có thể đổi mô hình rẻ hơn", không tự đổi.
- **Việc thử của AI** đặt tên riêng (`thu-…`) và chỉ thao tác trên việc đó; trước khi tắt hay chạy lại thứ dùng chung (render, tiến trình nền), kiểm có việc của David hoặc phiên khác đang chạy không, có thì hỏi trước.
- **Không dùng mod giao diện:** không cài mod, plugin vẽ bảng hay thanh tiến độ, dòng trên ô nhập; chỉ giữ plugin Telegram; muốn mod mới thì hỏi David trước.
- **Sửa thứ dùng chung** (script lịch, bot, hook): báo trước một dòng, giữ bản cũ chạy được tới khi bản mới đã thử.
- Không đăng bài (chỉ chuẩn bị gói đăng, David tự đăng); gửi tin, xoá ngoài quy trình dọn, mật khẩu: `AGENTS.md` quy tắc 4.

## 4. Cuối việc
1. **Soát:** đối chiếu "Xong khi"; chạy `bash tu-dong-hoa/soat-sau-viec.sh` (liên kết, cây quy trình, cổng gốc, quét bí mật, ngôn từ, chồng chéo, bài kiểm, cú pháp mã); đổi tên, đổi cấu trúc, đổi luồng thì chạy thử trọn một quy trình thật (video: `tu-dong-hoa/thiet-bi-khac/kiem-tra-thiet-bi.sh`); việc sửa hàng loạt thì đề nghị một AI chưa tham gia soát diff (David cho phép agent phụ, mục 3).
2. **Người khác làm lại được từ GitHub:** quét thư mục tạm của phiên và bộ nhớ riêng của AI; script, mẫu, cách làm, luật vừa dùng ra kết quả mà repo chưa có thì đưa vào đúng skill (file và một dòng chỉ đường trong SKILL.md hoặc khối), thay phần ghi cứng của một máy bằng phần tự nhận máy. Tự hỏi: "một phiên mới chỉ đọc repo có làm ra đúng kết quả này không?"
3. **Ghi sổ:** góp ý của David sửa vào đúng nguồn duy nhất và một dòng nhật ký thay đổi của skill; lỗi David phải sửa thì thêm một câu kiểm (`co-so-tri-thuc/bai-kiem/de.json` hoặc bộ kiểm video); lời David mới vào sổ (tầng 3) và cách làm (tầng 2); file tầng 0 thay đổi thì ghi `co-so-tri-thuc/so-dan-chung-goc.md`. Chỉ luật dùng chung cho nhiều skill mới vào `co-so-tri-thuc/bo-nho/`; có ghi nhớ gần giống thì sửa ghi nhớ đó, không tạo cái mới. `co-so-tri-thuc/david.md` chỉ ghi điều cố định đã chốt; ý tưởng, góp ý đang cân nhắc ghi `du-an/danh-sach-y-tuong.md` (hoặc file `du-an/` phù hợp), David chốt rồi mới đưa vào `david.md` (Đ3).
4. **Đo chồng chéo** sau mỗi việc có sửa bản luật: `python3 -I ky-nang/tai-cau-truc/do-chong-cheo.py`; báo "NÊN NÂNG CẤP" thì nhắc David một dòng; David đồng ý thì nâng cấp cả bộ não một đợt (`hoc-lien-tuc` Việc 4).
5. **Cập nhật file theo dõi:** `bao-cao-trang-thai.md` (chỉ việc còn sống), file `du-an/` liên quan, bản đồ nội dung `ban-do/` khi có file mới; kiến thức đáng giữ vào `co-so-tri-thuc/kien-thuc/`, nối tới ý tưởng, dự án, skill liên quan.
6. **Báo cáo ngắn, tiếng Việt:** đã làm gì · đã kiểm gì · chưa kiểm gì · điều cần David xác nhận · hai tới ba dòng so với hình mẫu (giống ở đâu, khác ở đâu, nên chỉnh gì). Học thêm được gì về hình mẫu hay về David thì ghi bản đồ hình mẫu và nhật ký của nó.
7. **Báo lên Telegram** (Mac chính) khi xong một việc trọn vẹn (render xong, đăng xong, sửa bộ não xong) hoặc khi vướng cần David quyết, không báo sau mỗi lượt: `bash tu-dong-hoa/so-tay/bao-cao.sh "✅ Xong: … · Ở đâu: … · Còn lại: …"` hoặc `"❓ Chờ anh: …"`, tối đa 5 dòng; việc giao qua Telegram mở đầu bằng số việc `#N`. Máy chỉ dựng video (`~/.claude/vai-may` ghi `chi-video`) không có `bao-cao.sh`: báo trong chat. Chi tiết: `tu-dong-hoa/so-tay/README.md` (Mac chính).
8. **Dọn thiết bị sau khi David duyệt** (video): render xong chạy `cho-dang.sh gui`; David nói "chốt" thì `don-tap.py --xoa` rồi `luu-drive.sh` (chép cả tập lên Drive, so khớp, mới xoá); "đã đăng <tập>" thì `cho-dang.sh xong`; không tự xoá bằng `find … -delete` (`-delete` làm mất tác dụng `-prune`, ngày 20/11/2026 đã xoá mất bản gốc DJI_0030). Thiết bị chỉ giữ bản cuối chưa đăng ở `~/Movies/cho-dang/<tập>/`; bản gốc và dự án dựng chỉ ở Drive. Kiểm nhanh trên Mac chính: trang `localhost:8765/mac` hoặc `python3 tu-dong-hoa/kiem-video-mac.py` (chỉ đọc); David nói "kiểm video" thì chạy lệnh này, "dọn Mac" thì chạy `luu-drive.sh` cho các dự án đã chốt. File tải về, dữ liệu ứng dụng, đồ cá nhân không đồng bộ: muốn xoá thì hỏi trước. Chi tiết: `san-xuat-video/quy-tac-chung.md` mục 8, ghi nhớ `video-chuyen-qua-drive`.
9. **Đẩy GitHub:** `bash tu-dong-hoa/dong-bo.sh --push`; David nói "cập nhật não" cũng chạy lệnh này.

## 5. Giữ phiên gọn

| Khi | AI làm |
|---|---|
| Việc tiếp theo lớn, hoặc David đưa việc mới khác hẳn việc đang làm | Đề nghị mở phiên mới, ghi sẵn bước tiếp ở file theo dõi |
| Phiên đã dài, hoặc đã tự tóm tắt mà việc chưa xong | Viết lời bàn giao trong một khung để dán vào phiên mới: đã xong · còn lại theo thứ tự · file ở đâu · đã chốt kèm lý do |
| Việc chính của phiên đã xong hoàn chỉnh (đã lưu file, đã đẩy GitHub) | Hỏi David một dòng "Xong rồi, đóng phiên này nhé?"; David đồng ý thì đóng (việc `#N`: `giao-viec.sh --dung N`, Mac chính) |
| David quay lại phiên cũ sau nhiều giờ để làm việc mới | Đề nghị phiên mới, vì phiên cũ nạp lại tốn hơn |
| Tin nhắn thiếu một trong ba điều: việc gì, file nào, muốn ra cái gì | Tự suy từ tài nguyên và skill (mục 2); chỉ hỏi khi không đoán được việc gì |
| David dán nhật ký hoặc văn bản dài | Vẫn làm; cuối việc nhắc lần sau chỉ cần đưa đường dẫn file |
| Tới bước nhẹ | Nhắc đổi mô hình rẻ hơn (mục 3) |
| Buổi nhìn lại cuối tuần, hoặc `co-so-tri-thuc/bo-nho/` quá 40 ghi nhớ | Đề nghị "dọn bộ nhớ" (skill `consolidate-memory`) |
| Công cụ đo chồng chéo báo "NÊN NÂNG CẤP", hoặc đã có ít nhất 10 video có số liệu từ lần nâng cấp trước | Nhắc một dòng (mục 4) |
| Vòng tuần quá 7 ngày (`dong-bo.sh` nhắc) | Chạy `bash tu-dong-hoa/hoc-lien-tuc/vong-tuan.sh` rồi làm `hoc-lien-tuc` Việc 1 |
| David hỏi phiên tốn vào đâu | Chạy "giải thích mức dùng" (skill `explain-usage`) |

**Thói quen của David** (để AI biết mà nhắc): mỗi việc một phiên · xong thì "cập nhật não" rồi đóng · làm liền một mạch · nói đủ việc, file, kết quả trong một tin nhắn · gộp việc nhỏ · trả lời gộp ("đồng ý cả 5", chỉ nêu câu muốn đổi) · đưa đường dẫn thay vì dán · nói "chỉ chụp 2–3 khung" khi muốn kiểm nhanh.
