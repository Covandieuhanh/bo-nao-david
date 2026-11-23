// Intro DAVID TRẦN — bản 4, 23/11/2026, khung ngang 1920×1080, 14,6 giây: 12 cảnh khác nhau, mỗi cảnh một lần, nhân vật làm trung tâm.
// Học từ intro diễn giả (John Sanei, Jacob Brown, Tony Robbins, Trần Hồng Hải): màu điện ảnh tối ấm, ít cảnh nhưng cảnh nào cũng đẹp,
// cắt đúng phách, vệt sáng ở điểm nhấn, chốt tên giãn chữ trên nền đen với vạch mảnh.
// Nhạc: "This Is Everything" — Josh Woodward (CC BY 3.0), đoạn 1:54,906–2:09,506; 156,6 BPM, phách 0,3831 s.
// Chữ "This is everything" rơi đúng phách 32 của intro → tên DAVID TRẦN hiện đúng lúc đó.
import React, { useEffect, useState } from 'react';
import {
  AbsoluteFill, Audio, OffthreadVideo, Sequence, continueRender, delayRender, interpolate, staticFile,
  useCurrentFrame, Easing,
} from 'remotion';
import '@fontsource/barlow-condensed/800.css';

const C = { text: '#F4F4F5', accent: '#FF7A45' };
const HEAD = '"Barlow Condensed", sans-serif';
const NHIP = 0.3831 * 30; // khung hình mỗi phách
const f = (k) => Math.round(k * NHIP);
export const TONG = 438; // 14,6 giây
const TEN = 32; // phách hiện tên

// [đoạn, phách đầu, phách cuối, kiểu chuyển động, dọc?] — 12 cảnh khác nhau, mỗi cảnh một lần (David 23/11)
const CANH = [
  ['o1', 0, 4, 'day'], ['o2', 4, 8, 'day'],
  ['m1', 8, 10, 'troi'], ['m2', 10, 12, 'day'], ['m3', 12, 14, 'day', true], ['m4', 14, 16, 'troi'],
  ['m5', 16, 18, 'day'], ['m6', 18, 20, 'troi'], ['m7', 20, 22, 'day', true], ['m8', 22, 24, 'troi'],
  ['c1', 24, 28, 'day', 'gan'], // cao trào: hội trường lớn, đúng câu "I realized"
  ['h1', 28, TEN, 'day'],
];
const VET_SANG = [0, 4, 8, 20, 24, 28]; // vệt sáng lóe qua ở các điểm nhấn của nhạc ("flashed" ở phách 20, "realized" ở phách 24–26)

const Canh = ({ src, dai, kieu, i }) => {
  const t = useCurrentFrame();
  const p = interpolate(t, [0, dai], [0, 1], { extrapolateRight: 'clamp' });
  let s = 1, x = 0;
  if (kieu === 'day') s = interpolate(p, [0, 1], [1.02, 1.1], { easing: Easing.inOut(Easing.sin) }); // đẩy máy chậm vào
  if (kieu === 'troi') { s = 1.08; x = interpolate(p, [0, 1], i % 2 ? [-28, 28] : [28, -28]); } // trôi ngang chậm
  if (kieu === 'dap') s = interpolate(t, [0, 6], [1.12, 1.04], { extrapolateRight: 'clamp', easing: Easing.out(Easing.cubic) });
  const vao = interpolate(t, [0, 3], [0.35, 0], { extrapolateRight: 'clamp' }); // chớp tối rất nhẹ ở mỗi cắt
  return (
    <AbsoluteFill style={{ background: '#000', overflow: 'hidden' }}>
      <OffthreadVideo src={staticFile(`canh/${src}.mp4`)} startFrom={9} muted
        style={{ width: '100%', height: '100%', objectFit: 'cover', transform: `translateX(${x}px) scale(${s})` }} />
      <AbsoluteFill style={{ background: '#000', opacity: vao }} />
    </AbsoluteFill>
  );
};

