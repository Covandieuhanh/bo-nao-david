// Cảnh toàn màn hình (thay hẳn hình người nói, tiếng vẫn chạy).
// Mọi nội dung nằm trong vùng an toàn x 70–900, y 210–1420; phần ngoài chỉ có nền.
import React from 'react';
import {vaoRa, tien, EASE} from '../lib/chuyen-dong';
import {AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {BODY, C, HEAD, SAFE, SAFE_W, ease, inOut, pop, rel} from '../theme';
import {Eyebrow} from './Overlays';
import {Pictogram} from '../lib/Icons';
import CAPTIONS from '../captions.js';
import {FULL_ORIGIN, FULL_SCALE, POD, VN, aboveGap} from '../podframe';

export const FullShell = ({children, hold}) => {   // hold: không mờ ra ở cuối (màn chốt kết thúc video)
  const f = useCurrentFrame();
  const {durationInFrames: d} = useVideoConfig();
  // vào: mờ nhoè → nét, đuôi dài; ra: ngắn hơn ~40 %, tăng tốc, mờ nhoè (thư viện hình chuyen-dong.js)
  const v = vaoRa(f, hold ? 1e9 : d, {vao: 9, ra: 5, mo: 12});
  return (
    <AbsoluteFill style={{opacity: v.opacity, filter: v.filter, background: C.bg, transform: `scale(${1.03 - 0.03 * tien(f, 0, 14, EASE.camera)})`}}>
      <AbsoluteFill style={{background: `radial-gradient(circle at 45% 38%, rgba(255,122,69,0.16), transparent 60%)`}} />
      <AbsoluteFill style={{backgroundImage: `linear-gradient(${C.line} 2px, transparent 2px), linear-gradient(90deg, ${C.line} 2px, transparent 2px)`,
        backgroundSize: '120px 120px', opacity: 0.35, maskImage: 'radial-gradient(circle at 50% 45%, black, transparent 75%)'}} />
      {POD ? <AbsoluteFill style={{transform: `scale(${FULL_SCALE})`, transformOrigin: FULL_ORIGIN}}>{children}</AbsoluteFill> : children}
    </AbsoluteFill>
  );
};

const Dots = ({filled, total = 12, y = 1374}) => (
  <div style={{position: 'absolute', top: y, left: SAFE.left, display: 'flex', gap: 12}}>
    {Array.from({length: total}).map((_, i) => (
      <div key={i} style={{width: i < filled ? 36 : 14, height: 14, borderRadius: 7,
        background: i < filled ? C.accent : C.dim, transition: 'none'}} />
    ))}
  </div>
);

// ---------- Dồn dập từng nghề, có ảnh ----------
// total: tổng số mục để đếm "05 / 12" (mặc định = số lớn nhất trong items); counter: false = bỏ số đếm + chấm
export const Montage = ({start, eyebrow, items, total = Math.max(...items.map((it) => it.n || 0)), counter = true}) => {
  const f = useCurrentFrame();
  const at = items.map((it) => rel(it.at, start));
  let idx = 0;
  at.forEach((a, i) => { if (f >= a) idx = i; });
  return (
    <FullShell>
      <div style={{position: 'absolute', top: 240, left: SAFE.left, width: SAFE_W}}>
        <Eyebrow style={{opacity: ease(f, 2, 12)}}>{eyebrow}</Eyebrow>
      </div>
      {items.map((it, i) => {
        if (i < idx - 1 || i > idx) return null;
        const lf = f - at[i];
        const p = pop(lf, 0, {damping: 20, stiffness: 160, mass: 0.7});
        const leaving = i < idx ? ease(f - at[idx], 0, 8) : 0;
        return (
          <React.Fragment key={i}>
            {counter && <div style={{position: 'absolute', top: 280, left: SAFE.left, display: 'flex', alignItems: 'baseline', gap: 14,
              opacity: (1 - leaving)}}>
              <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 150, lineHeight: 1, color: 'transparent',
                WebkitTextStroke: `4px ${C.accent}`, transform: `translateY(${(1 - p) * 60}px)`}}>
                {String(it.n).padStart(2, '0')}
              </div>
              <div style={{fontFamily: HEAD, fontWeight: 700, fontSize: 56, color: C.dim}}>/ {total}</div>
            </div>}
            <div style={{position: 'absolute', top: 440, left: SAFE.left, width: SAFE_W, height: 570, borderRadius: 40,
              overflow: 'hidden', boxShadow: '0 40px 100px rgba(0,0,0,0.6)', border: `2px solid ${C.line}`,
              opacity: Math.min(1, p * 1.5) * (1 - leaving),
              transform: `translateX(${(1 - p) * 260 - leaving * 160}px) rotate(${(1 - p) * 4}deg) scale(${0.92 + 0.08 * p})`}}>
              {it.icon ? <Pictogram name={it.icon} w={SAFE_W} h={570} at={at[i]} />   // không ảnh: biểu tượng vẽ dần
                : <Img src={staticFile(`photos/${it.photo}`)} style={{width: '100%', height: '100%', objectFit: 'cover',
                transform: `scale(${1.15 - ease(lf, 0, 90) * 0.1})`}} />}
              <AbsoluteFill style={{background: 'linear-gradient(transparent 55%, rgba(0,0,0,0.55))'}} />
            </div>
            {/* Chữ dưới khung ảnh: cách mép ảnh 34 px; dòng nhỏ (kicker) rồi chữ to — chừa aboveGap cho dấu chồng của chữ to */}
            <div style={{position: 'absolute', top: 1044, left: SAFE.left, width: SAFE_W, opacity: 1 - leaving}}>
              {it.kicker && <div style={{fontFamily: BODY, fontWeight: 600, fontSize: 38, lineHeight: 1.3, color: C.accent,
                opacity: ease(lf, 2, 12)}}>{it.kicker}</div>}
              {(() => {
                const size = it.label.length > 11 ? 92 : 120;
                return (
                  <div style={{overflow: 'hidden', paddingTop: size * VN.top, paddingBottom: size * VN.bot,
                    marginTop: (it.kicker ? aboveGap(size) : 0) - size * VN.top, marginBottom: -size * VN.bot}}>
                    <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: size, lineHeight: VN.lh + VN.gap,
                      color: C.text, textTransform: 'uppercase', transform: `translateY(${(1 - pop(lf, 3)) * 110}%)`}}>
                      {it.label}
                    </div>
                  </div>
                );
              })()}
            </div>
          </React.Fragment>
        );
      })}
      {counter && !CAPTIONS.length && <Dots filled={items[idx].n} total={total} />}   {/* có phụ đề: chừa đáy */}
    </FullShell>
  );
};

