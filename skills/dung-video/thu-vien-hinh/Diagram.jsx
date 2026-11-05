// SƠ ĐỒ NÓI THAY LỜI (David chốt 2026-11-05, khối 07): khác `Illus` (biểu tượng + nhãn), mỗi cảnh là MỘT hình diễn tả TRỌN một câu
// nói — cấu trúc của câu (tầng bậc, trong→ngoài, trước→sau, tăng dần, từ→thành) hiện thành hình. Học cách TRÌNH BÀY đơn giản của
// Hieu Nguyen (một ý / màn, xây dần theo lời), giữ thẩm mỹ của bộ nhận diện. Toàn màn hình, phụ đề vẫn chạy. Mọi chữ TRÍCH lời.
// props chung: mode, label (tiêu đề ≤ 4 chữ, hiện trên cùng, tuỳ chọn), items[{at, value?, label, sub?}], start, len
//   'tang'    tầng / kim tự tháp — items từ TRÊN xuống (ít → nhiều): {value: '108', label: 'LÃNH ĐẠO'}
//   'vong'    vòng đồng tâm — items từ TRONG ra NGOÀI: {label: 'BÊN TRONG'} … ngoài cùng = lớn nhất
//   'moc'     mốc thời gian trái → phải: {value: '2016', label: 'HƯỚNG DẪN'}
//   'cot'     biểu đồ cột tăng dần: {value: 10800, label: 'THÀNH VIÊN', show?: '10.800'} (chiều cao theo căn bậc của value)
//   'luoi'    lưới đếm: {total: 80, items: [{at, upto: 30, label: '30 NĂM'}]} — ô tô dần tới upto (vd. 80 năm cuộc đời)
//   'tu-thanh' từ → thành: items[0] = trước (mờ), items[1] = sau (cam); {label, sub?, icon?}
//   'anh'     ảnh thật trong khung bo góc: {photo: 'x.jpg' (motion/public/photos/), label, sub?, credit: 'Tác giả · CC BY-SA', ratio?: 3/4, pos?: '50% 30%'}
//             — chỉ ảnh giấy phép mở dùng thương mại (Wikimedia/Openverse) hoặc ảnh David gửi; ghi nguồn vào mô tả (nguon-anh.txt)
// Vùng vẽ như Illus: dọc 10–56% chiều cao · ngang 7–71% (chừa phụ đề + thanh thời gian).
import React from 'react';
import {AbsoluteFill, Img, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {BODY, C, HEAD, ease} from './tokens';
import {Icon} from './Icons';

const cl = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'};
const UP = {textTransform: 'uppercase', fontFamily: HEAD, fontWeight: 800, lineHeight: 1.15, paddingTop: '0.12em'};

export const Diagram = ({mode = 'tang', items = [], label = '', total = 0, start = 0, len}) => {
  const f = useCurrentFrame();
  const {fps, width: W, height: H, durationInFrames} = useVideoConfig();
  const Lf = len || durationInFrames;
  const land = W > H, M = Math.min(W, H);
  const rel = (t) => Math.round(((t ?? start) - start) * fps);
  const sp = (a) => spring({frame: f - a, fps, config: {damping: 15, stiffness: 140, mass: 0.7}});
  const out = interpolate(f, [Lf - 8, Lf], [1, 0], cl);
  const area = {left: W * 0.07, width: W * 0.86, top: H * (land ? 0.07 : 0.1), height: H * (land ? 0.64 : 0.46)};
  const AW = area.width, AH = area.height;
  const head = label ? M * (land ? 0.06 : 0.07) : 0;
  const bodyH = AH - (label ? head * 1.9 : 0);
  let body = null;

  if (mode === 'tang') {   // kim tự tháp ngược: dòng trên hẹp (ít), dòng dưới rộng (nhiều)
    const n = Math.max(1, items.length), gap = bodyH * 0.05, rh = (bodyH - gap * (n - 1)) / n;
    body = items.map((it, i) => {
      const p = sp(rel(it.at)), w = AW * (0.58 + 0.42 * (n === 1 ? 1 : i / (n - 1)));
      return (
        <div key={i} style={{position: 'absolute', left: (AW - w) / 2, top: i * (rh + gap), width: w, height: rh, borderRadius: rh * 0.22,
          background: i === 0 ? C.accent : `rgba(255,122,69,${0.1 + 0.1 * (n - 1 - i) / Math.max(1, n - 1)})`, border: `2px solid ${C.accent}`,
          display: 'flex', alignItems: 'center', justifyContent: 'center', gap: rh * 0.35, opacity: Math.min(1, p * 1.4),
          transform: `scaleX(${0.6 + 0.4 * p})`}}>
          {it.value && <div style={{...UP, fontSize: rh * 0.56, color: i === 0 ? C.bg : C.accent, fontVariantNumeric: 'tabular-nums'}}>{it.value}</div>}
          <div style={{...UP, fontSize: Math.min(rh * 0.34, w * 0.6 / Math.max(4, (it.label || '').length * 0.5)), color: i === 0 ? C.bg : C.text, whiteSpace: 'nowrap'}}>{it.label}</div>
        </div>
      );
    });
  } else if (mode === 'vong') {   // vòng đồng tâm: trong → ngoài, nhãn đặt ở đỉnh mỗi vòng
    const n = Math.max(1, items.length), R = Math.min(AW, bodyH) / 2, cx = AW / 2, cy = bodyH / 2;
    body = items.map((it, i) => {
      const r = R * (0.36 + 0.64 * (n === 1 ? 1 : i / (n - 1))), p = sp(rel(it.at));
      return (
        <React.Fragment key={i}>
          <div style={{position: 'absolute', left: cx - r, top: cy - r, width: r * 2, height: r * 2, borderRadius: r,
            border: `${i === 0 ? 0 : 3}px solid ${C.accent}`, background: i === 0 ? C.accent : 'transparent',
            opacity: Math.min(1, p * 1.3) * (i === 0 ? 1 : 0.35 + 0.65 * (1 - i / n)), transform: `scale(${0.7 + 0.3 * p})`}} />
          <div style={{position: 'absolute', left: cx - r, width: r * 2, top: i === 0 ? cy - R * 0.08 : cy - r + R * 0.06, textAlign: 'center',
            ...UP, fontSize: R * (i === 0 ? 0.13 : 0.1), color: i === 0 ? C.bg : C.text, opacity: ease(f, rel(it.at) + 6, rel(it.at) + 14)}}>{it.label}</div>
        </React.Fragment>
      );
    }).reverse();   // vẽ vòng ngoài trước để vòng trong nằm trên
  } else if (mode === 'moc') {   // mốc thời gian: đường kẻ chạy theo lời, mỗi mốc một chấm + giá trị + nhãn
    const n = Math.max(1, items.length), y = bodyH * 0.45, pad = AW * 0.06, step = (AW - pad * 2) / Math.max(1, n - 1);
    const lastA = rel(items[n - 1]?.at), firstA = rel(items[0]?.at);
    const lineP = interpolate(f, [firstA, Math.max(firstA + 1, lastA)], [0, 1], cl);
    body = (
      <>
        <div style={{position: 'absolute', left: pad, top: y - 3, width: (AW - pad * 2) * (n === 1 ? 1 : lineP), height: 6, borderRadius: 3, background: C.accent}} />
        {items.map((it, i) => {
          const x = n === 1 ? AW / 2 : pad + i * step, p = sp(rel(it.at)), cur = i === items.filter((q) => f >= rel(q.at)).length - 1;
          const sz = M * (land ? 0.045 : 0.05);
          return (
            <div key={i} style={{position: 'absolute', left: x - AW * 0.12, width: AW * 0.24, top: 0, height: bodyH, opacity: Math.min(1, p * 1.4)}}>
              {it.value && <div style={{position: 'absolute', bottom: bodyH - y + sz, width: '100%', textAlign: 'center', ...UP,
                fontSize: M * (land ? 0.075 : 0.085), color: cur ? C.accent : C.text}}>{it.value}</div>}
              <div style={{position: 'absolute', left: AW * 0.12 - sz / 2, top: y - sz / 2, width: sz, height: sz, borderRadius: sz,
                background: cur ? C.accent : C.bg, border: `4px solid ${C.accent}`, transform: `scale(${p})`,
                boxShadow: cur ? `0 0 30px ${C.accent}` : 'none'}} />
              <div style={{position: 'absolute', top: y + sz, width: '100%', textAlign: 'center', ...UP, fontSize: M * (land ? 0.036 : 0.04),
                color: C.text}}>{it.label}{it.sub && <div style={{fontFamily: BODY, fontWeight: 500, textTransform: 'none', fontSize: '0.7em',
                  color: C.muted, marginTop: 6}}>{it.sub}</div>}</div>
            </div>
          );
        })}
      </>
    );
  } else if (mode === 'cot') {   // cột tăng dần — chiều cao theo căn bậc (số chênh hàng trăm lần vẫn nhìn được)
    const n = Math.max(1, items.length), mx = Math.max(...items.map((it) => Math.sqrt(Math.max(0, it.value || 0))), 1);
    const gap = AW * 0.04, cw = Math.min(AW * 0.22, (AW - gap * (n - 1)) / n), x0 = (AW - (cw * n + gap * (n - 1))) / 2;
    const base = bodyH * 0.8, maxH = bodyH * 0.58;
    body = items.map((it, i) => {
      const a = rel(it.at), p = interpolate(f, [a, a + 18], [0, 1], {...cl, easing: (x) => 1 - Math.pow(1 - x, 3)});
      const h = Math.max(10, maxH * Math.sqrt(Math.max(0, it.value || 0)) / mx) * p;
      return (
        <React.Fragment key={i}>
          <div style={{position: 'absolute', left: x0 + i * (cw + gap), top: base - h, width: cw, height: h, borderRadius: `${cw * 0.12}px ${cw * 0.12}px 0 0`,
            background: i === n - 1 ? C.accent : 'rgba(255,122,69,0.35)'}} />
          <div style={{position: 'absolute', left: x0 + i * (cw + gap) - gap / 2, width: cw + gap, top: base - h - M * 0.075, textAlign: 'center', ...UP,
            fontSize: M * (land ? 0.055 : 0.06), color: i === n - 1 ? C.accent : C.text, opacity: ease(f, a + 10, a + 18)}}>{it.show ?? it.value}</div>
          <div style={{position: 'absolute', left: x0 + i * (cw + gap) - gap / 2, width: cw + gap, top: base + M * 0.015, textAlign: 'center', ...UP,
            fontSize: M * (land ? 0.032 : 0.036), color: C.muted, opacity: ease(f, a, a + 8)}}>{it.label}</div>
        </React.Fragment>
      );
    });
  } else if (mode === 'luoi') {   // lưới đếm: total ô, tô dần tới `upto` của từng mốc
    const T = Math.max(1, total), cols = Math.ceil(Math.sqrt(T * (AW / bodyH) * (land ? 1 : 0.9))), rows = Math.ceil(T / cols);
    const cell = Math.min(AW / cols, bodyH * 0.78 / rows), g = cell * 0.18, x0 = (AW - cell * cols) / 2;
    const marks = items.map((it) => ({a: rel(it.at), upto: it.upto || 0}));
    const filled = (k) => { let v = -1; for (const m of marks) if (f >= m.a) v = Math.max(v, Math.min(m.upto, Math.floor((f - m.a) / 1.2))); return k < v; };
    const cur = items.filter((it) => f >= rel(it.at)).pop();
    body = (
      <>
        {Array.from({length: T}).map((_, k) => (
          <div key={k} style={{position: 'absolute', left: x0 + (k % cols) * cell + g / 2, top: Math.floor(k / cols) * cell + g / 2, width: cell - g,
            height: cell - g, borderRadius: (cell - g) * 0.25, background: filled(k) ? C.accent : 'rgba(255,255,255,0.08)'}} />
        ))}
        {cur && <div style={{position: 'absolute', left: 0, width: AW, top: rows * cell + bodyH * 0.04, textAlign: 'center', ...UP,
          fontSize: M * (land ? 0.05 : 0.055), color: C.text}}>{cur.label}</div>}
      </>
    );
  } else if (mode === 'tu-thanh') {   // từ → thành
    const [a, b] = items, pw = AW * 0.38, ph = bodyH * 0.78, y = (bodyH - ph) / 2;
    const panel = (it, x, after) => {
      if (!it) return null;
      const p = sp(rel(it.at));
      return (
        <div style={{position: 'absolute', left: x, top: y, width: pw, height: ph, borderRadius: M * 0.03, opacity: Math.min(1, p * 1.3) * (after ? 1 : 0.6),
          background: after ? 'rgba(255,122,69,0.14)' : 'rgba(255,255,255,0.05)', border: `3px solid ${after ? C.accent : C.dim}`,
          display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: ph * 0.06, transform: `translateY(${(1 - p) * 40}px)`}}>
          {it.icon && <Icon name={it.icon} size={ph * 0.32} at={rel(it.at)} stroke={3} />}
          <div style={{...UP, fontSize: ph * 0.13, color: after ? C.accent : C.text, textAlign: 'center', padding: '0 4%'}}>{it.label}</div>
          {it.sub && <div style={{fontFamily: BODY, fontWeight: 600, fontSize: ph * 0.065, color: C.muted, textAlign: 'center', padding: '0 6%'}}>{it.sub}</div>}
        </div>
      );
    };
    const ap = b ? ease(f, rel(b.at) - 8, rel(b.at)) : 0;
    body = (
      <>
        {panel(a, 0, false)}
        <svg width={AW * 0.16} height={ph * 0.3} viewBox="0 0 100 40" style={{position: 'absolute', left: pw + AW * 0.04, top: y + ph * 0.35, opacity: ap}}>
          <path d="M5 20 H85 M68 6 L88 20 L68 34" fill="none" stroke={C.accent} strokeWidth="6" strokeLinecap="round" strokeLinejoin="round"
            strokeDasharray="140" strokeDashoffset={140 * (1 - ap)} />
        </svg>
        {panel(b, AW - pw, true)}
      </>
    );
  } else if (mode === 'anh') {   // ẢNH THẬT trong khung bo góc + nhãn + nguồn
    const it = items[0] || {}, p = sp(rel(it.at));
    const ph = bodyH * (it.label ? 0.8 : 0.95), pw = Math.min(AW * 0.9, ph * (it.ratio || (land ? 16 / 9 : 4 / 3))), x = (AW - pw) / 2;   // it.ratio: 3/4 cho chân dung
    const kb = 1.04 + Math.min(0.06, (f / fps) * 0.012);
    body = (
      <>
        <div style={{position: 'absolute', left: x, top: 0, width: pw, height: ph, borderRadius: M * 0.035, overflow: 'hidden',
          boxShadow: `0 30px 80px rgba(0,0,0,0.55), 0 0 0 3px ${C.accent}55`, opacity: Math.min(1, p * 1.3), transform: `scale(${0.92 + 0.08 * p})`}}>
          {it.photo && <Img src={staticFile(`photos/${it.photo}`)} style={{width: '100%', height: '100%', objectFit: 'cover', objectPosition: it.pos || '50% 35%', transform: `scale(${kb})`}} />}
          {it.credit && <div style={{position: 'absolute', right: 12, bottom: 10, fontFamily: BODY, fontSize: M * 0.016, color: 'rgba(255,255,255,0.75)',
            textShadow: '0 1px 4px rgba(0,0,0,0.8)'}}>{it.credit}</div>}
        </div>
        {it.label && <div style={{position: 'absolute', left: 0, width: AW, top: ph + bodyH * 0.05, textAlign: 'center', ...UP,
          fontSize: M * (land ? 0.05 : 0.055), color: C.text, opacity: ease(f, rel(it.at) + 8, rel(it.at) + 16)}}>{it.label}
          {it.sub && <span style={{color: C.accent}}> · {it.sub}</span>}</div>}
      </>
    );
  }

  const first = items.length ? rel(items[0].at) : 0;
  return (
    <AbsoluteFill style={{opacity: Math.min(ease(f, 0, 8), out)}}>
      <AbsoluteFill style={{background: C.bg}} />
      <AbsoluteFill style={{background: `radial-gradient(circle at 50% ${land ? 40 : 36}%, rgba(255,122,69,0.17), transparent 62%)`}} />
      <div style={{position: 'absolute', ...area}}>
        {label && <div style={{position: 'absolute', left: 0, width: AW, top: 0, textAlign: 'center', ...UP, fontSize: head, color: C.text,
          opacity: ease(f, Math.min(first, 4), Math.min(first, 4) + 10)}}>{label}
          <div style={{width: M * 0.1, height: 6, borderRadius: 3, background: C.accent, margin: `${head * 0.25}px auto 0`}} /></div>}
        <div style={{position: 'absolute', left: 0, top: label ? head * 1.9 : 0, width: AW, height: bodyH}}>{body}</div>
      </div>
    </AbsoluteFill>
  );
};
