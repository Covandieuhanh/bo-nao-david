# Thiết kế kịch bản cảnh

> Chọn bố cục theo `../../thiet-ke-bo-cuc/` và khối 07 (bố cục tự cân, không con số bắt buộc). File này là bảng loại cảnh + props + cách
> trích chữ. Lớp chữ to / thẻ có câu trích dài là kiểu cũ — khung dựng tự đổi chúng thành toàn màn hình, không câu trích; cảnh mới ưu
> tiên `illus`, `nhan`, `bocuc`, `diagram`, `ve`.

## Các loại cảnh có sẵn trong template

| type | Lớp | Dùng cho | props chính |
|---|---|---|---|
| `hook` | chữ (V4) | Thẻ tít 0–3 s — chỉ khi David yêu cầu (khối 06), chữ nguyên văn | eyebrow, lines[2], accentLine |
| `lower` | chữ (V4) | Giới thiệu người nói khi họ tự nói tên | name, role |
| `illus` | **toàn màn hình** | Mọi ý cần hình: biểu tượng vẽ động single / flow / vs / count / list + nhãn ≤ 3 chữ; phụ đề vẫn chạy (khối 07) | mode, items[{icon, at, label?, good?}], label, num |
| `nhan` | **điểm nhấn trên người** | Câu đắt / cú chốt / lúc muốn người xem nhìn vào người nói (không zoom): làm tối viền, chữ nhấn ≤ 4 chữ trích lời hoặc biểu tượng nhỏ bật cạnh mặt (bên phía trống; khung dọc → dưới cằm). 2–5 s. Phụ đề vẫn chạy | text ('DÒNG 1\nDÒNG 2', dòng cuối màu nhấn), icon, at (giây bật), toi (true) |
| `listItem` | nhãn (V4) | Người nói ĐẾM ý (≥ 3): số tròn cam + cụm việc nguyên văn, 2,5–4 s mỗi ý (học BS Tùng, HDK) | n, of (tuỳ chọn), text |
| `kinetic` | chữ (V4) | Một câu khẳng định đắt giá, ≤ 5 từ/dòng, 2 dòng | lines[] (in hoa, có dấu chấm cuối tạo cảm giác chốt) |
| `action` | màn hành động (toàn cảnh) | Người nói nêu việc người xem làm được → biểu tượng vẽ dần trong vòng + ô tick bật lúc `doneAt` + NGUYÊN VĂN câu (`**cụm**` nhấn); phụ đề tạm ẩn. 1–2 / video, 3–5 s | icon, quote, quoteAt, doneAt, eyebrow (chỉ khi trích được) |
| `cta` | màn chốt (toàn cảnh, ~4 s cuối MỌI video) | Video lùi vào khung bo góc phía trên + biểu tượng theo kiểu (tick nhỏ + tiếng ting sau 1,6 s) + câu chốt NGUYÊN VĂN câu David nói cuối video (khối 08); phụ đề nhường. Podcast: chỉ ô câu chốt giữa sân khấu | text, kind (comment · save · follow · share) |
| `card` | thẻ (V3) | Thông tin có cấu trúc. variant: `year` (mốc năm, đếm lùi), `job` (ảnh + tiêu đề), `marketing` (biểu đồ đi lên), `years4` (số lớn + thanh tiến độ), `daily` (đồng hồ + nhãn), `steps` (danh sách tick theo lời; `n` = nhãn số tuỳ chọn), `early` (2 đường so sánh), `vs` (2 dòng trước/sau: rows[{tag,title,note,at,hi}]), `ages` (các mốc số bật lần lượt + nhãn gạch: ages[{v,at}], unit, pill, pillAt), `quote` (eyebrow + câu trích + footer) | eyebrow, title, footer, footerAt, ... |
| `montage` | toàn màn hình (V2) | Liệt kê nhanh nhiều thứ cụ thể có ảnh (nghề, địa điểm, sản phẩm) — mỗi mục ≥ 1,3 s | eyebrow, items[{n,label,photo,at,kicker}], total (số đếm "n / total"), counter: false (bỏ số đếm khi chỉ 2–3 ảnh không phải danh sách) |
| `recap` | toàn màn hình | Tổng kết một con số lớn + các mục đã kể | jobs[], subtitle, subtitleAt |
| `converge` | toàn màn hình | Nhiều thứ → một điểm chung → các hệ quả | jobs[], mergeAt, outputs[{label,at}] |
| `master` | toàn màn hình | So sánh sâu-vs-rộng, một yếu tố đe doạ xuất hiện | masterAt, shallowAt, aiAt, replaceAt |
| `gens` | toàn màn hình | Các lớp chồng lên nhau (thế hệ, tầng, cấp độ) + chữ lớn cuối | eyebrow, layers[{label,at}], years, yearsAt, unit |
| `build` | toàn màn hình | Lộ trình từng bước dựng như tầng nhà (bước 1 = móng) | eyebrow, steps[{n,label,at}] |

