// Bố cục khung xuất. Mọi cảnh luôn được THIẾT KẾ trên khung video gốc (toạ độ dọc 1080×1920 như các component),
// Place đặt chúng vào khung xuất. Chế độ pillar (gốc dọc → xuất ngang 16:9):
//   cột giữa = video dọc thu về cao bằng khung; trái = chủ đề + từ khoá đang nói; phải = danh sách ý (hai-ben.jsx)
//   lớp phủ (thẻ, chữ to, tên) → thu nhỏ dải lớp phủ dọc vào ô SLOT ở cột trái
//   cảnh toàn màn hình, phụ đề → thay/đè video ở cột giữa (hai bên vẫn chạy); muốn phủ kín khung ngang thì viết component bản ngang
import React from 'react';
import {AbsoluteFill} from 'remotion';
import output from './dau-ra.js';
import project from './du-an.js';
import {SAFE, SAFE_W} from './chu-de';
import {POD, PF} from './khung-podcast';
import CAPTIONS from './phu-de.js';
import PLACEMENT from './vi-tri.js';
import HL from './doan-noi-bat.js';
import HS from './hoso.json';
import {TL_ON} from './thanh';
// 2 TRẠNG THÁI (hồ sơ hai_trang_thai, David chốt 2026-11-04): A = người + phụ đề, B = cảnh toàn màn hình + phụ đề. Lớp chữ không
// toàn màn hình (kinetic, lower, listItem…) KHÔNG được đè lên người → tự vẽ toàn màn hình. Ngoại lệ: thẻ tít mở đầu (hook) và
// ĐIỂM NHẤN TRÊN NGƯỜI 'nhan' (07/11/2026: làm tối viền, chữ / biểu tượng cạnh mặt — nhan.jsx tự tránh mặt, vẽ cả khung).
export const TWO = !!HS.hai_trang_thai && !project.podcast;
export const TWO_KEEP = new Set(['hook', 'nhan', 'bocuc']);   // 'bocuc' tự sắp người + nội dung (bo-cuc.jsx)
//   // 'nhan' = điểm nhấn trên người (David chốt 2026-11-07): được đè lên người, không che mặt

export const PILLAR = output?.layout === 'pillar';
export const OUT = PILLAR ? {W: output.width, H: output.height} : {W: project.width, H: project.height};
export const FULL = new Set(['illus', 'diagram', 'montage', 'recap', 'converge', 'master', 'gens', 'build', 'action', ...(project.podcast ? [] : ['card', 'cta'])]);   // thẻ toàn cảnh (trừ podcast)   // loại cảnh toàn màn hình (thêm loại mới vào đây)

const cw = Math.round(project.width * OUT.H / project.height / 2) * 2;
const pad = Math.round(OUT.W * 0.05), gap = Math.round(OUT.W * 0.021);
export const CENTER = {x: Math.round((OUT.W - cw) / 2), w: cw};
export const LEFT = {x: pad, w: CENTER.x - pad - gap};
export const RIGHT = {x: CENTER.x + cw + gap, w: OUT.W - CENTER.x - cw - gap - pad};
export const TOP = Math.round(OUT.H * 0.09), BOTTOM = Math.round(OUT.H * 0.91);
export const SLOT = {x: LEFT.x, y: Math.round(OUT.H * 0.47), w: LEFT.w};
const BAND_W = SAFE_W, BAND_H = SAFE.bottom - SAFE.overlayTop;
export const SLOT_H = Math.round(BAND_H * SLOT.w / BAND_W);

// Khung dọc (không pillar): lớp phủ (thẻ, chữ to, hook, tên) được THU NHỎ để thấy hình nhiều hơn. Mặc định đặt ngay TRÊN dải
// phụ đề ở đáy vùng an toàn. LUẬT: lớp phủ KHÔNG được che mặt/người nói (người dùng chốt) → vị trí từng cảnh lấy từ
// vi-tri.js (scripts/vi-tri-khuon-mat.py dò mặt, chọn chỗ trống: đỉnh, giữa hay đáy; thu nhỏ thêm nếu cần) hoặc `place: {top, scale}`
// đặt tay trong canh.js. Component vẫn vẽ trên dải gốc (overlayTop → bottom); Place dời/thu cả dải.
export const OV_SCALE = 0.78;
// dải phụ đề (đáy vùng an toàn); highlight ở video người nói (doan-noi-bat.js): thanh tập gốc chiếm đáy, phụ đề lên 40 px → dải cao hơn
export const CAP_H = CAPTIONS.length ? 140 + (TL_ON && !POD ? 40 : 0) : 0;   // thanh thời gian chiếm đáy → phụ đề lên
const OV_BOTTOM = SAFE.bottom - CAP_H;                           // đáy dải lớp phủ khi đặt mặc định
export const OV_TOP = Math.round(OV_BOTTOM - BAND_H * OV_SCALE);  // đỉnh mặc định

