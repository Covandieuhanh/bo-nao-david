# Khối 07-canh-minh-hoa: Bố cục tự cân (lớp trình bày) + cảnh minh hoạ + điểm nhấn trên người: biểu tượng vẽ, số chạy, sơ đồ + nhãn ≤ 3 chữ; ảnh thật chỉ khi cần

**Dùng trong:** cả 4
**Đầu vào:** lời (mốc từ words.srt)
**Đầu ra:** cảnh `illus` / card / montage… trong scenes.js · `illus` trong OVERLAYS
**Tham số hồ sơ:** chung: canh_minh_hoa.*, hai_trang_thai, <loai>: mat_do_canh_s
**Sửa khối này → chạy lại:** 05, 17

**File thật (code, một bản duy nhất):**
- `thu-vien-hinh/{chuyen-dong.js,ChuHien.jsx,mach.js}` · cảnh tự vẽ: `remotion-template/src/rieng/` (mẫu `MauMach.jsx`)
- `thu-vien-hinh/Illus.jsx (một nguồn)`
- `video-style-edit/assets/remotion-template/src/components/{CardFull,FullScreen,Action,Icons}.jsx`
- `video-style-edit/scripts/openverse.py`
- `video-style-edit/references/scene-design.md`

## Motion graphic KỂ CHUYỆN — tự do sáng tạo (David chốt 2026-11-09, đứng trên mọi mục bên dưới)
Motion graphic là để **diễn tả lại câu chuyện**, không phải đưa hình vào cho có. AI sáng tạo theo từng video, không dập khuôn.
- **Giữ cố định = chữ ký nhận diện** (David chốt 10/11/2026, `lib/nhan-dien-chung.md` mục 0): dấu góc, phụ đề, thanh thời gian,
  màn chốt, thẻ cuối, màu nhấn cam, hai font chính. Đủ để người xem nhận ra video của David.
- **Tự do:** nền (tối, sáng, giấy, người mờ), kết cấu, kiểu hình (biểu tượng nét tròn, phấn, ảnh, bóng người), chữ nhấn phụ,
  bố cục, chuyển động, độ dài, số cảnh. Danh mục kiểu cảnh dưới đây (`nhan`, `bocuc`, `illus`, `diagram`, `card`…)
  chỉ là công cụ có sẵn — dùng khi hợp, không bắt buộc. Cần hình riêng thì viết **cảnh tự vẽ** (`type: 've'`): component React riêng của
  video trong `motion/src/rieng/` (đăng ký ở `rieng/index.js`, xem mẫu `MauMach.jsx`), dùng `lib/chuyen-dong.js`, `lib/ChuHien.jsx`, `lib/cho.js` (tránh người).
- **Một hình diễn tả 1–2 ý, hoặc cả video:** không phải mỗi câu một hình. Trước khi viết cảnh, đọc cả lời và vẽ **mạch hình** — hình
  chính của câu chuyện sẽ lớn dần theo video.
- **Ý quay lại → vẽ tiếp:** người nói nhắc lại hay đi tiếp ý trước thì cảnh sau **vẽ tiếp lên hình đã có** (thêm nét, đổi trạng thái,
  đi tiếp con đường), không vẽ hình mới rời rạc. Dùng `lib/mach.js`: cùng component, `buoc` tăng dần, `tu_buoc` = bước đã vẽ ở cảnh trước.
- **Vẫn giữ:** chữ trên màn hình nguyên văn lời người nói (được rút gọn, đặt ở khoá `text`/`label`/`lines`/`quote`/`title` để máy soát);
  không che mặt khi vẽ cạnh người; câu cảm xúc, chuyện riêng thì để thấy mặt; đã vào là đứng yên; luật chuyển động cuối khối.
- **Mặt người / hình chiếm bao nhiêu:** AI tự cân theo câu chuyện, không con số cố định.
- Ghi trong `ke-hoach-canh.md`: mạch hình của video (một đoạn), mỗi cảnh vẽ bước nào của mạch, vì sao.

