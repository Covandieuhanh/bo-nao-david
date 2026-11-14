# Kế hoạch Obsidian: bộ nhớ có liên kết cho Claude

> Lập 14/11/2026 theo lời David: "tôi sẽ trao đổi rất nhiều và dần dần sẽ cần lưu trữ và truy xuất lượng lớn thông tin. Tôi chỉ làm việc trực tiếp với Claude, còn làm việc với Obsidian sẽ là Claude, nên làm sao để Obsidian hỗ trợ Claude tối đa."
> Trạng thái: **chờ David duyệt từng phần** (Mục tiêu → Kế hoạch → Quy trình → Thực thi). Chưa làm gì.

---

## 1. Mục tiêu

**Gốc rễ:** cái giúp Claude là **mạng lưới liên kết viết trong file** (bản đồ, thẻ, đường nối `[[...]]`). Obsidian là công cụ dựng, giữ và hiển thị mạng lưới đó. David chỉ nói chuyện với Claude; Claude là người ghi, nối và tra.

| # | Mục tiêu | Đo bằng |
|---|---|---|
| 1 | **Tra nhanh, ít token, ít sót** khi dữ liệu lớn dần | Bộ 10 câu hỏi thử: số file phải mở và token, đo trước / sau. Đích: giảm ≥ 40%, không câu nào sót file đúng |
| 2 | **Không còn file rời rạc**: mọi ghi chú nối vào mạng | File mồ côi (không link vào hay ra) = 0; link gãy = 0 |
| 3 | **Trao đổi có giá trị được giữ lại**, kể cả phần Claude giải thích (hiện máy gom đêm chỉ lấy lời David) | Cuối phiên có kiến thức mới thì có ghi chú tương ứng, nối vào bản đồ |
| 4 | **Dựng lại 100% từ GitHub** (luật 6) | Máy khác clone repo là có đủ vault, cấu hình, máy kiểm |
| 5 | **David không phải làm gì thêm** | David không cần mở Obsidian; mở ra thì thấy bản đồ rõ ràng |

---

## 2. Kế hoạch (thiết kế)

**Vault = chính thư mục `bo-nao-david`.** Không dời file, không đổi tên hàng loạt, Git và GitHub giữ nguyên.

### 2.1 Bốn lớp của mạng lưới

| Lớp | Là gì | Giúp Claude thế nào |
|---|---|---|
| **Chỉ mục tự sinh** `co-so-tri-thuc/chi-muc.md` | Máy tự sinh: mỗi ghi chú một dòng (tên, mô tả một câu, thẻ, nối tới đâu) | **Lớp tiết kiệm token nhất**: đọc một file là biết kho có gì, mở thẳng đúng file, không tìm dò |
| **Bản đồ nội dung** (Map of Content) `ban-do/` | Trang gốc theo chủ đề: ba hướng nghề, khách, nội dung, skill, ghi nhớ, công cụ… mỗi trang trỏ tới các ghi chú thuộc nó, kèm một câu vì sao | Đi theo chủ đề thay vì đoán từ khoá |
| **Thẻ đầu file** (frontmatter) | `loai`, `huong`, `trang-thai`, `ngay`, `mo-ta` | Lọc nhanh: "mọi quyết định hướng tài chính còn hiệu lực" |
| **Đường nối `[[...]]`** | Nối giữa các ghi chú liên quan (luật ↔ ghi nhớ ↔ skill ↔ dự án ↔ kiến thức) | Mối liên quan được ghi rõ, không phải suy đoán; các phiên nối giống nhau |

### 2.2 Ghi chú kiến thức mới: `co-so-tri-thuc/kien-thuc/`

- Mỗi khái niệm **một ghi chú nhỏ** (ví dụ `telegram-bot.md`, `telegram-mini-app.md`, `obsidian.md`), không gom thành file dài.
- Cuối phiên, nếu có kiến thức đáng giữ (cả lời Claude giải thích), Claude ghi hoặc bổ sung đúng ghi chú, nối vào bản đồ và ý tưởng liên quan. Luật này ghi vào `ky-nang/chuan-muc-lam-viec.md` mục 4 (một nhà, không ghi hai chỗ).
- Ghi chú mới dùng mẫu sẵn (thẻ + phần "Liên quan").

### 2.3 Máy giữ mạng lưới: `tu-dong-hoa/kiem-tra-lien-ket.py`

- Tìm link gãy, file mồ côi, file thiếu thẻ; sinh lại `chi-muc.md`.
- Chạy trong `dong-bo.sh` trước mỗi lần đẩy, giống `quet-bi-mat.py`. Link gãy thì báo, không đẩy.
- Đổi tên hay gộp file: máy sửa link theo.

### 2.4 Tra theo nghĩa (giai đoạn sau, chỉ khi cần)

Khi kho vượt khoảng 1.000 ghi chú, hoặc bộ câu hỏi thử bắt đầu sót: thêm tìm theo nghĩa. Hai đường, chọn bằng số đo lúc đó: (a) app Obsidian + plugin tìm theo nghĩa + MCP nối vào Claude; (b) script chỉ mục theo nghĩa chạy thẳng trên file, không cần mở app. **Chưa làm bây giờ.**

### 2.5 Dữ liệu riêng không lên GitHub

