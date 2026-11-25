---
description: "Khối 07 cảnh minh hoạ: bố cục tự cân, motion graphics kể chuyện, ảnh thật Việt Nam."
---

# Khối 07-canh-minh-hoa: Bố cục tự cân + motion graphic kể chuyện + điểm nhấn trên người + minh hoạ, sơ đồ, chuyển động

**Dùng trong:** cả 4
**Đầu vào:** lời (mốc từ moc-tung-tu.srt)
**Đầu ra:** cảnh `nhan` / `bocuc` / `illus` / `diagram` / `ve` / card… trong canh.js · `illus` trong OVERLAYS · `ke-hoach-canh.md`
**Tham số hồ sơ:** chung: `canh_minh_hoa.*`, `hai_trang_thai`
**Sửa khối này thì chạy lại:** 05, 17

**File thật (code, một bản duy nhất):**
- `thu-vien-tai-nguyen/{chuyen-dong.js,chu-hien.jsx,mach.js,minh-hoa.jsx,so-do.jsx,bieu-tuong.jsx,giu.js}` · cảnh tự vẽ: `mau-remotion/src/rieng/` (mẫu `mau-mach.jsx`)
- `dung-video-theo-phong-cach/assets/mau-remotion/src/thanh-phan/{CardFull,FullScreen,Action,BoCuc,Nhan}.jsx`
- `dung-video-theo-phong-cach/scripts/kho-anh-openverse.py`
- `dung-video-theo-phong-cach/references/thiet-ke-canh.md` (bảng loại cảnh + props)

## 1. Motion graphic kể chuyện — tự do sáng tạo (mục này đứng trên mọi mục dưới)
Motion graphic là để **diễn tả lại câu chuyện**, không phải đưa hình vào cho có. AI sáng tạo theo từng video, không rập khuôn.
- **Giữ cố định = chữ ký nhận diện** (`thu-vien-tai-nguyen/nhan-dien-chung.md` mục 0). Còn lại tự do: nền (tối, sáng, giấy, người mờ),
  kết cấu, kiểu hình (biểu tượng nét tròn, phấn, ảnh), chữ nhấn phụ, bố cục, chuyển động, độ dài, số cảnh.
- **Mọi video đều có điểm nhấn, nhưng chỉ vài kiểu hợp nội dung nhất** (quy-tac-chung mục 0, 4) — "dựng nhẹ" vẫn có điểm nhấn. Kiểu mạnh
  nhất để cho câu then chốt. Danh mục kiểu cảnh dưới đây (`nhan`, `bocuc`, `illus`, `diagram`, `card`…) chỉ là công cụ có sẵn — dùng
  khi hợp, không bắt buộc.
- Cần hình riêng thì dùng **cảnh tự vẽ** (`type: 've'`): component React riêng của video trong `chuyen-dong/src/rieng/` (đăng ký ở
  `rieng/diem-vao.js`, xem mẫu `mau-mach.jsx`), dùng `thu-vien/chuyen-dong.js`, `thu-vien/chu-hien.jsx`, `thu-vien/cho.js` (tránh người).
- **Một hình diễn tả 1–2 ý, hoặc cả video:** không phải mỗi câu một hình. Trước khi viết cảnh, đọc cả lời và vẽ **mạch hình** — hình
  chính của câu chuyện lớn dần theo video.
- **Ý quay lại thì vẽ tiếp:** người nói nhắc lại hay đi tiếp ý trước thì cảnh sau **vẽ tiếp lên hình đã có** (thêm nét, đổi trạng thái,
  đi tiếp con đường), không vẽ hình mới rời rạc. Dùng `thu-vien/mach.js`: cùng component, `buoc` tăng dần, `tu_buoc` = bước đã vẽ ở cảnh trước.