Các variant/loại cảnh này sinh ra từ nội dung một video cụ thể. Video mới có nội dung khác → tạo variant mới cùng
ngôn ngữ thiết kế (ví dụ `card` variant `quote`, `stat`, `compare`, `map`; full-screen `timeline`, `checklist`, `vs`).
Đổi tên prop cho hợp nội dung — `jobs` chỉ là tên lịch sử, nghĩa là "các mục".

## Mở đầu 3 giây
0–3 s là lời thật của David nói ngay video về cái gì (khối 06). Khi David yêu cầu thẻ tít `hook`: `start: 0`, `end` ≈ 3 s (kết thúc ở
chỗ ngắt câu gần nhất); `lines` = cụm nguyên văn đắt nhất (2 dòng in hoa, ≤ 4 từ/dòng, dòng nhấn là ý "đắt" nhất), `eyebrow` trích lời
hoặc bỏ trống; không câu kéo ("SỐC", "bí mật…"). Cảnh khác bắt đầu sau `end` của hook. Chế độ ghép nhiều clip: đoạn ghép mở đầu
đóng vai trò này (multi-clip 2d).

## Chọn loại cảnh từ lời nói

Đọc transcript, đánh dấu các "khoảnh khắc" theo thứ tự ưu tiên:
1. **Con số, mốc thời gian, số lượng** ("đi làm từ 2011", "4 năm", "15–30 triệu") → `card` có số chạy.
2. **Liệt kê ≥ 3 thứ cụ thể** → `montage` (có ảnh) hoặc `card steps` (trừu tượng).
3. **Câu chốt / quan điểm** ("không phải ngẫu nhiên", "rất rõ") → `kinetic`.
4. **Khái niệm trừu tượng, quan hệ nhân quả, so sánh** → cảnh toàn màn hình dạng sơ đồ.
5. **Lời giao việc** → `action`; câu cuối → màn chốt `cta` nguyên văn (khối 08).
Dùng `lower` nếu người nói giới thiệu tên.

## Quy tắc
- Không con số bắt buộc về mật độ, độ dài cảnh, tỷ lệ mặt (bố cục tự cân, khối 07). Chỉ giữ khoảnh khắc đắt (con số, tên riêng, so
  sánh, danh sách, câu chốt); bỏ cảnh chỉ nhắc lại điều phụ đề đã nói mà không có hình gì thêm.
- **Không chồng 2 lớp phủ cùng lúc** (thẻ + chữ to). Cảnh toàn màn hình che hết nên không cần lớp khác. Không hai cảnh cùng kiểu liền
  nhau (khối 07 mục 3).
- Thẻ toàn cảnh: cửa sổ cảnh khớp đúng câu được trích (`start` ≈ `quoteAt`, `end` ≈ hết câu) vì phụ đề nhường trong cảnh — đừng
  để cảnh kéo sang câu khác. Đừng để cảnh tồn tại khi người nói đã sang ý khác.
- `start` của cảnh = lúc bắt đầu câu liên quan (lấy từ srt), lệch sớm 0,1–0,3 s cũng được; các phần tử bên trong
  hiện đúng lúc từ khoá được nói (`at`, `footerAt`... theo giây tuyệt đối).
- **Chữ hiệu ứng = trích, không diễn đạt lại.** Được BỎ BỚT chữ cho ngắn (≤ 4–5 từ/dòng), KHÔNG được đổi chữ của người nói bằng chữ
  của mình. Mọi từ trên màn hình phải có trong câu nói cùng mốc (sửa chính tả lỗi Whisper thì được).
  Giữ nguyên: tên riêng, con số/mốc giờ, vế đối lập ("nhiều… nhưng…"), từ phủ định, từ chỉ mức độ ("một trong rất nhiều").
  Ví dụ David đã chỉ ra: nói "có thể dùng AI để tìm được hết" → "DÙNG AI / TÌM ĐƯỢC HẾT", không phải "HỎI AI LÀ RA";
  nói "dương khí nhiều nhưng rất dễ nhiễm lạnh" → giữ cả hai vế, không cắt còn "Rất dễ nhiễm lạnh".
  Toàn bộ lời nói đã có ở phụ đề — chữ hiệu ứng chỉ nhấn ý, nên càng phải đúng chữ người nói.
- Mỗi chữ/nhãn phải là **điều người nói đang nói ở đúng mốc đó**. Khi họ nêu một tên (phương pháp, sản phẩm, địa danh,
  người), nhãn lúc đó chính là cái tên — không đổi thành mô tả chung. Đọc lại từng nhãn đối chiếu câu nói cùng mốc
  trước khi render.

## Vùng an toàn

