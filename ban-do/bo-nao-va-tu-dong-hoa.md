---
description: Bản đồ bộ não và tự động hoá — luật, thói quen làm việc, quy ước liên kết và đặt tên, ghi nhớ quy tắc, cài đặt và đồng bộ GitHub, bot Sổ nhớ, lịch tự chạy, skill công cụ (hỏi, tự học, tái bản, tin nhắn, trình duyệt, trang cuộn), lưu trữ.
---

# Bộ não và tự động hoá

Gốc: [bản đồ bộ não](README.md).

## Luật và cách làm việc
- [AGENTS](../AGENTS.md) — Cửa vào cho mọi AI: thứ tự đọc, sáu luật, trỏ tới cây quy trình.
- [quy-trinh](../quy-trinh.md) — **Cây quy trình**: quy trình gốc 7 bước cho mọi việc, rồi nhánh, rồi lá (câu David hay nói, file quy trình, xong khi); công cụ kiểm tra `tu-dong-hoa/kiem-quy-trinh.py`.
- [CLAUDE](../CLAUDE.md) — Cấu hình Claude Code của repo, nạp AGENTS.md.
- [chi-dan-toan-cuc](../co-so-tri-thuc/chi-dan-toan-cuc.md) — Luật chung mọi phiên (bản gốc ~/.claude/CLAUDE.md).
- [tu-duy-goc](../co-so-tri-thuc/tu-duy-goc.md) — **Tư duy gốc (tầng 0)**: cách nghĩ khi làm mọi việc, bốn khối Bóc tách · Hành động (vòng kết quả hoặc vấn đề) · Học và thay đổi · Bản chất và kiểm sai; nguồn: [17 phiếu học](../tai-lieu-tham-khao/tu-duy-goc/README.md).
- [truc-tri-thuc](../co-so-tri-thuc/truc-tri-thuc.md) — **Trục tri thức (tầng 0)**: cách bộ não tiếp nhận, xử lý, học, nâng cấp mọi thông tin, dựng theo cách mô hình AI được làm ra (dữ liệu → chưng cất → phản hồi → đánh giá → ra bản).
- [bai-kiem toàn bộ não](../co-so-tri-thuc/bai-kiem/README.md) — Bộ đánh giá của trục: 18 tình huống từ chính lời David đã sửa; một trí tuệ nhân tạo chưa đọc gì làm bài, đạt ít nhất 17/18.
- [chuan-muc-lam-viec](../ky-nang/chuan-muc-lam-viec.md) — Nguyên lý làm việc chung mọi skill đọc trước (tầng 1): khi hai điều ngược nhau, đầu việc, có quy trình thì tự động hoàn toàn (chưa có thì duyệt bốn phần), trong lúc làm, cuối việc, giữ phiên gọn, tài liệu và nguồn.
- [quy-trinh-van-hanh-chung](../ky-nang/quy-trinh-van-hanh-chung.md) — Cách làm từng bước của chuẩn mực (tầng 2, cùng số mục): lệnh, mẫu bốn phần, câu báo, soát sau việc, ghi sổ, dọn dẹp thiết bị, push lên GitHub.
- [quy-uoc-lien-ket](../co-so-tri-thuc/quy-uoc-lien-ket.md) — Bộ quy tắc liên kết của bộ não — mô tả đầu file, đường nối, bản đồ nội dung, chỉ mục tự sinh, ghi chú kiến thức, công cụ kiểm tra; để Claude tra nhanh, ít token, không sót.
- [bang-thuat-ngu](../co-so-tri-thuc/bang-thuat-ngu.md) — Bảng thuật ngữ đặt tên: thuật ngữ kinh doanh tiếng Anh → tiếng Việt → tên file/thư mục dùng; tên bắt buộc của công cụ; cấu trúc thư mục.
- [chi-muc](../co-so-tri-thuc/chi-muc.md) — Chỉ mục tự sinh của bộ não — mỗi file .md một dòng (đường dẫn, mô tả, số file nối tới); Claude grep file này trước khi tìm toàn repo.