- **Vẫn giữ:** chữ trên màn hình nguyên văn lời người nói (được rút gọn, đặt ở khoá `text`/`label`/`lines`/`quote`/`title` để máy
  soát); không che mặt khi vẽ cạnh người; câu cảm xúc, chuyện riêng thì để thấy mặt; luật chuyển động (mục 8). Đoạn chạm lằn ranh
  không làm đồ hoạ.
- **Mặt người / hình chiếm bao nhiêu:** AI tự cân theo câu chuyện, không con số cố định.
- Ghi trong `ke-hoach-canh.md`: mạch hình của video (một đoạn), mỗi cảnh vẽ bước nào của mạch, vì sao.

## 2. Đường cảm xúc + một đỉnh (luật ở `quy-tac-chung.md` mục 2)
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
- **Một đỉnh**, thường là câu then chốt của David. Đỉnh nhận cảnh lớn nhất (thường là bước lớn nhất của mạch hình); không có ba đỉnh tranh nhau.
- Mỗi cảnh trong bảng cảnh ghi thêm cột "cảm xúc", lấy từ đường này.

## 3. Bố cục tự cân
**Trước hết tự chọn theo `../../thiet-ke-bo-cuc/huong-dan-lua-chon.md`** (chẩn đoán → bố cục nền, lớp thông tin như bảng ghi chú chạy `GHI_CHU`,
kiểu cảnh theo dạng câu nói — đi hết kho, không dừng ở vài kiểu quen). Không con số bắt buộc. Mỗi đoạn chọn bố cục từ **`../../thiet-ke-bo-cuc/bo-cuc.md`** theo 4 câu hỏi ở `../../thiet-ke-bo-cuc/README.md` mục 2
(cần thấy người hay thấy ý · ý dài hay ngắn · khung còn chỗ không · trước / sau là gì). Ngang tự do; dọc mỗi lúc ít thứ. Ghi lý do
một dòng mỗi cảnh vào `ke-hoach-canh.md`. Bố cục mới học được thì thêm vào `thiet-ke-bo-cuc/` + `bo-cuc.jsx`, giữ chữ ký nhận diện.
Bố cục đã có code: người + phụ đề · `nhan` (mục 4) · **`bocuc`** (`the-canh` thẻ cạnh mặt · `o-nguoi` người vào ô bo góc + `illus` /
`diagram` / thẻ chữ · `chuong` màn chương · `muc-luc` mục lục tích luỹ · `tien-trinh` thanh tiến trình ý · `canh-nguoi` mạch hình vẽ
cạnh người, không thẻ — `thanh-phan/bo-cuc.jsx`) · `illus` / `diagram` toàn màn hình. Chữ trong thẻ: nguyên văn.
Cách viết + khi nào dùng từng kiểu: `bo-cuc.md`.
- **`phong: 'nguoi-mo' | 'hat'`** ở cảnh toàn màn hình — chỉ khi đoạn đó không có người nói trên hình (`quy-tac-chung.md` mục 4): nền là
  hình làm mờ / nền hạt, ngoài nền tối mặc định. Người còn trên hình thì vẽ vào chỗ trống thật (`ve`, mẫu `rieng/duong-may.jsx`).
- **`*từ*`** trong mọi chữ: một từ nhấn font phụ nghiêng màu cam; tối đa một chỗ mỗi cụm.
- Mỗi khung **một tiêu điểm**; cam chỉ là màu nhấn (khoảng 10 % khung) — soát ở khối 17.
- **Không hai cảnh cùng kiểu liền nhau** (`type` + `mode` / `kieu`, ví dụ hai `bocuc` `the-canh`): xen kiểu khác. Việc đổi kiểu là để
  đỡ nhàm, không phải để thêm kiểu mới; cả video vẫn chỉ xoay quanh vài kiểu hợp nội dung. Hai ý cùng loại liền nhau mà giữ cùng kiểu
  giúp người xem dễ theo hơn thì giữ, ghi lý do một dòng ở `ke-hoach-canh.md`. Cảnh "vẽ tiếp" cùng mạch hình (`tu_buoc`) được nối
  nhau. `soat-canh.mjs` (khối 17) tự nhắc P2.

