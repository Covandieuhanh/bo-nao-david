---
description: "Khối 00 bộ lọc nội dung: lọc tài nguyên theo hồ sơ David, phân hướng nghề, bán được gì, phân phối kênh."
---

# Khối 00-sang-loc-noi-dung: Bộ lọc nội dung + phân phối kênh (làm TRƯỚC mọi việc dựng)

**Dùng trong:** cả 4 loại, và mọi tài nguyên David đưa (video, file ghi âm, bài viết).
**Đầu vào:** tài nguyên David đưa — thường KHÔNG kèm yêu cầu · hồ sơ `~/.claude/david.md` · hồ sơ kênh `../../ho-so-thuong-hieu/kenh.json` · sổ `~/Movies/_danh-muc-noi-dung/danh-muc-noi-dung.md` · **kho 100 video `du-an/ke-hoach-noi-dung-100-video.md`** (kế hoạch nội dung, repo bộ não)
**Đầu ra:** phiếu lọc (ghi vào dự án; là nguồn của 4 phần gọn David duyệt, không có cổng duyệt riêng) · `phan-huong.md` của tập · mục nhật ký nội dung từng hướng (`du-an/nhat-ky-noi-dung/`) · một dòng trong sổ danh mục
**Hình mẫu:** Hieu Nguyen (2 mảng lặp lại 50/50 tập), Alex Hormozi ("được biết đến vì một điều"), Justin Welsh (content pillars), Gary Vaynerchuk (một lần nói thì nhiều bài).
**Sửa khối này thì chạy lại:** không có code; đổi luật kênh thì sửa `ho-so-thuong-hieu/kenh.json`.

## Nguyên tắc
- **David chỉ đưa tài nguyên.** Claude tự phân tích, tự chọn làm gì · làm thế nào · đăng kênh nào · lúc nào (`chuan-muc-lam-viec.md`
  mục 2), ghi vào phiếu lọc; 4 phần gọn lấy từ phiếu (`phan-phoi-da-kenh` bước 0), David duyệt rồi làm một mạch. David nói tự do, bộc phát — không đòi David theo khuôn.
- **Không làm gì không có mục tiêu**: mỗi bài phải kéo tương tác trên đúng nền tảng đó → chuyển hoá → nhắn "gỡ". Nội dung "cho vui"
  chỉ được làm khi nó xây nhân hiệu trainer.
- **Không khung thời lượng cố định**: dạng + độ dài theo chính nội dung; có khi giữ nguyên bản gốc.
- Claude chấm, ghi lý do và tự chốt; David sửa ở bản cuối nếu muốn.

## 0. Phân hướng (làm đầu tiên — hồ sơ David mục 4.1)
| Hướng | Nhận ra khi | Nơi đăng | Bán gì |
|---|---|---|---|
| **1. Tài chính** | giao dịch hàng hoá, thị trường, đầu tư, hành trình làm tài chính | YouTube David Trần Official (+ clip ngắn kênh đó) | hợp tác môi giới / mở tài khoản hợp pháp |
| **2. Trainer con người** | làm chủ bản thân, công việc, mối quan hệ; dẫn người; từ trường số và dẫn chứng (thần số học, thiền, "nghiệp"…), hệ 135 | YouTube trainer + highlight, Facebook cá nhân | gói trainer (hồ sơ 4.4) |
| **3. Giải pháp công nghệ AI** | mọi thứ khác: công nghệ / AI thực chiến, số hoá cho tổ chức, đời thường, hành trình | Facebook cá nhân, fanpage, TikTok | gói công nghệ cá nhân, giải pháp số hoá cho tổ chức + đào tạo tới khi ra kết quả |

Mọi tài nguyên đều **phân đủ theo cả ba hướng** (mục 0b): hướng nào có ý trọn thì ra một bản riêng, phần không thuộc hướng nào thì
bỏ. Cách soi mục tiêu / nỗi đau: ba phạm trù **Tiền · Thị trường · Con người** (`co-so-tri-thuc/mo-hinh-kinh-doanh.md`); marketing,
khách, thị trường của chính người xem = "làm chủ thị trường" thì hướng 2.

## 0b. Phân hướng từng đoạn, ghép bản theo hướng
1. **Chia đoạn theo ý**: đọc cả bản lời, mỗi đoạn một ý: mốc vào–ra · ý một dòng · hướng (1 / 2 / 3) · hoặc **Bỏ** kèm lý do (không
   liên quan, chào hỏi, chuyện riêng, lằn ranh mục 3, ý chưa trọn). Một đoạn chạm hai hướng: gán hướng chính, ghi "dùng lại ở hướng X"
   (ví dụ: phép thử nỗi đau thuộc hướng 2, hướng 3 dùng lại làm câu mở tư vấn).
