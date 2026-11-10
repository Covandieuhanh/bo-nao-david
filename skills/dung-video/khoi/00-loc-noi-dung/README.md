# Khối 00-loc-noi-dung: Bộ lọc nội dung + phân phối kênh (làm TRƯỚC mọi việc dựng)

**Dùng trong:** cả 4 loại, và mọi tài nguyên David đưa (video, file ghi âm, bài viết).
**Đầu vào:** tài nguyên David đưa — KHÔNG kèm yêu cầu (David chốt 05/11/2026) · hồ sơ `~/.claude/David.md` · hồ sơ kênh `../../ho-so/kenh.json` · sổ `~/Movies/_so-danh-muc/danh-muc.md` · **kho 100 video `dang-lam/kho-100-video.md`** (kế hoạch nội dung, repo bộ não)
**Đầu ra:** phiếu lọc (gửi David = cổng duyệt 1) · một dòng trong sổ danh mục
**Hình mẫu:** Hieu Nguyen (2 mảng lặp lại 50/50 tập), Alex Hormozi ("được biết đến vì một điều"), Justin Welsh (content pillars), Gary Vaynerchuk (một lần nói → nhiều bài).
**Sửa khối này → chạy lại:** không có code; đổi luật kênh → sửa `ho-so/kenh.json`.

## Nguyên tắc
- **David chỉ đưa tài nguyên.** Claude tự phân tích, đề xuất làm gì · làm thế nào · đăng kênh nào · lúc nào, rồi HỎI LẠI (skill
  `hoi-chuyen-gia`, một vòng, câu nào cũng có đề xuất "đồng ý" được). David nói tự do, bộc phát — không đòi David theo khuôn.
- **Không làm gì không có mục tiêu**: mỗi bài phải kéo tương tác trên đúng nền tảng đó → chuyển hoá → nhắn "gỡ". Nội dung "cho vui"
  chỉ được làm khi nó xây nhân hiệu trainer.
- **Không khung thời lượng cố định**: dạng + độ dài theo chính nội dung; có khi giữ nguyên bản gốc.
- Claude chấm và ghi lý do; **David chốt cuối**.

## 1. Câu hỏi gốc
> Nội dung này có giúp **người lần đầu dẫn người** (quản lý trẻ, quản lý mới) **làm chủ bản thân** — hoặc **áp dụng việc làm chủ
> bản thân vào chính công việc của họ** — thêm một bước không?

**Cây nội dung** (hồ sơ David mục 4.2): **Gốc** = làm chủ bản thân · **Nhánh chính** = áp dụng vào công việc của chính họ (môi trường
để tự phát huy thế mạnh) · **Nhánh phụ** = mối quan hệ, chỉ khi bắt nguồn từ bản thân · **Nhân hiệu** = đời thường / hành trình của
David, chỉ khi giúp người xem tin David là trainer. Không có nhánh kinh doanh / mô hình kinh doanh.

## 1b. Đối chiếu kho 100 video (David chốt 10/11/2026 — bắt buộc mọi tài nguyên)
Kho `dang-lam/kho-100-video.md` là **kế hoạch nội dung** của kênh: dần dần mọi video phải đi theo kho, tránh làm video lệch mục tiêu.
Đọc phần "Luật đối chiếu" ở đầu kho, rồi tìm (`grep` nỗi đau / cách làm / từ khoá của lời chép) ý khớp nhất:
- **Khớp** → ghi `Kho 100: ý <số> "<nỗi đau>"` + kiểu dẫn dắt của ý đó (kho thắng tỉ lệ tự đếm, trừ khi David chọn khác).
- **Không khớp ý nào** → ⚠️ cảnh báo trong phiếu, David chọn: thêm làm ý mới (cuối giai đoạn hợp) · cất kho · bỏ. Không tự dựng.
- **Khớp giai đoạn 3** (cơ sở chạy khi vắng chủ — hướng kinh doanh đã bỏ) → ⚠️ cảnh báo rõ.
- Luôn gợi ý **ý kế tiếp nên quay**: ý "Ý tưởng" số nhỏ nhất (bỏ giai đoạn 3) — nhắc David quay theo kế hoạch.
- Sau cổng 1 / dựng / đăng: đổi cột Trạng thái của ý trong kho (Đã dựng <ngày> · `tap-<tên>` → Đã đăng <ngày> + link), đẩy GitHub.

## 2. Chấm 5 tiêu chí (0–2 mỗi tiêu chí)
| # | Tiêu chí | 2 | 1 | 0 |
|---|---|---|---|---|
| 1 | **Gắn gốc** | nói thẳng về làm chủ bản thân / áp dụng vào công việc | chạm gián tiếp | không liên quan |
| 2 | **Hữu ích cho tệp** | người lần đầu dẫn người dùng được ngay | dùng được nếu tự liên hệ | không phải tệp |
| 3 | **Hành động** | có việc cụ thể làm theo (Thực thi) | có gợi ý chung | chỉ chia sẻ |
| 4 | **Kéo tương tác** | có câu mở giữ người xem + chỗ hỏi "Vấn đề" / "Kết quả" tự nhiên | có một trong hai | không |
| 5 | **Nhân hiệu** | chuyện thật của David, thấy cách David dẫn dắt | có chuyện thật | không |

**Khung 3 phần** Vấn đề · Giải pháp · Thực thi: được **sắp lại thứ tự đoạn** từ nguyên lời David; thiếu hẳn một phần (thường là
Thực thi) → không bịa, báo "thiếu phần X" để David quyết nói bổ sung hay cất kho.

