---
description: "Tái bản 2 (10/11), phần bộ não: AGENTS.md, CLAUDE.md, david.md, chuan-muc-lam-viec."
---

# Tái bản 2 — bộ nao

Bộ gồm: `AGENTS.md` · `CLAUDE.md` · `co-so-tri-thuc/david.md` · `ky-nang/chuan-muc-lam-viec.md`. Sổ: lịch sử git và `co-so-tri-thuc/bo-nho/`.

Công cụ đo lúc mở: `dau_ngay 17/15 · ghi_de 2/6 · trung 0/4 · sua 19/25 · dong 276/600` nghĩa là vượt ngưỡng dấu ngày.
Công cụ đo sau khi viết lại: `dau_ngay 3/15 · ghi_de 0/6 · trung 0/4 · sua 19/25 · dong 274/600` nghĩa là dưới ngưỡng. 3 dấu ngày còn lại là dữ kiện: ngày cập nhật hồ sơ, ngày của hồ sơ CCL, tên file PDF huyền học. `sua 19` là số commit git, chỉ giảm khi có mốc `tai-ban-2`.

Nguồn duy nhất: **A** là `AGENTS.md` (điểm vào: thứ tự đọc, sáu luật, chọn skill, giữ não mới) · **D** là `co-so-tri-thuc/david.md` (hồ sơ, định hướng và cách làm việc với David) · **T** là `ky-nang/chuan-muc-lam-viec.md` (thói quen chung của mọi skill) · **C** là `CLAUDE.md`.

## Bảng luật hiện hành

