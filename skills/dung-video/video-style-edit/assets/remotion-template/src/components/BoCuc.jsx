// BỐ CỤC (type 'bocuc' — lớp trình bày, David chốt 2026-11-07; xem ../../../../trinh-bay/README.md)
// Chỉ lo SẮP XẾP: người ở đâu, nội dung ở đâu, hiện theo thứ tự nào. Màu, chữ, nét, chuyển động lấy từ thư viện hình (lib/tokens,
// Illus, Diagram, Icons) — học bố cục mới thì thêm `kieu` ở đây, KHÔNG thêm màu / font / kiểu chuyển động riêng.
// Không có con số bắt buộc: vị trí, cỡ ô, độ dài cảnh do Claude tự cân theo nội dung (props ghi đè mặc định).
//
// kieu:
//  'o-nguoi'  người thu vào một ô bo góc, phần còn lại của khung là nội dung. Ô co từ toàn khung vào chỗ, hết cảnh nở lại.
//             props: o? {x, y, w, h} (0–1 theo khung; mặc định ngang = cột phải, dọc = nửa trên) · noi_dung: {type: 'illus'|'diagram'|'the', props}
//  'the-canh' người giữ nguyên khung, một thẻ ở phía còn trống cạnh mặt (mat.js), chữ hiện dần theo lời.
//             props: ben? 'trai'|'phai' (mặc định phía trống) · tieu_de? · dong: [{text, at, to?: true, gach?: <giây>}]
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

const W = project.width, H = project.height, LAND = W > H;
const NOI = {illus: Illus, diagram: Diagram};

// Thẻ chữ hiện dần (dùng cho 'the-canh' và nội dung 'the' trong 'o-nguoi')
const The = ({start, tieu_de, dong = [], w, f, fs}) => (
  <div style={{width: w, padding: fs * 0.9, borderRadius: fs * 0.7, background: C.card, border: `2px solid ${C.line}`,
    boxShadow: '0 30px 90px rgba(0,0,0,0.5)', backdropFilter: 'blur(14px)', display: 'flex', flexDirection: 'column', gap: fs * 0.35}}>
    {tieu_de && <div style={{fontFamily: BODY, fontWeight: 700, fontSize: fs * 0.42, letterSpacing: 3, color: C.accent, textTransform: 'uppercase',
      opacity: ease(f, 2, 10)}}>{tieu_de}</div>}
    {dong.map((d, i) => {
      const a = rel(d.at ?? start, start), p = pop(f, a);
      const g = d.gach != null ? ease(f, rel(d.gach, start), rel(d.gach, start) + 8) : 0;
      return (
        <div key={i} style={{position: 'relative', alignSelf: 'flex-start', opacity: Math.min(1, p * 1.4) * (1 - 0.45 * g),
          transform: `translateY(${(1 - p) * fs * 0.6}px)`}}>
          <div style={{fontFamily: d.to ? HEAD : BODY, fontWeight: d.to ? 800 : 500, lineHeight: 1.08,
            fontSize: d.to ? Math.max(fs * 0.8, Math.min(fs * 1.35, (w - fs * 1.8) / (0.46 * Math.max(4, d.text.length)))) : fs * 0.62,   // chữ to: co cho vừa một dòng, không nhỏ hơn 0,8 — dài quá thì xuống dòng
            color: d.to && i === dong.length - 1 ? C.accent : C.text, textTransform: d.to ? 'uppercase' : 'none'}}>{d.text}</div>
          {g > 0 && <div style={{position: 'absolute', left: 0, top: '52%', height: Math.max(3, fs * 0.08), width: `${g * 100}%`, background: C.accent}} />}
        </div>
      );
    })}
  </div>
);