## 4. Điểm nhấn trên người — `nhan`
Điểm nhấn kéo mắt vào người đang nói, đè lên người nhưng không che mặt.
| Kiểu | props | Khi |
|---|---|---|
| Làm tối viền | `toi: true` | câu tâm tình / câu muốn người xem lặng lại nghe |
| Chữ nhấn cạnh mặt | `text: 'DÒNG 1\nDÒNG 2'` tối đa 4 chữ, trích lời, dòng cuối màu nhấn; `at` = giây bật | cụm đắt người nói vừa thốt ra |
| Biểu tượng nhỏ cạnh mặt | `icon: '<tên>'`, `at` | vật / việc cụ thể, không cần cả màn minh hoạ |
Ví dụ: `{id: 'n1', type: 'nhan', start: 37.4, end: 42.1, props: {text: 'NHẤC CHÂN LÊN', at: 39.9}}` — 2–5 s, không chồng cảnh khác.
Không che ai: `vi-tri-nhan.py` (vi-tri-khuon-mat.sh) ghi mọi người + người đang nói vào `mat.js`; nhan.jsx đặt chữ / biểu tượng vào khoảng
trống sát người đang nói (`bam` để bám người khác, vd thẻ tên khách), co cỡ theo chỗ, khung dọc hẹp thì dưới cằm.
**Không zoom vào / zoom ra trên hình quay** (`quy-tac-chung.md` mục 2; `zoom` trong scenes cũ bị bỏ qua). Đoạn chạm lằn ranh: không dùng.

## 5. Cảnh minh hoạ `illus` (`thu-vien-tai-nguyen/minh-hoa.jsx`, một bản cho mọi khung dựng)
Hình động minh hoạ ĐÚNG Ý đang nói + **nhãn ngắn** (tên riêng / con số / cụm đắt — trích lời), dài và dày theo nội dung. Phụ đề vẫn chạy.
| mode | Dùng khi người nói… | items |
|---|---|---|
| `single` | nêu một vật / việc / khái niệm | 1 biểu tượng |
| `flow` | nói nhân quả / các bước ("đi bộ → khoẻ → sống thọ") | 2–3, mũi tên nối, mỗi cái hiện đúng lúc nhắc |
| `vs` | so sánh nên / không nên, trước / sau | 2, `good: true/false` (tick xanh / dấu x đỏ) |
| `count` | nêu con số ("15 phút", "3 năm") | 1 biểu tượng + `num: {to, at, unit}` — ĐÚNG con số người nói |
| `list` | liệt kê 3–5 thứ | 3–5 biểu tượng hiện dần (+ nhãn từng cái); 4–5 hình ở khung dọc tự xếp lưới 2 cột |

Viết ở đâu:
- 1 video / podcast (canh.js): `{id: 'm1', type: 'illus', start: 33.1, end: 37.0, props: {mode: 'count', items: [{icon: 'clock', at: 33.4}], num: {to: 15, at: 33.6, unit: 'PHÚT'}, label: 'MỖI NGÀY'}}`
- Vlog (ke-hoach.json fx): `{"type": "illus", "c": "c3", "at": 82.0, "len": 4, "mode": "flow", "items": [["footsteps", 82.5, "ĐI BỘ"], ["heart", 84.0, "SỐNG THỌ"]]}`
- Highlight / danh-sach-cat.js (OVERLAYS, giây timeline): `{type: 'illus', start: TS(140.2), end: TS(144), mode: 'single', items: [{icon: 'brain', at: TS(140.5)}], label: 'BỘ NÃO'}`
Biểu tượng: `thu-vien-tai-nguyen/bieu-tuong.jsx` (thiếu thì vẽ thêm lưới 64×64 cùng kiểu nét — thêm ở thư viện là cả 4 loại có).

