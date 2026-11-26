---
description: "Điểm vào tư duy dựng video: loại nội dung cả video → người xem gặp khó gì ở từng đoạn → nguyên lý (12 nguyên lý Mayer + 4 nhu cầu ngoài Mayer) → cách thể hiện. AI nào đọc cũng tự lập luận được, không cần tra bảng."
---

# Nhu cầu người xem — tư duy dựng video

File này dạy **cách nghĩ**, không phải danh mục có sẵn. Bất kỳ AI nào (Claude, Codex, Gemini…) trên thiết bị nào, chỉ cần đọc file này rồi
`huong-dan-lua-chon.md` là dựng được video phù hợp nội dung. Kho kiểu thể hiện (`bo-cuc.md`, khối 07) chỉ là **các cách thể hiện có sẵn**; không có cách
nào khớp thì AI tự sáng tạo theo nguyên lý (cảnh tự vẽ `ve`).

## 0. Thứ tự suy nghĩ (luôn đi đủ các bước, ghi lại thành văn bản)

1. **Cả video thuộc loại nội dung nào?** (mục 1) Từ đó xác định người xem đến để làm gì: hiểu, nhớ, tin, hay cảm. Câu trả lời này quyết định
   mật độ hình, nhịp, nhạc, cách mở và kết cho **cả video**.
2. **Từng đoạn: nếu chỉ nghe, người xem có gặp khó không? Khó gì?** Nếu không khó thì chỉ để người nói và phụ đề, không dựng thêm gì (nguyên lý
   Tinh gọn). Nếu khó thì gọi tên điểm khó (không biết đang ở đâu, không hình dung được, không so sánh được, quên ý trước, không tin…).
3. **Điểm khó đó do nguyên lý nào giải quyết?** (mục 2, 3) — một đoạn thường chỉ cần một nguyên lý chính.
4. **Cách thể hiện:** chọn trong kho cách đúng nguyên lý nhất (`huong-dan-lua-chon.md` bước 4); nếu không có thì tự vẽ. Sau đó đọc dòng
   **"phản tác dụng khi"** của nguyên lý để tự kiểm.
5. **Ghi lại** vào `ke-hoach-canh.md` (mục 4). Công cụ kiểm tra (`soat-canh.mjs`) chặn khi thiếu.

Luật bắt buộc vẫn áp dụng cho mọi lựa chọn: chữ trên hình là **nguyên văn lời người nói**; không che mặt; chữ ký nhận diện (màu cam, hai
font, dấu góc, phụ đề, thanh thời gian, màn chốt) không đổi (`README.md` mục 1, 3).

## 1. Loại nội dung cả video

Danh sách loại lấy từ các video kênh đã làm (`du-an/danh-muc-noi-dung.md`). Loại mới xuất hiện qua video quay thêm thì thêm dòng ở đây và ở `nguyen-ly.json`.