## Đường cảm xúc + một đỉnh (David chốt 2026-11-10 — luật ở `luat-chung.md` mục 2, học từ scroll-craft)
Viết **trước** bảng cảnh, vì cảm xúc chọn kiểu cảnh chứ không ngược lại. Ghi vào `ke-hoach-canh.md` ngay dưới mạch hình:
```
## Đường cảm xúc
0:00–0:40  tò mò     → câu hỏi David đặt ra, mặt cận, chưa có hình
0:40–2:10  day dứt   → chuyện thật, để thấy mặt, ít hình
2:10–2:30  lặng      → (trước đỉnh) chỉ phụ đề
2:30–3:00  vỡ ra     → ĐỈNH: cảnh vẽ lớn nhất của mạch hình
...
Đỉnh: 2:30 — "<câu người xem sẽ kể lại với bạn>"
```
- Gợi ý cảm xúc (không đóng): tò mò, nhận ra mình, day dứt, nghi ngờ, căng, vỡ ra, nhẹ nhõm, gần gũi, tin, quyết, bình yên.
- Cảm xúc được định nghĩa bởi cái đứng trước nó: nhẹ nhõm cần căng phía trước, vỡ ra cần lặng phía trước.
- **Một đỉnh**, thường là câu đắt nhất của David. Đỉnh nhận cảnh lớn nhất (thường là bước lớn nhất của mạch hình); không có ba đỉnh tranh nhau.
- Mỗi cảnh trong bảng cảnh ghi thêm cột "cảm xúc", lấy từ đường này.

## Chiều sâu, nền, chữ nhấn (David chốt 2026-11-10 — học Ali Abdaal + Joseph Video Editing)
Thêm vào kho, dùng khi hợp nội dung (cách viết + khi nào dùng: `../../trinh-bay/bo-cuc.md` mục "Chiều sâu, nền, chữ nhấn"):
- **`chusau`** chữ to sau người / `bong: true` bóng người trên nền giấy. Sau khi viết scenes.js: `python3 -I $SKILL/scripts/tach_nguoi.py "$P"`
  (Vision tách người từng khung). Chữ nguyên văn, 2–6 chữ; chụp thử xem người che có làm mất chữ không.
- **`bocuc` `muc-luc`** (mục lục tích luỹ) · **`tien-trinh`** (thanh tiến trình ý) · **`canh-nguoi`** (mạch hình vẽ cạnh người, không thẻ).
- **`phong: 'nguoi-mo' | 'hat'`** ở cảnh toàn màn hình: nền là người nói làm mờ / nền hạt, thay nền tối mặc định.
- **`*từ*`** trong mọi chữ: một từ nhấn font phụ nghiêng màu cam; tối đa một chỗ mỗi cụm.
- Mỗi khung **một tiêu điểm**; cam chỉ là màu nhấn (khoảng 10 % khung) — soát ở khối 17.

## Không hai cảnh cùng kiểu liền nhau (David chốt 2026-11-10)
Hai cảnh đi liền nhau không cùng kiểu (`type` + `mode` / `kieu`, ví dụ hai `bocuc` `the-canh` liền nhau). Xen kiểu khác: `nhan` zoom,
biểu tượng, sơ đồ, toàn màn hình… Không con số tối thiểu (bố cục tự cân). **Ngoại lệ:** cảnh "vẽ tiếp" cùng mạch hình (`tu_buoc`) được
nối nhau. `soat_canh.mjs` (khối 17) tự nhắc P2.

## Bố cục tự cân (David chốt 2026-11-07 — thay luật 2 trạng thái ngày 04/11)
Không con số bắt buộc. Mỗi đoạn chọn bố cục từ **`../../trinh-bay/bo-cuc.md`** theo 4 câu hỏi ở `../../trinh-bay/README.md`
(cần thấy người hay thấy ý · ý dài hay ngắn · khung còn chỗ không · trước / sau là gì). Ngang tự do; dọc mỗi lúc ít thứ. Ghi lý do
một dòng mỗi cảnh vào `ke-hoach-canh.md`. Bố cục mới học được → thêm vào `trinh-bay/` + `BoCuc.jsx`, giữ chữ ký nhận diện.
Bố cục đã có code: người + phụ đề · `nhan` (dưới đây) · **`bocuc`** (`the-canh` thẻ cạnh mặt · `o-nguoi` người vào ô bo góc + `illus` /
`diagram` / thẻ chữ · `chuong` màn chương — `components/BoCuc.jsx`) · `illus` / `diagram` toàn màn hình. Chữ trong thẻ: nguyên văn.