Tự động (lưới an toàn): lớp chữ cũ (kinetic, lower, listItem, pow, chips, location, nameCard…) nếu vẫn viết thì khung dựng tự vẽ toàn
màn hình khi che người (dài theo nội dung); thẻ `card` / `action` bỏ câu trích dài (chỉ hình + nhãn `label`); tít ghim tắt. Muốn giữ
lớp phủ một cảnh: đặt tay `place` (1 video) / `keep: true` (ghép). Ưu tiên viết `illus` / `nhan` / `bocuc` hơn lớp chữ cũ.

## 6. Sơ đồ nói thay lời + ảnh khung bo góc (`diagram`, `thu-vien-tai-nguyen/so-do.jsx`)
Khi câu nói có CẤU TRÚC, vẽ chính cấu trúc đó (mọi chữ trích lời):
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
| quy trình 3–6 bước kể liền một mạch ("đầu tiên… rồi… cuối cùng") | `chuoi` (items `{at, label 1–3 chữ, icon?}`; bước đang nói sáng, bước cũ mờ) | "câu lệnh … viết code … chụp khung … ghép video" |
| việc đi từ người này sang người kia | `chuyen-giao` (items[0] bên giao, giữa = các việc `{icon, label, at}`, cuối = bên nhận) | "báo cáo tuần … xếp lịch … giao lại cho đội" |
| người / nơi / tổ chức có thật | `anh` (ảnh giấy phép mở hoặc ảnh David gửi, khung bo góc + nhãn + nguồn) | "CCL", "Hưng Yên", "Bác Hồ" |
`tang`, `cot` thêm `mot_diem: true` khi các mục được nói lần lượt: chỉ mục đang nói sáng (nguyên lý Báo hiệu, `thiet-ke-bo-cuc/huong-dan-lua-chon.md` bước 4b).
Ảnh (chỉ ảnh Việt Nam, `quy-tac-chung.md` mục 4): `kho-anh-openverse.py search/fetch` (CC0 / PD / CC BY / CC BY-SA, dùng thương mại) thì chép vào `chuyen-dong/public/anh/`, ghi `credit` trên ảnh +
`nguon-anh.txt` cho mô tả. Không có ảnh đúng (logo thương hiệu, ảnh mơ hồ) thì dùng sơ đồ, không ép ảnh. Podcast dài: ưu tiên `diagram`
hơn `illus`. Vlog (`ke-hoach.json` fx): `{"type": "diagram", "c", "at", "len", "mode", "label", "items": [{"at": giây clip, …}]}`.

## 7. Lên kịch bản cảnh (canh.js)
1. Viết mạch hình + đường cảm xúc (mục 1–2), rồi `chuyen-dong/src/canh.js` từ transcript theo `../../dung-video-theo-phong-cach/references/thiet-ke-canh.md`
   (loại cảnh cho loại câu nói, props). `references/vi-du-canh.js` là một kịch bản thật đã duyệt — đọc để lấy cảm giác nhịp và
   cách gắn mốc. Ghi `$P/ke-hoach-canh.md`: bảng cảnh (thời gian, loại, nội dung, minh hoạ, cảm xúc, lý do bố cục).
2. Thẻ tít `hook` mở đầu: khối 06.
3. **Quét transcript tìm câu hành động** rồi đặt cảnh `action` `{icon, quote, quoteAt, doneAt}` ngay lúc nói (doneAt = lúc nói xong cụm
   việc). Câu hành động rơi vào 4 s cuối thì đặt màn hành động ngay trước màn chốt.
4. **Cảnh cuối luôn là màn chốt** (khối 08): `{id: 'chot', type: 'cta', start: <thời lượng − 4>, end: <thời lượng>, props: {text, kind}}`
   — `text` = nguyên văn câu David nói cuối video (thời lượng = `duration` trong du-an.js; cảnh trước đó phải kết thúc trước mốc này).