| # | Luật | Nguồn nên ở | Nguồn cũ | Ngày chốt gần nhất | Trạng thái |
|---|---|---|---|---|---|
| 1 | Thứ tự đọc 7 bước; tra `tai-lieu-tham-khao/ccl/` khi làm nội dung lãnh đạo | A | A:5–17 | 08/11 | sống |
| 2 | Hồ sơ thấu hiểu: phần định hướng nghề đã lỗi thời, nếu lệch thì theo D | A | A:10 | 17/10 | sống (bỏ ngày) |
| 3 | Trả lời bằng tiếng Việt, ngắn gọn | A luật 1 | A:21, D:3.7 | 05/11 | trùng → D trỏ |
| 4 | Hỏi trước khi tạo/sửa, chờ "ok" (cách hỏi ở `thu-thap-yeu-cau`) | A luật 2 | A:22, D:3.1 | 08/11 | trùng → D trỏ |
| 5 | Không hỏi lại điều đã biết | T mục 2 | D:3.7, T:28, A:3 | 08/11 | trùng → D bỏ, A giữ câu mở |
| 6 | Con người làm trung tâm, không kinh doanh; không trị liệu/chẩn đoán; không công khai huyền học; không "chữa lành" | D 4.1, 4.7 (chi tiết) · A luật 3 (tóm tắt và trỏ) | A:23, D:4.1, 4.7, 7 | 05/11 | sống, A trỏ D |
| 7 | Nội dung là của David, không đưa mẫu lời | A luật 4 | A:24 | 05/11 | sống |
| 8 | Không đăng/gửi/xoá khi chưa duyệt; không nhập mật khẩu | A luật 5 | A:25, T:44 | — | trùng → T trỏ |
| 9 | GitHub là bản gốc; đẩy ngay bằng `dong-bo.sh --push`; "cập nhật não" là lệnh này; chỉ sản phẩm, dữ liệu khách hàng, giấy tờ cá nhân ở lại máy; danh sách không đưa lên | A luật 6 | A:26, A:47, A:50, D:3.8, T:59 | 07/11 | trùng → gộp vào A luật 6; D, T trỏ |
| 10 | Thứ tự khi nguồn mâu thuẫn: lời David vừa nói > D > ghi nhớ mới > ghi nhớ cũ | T mục 0 | A:28 | — | sống, A trỏ (xem Hỏi David 1) |
| 11 | Khi mâu thuẫn: chất lượng thắng tiết kiệm; lời David vừa nói > ngày chốt gần nhất > cũ; mơ hồ thì xem sản phẩm được duyệt mới nhất rồi hỏi | T mục 0 | T:8–11 | 08/11 | sống (bỏ câu lịch sử "trước 08/11") |
| 12 | AI sáng tạo bên trong khung; luật nội dung không phải là mẫu | T mục 0 | T:13–15 | 09/11 | sống (bỏ ngày) |
| 13 | David thường chỉ gửi tài nguyên, khi đó bắt đầu bằng `phan-phoi-da-kenh`; bảng chọn skill | A | A:30–44 | 10/11 | sống |
| 14 | Môi trường không phải Claude Code: skill là tài liệu quy trình, ánh xạ đường dẫn, nói rõ phần không làm được, chỉ tin repo và lời David | A | A:46–51 | — | sống |
| 15 | Cuối việc làm theo T mục 4 | A trỏ | A:56 | — | sống |
| 16 | Tên không dấu, chữ thường, gạch nối; ghi nhớ chỉ của một máy đặt tiền tố `may-`, không đưa lên repo | A | A:58 | 07/11 | sống |
| 17 | C: nạp `@AGENTS.md`; thiếu `~/.claude/david.md` thì đề nghị chạy `cai-dat-bo-nao.sh` | C | C:1–3 | — | sống |
| 18 | Hồ sơ David (tên, vai trò, kinh nghiệm, nơi ở, thước đo) | D 1 | D:9–20 | 05/11 | sống |
| 19 | Luật cá nhân: đợt năng lượng, 4 tiếng, chờ vài ngày, nhìn lại cuối tuần, mất nhịp 3 tuần | D 2 | D:22–28 | — | sống |
| 20 | Kế hoạch 4 phần | D 3 | D:3.2 | — | sống |
| 21 | Dịch đúng thuật ngữ, chỉ một bản dịch | D 3 | D:3.3 | — | sống |
| 22 | Tài liệu về một tổ chức chỉ gồm nội dung của tổ chức đó | D 3 | D:3.4 | — | sống |
| 23 | Tài liệu do AI khác viết: lấy khung Claude làm chuẩn, kiểm tra nguồn | D 3 | D:3.5 | — | sống |
| 24 | Sách tự mua | D 3 | D:3.6 | — | sống |
| 25 | Định hướng gốc và tệp khách chính "người lần đầu dẫn người" | D 4.1 | D:42–44 | 05/11, 04/11 | sống (bỏ ngày) |
| 26 | Ba tầng làm chủ; CCL làm gốc | D 4.2 | D:46–55 | — | sống |
| 27 | Các chặng nghề | D 4.3 | D:57–65 | — | sống |
| 28 | Chương trình và bảng giá | D 4.4 | D:67–69 | — | sống |
| 29 | Quy trình một trường hợp | D 4.5 | D:71–72 | — | sống |
| 30 | Quyết định đã chốt (bỏ sim, phủ trước, ICF, Đức, cần tìm, để sau) | D 4.6 | D:74–80 | — | sống |
| 31 | Lằn ranh nghề | D 4.7 | D:82–85 | — | sống |
| 32 | Kênh video: bản gốc YouTube và highlight, 3 phần, "Vấn đề/Kết quả", 3 dòng trước khi quay, lịch ở `kenh.json`, đo bằng "gỡ" | D 5 | D:87–92 | 10/11 | sống (xem Chéo bộ 1) |
| 33 | Kho 100 video: đối chiếu ở phiếu lọc; bỏ qua giai đoạn 3; cần làm lại theo ba tầng | D 5 | D:92 | 10/11 | sống (bỏ ngày, viết lại "đã bỏ") |
| 34 | Nghiên cứu CCL: hồ sơ 10 phần là tham chiếu chuẩn; tài liệu cũ không dùng làm chính; GPT/Perplexity đã đối chiếu, Gemini không dùng; sách sẽ mua; Lộ trình kiếm tiền tạm hoãn | D 6 | D:94–101 | 07/11 | sống (bỏ ngày chốt, bỏ câu link cũ) |
| 35 | Công cụ số học chỉ dùng trong buổi riêng, kèm điều kiện | D 7 | D:103–107 | — | sống |
| 36 | Bộ lọc nội dung: câu hỏi gốc, cây nội dung, David chỉ đưa tài nguyên | D 8 | D:110–115 | 05/11 | sống (bỏ ngày; chi tiết ở khối 00) |
| 37 | Dữ liệu huyền học nền: bản chuẩn PDF, hai file .md cũ không dùng, cách dùng, không ghi số căn cước… | D 9 | D:117–124 | 07/11 | sống (bỏ câu "gộp từ…") |
| 38 | Phạm vi file T; mỗi luật chỉ ở một chỗ | T đầu | T:1–5 | 08/11 | sống (bỏ "Chốt 08/11…") |
| 39 | Đầu việc: Mục tiêu/Xong khi, đọc đúng phần cần, không đọc cả repo, dùng grep, tự tra sự thật | T 1 | T:17–23 | 08/11 | sống |
| 40 | Hỏi một lần, gộp, đề xuất đứng đầu; "làm đi" không chốt lựa chọn; giữa chừng chỉ dừng ở 6 tín hiệu | T 2 | T:25–30 | 08/11 | sống |
| 41 | Ngoại lệ tự chọn: cắt highlight, làm lại video cũ | T 2 | T:31 | 07/11 | sống (bỏ "David đã chốt") |
| 42 | Phần cố định không hỏi, không đổi | T 2 | T:32–34 | 10/11 | sống (bỏ ngày) |
| 43 | Lệnh chạy theo lô, chạy nền khi quá 2 phút, render nối tiếp; chụp kiểm tra có giới hạn; dùng agent phụ khi được phép; bước nhẹ thì nhắc | T 3 | T:37–42 | 08/11 | sống |
| 44 | Không tự render lại sau góp ý | T 3 | T:43 | 05/11 | sống (xem Chéo bộ 2) |
| 45 | Báo cáo ngắn 4 phần | T 4 | T:47 | — | sống |
| 46 | Góp ý ghi đúng một chỗ; chỉ luật dùng chung cho nhiều skill mới vào `co-so-tri-thuc/bo-nho/`, có ghi nhớ gần giống thì sửa ghi nhớ đó | T 4 | T:48, T:55 | — | sống (dời câu bộ nhớ về đúng gạch đầu dòng) |
| 47 | Sửa trực tiếp, không chồng câu; ba loại file ở `tai-cau-truc` | T 4 | T:49–52 | 10/11 | sống |
| 48 | Đo chồng chéo sau mỗi lần sửa bản luật; công cụ cảnh báo thì nhắc một dòng, David quyết định | T 4 | T:53–54, T:81 | 10/11 | trùng → bảng mục 5 trỏ mục 4 |
| 49 | Video đã chốt/đăng: dọn bằng `don-tap.py --xoa`, chỉ hỏi khi có ⏸, chuyển vào Thùng rác | T 4 | T:56–57 | 08/11 | sống (bỏ ngày; xem Chéo bộ 2) |
| 50 | Cập nhật file theo dõi khi xong đợt | T 4 | T:58 | — | sống |
| 51 | Việc tiếp theo lớn thì đề nghị phiên mới, ghi bước tiếp theo | T 5 (bảng) | T:60, T:74 | 08/11 | trùng → gộp vào hàng bảng |
| 52 | Mục tiêu và Xong khi: ở đầu, giữa, cuối việc | T 5 | T:63–68 | 08/11 | sống (bỏ ngày ở tiêu đề) |
| 53 | Nhắc một dòng, mỗi chuyện một lần; bảng "Khi → Claude làm" | T 5 | T:70–82 | 08/11 | sống |
| 54 | Thói quen của David để nhắc | T 5 | T:84–86 | 08/11 | sống |
| 55 | Ngày cập nhật hồ sơ D (dữ kiện) | D đầu | D:5 | 08/11 | giữ ngày, bỏ lời kể "chuẩn hoá…" |