// ---------- Tổng kết 12 nghề ----------
export const Recap = ({start, jobs, subtitle, subtitleAt}) => {
  const f = useCurrentFrame();
  const n = Math.max(1, Math.round(ease(f, 4, 40) * jobs.length));
  const s = ease(f, rel(subtitleAt, start), rel(subtitleAt, start) + 12);
  return (
    <FullShell>
      <div style={{position: 'absolute', top: 240, left: SAFE.left, width: SAFE_W, textAlign: 'center'}}>
        <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 280, lineHeight: 0.9, color: C.text}}>{n}</div>
        <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 96, letterSpacing: 16, color: C.accent, marginTop: 6}}>NGHỀ</div>
      </div>
      <div style={{position: 'absolute', top: 650, left: SAFE.left, width: SAFE_W, display: 'flex', flexWrap: 'wrap', gap: 16, justifyContent: 'center'}}>
        {jobs.map((j, i) => {
          const p = pop(f, 6 + i * 3);
          return (
            <div key={j} style={{padding: '16px 26px', borderRadius: 999, border: `2px solid ${i === jobs.length - 1 ? C.accent : C.line}`,
              background: 'rgba(255,255,255,0.05)', fontFamily: BODY, fontWeight: 600, fontSize: 34, color: C.text,
              opacity: Math.min(1, p * 1.4), transform: `translateY(${(1 - p) * 40}px) scale(${0.8 + 0.2 * p})`}}>{j}</div>
          );
        })}
      </div>
      <div style={{position: 'absolute', top: 1150, left: SAFE.left, width: SAFE_W, textAlign: 'center', fontFamily: BODY, fontWeight: 600,
        fontSize: 46, lineHeight: 1.35, color: C.muted, opacity: s, transform: `translateY(${(1 - s) * 20}px)`}}>
        {subtitle}
      </div>
    </FullShell>
  );
};

