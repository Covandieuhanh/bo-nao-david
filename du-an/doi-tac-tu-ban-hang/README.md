# Văn Phòng Shop: đội AI cho người bán hàng online

Ứng viên **gói công nghệ thứ 2** của hướng 3 (`co-so-tri-thuc/chien-luoc-nghe-nghiep.md` mục 4.1). Gói 1 vẫn là dựng video bằng AI; gói này chưa chốt, ghi ở `du-an/danh-sach-y-tuong.md` #3.
Hình mẫu tham khảo: [nghien-cuu-phan-nho-mmo.md](nghien-cuu-phan-nho-mmo.md) (BigmanBot, Agent TikTok Shop). Bản mẫu giao diện: [ban-mau.html](ban-mau.html).

## Mục tiêu
Chủ shop online nhỏ (1–5 người, bán trên TikTok Shop, Shopee, fanpage) **nhắn tin với từng AI như nhắn Zalo**. Mỗi AI làm một việc. Việc gửi ra ngoài, tiêu tiền hay đăng bài thì phải chờ chủ shop duyệt. David kèm từng bước tới khi shop **tự vận hành được đội AI** (thước đo `david.md` mục 1: khách tự đứng được).

Kết quả của gói, đo được sau 14 ngày dùng thử với 1 shop:
- Chủ shop đỡ **≥ 1 giờ/ngày** việc lặp lại (tự ghi giờ trước và sau).
- Báo cáo sáng có đều **14/14 ngày**. Chủ shop duyệt việc trong **≤ 10 phút/ngày**.
- Chủ shop tự giao được việc mới cho AI mà không cần hỏi David.

**Điểm khác hình mẫu:** họ bán tool và agent rồi để khách tự mò. David bán **đội AI + đào tạo tới khi ra kết quả**, có AI "Hướng" (huấn luyện viên) giải thích lý do cho mỗi đề xuất. Chỉ dùng cách làm hợp lệ: không xào video để né quét, không re-up, không mua page (lằn ranh 4.7).

## Kế hoạch
| Giai đoạn | Làm gì | Xong khi |
|---|---|---|
| **0. Bản mẫu** | Trang chat 9 ô (8 AI + phòng chung), dữ liệu minh hoạ, AI trả lời thật theo vai | ✅ 14/11: [ban-mau.html](ban-mau.html) |
| **1. Bản 0 cho 1 shop** | Chỉ chạy **3 AI**: Chi (báo cáo sáng), Lan (soạn trả lời khách), An (lãi thật). Dữ liệu lấy từ file xuất của sàn / Google Sheets, chưa nối API sàn | shop thử dùng 7 ngày liền |
| **2. Nối thêm** | Thêm Minh (đơn, kho), Vy (nội dung), Khoa (quảng cáo); có lịch chạy, phòng chung gọi @tên | đạt 3 kết quả ở mục tiêu |
| **3. Đóng gói bán** | Gói = cài đội AI + 4 buổi đào tạo + 14 ngày kèm; chốt giá từ số liệu bán thử | có khoản thu đầu tiên |

**Đã chọn** (đổi được khi David muốn):
- **Bắt đầu 3 AI, chưa đủ 8**: shop nhỏ chưa cần đủ đội, ít AI thì dễ đo cái nào có ích.
- **Chưa nối API sàn ở bản 0**: xin API TikTok Shop khó (chính hình mẫu cũng đang kẹt chỗ này). File xuất + Sheets đủ để chứng minh giá trị.
- **Phần chạy sau dùng Claude** (Agent SDK hoặc Claude Code chạy trên VPS, mỗi AI = hồ sơ vai + skill + lịch), cách đã chạy thật trong bộ não David. App như BigmanBot chỉ để tham khảo giao diện, không dựng trên đó.
- **Mỗi AI có hồ sơ 4 dòng**: việc làm · lịch chạy · quyền ("tự làm" hay "cần duyệt") · cách nói. Bản mẫu đã có đủ cho 8 AI.

## Quy trình
**Dựng một AI (lặp cho từng AI):**
1. Ngồi cùng chủ shop 20 phút: việc gì lặp lại mỗi ngày, mất bao lâu, làm tay ra sao.
2. Viết hồ sơ AI: việc làm, lịch chạy, quyền, cách nói, mẫu trả lời đúng ý chủ shop.
3. Nối dữ liệu: file xuất / Sheet / hộp thư, chỉ quyền đọc trước.
4. Chạy song song 3 ngày: AI soạn, người vẫn làm tay, so kết quả.
5. Đạt thì bật lịch chạy. Việc đọc thì để AI tự làm; việc gửi, tiêu tiền thì giữ ở "cần duyệt".
6. Cuối tuần, AI Hướng cùng chủ shop nhìn lại: được gì, kẹt đâu, tuần sau giao thêm việc gì.

**Bán (theo `du-an/pheu-ban-hang-goi-cong-nghe.md`):** nội dung phễu cho thấy đội AI chạy thật → trò chuyện 20 phút → bán thử 1–3 shop → chốt giá.

## Thực thi (checklist)
- [x] Xem 84 video kênh mẫu, tổng kết sản phẩm, ý tưởng (14/11)
- [x] Bản mẫu giao diện chat từng AI, có AI trả lời thật (14/11)
- [ ] David mở bản mẫu, nhắn thử 3 AI, ghi chỗ muốn sửa
- [ ] David chốt: có làm gói 2 này không, hay để sau gói 1 (`danh-sach-y-tuong.md` #3)
- [ ] Chọn 1 shop quen để thử (người bán mỹ phẩm, thời trang… đang bán TikTok Shop / Shopee)
- [ ] Hỏi shop đó 20 phút: 3 việc lặp lại mất thời gian nhất
- [ ] Viết hồ sơ thật cho Chi, Lan, An theo câu trả lời của shop
- [ ] Hỏi người lập trình của David: dựng phần chạy sau (VPS + Claude) cho 3 AI, mất bao lâu, tốn bao nhiêu/tháng
- [ ] Chạy song song 3 ngày, ghi giờ trước/sau
- [ ] 14 ngày dùng thử, đo 3 kết quả, xin lời chứng
- [ ] Chốt giá. Mốc tham khảo thị trường: agent vận hành TikTok Shop 1,99 triệu, khoá 3 buổi 1,45 triệu (kênh mẫu)