// Cảnh quay dọc trong khung ngang: nền là chính cảnh đó phóng to, mờ, tối; cảnh nét ở giữa, viền mảnh, bóng mềm
const CanhDoc = ({ src, dai, lop, gan }) => {
  const t = useCurrentFrame();
  const p = interpolate(t, [0, dai], [0, 1], { extrapolateRight: 'clamp' });
  const s = interpolate(p, [0, 1], [1.0, 1.06], { easing: Easing.inOut(Easing.sin) });
  const vao = interpolate(t, [0, 3], [0.35, 0], { extrapolateRight: 'clamp' });
  const v = (style) => (
    <OffthreadVideo src={staticFile(`canh/${src}.mp4`)} startFrom={9} muted style={style} />
  );
  const H = 980;
  const trong = gan ? interpolate(p, [0, 1], [1.12, 1.32], { easing: Easing.inOut(Easing.sin) }) : 1; // cao trào: đẩy vào gần David
  if (lop === 'khung') {
    return (
      <AbsoluteFill>
        <div style={{
          position: 'absolute', left: '50%', top: '50%', height: H, aspectRatio: '9 / 16', transform: `translate(-50%, -50%) scale(${0.97 + 0.03 * s})`,
          borderRadius: 4, overflow: 'hidden', boxShadow: '0 30px 90px rgba(0,0,0,0.75)', outline: '1px solid rgba(255,236,220,0.3)',
        }}>
          {v({ width: '100%', height: '100%', objectFit: 'cover', transform: `scale(${trong})`, transformOrigin: '50% 42%' })}
          <AbsoluteFill style={{ background: '#000', opacity: vao }} />
        </div>
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: '#000', overflow: 'hidden' }}>
      {v({ position: 'absolute', inset: -80, width: 'calc(100% + 160px)', height: 'calc(100% + 160px)', objectFit: 'cover',
        filter: 'blur(38px) brightness(0.42) saturate(0.9)', transform: `scale(${1.1 + 0.05 * p})` })}
      <AbsoluteFill style={{ background: 'radial-gradient(ellipse 50% 70% at 50% 50%, rgba(0,0,0,0) 30%, rgba(0,0,0,0.55) 100%)' }} />
      <AbsoluteFill style={{ background: '#000', opacity: vao }} />
    </AbsoluteFill>
  );
};

// Vệt sáng ấm lóe qua khung (ánh sáng lọt ống kính)
const VetSang = () => {
  const t = useCurrentFrame();
  const p = interpolate(t, [0, 16], [0, 1], { extrapolateRight: 'clamp' });
  const op = interpolate(t, [0, 4, 16], [0, 0.85, 0], { extrapolateRight: 'clamp' });
  return (
    <AbsoluteFill style={{
      mixBlendMode: 'screen', opacity: op,
      background: `radial-gradient(ellipse 55% 80% at ${-20 + p * 140}% 45%, rgba(255,170,90,0.95), rgba(255,122,69,0.45) 40%, rgba(0,0,0,0) 72%)`,
    }} />
  );
};

// Hạt phim rất nhẹ cho chất điện ảnh
const HatPhim = () => {
  const t = useCurrentFrame();
  const seed = Math.floor(t / 2);
  return (
    <svg width="1920" height="1080" style={{ position: 'absolute', inset: 0, opacity: 0.07, mixBlendMode: 'overlay' }}>
      <filter id="hat"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed={seed} /></filter>
      <rect width="100%" height="100%" filter="url(#hat)" />
    </svg>
  );
};

// Hai dải đen trên dưới: khung điện ảnh 2,35:1, mở ra từ giữa lúc bắt đầu
const KhungPhim = () => {
  const t = useCurrentFrame();
  const h = interpolate(t, [0, 10], [540, 131], { extrapolateRight: 'clamp', easing: Easing.out(Easing.cubic) });
  return (
    <>
      <div style={{ position: 'absolute', left: 0, right: 0, top: 0, height: h, background: '#000' }} />
      <div style={{ position: 'absolute', left: 0, right: 0, bottom: 0, height: h, background: '#000' }} />
    </>
  );
};

