// BỐ CỤC (type 'bocuc' — lớp trình bày, David chốt 2026-11-07; xem ../../../../thiet-ke-bo-cuc/README.md)
// Chỉ lo SẮP XẾP: người ở đâu, nội dung ở đâu, hiện theo thứ tự nào. Màu, chữ, nét, chuyển động lấy từ thư viện hình (lib/tokens,
// Illus, Diagram, Icons) — học bố cục mới thì thêm `kieu` ở đây, giữ chữ ký nhận diện (lib/nhan-dien-chung.md mục 0); ngoài đó tự do.
// Không có con số bắt buộc: vị trí, cỡ ô, độ dài cảnh do Claude tự cân theo nội dung (props ghi đè mặc định).
//
// kieu:
//  'o-nguoi'  người thu vào một ô bo góc, phần còn lại của khung là nội dung. Ô co từ toàn khung vào chỗ, hết cảnh nở lại.
//             Tỉ lệ ô TỰ DO = tỉ lệ khung cắt quanh người đang nói (không cố định 16:9 hay dọc); không bao giờ cắt ngang
//             một gương mặt — người bên cạnh hoặc vào trọn, hoặc ra hẳn; ô nằm đúng phía người đó ngồi, nội dung phía còn lại.
//             props: noi_dung: {type: 'illus'|'diagram'|'the', props} · khung? 'ca-hai' (ô chứa mọi người) · bam? 'trai'|'phai'
//             · o? {x, y, w, h} (0–1, chỉ khi thật cần ép tay)
//             · nguoi_duoi? true (chỉ khung dọc; học Cường Mê AI 20/11/2026): người xuống nửa dưới sát dải phụ đề, hình/thẻ ở nửa trên —
//               giải thích dài vẫn thấy người, mắt đọc hình trước rồi xuống người. Mặc định tắt (ô trên, nội dung dưới như cũ).
//  'the-canh' người giữ nguyên khung, thẻ vào khoảng trống sát người đang nói (lib/cho.js), co theo khoảng trống, không đè ai;
//             không khoảng nào đủ rộng → tự chuyển sang 'o-nguoi'. props: bam? · tieu_de? · dong: [{text, at, to?: true, gach?: <giây>}]
//  'chuong'   màn chương toàn khung: số mờ to + nhãn nhỏ + tên phần (dòng cuối màu nhấn). props: so?, nhan?, ten
//  — thêm 10/11/2026 (học Ali Abdaal, Joseph Video Editing) —
//  'muc-luc'  MỤC LỤC TÍCH LUỸ: người vào ô, danh sách đánh số hiện dần theo lời; mục đang nói sáng, mục cũ mờ lại.
//             props: tieu_de? · muc: [{text, at}] · (mọi props của 'o-nguoi': bam, khung…) · nen? (xem FullShell)
//             Dùng cho "trong video này có 3 điều", nhắc lại các ý đã qua. Cũng đặt được làm noi_dung {type: 'muc-luc'} của 'o-nguoi'.
//  'tien-trinh' THANH TIẾN TRÌNH Ý: một đường nối các nút 1…n, nút đang tới sáng lên, thẻ tên ý hiện dưới nút.
//             props: so (ý thứ mấy) · tong · nhan? ('Ý' / 'Bước'…, nguyên văn) · ten (tên ý, nguyên văn). Thay màn chương khi
//             video đi theo danh sách (mẹo 1, 2, 3); người xem thấy mình đang ở đâu.
//  'canh-nguoi' MẠCH HÌNH CẠNH NGƯỜI (kiểu bảng phấn của Ali): người giữ nguyên khung, hình (illus / diagram / cảnh tự vẽ 've')
//             vẽ thẳng vào khoảng trống sát người, KHÔNG thẻ nền — như vẽ lên tường phía sau. Hợp khung ngang, đoạn giải thích dài
//             mà vẫn muốn thấy người; nhiều cảnh nối nhau vẽ tiếp một mạch (`buoc`, `tu_buoc` của lib/mach.js).
//             props: noi_dung: {type: 'illus'|'diagram'|'ve', props} · bam? · toi? (false = không làm tối khoảng trống)
//             Không khoảng nào đủ rộng → tự chuyển 'o-nguoi'.
//  — thêm 20/11/2026 (học kênh MagentX; chỉ chọn khi có dấu hiệu ở thiet-ke-bo-cuc/huong-dan-lua-chon.md) —
//  'dung-hay' CẶP ĐỪNG / HÃY LẶP KHUÔN: nhãn mục + hai ô ✗ (sai) / ✓ (đúng), cùng một chỗ cho mọi cặp — người xem học khuôn một
//             lần, sau chỉ nhìn chỗ đổi. Dọc: ô trên đầu người nếu mặt đủ thấp, không thì người xuống nửa dưới (o-nguoi nguoi_duoi).
//             Ngang: vào khoảng trống cạnh người, chật thì o-nguoi. props: cap: [{nhan?, at, dung: NGUON, hay: NGUON, at_hay?}]
//             · chu_dung? ('ĐỪNG') · chu_hay? ('HÃY') — chữ nguyên văn lời người nói ("SAI"/"ĐÚNG", "THAY VÌ"/"HÃY"…)
//  'tren-duoi' ĐỐI CHIẾU SONG SONG: hai hình cùng chạy — dọc xếp trên/dưới, ngang trái/phải; nhãn nhỏ ở góc mỗi hình.
//             props: tren: NGUON & {nhan?} · duoi: NGUON & {nhan?}. Không có chữ lớn → nên để giuPhuDe: true.
//  'o-tron'   HÌNH TOÀN KHUNG + NGƯỜI NÓI Ô TRÒN: lời đang tả chi tiết một thứ cần nhìn kỹ; người thu vào ô tròn (dọc: giữa, trên
//             dải phụ đề; ngang: góc dưới phải) để mạch lời không đứt. props: hinh: NGUON  hoặc  noi_dung: {type: 'illus'|'diagram', props}
//  'cau-hoi'  THẺ CÂU HỎI (phỏng vấn, lời chứng): câu người hỏi hiện thành thẻ có vạch màu nhấn dưới mặt người; câu trả lời sau
//             đó người xem biết trả lời cho câu gì. Tên + vai trò người trả lời: dùng cảnh 'lower' có sẵn. props: cau, at?, nhan?
//  'the-canh' thêm props so? — số thứ tự to làm mốc cạnh thẻ ("1 khuôn mặt", "4 đôi mắt"), khi lời đếm ≥ 3 mục.
//  NGUON = {photo: 'ten.jpg'} (public/anh) · {video: 'goc', tu?: giây} (video gốc) · {video: 'ten.mp4', tu?} (public) · {text: '…'}
// Chữ trong thẻ / chương là NGUYÊN VĂN lời người nói (luật chữ trên màn hình).
import React from 'react';
import {AbsoluteFill, Easing, Img, OffthreadVideo, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {BODY, C, HEAD, SAFE, BRAND_BOT, ease, pop, rel} from '../chu-de';
import {FullShell} from './toan-man-hinh';
import {Illus} from '../thu-vien/minh-hoa';
import {Diagram} from '../thu-vien/so-do';
import project from '../du-an.js';
import {fr} from '../canh';
import MAT from '../mat.js';
import {nguoi, chonCho, nguoiBam} from '../thu-vien/cho';
import {ChuHien} from '../thu-vien/chu-hien';
import {kieuChu} from '../thu-vien/chuyen-dong';
import {VE} from '../rieng/diem-vao';

const W = project.width, H = project.height, LAND = W > H;
const NOI = {illus: Illus, diagram: Diagram, ve: ({ve, ...p}) => { const V = VE[ve]; if (!V) throw new Error(`cảnh tự vẽ '${ve}' chưa đăng ký`); return <V {...p} />; }};

// Vùng vẽ thật của nội dung lồng (tỉ lệ khung). Sơ đồ và minh hoạ khung ngang trải 86–88% bề ngang (so-do.jsx, minh-hoa.jsx):
// co và canh giữa theo đúng vùng đó, không thì tràn mép phải khi đặt cạnh người. Cảnh tự vẽ và khung dọc giữ vùng giữa 60%.
const VUNG_NOI = LAND ? {diagram: {x: 0.07, w: 0.86, y: 0.12, h: 0.68}, illus: {x: 0.06, w: 0.88, y: 0.12, h: 0.68}} : {};
const vungNoi = (noi_dung) => (noi_dung && VUNG_NOI[noi_dung.type]) || (LAND ? {x: 0.2, w: 0.6, y: 0.07, h: 0.64} : {x: 0.2, w: 0.6, y: 0.1, h: 0.46});

// Thẻ chữ hiện dần (dùng cho 'the-canh' và nội dung 'the' trong 'o-nguoi')
// Xuống dòng cân (textWrap balance): dòng đều nhau, không để một chữ đứng lẻ ("LUYỆN TẬP LẠI THÓI / QUEN" — lỗi 09/11/2026);
// '\n' trong chữ = chỗ xuống dòng theo cụm nghĩa do kịch bản đặt.
// so (20/11/2026): số thứ tự to đứng trước thẻ làm mốc danh sách; không có so → thẻ y như cũ
const The = ({so, ...p}) => so == null ? <TheGoc {...p} /> : (
  <div style={{display: 'flex', alignItems: 'center', gap: p.fs * 0.4, width: p.w}}>
    <div style={{flex: 'none', fontFamily: HEAD, fontWeight: 800, fontSize: p.fs * 2.6, lineHeight: 0.9, color: C.accent,
      opacity: Math.min(1, pop(p.f, 0) * 1.3), transform: `translateY(${(1 - pop(p.f, 0)) * 30}px)`, textShadow: `0 8px 30px rgba(${C.bongRgb},0.6)`}}>{so}</div>
    <TheGoc {...p} w={p.w - p.fs * 2.2} />
  </div>
);
const TheGoc = ({start, tieu_de, dong = [], w, f, fs, kc = 'mo'}) => (
  <div style={{width: w, padding: fs * 0.9, borderRadius: fs * 0.7, background: C.card, border: `2px solid ${C.line}`,
    boxShadow: `0 30px 90px rgba(${C.bongRgb},0.5)`, display: 'flex', flexDirection: 'column', gap: fs * 0.6}}>
    {tieu_de && <div style={{fontFamily: BODY, fontWeight: 700, fontSize: fs * 0.42, letterSpacing: 3, color: C.accent, textTransform: 'uppercase',
      opacity: ease(f, 2, 10), textWrap: 'balance'}}>{tieu_de}</div>}
    {dong.map((d, i) => {
      const a = rel(d.at ?? start, start), p = pop(f, a);
      const g = d.gach != null ? ease(f, rel(d.gach, start), rel(d.gach, start) + 8) : 0;
      // trình bày ý (David góp ý 26/11/2026): gạch đầu dòng, viết hoa chữ đầu, các ý cách nhau rõ
      const co = d.to ? Math.max(fs * 0.8, Math.min(fs * 1.35, (w - fs * 2.6) / (0.46 * Math.max(4, d.text.length)))) : fs * 0.62;   // chữ to: co cho vừa một dòng, không nhỏ hơn 0,8 — dài quá thì xuống dòng
      const lh = 1.18, day = Math.max(4, fs * 0.08);
      return (
        <div key={i} style={{alignSelf: 'flex-start', display: 'flex', alignItems: 'flex-start', gap: fs * 0.28,
          opacity: (1 - 0.45 * g) * (f < a ? 0 : 1)}}>
          {dong.length > 1 && <div style={{flex: 'none', width: fs * 0.3, height: day, borderRadius: 4, background: C.accent, marginTop: co * lh / 2 - day / 2,
            opacity: Math.min(1, p * 1.4)}} />}
          <div style={{position: 'relative', minWidth: 0}}>
            <div style={{fontFamily: d.to ? HEAD : BODY, fontWeight: d.to ? 800 : 500, lineHeight: lh, fontSize: co,
              color: d.to && i === dong.length - 1 ? C.accent : C.text, textTransform: d.to ? 'uppercase' : 'none',
              textWrap: 'pretty', whiteSpace: 'pre-line', hyphens: 'none'}}>
              <ChuHien text={d.text.replace(/^([^\p{L}\p{N}]*)(\p{L})/u, (_, a, b) => a + b.toLocaleUpperCase('vi'))} a={a} kieu={kc} /></div>
            {g > 0 && <div style={{position: 'absolute', left: 0, top: '52%', height: Math.max(3, fs * 0.08), width: `${g * 100}%`, background: C.accent}} />}
          </div>
        </div>
      );
    })}
  </div>
);

// Mục lục tích luỹ: hàng số + chữ, mục mới nhất sáng, mục cũ mờ 45 %
const MucLuc = ({start, f, w, fs, tieu_de, muc = []}) => {
  const hien = muc.filter((m) => rel(m.at ?? start, start) <= f);
  return (
    <div style={{width: w, display: 'flex', flexDirection: 'column', gap: fs * 0.45}}>
      {tieu_de && <div style={{fontFamily: BODY, fontWeight: 700, fontSize: fs * 0.55, letterSpacing: 3, color: C.muted, textTransform: 'uppercase',
        opacity: ease(f, 2, 10)}}><ChuHien text={tieu_de} a={2} /></div>}
      {muc.map((m, i) => {
        const a = rel(m.at ?? start, start), p = pop(f, a);
        const cu = hien.length && hien[hien.length - 1] !== m && f >= a ? 1 : 0;
        return (
          <div key={i} style={{display: 'flex', alignItems: 'center', gap: fs * 0.55, padding: `${fs * 0.42}px ${fs * 0.6}px`, borderRadius: fs * 0.5,
            background: C.card, border: `2px solid ${cu ? C.line : `rgba(${C.accentRgb},0.45)`}`, boxShadow: `0 20px 60px rgba(${C.bongRgb},0.45)`,
            opacity: Math.min(1, p * 1.4) * (1 - 0.55 * cu), transform: `translateY(${(1 - p) * 24}px) scale(${0.95 + 0.05 * p})`}}>
            <div style={{flex: 'none', width: fs * 1.25, height: fs * 1.25, borderRadius: '50%', background: cu ? C.dim : C.accent, color: C.trenNhan,
              display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: HEAD, fontWeight: 800, fontSize: fs * 0.8}}>{i + 1}</div>
            <div style={{fontFamily: BODY, fontWeight: 600, fontSize: fs * 0.82, lineHeight: 1.25, color: C.text, textWrap: 'balance'}}>
              <ChuHien text={m.text} a={a + 3} kieu="muc" /></div>
          </div>
        );
      })}
    </div>
  );
};

// Ô NGƯỜI tỉ lệ tự do (David chốt 08/11): khung cắt bám NGƯỜI ĐANG NÓI (hoặc props.khung = 'ca-hai' / props.bam), không bao giờ cắt
// ngang một gương mặt — người bên cạnh hoặc vào trọn, hoặc ra hẳn. Tỉ lệ ô = tỉ lệ khung cắt. Ô nằm đúng phía người đó đang ngồi,
// nội dung ở phía còn lại.
const khungCat = (m, khung, bam) => {
  const ps = (m.nguoi && m.nguoi.length ? m.nguoi : [{...m, t: m.cy - m.h / 2, b: m.cy + m.h / 2, l: m.l ?? m.cx - m.w / 2, r: m.r ?? m.cx + m.w / 2, noi: true}])
    .slice().sort((a, b) => a.cx - b.cx);
  const t = bam === 'trai' ? ps[0] : bam === 'phai' ? ps[ps.length - 1] : (ps.find((p) => p.noi) || ps[0]);
  let chon = khung === 'ca-hai' ? ps : [t];
  for (let lap = 0; lap < 3; lap++) {
    const fw = Math.max(...chon.map((p) => p.w));
    const l = Math.min(...chon.map((p) => p.l)) - fw * 1.1, r = Math.max(...chon.map((p) => p.r)) + fw * 1.1;
    // người khác mà mặt (kèm đệm tai tóc) bị khung cắt ngang → cho vào trọn
    const cat = ps.filter((p) => !chon.includes(p) && p.r + p.w * 0.3 > l && p.l - p.w * 0.3 < r);
    if (!cat.length) break;
    chon = [...chon, ...cat];
  }
  const fw = Math.max(...chon.map((p) => p.w)), fh = Math.max(...chon.map((p) => p.h));
  let l = Math.min(...chon.map((p) => p.l)) - fw * 1.1, r = Math.max(...chon.map((p) => p.r)) + fw * 1.1;
  // người ngoài khung: kéo mép khung lùi lại cho khỏi chạm mặt họ
  for (const p of ps) if (!chon.includes(p)) { if (p.cx < t.cx) l = Math.max(l, p.r + p.w * 0.4); else r = Math.min(r, p.l - p.w * 0.4); }
  const top = Math.min(...chon.map((p) => p.t)) - fh * 0.9, bot = Math.max(...chon.map((p) => p.b)) + fh * 2.2;   // đầu + vai + tay
  const c = {l: Math.max(0, l), r: Math.min(1, r), t: Math.max(0, top), b: Math.min(1, bot)};
  return {...c, phia: t.cx < 0.5 ? 'trai' : 'phai'};
};

const ONguoi = ({sceneId, start, o, noi_dung, khung, bam, nguoi_duoi = false}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d} = useVideoConfig();
  const m = MAT[sceneId] || {cx: 0.5, cy: 0.42, w: 0.18, h: 0.3};
  const kc = khung === 'toan-canh'
    ? {l: 0, r: 1, t: 0, b: 1, phia: bam === 'phai' ? 'phai' : 'trai'}
    : khungCat(m, khung, bam);
  const cw = (kc.r - kc.l) * W, ch = (kc.b - kc.t) * H, ar = cw / ch;
  // cỡ ô: theo tỉ lệ khung cắt, vừa trong tối đa 46% bề ngang × 72% bề cao (ngang) — dọc: rộng hết, cao tối đa 40%
  const duoi = !LAND && nguoi_duoi && !o;
  const maxW = LAND ? W * 0.46 : W * 0.88, maxH = LAND ? H * 0.72 : duoi ? H * 0.3 : H * 0.4;
  const bw = Math.min(maxW, maxH * ar), bh = bw / ar;
  const aTop = Math.max(SAFE.top, BRAND_BOT + 40);   // dưới dấu góc kênh (chu-de.js)
  const b = o ? {x: o.x * W, y: o.y * H, w: o.w * W, h: o.h * H}
    : LAND ? {x: kc.phia === 'trai' ? SAFE.left : W - SAFE.right - bw, y: aTop + (SAFE.bottom - aTop - bh) / 2, w: bw, h: bh}
      : {x: (W - bw) / 2, y: duoi ? SAFE.bottom - bh : H * 0.07, w: bw, h: bh};
  // co vào (14 khung) · nở lại toàn khung ở cuối (10 khung)
  const k = Math.min(ease(f, 0, 14), ease(f, d - 10, d, 1, 0, Easing.inOut(Easing.cubic)));
  const x = b.x * k, y = b.y * k, w = W + (b.w - W) * k, h = H + (b.h - H) * k;
  const cl = kc.l * k, ct = kc.t * k, cr = 1 + (kc.r - 1) * k, cb = 1 + (kc.b - 1) * k;   // khung cắt từ toàn khung → khung người
  const sc = Math.max(w / ((cr - cl) * W), h / ((cb - ct) * H));
  // vùng nội dung = phía còn lại, chừa dải phụ đề
  const area = LAND
    ? (kc.phia === 'trai' && !o ? {x: b.x + b.w + SAFE.left * 0.8, y: aTop, w: W - SAFE.right - (b.x + b.w + SAFE.left * 0.8), h: SAFE.bottom - aTop}
      : {x: SAFE.left, y: aTop, w: b.x - SAFE.left * 1.8, h: SAFE.bottom - aTop})
    : duoi ? {x: SAFE.left, y: aTop, w: W - SAFE.left - SAFE.right * 0.4, h: b.y - aTop - 40}
      : {x: SAFE.left, y: b.y + b.h + 30, w: W - SAFE.left - SAFE.right * 0.4, h: SAFE.bottom - (b.y + b.h) - 60};
  const show = ease(f, 8, 18) * ease(f, d - 12, d - 4, 1, 0);
  const Comp = noi_dung && NOI[noi_dung.type];
  const v = vungNoi(noi_dung);
  const s = Math.min(1, area.w / (W * v.w), area.h / (H * v.h));
  const cx = area.x + area.w / 2, cy = area.y + area.h / 2;
  return (
    <FullShell hold>
      <div style={{position: 'absolute', left: x, top: y, width: w, height: h, borderRadius: 36 * k, overflow: 'hidden',
        border: k > 0.5 ? `3px solid ${C.accent}` : 'none', boxShadow: `0 30px 90px rgba(${C.bongRgb},0.6)`}}>
        <OffthreadVideo src={staticFile('goc.mp4')} trimBefore={fr(start)} muted
          style={{position: 'absolute', left: -cl * W * sc + (w - (cr - cl) * W * sc) / 2, top: -ct * H * sc + (h - (cb - ct) * H * sc) / 2,
            width: W * sc, height: H * sc, maxWidth: 'none'}} />
      </div>
      {noi_dung && (
        Comp ? <div style={{position: 'absolute', left: cx - W * (v.x + v.w / 2) * s, top: cy - H * (v.y + v.h / 2) * s, width: W, height: H, opacity: show,
            transform: `scale(${s})`, transformOrigin: '0 0'}}><Comp start={start} sceneId={sceneId} nen={false} {...noi_dung.props} /></div>
          : <div style={{position: 'absolute', left: area.x, top: area.y, width: area.w, height: area.h, opacity: show,
            display: 'flex', alignItems: LAND ? 'center' : 'flex-start', justifyContent: 'center'}}>
            {noi_dung.type === 'dung-hay'
              ? <DungHayKhung start={start} f={f} w={area.w * 0.96} h={area.h} {...noi_dung.props} />
              : noi_dung.type === 'muc-luc'
              ? <MucLuc start={start} f={f} w={area.w * 0.94} fs={Math.min(LAND ? H * 0.05 : W * 0.062,   // co cho đủ mọi mục trong vùng nội dung
                  area.h / ((noi_dung.props.muc || []).length * 2.15 + (noi_dung.props.tieu_de ? 1.4 : 0) + 0.6))} {...noi_dung.props} />
              : <The start={start} f={f} w={area.w * 0.92} fs={LAND ? H * 0.06 : W * 0.075} {...noi_dung.props} />}</div>
      )}
    </FullShell>
  );
};

