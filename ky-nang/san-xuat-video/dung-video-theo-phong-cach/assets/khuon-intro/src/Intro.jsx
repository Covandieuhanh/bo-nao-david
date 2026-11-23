// Intro DAVID TRẦN — khoảng 12 giây, dựng theo nhịp nhạc intro-soi (113 BPM: nhịp 0,530 s, pha 0,015 s).
// Ba hồi: (1) cắt nhanh theo nhịp · (2) khung ba ô chạy chéo nối bằng đường cam = kết nối · (3) chốt tên.
// Chỉ xuất khung ngang 1920×1080 (David 23/11: bỏ bản dọc). Code vẫn tính theo W, H nên thêm khung khác không phải viết lại.
import React, { useEffect, useState } from 'react';
import {
  AbsoluteFill, Audio, OffthreadVideo, Sequence, continueRender, delayRender, interpolate, spring,
  staticFile, useCurrentFrame, useVideoConfig, Easing,
} from 'remotion';
import '@fontsource/barlow-condensed/800.css';
import '@fontsource/be-vietnam-pro/700.css';

const C = { bg: '#0D0D10', nen: '#141418', text: '#F4F4F5', accent: '#FF7A45' };
const HEAD = '"Barlow Condensed", sans-serif';

const NHIP = 0.53 * 30;
const PHA = 0.015 * 30;
const f = (n) => Math.round(PHA + n * NHIP); // khung hình của phách thứ n
export const TONG = 360; // 12 giây

// Hồi 1: [đoạn, phách bắt đầu, phách kết thúc, chỗ mặt người theo chiều ngang %]
const HOI1 = [ // [đoạn, phách đầu, phách cuối, chỗ mặt % khung ngang, chỗ mặt % khung dọc]
  ['a1', 0, 1, 30, 26], ['a2', 1, 2, 42, 42], ['a3', 2, 3, 68, 82], ['a4', 3, 3.5, 78, 94], ['a5', 3.5, 4, 55, 65],
  ['a6', 4, 5, 42, 38], ['a7', 5, 5.5, 62, 71], ['a8', 5.5, 6, 72, 94], ['a9', 6, 7, 68, 82], ['a10', 7, 8, 45, 65],
];
// Hồi 2: hai bộ ba ô
const BO = [
  { tu: 8, den: 12.5, o: [['b1', 86], ['b2', 60], ['b3', 64]] },
  { tu: 12.5, den: 17, o: [['b4', 35], ['b5', 45], ['b6', 42]] },
];
const HOI3 = 17;

const Phim = ({ src, fx, batDau = 9, scale = 1, rot = 0, style }) => (
  <OffthreadVideo
    src={staticFile(`canh/${src}.mp4`)} startFrom={batDau} muted
    style={{
      position: 'absolute', inset: 0, width: '100%', height: '100%', objectFit: 'cover',
      objectPosition: `${fx}% 45%`, transform: `scale(${scale}) rotate(${rot}deg)`, ...style,
    }}
  />
);

// ---------- Hồi 1: cắt nhanh, mỗi cảnh đập vào bằng zoom + chớp sáng + vệt cam ----------
const Canh1 = ({ src, fx, dai, i }) => {
  const t = useCurrentFrame();
  const { width: W } = useVideoConfig();
  const s = interpolate(t, [0, dai], [1.24, 1.06], { extrapolateRight: 'clamp', easing: Easing.out(Easing.cubic) });
  const r = interpolate(t, [0, 6], [i % 2 ? 2.5 : -2.5, 0], { extrapolateRight: 'clamp', easing: Easing.out(Easing.cubic) });
  const chop = interpolate(t, [0, 4], [0.6, 0], { extrapolateRight: 'clamp' });
  const vet = interpolate(t, [0, 7], [-0.6, 1.4], { extrapolateRight: 'clamp', easing: Easing.inOut(Easing.quad) });
  return (
    <AbsoluteFill style={{ overflow: 'hidden', background: C.bg }}>
      <Phim src={src} fx={fx} scale={s} rot={r} />
      {i % 2 === 1 && (
        <div style={{
          position: 'absolute', top: '-20%', bottom: '-20%', width: W * 0.22, left: vet * W,
          background: C.accent, transform: 'skewX(-18deg)', opacity: 0.9,
        }} />
      )}
      <AbsoluteFill style={{ background: '#fff', opacity: chop }} />
    </AbsoluteFill>
  );
};