// Chốt tên: nền đen, chữ giãn rộng rồi khép dần, hai vạch cam mảnh mở từ giữa, một vệt sáng quét qua chữ
const ChotTen = () => {
  const t = useCurrentFrame();
  const dai = TONG - f(TEN);
  const chop = interpolate(t, [0, 4], [0.55, 0], { extrapolateRight: 'clamp' });
  const hien = interpolate(t, [1, 12], [0, 1], { extrapolateRight: 'clamp', easing: Easing.out(Easing.cubic) });
  const gian = interpolate(t, [0, dai], [0.62, 0.34], { easing: Easing.out(Easing.cubic) });
  const vach = interpolate(t, [6, 22], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.out(Easing.cubic) });
  const quet = interpolate(t, [16, 40], [-30, 130], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.inOut(Easing.quad) });
  const het = interpolate(t, [dai - 8, dai], [1, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const Vach = ({ y }) => (
    <div style={{ position: 'absolute', left: '50%', top: y, height: 3, width: 820 * vach, transform: 'translateX(-50%)', background: C.accent }} />
  );
  return (
    <AbsoluteFill style={{ background: 'radial-gradient(ellipse 60% 55% at 50% 50%, #1f130d 0%, #070605 60%, #000 100%)', opacity: het }}>
      <Vach y={540 - 118} />
      <Vach y={540 + 115} />
      <div style={{
        position: 'absolute', left: 0, right: 0, top: 540 - 95, textAlign: 'center', opacity: hien,
        fontFamily: HEAD, fontWeight: 800, fontSize: 168, lineHeight: '190px',
        letterSpacing: `${gian}em`, paddingLeft: `${gian}em`, transform: `scale(${0.96 + 0.04 * hien})`,
        backgroundImage: `linear-gradient(100deg, ${C.text} ${quet - 12}%, #fff3e6 ${quet}%, ${C.text} ${quet + 12}%)`,
        WebkitBackgroundClip: 'text', backgroundClip: 'text', WebkitTextFillColor: 'transparent',
      }}>DAVID TRẦN</div>
      <AbsoluteFill style={{ background: '#fff4ea', opacity: chop }} />
    </AbsoluteFill>
  );
};

export const Intro = () => {
  const t = useCurrentFrame();
  const [h] = useState(() => delayRender('phông chữ'));
  useEffect(() => {
    document.fonts.load(`800 100px "Barlow Condensed"`, 'DAVID TRẦN').then(() => continueRender(h));
  }, [h]);
  const moDau = interpolate(t, [0, 8], [1, 0], { extrapolateRight: 'clamp' });
  return (
    <AbsoluteFill style={{ background: '#000' }}>
      {CANH.map(([src, a, b, kieu, doc], i) => (
        <Sequence key={src} from={f(a)} durationInFrames={f(b) - f(a)}>
          {doc ? <CanhDoc src={src} dai={f(b) - f(a)} lop="nen" /> : <Canh src={src} dai={f(b) - f(a)} kieu={kieu} i={i} />}
        </Sequence>
      ))}
      <Sequence from={0} durationInFrames={f(TEN)}>
        <HatPhim />
        <KhungPhim />
      </Sequence>
      {CANH.filter((c) => c[4]).map(([src, a, b, , doc]) => (
        <Sequence key={`k${src}`} from={f(a)} durationInFrames={f(b) - f(a)}>
          <CanhDoc src={src} dai={f(b) - f(a)} lop="khung" gan={doc === 'gan'} />
        </Sequence>
      ))}
      {VET_SANG.map((k) => (
        <Sequence key={`v${k}`} from={Math.max(0, f(k) - 4)} durationInFrames={18}>
          <VetSang />
        </Sequence>
      ))}
      <AbsoluteFill style={{ background: '#000', opacity: moDau }} />
      <Sequence from={f(TEN)}>
        <ChotTen />
      </Sequence>
      <Audio src={staticFile('nhac-intro.wav')} />
      <Sequence from={f(TEN)}>
        <Audio src={staticFile('sting.wav')} volume={0.3} />
      </Sequence>
    </AbsoluteFill>
  );
};