55 luật sống · 7 luật trùng đã gộp về một nguồn duy nhất (dòng 3, 4, 5, 8, 9, 48, 51) · 0 luật bỏ · không đổi nghĩa luật nào. Số mục của `chuan-muc-lam-viec.md` giữ 0–5 để đường trỏ "mục N" ở skill khác vẫn khớp; `co-so-tri-thuc/david.md` mục 3 đánh số lại 1–5 (không file nào trỏ tới số con của mục 3).

## Sổ (đã gỡ khỏi bản luật, giữ lại để không mất)

- `AGENTS.md` dòng hồ sơ thấu hiểu: "Ghi 17/10/2026" là ngày ghi chú rằng phần định hướng nghề đã cũ.
- `co-so-tri-thuc/david.md` đầu file: "Cập nhật lần cuối: 08/11/2026 (chuẩn hoá: mục 3.1, 3.8, 5 trỏ về nhà chính của luật)". Nay: cập nhật 10/11/2026 (tái bản 2).
- `co-so-tri-thuc/david.md` 3.8: GitHub là bản gốc, bắt buộc từ 07/11/2026; nay nguồn ở `AGENTS.md` luật 6, chi tiết ở ghi nhớ `co-so-tri-thuc-github-ban-goc`.
- `co-so-tri-thuc/david.md` 4.1: định hướng gốc ngày 05/11/2026; tệp khách chính quyết định ngày 04/11/2026.
- `co-so-tri-thuc/david.md` 5: đối chiếu kho 100 video ở phiếu lọc, David chốt 10/11/2026. Giai đoạn 3 "Cơ sở chạy khi vắng chủ" bị bỏ (cùng với định hướng 05/11 không kinh doanh).
- `co-so-tri-thuc/david.md` 6: hồ sơ CCL 10 phần là tham chiếu chính, David chốt 07/11/2026. Link claude.ai cũ (bản ghi "13 phần") không còn mở được nên đã bỏ.
- `co-so-tri-thuc/david.md` 8: bộ lọc nội dung David chốt 05/11/2026 cùng Claude Code.
- `co-so-tri-thuc/david.md` 9: PDF huyền học bản gộp được làm từ bản PDF 31/10/2026 và hai file .md cũ (07/11/2026).
- `chuan-muc-lam-viec.md` đầu file: "Chốt 08/11/2026 (`du-an/chuan-hoa-ky-nang.md`, vòng 2)".
- `chuan-muc-lam-viec.md` mục 0: "Trước 08/11/2026 các skill không nối với nhau, nên chỗ lệch là do chỗ đó chưa được cập nhật, không phải ý David." Câu này được viết lại không có ngày: chỗ lệch giữa các file thường do một chỗ chưa được cập nhật.
- `chuan-muc-lam-viec.md` mục 0: AI sáng tạo bên trong khung, David chốt 09/11/2026 (ghi nhớ `video-motion-ke-chuyen`).
- `chuan-muc-lam-viec.md` mục 2: ngoại lệ tự chọn, David chốt 07/11/2026 (ghi nhớ `quy-tac-goi-y-de-david-chon`); phần cố định không hỏi, David chốt 10/11/2026.
- `chuan-muc-lam-viec.md` mục 4: dọn file tạm của video đã chốt, chốt 08/11/2026.
- `chuan-muc-lam-viec.md` mục 5: "Luôn đi tới mục tiêu, giữ phiên gọn", David chốt 08/11/2026.