**Chấm cả câu chuyện, không chấm từng đoạn để giữ đoạn điểm cao** (David chốt 2026-11-05): 70–80% câu chuyện là dẫn dắt, bối cảnh, tình
huống để đoạn đắt có giá trị. Video dài là bản gốc và để nguyên (luat-chung 2); video ngắn chỉ trích từ đó. Claude chỉ đọc lời chép, không
cảm được giọng và sức nặng câu chuyện, nên không quyết đoạn nào "ít giá trị".

## 3. Lằn ranh = CẢNH BÁO, David quyết (hồ sơ 4.7 + 7)
Huyền học / số học / từ trường số / tâm linh dạng huyền học · chữ "chữa lành" · tư vấn thuế, pháp lý · trị liệu, chẩn đoán tâm lý ·
chuyện người khác không ẩn danh · nhắc vai coach trên kênh công khai · kinh doanh, mô hình kinh doanh, hứa thu nhập · nói giá.
Chạm → **luôn cảnh báo trong phiếu**: mốc giây, lời chạm, rủi ro, câu hỏi "cắt hay giữ?". Không tự cắt. David có thể giữ vì đã tự cân đối khi kể
(David chốt 2026-11-05). Giữ → ghi "đã cảnh báo, David giữ" vào sổ; chữ đồ hoạ, tiêu đề, thumbnail, mô tả, clip ngắn vẫn không lấy nội dung đó.

## 4. Bảy kết luận
| Nhãn | Khi | Làm |
|---|---|---|
| ⭐ **Rất tốt** | 9–10, không chạm lằn ranh | đủ bộ: YouTube (bản gốc / biên tập) + highlight Reels, TikTok + bài viết trang |
| ✅ **Phù hợp** | 7–8 | theo kênh đề xuất (thường YouTube hoặc highlight + bài viết) |
| ✂️ **Trích ngắn từ gốc** | bản dài đã duyệt có đoạn đắt cho video ngắn | bản dài vẫn để nguyên làm gốc; clip là phần thêm, không thay bản dài |
| 🔁 **Trùng / dư** | đã có bài gần giống trong 30 ngày, hoặc nhánh đang quá tỉ lệ | gộp vào bài cũ / để sau |
| 🗂 **Lưu kho** | có giá trị nhưng chưa đúng lúc / chưa đủ 3 phần | lưu lời chép + nhãn, chờ ghép series |
| 👤 **Chỉ Facebook cá nhân** | ≤ 6, đời thường có ích cho nhân hiệu | câu chia sẻ ngắn, không dựng nặng |
| ⛔ **Không làm** | không liên quan, hoặc David chọn không làm sau cảnh báo lằn ranh | không dựng, không tốn thời gian |

## 5. Phân phối kênh (`ho-so/kenh.json`)
YouTube (chính) = bản gốc hoặc biên tập · Trang Facebook = Reels + bài viết + mời nhắn "gỡ" · TikTok cá nhân = clip ngắn ·
Facebook cá nhân = đời thường, hành trình, chia sẻ lại bài trang. Lịch thứ Ba + thứ Sáu 20:00 giờ Việt Nam. Kiểu dẫn dắt mỗi bài:
**Không · Gợi mở · Mời** theo tỉ lệ 4 · 4 · 2 (bài thứ 5 và 10 mỗi chục là Mời).

## 6. Phiếu lọc (gửi David — một màn hình)
```
📥 <tên file> · <độ dài> · <loại dựng: làm video / ghép vlog / podcast / highlight>
Kết luận: <nhãn> · <điểm>/10   (Gốc x · Tệp x · Hành động x · Tương tác x · Nhân hiệu x)
Lý do: <1–2 dòng>  · Lằn ranh: <không / ⚠️ chạm ở mm:ss, lý do, rủi ro → hỏi cắt hay giữ>
Nhánh: <gốc / công việc / quan hệ / nhân hiệu> · Trùng sổ 30 ngày: <… / không>
Kho 100: <ý số … "nỗi đau" · dẫn dắt theo kho / ⚠️ không khớp ý nào / ⚠️ giai đoạn 3 đã bỏ> · Ý kế tiếp nên quay: <số + nỗi đau>
Đề xuất: <sản phẩm → kênh → ngày giờ> (vd. YouTube bản biên tập ~9 phút T3 20:00 · 2 highlight Reels+TikTok T6 · bài viết trang)
3 phần: Vấn đề <mm:ss> · Giải pháp <mm:ss> · Thực thi <mm:ss / THIẾU>
Câu mở: "<trích lời>" · Bình luận: "Vấn đề" / "Kết quả" · Dẫn dắt: <Không / Gợi mở / Mời>
❓ <câu hỏi chỉ David quyết được, mỗi câu có ➡️ đề xuất>
```

## 7. Sổ danh mục `~/Movies/_so-danh-muc/danh-muc.md`
Một dòng mỗi tài nguyên: ngày · file · nhãn · điểm · nhánh · kênh · dẫn dắt · trạng thái (lọc / dựng / chờ đăng / đã đăng / kho / bỏ).
Mỗi lần lọc, Claude xem sổ và CẢNH BÁO trong phiếu: nhánh nào đang quá nhiều / thiếu (mục tiêu: gốc + công việc ≥ 70%), tuần chưa có
bài Mời, kho quay sẵn < 4 video, lịch thứ Ba / thứ Sáu tới chưa có bài, chủ đề trùng trong 30 ngày.