// ---------- Hồi 2: ba ô chéo, đường cam nối các ô ----------
const BoBa = ({ o, dai, ngang }) => {
  const t = useCurrentFrame();
  const { fps, width: W, height: H } = useVideoConfig();
  const tre = Math.round(NHIP / 2);
  const pw = ngang ? 520 : 860, ph = ngang ? 690 : 450;
  const tam = o.map((_, k) => (ngang ? { x: W / 2 + (k - 1) * 600, y: H / 2 - 30 } : { x: W / 2 + 30, y: H / 2 + (k - 1) * 520 - 40 }));
  const ra = interpolate(t, [dai - 5, dai], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.in(Easing.cubic) });
  // đường nối: ngang chạy dưới các ô, dọc chạy bên trái các ô
  const d0 = ngang ? { x: tam[0].x - pw / 2 - 40, y: tam[0].y + ph / 2 + 70 } : { x: 70, y: tam[0].y - ph / 2 - 30 };
  const d1 = ngang ? { x: tam[2].x + pw / 2 + 40, y: d0.y } : { x: 70, y: tam[2].y + ph / 2 + 30 };
  const dai_duong = Math.hypot(d1.x - d0.x, d1.y - d0.y);
  const ve = interpolate(t, [0, tre * 3 + 6], [0, 1], { extrapolateRight: 'clamp', easing: Easing.out(Easing.cubic) });
  return (
    <AbsoluteFill>
      <svg width={W} height={H} style={{ position: 'absolute', inset: 0 }}>
        <line x1={d0.x} y1={d0.y} x2={d1.x} y2={d1.y} stroke={C.accent} strokeWidth={8} strokeLinecap="round"
          strokeDasharray={dai_duong} strokeDashoffset={dai_duong * (1 - ve)} opacity={1 - ra} />
        {tam.map((p, k) => {
          const no = spring({ frame: t - k * tre - 6, fps, config: { damping: 9, stiffness: 180 } });
          const cx = ngang ? p.x : 70, cy = ngang ? d0.y : p.y;
          const nhay = 1 + 0.25 * Math.max(0, Math.sin(((t - k * tre) / NHIP) * Math.PI * 2));
          return (
            <g key={k} opacity={1 - ra}>
              <circle cx={cx} cy={cy} r={30 * no * nhay} fill={C.accent} opacity={0.25} />
              <circle cx={cx} cy={cy} r={15 * no} fill={C.accent} />
              <circle cx={cx} cy={cy} r={6 * no} fill="#fff" />
            </g>
          );
        })}
      </svg>
      {o.map(([src, fx], k) => {
        const vao = spring({ frame: t - k * tre, fps, config: { damping: 14, stiffness: 160 } });
        const lech = ngang ? { x: 0, y: (1 - vao) * (k % 2 ? -260 : 260) } : { x: (1 - vao) * (k % 2 ? -400 : 400), y: 0 };
        const thoat = ngang ? { x: 0, y: -ra * H } : { x: ra * W * (k % 2 ? -1 : 1), y: 0 };
        const zoom = interpolate(t, [k * tre, dai], [1.18, 1.04], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
        const chop = interpolate(t - k * tre, [0, 5], [0.7, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
        return (
          <div key={src} style={{
            position: 'absolute', left: tam[k].x - pw / 2, top: tam[k].y - ph / 2, width: pw, height: ph,
            transform: `translate(${lech.x + thoat.x}px, ${lech.y + thoat.y}px) skewX(-6deg)`,
            opacity: Math.min(1, vao * 1.5), borderRadius: 22, overflow: 'hidden',
            border: `5px solid ${k === 1 ? C.accent : C.text}`, boxShadow: '0 30px 80px rgba(0,0,0,0.55)', background: C.nen,
          }}>
            <div style={{ position: 'absolute', inset: -40, transform: 'skewX(6deg)' }}>
              <Phim src={src} fx={fx} batDau={6} scale={zoom} />
            </div>
            <div style={{ position: 'absolute', inset: 0, background: '#fff', opacity: chop }} />
          </div>
        );
      })}
    </AbsoluteFill>
  );
};

const NenHoi2 = () => {
  const t = useCurrentFrame();
  const { width: W, height: H } = useVideoConfig();
  const x = 50 + 25 * Math.sin(t / 22), y = 45 + 20 * Math.cos(t / 30);
  return (
    <AbsoluteFill style={{
      background: `radial-gradient(circle at ${x}% ${y}%, rgba(255,122,69,0.28), rgba(13,13,16,0) 55%), ${C.bg}`,
    }}>
      <svg width={W} height={H} style={{ position: 'absolute', inset: 0, opacity: 0.18 }}>
        {Array.from({ length: Math.ceil(W / 60) * Math.ceil(H / 60) }).map((_, k) => {
          const cot = Math.ceil(W / 60);
          return <circle key={k} cx={(k % cot) * 60 + 30} cy={Math.floor(k / cot) * 60 + 30 - (t * 1.5) % 60} r={2} fill="#fff" />;
        })}
      </svg>
    </AbsoluteFill>
  );
};

// ---------- Hồi 3: chốt tên DAVID TRẦN ----------
const Nhan = ({ chu, nen, mau, tre, tu, co }) => {
  const t = useCurrentFrame();
  const { fps } = useVideoConfig();
  const vao = spring({ frame: t - tre, fps, config: { damping: 11, stiffness: 170 } });
  return (
    <div style={{
      display: 'inline-flex', background: nen, padding: `0 ${co * 0.16}px`, borderRadius: 10, overflow: 'hidden',
      transform: `translateX(${(1 - vao) * tu}px) scale(${0.7 + 0.3 * vao})`, opacity: Math.min(1, vao * 2),
      boxShadow: '0 18px 50px rgba(0,0,0,0.35)', transformOrigin: 'left center',
    }}>
      {[...chu].map((ch, k) => {
        const len = spring({ frame: t - tre - 3 - k * 2, fps, config: { damping: 12, stiffness: 200 } });
        return (
          <span key={k} style={{
            fontFamily: HEAD, fontWeight: 800, fontSize: co, lineHeight: 1.08, color: mau, letterSpacing: co * 0.02,
            display: 'inline-block', transform: `translateY(${(1 - len) * co * 0.9}px)`,
          }}>{ch}</span>
        );
      })}
    </div>
  );
};

const Hoi3 = ({ ngang }) => {
  const t = useCurrentFrame();
  const { width: W, height: H } = useVideoConfig();
  const dai = TONG - f(HOI3);
  const s = interpolate(t, [0, dai], ngang ? [1.28, 1.08] : [1.12, 1.0], { extrapolateRight: 'clamp', easing: Easing.out(Easing.cubic) });
  const chop = interpolate(t, [0, 6], [0.85, 0], { extrapolateRight: 'clamp' });
  const co = ngang ? 190 : 150;
  return (
    <AbsoluteFill style={{ overflow: 'hidden', background: C.bg }}>
      <Phim src={ngang ? 'h1' : 'h2'} fx={ngang ? 55 : 40} batDau={6} scale={s} />
      {ngang ? (
        <div style={{ position: 'absolute', left: W * 0.05, bottom: H * 0.075, display: 'flex', gap: 18, alignItems: 'flex-end' }}>
          <Nhan chu="DAVID" nen={C.text} mau={C.nen} tre={2} tu={-500} co={co} />
          <Nhan chu="TRẦN" nen={C.accent} mau="#fff" tre={8} tu={500} co={co} />
        </div>
      ) : (
        <div style={{ position: 'absolute', left: 70, top: 1236, display: 'flex', gap: 14, alignItems: 'flex-end' }}>
          <Nhan chu="DAVID" nen={C.text} mau={C.nen} tre={2} tu={-500} co={co} />
          <Nhan chu="TRẦN" nen={C.accent} mau="#fff" tre={8} tu={500} co={co} />
        </div>
      )}
      <AbsoluteFill style={{ background: '#fff', opacity: chop }} />
    </AbsoluteFill>
  );
};

export const Intro = () => {
  const { width: W, height: H } = useVideoConfig();
  const ngang = W > H;
  const [h] = useState(() => delayRender('phông chữ'));
  useEffect(() => {
    Promise.all([
      document.fonts.load(`800 100px "Barlow Condensed"`, 'DAVID TRẦN'),
    ]).then(() => continueRender(h));
  }, [h]);
  const amNhac = (fr) => interpolate(fr, [TONG - 36, TONG - 2], [1, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  return (
    <AbsoluteFill style={{ background: C.bg }}>
      {HOI1.map(([src, a, b, fx, fxDoc], i) => (
        <Sequence key={src} from={f(a)} durationInFrames={f(b) - f(a)}>
          <Canh1 src={src} fx={ngang ? fx : fxDoc} dai={f(b) - f(a)} i={i} />
        </Sequence>
      ))}
      <Sequence from={f(8)} durationInFrames={f(HOI3) - f(8)}>
        <NenHoi2 />
      </Sequence>
      {BO.map((bo, k) => (
        <Sequence key={k} from={f(bo.tu)} durationInFrames={f(bo.den) - f(bo.tu)}>
          <BoBa o={bo.o} dai={f(bo.den) - f(bo.tu)} ngang={ngang} />
        </Sequence>
      ))}
      <Sequence from={f(HOI3)}>
        <Hoi3 ngang={ngang} />
      </Sequence>
      <Audio src={staticFile('intro-soi.mp3')} volume={amNhac} />
      {BO.map((bo, k) => (
        <Sequence key={`tua${k}`} from={Math.max(0, f(bo.tu) - 6)}>
          <Audio src={staticFile('tua.wav')} volume={0.45} />
        </Sequence>
      ))}
      <Sequence from={f(HOI3)}>
        <Audio src={staticFile('sting.wav')} volume={0.5} />
      </Sequence>
    </AbsoluteFill>
  );
};