## Điểm nhấn trên người — `nhan` (David chốt 2026-11-07, nới luật trên)
**Mọi video đều phải có motion graphics** — hiểu là điểm nhấn kéo mắt người xem, có nhiều loại, không chỉ cảnh toàn màn hình.
"Dựng nhẹ" vẫn có (vd. video ~4 phút: ~3 cảnh `illus` + ~4 `nhan` + màn chốt). Trộn loại để mắt không quen; kiểu mạnh nhất để cho câu đắt nhất.
| Kiểu | props | Khi |
|---|---|---|
| Zoom dồn vào mặt | `zoom: 1.15` (1,12–1,2) | cú chốt, câu đắt, lúc cảm xúc lên |
| Làm tối viền | `toi: true` | câu tâm tình / câu muốn người xem lặng lại nghe |
| Chữ nhấn cạnh mặt | `text: 'DÒNG 1\nDÒNG 2'` ≤ 4 chữ, trích lời, dòng cuối màu nhấn; `at` = giây bật | cụm đắt người nói vừa thốt ra |
| Biểu tượng nhỏ cạnh mặt | `icon: '<tên>'`, `at` | vật / việc cụ thể, không cần cả màn minh hoạ |
Ví dụ: `{id: 'n1', type: 'nhan', start: 37.4, end: 42.1, props: {zoom: 1.15, text: 'NHẤC CHÂN LÊN', at: 39.9}}` — 2–5 s, không chồng cảnh khác.
Không che ai: `nhan_place.py` (face_place.sh) ghi mọi người + người đang nói vào `mat.js`; Nhan.jsx đặt chữ / biểu tượng vào khoảng trống sát người đang nói
(`bam` để bám người khác, vd thẻ tên khách), co cỡ theo chỗ, khung dọc hẹp → dưới cằm; render_preview.py zoom dồn vào **người đang nói**. Đoạn chạm lằn ranh: không dùng. Vlog / highlight (khung ghép): dùng `zoom` + `pow` có sẵn, `keep: true`.

**Cảnh B = `illus`** (`thu-vien-hinh/Illus.jsx`, một bản cho mọi khung dựng): hình động minh hoạ ĐÚNG Ý đang nói + **nhãn ngắn**
(tên riêng / con số / cụm đắt — trích lời), dài và dày theo nội dung. Phụ đề vẫn chạy.
| mode | Dùng khi người nói… | items |
|---|---|---|
| `single` | nêu một vật / việc / khái niệm | 1 biểu tượng |
| `flow` | nói nhân quả / các bước ("đi bộ → khoẻ → sống thọ") | 2–3, mũi tên nối, mỗi cái hiện đúng lúc nhắc |
| `vs` | so sánh nên / không nên, trước / sau | 2, `good: true/false` (tick xanh / dấu x đỏ) |
| `count` | nêu con số ("15 phút", "3 năm") | 1 biểu tượng + `num: {to, at, unit}` — ĐÚNG con số người nói |
| `list` | liệt kê 3–5 thứ | 3–5 biểu tượng hiện dần (+ nhãn từng cái) |

Viết ở đâu:
- 1 video / podcast (scenes.js): `{id: 'm1', type: 'illus', start: 33.1, end: 37.0, props: {mode: 'count', items: [{icon: 'clock', at: 33.4}], num: {to: 15, at: 33.6, unit: 'PHÚT'}, label: 'MỖI NGÀY'}}`
- Vlog (plan.json fx): `{"type": "illus", "c": "c3", "at": 82.0, "len": 4, "mode": "flow", "items": [["footsteps", 82.5, "ĐI BỘ"], ["heart", 84.0, "SỐNG THỌ"]]}`
- Highlight / edl.js (OVERLAYS, giây timeline): `{type: 'illus', start: TS(140.2), end: TS(144), mode: 'single', items: [{icon: 'brain', at: TS(140.5)}], label: 'BỘ NÃO'}`
Biểu tượng: `thu-vien-hinh/Icons.jsx` (~60 hình; thiếu thì vẽ thêm lưới 64×64 cùng kiểu nét — thêm ở thư viện là cả 4 loại có).

Tự động (không cần nhớ): lớp chữ cũ (kinetic, lower, listItem, pow, chips, location, nameCard…) nếu vẫn viết → khung dựng tự vẽ
toàn màn hình khi che người (dài theo nội dung); thẻ `card` / `action` bỏ câu trích dài (chỉ hình + nhãn `label`); tít ghim tắt. Muốn giữ
lớp phủ một cảnh: đặt tay `place` (1 video) / `keep: true` (ghép). **Ưu tiên viết `illus`** — lớp chữ tự chuyển chỉ là lưới an toàn.