// ---------- Các nghề hội tụ về một điểm chung ----------
export const Converge = ({start, jobs, mergeAt, outputs}) => {
  const f = useCurrentFrame();
  const m = ease(f, rel(mergeAt, start) - 20, rel(mergeAt, start) + 4);
  const cx = SAFE.left + SAFE_W / 2, cy = 640, RX = 210, RY = 280;
  const core = pop(f, rel(mergeAt, start) - 4);
  return (
    <FullShell>
      <div style={{position: 'absolute', top: 240, left: SAFE.left, width: SAFE_W, textAlign: 'center'}}>
        <Eyebrow style={{opacity: ease(f, 2, 12)}}>TẤT CẢ NHỮNG NGHỀ ĐÃ LÀM</Eyebrow>
      </div>
      {jobs.map((j, i) => {
        // 2 cột x 6 hàng, so le nhẹ cho tự nhiên
        const col = i % 2, row = Math.floor(i / 2);
        const p = pop(f, 2 + i * 2);
        const x = interpolate(m, [0, 1], [cx + (col ? 1 : -1) * (RX - (row % 2) * 30), cx]);
        const y = interpolate(m, [0, 1], [cy - RY + row * (RY * 2 / 5), cy]);
        return (
          <div key={j} style={{position: 'absolute', left: x, top: y, transform: `translate(-50%, -50%) scale(${(0.6 + 0.4 * p) * (1 - 0.7 * m)})`,
            opacity: Math.min(1, p * 1.4) * (1 - m), padding: '12px 22px', borderRadius: 999, whiteSpace: 'nowrap',
            border: `2px solid ${C.line}`, background: 'rgba(255,255,255,0.06)', fontFamily: BODY, fontWeight: 600, fontSize: 34, color: C.text}}>
            {j}
          </div>
        );
      })}
      <div style={{position: 'absolute', left: cx, top: cy, width: 340, height: 340, borderRadius: 170,
        transform: `translate(-50%, -50%) scale(${core})`, background: C.accent,
        boxShadow: '0 0 80px rgba(255,122,69,0.6)', display: 'flex', alignItems: 'center', justifyContent: 'center',
        textAlign: 'center'}}>
        <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 80, lineHeight: 0.95, color: C.bg}}>ĐIỂM<br />CHUNG</div>
      </div>
      <div style={{position: 'absolute', top: 1010, left: SAFE.left, width: SAFE_W}}>
        {outputs.map((o, i) => {
          const a = rel(o.at, start);
          const p = pop(f, a);
          const last = i === outputs.length - 1;
          return (
            <div key={o.label} style={{display: 'flex', alignItems: 'center', gap: 22, padding: '16px 0',
              borderTop: `2px solid ${C.line}`, opacity: Math.min(1, p * 1.4), transform: `translateX(${(1 - p) * -60}px)`}}>
              <svg width="46" height="46" viewBox="0 0 24 24" fill="none" stroke={C.accent} strokeWidth="2.6" strokeLinecap="round" strokeLinejoin="round">
                <path d="M5 12h14M13 6l6 6-6 6" /></svg>
              <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: last ? 76 : 88, lineHeight: 1,
                color: last ? C.accent : C.text}}>{o.label}</div>
            </div>
          );
        })}
      </div>
    </FullShell>
  );
};

