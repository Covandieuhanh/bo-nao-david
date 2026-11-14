// Lớp phủ nền trong suốt: tên người nói, chữ to, thẻ thông tin.
// Tất cả nằm gọn trong vùng an toàn: x 70–900, y 985–1420 (dưới mặt, trên phần tiêu đề của nền tảng).
import React, {createContext, useContext} from 'react';
import {AbsoluteFill, Easing, Img, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {BODY, C, HEAD, SAFE, SAFE_W, ease, inOut, pop, rel} from '../chu-de';
import {VN, aboveGap} from '../khung-podcast';
import BRAND from '../lib/brand.json';
import {DauGoc} from '../lib/dau-goc';
import {Pictogram} from '../lib/bieu-tuong';

const Arrow = ({size = 30, color = C.accent}) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="2.4"
    strokeLinecap="round" strokeLinejoin="round"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
);

export const Eyebrow = ({children, style}) => (
  <div style={{fontFamily: BODY, fontWeight: 700, fontSize: 26, letterSpacing: 4, color: C.accent, ...style}}>
    {children}
  </div>
);

// Nền tối sau chữ do Place (bo-cuc.js) vẽ toàn khung — lớp phủ bị thu nhỏ nên nền vẽ ở đây sẽ thành một ô lộ mép;
// khung ngang pillar thì nền hai bên đã tối sẵn. Giữ chỗ gọi <Scrim /> để component mới viết theo cùng mẫu.
const Scrim = () => null;

// ---------- DẤU KÊNH (người dùng chốt 2026-11-04): ● DAVID │ chủ đề — CÙNG kiểu ở cả 4 loại video (Hud của chế độ ghép) ----------
// brand.json = một nguồn tên kênh. Video 1 người: phu-de.jsx đặt ở góc trên vùng an toàn; podcast: đầu sân khấu (san-khau.jsx).
export const BrandMark = ({topic, style}) => <DauGoc topic={topic} style={style} />;   // một bản: thu-vien-tai-nguyen/dau-goc.jsx

// ---------- Tên người nói ----------
export const LowerThird = ({name, role}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d} = useVideoConfig();
  const o = inOut(f, d, 12, 10);
  const bar = ease(f, 4, 22);
  return (
    <AbsoluteFill style={{opacity: o}}>
      <Scrim />
      <div style={{position: 'absolute', left: SAFE.left, top: 1150}}>
        <div style={{width: 420 * bar, height: 6, background: C.accent, borderRadius: 3}} />
        <div style={{overflow: 'hidden', marginTop: aboveGap(130) - 130 * VN.top, paddingTop: 130 * VN.top, paddingBottom: 130 * VN.bot, marginBottom: -130 * VN.bot}}>
          <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 130, lineHeight: VN.lh, color: C.text,
            letterSpacing: 4, transform: `translateY(${(1 - pop(f, 6)) * 110}%)`}}>{name}</div>
        </div>
        <div style={{fontFamily: BODY, fontWeight: 500, fontSize: 40, color: C.muted, marginTop: 8,
          opacity: ease(f, 16, 28), transform: `translateX(${(1 - ease(f, 16, 30)) * -30}px)`}}>{role}</div>
      </div>
    </AbsoluteFill>
  );
};

