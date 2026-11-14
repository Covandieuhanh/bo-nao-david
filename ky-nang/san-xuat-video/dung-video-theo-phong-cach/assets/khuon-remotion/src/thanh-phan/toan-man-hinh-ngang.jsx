// Cảnh toàn màn hình bản NGANG 1920×1080, thiết kế toàn khung (podcast ngang — không chia cột).
// Cùng props với bản dọc (toan-man-hinh.jsx); Root tự chọn bản này khi khung ngang. Nội dung trong x 96–1824, y 54–790
// (dưới 790 là phụ đề + thanh thời gian). recap/converge/master chưa có bản ngang → đừng dùng ở khung ngang.
import React from 'react';
import {AbsoluteFill, Img, staticFile, useCurrentFrame} from 'remotion';
import {BODY, C, HEAD, ease, pop, rel} from '../chu-de';
import {Eyebrow} from './lop-phu';
import {FullShell} from './toan-man-hinh';
import {Pictogram} from '../thu-vien/bieu-tuong';
import {PF, VN, aboveGap} from '../khung-podcast';

const fit = (text, w, max) => Math.min(max, Math.floor(w / (Math.max(1, text.length) * 0.46)));

// ---------- Danh sách có ảnh: ảnh lớn trái, số đếm + nhãn phải ----------
export const MontageL = ({start, eyebrow, items, total = Math.max(...items.map((it) => it.n || 0)), counter = true}) => {
  const f = useCurrentFrame();
  const at = items.map((it) => rel(it.at, start));
  let idx = 0;
  at.forEach((a, i) => { if (f >= a) idx = i; });
  const RX = 1170, RW = PF.right - RX;
  return (
    <FullShell>
      <div style={{position: 'absolute', top: 70, left: PF.left}}><Eyebrow style={{opacity: ease(f, 2, 12)}}>{eyebrow}</Eyebrow></div>
      {items.map((it, i) => {
        if (i < idx - 1 || i > idx) return null;
        const lf = f - at[i];
        const p = pop(lf, 0, {damping: 20, stiffness: 160, mass: 0.7});
        const leaving = i < idx ? ease(f - at[idx], 0, 8) : 0;
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', top: 130, left: PF.left, width: 1020, height: 640, borderRadius: 40, overflow: 'hidden',
              boxShadow: '0 40px 100px rgba(0,0,0,0.6)', border: `2px solid ${C.line}`, opacity: Math.min(1, p * 1.5) * (1 - leaving),
              transform: `translateY(${(1 - p) * 120 - leaving * 80}px) rotate(${(1 - p) * -3}deg) scale(${0.92 + 0.08 * p})`}}>
              {it.icon ? <Pictogram name={it.icon} w={1020} h={640} at={at[i]} />   // không ảnh: biểu tượng vẽ dần
                : <Img src={staticFile(`anh/${it.photo}`)} style={{width: '100%', height: '100%', objectFit: 'cover',
                transform: `scale(${1.15 - ease(lf, 0, 90) * 0.1})`}} />}
            </div>
            <div style={{position: 'absolute', left: RX, width: RW, top: 170, opacity: 1 - leaving}}>
              {counter && <div style={{display: 'flex', alignItems: 'baseline', gap: 14, marginBottom: 30, transform: `translateY(${(1 - p) * 40}px)`}}>
                <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 150, lineHeight: 1, color: 'transparent', WebkitTextStroke: `4px ${C.accent}`}}>
                  {String(it.n).padStart(2, '0')}</div>
                <div style={{fontFamily: HEAD, fontWeight: 700, fontSize: 56, color: C.dim}}>/ {total}</div>
              </div>}
              {it.kicker && <div style={{fontFamily: BODY, fontWeight: 600, fontSize: 40, color: C.accent, marginBottom: 8, opacity: ease(lf, 2, 12)}}>{it.kicker}</div>}
              <div style={{overflow: 'hidden', paddingTop: fit(it.label, RW, 150) * VN.top, paddingBottom: fit(it.label, RW, 150) * VN.bot,
                marginTop: (it.kicker ? aboveGap(fit(it.label, RW, 150)) : 0) - fit(it.label, RW, 150) * VN.top}}>   {/* chừa chỗ dấu chồng dưới kicker */}
                <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: fit(it.label, RW, 150), lineHeight: VN.lh + VN.gap, color: C.text,
                  textTransform: 'uppercase', transform: `translateY(${(1 - pop(lf, 3)) * 110}%)`}}>{it.label}</div>
              </div>
            </div>
          </React.Fragment>
        );
      })}
    </FullShell>
  );
};