// ---------- Siêu cao thủ một nghề vs biết mỗi thứ một chút (thời đại AI) ----------
export const Master = ({start, masterAt, shallowAt, aiAt, replaceAt}) => {
  const f = useCurrentFrame();
  const a = rel(masterAt, start), b = rel(shallowAt, start), c = rel(aiAt, start), d = rel(replaceAt, start);
  const tall = pop(f, a + 4, {damping: 22, stiffness: 90, mass: 1});
  const ai = pop(f, c);
  const gray = ease(f, c + 4, c + 16);
  const strike = ease(f, d, d + 12);
  const base = 1180;
  const small = [130, 95, 145, 110, 80, 135, 100, 120];
  return (
    <FullShell>
      <div style={{position: 'absolute', top: 240, left: SAFE.left, width: SAFE_W}}>
        <Eyebrow style={{opacity: ease(f, a, a + 10)}}>THÀ LÀM</Eyebrow>
        <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 104, lineHeight: 1, color: C.text, marginTop: 10,
          opacity: ease(f, a + 2, a + 14)}}>MASTER MỘT NGHỀ</div>
      </div>
      {/* cột cao thủ */}
      <div style={{position: 'absolute', left: 90, bottom: 1920 - base, width: 200, height: 680 * tall, borderRadius: '28px 28px 0 0',
        background: `linear-gradient(${C.accent}, #C2410C)`, boxShadow: `0 0 ${40 + 30 * strike}px rgba(255,122,69,${0.35 + 0.3 * strike})`}} />
      <div style={{position: 'absolute', left: 90, top: base + 24, width: 260, fontFamily: BODY, fontWeight: 700, fontSize: 36,
        color: C.text, opacity: tall}}>Siêu cao thủ<br /><span style={{color: C.accent}}>1 nghề</span></div>
      {/* nhiều cột thấp */}
      {small.map((h, i) => {
        const p = pop(f, b + i * 2);
        return <div key={i} style={{position: 'absolute', left: 380 + i * 60, bottom: 1920 - base, width: 40, height: h * p,
          borderRadius: '12px 12px 0 0', background: interpolate(gray, [0, 1], [0, 1]) > 0.5 ? C.dim : '#E4E4E7',
          opacity: 1 - 0.4 * strike}} />;
      })}
      <div style={{position: 'absolute', left: 380, top: base + 24, width: 480, fontFamily: BODY, fontWeight: 700, fontSize: 36,
        color: C.muted, opacity: ease(f, b, b + 10)}}>Biết mỗi thứ<br />một chút</div>
      <div style={{position: 'absolute', left: 370, top: base - 180, width: 500, height: 8, background: C.accent, borderRadius: 4,
        transformOrigin: 'left center', transform: `rotate(-14deg) scaleX(${strike})`}} />
      {/* AI */}
      <div style={{position: 'absolute', left: 560, top: 600, width: 180, height: 180, borderRadius: 36, border: `4px solid ${C.accent}`,
        background: C.bg, display: 'flex', alignItems: 'center', justifyContent: 'center',
        opacity: Math.min(1, ai * 1.3), transform: `translateY(${(1 - ai) * -120}px) scale(${0.7 + 0.3 * ai})`,
        boxShadow: '0 0 60px rgba(255,122,69,0.4)'}}>
        <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 104, color: C.accent}}>AI</div>
      </div>
      <div style={{position: 'absolute', left: SAFE.left, width: SAFE_W, top: 1316, textAlign: 'center', fontFamily: HEAD, fontWeight: 800,
        fontSize: 84, color: C.accent, opacity: strike, transform: `translateY(${(1 - strike) * 30}px)`}}>
        DỄ BỊ THAY THẾ
      </div>
    </FullShell>
  );
};