Dọc 1080×1920 (Reels/TikTok/Shorts): nội dung trong x 70–900, y 210–1420. Ngoài vùng đó chỉ có nền.
- Dưới y 1420: tiêu đề, mô tả, thanh âm thanh của nền tảng.
- Phải x 900: cột nút thích/bình luận/chia sẻ.
- Trên y 210: thanh tab/tìm kiếm.
Component thiết kế trong một dải 435 px (y 985–1420 trong toạ độ component) nên thẻ phải gọn: tối đa ~4 dòng nội dung.
Khi xuất, dải này được thu nhỏ còn 78% và **đặt từng cảnh theo chỗ trống, KHÔNG che mặt/người nói**:
mặc định ngay trên dải phụ đề (y ~941–1280; phụ đề 1280–1420); mặt nằm thấp → dời lên đỉnh vùng an toàn (y 210–549);
không vừa → thu nhỏ 68% / 60%. `vi-tri-khuon-mat.sh` dò mặt và ghi `vi-tri.js`; đặt tay bằng `place: {top, scale}` trong cảnh.
Vùng cấm = đầu (cả tóc) + cằm/cổ; thân người nên tránh khi còn chỗ. Cảnh toàn màn hình không bị ràng buộc này.
Thiết kế component mới không giả định vị trí cố định (vd. "luôn dưới mặt") — chỉ vẽ trong dải, Place lo vị trí.
Ngang 16:9: lề 5% mỗi bên, chừa 15% dưới cho thanh điều khiển/phụ đề.
Kiểm tra bằng `vung-an-toan.py` + `ghep-anh-tinh.sh` — đừng tin vào ước lượng bằng mắt.

## Thẻ = màn hình toàn cảnh
Mọi `card` (trừ podcast) render bằng `the-toan-man.jsx`: nền toàn cảnh, khung thẻ (hình động của variant: số chạy, danh sách tick, đồng
hồ, biểu đồ, biểu tượng vẽ…) ở giữa. `quote` (nếu dùng) = **NGUYÊN VĂN câu người nói** ở đoạn đó (lấy từ phu-de.js, đúng từng chữ —
chỉ sửa chính tả Whisper; không tóm tắt, không diễn đạt lại); câu trích dài thì khung dựng tự bỏ, chỉ giữ hình + nhãn. `**cụm**` = tô
màu nhấn (từ khoá, con số). `quoteAt` = mốc bắt đầu câu. Chữ trong khung thẻ (eyebrow/title/footer) giữ ngắn. Độ dài theo ý chính,
không kéo cả đoạn dài.
Ví dụ: `{type: 'card', start: 33.1, end: 40.0, props: {variant: 'vs', eyebrow: 'ĐI VÀO BUỔI ĐÊM', rows: [...],
quote: 'Ngày trước là đi **xe xăng** thì … chuyển sang đi **VF6, VF7** của công ty thì **đỡ hơn rất nhiều**', quoteAt: 33.4}}`

## Ô chữ tóm ý được ưa
Thẻ/chữ to tóm ý chính (trích lời) là kiểu David thích. Đã thử bỏ hết chữ, chỉ còn hình động (biểu tượng + mũi tên + ✓/✗) — David
thấy kém đẹp hơn. Biểu tượng vẽ thay ẢNH bên trong thẻ/montage, không bỏ hết chữ nhấn.

## Minh hoạ: biểu tượng vẽ (mặc định) hoặc ảnh

- **Mặc định: biểu tượng nét vẽ dần** (`bieu-tuong.jsx`, `<Pictogram>`): `montage` items `{icon: 'mic', label, at}`, `card job` `{icon: 'sneaker'}`.
  Hình có sẵn: sneaker, tray, bricks, welding, hammer, mower, golf, megaphone, guideflag, mic, tv, briefcase, laptop, chart,
  person, people, meditate, heart, bulb, target, chat, book, write (viết ra giấy), check, star, house, building, clock, calendar, money, coins, phone,
  car, globe, pin, mountain, road, stairs, chip, gear, leaf, sun, moon. Đặt tên theo VẬT; chọn hình gần nghĩa nhất, thiếu thì
  vẽ thêm (64×64, 2–5 nét, nét tròn) rồi chụp thử.
- **Ảnh** chỉ khi hình vẽ không thay được cái thật: địa danh/công trình cụ thể, nhân vật có thật (ảnh tư liệu có giấy phép),
  sự kiện/tư liệu quá khứ, minh chứng xác thực, sản phẩm cụ thể — và tìm được ảnh tốt (khối 07 mục 7).
- Số liệu → hiệu ứng (số chạy, biểu đồ, tỉ lệ), chỉ con số người nói đưa ra.
  Ảnh đặt trong khung bo góc; luôn có zoom chậm nhẹ (Ken Burns).
- Ý trừu tượng → sơ đồ/chữ, không ảnh stock sáo rỗng.