// ---------- Chữ to nhấn mạnh (kinetic typography) ----------
export const Kinetic = ({lines}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d} = useVideoConfig();
  const o = inOut(f, d, 6, 10);
  const words = lines.map((l) => l.split(' '));
  let k = 0;
  const lineDone = 6 + words.flat().length * 3;
  // Cỡ lớn nhất để dòng dài nhất không xuống hàng (chữ cô đặc in hoa có dấu ≈ 0,46 em/ký tự)
  const size = Math.min(120, Math.floor(SAFE_W / (Math.max(...lines.map((l) => l.length)) * 0.46)));
  return (
    <AbsoluteFill style={{opacity: o}}>
      <Scrim />
      <div style={{position: 'absolute', left: SAFE.left, width: SAFE_W, top: 1040}}>
        {words.map((ws, li) => (
          <div key={li} style={{display: 'flex', flexWrap: 'wrap', gap: '0 24px', marginTop: li ? size * VN.gap : 0}}>
            {ws.map((w, wi) => {
              const p = pop(f, 2 + (k++) * 3, {damping: 18, stiffness: 170, mass: 0.6});
              return (
                <div key={wi} style={{overflow: 'hidden',   // chừa chỗ cho dấu chồng/dấu nặng theo cỡ chữ (VN, khung-podcast.js)
                  paddingTop: size * VN.top, marginTop: -size * VN.top, paddingBottom: size * VN.bot, marginBottom: -size * VN.bot}}>
                  <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: size, lineHeight: VN.lh, color: C.text,
                    textShadow: '0 6px 30px rgba(0,0,0,0.45)',
                    transform: `translateY(${(1 - p) * 105}%)`}}>{w}</div>
                </div>
              );
            })}
          </div>
        ))}
        <div style={{height: 9, marginTop: 28, borderRadius: 5, background: C.accent,
          width: `${ease(f, lineDone, lineDone + 14) * 80}%`, boxShadow: '0 0 24px rgba(255,122,69,0.55)'}} />
      </div>
    </AbsoluteFill>
  );
};

