// BỐ CỤC (type 'bocuc' — lớp trình bày, David chốt 2026-11-07; xem ../../../../trinh-bay/README.md)
// Chỉ lo SẮP XẾP: người ở đâu, nội dung ở đâu, hiện theo thứ tự nào. Màu, chữ, nét, chuyển động lấy từ thư viện hình (lib/tokens,
// Illus, Diagram, Icons) — học bố cục mới thì thêm `kieu` ở đây, KHÔNG thêm màu / font / kiểu chuyển động riêng.
// Không có con số bắt buộc: vị trí, cỡ ô, độ dài cảnh do Claude tự cân theo nội dung (props ghi đè mặc định).
//
// kieu:
//  'o-nguoi'  người thu vào một ô bo góc, phần còn lại của khung là nội dung. Ô co từ toàn khung vào chỗ, hết cảnh nở lại.
//             Tỉ lệ ô TỰ DO = tỉ lệ khung cắt quanh người đang nói (không cố định 16:9 hay dọc); không bao giờ cắt ngang
//             một gương mặt — người bên cạnh hoặc vào trọn, hoặc ra hẳn; ô nằm đúng phía người đó ngồi, nội dung phía còn lại.
//             props: noi_dung: {type: 'illus'|'diagram'|'the', props} · khung? 'ca-hai' (ô chứa mọi người) · bam? 'trai'|'phai'
//             · o? {x, y, w, h} (0–1, chỉ khi thật cần ép tay)
//  'the-canh' người giữ nguyên khung, thẻ vào khoảng trống sát người đang nói (lib/cho.js), co theo khoảng trống, không đè ai;
//             không khoảng nào đủ rộng → tự chuyển sang 'o-nguoi'. props: bam? · tieu_de? · dong: [{text, at, to?: true, gach?: <giây>}]
//  'chuong'   màn chương toàn khung: số mờ to + nhãn nhỏ + tên phần (dòng cuối màu nhấn). props: so?, nhan?, ten
// Chữ trong thẻ / chương là NGUYÊN VĂN lời người nói (luật chữ trên màn hình).
import React from 'react';
import {AbsoluteFill, Easing, OffthreadVideo, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {BODY, C, HEAD, SAFE, BRAND_BOT, ease, pop, rel} from '../theme';
import {FullShell} from './FullScreen';
import {Illus} from '../lib/Illus';
import {Diagram} from '../lib/Diagram';
import project from '../project.js';
import {fr} from '../scenes';
import MAT from '../mat.js';
import {nguoi, chonCho, nguoiBam} from '../lib/cho';
import {ChuHien} from '../lib/ChuHien';
import {kieuChu} from '../lib/chuyen-dong';

const W = project.width, H = project.height, LAND = W > H;
const NOI = {illus: Illus, diagram: Diagram};

// Thẻ chữ hiện dần (dùng cho 'the-canh' và nội dung 'the' trong 'o-nguoi')
// Xuống dòng cân (textWrap balance): dòng đều nhau, không để một chữ đứng lẻ ("LUYỆN TẬP LẠI THÓI / QUEN" — lỗi 09/11/2026);
// '\n' trong chữ = chỗ xuống dòng theo cụm nghĩa do kịch bản đặt.
const The = ({start, tieu_de, dong = [], w, f, fs, kc = 'mo'}) => (
  <div style={{width: w, padding: fs * 0.9, borderRadius: fs * 0.7, background: C.card, border: `2px solid ${C.line}`,
    boxShadow: '0 30px 90px rgba(0,0,0,0.5)', backdropFilter: 'blur(14px)', display: 'flex', flexDirection: 'column', gap: fs * 0.35}}>
    {tieu_de && <div style={{fontFamily: BODY, fontWeight: 700, fontSize: fs * 0.42, letterSpacing: 3, color: C.accent, textTransform: 'uppercase',
      opacity: ease(f, 2, 10), textWrap: 'balance'}}>{tieu_de}</div>}
    {dong.map((d, i) => {
      const a = rel(d.at ?? start, start), p = pop(f, a);
      const g = d.gach != null ? ease(f, rel(d.gach, start), rel(d.gach, start) + 8) : 0;
      return (
        <div key={i} style={{position: 'relative', alignSelf: 'flex-start', opacity: 1 - 0.45 * g}}>
          <div style={{fontFamily: d.to ? HEAD : BODY, fontWeight: d.to ? 800 : 500, lineHeight: 1.08,
            fontSize: d.to ? Math.max(fs * 0.8, Math.min(fs * 1.35, (w - fs * 1.8) / (0.46 * Math.max(4, d.text.length)))) : fs * 0.62,   // chữ to: co cho vừa một dòng, không nhỏ hơn 0,8 — dài quá thì xuống dòng
            color: d.to && i === dong.length - 1 ? C.accent : C.text, textTransform: d.to ? 'uppercase' : 'none',
            textWrap: 'balance', whiteSpace: 'pre-line', hyphens: 'none'}}><ChuHien text={d.text} a={a} kieu={kc} /></div>
          {g > 0 && <div style={{position: 'absolute', left: 0, top: '52%', height: Math.max(3, fs * 0.08), width: `${g * 100}%`, background: C.accent}} />}
        </div>
      );
    })}
  </div>
);

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

const ONguoi = ({sceneId, start, o, noi_dung, khung, bam}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d} = useVideoConfig();
  const m = MAT[sceneId] || {cx: 0.5, cy: 0.42, w: 0.18, h: 0.3};
  const kc = khungCat(m, khung, bam);
  const cw = (kc.r - kc.l) * W, ch = (kc.b - kc.t) * H, ar = cw / ch;
  // cỡ ô: theo tỉ lệ khung cắt, vừa trong tối đa 46% bề ngang × 72% bề cao (ngang) — dọc: rộng hết, cao tối đa 40%
  const maxW = LAND ? W * 0.46 : W * 0.88, maxH = LAND ? H * 0.72 : H * 0.4;
  const bw = Math.min(maxW, maxH * ar), bh = bw / ar;
  const aTop = Math.max(SAFE.top, BRAND_BOT + 40);   // dưới dấu góc kênh (theme.js)
  const b = o ? {x: o.x * W, y: o.y * H, w: o.w * W, h: o.h * H}
    : LAND ? {x: kc.phia === 'trai' ? SAFE.left : W - SAFE.right - bw, y: aTop + (SAFE.bottom - aTop - bh) / 2, w: bw, h: bh}
      : {x: (W - bw) / 2, y: H * 0.07, w: bw, h: bh};
  // co vào (14 khung) · nở lại toàn khung ở cuối (10 khung)
  const k = Math.min(ease(f, 0, 14), ease(f, d - 10, d, 1, 0, Easing.inOut(Easing.cubic)));
  const x = b.x * k, y = b.y * k, w = W + (b.w - W) * k, h = H + (b.h - H) * k;
  const cl = kc.l * k, ct = kc.t * k, cr = 1 + (kc.r - 1) * k, cb = 1 + (kc.b - 1) * k;   // khung cắt từ toàn khung → khung người
  const sc = Math.max(w / ((cr - cl) * W), h / ((cb - ct) * H));
  // vùng nội dung = phía còn lại, chừa dải phụ đề
  const area = LAND
    ? (kc.phia === 'trai' && !o ? {x: b.x + b.w + SAFE.left * 0.8, y: aTop, w: W - SAFE.right - (b.x + b.w + SAFE.left * 0.8), h: SAFE.bottom - aTop}
      : {x: SAFE.left, y: aTop, w: b.x - SAFE.left * 1.8, h: SAFE.bottom - aTop})
    : {x: SAFE.left, y: b.y + b.h + 30, w: W - SAFE.left - SAFE.right * 0.4, h: SAFE.bottom - (b.y + b.h) - 60};
  const show = ease(f, 8, 18) * ease(f, d - 12, d - 4, 1, 0);
  const Comp = noi_dung && NOI[noi_dung.type];
  const s = Math.min(1, area.w / (W * 0.6), area.h / (H * (LAND ? 0.64 : 0.46)));
  const cx = area.x + area.w / 2, cy = area.y + area.h / 2;
  return (
    <FullShell hold>
      <div style={{position: 'absolute', left: x, top: y, width: w, height: h, borderRadius: 36 * k, overflow: 'hidden',
        border: k > 0.5 ? `3px solid ${C.accent}` : 'none', boxShadow: '0 30px 90px rgba(0,0,0,0.6)'}}>
        <OffthreadVideo src={staticFile('goc.mp4')} trimBefore={fr(start)} muted
          style={{position: 'absolute', left: -cl * W * sc + (w - (cr - cl) * W * sc) / 2, top: -ct * H * sc + (h - (cb - ct) * H * sc) / 2,
            width: W * sc, height: H * sc, maxWidth: 'none'}} />
      </div>
      {noi_dung && (
        Comp ? <div style={{position: 'absolute', left: cx - W * s / 2, top: cy - H * (LAND ? 0.39 : 0.33) * s, width: W, height: H, opacity: show,
            transform: `scale(${s})`, transformOrigin: '0 0'}}><Comp start={start} sceneId={sceneId} nen={false} {...noi_dung.props} /></div>
          : <div style={{position: 'absolute', left: area.x, top: area.y, width: area.w, height: area.h, opacity: show,
            display: 'flex', alignItems: LAND ? 'center' : 'flex-start', justifyContent: 'center'}}>
            <The start={start} f={f} w={area.w * 0.92} fs={LAND ? H * 0.06 : W * 0.075} {...noi_dung.props} /></div>
      )}
    </FullShell>
  );
};

