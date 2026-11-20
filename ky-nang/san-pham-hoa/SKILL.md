---
name: san-pham-hoa
description: Máy gom và đóng gói của David — mỗi đêm gom phần mới ở mọi nguồn (lời David trong phiên Claude, sổ nhớ bot Telegram, tổng hợp tin nhắn, lời trong video, bài đăng, số liệu) rồi phân loại theo ba hướng nghề, mục tiêu / nỗi đau, bán được gì; mỗi sáng thứ 6 (ngày tổng kết tuần) đóng nguyên liệu thành sản phẩm bán được (bổ sung gói đang chạy, bài phễu nháp, đề xuất gói mới khi ≥ 5 người cùng gặp một nỗi đau) và gói có các bước để trainer lại. Dùng khi lịch đêm / tuần chạy, khi David nói "gom", "phân loại", "đóng gói", "tuần này có gì bán được", "nỗi đau nào đang lặp", "/san-pham-hoa".
---

# Gom và đóng gói

Đọc trước: `ky-nang/chuan-muc-lam-viec.md`. Kế hoạch 4 phần: `du-an/san-pham-hoa.md`.

**Mục tiêu:** không ý, nỗi đau, bài học nào trôi mất; mỗi tuần nguyên liệu thật thành thứ bán được (`co-so-tri-thuc/david.md` 4.1: mục tiêu chung là ra tiền).

## Chỗ để

| Thứ | Ở đâu | GitHub |
|---|---|---|
| Kho thô mỗi ngày (script ghi) | `~/Documents/2-ca-nhan/so-tay/kho-du-lieu/ngay/<ngày>.md` | không |
| Nguyên liệu đã phân loại | `…/kho-du-lieu/nguyen-lieu.md` | không |
| Sổ nỗi đau (đếm lặp) | `…/kho-du-lieu/noi-dau.md` | không |
| Bài phễu nháp (sản phẩm) | `…/kho-du-lieu/bai-pheu/<ngày>-<ten>.md` | không |
| Phiếu tuần (đã ẩn danh) | `du-an/dong-goi/<ngày thứ 6>.md` | có |
| Bổ sung gói đang chạy | thư mục gói, ví dụ `du-an/goi-dao-tao-dung-video-ai/` | có |

Gọi tắt `KG/` = `~/Documents/2-ca-nhan/so-tay/kho-du-lieu/`.

## Luật cứng
- **Ẩn danh khi ra khỏi `KG/`:** không tên khách, không người quen, không số điện thoại, số tài khoản, địa chỉ, sức khoẻ. Chỉ chuyện thật; chuyện người khác thì "một học viên", "một người bạn".
- **Không đăng, không gửi tin cho ai** ngoài báo cáo về bot của David (`AGENTS.md` luật 4). Bài phễu là nháp chờ David duyệt.
- **Lằn ranh nghề** (`co-so-tri-thuc/david.md` 4.7): từ trường số là nội dung hướng trainer (không đọc số người thật chưa đồng ý, không hứa kết quả nhờ con số), không "chữa lành", tài chính không hứa lợi nhuận, không gọi lệnh; gói công nghệ chỉ hứa kết quả đã chạy thật.
- Soạn hay bổ sung gói hướng 3: theo **Luật soạn gói hướng 3** ở `co-so-tri-thuc/chien-luoc-nghe-nghiep.md` mục 4.1 (luật của nghề, không thuộc skill này).
- Không đọc lại cả kho cũ: mỗi đêm chỉ đọc file ngày mới nhất; mỗi tuần đọc `nguyen-lieu.md` (7 ngày) + `noi-dau.md`.

## Nguồn (script `tu-dong-hoa/thu-thap-du-lieu/gom.py` lo, không tốn token)
Lời David gõ trong mọi phiên Claude (bỏ phiên bot Sổ nhớ vì bot đã ghi vào sổ, bỏ lời ngắn kiểu "ok") · phần mới của sổ nhớ
(việc, ý tưởng, kiến thức, lịch hẹn, nhật ký, báo cáo phiên) · tổng hợp tin nhắn mỗi sáng · lời trong video (chép lời bản gốc, bỏ bản
trùng và thư mục `thu-…`; tập đã có mục trong nhật ký nội dung theo hướng `du-an/nhat-ky-noi-dung/` thì lấy ý từ đó, không phân loại lại) · bài đăng, số liệu, danh mục video (chỉ khi đã điền số). Mốc lần trước ở `KG/.moc.json`.

## Việc 1 — Phân loại mỗi đêm (lịch 23:00)
1. `python3 -I tu-dong-hoa/thu-thap-du-lieu/gom.py` (ở thư mục bộ não). In "Không có gì mới" → dừng, không báo.
2. Đọc file ngày vừa ghi. Tách thành **ý**: một ý = một điều có thể dùng lại (một nỗi đau, một câu chuyện thật, một bài học, một
   cách làm, một câu hỏi của người khác, một số liệu, một quyết định của David). Bỏ: lệnh kỹ thuật thuần, lời chào, việc vặt; **chuyện riêng của David và gia đình (nợ, đất, pháp lý, sức khoẻ, tâm linh) không chép
   vào nguyên liệu**, kể cả ở `KG/`.
