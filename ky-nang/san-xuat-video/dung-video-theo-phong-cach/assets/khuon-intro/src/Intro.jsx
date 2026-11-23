// Intro DAVID TRẦN — bản 6, 23/11/2026, khung ngang 1920×1080, 22,3 giây.
// Mỗi video trong album (và thư mục Drive) một cảnh: 20 cảnh; video dọc được cắt khung ngang 16:9 vừa chỗ David xuất hiện.
// Nhân vật làm trung tâm, chuyển cảnh mềm và đa dạng. Học từ intro diễn giả (John Sanei, Jacob Brown, Tony Robbins,
// Trần Hồng Hải): màu điện ảnh tối ấm, cắt đúng phách, vệt sáng ở điểm nhấn, chốt tên giãn chữ trên nền đen với vạch mảnh.
// Nhạc: "This Is Everything" — Josh Woodward (CC BY 3.0), đoạn 1:47,244–2:09,511; 156,6 BPM, phách 0,3831 s.
// Chữ "This is everything" rơi đúng phách 52 của intro → tên DAVID TRẦN hiện đúng lúc đó.
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
export const TONG = 668; // 22,3 giây
const TEN = 52; // phách hiện tên
const T = 10; // độ dài một lần chuyển cảnh (khung hình), một nửa nằm mỗi bên điểm cắt

// [đoạn, phách đầu, phách cuối, chuyển động trong cảnh, kiểu chuyển VÀO cảnh này]
// Kiểu chuyển: sang = tan cảnh qua vệt sáng ấm · zoom = phóng xuyên qua có nhòe · luot / luotNguoc = lướt ngang có nhòe
//              loc = quét chéo mép mềm · cat = cắt thẳng có nhấn (đoạn dồn trước cao trào)
const CANH = [
  ['c01', 0, 4, 'day', null],          // phòng đào tạo, cảnh toàn
  ['c02', 4, 7, 'day', 'sang'],        // phòng thu talk show
  ['c03', 7, 9, 'troi', 'zoom'],       // chia sẻ ở quán
  ['c04', 9, 12, 'day', 'luot'],       // đứng bảng, vest cam (dọc)
  ['c05', 12, 14, 'troi', 'loc'],      // viết sổ
  ['c06', 14, 17, 'day', 'zoom'],      // showroom cùng đối tác
  ['c07', 17, 19, 'day', 'luotNguoc'], // bắt tay ký kết (dọc)
  ['c08', 19, 22, 'troi', 'sang'],     // trò chuyện phòng khách
  ['c09', 22, 24, 'day', 'loc'],       // phòng spa
  ['c10', 24, 27, 'day', 'zoom'],      // bảng giảng (dọc)
  ['c11', 27, 29, 'troi', 'luot'],     // đội văn phòng
  ['c12', 29, 32, 'day', 'loc'],       // ngày hội kết nối kinh doanh (dọc)
  ['c13', 32, 34, 'troi', 'luotNguoc'],// trong tiệm spa
  ['c14', 34, 37, 'day', 'zoom'],      // trình bày, đội mũ (dọc)
  ['c15', 37, 39, 'troi', 'sang'],     // chào ở văn phòng
  ['c16', 39, 42, 'day', 'zoom'],      // hội trường lớn (dọc), "flashed before my eyes"
  ['c17', 42, 44, 'day', 'luotNguoc'], // sảnh, vest xám (dọc)
  ['c18', 44, 46, 'dap', 'cat'],       // trong ô tô ban đêm
  ['c19', 46, 48, 'dap', 'cat'],       // chỉ màn hình ở văn phòng
  ['h1', 48, TEN, 'day', 'sang'],      // cảnh chào cuối trên du thuyền
];
const VET_SANG = [0, 40, 48]; // vệt sáng lớn lóe qua ở điểm nhấn ngoài các lần chuyển "sang"