// THẺ CẠNH NGƯỜI (David chốt 08/11): thẻ vào khoảng trống sát người đang nói (hoặc props.bam), co theo khoảng trống, không đè ai.
// Không khoảng nào đủ rộng → chuyển sang ô người (người thu vào ô, thẻ ở phía còn lại).
const TheCanh = ({sceneId, start, ben, bam, tieu_de, dong, so}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d} = useVideoConfig();
  const m = MAT[sceneId] || {cx: 0.5, cy: 0.42, w: 0.18};
  const o = Math.min(ease(f, 0, 10), ease(f, d - 6, d, 1, 0, Easing.in(Easing.cubic)));
  const mo = o < 1 && f > d / 2 ? `blur(${(8 * (1 - o)).toFixed(2)}px)` : undefined;   // ra: mờ nhoè + tan (chuyen-dong.js luật 5)
  if (!LAND) {   // dọc: một thẻ hẹp phía dưới mặt, trên dải phụ đề — ít chữ cùng lúc
    const slide = (1 - ease(f, 0, 14)) * 60;
    return (
      <AbsoluteFill style={{opacity: o, filter: mo}}>
        <div style={{position: 'absolute', left: SAFE.left, top: SAFE.overlayTop, transform: `translateY(${-slide}px)`}}>
          <The start={start} f={f} w={W - SAFE.left - SAFE.right} fs={W * 0.07} tieu_de={tieu_de} dong={dong} so={so} kc={kieuChu(sceneId)} />
        </div>
      </AbsoluteFill>
    );
  }
  const ps = nguoi(m);
  const t = nguoiBam(ps, bam || ben);
  const MIN = W * 0.2;
  const k = chonCho(ps, MIN, t);
  if (k.w < MIN) return <ONguoi sceneId={sceneId} start={start} bam={bam || ben} noi_dung={{type: 'the', props: {tieu_de, dong, so}}} />;
  const w = Math.min(W * 0.34, k.w);
  const left = k.ke === 'trai' ? k.x1 - w : k.x0;     // sát người được bám
  const slide = (1 - ease(f, 0, 14)) * 60 * (k.ke === 'phai' ? 1 : -1);
  const fs = Math.min(H * 0.055, w / 9);
  return (
    <AbsoluteFill style={{opacity: o, filter: mo}}>
      <div style={{position: 'absolute', left, top: Math.max(H * 0.17, BRAND_BOT + 40), transform: `translateX(${slide}px)`}}>
        <The start={start} f={f} w={w} fs={fs} tieu_de={tieu_de} dong={dong} so={so} kc={kieuChu(sceneId)} />
      </div>
    </AbsoluteFill>
  );
};