5. Sau khi viết (và mỗi lần sửa mốc) canh.js: `zsh $SKILL/scripts/vi-tri-khuon-mat.sh "$P"` (khối 05; lần đầu dò mặt khoảng 1 phút / 5 phút
   video). Đọc `kiem-tra/khuon-mat/placement.md`: cảnh không có chỗ tránh được **mặt + đầu + vai + ngực** thì script tự chuyển toàn màn hình.
   Muốn giữ lớp phủ: `place: {top: <px>, scale: 0.6}` hoặc `place: {full: false}` trong cảnh (thứ tự khoá: `id, type, start, end, place,
   props`). Cảnh toàn màn hình (`FULL`, gồm cả thẻ toàn cảnh) che hết hình nên không cần tránh. Ngang pillar: lớp phủ ở cột trái.
6. *Khung ngang từ gốc dọc* — viết thêm `SIDES` (mẫu trong canh.js): `title` = chủ đề video ngắn gọn, `speaker`, `keywords` = từ
   khoá ý đang nói (đổi theo từng đoạn khoảng 15–40 s, tối đa 3 từ, mốc = lúc bắt đầu ý), `points` = 5–9 ý chính theo thứ tự nói (tối đa 4 từ mỗi ý,
   mốc = lúc bắt đầu nói ý đó). Chữ lấy từ lời nói. Ô từ khoá tự ẩn khi thẻ/chữ to chiếm ô; không chồng hai lớp phủ.

**Minh hoạ: biểu tượng vẽ (mặc định) hoặc ảnh** (luật ở `../../quy-tac-chung.md` mục 4). Biểu tượng: `icon: '<tên>'` thay `photo` trong
`montage` và `card job`. Không dùng ảnh kho vì hay lệch ngữ cảnh, lạc tông nền, phải ghi nguồn, có thể lộ mặt người lạ. Không có ảnh
tốt thì dùng biểu tượng + tên gọi đúng, không ảnh tạm. David nói "không dùng ảnh" thì không ảnh nào; "thêm ảnh" thì tìm ảnh cho mọi thứ cụ thể.
Khi cần ảnh: viết `$P/hinh-anh/tu-khoa-tim.json` (từ khoá tiếng Anh) rồi:
```bash
python3 -I $SKILL/scripts/kho-anh-openverse.py search "$P" "$P/hinh-anh/tu-khoa-tim.json"     # chạy nền, ~20 s/từ khoá
```
Xem từng `hinh-anh/bang-anh/<key>.jpg` (8 ảnh, số 0–7 từ trái) và chọn. Loại bỏ: người nổi tiếng/người dễ nhận ra ở bối cảnh nhạy cảm,
logo thương hiệu nổi bật, hình vẽ clip-art lạc tông với ảnh chụp, ảnh mờ/chữ đè, ảnh không khớp nghĩa. Không có ảnh ổn thì thêm từ khoá
khác vào tu-khoa-tim.json và search lại (chỉ các key đó). Rồi:
```bash
python3 -I $SKILL/scripts/kho-anh-openverse.py fetch "$P" "$P/hinh-anh/anh-chon.json"
```
Ảnh vào `chuyen-dong/public/anh/<key>.jpg`; dùng trong canh.js qua `photo: '<key>.jpg'`.

**Giữ cảnh sau chữ cuối:** hình / chữ chạy theo lời không tắt ngay khi chữ cuối vừa hiện: hết cảnh ít nhất mốc phần tử cuối + 0,5 s hiện
vào + `giu_sau_s` (hồ sơ chung) + 0,3 s mờ ra (+`giu_moi_chu_s` mỗi chữ nhãn vượt 3), tối đa 6 s từ đầu cảnh, không lấn lớp kế tiếp /
màn chốt. Khung dựng TỰ kéo dài khi render (`thu-vien-tai-nguyen/giu.js`, dùng ở montage `chuong-trinh.jsx` + remotion `goc.jsx`) — viết `len`
như thường, không tính tay. `keepEnd: true` = tắt luật cho lớp đó. Áp cho: illus · action (tính từ `doneAt`) · chips · pow · listItem ·
kinetic · scene. Bị chặn bởi trần 6 s (phần tử cuối hiện sau giây thứ khoảng 4 của cảnh) thì dời `start`/`at` của cảnh muộn hơn cho phần tử
đầu sát lúc nói.