## Trạng thái và dự án của bộ não
- [bao-cao-trang-thai](../bao-cao-trang-thai.md) — Báo cáo trạng thái: việc đang làm chưa xong, việc chờ David quyết, câu hỏi còn mở, cảnh báo, việc phải nhớ.
- [du-an](../du-an/README.md) — Thư mục dự án: chỉ giữ file theo dõi việc làm chưa xong; dự án video và thành phẩm nằm ở thiết bị và Drive.
- [lien-ket-tri-thuc](../du-an/lien-ket-tri-thuc.md) — Dự án liên kết tri thức (14/11): biến bộ não thành mạng lưới file nối nhau để Claude tra nhanh, ít token; kế hoạch 4 phần và số đo trước / sau.
- [chuan-hoa-ten](../du-an/chuan-hoa-ten.md) — Bản đồ chuẩn hoá tên toàn bộ (14/11, đã xong): tên cũ đổi sang tên mới theo thuật ngữ kinh doanh tiếng Anh dịch sang tiếng Việt.
- [chuan-hoa-ky-nang](../du-an/chuan-hoa-ky-nang.md) — Dự án chuẩn hoá bộ skill theo thói quen làm việc chung (08/11): các bước, mốc commit, việc còn lại.
- [danh-gia-luat](../du-an/danh-gia-luat.md) — Rà soát luật bộ skill video (08/11), bước 1 của chuẩn hoá skill: luật trùng, lệch, cần gộp.
- [nang-cap-4](../du-an/nang-cap/nang-cap-4.md) — Nâng cấp 4 (20/11): công cụ đo đổi sang đo trùng / rối, video gần trùng 49 xuống 16.
- [nang-cap-5](../du-an/nang-cap/nang-cap-5.md) — Nâng cấp 5 (20/11): trục tri thức, gắn tầng, bộ kiểm toàn não, luật viết đủ từ.
- [tai-ban-3](../du-an/nang-cap/tai-ban-3.md) — Tái bản 3 toàn bộ bộ não (mở 14/11): theo dõi chung, file từng phiên con.
- [tai-cau-truc-2](../du-an/nang-cap/tai-cau-truc-2.md) — Tái bản lần 2 toàn bộ bộ não (10/11): điều phối các phiên con, mốc, kết quả.
- [tai-cau-truc-2-nao](../du-an/nang-cap/tai-cau-truc-2-nao.md) — Tái bản 2 (10/11), phần bộ não: AGENTS.md, CLAUDE.md, david.md, chuan-muc-lam-viec.
- [tai-cau-truc-2-hoi](../du-an/nang-cap/tai-cau-truc-2-hoi.md) — Tái bản 2 (10/11), phần bộ hỏi skill thu-thap-yeu-cau.
- [tai-cau-truc-2-ghi-nho](../du-an/nang-cap/tai-cau-truc-2-ghi-nho.md) — Tái bản 2 (10/11), phần dọn ghi nhớ bo-nho: gộp, bỏ, chuyển lưu trữ.

