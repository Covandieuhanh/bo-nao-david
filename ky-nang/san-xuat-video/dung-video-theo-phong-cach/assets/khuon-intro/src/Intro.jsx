// Intro DAVID TRẦN — bản 7, 23/11/2026, khung ngang 1920×1080, 12,65 giây (cả 2 giây nhạc nhỏ dần ở cuối).
// Độ dài theo hình mẫu: thẻ thương hiệu của kênh lớn 4–11 giây (Mel Robbins khoảng 5, Tony Robbins khoảng 5, Vietcetera
// "10.000 hours" khoảng 10), đặt sau đoạn mở đầu hút người xem. Chỉ 9 cảnh đẹp và ấn tượng nhất, 1 cảnh nhấn (quay chậm, lóe sáng).
// Thay cảnh về sau: sửa danh-sach-canh.txt (giữ tên đoạn) rồi cắt lại, không cần sửa code.
// Nhạc: "This Is Everything" — Josh Woodward (CC BY 3.0), trọn câu "And life is all you know, and when it flashed before my eyes,
// I realized, this is everything" (1:58,354–2:11,004); 156,6 BPM, phách 0,3831 s; nhạc nhỏ dần 2 giây sau chữ "everything"
// để nối mềm sang âm thanh chính của video.
import React, { useEffect, useState } from 'react';
import {
  AbsoluteFill, Audio, OffthreadVideo, Sequence, continueRender, delayRender, interpolate, staticFile,
  useCurrentFrame, Easing,
} from 'remotion';
import '@fontsource/barlow-condensed/800.css';

const C = { text: '#F4F4F5', accent: '#FF7A45' };
const HEAD = '"Barlow Condensed", sans-serif';
const W = 1920;
const NHIP = 0.3831 * 30; // khung hình mỗi phách
const f = (k) => Math.round(k * NHIP);
export const TONG = 380; // 12,65 giây
const TEN = 23; // phách hiện tên: chữ "This"
const T = 12; // độ dài một lần chuyển cảnh (khung hình), một nửa nằm mỗi bên điểm cắt

// [đoạn, phách đầu, phách cuối, chuyển động trong cảnh, kiểu chuyển VÀO cảnh này, nhấn?]
// Kiểu chuyển: sang = tan cảnh qua vệt sáng ấm · zoom = phóng xuyên có nhòe · luot / luotNguoc = lướt ngang có nhòe
//   loc = quét chéo mép mềm có đường sáng · mo = mở nét dần (cảnh cũ nhòe tan, cảnh mới nét lại) · vong = mở tròn mềm từ giữa
//   quay = xoay phóng nhẹ có nhòe · trang = lóe trắng ấm (chỉ cho cảnh nhấn)
const CANH = [
  ['e01', 0, 3, 'day', null],          // phòng đào tạo, cảnh toàn
  ['e02', 3, 5, 'troi', 'mo'],         // viết sổ
  ['e03', 5, 7, 'day', 'luot'],        // phòng thu talk show
  ['e04', 7, 9, 'day', 'vong'],        // bắt tay ký kết
  ['e05', 9, 11, 'troi', 'quay'],      // đứng bảng, vest cam
  ['e06', 11, 15, 'gan', 'trang', true], // CẢNH NHẤN: hội trường lớn, "flashed before my eyes" — quay chậm, đẩy vào
  ['e07', 15, 17, 'troi', 'zoom'],     // chia sẻ ở quán
  ['e08', 17, 19, 'day', 'loc'],       // trò chuyện phòng khách
  ['h1', 19, TEN, 'day', 'sang'],      // cảnh chào cuối trên du thuyền, "I realized"
];