Sổ tay, danh bạ, tin nhắn, kho dữ liệu ở `~/Documents/2-ca-nhan/so-tay/` có thể thành **vault riêng thứ hai**, cùng quy ước, chỉ ở máy, không lên GitHub. Phần này đụng quyền riêng tư nên **David chốt** (câu 1 dưới).

### 2.6 App Obsidian

Cấu hình vault `.obsidian/` (plugin, cài đặt) lên GitHub để dựng lại được; bỏ file trạng thái màn hình. Cài app chỉ để David xem bản đồ khi muốn: Claude **không cần app** cho lớp 1–4. Tải và cài app sẽ hỏi David trước.

### Câu David cần chốt

1. Sổ tay riêng (`2-ca-nhan/so-tay`) có làm vault thứ hai chỉ trên máy không? Đề xuất: **có**, vì danh bạ, tin nhắn, ý tưởng là phần sẽ lớn nhanh nhất.
2. ~~Có cài app Obsidian không?~~ David đã rõ (14/11): liên kết và bộ quy tắc liên kết nằm trong file, **không cần app**; app chỉ để mở xem bản đồ cho vui, cài hay không tuỳ lúc David muốn.

---

## 3. Quy trình (từng giai đoạn, mỗi giai đoạn xong báo David một dòng)

| GĐ | Việc | Xong khi |
|---|---|---|
| 0 | **Đo trước**: soạn 10 câu hỏi thử từ việc thật, ghi số file mở và token | Có bảng số đo gốc trong file này |
| 1 | **Quy ước + máy**: thêm thuật ngữ vào bảng thuật ngữ, mẫu ghi chú, `kiem-tra-lien-ket.py`, `chi-muc.md` tự sinh, gắn vào `dong-bo.sh` | Máy chạy, báo đúng số link gãy / mồ côi hiện tại |
| 2 | **Nối kho hiện có** (232 file), theo nhóm: ghi nhớ → cơ sở tri thức → dự án → skill → còn lại; thêm thẻ, dựng `ban-do/` | Mồ côi = 0, link gãy = 0 |
| 3 | **Luồng ghi kiến thức cuối phiên**: sửa `chuan-muc-lam-viec.md` mục 4; tạo ghi chú đầu tiên (Telegram, Obsidian) | Phiên thử ghi đúng ghi chú, nối đúng bản đồ |
| 4 | **Vault riêng** (nếu David đồng ý câu 1) + **app Obsidian** (nếu David đồng ý câu 2) | Mở được cả hai vault; cấu hình lên GitHub |
| 5 | **Đo sau**: chạy lại 10 câu hỏi, so với GĐ 0 | Báo David số giảm token và số file sót |
| 6 | (Sau này) Tra theo nghĩa, khi số đo cho thấy cần | — |

---

## 4. Thực thi (checklist)

**GĐ 0, đo trước**
- [ ] Soạn 10 câu hỏi thử (mỗi hướng nghề, ghi nhớ, skill, dự án, ý tưởng)
- [ ] Ghi file đúng cho từng câu
- [ ] Chạy thử, ghi số file mở + token vào bảng

**GĐ 1, quy ước + máy**
- [ ] Thêm thuật ngữ (Map of Content → Bản đồ nội dung `ban-do`, Index → Chỉ mục `chi-muc`, Knowledge Note → Ghi chú kiến thức `kien-thuc`, Vault → Kho ghi chú) vào `bang-thuat-ngu.md`
- [ ] Viết mẫu ghi chú (thẻ + "Liên quan")
- [ ] Viết `kiem-tra-lien-ket.py`: link gãy, mồ côi, thiếu thẻ
- [ ] Thêm phần sinh `chi-muc.md`
- [ ] Gắn vào `dong-bo.sh` trước bước đẩy
- [ ] Chạy lần đầu, ghi con số hiện trạng

**GĐ 2, nối kho hiện có**
- [ ] Nhóm ghi nhớ `bo-nho/` (~50 file): thẻ + nối
- [ ] Nhóm `co-so-tri-thuc/` còn lại
- [ ] Nhóm `du-an/`
- [ ] Nhóm `ky-nang/`
- [ ] Phần còn lại (`nghien-cuu/`, `tai-lieu-tham-khao/`, `tu-dong-hoa/`, file gốc)
- [ ] Dựng `ban-do/`: trang gốc + từng chủ đề
- [ ] AGENTS.md trỏ tới `chi-muc.md` + `ban-do/` (Claude đọc đầu phiên)
- [ ] Máy kiểm báo 0 / 0

**GĐ 3, luồng ghi kiến thức**
- [ ] Sửa `chuan-muc-lam-viec.md` mục 4: cuối phiên ghi kiến thức mới vào `kien-thuc/`
- [ ] Ghi chú `telegram-bot.md`, `telegram-mini-app.md`, `obsidian.md`, nối với ý tưởng số 3
- [ ] Thử một phiên thật, kiểm ghi chú sinh ra

**GĐ 4, vault riêng + app** (chờ David chốt câu 1, 2)
- [ ] Vault `so-tay`: thẻ + nối + chỉ mục riêng, không lên GitHub
- [ ] Hỏi David trước khi tải app Obsidian; cài, mở hai vault
- [ ] Đưa `.obsidian/` lên GitHub (bỏ `workspace*.json`), ghi cách cài vào `huong-dan-cai-dat.md`

**GĐ 5, đo sau**
- [ ] Chạy lại 10 câu hỏi, so bảng
- [ ] Báo David một dòng; cập nhật `bao-cao-trang-thai.md`