const Scaled = ({x, y, s, children}) => (
  <div style={{position: 'absolute', left: x, top: y, width: project.width, height: project.height,
    transform: `scale(${s})`, transformOrigin: '0 0'}}>{children}</div>
);

// Podcast (không có hình gốc): lớp phủ phóng/đặt vào vùng giữa sân khấu (khung-podcast.js: PF.ov) — dọc hoặc ngang toàn khung

// Mép chặn cứng: lớp phủ KHÔNG BAO GIỜ tràn xuống dải phụ đề (người dùng chỉ ra: ô hiệu ứng cao quá dải → phụ đề đè lên).
// Đây là lưới an toàn — component vẫn phải tự vừa dải (chụp thử để thấy phần bị cắt).
const Clip = ({h, children}) => (
  <div style={{position: 'absolute', left: 0, top: 0, width: '100%', height: h, overflow: 'hidden'}}>{children}</div>
);

export const Place = ({type, id, place, children}) => {
  if (!PILLAR) {
    if (FULL.has(type) || type === 'captions' || type === 'nhan' || type === 'bocuc' || type === 've' || type === 'sides' || type === 'stage' || type === 'cover' || type === 'endcard') return children;
    if (POD) {
      const pl = place || PF.ov;
      const x = PF.left - SAFE.left * pl.scale;   // dải lớp phủ canh trái vùng an toàn (ngang: bên phải là vòng micro)
      return <AbsoluteFill><Clip h={PF.contentBottom}><Scaled x={x} y={pl.top - SAFE.overlayTop * pl.scale} s={pl.scale}>{children}</Scaled></Clip></AbsoluteFill>;
    }
    const pl = place || PLACEMENT[id] || {};
    // TỰ CHUYỂN TOÀN MÀN HÌNH (vi-tri-khuon-mat.py: lớp phủ sẽ che mặt / thân trên — David chốt 2026-11-04): nền tối + quầng cam như
    // cảnh toàn màn hình, nội dung dải lớp phủ phóng to đặt giữa khung (phụ đề vẫn chạy ở lớp trên cùng)
    if ((pl.full && pl.full !== false) || (TWO && !TWO_KEEP.has(type) && !place)) {   // đặt tay `place` (vd {full:false} / {top,scale}) = giữ lớp phủ
      const fs = Math.min(1.25, (project.width * 0.9) / BAND_W), y0 = Math.round(project.height * 0.42 - BAND_H * fs / 2);
      return (
        <AbsoluteFill style={{background: '#0D0D10'}}>
          <AbsoluteFill style={{background: 'radial-gradient(circle at 50% 42%, rgba(255,122,69,0.2), transparent 60%)'}} />
          <Scaled x={(project.width - BAND_W * fs) / 2 - SAFE.left * fs} y={y0 - SAFE.overlayTop * fs} s={fs}>{children}</Scaled>
        </AbsoluteFill>
      );
    }
    const sc = pl.scale || OV_SCALE, top = pl.top ?? OV_TOP;
    // Không nền đen mờ sau lớp phủ: thẻ tự có nền sẫm đặc (C.card)
    return (
      <AbsoluteFill>
        <Clip h={OV_BOTTOM}><Scaled x={SAFE.left * (1 - sc)} y={top - SAFE.overlayTop * sc} s={sc}>{children}</Scaled></Clip>
      </AbsoluteFill>
    );
  }
  if (type === 'sides' || type === 'stage' || type === 'endcard') return children;   // sân khấu podcast: khung dọc riêng, pillar_base ghép vào giữa
  if (FULL.has(type) || type === 'captions' || type === 'nhan' || type === 'bocuc' || type === 've') return <AbsoluteFill><Scaled x={CENTER.x} y={0} s={OUT.H / project.height}>{children}</Scaled></AbsoluteFill>;
  const s = SLOT.w / BAND_W;
  return (
    <AbsoluteFill>
      <div style={{position: 'absolute', left: SLOT.x, top: SLOT.y, width: SLOT.w, height: SLOT_H, overflow: 'hidden'}}>
        <Scaled x={-SAFE.left * s} y={-SAFE.overlayTop * s} s={s}>{children}</Scaled>
      </div>
    </AbsoluteFill>
  );
};
