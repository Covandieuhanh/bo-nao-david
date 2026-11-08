# Thói quen làm việc chung — mọi skill đọc file này trước

Chốt 08/11/2026 (`dang-lam/chuan-hoa-skill.md`, vòng 2). Mục tiêu: làm đúng quy trình, ra đúng ý ngay lần đầu, không tốn token vô ích.
File này giữ các thói quen **dùng chung cho mọi skill**. Luật riêng của từng việc nằm trong skill đó; luật riêng của video nằm ở
`dung-video/luat-chung.md`. Mỗi luật chỉ nằm một chỗ; chỗ khác chỉ trỏ về đây.

## 0. Khi hai điều ngược nhau
1. **Chất lượng thắng tiết kiệm** ("kết quả hơn tốc độ"). Chỉ tiết kiệm ở chỗ không đổi kết quả.
2. **Lời David vừa nói > bên có ngày chốt gần nhất > bên cũ hơn.** Trước 08/11/2026 các skill không nối với nhau, nên chỗ lệch là do
   chỗ đó chưa được cập nhật, không phải ý David.
3. Luật còn mơ hồ → xem **sản phẩm mới nhất David đã duyệt** làm chứng cứ, rồi hỏi nếu vẫn chưa rõ.

## 1. Đầu việc: đọc đúng phần cần
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
- Ngoại lệ được tự chọn, không hỏi trước (David đã chốt): cắt highlight, làm lại video cũ. Vẫn báo rõ đã chọn gì để David sửa.

## 3. Trong lúc làm
- **Lệnh theo lô:** các lệnh không phụ thuộc nhau gộp vào một lần gọi. Lệnh > 2 phút chạy nền, không thăm dò; render nối tiếp, không song song.
- **Chụp kiểm có giới hạn:** chụp đúng mốc dễ lỗi (khung mới lần đầu, chỗ chồng lớp, mối cắt, màn chốt, thẻ cuối, chỗ David góp ý),
  không chụp từng cảnh. Xem bố cục thì dùng ảnh thu nhỏ.
- **Agent phụ** chỉ khi David cho phép.
- **Bước nhẹ:** skill ghi rõ bước nào nhẹ (chép, đổi tên, chạy lệnh có sẵn). Tới đó nhắc một dòng "bước này nhẹ, bạn có thể đổi
  mô hình rẻ hơn" — không tự đổi.
- **Không tự render lại** sau góp ý: chỉ sửa skill, kịch bản; render khi David nói "render".
- Không đăng, không gửi, không xoá khi David chưa duyệt. Không nhập mật khẩu thay David.

## 4. Cuối việc
- **Báo cáo ngắn, tiếng Việt:** đã làm gì · đã kiểm gì · chưa kiểm gì · điều cần David xác nhận.
- **Góp ý của David ghi đúng một chỗ:** sửa skill hoặc khối bị ảnh hưởng + một dòng nhật ký (`changelog` của skill, hoặc mục "Nhật ký").
  Chỉ luật dùng chung cho nhiều skill mới vào `nao/bo-nho/`; đã có ghi nhớ gần giống thì sửa ghi nhớ đó, không tạo cái mới.
- **Cập nhật file theo dõi** (`dang-lam/…`, `TRANG-THAI-HIEN-TAI.md`) khi xong một đợt việc.
- **Đẩy GitHub ngay** khi có thay đổi về skill hoặc não: `bash scripts/sync.sh --push`.
- Việc tiếp theo lớn → đề nghị mở **phiên mới**, ghi sẵn bước tiếp ở file theo dõi để phiên mới không phải tìm lại.
