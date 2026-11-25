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
//   'xay-tang' xây từ GỐC lên (khối 07, 2026-11-06) — items từ DƯỚI lên: {label, sub?}; ô trống hiện sẵn, mỗi tầng chỉ sáng đúng lúc nhắc (tầng sau xây trên tầng trước)
//   'doi-trang-thai' MỘT vật giữ nguyên, trạng thái đổi: items[0] = trước (xám), items[1] = sau (cam); {label, sub?, icon?} — bỏ icon ở items[1] = giữ hình cũ
//   'chuyen-giao' việc đi từ bên này sang bên kia: items[0] = bên giao, items[cuối] = bên nhận {label, icon}; giữa = các việc được chuyển {icon, label, at}
//   'chuoi'   CHUỖI BƯỚC (học Cường Mê AI, 20/11/2026): quy trình 3–6 bước kể liền một mạch. Bước hiện đúng lúc nói, dây nối từ bước
//             trước chạy tới (chấm sáng ở đầu dây chỉ hướng), bước đang nói viền cam, bước đã qua mờ. Dọc: cột trên → dưới · ngang: hàng
//             trái → phải (lồng trong bố cục thì luôn cột dọc). items: [{at, label (1–3 chữ nguyên văn), icon?}]
// mot_diem: true (tang, cot) — chỉ mục đang nói sáng cam, mục khác nhạt (nguyên lý "một chỗ sáng", huong-dan-lua-chon.md bước 4a). Mặc định tắt.
//   'anh'     ảnh thật trong khung bo góc: {photo: 'x.jpg' (chuyen-dong/public/anh/), label, sub?, credit: 'Tác giả · CC BY-SA', ratio?: 3/4, pos?: '50% 30%'}
//             — chỉ ảnh giấy phép mở dùng thương mại (Wikimedia/Openverse) hoặc ảnh David gửi; ghi nguồn vào mô tả (nguon-anh.txt)
// Vùng vẽ như Illus: dọc 10–56% chiều cao · ngang 12–80% (chừa phụ đề + thanh thời gian).
import React from 'react';
import {AbsoluteFill, Easing, Img, interpolate, interpolateColors, spring, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {BODY, C, HEAD, ease} from './bien-thiet-ke';
import {Icon} from './bieu-tuong';
import {NenPhong, usePhong} from './phong';

const cl = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'};
const UP = {textTransform: 'uppercase', fontFamily: HEAD, fontWeight: 800, lineHeight: 1.15, paddingTop: '0.12em'};
const fit = (txt, width, max) => Math.min(max, width / (Math.max(4, (txt || '').length) * 0.46));   // Barlow Condensed in hoa có dấu ≈ 0,46 em/ký tự

export const Diagram = ({mode = 'tang', items = [], label = '', total = 0, start = 0, len, nen = true, mot_diem = false}) => {   // nen=false: không vẽ nền (lồng trong bố cục BoCuc)
  const f = useCurrentFrame();
  const {fps, width: W, height: H, durationInFrames} = useVideoConfig();
  const Lf = len || durationInFrames;
  const land = W > H, M = Math.min(W, H);
  const rel = (t) => Math.round(((t ?? start) - start) * fps);
  const sp = (a) => spring({frame: f - a, fps, config: {damping: 15, stiffness: 140, mass: 0.7}});
  const out = interpolate(f, [Lf - 5, Lf], [1, 0], cl);   // ra ngắn hơn vào ~40%
  const area = {left: W * 0.07, width: W * 0.86, top: H * (land ? 0.12 : 0.1), height: H * (land ? 0.68 : 0.46)};
  const AW = area.width, AH = area.height;
  const head = label ? M * (land ? 0.06 : 0.07) : 0;
  const bodyH = AH - (label ? head * 1.9 : 0);
  let body = null;
  const curI = items.filter((it) => f >= rel(it.at)).length - 1;   // mục đang nói (mot_diem, chuoi)

  if (mode === 'tang') {   // kim tự tháp ngược: dòng trên hẹp (ít), dòng dưới rộng (nhiều)
    const n = Math.max(1, items.length), gap = bodyH * 0.05, rh = (bodyH - gap * (n - 1)) / n;
    body = items.map((it, i) => {
      const p = sp(rel(it.at)), w = AW * (0.58 + 0.42 * (n === 1 ? 1 : i / (n - 1))), hl = mot_diem ? i === curI : i === 0;
      return (
        <div key={i} style={{position: 'absolute', left: (AW - w) / 2, top: i * (rh + gap), width: w, height: rh, borderRadius: rh * 0.22,
          background: hl ? C.accent : `rgba(255,122,69,${0.1 + 0.1 * (n - 1 - i) / Math.max(1, n - 1)})`, border: `2px solid ${mot_diem && !hl ? 'rgba(255,122,69,0.4)' : C.accent}`,
          display: 'flex', alignItems: 'center', justifyContent: 'center', gap: rh * 0.35, opacity: Math.min(1, p * 1.4),
          transform: `scaleX(${0.6 + 0.4 * p})`}}>
          {it.value && <div style={{...UP, fontSize: rh * 0.56, color: hl ? C.bg : C.accent, fontVariantNumeric: 'tabular-nums'}}>{it.value}</div>}
          <div style={{...UP, fontSize: Math.min(rh * 0.34, w * 0.6 / Math.max(4, (it.label || '').length * 0.5)), color: hl ? C.bg : mot_diem ? C.muted : C.text, whiteSpace: 'nowrap'}}>{it.label}</div>
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
      const h = Math.max(10, maxH * Math.sqrt(Math.max(0, it.value || 0)) / mx) * p, hl = mot_diem ? i === curI : i === n - 1;
      return (
        <React.Fragment key={i}>
          <div style={{position: 'absolute', left: x0 + i * (cw + gap), top: base - h, width: cw, height: h, borderRadius: `${cw * 0.12}px ${cw * 0.12}px 0 0`,
            background: hl ? C.accent : 'rgba(255,122,69,0.35)'}} />
          <div style={{position: 'absolute', left: x0 + i * (cw + gap) - gap / 2, width: cw + gap, top: base - h - M * 0.075, textAlign: 'center', ...UP,
            fontSize: M * (land ? 0.055 : 0.06), color: hl ? C.accent : mot_diem ? C.muted : C.text, opacity: ease(f, a + 10, a + 18)}}>{it.show ?? it.value}</div>
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
  } else if (mode === 'xay-tang') {   // xây từ gốc lên: ô trống hiện sẵn, tầng sáng đúng lúc nhắc; tầng đang nói = cam đặc
    const n = Math.max(1, items.length), gap = bodyH * 0.04, rh = (bodyH - gap * (n - 1)) / n;
    const lit = items.filter((it) => f >= rel(it.at)).length;
    body = items.map((it, i) => {
      const a = rel(it.at), p = sp(a), cur = i === lit - 1;
      const w = AW * (1 - 0.3 * (n === 1 ? 0 : i / (n - 1))), x = (AW - w) / 2, y = (n - 1 - i) * (rh + gap);
      return (
        <React.Fragment key={i}>
          <div style={{position: 'absolute', left: x, top: y, width: w, height: rh, borderRadius: rh * 0.16, border: `3px dashed ${C.dim}`, boxSizing: 'border-box'}} />
          <div style={{position: 'absolute', left: x, top: y, width: w, height: rh, borderRadius: rh * 0.16, boxSizing: 'border-box',
            background: cur ? C.accent : 'rgba(255,122,69,0.16)', border: `2px solid ${C.accent}`, opacity: Math.min(1, p * 1.4),
            transform: `translateY(${(1 - p) * rh * 0.45}px)`, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center'}}>
            <div style={{...UP, fontSize: fit(it.label, w * 0.88, rh * 0.42), color: cur ? C.bg : C.text, whiteSpace: 'nowrap'}}>{it.label}</div>
            {it.sub && <div style={{fontFamily: BODY, fontWeight: 600, fontSize: rh * 0.15, color: cur ? C.bg : C.muted}}>{it.sub}</div>}
          </div>
        </React.Fragment>
      );
    });
  } else if (mode === 'doi-trang-thai') {   // một vật đứng yên, màu tràn từ giữa ra + nhãn đổi: trước (xám) → sau (cam)
    const [a, b] = items, ta = rel(a?.at), tb = b ? rel(b.at) : 1e9, pIn = sp(ta);
    const flip = interpolate(f, [tb, tb + 12], [0, 1], {...cl, easing: Easing.inOut(Easing.quad)}), sw = ease(f, tb, tb + 5);
    const S = Math.min(AW, bodyH) * 0.62, cx = AW / 2, cy = S / 2 + bodyH * 0.02, col = interpolateColors(flip, [0, 1], [C.dim, C.accent]);
    const nameOf = (it, on, blur) => it && (
      <div style={{position: 'absolute', left: 0, width: AW, top: S + bodyH * 0.07, textAlign: 'center', opacity: on, filter: `blur(${blur}px)`}}>
        <div style={{...UP, fontSize: fit(it.label, AW * 0.94, M * (land ? 0.075 : 0.095)), color: it === b ? C.accent : C.text}}>{it.label}</div>
        {it.sub && <div style={{fontFamily: BODY, fontWeight: 600, fontSize: M * 0.032, color: C.muted, marginTop: M * 0.008}}>{it.sub}</div>}
      </div>
    );
    body = (
      <>
        <div style={{position: 'absolute', left: cx - S * 1.5, top: cy - S * 1.5, width: S * 3, height: S * 3, borderRadius: S * 1.5,
          background: 'radial-gradient(circle, rgba(255,122,69,0.3), transparent 68%)', opacity: flip, transform: `scale(${0.25 + 0.75 * flip})`}} />
        <div style={{position: 'absolute', left: cx - S / 2, top: cy - S / 2, width: S, height: S, borderRadius: S, boxSizing: 'border-box', border: `4px solid ${col}`,
          background: flip > 0 ? `rgba(255,122,69,${0.12 * flip})` : 'rgba(255,255,255,0.04)', opacity: Math.min(1, pIn * 1.4), transform: `scale(${0.85 + 0.15 * pIn})`}}>
          {a?.icon && <div style={{position: 'absolute', left: S * 0.18, top: S * 0.18, opacity: b?.icon ? 1 - sw : 1, filter: `grayscale(${1 - flip}) brightness(${0.75 + 0.25 * flip})`}}>
            <Icon name={a.icon} size={S * 0.64} at={ta} stroke={2.8} /></div>}
          {b?.icon && f >= tb && <div style={{position: 'absolute', left: S * 0.18, top: S * 0.18, opacity: sw}}>
            <Icon name={b.icon} size={S * 0.64} at={tb} stroke={2.8} /></div>}
        </div>
        {nameOf(a, Math.min(1, pIn * 1.4) * (1 - sw), 8 * sw)}
        {nameOf(b, sw, 8 * (1 - sw))}
      </>
    );
  } else if (mode === 'chuyen-giao') {   // việc rời bên giao, đi theo đường cong (đường cam chạy theo), lọt vào bên nhận rồi nằm lại; bên giao nhẹ dần
    const n = items.length, A = items[0] || {}, Z = n > 1 ? items[n - 1] : {}, moved = items.slice(1, -1);
    const ns = Math.min(AW * 0.34, bodyH * 0.42), yN = Math.max(0, (bodyH - ns * 2.05) / 2), xZ = AW - ns, cyN = yN + ns / 2;
    const TR = 24, xFrom = ns / 2, xTo = xZ + ns / 2, arc = ns * 0.3;   // 0,8 s, đủ để mắt theo kịp
    const land1 = (it) => rel(it.at) + TR, done = moved.filter((it) => f >= land1(it));
    const cur = moved.filter((it) => f >= rel(it.at) - 6).pop();
    const lastLand = done.length ? land1(done[done.length - 1]) : -99;
    const bump = done.length ? 1 + 0.06 * (1 - ease(f, lastLand, lastLand + 12)) : 1;   // bên nhận đón việc một lần rồi đứng yên
    const ripple = done.length ? ease(f, lastLand, lastLand + 16) : 1;
    const lighten = moved.length ? done.length / moved.length : 0;
    const node = (it, x, after, sc = 1, op = 1) => (
      <div style={{position: 'absolute', left: x, top: yN, width: ns, opacity: op * Math.min(1, sp(rel(it.at)) * 1.4)}}>
        <div style={{position: 'relative', width: ns, height: ns, borderRadius: ns, boxSizing: 'border-box', border: `4px solid ${after ? C.accent : C.dim}`,
          background: after ? 'rgba(255,122,69,0.14)' : 'rgba(255,255,255,0.05)', transform: `scale(${sc})`}}>
          {it.icon && <div style={{position: 'absolute', left: ns * 0.2, top: ns * 0.2}}><Icon name={it.icon} size={ns * 0.6} at={rel(it.at)} stroke={3} /></div>}
        </div>
        <div style={{...UP, textAlign: 'center', fontSize: fit(it.label, ns * 1.1, M * (land ? 0.05 : 0.06)), color: after ? C.accent : C.text, marginTop: ns * 0.05}}>{it.label}</div>
      </div>
    );
    const U0 = 0.14, U1 = 0.86;   // đi từ mép bên giao tới mép bên nhận, không che biểu tượng ở hai đầu
    const uOf = (t) => U0 + (U1 - U0) * t;
    const pos = (t) => { const u = uOf(t); return [xFrom + (xTo - xFrom) * u, cyN - 4 * arc * u * (1 - u)]; };   // đúng theo đường cong bên dưới
    const curve = `M${xFrom} ${cyN} Q${(xFrom + xTo) / 2} ${cyN - arc * 2} ${xTo} ${cyN}`;
    const inFlight = moved.filter((it) => f >= rel(it.at) - 6 && f < land1(it) + 8).pop();
    const tLine = inFlight ? interpolate(f, [rel(inFlight.at), land1(inFlight)], [0, 1], {...cl, easing: Easing.inOut(Easing.cubic)}) : 0;
    const lineOp = inFlight ? ease(f, rel(inFlight.at) - 6, rel(inFlight.at)) * (1 - ease(f, land1(inFlight), land1(inFlight) + 8)) : 0;
    body = (
      <>
        <svg width={AW} height={bodyH} style={{position: 'absolute', left: 0, top: 0, overflow: 'visible'}}>
          <mask id="giao-duong" maskUnits="userSpaceOnUse" x={-AW} y={-bodyH} width={AW * 3} height={bodyH * 3}>   {/* đường dừng ở mép hai vòng tròn */}
            <rect x={-AW} y={-bodyH} width={AW * 3} height={bodyH * 3} fill="white" />
            <circle cx={xFrom} cy={cyN} r={ns / 2 + 8} fill="black" /><circle cx={xTo} cy={cyN} r={ns / 2 + 8} fill="black" />
          </mask>
          <g mask="url(#giao-duong)">
          <path d={curve} fill="none" stroke={C.dim} strokeWidth={3} strokeDasharray="4 14" strokeLinecap="round" opacity={0.8} />
          <path d={curve} pathLength={1} fill="none" stroke={C.accent} strokeWidth={5} strokeLinecap="round" strokeDasharray="1 1" strokeDashoffset={1 - uOf(tLine)} opacity={lineOp} />
          </g>
        </svg>
        {node(A, 0, false, 1, 1 - 0.45 * lighten)}
        {node(Z, xZ, true, bump)}
        {done.length > 0 && ripple < 1 && <div style={{position: 'absolute', left: xZ + ns / 2 - ns / 2, top: yN, width: ns, height: ns, borderRadius: ns, boxSizing: 'border-box',
          border: `4px solid ${C.accent}`, opacity: 0.7 * (1 - ripple), transform: `scale(${1 + 0.35 * ripple})`}} />}
        {moved.map((it, i) => {
          const a = rel(it.at);
          if (f < a - 6 || f >= a + TR) return null;
          const t = interpolate(f, [a, a + TR], [0, 1], {...cl, easing: Easing.inOut(Easing.cubic)}), [x, y] = pos(t), S = ns * 0.46;
          const scale = ease(f, a - 6, a, 0.55, 1) * interpolate(t, [0.72, 1], [1, 0.5], cl);   // nhô ra khỏi bên giao · thu nhỏ khi lọt vào bên nhận
          return (
            <div key={i} style={{position: 'absolute', left: x - S / 2, top: y - S / 2, width: S, height: S, borderRadius: S, boxSizing: 'border-box', background: C.accent,
              boxShadow: '0 14px 40px rgba(0,0,0,0.5)', opacity: ease(f, a - 6, a - 2) * (1 - ease(f, a + TR - 3, a + TR)), transform: `scale(${scale})`,
              display: 'flex', alignItems: 'center', justifyContent: 'center', color: C.bg}}>
              <div style={{filter: 'brightness(0)'}}><Icon name={it.icon} size={S * 0.62} at={-99} stroke={3.6} /></div>
            </div>
          );
        })}
        <div style={{position: 'absolute', left: xZ - ns * 0.1, width: ns * 1.2, top: yN + ns * 1.38, display: 'flex', justifyContent: 'center', gap: ns * 0.05}}>
          {done.map((it, i) => { const p = sp(land1(it)); return <div key={i} style={{opacity: Math.min(1, p * 1.4), transform: `scale(${0.6 + 0.4 * p})`}}><Icon name={it.icon} size={ns * 0.24} at={-99} stroke={4} /></div>; })}
        </div>
        {moved.map((it, i) => {   // tên việc: đổi bằng mờ nhoè ngắn, không đè lên nhau
          const next = moved[i + 1], o = ease(f, rel(it.at) - 6, rel(it.at) + 2) * (next ? 1 - ease(f, rel(next.at) - 8, rel(next.at) - 4) : 1);
          return o > 0 && <div key={i} style={{position: 'absolute', left: 0, width: AW, top: yN + ns * 1.74, textAlign: 'center', ...UP,
            fontSize: fit(it.label, AW * 0.92, M * (land ? 0.07 : 0.085)), color: C.text, opacity: o, filter: `blur(${(1 - o) * 8}px)`}}>{it.label}</div>;
        })}
      </>
    );
  } else if (mode === 'chuoi') {   // chuỗi bước: hiện theo lời, dây chạy từ bước trước tới, một chỗ sáng
    const n = Math.max(1, items.length), doc = !land || !nen;   // lồng trong bố cục (cạnh người / ô người) → xếp dọc cho vừa cột
    const gap = doc ? bodyH * 0.07 : AW * 0.05;
    const bw = doc ? Math.min(AW * 0.78, bodyH * (land ? 0.9 : 2)) : (AW - gap * (n - 1)) / n, bh = doc ? Math.min((bodyH - gap * (n - 1)) / n, bodyH * 0.2) : Math.min(bodyH * 0.5, bw * 0.62);
    const x0 = doc ? (AW - bw) / 2 : 0, y0 = doc ? (bodyH - (bh * n + gap * (n - 1))) / 2 : (bodyH - bh) / 2;
    const at = (i) => doc ? [x0, y0 + i * (bh + gap)] : [x0 + i * (bw + gap), y0];
    const RUN = 9;   // dây chạy ~0,3 s trước khi bước mới hiện
    const lines = items.slice(1).map((it, j) => {
      const i = j + 1, a = rel(it.at), t = interpolate(f, [a - RUN, a], [0, 1], {...cl, easing: Easing.inOut(Easing.cubic)});
      const [px, py] = at(i - 1), [qx, qy] = at(i);
      const A = doc ? [px + bw / 2, py + bh] : [px + bw, py + bh / 2], B = doc ? [qx + bw / 2, qy] : [qx, qy + bh / 2];
      const hx = A[0] + (B[0] - A[0]) * t, hy = A[1] + (B[1] - A[1]) * t, dot = M * 0.012, on = f >= a - RUN;
      return (
        <React.Fragment key={'l' + i}>
          <div style={{position: 'absolute', left: Math.min(A[0], B[0]) - (doc ? 2 : 0), top: Math.min(A[1], B[1]) - (doc ? 0 : 2),
            width: doc ? 4 : Math.abs(B[0] - A[0]), height: doc ? Math.abs(B[1] - A[1]) : 4, borderRadius: 2, background: C.line, opacity: f >= rel(items[i - 1].at) ? 1 : 0}} />
          <div style={{position: 'absolute', left: A[0] - (doc ? 2 : 0), top: A[1] - (doc ? 0 : 2), width: doc ? 4 : hx - A[0], height: doc ? hy - A[1] : 4,
            borderRadius: 2, background: C.accent, opacity: on ? 1 : 0}} />
          {on && t < 1 && <div style={{position: 'absolute', left: hx - dot, top: hy - dot, width: dot * 2, height: dot * 2, borderRadius: dot,
            background: C.accent, boxShadow: `0 0 ${dot * 3}px ${C.accent}`}} />}
        </React.Fragment>
      );
    });
    const boxes = items.map((it, i) => {
      const a = rel(it.at), p = sp(a), cur = i === curI, cu = i < curI, [x, y] = at(i);
      const fsz = fit(it.label, bw * (it.icon ? 0.62 : 0.86), Math.min(bh * 0.36, M * (land ? 0.05 : 0.065)));
      return (
        <div key={i} style={{position: 'absolute', left: x, top: y, width: bw, height: bh, borderRadius: Math.min(bh, bw) * 0.18, boxSizing: 'border-box',
          background: cur ? C.accentSoft : C.card, border: `${cur ? 3 : 2}px solid ${cur ? C.accent : C.line}`,
          boxShadow: cur ? `0 0 ${M * 0.05}px rgba(255,122,69,0.28)` : '0 20px 60px rgba(0,0,0,0.45)',
          display: 'flex', alignItems: 'center', justifyContent: 'center', gap: bh * 0.18, padding: `0 ${bh * 0.2}px`,
          opacity: Math.min(1, p * 1.4) * (cu ? 0.5 : 1), transform: `translateY(${(1 - p) * bh * 0.25}px) scale(${0.94 + 0.06 * p})`}}>
          {it.icon && <div style={{flex: 'none'}}><Icon name={it.icon} size={bh * 0.48} at={a} stroke={3} /></div>}
          <div style={{...UP, fontSize: fsz, color: cur ? C.text : cu ? C.muted : C.text, whiteSpace: 'nowrap'}}>{it.label}</div>
        </div>
      );
    });
    body = <>{lines}{boxes}</>;
  } else if (mode === 'anh') {   // ẢNH THẬT trong khung bo góc + nhãn + nguồn
    const it = items[0] || {}, p = sp(rel(it.at));
    const ph = bodyH * (it.label ? 0.8 : 0.95), pw = Math.min(AW * 0.9, ph * (it.ratio || (land ? 16 / 9 : 4 / 3))), x = (AW - pw) / 2;   // it.ratio: 3/4 cho chân dung
    const kb = 1;   // không zoom ảnh (13/11/2026 — David: bỏ zoom vào / ra)
    body = (
      <>
        <div style={{position: 'absolute', left: x, top: 0, width: pw, height: ph, borderRadius: M * 0.035, overflow: 'hidden',
          boxShadow: `0 30px 80px rgba(0,0,0,0.55), 0 0 0 3px ${C.accent}55`, opacity: Math.min(1, p * 1.3), transform: `scale(${0.92 + 0.08 * p})`}}>
          {it.photo && <Img src={staticFile(`anh/${it.photo}`)} style={{width: '100%', height: '100%', objectFit: 'cover', objectPosition: it.pos || '50% 35%', transform: `scale(${kb})`}} />}
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
      {nen && (usePhong().phong ? <NenPhong glow={false} /> : <AbsoluteFill style={{background: C.bg}} />)}
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