2. **Mỗi hướng một bản** khi gom được bối cảnh + ít nhất một ý trọn (chấm 5 tiêu chí theo hướng, mục 2). Không đủ thì không ép ra bản,
   chỉ ghi nhật ký. Dạng mặc định, độ dài vẫn theo nội dung:
   | Hướng | Bản | Nơi đăng |
   |---|---|---|
   | 1 Tài chính | bản YouTube + clip ngắn | David Trần Official |
   | 2 Trainer con người | bản dài + highlight | YouTube trainer, Facebook cá nhân |
   | 3 Giải pháp công nghệ AI | bản vừa khoảng 8–15 phút + clip dọc | Facebook cá nhân, fanpage, TikTok |
3. **Ghép trọn ý** (cùng bốn câu của highlight, khối 13):
   - **Bối cảnh**: đoạn mở phải đủ để người xem hiểu ai đang nói gì; thiếu thì kéo thêm câu bối cảnh liền trước, không tự viết lời dẫn.
   - **Ý trọn**: vào / ra ở cuối câu, bắt chỗ lặng gần nhất; không cắt giữa lập luận. Trong mỗi đoạn để nguyên (quy-tac-chung mục 2).
   - **Lời trỏ về trước** ("như em nói lúc nãy", "cái vừa nãy"): kéo theo đoạn được nhắc, hoặc bỏ câu trỏ đó.
   - **Mối nối**: giữ thứ tự buổi nói; hai đoạn không nối liền ý thì chèn thẻ chương bằng chữ nguyên văn của David.
4. **Ý dùng cho công việc** (nội bộ, không đăng): mỗi hướng có bản thì rút 2–4 ý: nỗi đau · cách làm / giải pháp · câu dùng khi tư vấn
   hoặc đứng lớp · mốc. Lấy từ lời trong tập, không bịa.
5. **Ghi lại** (bắt buộc, kể cả tập ⛔ / 🗂 và hướng không ra bản):
   - `<thư mục tập>/phan-huong.md` theo mẫu [mau-phan-huong.md](mau-phan-huong.md): bảng đoạn, danh sách đoạn từng bản, mối nối cần
     soát, lằn ranh, ý dùng cho công việc. Phiên dựng sau chỉ cần đọc file này + bản lời là cắt được.
   - Một mục vào **nhật ký nội dung** của từng hướng có ý: `du-an/nhat-ky-noi-dung/` (luật ghi ở README thư mục đó).

## 1. Câu hỏi gốc (theo hướng)
- **Tài chính:** có giúp người xem hiểu giao dịch hàng hoá hợp pháp thêm một bước, và tin David trong lĩnh vực này không?
- **Trainer:** có giúp người xem **tự làm chủ bản thân** (tiền, thị trường, con người của chính họ; lõi là người lần đầu dẫn người)
  hoặc **áp dụng vào chính công việc của họ** thêm một bước không?
- **Giải pháp công nghệ AI:** có chạm một **mục tiêu / nỗi đau / vấn đề** mà một gói hay giải pháp công nghệ giải được, hoặc cho thấy David làm được thật không?

**Cây nội dung kênh trainer** (hồ sơ David mục 4.2): **Gốc** = làm chủ bản thân · **Nhánh chính** = áp dụng vào công việc của chính
họ · **Nhánh phụ** = mối quan hệ, chỉ khi bắt nguồn từ bản thân · **Nhân hiệu** = đời thường / hành trình của David, chỉ khi giúp người
xem tin David là trainer.

**Bán được gì (bắt buộc mọi phiếu):** mục tiêu / nỗi đau → gói nào → bước phễu tiếp theo (`du-an/pheu-ban-hang-goi-cong-nghe.md`).

## 1b. Đối chiếu kho 100 video (bắt buộc với hướng trainer)
Kho `du-an/ke-hoach-noi-dung-100-video.md` là **kế hoạch nội dung** của kênh: dần dần mọi video phải đi theo kho, tránh làm video lệch mục tiêu.
Đọc phần "Luật đối chiếu" ở đầu kho, rồi tìm (`grep` nỗi đau / cách làm / từ khoá của lời chép) ý khớp nhất:
- **Khớp** thì ghi `Kho 100: ý <số> "<nỗi đau>"` + kiểu dẫn dắt của ý đó (kho thắng tỉ lệ tự đếm, trừ khi David chọn khác).
- **Không khớp ý nào** thì ⚠️ cảnh báo trong phiếu, David chọn: thêm làm ý mới (cuối giai đoạn hợp) · cất kho · bỏ. Không tự dựng.
- **Khớp giai đoạn 3** (cơ sở chạy khi vắng chủ) thì không thuộc kênh trainer; hợp gói công nghệ thì chuyển hướng 3.
- Luôn gợi ý **ý kế tiếp nên quay**: ý "Ý tưởng" số nhỏ nhất (bỏ giai đoạn 3) — nhắc David quay theo kế hoạch.
- Sau khi dựng / đăng: đổi cột Trạng thái của ý trong kho (Đã dựng <ngày> · `tap-<tên>` thành Đã đăng <ngày> + link), đẩy GitHub.