const ONguoi = ({sceneId, start, o, noi_dung}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d} = useVideoConfig();
  const m = MAT[sceneId] || {cx: 0.5, cy: 0.42};
  const b = o || (LAND ? {x: 0.62, y: 0.12, w: 0.33, h: 0.7} : {x: 0.06, y: 0.07, w: 0.88, h: 0.36});
  // co vào (14 khung) · nở lại toàn khung ở cuối (10 khung) — người xem thấy "người lùi lại nhường chỗ cho nội dung" rồi trở về
  const k = Math.min(ease(f, 0, 14), ease(f, d - 10, d, 1, 0, Easing.inOut(Easing.cubic)));
  const x = b.x * W * k, y = b.y * H * k, w = W + (b.w * W - W) * k, h = H + (b.h * H - H) * k;
  // vùng nội dung = phần khung còn lại (bên trái ô khi ngang, bên dưới ô khi dọc), chừa dải phụ đề ở đáy
  const aTop = Math.max(SAFE.top, BRAND_BOT + 40);   // dưới dấu góc kênh (theme.js)
  const area = LAND ? {x: SAFE.left, y: aTop, w: b.x * W - SAFE.left * 1.6, h: SAFE.bottom - aTop}
    : {x: SAFE.left, y: (b.y + b.h) * H + 30, w: W - SAFE.left - SAFE.right * 0.4, h: SAFE.bottom - (b.y + b.h) * H - 60};
  const show = ease(f, 8, 18) * ease(f, d - 12, d - 4, 1, 0);
  const Comp = noi_dung && NOI[noi_dung.type];
  // hình minh hoạ vẽ trên khung đầy đủ (vùng vẽ ~ giữa 60% bề ngang, tâm dọc ~0,39) → thu cho vừa vùng nội dung, canh tâm vùng
  const s = Math.min(1, area.w / (W * 0.6), area.h / (H * (LAND ? 0.64 : 0.46)));   // vùng vẽ Illus: ngang 7–71% · dọc 10–56% chiều cao
  const cx = area.x + area.w / 2, cy = area.y + area.h / 2;
  return (
    <FullShell hold>
      <div style={{position: 'absolute', left: x, top: y, width: w, height: h, borderRadius: 36 * k, overflow: 'hidden',
        border: k > 0.5 ? `3px solid ${C.accent}` : 'none', boxShadow: '0 30px 90px rgba(0,0,0,0.6)'}}>
        <OffthreadVideo src={staticFile('goc.mp4')} trimBefore={fr(start)} muted
          style={{width: '100%', height: '100%', objectFit: 'cover', objectPosition: `${m.cx * 100}% ${m.cy * 100}%`}} />
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

const TheCanh = ({sceneId, start, ben, tieu_de, dong}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d} = useVideoConfig();
  const m = MAT[sceneId] || {cx: 0.5, cy: 0.42, w: 0.18};
  const side = ben || (m.cx > 0.5 ? 'trai' : 'phai');
  const o = Math.min(ease(f, 0, 10), ease(f, d - 8, d, 1, 0, Easing.in(Easing.cubic)));
  const slide = (1 - ease(f, 0, 14)) * 60 * (side === 'phai' ? 1 : -1);
  if (!LAND) {   // dọc: một thẻ hẹp phía dưới mặt, trên dải phụ đề — ít chữ cùng lúc
    return (
      <AbsoluteFill style={{opacity: o}}>
        <div style={{position: 'absolute', left: SAFE.left, top: SAFE.overlayTop, transform: `translateY(${-slide}px)`}}>
          <The start={start} f={f} w={W - SAFE.left - SAFE.right} fs={W * 0.07} tieu_de={tieu_de} dong={dong} />
        </div>
      </AbsoluteFill>
    );
  }
  const faceR = ((m.r ?? m.cx + m.w / 2) + m.w * 0.35) * W, faceL = ((m.l ?? m.cx - m.w / 2) - m.w * 0.35) * W;
  const room = side === 'phai' ? W - SAFE.right - faceR : faceL - SAFE.left;
  const w = Math.max(W * 0.24, Math.min(W * 0.34, room));
  const left = side === 'phai' ? W - SAFE.right - w : SAFE.left;
  return (
    <AbsoluteFill style={{opacity: o}}>
      <div style={{position: 'absolute', left, top: Math.max(H * 0.17, BRAND_BOT + 40), transform: `translateX(${slide}px)`}}>   {/* dưới dấu góc kênh (BRAND_BOT, theme.js) */}
        <The start={start} f={f} w={w} fs={H * 0.055} tieu_de={tieu_de} dong={dong} />
      </div>
    </AbsoluteFill>
  );
};

const Chuong = ({start, so, nhan, ten = ''}) => {
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
          const p = pop(f, 8 + i * 5);
          return <div key={i} style={{fontFamily: HEAD, fontWeight: 800, fontSize: fs, lineHeight: 1.02, textTransform: 'uppercase',
            color: i === lines.length - 1 && lines.length > 1 ? C.accent : C.text, opacity: Math.min(1, p * 1.3),
            transform: `translateY(${(1 - p) * 40}px)`}}>{l}</div>;
        })}
      </div>
    </FullShell>
  );
};

export const BoCuc = ({kieu = 'o-nguoi', ...p}) =>
  kieu === 'the-canh' ? <TheCanh {...p} /> : kieu === 'chuong' ? <Chuong {...p} /> : <ONguoi {...p} />;