// ---------- Mở đầu (hook) — 3 giây đầu: nói ngay video về cái gì ----------
// Hiện từ khung đầu tiên (không để màn hình trống lúc người xem quyết định lướt hay ở lại):
// tiêu đề đập vào (phóng 1,25 → 1), nhãn chủ đề trượt vào, dòng nhấn có nền màu quét qua.
// lines: 2 dòng in hoa, ≤ 4 từ/dòng; accentLine: dòng tô màu nhấn (mặc định dòng cuối)
export const Hook = ({eyebrow, lines, accentLine = lines.length - 1}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d} = useVideoConfig();
  const p = pop(f, 0, {damping: 14, stiffness: 190, mass: 0.6});
  const out = ease(f, d - 8, d, 0, 1, Easing.in(Easing.cubic));
  // Cỡ chữ lớn nhất mà dòng dài nhất vẫn nằm trên MỘT dòng (chữ cô đặc in hoa có dấu ≈ 0,46 em/ký tự — đổi font thì đo lại)
  const size = Math.min(118, Math.floor((SAFE_W - 30) / (Math.max(...lines.map((l) => l.length)) * 0.46)));
  const flash = interpolate(f, [0, 4], [0.15, 0], {extrapolateRight: 'clamp'});
  const line = {fontFamily: HEAD, fontWeight: 800, fontSize: size, lineHeight: 1.08, whiteSpace: 'nowrap',
    padding: `${size * 0.26}px 14px ${size * 0.24}px`};   // ô màu bọc trọn dấu chồng + dấu nặng
  return (
    <AbsoluteFill style={{opacity: 1 - out}}>
      <Scrim />
      <AbsoluteFill style={{background: '#fff', opacity: flash}} />
      <div style={{position: 'absolute', left: SAFE.left, width: SAFE_W, top: SAFE.overlayTop + 10,
        transform: `translateY(${out * 40}px)`}}>
        {/* KHUÔN TIÊU ĐỀ CHUNG (người dùng chốt 2026-11-04, cả 4 loại video — giống Title của chế độ ghép): dòng nhỏ cam → gạch cam →
            chữ cô đặc in hoa trắng, dòng nhấn màu cam */}
        {eyebrow && (
          <div style={{fontFamily: BODY, fontWeight: 700, fontSize: 30, letterSpacing: 4, color: C.accent, textShadow: '0 4px 20px rgba(0,0,0,0.5)',
            transform: `translateX(${(1 - ease(f, 0, 8)) * -60}px)`, opacity: ease(f, 0, 6)}}>{eyebrow}</div>
        )}
        <div style={{width: 420 * ease(f, 2, 16), height: 6, borderRadius: 3, background: C.accent, marginTop: 14}} />
        <div style={{marginTop: 18, transform: `scale(${1.25 - 0.25 * p})`, transformOrigin: 'left center', opacity: 0.8 + 0.2 * p, marginLeft: -14}}>
          {lines.map((l, i) => {
            const hi = i === accentLine;
            const wipe = ease(f, 5 + i * 3, 15 + i * 3);
            return (
              <div key={i} style={{position: 'relative', display: 'table', marginTop: i ? size * 0.06 : 0}}>   {/* ô màu đã có đệm cho dấu → khe nhỏ */}
                <div style={{...line, color: C.text, textShadow: '0 6px 30px rgba(0,0,0,0.5)'}}>{l}</div>
                {hi && (   // dòng nhấn: chữ cam quét dần từ trái sang (khuôn chung — không còn ô nền màu)
                  <div style={{...line, position: 'absolute', inset: 0, color: C.accent, textShadow: '0 6px 30px rgba(0,0,0,0.5)',
                    clipPath: `inset(0 ${(1 - wipe) * 100}% 0 0)`}}>{l}</div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ---------- Thẻ thông tin ----------
// Thẻ toàn cảnh (the-toan-man.jsx) bật cờ này → khung thẻ vẽ trong dòng chảy (không định vị tuyệt đối ở dải lớp phủ)
export const CardInline = createContext(false);

const CardShell = ({children}) => {
  const inline = useContext(CardInline);
  const f = useCurrentFrame();
  const {durationInFrames: d} = useVideoConfig();
  const p = pop(f, 0);
  const out = ease(f, d - 9, d, 0, 1);
  if (inline) return (
    <div style={{width: SAFE_W, boxSizing: 'border-box', background: C.card, border: `2px solid ${C.line}`, borderRadius: 36,
      padding: '32px 40px 34px', boxShadow: '0 30px 80px rgba(0,0,0,0.45)', opacity: Math.min(1, p * 1.4),
      transform: `translateY(${(1 - p) * 50}px) scale(${0.94 + 0.06 * p})`}}>{children}</div>
  );
  return (
    <AbsoluteFill>
      <div style={{position: 'absolute', left: SAFE.left, width: SAFE_W, top: SAFE.overlayTop, boxSizing: 'border-box',
        maxHeight: SAFE.bottom - SAFE.overlayTop, overflow: 'hidden',
        background: C.card, border: `2px solid ${C.line}`, borderRadius: 36, padding: '32px 40px 34px',
        boxShadow: '0 30px 80px rgba(0,0,0,0.45)',
        opacity: Math.min(1, p * 1.4) * (1 - out),
        transform: `translateY(${(1 - p) * 50 + out * 24}px) scale(${0.94 + 0.06 * p})`, transformOrigin: 'left top'}}>
        {children}
      </div>
    </AbsoluteFill>
  );
};

const Footer = ({text, at, style}) => {
  const f = useCurrentFrame();
  if (useContext(CardInline) === 'min') return null;   // thẻ toàn cảnh có quote: chỉ giữ hình động + nhãn
  const o = ease(f, at, at + 10);
  return (
    <div style={{display: 'flex', alignItems: 'center', gap: 12, marginTop: 22, opacity: o,
      transform: `translateX(${(1 - o) * -24}px)`, ...style}}>
      <Arrow />
      <div style={{fontFamily: BODY, fontWeight: 600, fontSize: 36, color: C.accent}}>{text}</div>
    </div>
  );
};

const Title = ({children, size = 60}) => useContext(CardInline) === 'min' ? null : (
  <div style={{fontFamily: BODY, fontWeight: 700, fontSize: size, color: C.text, lineHeight: 1.15, marginTop: 8}}>
    {children}
  </div>
);

export const Card = ({start, ...p}) => {
  const f = useCurrentFrame();
  const min = useContext(CardInline) === 'min';   // thẻ toàn cảnh có quote: bỏ chữ phụ lặp lại câu nói (note, pill)
  const R = (abs) => rel(abs, start);
  const V = {
    year: () => {
      const from = Math.round(interpolate(f, [R(p.toAt), R(p.toAt) + 30], [p.to, p.from], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}));
      const span = ease(f, R(p.fromAt), R(p.fromAt) + 14);
      return (<>
        <Eyebrow>{p.eyebrow}</Eyebrow>
        <div style={{display: 'flex', alignItems: 'baseline', gap: 24}}>
          <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 160, lineHeight: 1, color: C.text}}>{from}</div>
          <div style={{fontFamily: BODY, fontWeight: 600, fontSize: 40, color: C.muted, opacity: span}}>→ {p.to}</div>
        </div>
        <div style={{position: 'relative', height: 12, background: C.line, borderRadius: 6, marginTop: 14}}>
          <div style={{position: 'absolute', inset: 0, width: `${span * 100}%`, background: C.accent, borderRadius: 6}} />
        </div>
        <div style={{display: 'flex', justifyContent: 'space-between', fontFamily: BODY, fontSize: 28,
          color: C.muted, marginTop: 10, opacity: span}}>
          <span>{p.from}</span><span style={{color: C.text, fontWeight: 700}}>{p.to - p.from} năm đi làm</span><span>{p.to}</span>
        </div>
        <Footer text={p.footer} at={R(p.footerAt)} />
      </>);
    },
    job: () => (
      <div style={{display: 'flex', gap: 32, alignItems: 'center'}}>
        <div style={{width: 300, height: 300, borderRadius: 24, overflow: 'hidden', flexShrink: 0}}>
          {p.icon ? <Pictogram name={p.icon} w={300} h={300} at={4} />   // không ảnh: biểu tượng vẽ dần
            : <Img src={staticFile(`photos/${p.photo}`)} style={{width: '100%', height: '100%', objectFit: 'cover',
            transform: `scale(${1.12 - ease(f, 0, 120) * 0.08})`}} />}
        </div>
        <div>
          <Eyebrow>{p.eyebrow}</Eyebrow>
          <Title size={56}>{p.title}</Title>
          <Footer text={p.footer} at={R(p.footerAt)} style={{alignItems: 'flex-start'}} />
        </div>
      </div>
    ),
    marketing: () => {
      const pts = [[0, 150], [100, 130], [200, 140], [300, 95], [400, 105], [500, 60], [600, 66], [730, 16]];
      const len = 1000;
      const draw = ease(f, 10, 50);
      const path = pts.map(([x, y], i) => `${i ? 'L' : 'M'}${x} ${y}`).join(' ');
      return (<>
        <Eyebrow>{p.eyebrow}</Eyebrow>
        <Title size={60}>{p.title}</Title>
        <svg width="740" height="170" viewBox="-10 0 750 170" style={{marginTop: 16, overflow: 'visible'}}>
          {[40, 90, 140].map((y) => <line key={y} x1="0" x2="740" y1={y} y2={y} stroke={C.line} strokeWidth="2" />)}
          {pts.map(([x], i) => {
            const h = (26 + i * 15) * pop(f, 8 + i * 3);
            return <rect key={i} x={x - 16} y={165 - h} width="32" height={h} rx="7" fill={C.accentSoft} />;
          })}
          <path d={path} fill="none" stroke={C.accent} strokeWidth="7" strokeLinejoin="round" strokeLinecap="round"
            strokeDasharray={len} strokeDashoffset={len * (1 - draw)} style={{filter: 'drop-shadow(0 0 10px rgba(255,122,69,.6))'}} />
          <circle cx="730" cy="16" r={11 * ease(f, 48, 56)} fill={C.accent} />
        </svg>
        <Footer text={p.footer} at={R(p.footerAt)} />
      </>);
    },
    years4: () => (<>
      <Eyebrow>{p.eyebrow}</Eyebrow>
      <div style={{display: 'flex', alignItems: 'baseline', gap: 20}}>
        <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 190, lineHeight: 1, color: C.text}}>
          {Math.max(1, Math.round(ease(f, 4, 34) * p.value))}
        </div>
        <div style={{fontFamily: HEAD, fontWeight: 700, fontSize: 90, color: C.accent}}>{p.unit}</div>
      </div>
      <div style={{display: 'flex', gap: 12, marginTop: 10}}>
        {[0, 1, 2, 3].map((i) => (
          <div key={i} style={{flex: 1, height: 14, borderRadius: 7, background: C.line, overflow: 'hidden'}}>
            <div style={{height: '100%', width: `${ease(f, 4 + i * 8, 12 + i * 8) * 100}%`, background: C.accent}} />
          </div>
        ))}
      </div>
      <Footer text={p.footer} at={R(p.footerAt)} />
    </>),
    daily: () => {
      const r = 88, c = 2 * Math.PI * r;
      const fill = ease(f, 6, 70);
      const pill = pop(f, R(p.pillAt));
      return (<>
        <div style={{display: 'flex', alignItems: 'center', gap: 36}}>
          <svg width="220" height="220" viewBox="0 0 220 220" style={{flexShrink: 0}}>
            <circle cx="110" cy="110" r={r} stroke={C.line} strokeWidth="18" fill="none" />
            <circle cx="110" cy="110" r={r} stroke={C.accent} strokeWidth="18" fill="none" strokeLinecap="round"
              strokeDasharray={c} strokeDashoffset={c * (1 - 0.22 * fill)} transform="rotate(-90 110 110)" />
            <circle cx="110" cy="110" r="8" fill={C.text} />
            <line x1="110" y1="110" x2="110" y2="66" stroke={C.text} strokeWidth="9" strokeLinecap="round" />
            <line x1="110" y1="110" x2="110" y2="50" stroke={C.accent} strokeWidth="5" strokeLinecap="round"
              transform={`rotate(${fill * 79} 110 110)`} />
          </svg>
          <div>
            <Eyebrow>{p.eyebrow}</Eyebrow>
            <Title size={56}>{p.title}</Title>
          </div>
        </div>
        {!min && <div style={{display: 'inline-flex', alignItems: 'center', gap: 14, marginTop: 24, padding: '14px 26px',
          borderRadius: 999, background: C.accentSoft, border: `2px solid ${C.accent}`,
          opacity: Math.min(1, pill * 1.3), transform: `scale(${0.85 + 0.15 * pill})`, transformOrigin: 'left center'}}>
          {p.icon !== false && (   // chuông tắt ("không ai làm phiền"); icon: false để bỏ
            <svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke={C.accent} strokeWidth="2.2" strokeLinecap="round">
              <path d="M18 8a6 6 0 0 0-9.33-5M6.26 6.26A6 6 0 0 0 6 8c0 7-3 9-3 9h14M13.73 21a2 2 0 0 1-3.46 0M3 3l18 18" />
            </svg>
          )}
          <div style={{fontFamily: BODY, fontWeight: 700, fontSize: 32, letterSpacing: 3, color: C.accent}}>{p.pill}</div>
        </div>}
      </>);
    },
    steps: () => (<>
      <Eyebrow>{p.eyebrow}</Eyebrow>
      <div style={{marginTop: 8}}>
        {p.steps.map((s, i) => {
          const a = R(s.at);
          const o = ease(f, a, a + 10);
          const check = ease(f, a + 6, a + 16);
          return (
            <div key={i} style={{display: 'flex', alignItems: 'center', gap: 26, padding: '16px 0',
              borderBottom: i < p.steps.length - 1 ? `2px solid ${C.line}` : 'none',
              opacity: 0.25 + 0.75 * o, transform: `translateX(${(1 - o) * -20}px)`}}>
              <div style={{width: 68, height: 68, borderRadius: 34, flexShrink: 0, display: 'flex', alignItems: 'center',
                justifyContent: 'center', background: check > 0.5 ? C.accent : 'transparent', border: `3px solid ${o > 0.5 ? C.accent : C.dim}`,
                fontFamily: HEAD, fontWeight: 800, fontSize: String(s.n ?? i + 1).length > 1 ? 32 : 42, color: check > 0.5 ? C.bg : C.muted}}>{s.n ?? i + 1}</div>
              <div style={{fontFamily: BODY, fontWeight: 600, fontSize: 42, color: C.text}}>{s.text}</div>
            </div>
          );
        })}
      </div>
    </>),
    // Hai dòng so sánh trước/sau: rows[{tag, title, note, at, hi}]
    vs: () => (<>
      <Eyebrow>{p.eyebrow}</Eyebrow>
      <div style={{marginTop: 10}}>
        {p.rows.map((r, i) => {
          const a = R(r.at);
          const o = ease(f, a, a + 10);
          return (
            <div key={i} style={{display: 'flex', alignItems: 'center', gap: 24, padding: '16px 0',
              borderBottom: i < p.rows.length - 1 ? `2px solid ${C.line}` : 'none',
              opacity: 0.2 + 0.8 * o, transform: `translateX(${(1 - o) * -24}px)`}}>
              <div style={{width: 190, flexShrink: 0, fontFamily: BODY, fontWeight: 700, fontSize: 28, letterSpacing: 2,
                color: r.hi ? C.accent : C.muted}}>{r.tag}</div>
              <div>
                <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 72, lineHeight: 1, color: C.text}}>{r.title}</div>
                {!min && <div style={{fontFamily: BODY, fontWeight: 600, fontSize: 36, marginTop: 6, color: r.hi ? C.accent : C.muted}}>{r.note}</div>}
              </div>
            </div>
          );
        })}
      </div>
    </>),
    // Các mốc tuổi bật lần lượt + nhãn gạch: ages[{v, at}], unit, pill, pillAt
    ages: () => {
      const pill = pop(f, R(p.pillAt));
      return (<>
        <Eyebrow>{p.eyebrow}</Eyebrow>
        <div style={{display: 'flex', alignItems: 'baseline', gap: 30, marginTop: 6}}>
          {p.ages.map((a, i) => {
            const q = pop(f, R(a.at));
            return <div key={i} style={{fontFamily: HEAD, fontWeight: 800, fontSize: 150, lineHeight: 1,
              color: i === p.ages.length - 1 ? C.accent : C.text, opacity: Math.min(1, q * 1.4),
              transform: `translateY(${(1 - q) * 40}px)`}}>{a.v}</div>;
          })}
          <div style={{fontFamily: HEAD, fontWeight: 700, fontSize: 64, color: C.muted, opacity: ease(f, R(p.ages[0].at), R(p.ages[0].at) + 10)}}>{p.unit}</div>
        </div>
        {!min && <div style={{display: 'inline-flex', alignItems: 'center', gap: 14, marginTop: 22, padding: '14px 26px',
          borderRadius: 999, background: C.accentSoft, border: `2px solid ${C.accent}`,
          opacity: Math.min(1, pill * 1.3), transform: `scale(${0.85 + 0.15 * pill})`, transformOrigin: 'left center'}}>
          <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke={C.accent} strokeWidth="2.8" strokeLinecap="round"><path d="M6 6l12 12M18 6L6 18" /></svg>
          <div style={{fontFamily: BODY, fontWeight: 700, fontSize: 34, letterSpacing: 2, color: C.accent}}>{p.pill}</div>
        </div>}
      </>);
    },
    // Trích một câu: eyebrow, title, footer
    quote: () => (<>
      <Eyebrow>{p.eyebrow}</Eyebrow>
      <Title size={58}>{p.title}</Title>
      <Footer text={p.footer} at={R(p.footerAt)} />
    </>),
    early: () => {
      const a = ease(f, 6, 40), b = ease(f, R(p.secondAt), R(p.secondAt) + 30);
      return (<>
        <Eyebrow>{p.eyebrow}</Eyebrow>
        <Title size={54}>{p.title}</Title>
        <svg width="740" height="200" viewBox="0 0 740 200" style={{marginTop: 16}}>
          <line x1="0" x2="740" y1="192" y2="192" stroke={C.line} strokeWidth="3" />
          <path d="M0 192 C 230 186, 410 120, 730 14" fill="none" stroke={C.accent} strokeWidth="8" strokeLinecap="round"
            strokeDasharray="900" strokeDashoffset={900 * (1 - a)} />
          <path d="M380 192 C 510 188, 620 165, 730 125" fill="none" stroke={C.dim} strokeWidth="6" strokeLinecap="round"
            strokeDasharray="450" strokeDashoffset={450 * (1 - b)} />
          <text x="0" y="160" fill={C.accent} opacity={a} style={{fontFamily: BODY, fontWeight: 700, fontSize: 30}}>Tìm sớm</text>
          <text x="470" y="160" fill={C.muted} opacity={b} style={{fontFamily: BODY, fontWeight: 600, fontSize: 30}}>Tìm muộn</text>
        </svg>
      </>);
    },
  };
  return <CardShell>{V[p.variant]()}</CardShell>;
};