## 2. Chấm 5 tiêu chí (0–2 mỗi tiêu chí)
| # | Tiêu chí | 2 | 1 | 0 |
|---|---|---|---|---|
| 1 | **Gắn gốc** | nói thẳng về làm chủ bản thân / áp dụng vào công việc | chạm gián tiếp | không liên quan |
| 2 | **Hữu ích cho tệp** | người lần đầu dẫn người dùng được ngay | dùng được nếu tự liên hệ | không phải tệp |
| 3 | **Hành động** | có việc cụ thể làm theo (Thực thi) | có gợi ý chung | chỉ chia sẻ |
| 4 | **Kéo tương tác** | có câu mở giữ người xem + chỗ hỏi "Vấn đề" / "Kết quả" tự nhiên | có một trong hai | không |
| 5 | **Nhân hiệu** | chuyện thật của David, thấy cách David dẫn dắt | có chuyện thật | không |

**Khung 3 phần** Vấn đề · Giải pháp · Thực thi: được **sắp lại thứ tự đoạn** từ nguyên lời David; thiếu hẳn một phần (thường là
Thực thi) thì không bịa, báo "thiếu phần X" để David quyết nói bổ sung hay cất kho.

**Chấm cả câu chuyện, không chấm từng đoạn để giữ đoạn điểm cao**: 70–80% câu chuyện là dẫn dắt, bối cảnh, tình
huống để đoạn đắt có giá trị. Video dài một hướng là bản gốc và để nguyên (quy-tac-chung mục 2); nhiều hướng thì mỗi bản theo hướng
bỏ trọn đoạn ngoài hướng, trong đoạn vẫn để nguyên (mục 0b); video ngắn chỉ trích từ bản đó. Claude chỉ đọc lời chép, không
cảm được giọng và sức nặng câu chuyện, nên không quyết đoạn nào "ít giá trị".

Chấm 5 tiêu chí trên dùng cho hướng trainer. Hướng khác đổi nghĩa tiêu chí 1–2 theo câu hỏi gốc của hướng (mục 1); tiêu chí 5 =
tin David trong hướng đó.

## 3. Lằn ranh = CẢNH BÁO, David quyết (hồ sơ 4.7 + 7, theo từng hướng)
**Mọi hướng:** phạm pháp hay mập mờ pháp lý (quan trọng nhất) · chữ "chữa lành", công dụng sức khoẻ của sản phẩm · tư vấn thuế, pháp lý · chuyện người khác không ẩn danh (tên thật, nơi làm, chi tiết lộ danh tính khách, học viên, nhân viên) · hứa thu nhập.
**Tài chính:** cam kết lợi nhuận · gọi lệnh mua/bán cụ thể · thiếu cảnh báo rủi ro · nhắc đơn vị không được cấp phép.
**Trainer:** trị liệu, chẩn đoán tâm lý · nhắc vai coach trên kênh công khai · nói giá, tên gói dịch vụ trên video · đọc số của người thật khi họ chưa đồng ý · hứa tiền hay kết quả nhờ con số · nghi thức cầu xin, phóng sinh. Còn nội dung từ trường số (kèm dẫn chứng thần số học, thiền, "nghiệp"…) thuộc hướng trainer, được nói công khai (hệ 135, hồ sơ 4.1).
**Gói công nghệ:** hứa kết quả gói chưa làm ra thật. Giá sản phẩm công nghệ của David được công bố (tự quảng bá), không phải lằn ranh.
Chạm thì **luôn cảnh báo trong phiếu và báo cáo**: mốc giây, lời chạm, rủi ro. Mặc định **giữ lời, không tự cắt** (David có thể đã tự cân đối khi kể); David muốn cắt thì nói ở bản cuối. Ghi "đã cảnh báo" vào sổ; chữ đồ hoạ, tiêu đề, thumbnail, mô tả, clip ngắn vẫn không lấy nội dung đó.