// Thanh tiến trình ý: nút 1…tong trên một đường, đường chạy tới nút `so`, thẻ tên ý dưới nút đó
const TienTrinh = ({sceneId, start, so = 1, tong = 3, nhan, ten = ''}) => {
  const f = useCurrentFrame();
  const L = SAFE.left * (LAND ? 2.2 : 1.3), R = W - L, y = LAND ? H * 0.4 : H * 0.36;
  const xs = Array.from({length: tong}, (_, i) => L + (R - L) * (tong === 1 ? 0.5 : i / (tong - 1)));
  const toi = ease(f, 4, 22, so - 1.6, so - 1, Easing.inOut(Easing.cubic));   // đường chạy từ ý trước tới ý này
  const xRun = L + (R - L) * Math.max(0, toi) / Math.max(1, tong - 1);
  const r = LAND ? H * 0.034 : W * 0.04, fs = LAND ? H * 0.075 : W * 0.085;
  const x = xs[so - 1], p = pop(f, 18);
  return (
    <FullShell>
      <div style={{position: 'absolute', left: L, top: y - 3, width: R - L, height: 6, borderRadius: 3, background: C.line}} />
      <div style={{position: 'absolute', left: L, top: y - 3, width: xRun - L, height: 6, borderRadius: 3, background: C.accent}} />
      {xs.map((cx, i) => {
        const on = i < so - 1 || (i === so - 1 && f >= 18);
        return <div key={i} style={{position: 'absolute', left: cx - r, top: y - r, width: r * 2, height: r * 2, borderRadius: '50%',
          background: on ? C.accent : C.bg, border: `4px solid ${on ? C.accent : C.dim}`, display: 'flex', alignItems: 'center', justifyContent: 'center',
          fontFamily: HEAD, fontWeight: 800, fontSize: r * 1.05, color: on ? C.trenNhan : C.dim,
          transform: i === so - 1 ? `scale(${1 + 0.18 * p - 0.18 * ease(f, 26, 36)})` : undefined}}>{i + 1}</div>;
      })}
      <div style={{position: 'absolute', top: y + r * 2.1, left: Math.min(Math.max(SAFE.left, x - W * 0.3), W - SAFE.right - W * 0.6), width: W * 0.6,
        display: 'flex', flexDirection: 'column', alignItems: 'center', opacity: Math.min(1, p * 1.3), transform: `translateY(${(1 - p) * 30}px)`}}>
        {nhan && <div style={{fontFamily: BODY, fontWeight: 700, fontSize: fs * 0.32, letterSpacing: 4, color: C.accent, textTransform: 'uppercase',
          marginBottom: fs * 0.12}}>{nhan}</div>}
        <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: fs, lineHeight: 1.04, textTransform: 'uppercase', color: C.text,
          textAlign: 'center', textWrap: 'balance', whiteSpace: 'pre-line'}}><ChuHien text={ten} a={22} kieu={kieuChu(sceneId)} /></div>
      </div>
    </FullShell>
  );
};