// ---------- NHÃN SỐ DANH SÁCH (David duyệt 2026-11-04, học BS Tùng / Huỳnh Duy Khương: mỗi ý một nhãn đúng lúc nói) ----------
// {type: 'listItem', start, end, props: {n: 3, of: 10, text: 'Tránh xa thức ăn nhanh'}} — text NGUYÊN VĂN cụm việc (bỏ bớt chữ),
// 2,5–4 s mỗi ý; vẽ trong dải lớp phủ (Place lo vị trí, không che mặt). `of` tuỳ chọn (hiện "3/10" nhỏ để người xem chờ tới cuối).
export const ListItem = ({n, of, text}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d} = useVideoConfig();
  const o = inOut(f, d, 5, 8);
  const p = pop(f, 0, {damping: 14, stiffness: 190, mass: 0.6});
  const size = Math.min(92, Math.floor((SAFE_W - 200) / (Math.max(8, text.length) * 0.46)));
  return (
    <AbsoluteFill style={{opacity: o}}>
      <div style={{position: 'absolute', left: SAFE.left, width: SAFE_W, top: 1110, display: 'flex', alignItems: 'center', gap: 26}}>
        <div style={{flex: '0 0 auto', width: 150, height: 150, borderRadius: 75, background: C.accent, display: 'flex', alignItems: 'center',
          justifyContent: 'center', transform: `scale(${p})`, boxShadow: '0 0 40px rgba(255,122,69,0.5)'}}>
          <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 104, lineHeight: 1, color: C.bg, paddingTop: 8}}>{n}</div>
        </div>
        <div style={{display: 'flex', flexDirection: 'column', gap: 6, transform: `translateX(${(1 - ease(f, 2, 12)) * 30}px)`}}>
          {of && <div style={{fontFamily: BODY, fontWeight: 700, fontSize: 34, color: C.accent}}>{n}/{of}</div>}
          <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: size, lineHeight: VN.lh, color: C.text, textTransform: 'uppercase',
            textShadow: '0 6px 30px rgba(0,0,0,0.55)', paddingTop: size * VN.top * 0.5}}>{text}</div>
        </div>
      </div>
    </AbsoluteFill>
  );
};