// ---------- Các lớp chồng lên nhau (trái) + chữ lớn (phải) ----------
export const GensL = ({start, eyebrow, layers, years, yearsAt, unit = 'NĂM'}) => {
  const f = useCurrentFrame();
  const y = pop(f, rel(yearsAt, start));
  const base = 740, cx = 560, H0 = 140;
  return (
    <FullShell>
      <div style={{position: 'absolute', top: 70, left: PF.left}}><Eyebrow style={{opacity: ease(f, 2, 12)}}>{eyebrow}</Eyebrow></div>
      {layers.map((l, i) => {
        const p = pop(f, rel(l.at, start), {damping: 18, stiffness: 150, mass: 0.8});
        const w = 760 - i * 90, lastL = i === layers.length - 1;
        return (
          <div key={i} style={{position: 'absolute', left: cx - w / 2, top: base - (i + 1) * (H0 + 16), width: w, height: H0, borderRadius: 22,
            background: lastL ? C.accent : 'rgba(255,255,255,0.07)', border: `2px solid ${lastL ? C.accent : C.line}`,
            display: 'flex', alignItems: 'center', justifyContent: 'center', opacity: Math.min(1, p * 1.4), transform: `translateY(${(1 - p) * -160}px)`}}>
            <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 72, letterSpacing: 2, color: lastL ? C.bg : C.text}}>{l.label}</div>
          </div>
        );
      })}
      <div style={{position: 'absolute', top: base, left: cx - 420, width: 840, height: 10, borderRadius: 5, background: C.dim}} />
      <div style={{position: 'absolute', left: 1080, width: PF.right - 1080, top: 300, opacity: Math.min(1, y * 1.4),
        transform: `translateX(${(1 - y) * 60}px)`}}>
        <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: fit(String(years), PF.right - 1080, 200), lineHeight: VN.lh, color: C.text}}>{years}</div>
        {unit && <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 90, color: C.accent, marginTop: 10}}>{unit}</div>}
      </div>
    </FullShell>
  );
};

// ---------- Xây từng bước: công trình trái, BƯỚC n + nhãn phải ----------
export const BuildL = ({start, eyebrow, steps}) => {
  const f = useCurrentFrame();
  let idx = 0;
  steps.forEach((s, i) => { if (f >= rel(s.at, start)) idx = i; });
  const cur = steps[idx];
  const cp = pop(f, rel(cur.at, start));
  const base = 760, cx = 560, RX = 1080, RW = PF.right - RX;
  return (
    <FullShell>
      <div style={{position: 'absolute', top: 70, left: PF.left}}><Eyebrow style={{opacity: ease(f, 2, 12)}}>{eyebrow}</Eyebrow></div>
      {steps.map((s, i) => {
        const p = pop(f, rel(s.at, start), {damping: 18, stiffness: 140, mass: 0.8});
        const isBase = i === 0, w = isBase ? 780 : 580, h = isBase ? 80 : 150;
        const top = isBase ? base - h : base - 80 - i * (150 + 12);
        const active = i === idx;
        return (
          <div key={i} style={{position: 'absolute', left: cx - w / 2, top, width: w, height: h, borderRadius: isBase ? 12 : 18,
            background: active ? C.accent : isBase ? '#3F3F46' : 'rgba(255,255,255,0.08)', border: `2px solid ${active ? C.accent : C.line}`,
            opacity: Math.min(1, p * 1.4), transform: `translateY(${(1 - p) * -140}px)`, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 22}}>
            {!isBase && [0, 1, 2].map((k) => <div key={k} style={{width: 100, height: 72, borderRadius: 10, background: active ? 'rgba(13,13,16,0.25)' : 'rgba(255,255,255,0.08)'}} />)}
            {isBase && <div style={{fontFamily: BODY, fontWeight: 700, fontSize: 30, letterSpacing: 4, color: active ? C.bg : C.muted}}>MÓNG</div>}
          </div>
        );
      })}
      <div style={{position: 'absolute', top: base, left: cx - 460, width: 920, height: 10, borderRadius: 5, background: C.dim}} />
      <div key={idx} style={{position: 'absolute', left: RX, width: RW, top: 260, opacity: Math.min(1, cp * 1.4), transform: `translateY(${(1 - cp) * 30}px)`}}>
        <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 110, lineHeight: VN.lh + VN.gap, color: C.accent}}>BƯỚC {cur.n}</div>
        <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: fit(cur.label, RW, 120), lineHeight: VN.lh + VN.gap, color: C.text, textTransform: 'uppercase', marginTop: aboveGap(fit(cur.label, RW, 120)) - fit(cur.label, RW, 120) * (VN.lh - 1)}}>{cur.label}</div>
      </div>
    </FullShell>
  );
};