const ease = Easing.inOut(Easing.cubic);
const kep = { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' };

// Mỗi cảnh là một lớp: tự lo chuyển động bên trong + hiệu ứng lúc vào (lớp trên) và lúc ra (lớp dưới)
const Lop = ({ src, dai, keo, kieuVao, kieuRa, truoc, i }) => {
  const t = useCurrentFrame();
  const tt = t - truoc; // thời gian tính từ điểm cắt danh nghĩa
  const p = interpolate(tt, [0, dai], [0, 1], kep);
  let s = 1, x = 0;
  if (keo === 'day') s = interpolate(p, [0, 1], [1.03, 1.11], { easing: Easing.inOut(Easing.sin) });
  if (keo === 'troi') { s = 1.09; x = interpolate(p, [0, 1], i % 2 ? [-30, 30] : [30, -30]); }
  if (keo === 'dap') s = interpolate(tt, [0, 6], [1.14, 1.05], { ...kep, easing: Easing.out(Easing.cubic) });

  let op = 1, blur = 0, tx = 0, sc = 1, sang = 0, mask;
  // vào
  const dv = kieuVao && kieuVao !== 'cat' ? T : 0;
  if (dv) {
    const q = ease(Math.min(1, Math.max(0, t / dv)));
    if (kieuVao === 'sang') { op = q; sang = (1 - q) * 0.7; }
    if (kieuVao === 'zoom') { op = Math.min(1, q * 1.8); sc *= 1.28 - 0.28 * q; blur = 14 * (1 - q); }
    if (kieuVao === 'luot') { op = Math.min(1, q * 2); tx = (1 - q) * W * 0.55; blur = 16 * (1 - q); }
    if (kieuVao === 'luotNguoc') { op = Math.min(1, q * 2); tx = -(1 - q) * W * 0.55; blur = 16 * (1 - q); }
    if (kieuVao === 'loc') {
      const m = -25 + 150 * q;
      mask = `linear-gradient(115deg, #000 ${m - 22}%, rgba(0,0,0,0) ${m}%)`;
      sc *= 1.06 - 0.06 * q;
    }
  }
  const nhan = kieuVao === 'cat' ? interpolate(t, [0, 4], [0.28, 0], kep) : 0; // chớp sáng nhẹ ở cắt thẳng
  // ra
  const tongDai = truoc + dai + (kieuRa && kieuRa !== 'cat' ? T / 2 : 0);
  if (kieuRa && kieuRa !== 'cat') {
    const r = ease(Math.min(1, Math.max(0, (t - (tongDai - T)) / T)));
    if (kieuRa === 'zoom') { sc *= 1 + 0.3 * r; blur = Math.max(blur, 14 * r); }
    if (kieuRa === 'luot') { tx += -r * W * 0.4; blur = Math.max(blur, 16 * r); }
    if (kieuRa === 'luotNguoc') { tx += r * W * 0.4; blur = Math.max(blur, 16 * r); }
    if (kieuRa === 'sang') { sang = Math.max(sang, r * 0.5); }
    if (kieuRa === 'loc') { sc *= 1 + 0.04 * r; }
  }
  return (
    <AbsoluteFill style={{ overflow: 'hidden', opacity: op, WebkitMaskImage: mask, maskImage: mask }}>
      <AbsoluteFill style={{ background: '#000' }} />
      <OffthreadVideo src={staticFile(`canh/${src}.mp4`)} startFrom={Math.max(0, 9 - truoc)} muted
        style={{
          width: '100%', height: '100%', objectFit: 'cover',
          transform: `translateX(${x + tx}px) scale(${s * sc})`, filter: blur > 0.3 ? `blur(${blur}px)` : undefined,
        }} />
      <AbsoluteFill style={{ background: '#fff1e2', opacity: Math.max(sang * 0.6, nhan), mixBlendMode: 'screen' }} />
    </AbsoluteFill>
  );
};

// Đường sáng ấm mảnh chạy dọc mép quét chéo (lớp riêng, không bị mặt nạ che)
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

// Vệt sáng ấm lóe qua khung (ánh sáng lọt ống kính)
const VetSang = ({ manh = 0.85 }) => {
  const t = useCurrentFrame();
  const p = interpolate(t, [0, 16], [0, 1], { extrapolateRight: 'clamp' });
  const op = interpolate(t, [0, 4, 16], [0, manh, 0], { extrapolateRight: 'clamp' });
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
  const vach = interpolate(t, [6, 22], [0, 1], { ...kep, easing: Easing.out(Easing.cubic) });
  const quet = interpolate(t, [16, 40], [-30, 130], { ...kep, easing: Easing.inOut(Easing.quad) });
  const het = interpolate(t, [dai - 8, dai], [1, 0], kep);
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
      {CANH.map(([src, a, b, keo, vao], i) => {
        const ra = i + 1 < CANH.length ? CANH[i + 1][4] : null;
        const truoc = vao && vao !== 'cat' ? T / 2 : 0;
        const sau = ra && ra !== 'cat' ? T / 2 : 0;
        const tu = f(a) - truoc;
        return (
          <Sequence key={src} from={tu} durationInFrames={f(b) + sau - tu}>
            <Lop src={src} dai={f(b) - f(a)} keo={keo} kieuVao={vao} kieuRa={ra} truoc={truoc} i={i} />
          </Sequence>
        );
      })}
      {CANH.filter((c) => c[4] === 'sang').map(([src, a]) => (
        <Sequence key={`vs${src}`} from={f(a) - 8} durationInFrames={18}>
          <VetSang manh={0.7} />
        </Sequence>
      ))}
      {CANH.filter((c) => c[4] === 'loc').map(([src, a]) => (
        <Sequence key={`mq${src}`} from={f(a) - T / 2} durationInFrames={T}>
          <MepQuet />
        </Sequence>
      ))}
      {VET_SANG.map((k) => (
        <Sequence key={`v${k}`} from={Math.max(0, f(k) - 4)} durationInFrames={18}>
          <VetSang />
        </Sequence>
      ))}
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