## 8. Luật chuyển động (code: `thu-vien-tai-nguyen/chuyen-dong.js` + `chu-hien.jsx`)
Chuyển động phải dẫn mắt tới ý đang nói, không để trang trí. Thành phần mới dùng hàm ở `chuyen-dong.js`, không tự đặt easing riêng.
- **Đã vào là đứng yên:** không lơ lửng, không vòng xoay, không quầng nhấp nháy lặp lại — đó là dấu hiệu "máy làm". Chuyển động liên
  tục chỉ giữ khi có nghĩa: sóng âm theo giọng, thanh thời gian, nút mời bấm ở màn kết. Tiêu đề hiện xong thì đứng yên tới lúc rời đi.
- **Easing theo vai:** vào = đuôi dài (`EASE.vao` exp-out) · zoom/đẩy khung, đổi nền = `EASE.camera` (inOut) · ra = `EASE.ra` (tăng
  tốc). Ra ngắn hơn vào 40–50 % (vào 8 khung, ra 5 khung). Một kiểu cho mọi thứ là dấu hiệu "máy làm".
- **Kiểu vào theo ý của câu**, không để mọi cảnh cùng trồi lên: 1 hình = phóng tại chỗ · nhân quả = đi theo hướng đọc · so sánh = hai
  phía tiến vào · danh sách = trồi lên lần lượt.
- **Nối gối, so le:** phần sau bắt đầu khi phần trước xong 30–50 %; từ cách nhau 60–120 ms, mục danh sách 40–80 ms.
- **Chữ hiện từng từ, không dịch chỗ** (`ChuHien`): `mo` (mờ 6 px sang nét, 0,13 s, cách khoảng 0,067 s) · `muc` (xám nhạt sang màu chữ) · `dong`
  (cả dòng mờ thì nét). Kiểu đổi theo cảnh (`kieuChu(id)`), không để mọi cảnh mờ + trượt lên.
- **Chỉ vị trí và cỡ được nảy nhẹ** — lò xo theo ζ (`loXo(zeta)`): 0,7–0,85 sang, 0,4–0,6 vui. Độ mờ và màu không nảy. Phản hồi một
  lần thì được (bên nhận đón việc), lặp lại thì không.
- **Thoát:** mờ nhoè + tan 0,13–0,25 s, ngắn hơn lúc vào; khung toàn màn hình vào bằng mờ nhoè sang nét (`vaoRa`).
- **Giữ đủ đọc:** 0,5 s + 0,3 s mỗi từ (`docDu`); câu cuối video ít nhất 2 s.
- **Vào cảnh qua một vật trên màn hình khi được** (việc bay sang bên nhận, màu tràn từ vật ra), không mờ chồng cả khung.
- **Chuyển cảnh có nguyên do, 3–5 kiểu một video:** tối nhẹ khoảng 40 % trong 3 khung trước cắt cứng · đổi trên cùng nền (mờ ra 8 px thì mờ
  vào) · màu tràn nền · vật trên màn hình lớn dần thành cảnh sau. Tối đa một phần ba số điểm nối là cắt cứng.
- Không cắt theo nhịp nhạc (video của David đi theo lời).
- **Soát kiểu "máy làm" khi xem chụp thử:** che chữ đi, hình còn kể được ý không; mọi cảnh có vào giống nhau không; có gì còn
  trôi/phóng sau khi đã vào không.