| Loại (`Loại:`) | Nhận ra bằng | Nhu cầu chính của người xem | Nguyên lý ưu tiên | Mức hình · nhịp · nhạc | Tránh |
|---|---|---|---|---|---|
| `day-ky-nang` — dạy kỹ năng, chia sẻ kiến thức | có vấn đề → cách làm → bước; nhiều liệt kê, con số, "đầu tiên… sau đó…" | **hiểu + nhớ** để làm theo | Chia đoạn, Biết trước, Lời kèm hình, Báo hiệu | hình vừa phải ở ý khó (bước, so sánh, con số); nhịp đều; nhạc `kien_thuc` | dựng hình cho cả câu dễ; chữ dài trên hình |
| `chia-se-quan-diem` — quan điểm, lý do, góc nhìn | "tôi nghĩ", "lý do là", lập luận A vì B; ít bước | **hiểu lập luận + tin** người nói | Báo hiệu (chỗ chốt), Lời kèm hình (quan hệ vì–nên), Tin | hình thưa, ở chỗ chuyển ý và câu chốt; nhịp chậm vừa | biến quan điểm thành "bước"; minh hoạ tự đặt |
| `ke-chuyen` — chuyện đời, hành trình | thời gian quá khứ, "hồi đó", cảm xúc, nhân vật | **cảm** rồi mới hiểu bài học | Cảm xúc, Mặt người nói, Tinh gọn | rất ít hình; chữ nhấn ở đỉnh cảm xúc; nền hạt / người mờ; nhạc `tam_su` / `y_nghia`, chuyển cảnh lắng | sơ đồ giữa lúc kể; nhạc sôi động |
| `suy-ngam` — độc thoại, podcast một người | nói liền, ít nhìn vào bước cụ thể, câu hỏi tự vấn | **theo kịp mạch** suy nghĩ | Chia đoạn, Báo hiệu, Giọng trò chuyện | chủ đề đang bàn + màn chương; hình ở câu then chốt; nhịp chậm | phủ hình liên tục |
| `tro-chuyen` — trò chuyện, phỏng vấn hai người | hai giọng, hỏi – đáp | **biết ai đang nói gì, trả lời cho câu nào** | Báo hiệu (thẻ câu hỏi, tên), Gần chỗ, Mặt người nói | thẻ cạnh người nói; ô người bám đúng người; nhạc theo cảm xúc chủ đạo | che mặt người kia; hình toàn khung lâu |
| `loi-chung` — lời chứng học viên, khách hàng | một người kể kết quả với David / khoá học | **tin** (người thật, vai trò thật, kết quả thật) | Tin, Mặt người nói, Báo hiệu (tên · vai trò) | giữ người là chính; thẻ tên + vai trò; minh chứng (ảnh, trước/sau) nếu có | lời quảng cáo tự đặt; số liệu không do họ nói |
| `vlog` — đời thường, sự kiện | nhiều cảnh, di chuyển, ít lời liền | **cảm không khí + theo được hành trình** | Cảm xúc, Chia đoạn (vòng, nơi chốn), Giữ chú ý | thẻ nơi chốn, tên vòng; nhạc theo không khí; mẫu ghép | thẻ kiến thức dày |
| `huong-dan-man-hinh` — quay màn hình, thao tác, cuộc gọi | chủ thể là màn hình / người không nhìn camera | **thấy đúng chỗ đang thao tác + giữ được ý** | Gần chỗ, Báo hiệu, Chia đoạn | khung chủ thể + bảng ghi chú chạy; nhãn sát chỗ thao tác | che vùng thao tác; hình rời màn hình lâu |
| `meo-ngan` — mẹo nhanh dọc, một ý | tối đa 90 s, dọc, một lời khuyên | **bắt được ý trong vài giây + nhớ** | Giữ chú ý, Báo hiệu (từ khoá to), Tinh gọn | mỗi thời điểm một điểm nhìn; hình lớn ít chữ; nhịp nhanh, nhạc `vui` hoặc theo cảm xúc | nhiều lớp cùng lúc |

Một video có thể **kết hợp** hai loại (ví dụ: kể chuyện rồi rút bài học = `ke-chuyen` → `day-ky-nang`): ghi loại chính và đoạn đổi loại.
Clip highlight lấy loại của đoạn gốc.

## 2. Mười hai nguyên lý (Richard Mayer, *Multimedia Learning*)

Tên tiếng Anh giữ đúng nguồn, mỗi tên **một** bản dịch (dùng đúng chữ đó trong dòng `Cần:`). Nghiên cứu gốc đo trên bài giảng; kênh
áp dụng vào video người nói trên mạng xã hội, chỗ nào khác hoàn cảnh thì ghi rõ "Ở kênh này".

### Tinh gọn — Coherence Principle
- **Cái khó:** yếu tố không mang nghĩa (trang trí, nhạc to, hình chỉ để giải trí) chiếm dung lượng nhận thức, người xem hiểu ít hơn.
- **Làm:** chỉ dựng hình cho ý khó hiểu nếu chỉ nghe; nền tĩnh; mỗi thời điểm một điểm nhìn; hình phủ quá khoảng 45 % thời lượng là thừa.
- **Phản tác dụng khi:** bỏ cả hình ở ý thật sự khó (quy trình, so sánh) chỉ để "gọn".
- **Đã học:** Ali–Joseph (bỏ chữ sau người, "nhiều hiệu ứng quá bị rối"); Cường Mê AI (ít chữ, nền tĩnh); MagentX (reel đồ hoạ dày nhất ít lượt xem nhất).

### Báo hiệu — Signaling Principle
- **Cái khó:** người xem không biết chỗ nào quan trọng, đang ở phần nào.
- **Làm:** một điểm sáng (mục đang nói màu cam, mục cũ mờ); từ nhấn `*từ*`, từ khoá to `^`; màn chương, thanh tiến trình, số thứ tự to; thẻ câu hỏi ở phỏng vấn.
- **Phản tác dụng khi:** báo hiệu mọi thứ — nhiều điểm sáng cùng lúc thì không điểm nào nổi bật.
- **Đã học:** Ali (tiến trình, mục lục); Cường Mê AI (một điểm sáng); MagentX (số to, từ khoá to, thẻ câu hỏi, mẫu đừng/hãy lặp).