3. Mỗi ý một dòng, thêm vào cuối `KG/nguyen-lieu.md` (chưa có thì tạo với dòng tiêu đề):
   `| ngày | nguồn | ý (≤ 1 dòng, lời gốc nếu đắt) | hướng | tầng / phạm trù | nỗi đau hay mục tiêu | bán được gì | dạng |`
   - **hướng:** `1 tài chính` · `2 trainer` · `3 công nghệ` · `nền` (về bộ não, cách làm việc với Claude: chỉ giữ khi là bài học cho gói 3).
   - **tầng / phạm trù:** hướng 2 ghi tầng (bản thân / công việc / quan hệ); mọi hướng ghi phạm trù chính (Tiền / Thị trường / Con người, `co-so-tri-thuc/mo-hinh-kinh-doanh.md`).
   - **nỗi đau hay mục tiêu:** viết bằng lời của người có nỗi đau, ngắn ("làm cả ngày mà không ra kết quả").
   - **bán được gì:** gói đang có (`du-an/pheu-ban-hang-goi-cong-nghe.md`, `co-so-tri-thuc/david.md` 4.4) hoặc `chưa có gói`.
   - **dạng:** bài phễu · bài học gói · lỗi thường gặp · câu hỏi thường gặp · ý video mới · lời chứng · quà tặng (PDF, checklist).
   - Lời David sửa Claude khi dựng video, làm slide… là **lỗi thường gặp khi dùng AI** → nguyên liệu bài học cho gói 3.
4. Cộng `KG/noi-dau.md`: bảng `| nỗi đau | hướng | số người | ai (ẩn danh) | nguồn gần nhất | gói khớp | trạng thái |`. Cùng nghĩa thì gộp một dòng,
   **số người** = số người khác nhau gặp nỗi đau đó (một người nói nhiều lần, nhiều ngày vẫn tính một; David tự gặp tính một và ghi
   "David tự gặp", đó là bằng chứng gói chạy thật trên chính David). Trạng thái: `theo dõi` · `≥5 chờ đề xuất` · `đã đề xuất` · `có gói`.
5. Không báo Telegram mỗi đêm. Chỉ báo khi một nỗi đau vừa chạm 5 người: `bash tu-dong-hoa/so-tay/bao-cao.sh --chi-gui "🔔 Nỗi đau 5 người gặp: … · sẽ đề xuất gói ở phiếu sáng thứ 6"`.

## Việc 2 — Đóng gói sáng thứ 6 (lịch 06:30, trước tin tổng kết tuần 07:30)
Đọc `KG/nguyen-lieu.md` 7 ngày qua, `KG/noi-dau.md`, `du-an/pheu-ban-hang-goi-cong-nghe.md`, README của gói đang chạy.
1. **Gói đang chạy** (gói David đã chốt trong `pheu-ban-hang-goi-cong-nghe.md`, hiện là Gói 1 `goi-dao-tao-dung-video-ai`): nguyên liệu dạng bài học,
   lỗi thường gặp, câu hỏi thường gặp → bổ sung thẳng vào đúng file của gói (giáo trình, SOP, danh sách kiểm soát), viết thành bước +
   chuẩn đạt, sửa thẳng câu cũ nếu trùng (luật 5). Mỗi tuần tối đa 5 bổ sung, chọn cái giúp học viên ra kết quả nhanh nhất.
2. **Bài phễu nháp:** 2–3 bài từ chuyện thật trong tuần, mỗi bài chạm một nỗi đau đang lặp nhiều nhất, theo giọng
   `ky-nang/san-xuat-video/ho-so-thuong-hieu/giong-thuong-hieu-david.md`, cuối bài mời nhắn từ khoá của hướng đó. Lưu `KG/bai-pheu/`. Bài cho hướng 2 dùng
   lời David trong video / tin nhắn, không đặt lời vào miệng David.
3. **Đề xuất gói mới:** mỗi nỗi đau `≥5 chờ đề xuất` → một mục trong phiếu tuần theo 4 phần: Mục tiêu (kết quả hứa, đo được) ·
   Kế hoạch (số buổi, công cụ) · Quy trình (bước dạy) · Thực thi (việc làm ngay để bán thử). Đổi trạng thái `đã đề xuất`. Không tạo
   thư mục gói khi David chưa chọn.
4. **Ý video mới:** ý `ý video mới` theo hướng 1 và 2, đối chiếu `du-an/ke-hoach-noi-dung-100-video.md` (khớp ý số mấy, hay ý mới).
5. **Phiếu tuần** `du-an/dong-goi/<ngày>.md` (đã ẩn danh): Top nỗi đau (số người) · Đã bổ sung vào gói nào, ở đâu · Bài phễu nháp
   (tên, nỗi đau) · Đề xuất gói mới · Ý video mới · Chờ David quyết.
6. Báo bot (≤ 8 dòng): `bash tu-dong-hoa/so-tay/bao-cao.sh "📦 Đóng gói tuần: … · Bài phễu: N nháp ở kho-du-lieu/bai-pheu · Chờ anh: …"`.
7. Cuối việc theo `chuan-muc-lam-viec.md` mục 4 (đẩy GitHub phiếu tuần và phần sửa gói: `bash tu-dong-hoa/dong-bo.sh --push`).

## Lịch
Nằm trong repo, không gắn tài khoản: `tu-dong-hoa/lich/lich-chay.md` (gom 23:00 mỗi đêm, đóng gói 06:30 thứ 6), lời giao ở `tu-dong-hoa/lich/loi-giao/`. Tới giờ máy canh bot mở phiên "Lịch · <tên>" hiện trong app Claude; đổi giờ thì sửa đúng file đó.