const ease = Easing.inOut(Easing.cubic);
const kep = { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' };
const co = (kieu) => kieu && kieu !== 'cat';

// Mỗi cảnh là một lớp: chuyển động bên trong + hiệu ứng lúc vào (lớp trên) và lúc ra (lớp dưới)
const Lop = ({ src, dai, keo, kieuVao, kieuRa, truoc, i, nhan }) => {
  const t = useCurrentFrame();
  const tt = t - truoc;
  const p = interpolate(tt, [0, dai], [0, 1], kep);
  let s = 1, x = 0;
  if (keo === 'day') s = interpolate(p, [0, 1], [1.03, 1.11], { easing: Easing.inOut(Easing.sin) });
  if (keo === 'troi') { s = 1.09; x = interpolate(p, [0, 1], i % 2 ? [-30, 30] : [30, -30]); }
  if (keo === 'gan') s = interpolate(p, [0, 1], [1.0, 1.22], { easing: Easing.out(Easing.quad) });

  let op = 1, blur = 0, tx = 0, sc = 1, rot = 0, sang = 0, mask;
  if (co(kieuVao)) {
    const q = ease(Math.min(1, Math.max(0, t / T)));
    if (kieuVao === 'sang') { op = q; sang = (1 - q) * 0.7; }
    if (kieuVao === 'zoom') { op = Math.min(1, q * 1.8); sc *= 1.28 - 0.28 * q; blur = 14 * (1 - q); }
    if (kieuVao === 'luot') { op = Math.min(1, q * 2); tx = (1 - q) * W * 0.55; blur = 16 * (1 - q); }
    if (kieuVao === 'luotNguoc') { op = Math.min(1, q * 2); tx = -(1 - q) * W * 0.55; blur = 16 * (1 - q); }
    if (kieuVao === 'loc') { const m = -25 + 150 * q; mask = `linear-gradient(115deg, #000 ${m - 22}%, rgba(0,0,0,0) ${m}%)`; sc *= 1.06 - 0.06 * q; }
    if (kieuVao === 'mo') { op = q; blur = 22 * (1 - q); sc *= 1.04 - 0.04 * q; }
    if (kieuVao === 'vong') { const r = 140 * q; mask = `radial-gradient(circle at 50% 50%, #000 ${Math.max(0, r - 18)}%, rgba(0,0,0,0) ${r}%)`; sc *= 1.08 - 0.08 * q; }
    if (kieuVao === 'quay') { op = Math.min(1, q * 1.6); rot = (1 - q) * -7; sc *= 1.22 - 0.22 * q; blur = 12 * (1 - q); }
    if (kieuVao === 'trang') { op = Math.min(1, q * 2.2); sang = (1 - q) * 1.0; sc *= 1.12 - 0.12 * q; }
  }
  const tongDai = truoc + dai + (co(kieuRa) ? T / 2 : 0);
  if (co(kieuRa)) {
    const r = ease(Math.min(1, Math.max(0, (t - (tongDai - T)) / T)));
    if (kieuRa === 'zoom') { sc *= 1 + 0.3 * r; blur = Math.max(blur, 14 * r); }
    if (kieuRa === 'luot') { tx += -r * W * 0.4; blur = Math.max(blur, 16 * r); }
    if (kieuRa === 'luotNguoc') { tx += r * W * 0.4; blur = Math.max(blur, 16 * r); }
    if (kieuRa === 'sang') sang = Math.max(sang, r * 0.5);
    if (kieuRa === 'loc' || kieuRa === 'vong') sc *= 1 + 0.04 * r;
    if (kieuRa === 'mo') blur = Math.max(blur, 22 * r);
    if (kieuRa === 'quay') { rot += r * 6; sc *= 1 + 0.2 * r; blur = Math.max(blur, 12 * r); }
    if (kieuRa === 'trang') sang = Math.max(sang, r * 0.9);
  }
  return (
    <AbsoluteFill style={{ overflow: 'hidden', opacity: op, WebkitMaskImage: mask, maskImage: mask }}>
      <OffthreadVideo src={staticFile(`canh/${src}.mp4`)} startFrom={Math.max(0, 9 - truoc)} muted
        playbackRate={nhan ? 0.6 : 1}
        style={{
          width: '100%', height: '100%', objectFit: 'cover',
          transform: `translateX(${x + tx}px) scale(${s * sc}) rotate(${rot}deg)`,
          filter: blur > 0.3 ? `blur(${blur}px)` : undefined,
        }} />
      <AbsoluteFill style={{ background: '#fff1e2', opacity: sang * 0.65, mixBlendMode: 'screen' }} />
    </AbsoluteFill>
  );
};

// Đường sáng ấm mảnh chạy dọc mép quét chéo
const MepQuet = () => {
  const t = useCurrentFrame();
  const q = ease(Math.min(1, Math.max(0, t / T)));
  const m = -25 + 150 * q - 11;
  const op = interpolate(t, [0, 2, T - 2, T], [0, 1, 1, 0], kep);
  return (
    <AbsoluteFill style={{
      mixBlendMode: 'screen', opacity: op,
      background: `linear-gradient(115deg, rgba(0,0,0,0) ${m - 4}%, rgba(255,196,140,0.75) ${m}%, rgba(0,0,0,0) ${m + 4}%)`,
    }} />
  );
};

// Vòng sáng ấm mảnh chạy theo mép mở tròn
const MepVong = () => {
  const t = useCurrentFrame();
  const q = ease(Math.min(1, Math.max(0, t / T)));
  const r = 140 * q - 9;
  const op = interpolate(t, [0, 2, T - 2, T], [0, 0.9, 0.9, 0], kep);
  return (
    <AbsoluteFill style={{
      mixBlendMode: 'screen', opacity: op,
      background: `radial-gradient(circle at 50% 50%, rgba(0,0,0,0) ${r - 3}%, rgba(255,196,140,0.7) ${r}%, rgba(0,0,0,0) ${r + 3}%)`,
    }} />
  );
};

// Vệt sáng ấm lóe qua khung (ánh sáng lọt ống kính)
const VetSang = ({ manh = 0.85, rong = 55 }) => {
  const t = useCurrentFrame();
  const p = interpolate(t, [0, 16], [0, 1], { extrapolateRight: 'clamp' });
  const op = interpolate(t, [0, 4, 16], [0, manh, 0], { extrapolateRight: 'clamp' });
  return (
    <AbsoluteFill style={{
      mixBlendMode: 'screen', opacity: op,
      background: `radial-gradient(ellipse ${rong}% 80% at ${-20 + p * 140}% 45%, rgba(255,170,90,0.95), rgba(255,122,69,0.45) 40%, rgba(0,0,0,0) 72%)`,
    }} />
  );
};

// Tia sáng tỏa từ giữa cho cảnh nhấn
const BungSang = () => {
  const t = useCurrentFrame();
  const op = interpolate(t, [0, 3, 20], [0, 0.9, 0], kep);
  const r = interpolate(t, [0, 20], [10, 90], kep);
  return (
    <AbsoluteFill style={{
      mixBlendMode: 'screen', opacity: op,
      background: `radial-gradient(circle at 50% 45%, rgba(255,240,220,0.95) 0%, rgba(255,160,90,0.55) ${r * 0.4}%, rgba(0,0,0,0) ${r}%)`,
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

// Chốt tên: nền đen, chữ giãn rộng rồi khép dần, hai vạch cam mảnh mở từ giữa, vệt sáng quét qua chữ;
// cuối cùng tên mờ dần cùng lúc nhạc nhỏ dần (khoảng 1,7 giây) để nối mềm sang nội dung chính
const ChotTen = () => {
  const t = useCurrentFrame();
  const dai = TONG - f(TEN);
  const chop = interpolate(t, [0, 4], [0.55, 0], { extrapolateRight: 'clamp' });
  const hien = interpolate(t, [1, 12], [0, 1], { extrapolateRight: 'clamp', easing: Easing.out(Easing.cubic) });
  const gian = interpolate(t, [0, dai], [0.62, 0.3], { easing: Easing.out(Easing.cubic) });
  const vach = interpolate(t, [6, 22], [0, 1], { ...kep, easing: Easing.out(Easing.cubic) });
  const quet = interpolate(t, [16, 40], [-30, 130], { ...kep, easing: Easing.inOut(Easing.quad) });
  const het = interpolate(t, [dai - 52, dai], [1, 0], { ...kep, easing: Easing.inOut(Easing.sin) });
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
      {CANH.map(([src, a, b, keo, vao, nhan], i) => {
        const ra = i + 1 < CANH.length ? CANH[i + 1][4] : null;
        const truoc = co(vao) ? T / 2 : 0;
        const sau = co(ra) ? T / 2 : 0;
        const tu = f(a) - truoc;
        return (
          <Sequence key={src} from={tu} durationInFrames={f(b) + sau - tu}>
            <Lop src={src} dai={f(b) - f(a)} keo={keo} kieuVao={vao} kieuRa={ra} truoc={truoc} i={i} nhan={nhan} />
          </Sequence>
        );
      })}
      {CANH.filter((c) => c[4] === 'sang').map(([src, a]) => (
        <Sequence key={`vs${src}`} from={f(a) - 8} durationInFrames={18}><VetSang manh={0.7} /></Sequence>
      ))}
      {CANH.filter((c) => c[4] === 'loc').map(([src, a]) => (
        <Sequence key={`mq${src}`} from={f(a) - T / 2} durationInFrames={T}><MepQuet /></Sequence>
      ))}
      {CANH.filter((c) => c[4] === 'vong').map(([src, a]) => (
        <Sequence key={`mv${src}`} from={f(a) - T / 2} durationInFrames={T}><MepVong /></Sequence>
      ))}
      {CANH.filter((c) => c[5]).map(([src, a]) => (
        <Sequence key={`bs${src}`} from={f(a) - 3} durationInFrames={22}><BungSang /></Sequence>
      ))}
      <Sequence from={0} durationInFrames={18}><VetSang /></Sequence>
      <Sequence from={0} durationInFrames={f(TEN)}>
        <HatPhim />
        <KhungPhim />
      </Sequence>
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