// THẺ CẠNH NGƯỜI (David chốt 08/11): thẻ vào khoảng trống sát người đang nói (hoặc props.bam), co theo khoảng trống, không đè ai.
// Không khoảng nào đủ rộng → chuyển sang ô người (người thu vào ô, thẻ ở phía còn lại).
const TheCanh = ({sceneId, start, ben, bam, tieu_de, dong}) => {
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
          <The start={start} f={f} w={W - SAFE.left - SAFE.right} fs={W * 0.07} tieu_de={tieu_de} dong={dong} kc={kieuChu(sceneId)} />
        </div>
      </AbsoluteFill>
    );
  }
  const ps = nguoi(m);
  const t = nguoiBam(ps, bam || ben);
  const MIN = W * 0.2;
  const k = chonCho(ps, MIN, t);
  if (k.w < MIN) return <ONguoi sceneId={sceneId} start={start} bam={bam || ben} noi_dung={{type: 'the', props: {tieu_de, dong}}} />;
  const w = Math.min(W * 0.34, k.w);
  const left = k.ke === 'trai' ? k.x1 - w : k.x0;     // sát người được bám
  const slide = (1 - ease(f, 0, 14)) * 60 * (k.ke === 'phai' ? 1 : -1);
  const fs = Math.min(H * 0.055, w / 9);
  return (
    <AbsoluteFill style={{opacity: o, filter: mo}}>
      <div style={{position: 'absolute', left, top: Math.max(H * 0.17, BRAND_BOT + 40), transform: `translateX(${slide}px)`}}>
        <The start={start} f={f} w={w} fs={fs} tieu_de={tieu_de} dong={dong} kc={kieuChu(sceneId)} />
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

export const BoCuc = ({kieu = 'o-nguoi', ...p}) =>
  kieu === 'the-canh' ? <TheCanh {...p} /> : kieu === 'chuong' ? <Chuong {...p} /> : <ONguoi {...p} />;