## Ghi nhớ quy tắc và bộ não (sổ quyết định)
- [MEMORY](../co-so-tri-thuc/bo-nho/MEMORY.md) — Mục lục bộ nhớ: mỗi ghi nhớ một dòng.
- [quy-tac-cong-cu-cai-dua-vao-ky-nang](../co-so-tri-thuc/bo-nho/quy-tac-cong-cu-cai-dua-vao-ky-nang.md) — Công cụ David đã tải/cài (ví dụ: pyannote) là để nâng skill — công cụ giúp việc tốt hơn thì Claude đưa thẳng vào skill dựng video, không để công cụ không được dùng (2026-11-07)
- [quy-tac-david-md-chi-dieu-co-dinh](../co-so-tri-thuc/bo-nho/quy-tac-david-md-chi-dieu-co-dinh.md) — co-so-tri-thuc/david.md chỉ ghi điều cố định đã chốt; ý tưởng, góp ý đang cân nhắc ghi ở du-an/danh-sach-y-tuong.md
- [quy-tac-duyet-ke-hoach-4-phan](../co-so-tri-thuc/bo-nho/quy-tac-duyet-ke-hoach-4-phan.md) — Có quy trình thì tự động hoàn toàn, cần đổi thì sửa quy trình; chưa có quy trình thì trình 4 phần, David duyệt rồi mới làm; việc tự chạy hiện thành phiên trong app.
- [quy-tac-goi-trainer-chung](../co-so-tri-thuc/bo-nho/quy-tac-goi-trainer-chung.md) — Gói trainer công nghệ chỉ dạy một kỹ năng thuần, cách làm chung bằng AI và máy của học viên; không tư duy, không chi tiết riêng của David
- [quy-tac-goi-y-de-david-chon](../co-so-tri-thuc/bo-nho/quy-tac-goi-y-de-david-chon.md) — Tài nguyên vào, kết quả ra: đã có quy trình nên Claude tự làm một mạch theo mặc định skill, ghi "đã chọn X vì Y", không hỏi.
- [quy-tac-hoc-la-bo-sung](../co-so-tri-thuc/bo-nho/quy-tac-hoc-la-bo-sung.md) — Học video mẫu mới là BỔ SUNG vào skill, không thay thế những gì David đã sửa; lỗi cũ đã sửa không được quay lại; số của khung dọc không dùng cho khung ngang (2026-11-08)
- [quy-tac-ket-qua-hon-toc-do](../co-so-tri-thuc/bo-nho/quy-tac-ket-qua-hon-toc-do.md) — David ưu tiên làm đúng quy trình và có kết quả hơn làm nhanh; bước nào cần kết quả render thì chờ, chỗ chưa rõ thì trao đổi (2026-11-05)
- [quy-tac-khong-tu-chay-viec-cua-david](../co-so-tri-thuc/bo-nho/quy-tac-khong-tu-chay-viec-cua-david.md) — Không tự chạy, chạy tiếp, dừng hay làm lại việc David tạo (render, việc dựng…) khi David chưa ra lệnh — kể cả khi chính Claude đã ngắt việc đó
- [quy-tac-ky-nang-tu-cai-tien](../co-so-tri-thuc/bo-nho/quy-tac-ky-nang-tu-cai-tien.md) — Sáu luật AGENTS 12/11/2026: skill, giọng văn, luật kênh tự học theo hình mẫu có số liệu, phần sửa tự chạy theo quy trình, báo sau; bỏ luật 'con người làm trung t…
- [quy-tac-khong-dung-mod-giao-dien](../co-so-tri-thuc/bo-nho/quy-tac-khong-dung-mod-giao-dien.md) — Không dùng mod giao diện: David gỡ hết savvy-progress, collision-guard, goal-meter, Sổ việc (13/11/2026)
- [quy-tac-noi-dung-cua-david](../co-so-tri-thuc/bo-nho/quy-tac-noi-dung-cua-david.md) — Vai trò chia rõ — David tự xây nội dung, nói tự do có cảm xúc; skill lo hình. Người xem làm trung tâm; học kênh lớn ở nhịp và cách trình bày (2026-11-05, gộp 10/11)
- [quy-tac-phien-telegram-tu-chay](../co-so-tri-thuc/bo-nho/quy-tac-phien-telegram-tu-chay.md) — Phiên việc giao qua Telegram: có quy trình thì tự làm tới kết quả (chưa có thì trình 4 phần), ghi sổ; chỉ hỏi khi đăng/gửi, tốn tiền, đẩy đè GitHub, xoá ổ đĩa; mọi phiên…
- [quy-tac-tu-duy-goc](../co-so-tri-thuc/bo-nho/quy-tac-tu-duy-goc.md) — Lời David đặt bộ tư duy gốc, khung cố vấn làm nền tảng, học từ những chuyên gia hàng đầu thế giới (23/11).
- [quy-tac-truc-tri-thuc](../co-so-tri-thuc/bo-nho/quy-tac-truc-tri-thuc.md) — Lời David chốt trục tri thức cố định cho việc kaizen bộ não (20/11).
- [quy-tac-sua-thang-tai-ban](../co-so-tri-thuc/bo-nho/quy-tac-sua-thang-tai-ban.md) — Đổi luật thì sửa thẳng câu cũ (không chồng câu "bổ sung/thay luật", không ngày trong bản luật); định kỳ tái bản TOÀN BỘ bộ não một đợt khi công cụ đo chồng chéo báo…
- [quy-tac-thu-bang-doan-ngan](../co-so-tri-thuc/bo-nho/quy-tac-thu-bang-doan-ngan.md) — Thử skill dựng video thì chỉ dùng một đoạn ngắn TRỌN VẸN MỘT Ý (không cố định số giây), không chạy cả video dài
- [quy-tac-tu-hoi-khi-mo-ho](../co-so-tri-thuc/bo-nho/quy-tac-tu-hoi-khi-mo-ho.md) — Tự nhận diện lúc cần hỏi David (câu mơ hồ / đọc chính tả lệch, mâu thuẫn luật, việc tốn kém khó đảo ngược…) — không tự đoán rồi làm
- [co-so-tri-thuc-github-ban-goc](../co-so-tri-thuc/bo-nho/co-so-tri-thuc-github-ban-goc.md) — GitHub bo-nao-david là bản gốc của bộ não — có gì mới cho skill/não thì ĐẨY NGAY (bắt buộc); chỉ giữ mẫu, form, luật, hồ sơ; sản phẩm ở lại máy/tài khoản làm ra nó
- [co-so-tri-thuc-ho-so-va-bo-loc](../co-so-tri-thuc/bo-nho/co-so-tri-thuc-ho-so-va-bo-loc.md) — Hồ sơ David ở ~/.claude/david.md (ba hướng nghề, mô hình kinh doanh); mọi tài nguyên phải qua bộ lọc khối 00 trước khi dựng; luật kênh ở ho-so-thuong-hieu/kenh.json
- [co-so-tri-thuc-quy-uoc-dat-ten](../co-so-tri-thuc/bo-nho/co-so-tri-thuc-quy-uoc-dat-ten.md) — Mọi tên file, thư mục, skill, ghi nhớ đi từ thuật ngữ kinh doanh tiếng Anh chuẩn, dịch đúng nghĩa sang tiếng Việt không dấu; tra bảng thuật ngữ
- [thiet-bi-bo-cuc-thu-muc](../co-so-tri-thuc/bo-nho/thiet-bi-bo-cuc-thu-muc.md) — Bố cục thư mục trên MacBook của David (dọn 07/11 và 11/11/2026, đổi tên 14/11) — Mac chỉ giữ việc đang làm, còn lại ở Drive; App notion đã bỏ (chỉ máy này, khôn…
- [co-so-tri-thuc-bo-nao-cong-ty](../co-so-tri-thuc/bo-nho/co-so-tri-thuc-bo-nao-cong-ty.md) — việc công ty Veltrix làm ở bộ não riêng ~/Documents/bo-nao-veltrix (kho private veltrix), Văn Phòng Shop đã chuyển vào

## Cài đặt, đồng bộ, GitHub
- [](../README.md) — Trang đầu repo trên GitHub.
- [huong-dan-cai-dat](../huong-dan-cai-dat.md) — Hướng dẫn cài đặt bộ não lên máy mới / nơi khác từ GitHub: lệnh cài, lối tắt, bot, lịch, cái gì không lên GitHub.

## Bot, lịch, công cụ trên máy
- [nghien-cuu](../tac-tu/nghien-cuu.md) — Đọc tài liệu dài, tìm thông tin trong file hay trên web, tóm tắt ngắn gọn bằng tiếng Việt. Dùng cho việc cần đọc hoặc tìm nhiều mà không cần ra quyết định; trả kết…

## Skill công cụ
- [thu-thap-yeu-cau](../ky-nang/thu-thap-yeu-cau/SKILL.md) — Cách hỏi khi trình 4 phần (Mục tiêu · Kế hoạch · Quy trình · Thực thi) trước việc chưa có quy trình — hỏi theo vòng từ góc nhìn chuyên gia thực chiến, mỗi điểm cần chốt…
- [hoc-lien-tuc](../ky-nang/hoc-lien-tuc/SKILL.md) — Tự học, cải tiến liên tục: nhìn lại tuần, học hình mẫu có số liệu, học thành skill, và Việc 4 **Nâng cấp** định kỳ cả bộ não (đo trước / sau, chưng cất, cắt giảm, tái cấu trúc).
- [nhat-ky-thay-doi hoc-lien-tuc](../ky-nang/hoc-lien-tuc/references/nhat-ky-thay-doi.md) — Nhật ký thay đổi skill hoc-lien-tuc và máy đếm / ghi tín hiệu.
- [hoc-lien-tuc 2026-11-15](../du-an/hoc-lien-tuc/2026-11-15.md) — Phiếu tự học tuần 15/11: điều lặp, đã sửa, gộp ghi nhớ 47 thành 40, việc tuần sau.
- [hoc-lien-tuc 2026-11-26](../du-an/hoc-lien-tuc/2026-11-26.md) — Phiếu tự học tuần 26/11: ba điều lặp, lỗi mã hoá trên Windows, đề xuất thăng cấp, các chỗ đã sửa.
- [tai-cau-truc](../ky-nang/tai-cau-truc/SKILL.md) — Dọn luật — bước 4 của Nâng cấp: mỗi luật một nguồn duy nhất, không ngày, không câu trùng; công cụ đo chồng chéo chỉ cảnh báo khi có trùng lặp / rối.
- [dieu-khien-trinh-duyet](../ky-nang/dieu-khien-trinh-duyet/SKILL.md) — Automate browser interactions, test web pages and work with Playwright tests.
- [thiet-ke-trang-cuon](../ky-nang/thiet-ke-trang-cuon/SKILL.md) — >
- [lich-su](../ky-nang/tai-cau-truc/lich-su.md) — Lịch sử nâng cấp (trước 20/11 gọi là tái bản): mỗi đợt một dòng, mốc cho công cụ đo chồng chéo.

**Tài liệu dieu-khien-trinh-duyet**
- [chay-ma](../ky-nang/dieu-khien-trinh-duyet/references/chay-ma.md) — Điều khiển trình duyệt: chạy mã Playwright tuỳ ý (run-code).
- [dinh-kem-pr](../ky-nang/dieu-khien-trinh-duyet/references/dinh-kem-pr.md) — Điều khiển trình duyệt: đính kèm ảnh chụp, video vào pull request bằng gh.
- [gia-lap-yeu-cau](../ky-nang/dieu-khien-trinh-duyet/references/gia-lap-yeu-cau.md) — Điều khiển trình duyệt: chặn, giả lập, sửa yêu cầu mạng (request mocking).
- [kiem-thu-playwright](../ky-nang/dieu-khien-trinh-duyet/references/kiem-thu-playwright.md) — Điều khiển trình duyệt: chạy bộ kiểm thử Playwright.
- [quan-ly-phien](../ky-nang/dieu-khien-trinh-duyet/references/quan-ly-phien.md) — Điều khiển trình duyệt: nhiều phiên trình duyệt tách biệt, giữ trạng thái.
- [quay-video](../ky-nang/dieu-khien-trinh-duyet/references/quay-video.md) — Điều khiển trình duyệt: quay video phiên tự động (WebM).
- [tao-kiem-thu](../ky-nang/dieu-khien-trinh-duyet/references/tao-kiem-thu.md) — Điều khiển trình duyệt: viết và sửa kiểm thử Playwright (plan → generate → heal).
- [theo-vet](../ky-nang/dieu-khien-trinh-duyet/references/theo-vet.md) — Điều khiển trình duyệt: ghi vết (trace) để gỡ lỗi.
- [thuoc-tinh-phan-tu](../ky-nang/dieu-khien-trinh-duyet/references/thuoc-tinh-phan-tu.md) — Điều khiển trình duyệt: xem thuộc tính phần tử DOM (id, class, data-*).
- [trang-thai-luu-tru](../ky-nang/dieu-khien-trinh-duyet/references/trang-thai-luu-tru.md) — Điều khiển trình duyệt: quản lý cookie, localStorage, trạng thái lưu trữ.

**Tài liệu thiet-ke-trang-cuon**
- [nhat-ky-thay-doi](../ky-nang/thiet-ke-trang-cuon/nhat-ky-thay-doi.md) — Sổ thay đổi skill thiết kế trang cuộn.
- [dau-hieu-nhan-dang](../ky-nang/thiet-ke-trang-cuon/mau/dau-hieu-nhan-dang.md) — Thiết kế trang cuộn: sổ dấu hiệu nhận dạng mỗi trang đã làm để không lặp.
- [bay-xuyen-the-gioi](../ky-nang/thiet-ke-trang-cuon/references/bay-xuyen-the-gioi.md) — Thiết kế trang cuộn: chế độ bay xuyên một thế giới liên tục (worldflight).
- [bo-suu-tap-da-duyet](../ky-nang/thiet-ke-trang-cuon/references/bo-suu-tap-da-duyet.md) — Thiết kế trang cuộn: chuẩn 10 trang đã duyệt.
- [cam-giac](../ky-nang/thiet-ke-trang-cuon/references/cam-giac.md) — Thiết kế trang cuộn: trục cảm xúc người xem đi qua trang.
- [chieu-sau-phan-dau](../ky-nang/thiet-ke-trang-cuon/references/chieu-sau-phan-dau.md) — Thiết kế trang cuộn: chiều sâu nhiều lớp cho phần đầu trang (hero).
- [gu-thiet-ke](../ky-nang/thiet-ke-trang-cuon/references/gu-thiet-ke.md) — Thiết kế trang cuộn: chuẩn tối thiểu về gu thẩm mỹ, người làm đọc trước khi viết mã.
- [kiem-chung](../ky-nang/thiet-ke-trang-cuon/references/kiem-chung.md) — Thiết kế trang cuộn: kiểm chứng desktop, điện thoại, giảm chuyển động.
- [tai-nguyen](../ky-nang/thiet-ke-trang-cuon/references/tai-nguyen.md) — Thiết kế trang cuộn: tạo ảnh, video bằng kie.ai và mã hoá để cuộn.
- [the-gioi](../ky-nang/thiet-ke-trang-cuon/references/the-gioi.md) — Thiết kế trang cuộn: chọn thế giới (định hướng nghệ thuật) của trang.
- [thiet-bi](../ky-nang/thiet-ke-trang-cuon/references/thiet-bi.md) — Thiết kế trang cuộn: 9 cách cuộn làm đổi trang (bộ thiết bị).
- [tinh-doc-ban](../ky-nang/thiet-ke-trang-cuon/references/tinh-doc-ban.md) — Thiết kế trang cuộn: trục cấu trúc, bài học từ 4 trang đã làm.

## Nghiên cứu về cách dùng AI
- [nghien-cuu](../nghien-cuu/README.md) — Thư mục nghiên cứu: tài liệu đã tra cứu để ra quyết định hoặc nâng cấp skill, số liệu nhanh lỗi thời.
- [hoc-tu-16-bai-hoc-1000-gio-claude-2026-11-14](../nghien-cuu/hoc-tu-16-bai-hoc-1000-gio-claude-2026-11-14.md) — Nghiên cứu bài 16 bài học sau 1000 giờ dùng Claude (Nhật Anh AI, 14/11): ý áp dụng cho bộ não.

## Lưu trữ (không làm theo)
- [co-so-tri-thuc-kho-bo-nao](../co-so-tri-thuc/bo-nho/luu-tru/co-so-tri-thuc-kho-bo-nao.md) — Repo riêng tư Covandieuhanh/bo-nao-david là bộ não dùng chung cho mọi AI; bản trên máy ở ~/Documents/bo-nao-david; "cập nhật não" nghĩa là chạy tu-dong-hoa/dong-bo.sh --push
- [video-chuan-am-luong](../co-so-tri-thuc/bo-nho/luu-tru/video-chuan-am-luong.md) — Chuẩn âm lượng chung David chốt cho mọi video: nhạc thấp hơn giọng khoảng 23 dB lúc nói, cả bài -14 LUFS; giọng nhỏ kéo lên, nhạc to hạ xuống (2026-11-06)
- [video-doc-ngan-khong-thanh](../co-so-tri-thuc/bo-nho/luu-tru/video-doc-ngan-khong-thanh.md) — Video dọc ngắn (Reels/TikTok/Shorts) bỏ thanh thời gian và thẻ cuối; màn chốt hiện chữ trên khung hình, kết ở chữ cuối để tự lặp (2026-11-10)
- [video-luon-co-do-hoa-chuyen-dong](../co-so-tri-thuc/bo-nho/luu-tru/video-luon-co-do-hoa-chuyen-dong.md) — Mọi video phải có motion graphics, tức là điểm nhấn kéo mắt người xem, NHIỀU LOẠI (không chỉ cảnh toàn màn hình): hình vẽ, chữ giải thích, biểu tượng, làm nổi người đang…
- [video-nguoi-xem-trung-tam](../co-so-tri-thuc/bo-nho/luu-tru/video-nguoi-xem-trung-tam.md) — Nguyên tắc định hướng của bộ skill video — người xem làm trung tâm; học kênh lớn ở nhịp và cách trình bày, giữ thẩm mỹ của David (04/11, sửa 08/11)
- [video-quy-trinh-dung-theo-phong-cach](../co-so-tri-thuc/bo-nho/luu-tru/video-quy-trinh-dung-theo-phong-cach.md) — Người dùng dựng video talking-head dọc theo phong cách mẫu bằng skill ~/.claude/skills/dung-video-theo-phong-cach; người dùng chỉ muốn đưa 2 video rồi nhận MP4 đăng ngay
- [thiet-bi-don-documents-2026-11-07](../co-so-tri-thuc/bo-nho/luu-tru/thiet-bi-don-documents-2026-11-07.md) — Ngày 07/11/2026 dọn ~/Documents, chỉ còn David.Claude + Obsidian + mk.csv; App notion đã bỏ, mở phiên ở ~/Documents/David.Claude
- [video-podcast-bia-khong-mat](../co-so-tri-thuc/bo-nho/luu-tru/video-podcast-bia-khong-mat.md) — Lưu trữ: đã gộp vào video-chi-hinh-cua-chinh-video.
- [video-khong-nhan-ky-thuat](../co-so-tri-thuc/bo-nho/luu-tru/video-khong-nhan-ky-thuat.md) — Lưu trữ: đã gộp vào video-chu-nguyen-van.
- [video-hieu-hon-cau-ki](../co-so-tri-thuc/bo-nho/luu-tru/video-hieu-hon-cau-ki.md) — Lưu trữ: đã gộp vào video-tham-my-chi-giu-nhan-dien.
- [video-khong-cai-hyperframes](../co-so-tri-thuc/bo-nho/luu-tru/video-khong-cai-hyperframes.md) — Lưu trữ: đã gộp vào video-bo-ung-dung.
- [video-ban-chuan-2026-11-06](../co-so-tri-thuc/bo-nho/luu-tru/video-ban-chuan-2026-11-06.md) — Lưu trữ: đã gộp vào video-kien-truc-ky-nang.
- [video-thu-muc-xep-theo-tap](../co-so-tri-thuc/bo-nho/luu-tru/video-thu-muc-xep-theo-tap.md) — Lưu trữ: đã gộp vào video-chuyen-qua-drive.
- [video-chu-nhan-nhan-dan](../co-so-tri-thuc/bo-nho/luu-tru/video-chu-nhan-nhan-dan.md) — Lưu trữ: đã gộp vào video-nhan-dien-chung.

## Phần riêng Mac chính
- Bot Telegram, lịch tự chạy, trang xem kết quả, công cụ chỉ Mac, lưu trữ cũ: bản đồ `rieng-mac/ban-do.md` (chỉ có trên Mac chính, repo riêng tư `bo-nao-david-mac`).
