// CHỮ SAU NGƯỜI (type 'chusau' — David chốt 10/11/2026, học từ Ali Abdaal + Joseph Video Editing): chữ to đứng GIỮA nền và người —
// người che một phần chữ, tạo chiều sâu. Lớp người lấy từ scripts/tach_nguoi.py (Vision tách người từng khung → public/nguoi/<id>/).
// props:
//   text   chữ NGUYÊN VĂN lời người nói, '\n' xuống dòng, `*từ*` = một từ nhấn font phụ (ChuHien). Ngắn: 2–6 chữ đọc trọn.
//   at     giây tuyệt đối lúc chữ bật (mặc định đầu cảnh)
//   cao    'dau' (mặc định: đáy khối chữ ngang mắt — đầu chỉ che phần dưới dòng cuối) | 'tren' (cao hơn, đầu chạm nhẹ chân chữ)
//          | 'vai' (chữ ngang vai, hợp khi đầu nằm cao sát mép trên) — chọn cái để chữ vẫn đọc được, chụp thử để kiểm
//   bong   true = BÓNG NGƯỜI: nền giấy sáng, người thành bóng màu nhấn cam, chữ tối sau bóng (cảnh kể chuyện lắng, câu tâm tình)
// Không dùng chung với zoom (`nhan` zoom) cùng lúc: lớp người sẽ lệch. Chữ phải còn đọc được khi người che — chụp thử để kiểm.
import React from 'react';
import {AbsoluteFill, Easing, Img, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {C, HEAD, BRAND_BOT, SAFE, ease, rel} from '../theme';
import project from '../project.js';
import MAT from '../mat.js';
import NGUOI from '../nguoi.js';
import {ChuHien, boSao} from '../lib/ChuHien';
import {kieuChu} from '../lib/chuyen-dong';

const W = project.width, H = project.height, LAND = W > H;
const GIAY = '#ECE7DF', MUC = '#18181B';
// hạt giấy: nhiễu SVG nhẹ, không cần ảnh
const HAT = `url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.35 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")`;

export const NguoiLop = ({sceneId, f, bong}) => {
  const n = NGUOI[sceneId];
  if (!n) return null;   // chưa chạy tach_nguoi.py → chỉ còn chữ (soát cảnh báo P0)
  const src = staticFile(`nguoi/${sceneId}/${String(Math.min(f, n - 1)).padStart(5, '0')}.png`);
  if (!bong) return <Img src={src} style={{position: 'absolute', inset: 0, width: W, height: H}} />;
  return (
    <>
      <Img src={src} style={{position: 'absolute', inset: 0, width: W, height: H, opacity: 0}} />
      <div style={{position: 'absolute', inset: 0, background: C.accent, WebkitMaskImage: `url(${src})`, maskImage: `url(${src})`,
        WebkitMaskSize: '100% 100%', maskSize: '100% 100%'}} />
    </>
  );
};

export const ChuSau = ({sceneId, start, text = '', at, cao = 'dau', bong = false}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d} = useVideoConfig();
  const a = at != null ? rel(at, start) : 4;
  const m = MAT[sceneId] || {cx: 0.5, cy: 0.38, w: 0.16, h: 0.24};
  const lines = String(text).split('\n');
  const chars = Math.max(4, ...lines.map((l) => boSao(l).length));
  const maxW = (LAND ? 0.9 : 0.92) * W;
  const fs = Math.min(LAND ? H * 0.24 : W * 0.24, maxW / (0.5 * chars));   // Barlow Condensed in hoa ≈ 0,5 em mỗi chữ
  const blockH = fs * 0.98 * lines.length;
  // đáy khối chữ: ngang mắt (đầu che phần dưới dòng cuối, phần lớn chữ vẫn đọc được) · 'tren' cao hơn · 'vai' xuống ngang vai
  const day = (cao === 'vai' ? m.cy + m.h * 1.6 : cao === 'tren' ? m.cy - m.h * 0.25 : m.cy + m.h * 0.05) * H;
  const top = Math.max(BRAND_BOT + 20, Math.min(SAFE.bottom - 160 - blockH, day - blockH));
  const vao = ease(f, a, a + 10);
  const ra = ease(f, d - 7, d, 1, 0, Easing.in(Easing.cubic));
  const nen = bong ? ease(f, 0, 10) * ra : 0;
  return (
    <AbsoluteFill>
      {bong && <AbsoluteFill style={{opacity: nen, background: GIAY}}><AbsoluteFill style={{backgroundImage: HAT, opacity: 0.5}} /></AbsoluteFill>}
      <div style={{position: 'absolute', left: 0, width: W, top, textAlign: 'center', opacity: ra,
        filter: ra < 1 ? `blur(${(8 * (1 - ra)).toFixed(2)}px)` : undefined, transform: `scale(${1.06 - 0.06 * vao})`}}>
        {lines.map((l, i) => (
          <div key={i} style={{fontFamily: HEAD, fontWeight: 800, fontSize: fs, lineHeight: 0.98, textTransform: 'uppercase',
            letterSpacing: 1, color: bong ? MUC : C.text, whiteSpace: 'nowrap',
            textShadow: bong ? 'none' : '0 6px 40px rgba(0,0,0,0.45)'}}>
            <ChuHien text={l} a={a + i * 4} kieu={kieuChu(sceneId)} />
          </div>
        ))}
      </div>
      <AbsoluteFill style={{opacity: bong ? nen : 1}}><NguoiLop sceneId={sceneId} f={f} bong={bong} /></AbsoluteFill>
    </AbsoluteFill>
  );
};