// Mạch hình cạnh người: người giữ nguyên, hình vẽ thẳng vào khoảng trống sát người (không thẻ nền)
const CanhNguoi = ({sceneId, start, noi_dung, bam, toi = true}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d} = useVideoConfig();
  const m = MAT[sceneId] || {cx: 0.5, cy: 0.42, w: 0.18};
  const ps = nguoi(m);
  const t = nguoiBam(ps, bam);
  const MIN = W * (LAND ? 0.26 : 0.6);
  const k = chonCho(ps, MIN, t);
  if (k.w < MIN || !noi_dung) return <ONguoi sceneId={sceneId} start={start} bam={bam} noi_dung={noi_dung} />;
  const Comp = NOI[noi_dung.type];
  const o = Math.min(ease(f, 0, 10), ease(f, d - 6, d, 1, 0, Easing.in(Easing.cubic)));
  const top = Math.max(BRAND_BOT + 30, SAFE.top), bot = SAFE.bottom - 40;
  const v = vungNoi(noi_dung);
  const s = Math.min(1, k.w / (W * v.w), (bot - top) / (H * v.h));
  const cx = (k.x0 + k.x1) / 2, cy = (top + bot) / 2;
  return (
    <AbsoluteFill style={{opacity: o, filter: o < 1 && f > d / 2 ? `blur(${(8 * (1 - o)).toFixed(2)}px)` : undefined}}>
      {toi && <div style={{position: 'absolute', left: k.x0 - W * 0.04, top: 0, width: k.x1 - k.x0 + W * 0.08, height: H,
        background: `linear-gradient(${k.ke === 'phai' ? 90 : 270}deg, transparent, rgba(${C.theRgb},0.55) 25%, rgba(${C.theRgb},0.55) 75%, transparent)`}} />}
      <div style={{position: 'absolute', left: cx - W * (v.x + v.w / 2) * s, top: cy - H * (v.y + v.h / 2) * s, width: W, height: H,
        transform: `scale(${s})`, transformOrigin: '0 0'}}>
        {Comp && <Comp start={start} sceneId={sceneId} nen={false} {...noi_dung.props} />}
      </div>
    </AbsoluteFill>
  );
};

