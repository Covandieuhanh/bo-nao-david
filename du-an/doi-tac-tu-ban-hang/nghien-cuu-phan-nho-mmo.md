# Nghiên cứu kênh TikTok "Phan Nho MMO" (@phannhommo)

> Chỉ gồm nội dung của kênh này và các web bán hàng của họ (luật `david.md` mục 3.3). Phần áp dụng cho David nằm ở [README.md](README.md).
> Nguồn: chép lời đủ 84 video (28/11/2025 – 14/11/2026, ~108 phút) + đọc 3 web bán hàng, ngày 14/11/2026. Lời chép bằng Whisper nên có chỗ sai chữ; số liệu do kênh tự nói, chưa kiểm chứng.

## Họ là ai
- **Phan Đức Nho**, thương hiệu **Big Man Marketing**. Công ty ở phường Bắc Giang, tỉnh Bắc Ninh, đang tuyển nhân sự AI (nội dung, lập trình, editor). Làm MMO (kiếm tiền online) hơn 10 năm, từng làm agency chạy quảng cáo, booking.
- Kênh mở lại 28/11/2025 sau khi mất kênh cũ 400.000 follow. Hiện có 4.336 follow, 25.400 lượt thích.
- Hình thức video: ngồi nói hoặc quay màn hình bằng điện thoại, 30–180 giây, phần lớn là trả lời bình luận. Gần đây có thêm video giọng đọc AI theo kiểu tin công nghệ.

## Sản phẩm đang bán
| Sản phẩm | Là gì | Giá |
|---|---|---|
| **Tool Xào Video** (`xaovideo.webbanhang.io`, link trong bio) | Phần mềm cài máy: từ video thật tạo hàng loạt bản biến thể (cắt cảnh bằng AI, kịch bản, lồng tiếng, phụ đề) để chạy GMV Max hoặc làm affiliate. Không tính phí API theo video, khoá theo máy | dùng thử 3 ngày; 299k/tháng; 699k/3 tháng; 1,9tr/năm |
| **skillmau.com**: 11 skill dựng video | File `.SKILL.md` cho Claude Code, Antigravity, Codex: Remotion, vlog, talking-head, tóm tắt video dài, dựng tự động, video bản đồ bất động sản | 260k–399k/skill |
| **Agent Vận hành TikTok Shop** | 4 ca/ngày, 16 skill: quét đơn, báo cáo sáng, đề xuất tối ưu listing, soạn phản hồi đánh giá; chủ shop duyệt mới gửi | từ 1.990.000đ |
| **Khoá "Xây dựng hệ thống AI Agent"** | 3 buổi Zoom tối (19:30–22:30), tặng 8 agent làm sẵn, nhóm Zalo trọn đời | 1.450.000đ |
| **BigmanBot** (`bigmanbot.com`) | App máy tính miễn phí, giao diện như app nhắn tin: mỗi bot là một "liên hệ", có phòng chat chung. Bot chạy trên CLI claude / codex / grok bằng tài khoản của người dùng, dữ liệu lưu trên máy, kết nối ứng dụng qua Composio, gọi thoại với bot. Bản đám mây chạy 24/7 là **BigmanCloud** (trả phí) | app miễn phí; cloud trả phí |
| Trang "mẫu làm video" | Kho mẫu video AI + chatbot viết prompt + tool Veo3 | gói |
| Dịch vụ | Cài sẵn hệ thống chạy và chăm quảng cáo tự động, vận hành TikTok Shop / Shopee; cài skill dựng video lên máy khách, chỉnh theo ngành (ví dụ bất động sản) | báo giá riêng |
| Khác | Bán fanpage đã bật kiếm tiền; khoá "30 ngày vibe coding" (10 buổi Zoom); tìm đối tác in ấn để làm POD | — |