## Cách làm (chuyển nguyên văn từ SKILL.md cũ — ngày 2026-11-04)

### 5. Lên kịch bản cảnh

**Cảnh cuối luôn là màn chốt**: `{id: 'chot', type: 'cta', start: <thời lượng − 4>, end: <thời lượng>, props: {text, kind}}` (câu tự sáng tạo — luật "Màn chốt" ở đầu file) (thời lượng =
`duration` trong project.js; cảnh trước đó phải kết thúc trước mốc này). **Quét transcript tìm câu hành động** (luật trên) → cảnh
`action` `{icon, quote, quoteAt, doneAt}` ngay lúc nói (doneAt = lúc nói xong cụm việc). Câu hành động rơi vào 4 s cuối → đặt màn
hành động ngay trước màn chốt.

**Cảnh đầu tiên luôn là `hook` (0 → ~3 s)**: tiêu đề nói ngay video về cái gì, rút từ ý chính của cả video
(xem `scene-design.md` mục "Mở đầu 3 giây"). Rồi viết `motion/src/scenes.js` từ transcript theo `references/scene-design.md` (loại cảnh nào cho loại câu nói nào,
mật độ, độ dài, quy tắc không chồng lớp). `references/example-scenes.js` là một kịch bản thật đã được duyệt —
đọc để lấy cảm giác về nhịp và cách gắn mốc thời gian. Ghi `$P/ke-hoach-canh.md`: bảng cảnh (thời gian, loại,
nội dung, minh hoạ: biểu tượng nào / ảnh nào) để người dùng đọc lại sau.

**Lớp phủ KHÔNG được che người nói** (người dùng chốt): mọi chữ/thẻ/hiệu ứng không toàn màn hình mà hình người vẫn hiện
thì phải nằm ở chỗ trống — không cố định một vị trí. Sau khi viết (và mỗi lần sửa mốc) scenes.js:
```bash
zsh $SKILL/scripts/face_place.sh "$P"     # lần đầu dò mặt ~1 phút / 5 phút video (Vision), sau đó chỉ tính lại
```
→ `motion/src/placement.js` (vị trí + cỡ từng cảnh) và `check/faces/placement.md`. Đọc bảng: cột "Lớp phủ" là đáy (mặc định),
đỉnh hay y giữa; cảnh không có chỗ tránh được **mặt + đầu + vai + ngực** → script **tự chuyển toàn màn hình** (luat-chung 4)
— xem dòng tổng cuối bảng, tự cân tỷ lệ người / đồ hoạ theo nội dung (muốn giữ người: dùng `bocuc`). Muốn giữ lớp phủ: `place: {top: <px>, scale: 0.6}`
hoặc `place: {full: false}` trong cảnh (thứ tự khoá: `id, type, start, end, place, props`).
Cảnh toàn màn hình (`FULL`, gồm cả thẻ toàn cảnh) che hết hình nên không cần tránh. Ngang pillar không cần (lớp phủ ở cột trái).

*Khung ngang từ gốc dọc* — viết thêm `SIDES` (mẫu trong scenes.js): `title` = chủ đề video ngắn gọn, `speaker`,
`keywords` = từ khoá ý đang nói (đổi theo từng đoạn ~15–40 s, ≤ 3 từ, mốc = lúc bắt đầu ý), `points` = 5–9 ý chính
theo thứ tự nói (≤ 4 từ mỗi ý, mốc = lúc bắt đầu nói ý đó). Chữ lấy từ lời nói, không bịa. Ô từ khoá tự ẩn khi
thẻ/chữ to chiếm ô; vẫn giữ quy tắc không chồng hai lớp phủ.

### 6. Minh hoạ: biểu tượng vẽ (mặc định) hoặc ảnh

Luật ở `../luat-chung.md` mục 4. Biểu tượng: `icon: '<tên>'` thay `photo` trong `montage` và `card job` (~45 hình ở
`motion/src/components/Icons.jsx`, thiếu thì vẽ thêm trên lưới 64×64 cùng kiểu nét). Lý do không dùng ảnh kho: hay lệch ngữ cảnh,
lạc tông nền tối, phải ghi nguồn, có thể lộ mặt người lạ. Không có ảnh tốt → biểu tượng + tên gọi đúng, không ảnh tạm.
David nói "không dùng ảnh" → không ảnh nào; "thêm ảnh" → tìm ảnh cho mọi thứ cụ thể.