const Chuong = ({sceneId, start, so, nhan, ten = ''}) => {
  const f = useCurrentFrame();
  const lines = ten.split('\n');
  const fs = LAND ? H * 0.12 : W * 0.13;
  return (
    <FullShell>
      <div style={{position: 'absolute', left: SAFE.left * 1.4, top: Math.max(LAND ? H * 0.22 : H * 0.28, BRAND_BOT + 60)}}>
        {so != null && <div style={{position: 'absolute', left: -fs * 0.1, top: -fs * 1.1, fontFamily: HEAD, fontWeight: 800, fontSize: fs * 2.4,
          color: C.text, opacity: 0.06 * ease(f, 0, 12), lineHeight: 1}}>{String(so).padStart(2, '0')}</div>}
        {nhan && <div style={{fontFamily: BODY, fontWeight: 700, fontSize: fs * 0.22, letterSpacing: 4, color: C.accent, textTransform: 'uppercase',
          opacity: ease(f, 4, 12), marginBottom: fs * 0.15}}>{nhan}</div>}
        {lines.map((l, i) => {
          return <div key={i} style={{fontFamily: HEAD, fontWeight: 800, fontSize: fs, lineHeight: 1.02, textTransform: 'uppercase',
            color: i === lines.length - 1 && lines.length > 1 ? C.accent : C.text}}><ChuHien text={l} a={8 + i * 5} kieu={kieuChu(sceneId)} /></div>;
        })}
      </div>
    </FullShell>
  );
};