// ---------- Các thế hệ chồng lên nhau như tầng nhà + số năm ----------
// layers[{label, at}] (dưới lên trên), years: '50–60', yearsAt, eyebrow
export const Gens = ({start, eyebrow, layers, years, yearsAt, unit = 'NĂM'}) => {
  const f = useCurrentFrame();
  const y = pop(f, rel(yearsAt, start));
  const W0 = 620, H0 = 150, base = 1000;
  return (
    <FullShell>
      <div style={{position: 'absolute', top: 240, left: SAFE.left, width: SAFE_W}}>
        <Eyebrow style={{opacity: ease(f, 2, 12)}}>{eyebrow}</Eyebrow>
      </div>
      {layers.map((l, i) => {
        const p = pop(f, rel(l.at, start), {damping: 18, stiffness: 150, mass: 0.8});
        const w = W0 - i * 80;
        const last = i === layers.length - 1;
        return (
          <div key={i} style={{position: 'absolute', left: SAFE.left + (SAFE_W - w) / 2, top: base - (i + 1) * (H0 + 16), width: w, height: H0,
            borderRadius: 22, background: last ? C.accent : 'rgba(255,255,255,0.07)', border: `2px solid ${last ? C.accent : C.line}`,
            display: 'flex', alignItems: 'center', justifyContent: 'center', opacity: Math.min(1, p * 1.4),
            transform: `translateY(${(1 - p) * -160}px)`}}>
            <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 76, letterSpacing: 2, color: last ? C.bg : C.text}}>{l.label}</div>
          </div>
        );
      })}
      <div style={{position: 'absolute', top: base, left: SAFE.left, width: SAFE_W, height: 10, borderRadius: 5, background: C.dim}} />
      <div style={{position: 'absolute', top: base + 40, left: SAFE.left, width: SAFE_W, textAlign: 'center',
        opacity: Math.min(1, y * 1.4), transform: `scale(${0.8 + 0.2 * y})`}}>
        <span style={{fontFamily: HEAD, fontWeight: 800, fontSize: 170, lineHeight: 1, color: C.text}}>{years}</span>
        <span style={{fontFamily: HEAD, fontWeight: 800, fontSize: 80, color: C.accent, marginLeft: 18}}>{unit}</span>
      </div>
    </FullShell>
  );
};

// ---------- Xây từng bước: móng → tầng một → tầng hai ----------
// steps[{n, label, at}] — bước 1 là móng (rộng, thấp), các bước sau là tầng chồng lên
export const Build = ({start, eyebrow, steps}) => {
  const f = useCurrentFrame();
  let idx = 0;
  steps.forEach((s, i) => { if (f >= rel(s.at, start)) idx = i; });
  const cur = steps[idx];
  const cp = pop(f, rel(cur.at, start));
  const base = 1010, cx = SAFE.left + SAFE_W / 2;
  return (
    <FullShell>
      <div style={{position: 'absolute', top: 240, left: SAFE.left, width: SAFE_W}}>
        <Eyebrow style={{opacity: ease(f, 2, 12)}}>{eyebrow}</Eyebrow>
        <div key={idx} style={{marginTop: 12, opacity: Math.min(1, cp * 1.4), transform: `translateY(${(1 - cp) * 30}px)`}}>
          <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 96, lineHeight: VN.lh, color: C.accent}}>BƯỚC {cur.n}</div>
          <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 104, lineHeight: VN.lh + VN.gap, color: C.text, textTransform: 'uppercase',
            marginTop: aboveGap(104) - 104 * (VN.lh - 1)}}>{cur.label}</div>
        </div>
      </div>
      {steps.map((s, i) => {
        const p = pop(f, rel(s.at, start), {damping: 18, stiffness: 140, mass: 0.8});
        const isBase = i === 0;
        const w = isBase ? 700 : 520, h = isBase ? 90 : 170;
        const top = isBase ? base - h : base - 90 - i * (170 + 12);
        const active = i === idx;
        return (
          <div key={i} style={{position: 'absolute', left: cx - w / 2, top, width: w, height: h, borderRadius: isBase ? 12 : 18,
            background: active ? C.accent : isBase ? '#3F3F46' : 'rgba(255,255,255,0.08)',
            border: `2px solid ${active ? C.accent : C.line}`, opacity: Math.min(1, p * 1.4),
            transform: `translateY(${(1 - p) * -140}px)`, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 20}}>
            {!isBase && [0, 1, 2].map((k) => <div key={k} style={{width: 90, height: 80, borderRadius: 10,
              background: active ? 'rgba(13,13,16,0.25)' : 'rgba(255,255,255,0.08)'}} />)}
            {isBase && <div style={{fontFamily: BODY, fontWeight: 700, fontSize: 32, letterSpacing: 4, color: active ? C.bg : C.muted}}>MÓNG</div>}
          </div>
        );
      })}
      <div style={{position: 'absolute', top: base, left: SAFE.left, width: SAFE_W, height: 10, borderRadius: 5, background: C.dim}} />
    </FullShell>
  );
};