## Chéo bộ

1. **Luật kênh trùng với `kenh.json`** (bộ video): `co-so-tri-thuc/david.md` mục 5 vẫn ghi "Vấn đề / Kết quả", "đo bằng gỡ", 3 phần mỗi video; ghi nhớ `co-so-tri-thuc-ho-so-va-bo-loc` nói `kenh.json` là nguồn duy nhất của luật kênh (rà soát T3: "david.md giữ định hướng, bỏ chi tiết lặp"). Tái bản này giữ nguyên mục 5 (không đổi luật). Đề xuất: phiên điều phối đối chiếu với `ky-nang/san-xuat-video/ho-so-thuong-hieu/kenh.json`; chi tiết nào đã có ở đó thì `david.md` mục 5 chỉ còn một dòng trỏ.
2. **Luật riêng của video nằm trong thói quen chung** (bộ video): `chuan-muc-lam-viec.md` mục 3 "Không tự render lại", mục 4 "dọn file tạm bằng `don-tap.py --xoa` (khối 17)", mục 3 "render nối tiếp", mục 2 danh sách "phần cứng" (dấu góc, thẻ cuối, nhạc…). Đây là các luật chỉ dành cho video. Đề xuất: nguồn duy nhất đặt ở `ky-nang/san-xuat-video/quy-tac-chung.md`, thói quen chung chỉ giữ một dòng trỏ. Tái bản này chưa dời (cần bộ video tiếp nhận).
3. **Ghi nhớ trùng với bản luật** (bộ ghi-nho): `co-so-tri-thuc-github-ban-goc` lặp lại luật 6 của `AGENTS.md`; `quy-tac-goi-y-de-david-chon`, `quy-tac-ket-qua-hon-toc-do`, `quy-tac-tu-hoi-khi-mo-ho`, `quy-tac-sua-thang-tai-ban` lặp lại `chuan-muc-lam-viec.md` mục 0, 2, 4. Đề xuất: ghi nhớ giữ ngày, lời David và lý do (vai trò sổ), câu luật trỏ về nguồn duy nhất.
4. **`~/.claude/CLAUDE.md`** (ngoài repo hoặc lối tắt, phiên điều phối kiểm tra): có hai dòng "trả lời tiếng Việt" và "hỏi trước theo thu-thap-yeu-cau" trùng với `AGENTS.md` luật 1–2; đề xuất giữ vì file này được nạp ở mọi dự án ngoài repo, nhưng ghi rõ là dòng trỏ.
5. **`thu-thap-yeu-cau/SKILL.md:17`** trỏ "ngoại lệ được tự chọn" về `chuan-muc-lam-viec.md` mục 2; đường trỏ này vẫn đúng, số mục giữ nguyên (0–5) nên mọi đường trỏ "mục N" ở các skill khác vẫn khớp.

## Hỏi David

1. **Thứ tự khi nguồn mâu thuẫn có hai cách nói:** `AGENTS.md` cũ: "lời David vừa nói > `co-so-tri-thuc/david.md` > bộ nhớ ngày mới hơn > bộ nhớ cũ"; `chuan-muc-lam-viec.md` mục 0: "lời David vừa nói > bên có ngày chốt gần nhất > bên cũ hơn". Hai cách này lệch nhau khi một ghi nhớ mới hơn `david.md`. Bản mới đặt cả hai cạnh nhau ở mục 0, chưa đổi nghĩa. **Đề xuất:** gộp thành một câu "Lời David vừa nói > bản luật (`co-so-tri-thuc/david.md`, skill) > ghi nhớ; hai bản luật lệch nhau thì theo ngày ở sổ (git, changelog), mới hơn thắng"; cách này phù hợp với thiết kế tái bản (ghi nhớ là sổ, không chứa luật mà bản luật không có).
2. **Dời luật riêng của video khỏi thói quen chung** (Chéo bộ 2): David có đồng ý dời về `quy-tac-chung.md` không? Đề xuất: đồng ý.