// ===== Thêm 20/11/2026 (học kênh MagentX) =====
// Một nguồn hình: ảnh (public/anh), video gốc từ giây `tu`, video khác trong public, hoặc ô chữ
const Hinh = ({nguon = {}, start, fit = 'cover', fs = 40}) => {
  if (nguon.photo) return <Img src={staticFile(`anh/${nguon.photo}`)} style={{width: '100%', height: '100%', objectFit: fit, objectPosition: nguon.pos || '50% 50%'}} />;
  if (nguon.video) return <OffthreadVideo src={staticFile(nguon.video === 'goc' ? 'goc.mp4' : nguon.video)} trimBefore={fr(nguon.tu ?? start)} muted
    style={{width: '100%', height: '100%', objectFit: fit, objectPosition: nguon.pos || '50% 50%'}} />;
  return <div style={{width: '100%', height: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center', padding: fs * 0.5, boxSizing: 'border-box',
    background: C.card, fontFamily: BODY, fontWeight: 700, fontSize: fs, lineHeight: 1.2, color: C.text, textAlign: 'center', textWrap: 'balance'}}>{nguon.text || ''}</div>;
};
const DO = '#FF4D4D', XANH = '#3DDC84';   // cùng màu nghĩa với phụ đề (+ nên / - tránh, kieu-phu-de.js)
const Dau = ({ok, r}) => (
  <div style={{position: 'absolute', left: -r * 0.35, bottom: -r * 0.35, width: r * 2, height: r * 2, borderRadius: '50%', background: ok ? XANH : DO,
    display: 'flex', alignItems: 'center', justifyContent: 'center', boxShadow: `0 6px 20px rgba(${C.bongRgb},0.5)`}}>
    <svg width={r * 1.1} height={r * 1.1} viewBox="0 0 24 24" fill="none" stroke="#fff" strokeWidth="3.4" strokeLinecap="round" strokeLinejoin="round">
      {ok ? <path d="M5 12.5l4.5 4.5L19 7.5" /> : <path d="M6 6l12 12M18 6L6 18" />}</svg>
  </div>
);
// Khung đừng/hãy: cặp đang nói = cặp cuối đã tới; mỗi cặp mới vào lại cùng chỗ (khuôn lặp)
const DungHayKhung = ({start, f, w, h = Infinity, cap = [], chu_dung = 'ĐỪNG', chu_hay = 'HÃY'}) => {
  const toi = cap.filter((c) => rel(c.at ?? start, start) <= f);
  const c = toi[toi.length - 1] || cap[0];
  if (!c) return null;
  const a = rel(c.at ?? start, start), b = rel(c.at_hay ?? c.at ?? start, start);
  const col = (w - w * 0.06) / 2, th = Math.min(col * 0.75, (h - col * 0.42) * 0.8), fs = Math.min(col * 0.2, th * 0.3);
  const o = (t) => Math.min(1, pop(f, t) * 1.3), y = (t) => (1 - pop(f, t)) * 26;
  const Cot = ({ok, t, nguon}) => (
    <div style={{width: col, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: fs * 0.3, opacity: o(t), transform: `translateY(${y(t)}px)`}}>
      <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: fs * 1.25, lineHeight: 1, color: ok ? XANH : DO, textTransform: 'uppercase',
        textShadow: `0 4px 16px rgba(${C.bongRgb},0.6)`}}>{ok ? chu_hay : chu_dung}</div>
      <div style={{position: 'relative', width: col * 0.86, height: th}}>
        <div style={{width: '100%', height: '100%', borderRadius: fs * 0.5, overflow: 'hidden', border: `3px solid ${ok ? XANH : DO}`,
          boxShadow: `0 20px 60px rgba(${C.bongRgb},0.5)`, filter: ok ? undefined : 'saturate(0.7)'}}><Hinh nguon={nguon} start={start} fs={fs * 0.62} /></div>
        <Dau ok={ok} r={fs * 0.62} />
      </div>
    </div>
  );
  return (
    <div key={cap.indexOf(c)} style={{width: w, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: fs * 0.45}}>
      {c.nhan && <div style={{fontFamily: BODY, fontWeight: 700, fontSize: fs * 0.62, letterSpacing: 3, color: C.text, textTransform: 'uppercase',
        opacity: o(a), textShadow: `0 3px 12px rgba(${C.bongRgb},0.7)`}}>{c.nhan}</div>}
      <div style={{display: 'flex', justifyContent: 'space-between', width: '100%'}}>
        <Cot ok={false} t={a} nguon={c.dung} />
        {f >= b ? <Cot ok t={b} nguon={c.hay} /> : <div style={{width: col}} />}
      </div>
    </div>
  );
};
const DungHay = ({sceneId, start, ...p}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d} = useVideoConfig();
  const m = MAT[sceneId] || {cx: 0.5, cy: 0.42, w: 0.18, h: 0.3};
  const o = Math.min(ease(f, 0, 10), ease(f, d - 6, d, 1, 0, Easing.in(Easing.cubic)));
  const aTop = Math.max(SAFE.top, BRAND_BOT + 40);
  if (!LAND) {
    const w = W - SAFE.left - SAFE.right, hNeed = w * 0.36 + w * 0.2;   // nhãn + chữ đừng/hãy + ô
    const matTren = (m.cy - (m.h || 0.3) / 2) * H;
    if (aTop + hNeed + 30 > matTren) return <ONguoi sceneId={sceneId} start={start} nguoi_duoi noi_dung={{type: 'dung-hay', props: p}} />;   // không che mặt
    return <AbsoluteFill style={{opacity: o}}><div style={{position: 'absolute', left: SAFE.left, top: aTop}}>
      <DungHayKhung start={start} f={f} w={w} h={matTren - aTop - 30} {...p} /></div></AbsoluteFill>;
  }
  const ps = nguoi(m), k = chonCho(ps, W * 0.3, nguoiBam(ps));
  if (k.w < W * 0.3) return <ONguoi sceneId={sceneId} start={start} noi_dung={{type: 'dung-hay', props: p}} />;
  const w = Math.min(W * 0.4, k.w);
  return <AbsoluteFill style={{opacity: o}}><div style={{position: 'absolute', left: k.ke === 'trai' ? k.x1 - w : k.x0, top: aTop + H * 0.04}}>
    <DungHayKhung start={start} f={f} w={w} h={SAFE.bottom - aTop - H * 0.2} {...p} /></div></AbsoluteFill>;
};

