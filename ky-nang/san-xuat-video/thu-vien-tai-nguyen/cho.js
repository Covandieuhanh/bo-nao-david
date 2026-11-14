// CHỖ TRỐNG QUANH NGƯỜI (David chốt 08/11/2026: graphic KHÔNG được đè hay làm mờ bất kỳ nhân vật nào; bám người đang nói)
// Đọc một mục mat.js (nguoi_place.py): nguoi[] = mọi người trong khung, noi = người đang nói.
// Trả về các khoảng ngang trống ở độ cao mặt, sau zoom nếu có. Mỗi người chiếm [l − đệm, r + đệm] (đệm = tai, tóc, tay, khoảng thở).
import project from '../project.js';
import {SAFE} from '../theme';

const W = project.width, H = project.height;
const DEM = 0.55;   // đệm mỗi bên = 0,55 × bề rộng mặt (gồm tai, tóc, tay khua)

// toạ độ sau zoom (cùng công thức render_preview.py: khung zoom canh giữa người đang nói, kẹp trong khung)
export const zoomBox = (m, Z = 1) => {
  if (!Z || Z <= 1.001) return (p) => p;
  const x0 = Math.max(0, Math.min(1 - 1 / Z, m.cx - 0.5 / Z)), y0 = Math.max(0, Math.min(1 - 1 / Z, m.cy - 0.5 / Z));
  return (p) => ({...p, cx: (p.cx - x0) * Z, cy: (p.cy - y0) * Z, w: p.w * Z, h: p.h * Z,
    l: (p.l - x0) * Z, r: (p.r - x0) * Z, t: (p.t - y0) * Z, b: (p.b - y0) * Z});
};

// mọi người (px), xếp trái → phải; mục mat cũ (một mặt) vẫn chạy
export const nguoi = (m, Z = 1) => {
  const z = zoomBox(m, Z);
  const ds = m.nguoi && m.nguoi.length ? m.nguoi
    : [{...m, l: m.l ?? m.cx - m.w / 2, r: m.r ?? m.cx + m.w / 2, t: m.cy - m.h / 2, b: m.cy + m.h / 2, noi: true}];
  return ds.map((p) => z(p)).map((p) => ({...p, L: (p.l - p.w * DEM) * W, R: (p.r + p.w * DEM) * W}))
    .sort((a, b) => a.cx - b.cx);
};

// khoảng trống ngang giữa / quanh mọi người, kèm người đứng sát hai bên
export const khoang = (ps) => {
  const out = [];
  let x = SAFE.left, prev = null;
  for (const p of ps) {
    if (p.L - x > 0) out.push({x0: x, x1: p.L, w: p.L - x, trai: prev, phai: p});
    x = Math.max(x, p.R); prev = p;
  }
  if (W - SAFE.right - x > 0) out.push({x0: x, x1: W - SAFE.right, w: W - SAFE.right - x, trai: prev, phai: null});
  return out;
};

// chọn chỗ cho một graphic bám người `muc` (mặc định người đang nói). `can` = bề rộng cần ở cỡ đẹp, `canNho` = ở cỡ nhỏ nhất
// còn đọc tốt. Thứ tự: khoảng sát người đó đủ cỡ đẹp → khoảng sát người đó đủ cỡ nhỏ (chữ nhỏ lại nhưng vẫn đúng người)
// → khoảng rộng nhất. Trả {x0, x1, w, ke: 'trai'|'phai'} — ke = graphic nằm bên nào của người bám.
export const chonCho = (ps, can, muc, canNho = can) => {
  const t = muc || ps.find((p) => p.noi) || ps[0];
  const ks = khoang(ps);
  const sat = ks.filter((k) => k.trai === t || k.phai === t).sort((a, b) => b.w - a.w);
  const k = sat.find((k) => k.w >= can) || sat.find((k) => k.w >= canNho)
    || [...ks].sort((a, b) => b.w - a.w)[0] || {x0: SAFE.left, x1: W - SAFE.right, w: W - SAFE.left - SAFE.right};
  return {...k, ke: k.phai === t ? 'trai' : 'phai', nguoiBam: t};
};

// người được bám: props.bam = 'trai' | 'phai' | số thứ tự; mặc định người đang nói
export const nguoiBam = (ps, bam) =>
  bam === 'trai' ? ps[0] : bam === 'phai' ? ps[ps.length - 1] : typeof bam === 'number' ? ps[bam] : (ps.find((p) => p.noi) || ps[0]);