## 4. Bảy kết luận
| Nhãn | Khi | Làm |
|---|---|---|
| ⭐ **Rất tốt** | 9–10, không chạm lằn ranh | đủ bộ: YouTube (bản gốc / biên tập) + highlight Reels, TikTok + bài viết trang |
| ✅ **Phù hợp** | 7–8 | theo kênh đề xuất (thường YouTube hoặc highlight + bài viết) |
| ✂️ **Trích ngắn từ gốc** | bản dài đã duyệt có đoạn đắt cho video ngắn | bản dài vẫn để nguyên làm gốc; clip là phần thêm, không thay bản dài |
| 🔁 **Trùng / dư** | đã có bài gần giống trong 30 ngày, hoặc nhánh đang quá tỉ lệ | gộp vào bài cũ / để sau |
| 🗂 **Lưu kho** | có giá trị nhưng chưa đúng lúc / chưa đủ 3 phần | lưu lời chép + nhãn, chờ ghép series |
| 👤 **Chỉ Facebook cá nhân** | tối đa 6, đời thường có ích cho nhân hiệu | câu chia sẻ ngắn, không dựng nặng |
| ⛔ **Không làm** | không liên quan, hoặc David chọn không làm sau cảnh báo lằn ranh | không dựng, không tốn thời gian |

## 5. Phân phối kênh (`ho-so-thuong-hieu/kenh.json`)
Theo hướng (mục 0): **YouTube David Trần Official** = hướng tài chính · **YouTube trainer** = bản gốc hoặc biên tập hướng trainer ·
**Facebook cá nhân, fanpage, TikTok** = chia sẻ không giới hạn chủ đề, cũng nhận highlight của hai kênh YouTube, nhưng mỗi bài phải
dẫn về gói (thường là gói công nghệ) theo phễu `du-an/pheu-ban-hang-goi-cong-nghe.md`. Lịch thứ Ba + thứ Sáu 20:00 giờ Việt Nam. Phiếu lọc gán kiểu dẫn dắt
mỗi bài (**Không · Gợi mở · Mời**, tỉ lệ và cách viết: khối 08).

## 6. Phiếu lọc (gửi David — một màn hình)
```
📥 <tên file> · <độ dài> · <loại dựng: làm video / ghép vlog / podcast / highlight>
Phân hướng: H1 <bản / không> · H2 <bản, ~phút> · H3 <bản, ~phút> · Bỏ: <lý do> (chi tiết: phan-huong.md)
Bán được gì (mỗi hướng có bản): <nỗi đau → gói → bước phễu tiếp>
Kết luận: <nhãn> · <điểm>/10   (Gốc x · Tệp x · Hành động x · Tương tác x · Nhân hiệu x)
Lý do: <1–2 dòng>  · Lằn ranh: <không / ⚠️ chạm ở mm:ss, lý do, rủi ro → mặc định giữ lời, không làm đồ hoạ>
Nhánh: <gốc / công việc / quan hệ / nhân hiệu> · Trùng sổ 30 ngày: <… / không>
Kho 100: <ý số … "nỗi đau" · dẫn dắt theo kho / ⚠️ không khớp ý nào / ⚠️ giai đoạn 3 không làm> · Ý kế tiếp nên quay: <số + nỗi đau>
Đề xuất: <sản phẩm → kênh → ngày giờ> (vd. YouTube bản biên tập ~9 phút T3 20:00 · 2 highlight Reels+TikTok T6 · bài viết trang)
3 phần: Vấn đề <mm:ss> · Giải pháp <mm:ss> · Thực thi <mm:ss / THIẾU>
Câu mở: "<trích lời>" · Bình luận: "Vấn đề" / "Kết quả" · Dẫn dắt: <Không / Gợi mở / Mời>
Đã chọn: <mỗi lựa chọn Claude tự chốt + lý do một dòng — David sửa ở bản cuối nếu muốn>
```

## 7. Sổ danh mục `~/Movies/_danh-muc-noi-dung/danh-muc-noi-dung.md`
Một dòng mỗi tài nguyên: ngày · file · nhãn · điểm · nhánh · kênh · dẫn dắt · trạng thái (lọc / dựng / chờ đăng / đã đăng / kho / bỏ).
Mỗi lần lọc, Claude xem sổ và CẢNH BÁO trong phiếu: nhánh nào đang quá nhiều / thiếu (mục tiêu: gốc + công việc ít nhất 70%), tuần chưa có
bài Mời, kho quay sẵn < 4 video, lịch thứ Ba / thứ Sáu tới chưa có bài, chủ đề trùng trong 30 ngày.