// Đối chiếu song song: dọc trên / dưới, ngang trái / phải
const TrenDuoi = ({start, tren = {}, duoi = {}}) => {
  const f = useCurrentFrame();
  const aTop = Math.max(SAFE.top, BRAND_BOT + 40), bot = SAFE.bottom - (LAND ? 110 : 150);   // chừa dải phụ đề
  const gap = 24, x0 = SAFE.left, x1 = W - SAFE.right;
  const o1 = {x: x0, y: aTop, w: LAND ? (x1 - x0 - gap) / 2 : x1 - x0, h: LAND ? bot - aTop : (bot - aTop - gap) / 2};
  const o2 = LAND ? {...o1, x: x0 + o1.w + gap} : {...o1, y: aTop + o1.h + gap};
  const fs = LAND ? H * 0.026 : W * 0.032;
  const O = ({b, nguon, t, tu}) => {
    const p = ease(f, t, t + 14);
    return (
      <div style={{position: 'absolute', left: b.x, top: b.y, width: b.w, height: b.h, borderRadius: 28, overflow: 'hidden', border: `2px solid ${C.line}`,
        boxShadow: `0 30px 80px rgba(${C.bongRgb},0.55)`, opacity: p, transform: LAND ? `translateX(${(1 - p) * 60 * tu}px)` : `translateY(${(1 - p) * 60 * tu}px)`}}>
        <Hinh nguon={nguon} start={start} fs={fs * 1.6} />
        {nguon.nhan && <div style={{position: 'absolute', left: 18, top: 16, padding: `${fs * 0.25}px ${fs * 0.6}px`, borderRadius: fs, background: `rgba(${C.theRgb},0.82)`,
          fontFamily: BODY, fontWeight: 700, fontSize: fs, letterSpacing: 2, color: C.text, textTransform: 'uppercase'}}>{nguon.nhan}</div>}
      </div>
    );
  };
  return <FullShell><O b={o1} nguon={tren} t={2} tu={-1} /><O b={o2} nguon={duoi} t={8} tu={1} /></FullShell>;
};