Khi cần ảnh: viết `$P/images/queries.json` (từ khoá tiếng Anh) rồi:
```bash
python3 -I $SKILL/scripts/openverse.py search "$P" "$P/images/queries.json"     # chạy nền, ~20 s/từ khoá
```
Xem từng `images/sheets/<key>.jpg` (8 ảnh, số 0–7 từ trái) và chọn. Loại bỏ: người nổi tiếng/người dễ nhận ra
ở bối cảnh nhạy cảm, logo thương hiệu nổi bật, hình vẽ clip-art lạc tông với ảnh chụp, ảnh mờ/chữ đè, ảnh không
khớp nghĩa. Không có ảnh ổn → thêm từ khoá khác vào queries.json và search lại (chỉ các key đó). Rồi:
```bash
python3 -I $SKILL/scripts/openverse.py fetch "$P" "$P/images/picks.json"
```
Ảnh vào `motion/public/photos/<key>.jpg`; dùng trong scenes.js qua `photo: '<key>.jpg'`.


## Giữ cảnh sau chữ cuối (David chốt 2026-11-05)
Hình / chữ chạy theo lời không tắt ngay khi chữ cuối vừa hiện: hết cảnh ≥ mốc phần tử cuối + 0,5 s hiện vào + **`giu_sau_s` 1,2 s** + 0,3 s
mờ ra (+0,3 s mỗi chữ nhãn vượt 3), tối đa 6 s từ đầu cảnh, không lấn lớp kế tiếp / màn chốt. Khung dựng TỰ kéo dài khi render
(`thu-vien-hinh/giu.js`, dùng ở montage `Show.jsx` + remotion `Root.jsx`) — viết `len` như cũ, không tính tay. `keepEnd: true` = tắt luật cho lớp đó.
Áp cho: illus · action (tính từ `doneAt`) · chips · pow · listItem · kinetic · scene.
Bị chặn bởi trần 6 s (phần tử cuối hiện sau giây thứ ~4 của cảnh) → dời `start`/`at` của cảnh muộn hơn cho phần tử đầu sát lúc nói.
Danh sách `list` 4–5 hình ở khung dọc tự xếp lưới 2 cột (Illus.jsx — trước 2026-11-05 xếp một cột, tràn vùng vẽ).

## Sơ đồ nói thay lời + ảnh khung bo góc (`diagram`, David chốt 2026-11-05)
Không chỉ "biểu tượng + nhãn": khi câu nói có CẤU TRÚC, vẽ chính cấu trúc đó (thư viện `thu-vien-hinh/Diagram.jsx`, mọi chữ trích lời):
| Câu nói có dạng | mode | Ví dụ |
|---|---|---|
| tầng bậc, số lượng giảm dần / tăng dần theo cấp | `tang` | "10.800 thành viên … 108 lãnh đạo … trưởng làng" |
| trong → ngoài, cá nhân → cộng đồng | `vong` | "nhìn vào bên trong … bên ngoài … sứ mệnh" |
| mốc thời gian, chặng đường | `moc` | "năm 2016 hướng dẫn … gần đây gọi tên trainer … CCL Việt Nam" |
| so sánh độ lớn nhiều con số | `cot` | "thu nhập gấp 10 lần" |
| đếm phần trên tổng (đời người, tuần, ngày) | `luoi` (`total`, `upto`) | "80 năm cuộc đời … 30 năm đi làm" |
| trước → sau, từ … thành … | `tu-thanh` | "cộng đồng → nâng cấp thành làng" |
| xây dần từ gốc, tầng sau cần tầng trước ("bản thân → công việc → mối quan hệ") | `xay-tang` (items từ DƯỚI lên) | "muốn lên tầng sau phải qua tầng trước" |
| một thứ giữ nguyên nhưng đổi trạng thái (nhấn vào sự đổi, không so sánh hai bên) | `doi-trang-thai` (2 items; bỏ `icon` ở item sau = giữ hình) | "từ làm thay … thành dẫn đội" |
| việc đi từ người này sang người kia | `chuyen-giao` (items[0] bên giao, giữa = các việc `{icon, label, at}`, cuối = bên nhận) | "báo cáo tuần … xếp lịch … giao lại cho đội" |
| người / nơi / tổ chức có thật | `anh` (ảnh giấy phép mở hoặc ảnh David gửi, khung bo góc + nhãn + nguồn) | "CCL", "Singapore", "Bác Hồ" |
Ảnh: `openverse.py search/fetch` (CC0 / PD / CC BY / CC BY-SA, dùng thương mại) → `motion/public/photos/`, ghi `credit` trên ảnh + `nguon-anh.txt`
cho mô tả. Không có ảnh đúng (logo thương hiệu, ảnh mơ hồ) → dùng sơ đồ, không ép ảnh. Podcast dài: ưu tiên `diagram` hơn `illus`.
Vlog (`plan.json` fx): `{"type": "diagram", "c", "at", "len", "mode", "label", "items": [{"at": giây clip, …}]}`.