### Không trùng kênh — Redundancy Principle
- **Cái khó:** vừa nghe lời vừa phải đọc nguyên câu đó trên hình thì mắt và tai tranh nhau xử lý.
- **Ở kênh này:** phụ đề luôn chạy vì nhiều người xem không bật tiếng. Vì vậy: khi hình có chữ thì phụ đề nhường (mỗi thời điểm một vị trí chữ);
  chữ trên hình chỉ là cụm then chốt 1–3 chữ nguyên văn, không chép cả câu.
- **Phản tác dụng khi:** bỏ phụ đề ở video dọc ngắn.

### Gần chỗ — Spatial Contiguity Principle
- **Cái khó:** nhãn đặt xa đối tượng nó mô tả thì mắt phải đi tìm.
- **Làm:** nhãn sát hình; thẻ cạnh người đang nói (`the-canh`, `cho.js`); ở quay màn hình, nhãn sát chỗ thao tác; trước/sau đặt cạnh nhau (`tren-duoi`).
- **Phản tác dụng khi:** "sát" tới mức che mặt hoặc che vùng thao tác.

### Đúng lúc — Temporal Contiguity Principle
- **Cái khó:** hình hiện trước hoặc sau lời thì người xem không liên kết được hình với lời.
- **Làm:** lời nói tới đối tượng nào thì đối tượng đó mới hiện (`at` = lúc nói); không hiện cả danh sách một lần.
- **Phản tác dụng khi:** hiện quá sát khiến chữ chưa kịp đọc đã tắt (công cụ kiểm tra đo thời gian đọc).
- **Đã học:** Cường Mê AI (hình theo nhịp lời); Sang Huỳnh (chữ xây theo lời).

### Chia đoạn — Segmenting Principle
- **Cái khó:** nội dung dài liền một mạch thì người xem mệt và mất mạch.
- **Làm:** chia phần (chương, tiến trình ý, mục lục tích luỹ); một hình lớn dần qua các ý nối nhau (`chuoi`, `xay-tang`, `mach.js`); mẫu lặp cho danh sách (`dung-hay`).
- **Phản tác dụng khi:** chia nhỏ quá mức video ngắn một ý thành nhiều màn.