// Hình toàn khung + người nói trong ô tròn
const OTron = ({sceneId, start, hinh, noi_dung}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d} = useVideoConfig();
  const m = MAT[sceneId] || {cx: 0.5, cy: 0.42, w: 0.18, h: 0.3};
  const D = LAND ? H * 0.3 : W * 0.34;
  const cx = LAND ? W - SAFE.right - D / 2 : (SAFE.left + W - SAFE.right) / 2, cy = SAFE.bottom - (LAND ? 110 : 150) - D / 2;
  const s = Math.max(m.h * H, m.w * W) * 2.3, sc = D / s;   // ô = mặt + tóc + vai
  const k = pop(f, 6), ra = ease(f, d - 8, d, 1, 0);
  const Comp = noi_dung && NOI[noi_dung.type];
  return (
    <FullShell>
      <AbsoluteFill style={{opacity: ease(f, 0, 10)}}>
        {hinh ? <Hinh nguon={hinh} start={start} /> : Comp ? <Comp start={start} sceneId={sceneId} nen={false} {...noi_dung.props} /> : null}
      </AbsoluteFill>
      {hinh && <AbsoluteFill style={{background: `linear-gradient(transparent 55%, rgba(${C.theRgb},0.6))`}} />}
      <div style={{position: 'absolute', left: cx - D / 2, top: cy - D / 2, width: D, height: D, borderRadius: '50%', overflow: 'hidden',
        border: `4px solid ${C.accent}`, boxShadow: `0 20px 60px rgba(${C.bongRgb},0.6)`, transform: `scale(${k * ra})`}}>
        <OffthreadVideo src={staticFile('goc.mp4')} trimBefore={fr(start)} muted
          style={{position: 'absolute', left: D / 2 - m.cx * W * sc, top: D / 2 - m.cy * H * sc, width: W * sc, height: H * sc, maxWidth: 'none'}} />
      </div>
    </FullShell>
  );
};

// Thẻ câu hỏi (phỏng vấn): dưới mặt người, vạch màu nhấn bên trái
const CauHoi = ({start, cau = '', at, nhan}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d} = useVideoConfig();
  const a = rel(at ?? start, start), p = pop(f, a), o = Math.min(Math.min(1, p * 1.3), ease(f, d - 6, d, 1, 0));
  const w = LAND ? W * 0.42 : W - SAFE.left - SAFE.right, fs = LAND ? H * 0.04 : W * 0.052;
  return (
    <AbsoluteFill style={{opacity: o}}>
      <div style={{position: 'absolute', left: SAFE.left, top: SAFE.overlayTop, width: w, display: 'flex', gap: fs * 0.45,
        transform: `translateX(${(1 - p) * -40}px)`}}>
        <div style={{flex: 'none', width: Math.max(6, fs * 0.16), borderRadius: 4, background: C.accent}} />
        <div style={{padding: `${fs * 0.4}px ${fs * 0.6}px`, borderRadius: fs * 0.4, background: `rgba(${C.theRgb},0.86)`}}>
          {nhan && <div style={{fontFamily: BODY, fontWeight: 700, fontSize: fs * 0.5, letterSpacing: 3, color: C.accent, textTransform: 'uppercase', marginBottom: fs * 0.2}}>{nhan}</div>}
          <div style={{fontFamily: BODY, fontWeight: 700, fontSize: fs, lineHeight: 1.25, color: C.text, textWrap: 'balance'}}>
            <ChuHien text={cau} a={a + 2} kieu="muc" /></div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

export const BoCuc = ({kieu = 'o-nguoi', ...p}) =>
  kieu === 'the-canh' ? <TheCanh {...p} /> : kieu === 'chuong' ? <Chuong {...p} /> : kieu === 'tien-trinh' ? <TienTrinh {...p} />
    : kieu === 'dung-hay' ? <DungHay {...p} /> : kieu === 'tren-duoi' ? <TrenDuoi {...p} /> : kieu === 'o-tron' ? <OTron {...p} />
    : kieu === 'cau-hoi' ? <CauHoi {...p} />
    : kieu === 'canh-nguoi' ? <CanhNguoi {...p} />
      : kieu === 'muc-luc' ? <ONguoi {...p} noi_dung={{type: 'muc-luc', props: {tieu_de: p.tieu_de, muc: p.muc}}} /> : <ONguoi {...p} />;