## Luật chuyển động (David duyệt 2026-11-06 — học từ tài liệu `motion.md` của HyperFrames, tự viết lại cho khung dựng Remotion)
Chuyển động phải dẫn mắt tới ý đang nói, không để trang trí. Thêm hoặc sửa cảnh thì theo:
- **Đã vào là đứng yên:** không lơ lửng, không vòng xoay, không quầng nhấp nháy lặp lại — đó là dấu hiệu "máy làm". Chuyển động liên tục chỉ giữ khi có nghĩa: sóng âm theo giọng, thanh thời gian, nút mời bấm ở màn kết.
- **Vào có đuôi dài, ra gọn:** ra ngắn hơn vào 40–50% (hiện: vào 8 khung, ra 5 khung).
- **Kiểu vào theo ý của câu**, không để mọi cảnh cùng trồi lên: 1 hình = phóng tại chỗ · nhân quả = đi theo hướng đọc · so sánh = hai phía tiến vào · danh sách = trồi lên lần lượt.
- **Chỉ vị trí và cỡ được nảy nhẹ** (spring damping ~14–15), độ mờ và màu không nảy. Phản hồi một lần thì được (bên nhận đón việc), lặp lại thì không.
- **Vào cảnh qua một vật trên màn hình khi được** (việc bay sang bên nhận, màu tràn từ vật ra), thay vì mờ chồng cả khung.
- **Tiêu đề hiện xong thì đứng yên** tới lúc rời đi.
Không dùng: cắt theo nhịp nhạc (video của David đi theo lời).

### Bổ sung 2026-11-09 (David duyệt — học thêm bản mới của `motion.md` HyperFrames, tự viết lại; code ở `thu-vien-hinh/chuyen-dong.js` + `ChuHien.jsx`)
Không đổi màu, font, bố cục; chỉ nâng cách VÀO, ĐỨNG, RA. Thành phần mới dùng hàm ở `chuyen-dong.js`, không tự đặt easing riêng.
- **Easing theo vai:** vào = đuôi dài (`EASE.vao` exp-out) · zoom/đẩy khung, đổi nền = `EASE.camera` (inOut) · ra = `EASE.ra` (tăng tốc). Một kiểu cho mọi thứ là dấu hiệu "máy làm".
- **Nối gối, so le:** phần sau bắt đầu khi phần trước xong 30–50 %; từ cách nhau 60–120 ms, mục danh sách 40–80 ms.
- **Chữ hiện từng từ, không dịch chỗ** (`ChuHien`): `mo` (mờ 6 px → nét, 0,13 s, cách ~0,067 s) · `muc` (xám nhạt → màu chữ) · `dong` (cả dòng mờ → nét). Kiểu đổi theo cảnh (`kieuChu(id)`), không để mọi cảnh mờ + trượt lên.
- **Thoát:** mờ nhoè + tan 0,13–0,25 s, ngắn hơn lúc vào; khung toàn màn hình vào bằng mờ nhoè → nét (`vaoRa`).
- **Giữ đủ đọc:** 0,5 s + 0,3 s mỗi từ (`docDu`); câu cuối video ≥ 2 s.
- **Lò xo theo ζ** (`loXo(zeta)`): 0,7–0,85 sang, 0,4–0,6 vui; chỉ vị trí/cỡ được nảy.
- **Chuyển cảnh có nguyên do, 3–5 kiểu một video:** tối nhẹ ~40 % trong 3 khung trước cắt cứng · đổi trên cùng nền (mờ ra 8 px → mờ vào) · màu tràn nền · vật trên màn hình lớn dần thành cảnh sau. Tối đa một phần ba số mối nối là cắt cứng.
- **Soát kiểu "máy làm" khi xem chụp thử:** che chữ đi, hình còn kể được ý không; mọi cảnh có vào giống nhau không; có gì còn trôi/phóng sau khi đã vào không.