## Đội bot họ dựng để vận hành
Video tháng 10–11/2026 cho thấy cách họ làm việc:
- **Đội affiliate Hostinger** (hoa hồng 40%): bot lập kế hoạch → bot dựng video Remotion → bot đăng bài nuôi fanpage → bot quảng cáo → bot quản lý landing page. Luồng: chọn repo → kiểm chứng cài đặt → bài hướng dẫn + video → fanpage → đo đơn; chỉ chạy quảng cáo khi đo được đơn và chủ duyệt ngân sách.
- **Đội "Impact"**: bot quảng cáo, bot quản lý nội dung, bot quản lý web (sửa web, đưa lên GitHub). Bot tự tìm chương trình affiliate, tìm link đăng ký, dựng landing page, cài Pixel, postback.
- **Chăm quảng cáo Facebook 24/7**: tự cắt lỗ khi chi phí/đơn vượt 80.000đ ba ngày liền, tự tăng ngân sách, lên lịch bài, báo về Telegram. Họ nói đang chạy 28 chiến dịch.
- **Vận hành TikTok Shop / Shopee**: nhiều bot trao đổi với nhau, chạy trên VPS nên tắt máy vẫn chạy; mời nhà sáng tạo vào sự kiện 11/11.
- Đang dựng giao diện "doanh nghiệp một người": sơ đồ đội 3D, bảng KPI, dùng được với nhiều loại agent.

## Ý tưởng và cách nghĩ về kinh doanh (lời họ nói)
1. **Doanh nghiệp một người**: sợ quản trị, sợ trả lương cho đội đông, nên chuyển sang một người điều phối nhiều AI agent chạy 24/7.
2. **Viết tool giờ rẻ mạt** vì ai cũng vibe code được. Giá trị nằm ở **chuyên môn và kinh nghiệm** đưa vào tool, ở **tệp khách**, và ở **năng lực vận hành** tool. Bị sao chép là chuyện bình thường.
3. **Cách bán tool**: tìm ý tưởng (cộng đồng, Product Hunt) → làm landing page vẽ tính năng → ảnh demo bằng AI → mời đăng ký dùng thử, gom vào nhóm Zalo → đủ người mới làm → ra bản MVP sớm, sửa theo góp ý → buổi Zoom hướng dẫn kèm ưu đãi mua trong buổi (tháng / năm / vĩnh viễn).
4. **Dịch vụ cài đặt thắng phần mềm**: lấy repo miễn phí trên GitHub, sửa thành skill theo ngành khách, cài lên máy khách và hướng dẫn, khách trả tiền.
5. **Phần mềm tương lai phải có API / MCP** để AI điều khiển. Phần mềm chỉ cài cho một người dùng sẽ mất khách.
6. **Phễu**: tặng tool miễn phí hoặc dùng thử → "bình luận để nhận" / link bio → nhóm Zalo → bán gói, tư vấn, cài đặt.
7. Không dạy MMO đại trà, vì "dạy không ra tiền thì bị chửi". Thay vào đó tuyển nhân viên làm theo đúng quy trình của mình.

## Video nhiều view nhất
| View | Video | Chủ đề |
|---|---|---|
| 202.300 | Làm MMO ở nước ngoài xịn quá | đem công làm video sang bán ở thị trường nước ngoài |
| 195.900 | AI agent tiếp quản thiết kế kiến trúc | tin công nghệ, giọng đọc AI |
| 117.700 | Quả tăm huyền thoại | chuyện hack game ngày xưa → cần chuyên môn mới làm ra công cụ |
| 48.000 | Công cụ free xào video | tặng tool |
| 46.300 | Viết tool là nghề rẻ mạt | giá trị nằm ở chuyên môn |
| 40.000 | Nền tảng tải, dịch, lồng tiếng tự động | khoe tool |
| 37.200 | Tools ngon là được | lấy repo miễn phí, cài cho khách lấy tiền |
| 36.400 | Kèo MMO mới | fanpage bật kiếm tiền + Shopee affiliate |

Video quay màn hình đội bot (tháng 11/2026) chỉ được 300–5.600 view. Video nói thẳng một quan điểm về nghề, hoặc tặng công cụ, ăn view hơn video khoe hệ thống.

## Vùng xám trong nội dung của họ
Kênh có nhiều kèo sát lằn ranh chính sách nền tảng: "xào video" để tránh bị quét trùng lặp, re-up rồi "lách bản quyền", mua fanpage đã bật kiếm tiền, "page bơm", thuê "cổng" để lấy lại tài khoản bị khoá (họ nói 10–80 triệu), "lách" chính sách AI.