### Biết trước — Pre-training Principle
- **Cái khó:** gặp khái niệm lạ giữa lúc đang theo bước thì người xem vừa phải hiểu từ, vừa phải theo bước.
- **Làm:** khi người nói báo trước video / tập này nói về gì hoặc gồm những phần nào ("trong video này có 3 điều", "đây là tập cuối của
  loạt bài Tết, chủ đề là…", "trước hết hiểu X là gì") thì mục lục, màn chương mở đầu, thẻ khái niệm hiện trước phần chi tiết.
- **Khác Báo hiệu:** Biết trước là cho người xem **bản đồ trước khi vào** (đầu video, đầu phần); Báo hiệu là đánh dấu **chỗ quan trọng
  hoặc đang ở đâu** khi đã vào giữa nội dung. Cùng một màn chương: đặt ở lời giới thiệu mở tập là Biết trước, đặt ở chỗ đổi phần là Báo hiệu.
- **Phản tác dụng khi:** tự thêm phần giới thiệu mà người nói không nói (trái luật nguyên văn).

### Nghe thay đọc — Modality Principle
- **Cái khó:** giải thích bằng chữ in dài trên hình khó tiếp nhận hơn so với nghe giải thích kết hợp nhìn hình.
- **Làm:** để lời nói giải thích, phần hình chỉ gồm hình và nhãn ngắn; không dùng thẻ chữ dài khi người đang nói chính ý đó.
- **Phản tác dụng khi:** câu chốt cần nhớ nguyên văn — khi đó chữ to một câu là đúng (màn chốt).

### Lời kèm hình — Multimedia Principle
- **Cái khó:** ý trừu tượng (quan hệ, cấu trúc, con số) chỉ nghe thì khó giữ.
- **Làm:** dựng hình cho đúng **cấu trúc của câu**: tầng bậc thì `tang`; trong ra ngoài thì `vong`; từ … thành thì `tu-thanh`; bước thì `chuoi`; so sánh thì `vs`, `dung-hay`; con số thì `count`.
- **Phản tác dụng khi:** hình chỉ lặp lại lời mà không thêm cấu trúc (biểu tượng chỉ để trang trí).

### Giọng trò chuyện — Personalization Principle
- **Cái khó:** lời trang trọng, xa cách thì người xem ít gắn kết.
- **Ở kênh này:** lời là của David (nguyên văn), vốn đã mang giọng trò chuyện. Phần hình giữ đúng giọng đó: chữ trích lời "mình – bạn", không đổi sang văn quảng cáo.

### Giọng thật — Voice Principle
- **Cái khó:** giọng máy làm giảm mức tin tưởng và mức hiểu.
- **Ở kênh này:** chỉ dùng giọng thật của người nói; không lồng giọng AI.

### Mặt người nói — Image Principle
- **Nguồn nói:** thêm hình người nói lên màn **không tự làm** người xem hiểu bài hơn.
- **Ở kênh này:** vẫn giữ mặt David phần lớn thời gian vì nhu cầu **Tin** và **Cảm xúc** (mục 3), không vì hiểu. Hệ quả: khi đoạn
  cần hiểu (hình phức tạp), được phép thu người vào ô (`o-nguoi`, `o-tron`, `nguoi_duoi`) để nhường chỗ cho hình.
- **Phản tác dụng khi:** giấu mặt ở đoạn kể chuyện, lời mời, cảm xúc.

## 3. Bốn nhu cầu ngoài Mayer

Mayer đo việc **hiểu**. Video trên mạng còn phải được **xem tới cuối**, được **tin** và được **nhận ra**. Bốn nhu cầu này ghi rõ "ngoài Mayer".

| Tên (`Cần:`) | Cái khó | Làm | Phản tác dụng khi | Nguồn |
|---|---|---|---|---|
| **Giữ chú ý** | 3 giây đầu không có lý do ở lại; một bố cục kéo dài quá lâu thì người xem lướt qua | mở bằng câu then chốt của chính người nói; đổi lớp mỗi vài giây nhưng mỗi thời điểm chỉ một yếu tố mới; kết quả trước, cách làm sau | đổi liên tục không có nghĩa (giật, chớp) | kinh nghiệm giữ chân YouTube (Paddy Galloway); MagentX |
| **Cảm xúc** | người xem không cảm thì không nhớ, không hành động | giữ mặt, giữ khoảng lặng ở đỉnh cảm xúc, nhạc đúng cảm xúc, chữ nhấn ít | phủ hình hoặc nhạc lên câu cảm xúc | Walter Murch, *In the Blink of an Eye* (Rule of Six: cảm xúc trước) |
| **Tin** | người xem không chắc người nói có thật sự làm được không | mặt thật, minh chứng thật (ảnh, trước/sau, màn hình), tên + vai trò người làm chứng | dựng số liệu / lời mà người nói không nói | MagentX (lời chứng có vai trò, trước/sau) |
| **Nhận diện** | người xem không nhận ra đây là kênh David | giữ chữ ký nhận diện ở mọi video | thêm màu / font của nguồn học | `thu-vien-tai-nguyen/nhan-dien-chung.md` mục 0 |

## 4. Ghi gì vào `ke-hoach-canh.md`

Trong mục `## Chẩn đoán` (cùng các dòng của `huong-dan-lua-chon.md`):
```
Loại: day-ky-nang vì <dấu hiệu thấy ở lời / hình> · cần chính: hiểu + nhớ
```
Ngay dưới, **mỗi cảnh một dòng** (cảnh cố định như dấu kênh, tiêu đề, màn chốt thì không cần):
```
- s03 · Cần: Chia đoạn · Vì: 5 bước kể liền, chỉ nghe sẽ lạc bước 3 · Làm: diagram chuoi, bước đang nói sáng
- s04 · Cần: Cảm xúc · Vì: đỉnh câu chuyện, cần thấy mặt · Làm: nhan làm tối nhẹ, chữ nhấn một từ
```
`Cần:` dùng đúng tên ở mục 2–3 (danh sách cho công cụ đọc: `nguyen-ly.json`). Công cụ kiểm tra: thiếu `Loại:` hoặc không cảnh nào có dòng `Cần:` thì P0
(không render); một cảnh thiếu dòng, hoặc tên nguyên lý / loại không có trong danh sách thì P1.

## 5. Khi đi ngược nguyên lý là đúng

Nguyên lý là cách nghĩ, không phải luật bắt buộc. Có lý do rõ (người dùng yêu cầu trong `yeu-cau.md`, nội dung đặc biệt) thì làm khác,
nhưng ghi vào dòng `Vì:` nguyên lý nào bị bỏ và vì sao. Chỉ luật bắt buộc ở mục 0 là không bao giờ đổi.

## 6. Học thêm

Học nguồn mới theo `README.md` mục 4; điều học được ghi vào dòng "Đã học" (hoặc cột "Nguồn") của đúng nguyên lý ở đây.

**Học qua trường hợp thực tế:** [truong-hop-da-giai.md](truong-hop-da-giai.md) — 19 khoảnh khắc từ 8 hình mẫu thành công cùng thể loại, mỗi trường hợp đủ Cần · Vì · Làm.
**Tự kiểm:** [bai-kiem/](bai-kiem/README.md) — 10 đoạn, AI làm rồi chấm bằng `cham.py`, đạt ít nhất 8/10.
