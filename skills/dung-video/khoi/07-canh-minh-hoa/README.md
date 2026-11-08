# Khối 07-canh-minh-hoa: Bố cục tự cân (lớp trình bày) + cảnh minh hoạ + điểm nhấn trên người: biểu tượng vẽ, số chạy, sơ đồ + nhãn ≤ 3 chữ; ảnh thật chỉ khi cần

**Dùng trong:** cả 4
**Đầu vào:** lời (mốc từ words.srt)
**Đầu ra:** cảnh `illus` / card / montage… trong scenes.js · `illus` trong OVERLAYS
**Tham số hồ sơ:** chung: canh_minh_hoa.*, hai_trang_thai, <loai>: mat_do_canh_s
**Sửa khối này → chạy lại:** 05, 17

**File thật (code, một bản duy nhất):**
- `thu-vien-hinh/Illus.jsx (một nguồn)`
- `video-style-edit/assets/remotion-template/src/components/{CardFull,FullScreen,Action,Icons}.jsx`
- `video-style-edit/scripts/openverse.py`
- `video-style-edit/references/scene-design.md`

## Bố cục tự cân (David chốt 2026-11-07 — thay luật 2 trạng thái ngày 04/11)
Không con số bắt buộc. Mỗi đoạn chọn bố cục từ **`../../trinh-bay/bo-cuc.md`** theo 4 câu hỏi ở `../../trinh-bay/README.md`
(cần thấy người hay thấy ý · ý dài hay ngắn · khung còn chỗ không · trước / sau là gì). Ngang tự do; dọc mỗi lúc ít thứ. Ghi lý do
một dòng mỗi cảnh vào `ke-hoach-canh.md`. Bố cục mới học được → thêm vào `trinh-bay/` + `BoCuc.jsx`, không đổi thẩm mỹ.
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
Không che mặt: `nhan_place.py` (face_place.sh) ghi mặt từng cảnh vào `mat.js`; Nhan.jsx đặt chữ / biểu tượng bên phía trống, khung dọc hẹp → dưới cằm;
render_preview.py zoom video gốc canh giữa mặt. Đoạn chạm lằn ranh: không dùng. Vlog / highlight (khung ghép): dùng `zoom` + `pow` có sẵn, `keep: true`.

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
