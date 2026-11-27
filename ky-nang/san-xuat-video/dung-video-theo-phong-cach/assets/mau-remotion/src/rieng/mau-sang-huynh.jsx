// MẪU SANG HUỲNH + KHO HIỆU ỨNG AISLOP (27/11/2026) — 10 cách đã học trong `thiet-ke-bo-cuc/nguon-tham-khao/sang-huynh-claude-do-hoa-2026-11-07.md`
// mà trước đây "chưa có code". Dùng khi tái dựng theo đúng mẫu (thiet-ke-bo-cuc/README.md mục 4a) hoặc khi lời có đúng dấu hiệu ở bảng 4c.
// Màu, nhịp đo từ video mẫu (bảng khung 0,67 giây) và từ mã gốc của tác giả (aislop.vn/bo-hieu-ung/<tên>/template.txt, GSAP).
// Trong bản tái dựng giữ thẩm mỹ của mẫu (README mục 4a); dựng thường thì đổi `M` sang màu kênh (C) trước khi dùng.
// Mọi mốc `at` là GIÂY TUYỆT ĐỐI trong video gốc của dự án (như các cảnh khác); chữ là nguyên văn lời người nói.
//   ToaNhanh    điểm sáng, nhiều đường toả ra, nét đậm cho đường được chọn (mẫu 05:00)
//   HoiTu       hai đầu vào hội tụ vào công cụ rồi đi xuống đầu ra (mẫu 01:36, flowchart-highlight)
//   SoVang      số lớn có lớp chữ viền lặp + thanh (echo-number; mẫu 00:59)
//   SoiSang     làm tối màn hình, viền sáng vẽ quanh vùng, nhãn + đường chỉ (spotlight-magnifier)
//   GoLenh      thẻ câu lệnh gõ từng chữ trên màn hình làm tối (mẫu 02:45)
//   HangThe     hàng thẻ trên nền tối, thẻ đang nói sáng, nhãn "làm từ" dưới thẻ (mẫu 00:10)
//   HaiThe      hai thẻ trắng cạnh nhau trên nền kem, lần lượt tiết lộ (mẫu 15:50)
//   TheChao     thẻ chào chữ đậm hai tầng cạnh người (mẫu 18:49)
//   NguoiTrongThe chuỗi bước, một thẻ chứa chính video người nói (mẫu bố cục 3)
//   TheDocToi   thẻ dọc tối cạnh người, hình thu nhỏ và nhãn tăng dần (mẫu 00:28)
import React from 'react';
import {AbsoluteFill, Easing, Img, OffthreadVideo, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {BODY, HEAD, rel} from '../chu-de';
import {fr} from '../canh';

export const M = {   // màu đo từ mẫu
  toi: '#161616', toi2: '#262626', the: '#1E1E1E', vien: 'rgba(255,255,255,0.10)', kem: '#EDEBE6', trang: '#FFFFFF',
  nhan: '#E0664B', xanh: '#2FA84F', sang: '#F4EFE6', chu: '#16181D', mo: '#8D8D8D',
  navy: '#0B1426', navy2: '#04070F', vang: '#E3B25B', vang2: '#F5D28A',   // spotlight-magnifier (theme navy-gold của tác giả)
};
const MONO = 'JetBrains Mono, Menlo, monospace';
const kep = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'};
const ea = (f, a, b, e = Easing.out(Easing.cubic), from = 0, to = 1) => interpolate(f, [a, b], [from, to], {...kep, easing: e});
const EXPO = Easing.out(Easing.exp), BACK = Easing.out(Easing.back(1.6)), IO = Easing.inOut(Easing.quad), P3 = Easing.out(Easing.poly(3));
const rr = (f, at, start) => f - rel(at ?? start, start);   // số khung đã qua kể từ mốc
const nenToi = {background: `radial-gradient(ellipse 80% 70% at 50% 40%, ${M.toi2}, ${M.toi})`};
const nenKem = {background: `radial-gradient(ellipse 80% 70% at 50% 30%, #F6F5F2, ${M.kem})`};
// `*từ*` thành chữ màu nhấn (mẫu dùng cùng font, chỉ đổi màu)
const Hai = ({text = '', mau = M.nhan}) => <>{String(text).split(/(\*[^*]+\*)/).map((p, i) =>
  p.startsWith('*') ? <span key={i} style={{color: mau}}>{p.slice(1, -1)}</span> : <span key={i}>{p}</span>)}</>;
// chữ hiện theo từng từ (mờ + trượt), mốc riêng
const TuTu = ({text, f0, buoc = 3}) => <>{String(text).split(/(\s+)/).map((w, i) => {
  if (/^\s+$/.test(w)) return w;
  const k = ea(f0 - i * buoc / 2, 0, 8, EXPO);
  const nhan = w.includes('*');
  return <span key={i} style={{display: 'inline-block', opacity: k, transform: `translateY(${(1 - k) * 10}px)`, color: nhan ? M.nhan : undefined}}>{w.replace(/\*/g, '')}</span>;
})}</>;
const raCanh = (f, d) => ea(f, d - 9, d, Easing.in(Easing.cubic), 1, 0);
const Goc = ({start, tu, style}) => <OffthreadVideo src={staticFile('goc.mp4')} trimBefore={fr(tu ?? start)} muted
  style={{width: '100%', height: '100%', objectFit: 'cover', ...style}} />;
const Hinh = ({nguon, start}) => {
  if (!nguon) return null;
  if (nguon.photo) return <Img src={staticFile(`anh/${nguon.photo}`)} style={{width: '100%', height: '100%', objectFit: 'cover', objectPosition: nguon.pos || '50% 50%'}} />;
  if (nguon.video) return <Goc start={start} tu={nguon.tu} style={{objectPosition: nguon.pos || '50% 50%'}} />;
  return null;
};

// ───────────────── 1. Toả nhánh (mẫu 05:00–05:10) ─────────────────
// {nho, tieu_de, goc, nhanh:[{text, at}], chon:{text, at}, dung:{text, at}, chenh:{text, at}}
export const ToaNhanh = ({start, nho, tieu_de, tieu_at, goc, nhanh = [], chon, dung, chenh}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d, width: W, height: H} = useVideoConfig();
  const x0 = 0.17 * W, y0 = 0.56 * H, x1 = 0.62 * W;
  const n = nhanh.length;
  const yi = (i) => H * (0.27 + (0.55 * i) / Math.max(1, n - 1));
  const duong = (xa, ya, xb, yb) => `M${xa},${ya} C${xa + 0.22 * W},${ya} ${xb - 0.22 * W},${yb} ${xb},${yb}`;
  const ve = (at, dai = 20) => ea(rr(f, at, start), 0, dai, IO);
  const mo = chon ? ea(rr(f, chon.at, start), 0, 10) : 0;
  const kt = H * 0.019;
  const xc = 0.7 * W, yc = 0.88 * H, yd = 0.17 * H;
  return (
    <AbsoluteFill style={{...nenToi, opacity: Math.min(ea(f, 0, 8), raCanh(f, d))}}>
      {nho && <div style={{position: 'absolute', left: 0.05 * W, top: 0.07 * H, fontFamily: BODY, fontWeight: 800, fontSize: H * 0.022,
        letterSpacing: 2, color: M.nhan, textTransform: 'uppercase'}}><TuTu text={nho} f0={f} /></div>}
      {tieu_de && <div style={{position: 'absolute', left: 0.05 * W, top: 0.105 * H, fontFamily: HEAD, fontWeight: 800, fontSize: H * 0.07,
        color: M.sang, textTransform: 'uppercase', lineHeight: 1}}><TuTu text={tieu_de} f0={rr(f, tieu_at, start)} buoc={5} /></div>}
      <svg width={W} height={H} style={{position: 'absolute', inset: 0}}>
        {nhanh.map((b, i) => <path key={i} d={duong(x0, y0, x1, yi(i))} pathLength={1} strokeDasharray="1 1" strokeDashoffset={1 - ve(b.at)}
          fill="none" stroke="rgba(255,255,255,0.32)" strokeWidth={2} opacity={1 - 0.7 * mo} />)}
        {chon && <path d={duong(x0, y0, xc, yc)} pathLength={1} strokeDasharray="1 1" strokeDashoffset={1 - ve(chon.at, 32)} fill="none" stroke={M.nhan} strokeWidth={4} />}
        {dung && <path d={duong(x0, y0, xc, yd)} pathLength={1} strokeDasharray="1 1" strokeDashoffset={1 - ve(dung.at, 32)} fill="none" stroke={M.sang} strokeWidth={4} />}
        {chenh && <line x1={xc} y1={yd + 0.04 * H} x2={xc} y2={yc - 0.04 * H} stroke={M.nhan} strokeWidth={2} strokeDasharray="8 8"
          opacity={ve(chenh.at, 14)} />}
      </svg>
      <div style={{position: 'absolute', left: x0 - kt * 0.9, top: y0 - kt * 0.9, width: kt * 1.8, height: kt * 1.8, borderRadius: '50%',
        background: M.nhan, boxShadow: `0 0 ${kt * 1.6}px ${M.nhan}`, transform: `scale(${ea(f, 2, 14, BACK)})`}} />
      {goc && <div style={{position: 'absolute', left: x0 - 0.1 * W, width: 0.2 * W, top: y0 + kt * 1.4, textAlign: 'center', fontFamily: BODY,
        fontWeight: 700, fontSize: kt * 1.1, color: M.nhan, opacity: ea(f, 6, 16)}}>{goc}</div>}
      {nhanh.map((b, i) => <div key={i} style={{position: 'absolute', left: x1 + kt, top: yi(i) - kt * 0.8, fontFamily: MONO, fontSize: kt * 1.05,
        color: M.mo, opacity: ea(rr(f, b.at, start), 14, 22) * (1 - 0.7 * mo), whiteSpace: 'nowrap'}}>{b.text}</div>)}
      {[[chon, yc, M.nhan, '✕'], [dung, yd, M.xanh, '✓']].map(([o, y, mau, dau], i) => o && (
        <div key={i} style={{position: 'absolute', left: xc - kt * 0.9, top: y - kt * 0.9, display: 'flex', alignItems: 'center', gap: kt * 0.6,
          opacity: ea(rr(f, o.at, start), 26, 34), transform: `scale(${ea(rr(f, o.at, start), 26, 38, BACK, 0.6, 1)})`, transformOrigin: 'left center'}}>
          <div style={{width: kt * 1.8, height: kt * 1.8, borderRadius: '50%', background: mau, color: '#fff', display: 'flex', alignItems: 'center',
            justifyContent: 'center', fontSize: kt * 1.1, fontWeight: 800}}>{dau}</div>
          <div style={{fontFamily: BODY, fontWeight: 700, fontSize: kt * 1.25, color: M.sang, whiteSpace: 'nowrap'}}>{o.text}</div></div>))}
      {chenh && <div style={{position: 'absolute', left: xc + kt * 1.4, top: (yd + yc) / 2 - H * 0.035, fontFamily: HEAD, fontWeight: 800,
        fontSize: H * 0.06, color: M.nhan, textTransform: 'uppercase', opacity: ea(rr(f, chenh.at, start), 8, 16), whiteSpace: 'nowrap'}}>{chenh.text}</div>}
    </AbsoluteFill>
  );
};

// ───────────────── 2. Hội tụ (mẫu 01:36–01:41 · flowchart-highlight) ─────────────────
// {nho, vao:[{text, at}], giua:{text, at}, nhan:{text, at}, ra:{text, at, dau_at}, ben:{text, phu, at}}
export const HoiTu = ({start, nho, vao = [], giua, nhan, ra, ben}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d, width: W, height: H} = useVideoConfig();
  const kt = H * 0.022, cx = 0.5 * W, yv = 0.2 * H, yg = 0.44 * H, yr = 0.72 * H;
  const xv = (i) => cx + (i - (vao.length - 1) / 2) * 0.17 * W;
  const chip = (text, x, y, k, extra = {}) => (
    <div style={{position: 'absolute', left: x, top: y, transform: `translate(-50%,-50%) translateY(${(1 - k) * 14}px) scale(${0.94 + 0.06 * k})`, opacity: k,
      background: M.the, border: `1.5px solid ${M.vien}`, borderRadius: kt * 0.5, padding: `${kt * 0.55}px ${kt * 0.9}px`, fontFamily: BODY,
      fontWeight: 700, fontSize: kt * 1.15, color: M.sang, whiteSpace: 'nowrap', boxShadow: '0 12px 30px rgba(0,0,0,0.45)', ...extra}}>{text}</div>);
  const kg = giua ? ea(rr(f, giua.at, start), 0, 16, EXPO) : 0;
  const kn = nhan ? ea(rr(f, nhan.at, start), 0, 14, IO) : 0;
  const kr = ra ? ea(rr(f, ra.at, start), 0, 14, BACK) : 0;
  const kd = ra?.dau_at != null ? ea(rr(f, ra.dau_at, start), 0, 10, BACK) : 0;
  return (
    <AbsoluteFill style={{...nenToi, opacity: Math.min(ea(f, 0, 8), raCanh(f, d))}}>
      {nho && <div style={{position: 'absolute', left: 0.05 * W, top: 0.07 * H, fontFamily: BODY, fontWeight: 800, fontSize: H * 0.022,
        letterSpacing: 2, color: M.nhan, textTransform: 'uppercase'}}>{nho}</div>}
      <svg width={W} height={H} style={{position: 'absolute', inset: 0}}>
        {giua && vao.map((v, i) => <path key={i} d={`M${xv(i)},${yv + kt} C${xv(i)},${(yv + yg) / 2} ${cx},${(yv + yg) / 2 - 10} ${cx},${yg - kt}`}
          pathLength={1} strokeDasharray="1 1" strokeDashoffset={1 - ea(rr(f, giua.at, start), -10 + i * 2, 8 + i * 2, IO)}
          fill="none" stroke="rgba(255,255,255,0.35)" strokeWidth={2} />)}
        {nhan && <line x1={cx} y1={yg + kt * 1.2} x2={cx} y2={yg + kt * 1.2 + (yr - yg - kt * 2.6) * kn} stroke={M.nhan} strokeWidth={3} />}
      </svg>
      {vao.map((v, i) => chip(v.text, xv(i), yv, ea(rr(f, v.at, start), 0, 14, EXPO)))}
      {giua && chip(giua.text, cx, yg, kg)}
      {nhan && <div style={{position: 'absolute', left: cx + kt * 0.8, top: (yg + yr) / 2 - kt * 0.7, fontFamily: BODY, fontWeight: 700,
        fontSize: kt * 1.05, color: M.nhan, opacity: ea(rr(f, nhan.at, start), 8, 16)}}>{nhan.text}</div>}
      {ra && <div style={{position: 'absolute', left: cx, top: yr, transform: `translate(-50%,-50%) scale(${0.85 + 0.15 * kr})`, opacity: Math.min(1, kr * 1.4),
        background: M.trang, borderRadius: kt * 0.5, padding: `${kt * 0.7}px ${kt * 1.3}px`, display: 'flex', alignItems: 'center', gap: kt * 0.6,
        fontFamily: HEAD, fontWeight: 800, fontSize: kt * 1.9, color: M.chu, boxShadow: '0 16px 40px rgba(0,0,0,0.5)', whiteSpace: 'nowrap'}}>
        {ra.text}{ra.dau_at != null && <span style={{display: 'inline-flex', width: kt * 1.5, height: kt * 1.5, borderRadius: '50%', background: M.xanh,
          color: '#fff', fontSize: kt, alignItems: 'center', justifyContent: 'center', transform: `scale(${kd})`}}>✓</span>}</div>}
      {ben && (() => { const k = ea(rr(f, ben.at, start), 0, 12); return (
        <div style={{position: 'absolute', left: 0.73 * W, top: yr, transform: 'translateY(-50%)', opacity: 0.55 * k, background: M.the,
          border: `1.5px solid ${M.vien}`, borderRadius: kt * 0.5, padding: `${kt * 0.45}px ${kt * 0.8}px`, fontFamily: BODY}}>
          <div style={{fontWeight: 700, fontSize: kt, color: M.sang, textDecoration: 'line-through'}}>{ben.text}</div>
          {ben.phu && <div style={{fontSize: kt * 0.75, color: M.mo}}>{ben.phu}</div>}</div>); })()}
    </AbsoluteFill>
  );
};

// ───────────────── 3. Số vang (echo-number, mã tác giả 3,8 giây) + thanh (mẫu 00:59) ─────────────────
// {nhan, so, at, phu, thanh: {tu: 0–1, den: 0–1, at, dai giây}, nguoi: {pos}} — nửa phải là chính video người nói
export const SoVang = ({start, nhan, so, at, phu, thanh, nguoi = {}}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d, width: W, height: H, fps} = useVideoConfig();
  const s = W / 1920, t = (x) => fr(x);   // mốc tác giả tính bằng giây
  const g = rr(f, at, start);
  const the = {x: 75 * s, y: 243 * s * (H / W) / (1080 / 1920), w: 1062 * s, h: 592 * s};
  const kCard = ea(g, t(0.05), t(0.85), EXPO), kMain = ea(g, t(0.3), t(0.9), BACK), kKick = ea(g, t(0.6), t(1.1), EXPO);
  const vang = [[0.69, -336, 0.13], [0.57, -224, 0.2], [0.45, -112, 0.27], [0.45, 112, 0.27], [0.57, 224, 0.2], [0.69, 336, 0.13]];
  const troi = interpolate(f, [0, d], [0, -46 * s], kep);
  const kThanh = thanh ? ea(rr(f, thanh.at, start), 0, (thanh.dai ?? 1.2) * fps, IO) : 0;
  const muc = thanh ? thanh.tu + (thanh.den - thanh.tu) * kThanh : 0;
  const line = {position: 'absolute', left: 0, right: 0, top: '50%', marginTop: -58 * s, height: 130 * s, lineHeight: `${130 * s}px`,
    textAlign: 'center', fontFamily: HEAD, fontWeight: 900, fontSize: 112 * s, letterSpacing: '-0.02em', whiteSpace: 'nowrap'};
  return (
    <AbsoluteFill style={{background: 'linear-gradient(#f4f4f5, #e7e7e9)', opacity: Math.min(ea(f, 0, 6), raCanh(f, d))}}>
      <div style={{position: 'absolute', left: 1220 * s, top: 0, right: 0, bottom: 0, overflow: 'hidden', background: '#1d1e21'}}>
        <Goc start={start} style={{objectPosition: nguoi.pos || '50% 50%'}} /></div>
      <div style={{position: 'absolute', left: the.x, top: (H - the.h) / 2, width: the.w, height: the.h, borderRadius: 22 * s, overflow: 'hidden',
        background: 'radial-gradient(ellipse at 80% 15%, #dfe7ff 0%, #f7f9ff 45%, #ffffff 100%)',
        boxShadow: '0 30px 60px rgba(20,30,60,.22), inset 0 2px 0 rgba(255,255,255,.8)',
        transform: `translateY(${(1 - kCard) * 40 * s}px) scale(${0.96 + 0.04 * kCard})`, opacity: Math.min(1, kCard * 2)}}>
        {nhan && <div style={{position: 'absolute', left: 40 * s, top: 34 * s, zIndex: 2, fontFamily: BODY, fontSize: 28 * s, fontWeight: 800, color: '#2f3548',
          padding: `${8 * s}px ${20 * s}px`, borderRadius: 999, background: 'rgba(255,255,255,.92)', boxShadow: '0 6px 18px rgba(30,40,80,.12)',
          opacity: kKick, transform: `translateX(${(1 - kKick) * -16 * s}px)`}}>{nhan}</div>}
        <div style={{position: 'absolute', inset: 0, transform: `translateY(${troi}px)`,
          WebkitMaskImage: 'linear-gradient(transparent 0%, #000 22%, #000 78%, transparent 100%)'}}>
          {vang.map(([a, dy, al], i) => { const k = ea(g, t(a), t(a + 0.9), EXPO); return (
            <div key={i} style={{...line, color: 'transparent', WebkitTextStroke: `2px rgba(61,107,255,${al})`, opacity: k,
              transform: `translateY(${dy * s * k}px)`}}>{so}</div>); })}
          <div style={{...line, background: 'linear-gradient(rgba(61,107,255,0.78), #3D6BFF)', WebkitBackgroundClip: 'text', color: 'transparent',
            filter: 'drop-shadow(0 10px 22px rgba(61,107,255,0.28))', opacity: kMain, transform: `scale(${0.8 + 0.2 * kMain})`}}>{so}</div>
        </div>
        {phu && <div style={{position: 'absolute', left: 0, right: 0, bottom: thanh ? 96 * s : 48 * s, textAlign: 'center', fontFamily: BODY, fontWeight: 700,
          fontSize: 30 * s, color: '#2f3548', opacity: ea(g, t(0.9), t(1.4))}}>{phu}</div>}
        {thanh && <div style={{position: 'absolute', left: 60 * s, right: 60 * s, bottom: 52 * s, height: 14 * s, borderRadius: 99, background: '#e3e6ef'}}>
          <div style={{width: `${muc * 100}%`, height: '100%', borderRadius: 99, background: '#3D6BFF'}} /></div>}
      </div>
    </AbsoluteFill>
  );
};

// ───────────────── 4. Soi sáng (spotlight-magnifier, mã tác giả 10 giây, theme navy-gold) ─────────────────
// {vung:[{x, y, w, h (phần trăm của khung chụp), at, nhan, nx, ny (vị trí nhãn, phần trăm)}], zoom: 1.3}
export const SoiSang = ({start, vung = [], zoom = 1.3}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d, width: W, height: H} = useVideoConfig();
  const s = W / 1920, t = (x) => fr(x);
  const shot = {x: 100 * s, y: 110 * s * (H / W) / (1080 / 1920), w: 1720 * s, h: 860 * s};
  const kShot = ea(f, t(0.1), t(1.0), EXPO);
  // vùng đang bật: theo mốc tác giả (bật t, đóng t + 3,75 giây)
  const g = vung.map((v) => rr(f, v.at, start));
  const dang = g.findIndex((x) => x >= 0 && x < t(3.9));
  const v = vung[dang], q = dang >= 0 ? g[dang] : -1;
  const kDim = v ? Math.min(ea(q, 0, t(0.6), IO), ea(q, t(3.4), t(4.0), IO, 1, 0)) : 0;
  const kRing = v ? Math.min(ea(q, t(0.05), t(0.5), IO), ea(q, t(3.35), t(3.75), IO, 1, 0)) : 0;
  const kZoom = v ? Math.min(ea(q, t(0.3), t(0.8), P3), ea(q, t(3.3), t(3.75), IO, 1, 0)) : 0;
  const kLab = v ? Math.min(ea(q, t(0.05), t(0.35), P3), ea(q, t(3.5), t(3.75), Easing.in(Easing.quad), 1, 0)) : 0;
  const kPtr = v ? Math.min(ea(q, t(0.55), t(1.05)), ea(q, t(2.95), t(3.25), IO, 1, 0)) : 0;
  const kDot = v ? Math.min(ea(q, t(1.0), t(1.3), Easing.out(Easing.back(2.4))), ea(q, t(2.9), t(3.1), Easing.in(Easing.quad), 1, 0)) : 0;
  const R = v && {x: v.x / 100 * shot.w, y: v.y / 100 * shot.h, w: v.w / 100 * shot.w, h: v.h / 100 * shot.h};
  const sc = 1 + (zoom - 1) * kZoom;
  const tf = R ? `translate(${R.x + R.w / 2}px,${R.y + R.h / 2}px) scale(${sc}) translate(${-(R.x + R.w / 2)}px,${-(R.y + R.h / 2)}px)` : undefined;
  const L = v && {x: (v.nx ?? 7) / 100 * shot.w, y: (v.ny ?? 30) / 100 * shot.h};
  const nk = v ? [...String(v.nhan || '')] : [];
  return (
    <AbsoluteFill style={{background: `radial-gradient(ellipse 75% 70% at 50% 50%, ${M.navy}, ${M.navy2})`, opacity: Math.min(ea(f, 0, 6), raCanh(f, d))}}>
      <div style={{position: 'absolute', inset: 0, opacity: ea(f, 0, t(1)) * 0.7 + 0.3,
        backgroundImage: 'radial-gradient(circle, rgba(227,178,91,.5) 1.6px, transparent 1.6px)', backgroundSize: '90px 90px', backgroundPosition: '30px 20px',
        WebkitMaskImage: 'radial-gradient(ellipse 80% 75% at 50% 50%, transparent 45%, #000 100%)'}} />
      <div style={{position: 'absolute', left: shot.x, top: (H - shot.h) / 2, width: shot.w, height: shot.h,
        transform: `translateY(${(1 - kShot) * 26 * s}px) scale(${0.965 + 0.035 * kShot})`, opacity: 0.6 + 0.4 * kShot}}>
        <div style={{position: 'absolute', inset: 0, borderRadius: 16 * s, overflow: 'hidden', background: '#FBFBFA', boxShadow: '0 30px 80px rgba(0,0,0,.55)'}}>
          <div style={{position: 'absolute', inset: 0, filter: kDim > 0 ? `blur(${7 * kDim}px) saturate(${1 - 0.85 * kDim}) brightness(${1 - 0.5 * kDim})` : undefined}}>
            <Goc start={start} /></div>
        </div>
        {R && <div style={{position: 'absolute', inset: 0, transform: tf, opacity: kRing > 0 ? 1 : 0,
          clipPath: `inset(${R.y}px ${shot.w - R.x - R.w}px ${shot.h - R.y - R.h}px ${R.x}px round ${10 * s}px)`}}>
          <div style={{position: 'absolute', inset: 0, borderRadius: 16 * s, overflow: 'hidden'}}><Goc start={start} /></div></div>}
        {R && <svg width={shot.w} height={shot.h} style={{position: 'absolute', inset: 0, overflow: 'visible', transform: tf,
          filter: 'drop-shadow(0 0 12px rgba(227,178,91,.7)) drop-shadow(0 0 34px rgba(227,178,91,.35))'}}>
          <rect x={R.x} y={R.y} width={R.w} height={R.h} rx={12 * s} pathLength={1} strokeDasharray="1 1" strokeDashoffset={1 - kRing}
            fill="none" stroke={M.vang} strokeWidth={5 / sc} strokeLinecap="round" /></svg>}
        {R && <svg width={shot.w} height={shot.h} style={{position: 'absolute', inset: 0, overflow: 'visible'}}>
          <path d={`M${L.x + 40 * s},${L.y + 110 * s} L${R.x + R.w / 2 - R.w / 2 * sc},${R.y + R.h / 2}`} pathLength={1} strokeDasharray="1 1"
            strokeDashoffset={1 - kPtr} stroke={M.chu} strokeWidth={3} strokeLinecap="round" fill="none" />
          <circle cx={R.x + R.w / 2 - R.w / 2 * sc} cy={R.y + R.h / 2} r={15 * s * kDot} fill={M.chu} stroke="#fff" strokeWidth={3} opacity={kDot} /></svg>}
        {v && <div style={{position: 'absolute', left: L.x, top: L.y, background: '#fff', color: '#14171C', fontFamily: BODY, fontWeight: 600, fontSize: 42 * s,
          letterSpacing: '-.005em', lineHeight: 1, padding: `${34 * s}px ${40 * s}px`, borderRadius: 16 * s, boxShadow: '0 14px 40px rgba(0,0,0,.35)',
          transform: `scaleY(${0.05 + 0.95 * kLab})`, transformOrigin: 'left top', opacity: kLab, maxWidth: shot.w * 0.5}}>
          {nk.map((c, i) => { const k = ea(q - t(0.3) - (i * t(0.55)) / nk.length, 0, t(0.25)); return (
            <span key={i} style={{opacity: k, filter: k < 1 ? `blur(${5 * (1 - k)}px)` : undefined, display: 'inline-block', whiteSpace: 'pre',
              transform: `translateX(${(1 - k) * -6}px)`}}>{c}</span>); })}</div>}
      </div>
    </AbsoluteFill>
  );
};

// ───────────────── 5. Gõ lệnh (mẫu 02:45–02:54) ─────────────────
// {nhan: 'Prompt', text, at, toc (chữ mỗi giây), chu_thich: {text, phu}, goc_phai}
export const GoLenh = ({start, nhan = 'PROMPT', text = '', at, toc = 14, chu_thich, goc_phai}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d, width: W, height: H, fps} = useVideoConfig();
  const kt = H * 0.022, g = rr(f, at, start), kThe = ea(g, -6, 8, EXPO);
  const n = Math.max(0, Math.floor((g / fps) * toc)), hien = [...text].slice(0, n).join('');
  return (
    <AbsoluteFill style={{background: '#0d0d0d', opacity: Math.min(ea(f, 0, 6), raCanh(f, d))}}>
      <div style={{position: 'absolute', left: 0.03 * W, top: 0.025 * H, width: 0.94 * W, height: 0.86 * H, borderRadius: kt * 0.6, overflow: 'hidden'}}>
        <div style={{position: 'absolute', inset: 0, filter: `brightness(${1 - 0.6 * kThe}) blur(${3 * kThe}px)`}}><Goc start={start} /></div>
        <div style={{position: 'absolute', left: '12%', right: '12%', top: '22%', minHeight: '26%', background: '#2A2826', borderRadius: kt * 0.8,
          border: `1.5px solid ${M.vien}`, padding: kt * 1.6, boxSizing: 'border-box', boxShadow: '0 24px 70px rgba(0,0,0,.6)', opacity: kThe,
          transform: `translateY(${(1 - kThe) * 20}px) scale(${0.97 + 0.03 * kThe})`}}>
          <div style={{display: 'flex', alignItems: 'center', gap: kt * 0.5, fontFamily: MONO, fontSize: kt * 0.8, color: M.mo, letterSpacing: 2}}>
            <span style={{width: kt * 0.8, height: kt * 0.8, borderRadius: 4, background: M.nhan}} />{nhan.toUpperCase()}</div>
          <div style={{marginTop: kt * 1.1, fontFamily: BODY, fontWeight: 700, fontSize: kt * 1.7, color: M.sang, lineHeight: 1.35}}>
            {hien}<span style={{opacity: n < text.length && Math.floor(f / 8) % 2 === 0 ? 1 : 0, color: M.nhan}}>▍</span></div>
        </div>
        {goc_phai && <div style={{position: 'absolute', right: kt, top: kt, background: '#1b1b1b', color: M.sang, fontFamily: BODY, fontWeight: 600,
          fontSize: kt * 0.8, padding: `${kt * 0.35}px ${kt * 0.7}px`, borderRadius: 99, opacity: ea(g, 20, 30)}}>{goc_phai}</div>}
      </div>
      {chu_thich && <div style={{position: 'absolute', left: 0.03 * W, top: 0.905 * H, display: 'flex', alignItems: 'center', gap: kt * 0.6,
        fontFamily: BODY, fontSize: kt, opacity: ea(f, 4, 14)}}>
        <span style={{width: kt * 1.1, height: kt * 1.1, borderRadius: '50%', background: M.nhan}} />
        <b style={{color: M.sang}}>{chu_thich.text}</b><span style={{color: M.mo}}>{chu_thich.phu}</span></div>}
    </AbsoluteFill>
  );
};

// ───────────────── 6. Hàng thẻ (mẫu 00:10–00:18) ─────────────────
// {nho, the:[{hinh: {photo}|{video, tu}|null, chu, at, sang_tu, nhan, nhan_at}], lon: {text, at}}
export const HangThe = ({start, nho, nho_at, the = [], lon}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d, width: W, height: H} = useVideoConfig();
  const n = the.length, gap = 0.012 * W, w = Math.min(0.26 * W, (0.9 * W - gap * (n - 1)) / n), h = w * 0.56;
  const x0 = (W - (n * w + (n - 1) * gap)) / 2, y = lon ? 0.4 * H : 0.33 * H, kt = H * 0.02;
  const dangSang = the.reduce((a, t2, i) => (t2.sang_tu != null && rr(f, t2.sang_tu, start) >= 0 ? i : a), -1);
  return (
    <AbsoluteFill style={{...nenToi, opacity: Math.min(ea(f, 0, 8), raCanh(f, d))}}>
      {nho && <div style={{position: 'absolute', left: 0, right: 0, top: y - 0.13 * H, textAlign: 'center', fontFamily: BODY, fontWeight: 600,
        fontSize: kt * 1.05, color: M.mo}}><TuTu text={nho} f0={rr(f, nho_at, start)} /></div>}
      {the.map((t2, i) => {
        const k = ea(rr(f, t2.at, start), 0, 14, EXPO), sang = dangSang < 0 || dangSang === i;
        const kn = t2.nhan ? ea(rr(f, t2.nhan_at ?? t2.at, start), 0, 12, EXPO) : 0;
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: x0 + i * (w + gap), top: y, width: w, height: h, borderRadius: kt * 0.5, overflow: 'hidden',
              background: M.the, border: `2px solid ${sang && dangSang >= 0 ? M.nhan : M.vien}`,
              boxShadow: sang && dangSang >= 0 ? `0 0 ${kt * 1.6}px rgba(224,102,75,.45)` : '0 14px 36px rgba(0,0,0,.5)',
              opacity: k * (sang ? 1 : 0.45), transform: `translateY(${(1 - k) * 24}px) scale(${0.95 + 0.05 * k})`}}>
              <Hinh nguon={t2.hinh} start={start} />
              {t2.chu && <div style={{position: 'absolute', inset: 0, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: kt,
                textAlign: 'center', fontFamily: HEAD, fontWeight: 800, fontSize: kt * 1.6, color: M.sang, textTransform: 'uppercase', lineHeight: 1.05}}>{t2.chu}</div>}
            </div>
            {t2.nhan && <div style={{position: 'absolute', left: x0 + i * (w + gap) + w / 2, top: y + h + kt * 1.1, transform: `translateX(-50%) translateY(${(1 - kn) * 10}px)`,
              opacity: kn * (sang ? 1 : 0.55), background: '#1b1b1b', border: `1.5px solid ${M.vien}`, borderRadius: 99, padding: `${kt * 0.35}px ${kt * 0.9}px`,
              whiteSpace: 'nowrap', fontFamily: BODY}}>
              <span style={{fontSize: kt * 0.62, color: M.nhan, fontWeight: 800, letterSpacing: 1.5, marginRight: kt * 0.5}}>LÀM TỪ</span>
              <span style={{fontSize: kt * 0.95, color: M.sang, fontWeight: 700}}>{t2.nhan}</span></div>}
          </React.Fragment>);
      })}
      {lon && <div style={{position: 'absolute', left: 0, right: 0, top: y - 0.1 * H, textAlign: 'center', fontFamily: HEAD, fontWeight: 800,
        fontSize: H * 0.075, color: M.sang, textTransform: 'uppercase'}}><TuTu text={lon.text} f0={rr(f, lon.at, start)} buoc={5} /></div>}
    </AbsoluteFill>
  );
};

// ───────────────── 7. Hai thẻ (mẫu 15:50–15:56) ─────────────────
// {dau: {text, at}, the:[{hinh, tag, lon, so, sau_so, phu, at}]}
export const HaiThe = ({start, dau, the = []}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d, width: W, height: H} = useVideoConfig();
  const kt = H * 0.022, w = 0.34 * W, h = 0.3 * H, gap = 0.03 * W, x0 = (W - (the.length * w + (the.length - 1) * gap)) / 2;
  const kLen = dau ? ea(rr(f, the[0]?.at, start), -4, 14, IO) : 1;   // tiêu đề từ giữa khung đi lên khi thẻ đầu vào
  return (
    <AbsoluteFill style={{...nenKem, opacity: Math.min(ea(f, 0, 8), raCanh(f, d))}}>
      {dau && <div style={{position: 'absolute', left: 0, right: 0, top: interpolate(kLen, [0, 1], [0.44 * H, 0.2 * H]), textAlign: 'center',
        fontFamily: BODY, fontWeight: 800, fontSize: interpolate(kLen, [0, 1], [kt * 2, kt * 1.35]), color: M.chu}}>
        <span style={{display: 'inline-block', width: '0.8em', height: '0.8em', border: `0.09em solid ${M.chu}`, borderRadius: '50%', marginRight: '0.4em',
          verticalAlign: '-0.08em'}} /><TuTu text={dau.text} f0={rr(f, dau.at, start)} buoc={6} /></div>}
      {the.map((t2, i) => { const k = ea(rr(f, t2.at, start), 0, 16, EXPO); return (
        <div key={i} style={{position: 'absolute', left: x0 + i * (w + gap), top: 0.36 * H, width: w, height: h, background: M.trang, borderRadius: kt * 0.5,
          boxShadow: '0 18px 44px rgba(30,30,40,.16)', display: 'flex', gap: kt, padding: kt, boxSizing: 'border-box', opacity: k,
          transform: `translateY(${(1 - k) * 30}px)`}}>
          {t2.hinh && <div style={{flex: 'none', width: h * 0.62, height: '100%', borderRadius: kt * 0.4, overflow: 'hidden'}}><Hinh nguon={t2.hinh} start={start} /></div>}
          <div style={{display: 'flex', flexDirection: 'column', justifyContent: 'center', minWidth: 0}}>
            {t2.tag && <div style={{fontFamily: BODY, fontWeight: 800, fontSize: kt * 0.62, color: M.nhan, letterSpacing: 1.5, textTransform: 'uppercase'}}>{t2.tag}</div>}
            <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: kt * 2.1, color: M.chu, textTransform: 'uppercase', lineHeight: 1.05, marginTop: kt * 0.3}}>
              <Hai text={t2.lon} /></div>
            {t2.so && <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: kt * 1.3, color: M.chu, marginTop: kt * 0.2}}>
              <span style={{color: M.nhan}}>{t2.so}</span> {t2.sau_so}</div>}
            {t2.phu && <div style={{fontFamily: BODY, fontSize: kt * 0.75, color: M.mo, marginTop: kt * 0.3}}>{t2.phu}</div>}
          </div></div>); })}
    </AbsoluteFill>
  );
};

// ───────────────── 8. Thẻ chào hai tầng (mẫu 18:49–18:55) — lớp phủ, người vẫn chạy ─────────────────
// {nho, nut:[{text, at}], tren:{text, at}, giua:{text, at}, duoi:{text, at}, phai}
export const TheChao = ({start, nho, nut = [], tren, giua, duoi, phai = true}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d, width: W, height: H} = useVideoConfig();
  const kt = H * 0.022, x = phai ? 0.66 * W : 0.04 * W, w = 0.3 * W;
  const k1 = ea(f, 0, 12, EXPO), k2 = tren ? ea(rr(f, tren.at, start), -4, 10, EXPO) : 0, ra = raCanh(f, d);
  const the = {position: 'absolute', left: x, width: w, background: '#F3F0EB', borderRadius: kt * 0.6, boxShadow: '0 18px 50px rgba(0,0,0,.35)',
    padding: kt * 0.9, boxSizing: 'border-box'};
  return (
    <AbsoluteFill style={{opacity: ra}}>
      {(nho || nut.length > 0) && <div style={{...the, top: 0.07 * H, opacity: k1, transform: `translateY(${(1 - k1) * 16}px)`}}>
        {nho && <div style={{fontFamily: BODY, fontWeight: 800, fontSize: kt * 0.7, color: M.nhan, letterSpacing: 1.5, textTransform: 'uppercase'}}>{nho}</div>}
        <div style={{display: 'flex', gap: kt * 0.5, marginTop: kt * 0.6}}>{nut.map((b, i) => { const k = ea(rr(f, b.at, start), 0, 10, BACK); return (
          <div key={i} style={{background: M.nhan, color: '#fff', fontFamily: BODY, fontWeight: 700, fontSize: kt * 0.85, borderRadius: 99,
            padding: `${kt * 0.3}px ${kt * 0.8}px`, opacity: k, transform: `scale(${0.7 + 0.3 * k})`}}>{b.text}</div>); })}</div></div>}
      {tren && <div style={{...the, top: 0.27 * H, minHeight: 0.26 * H, opacity: k2, transform: `translateY(${(1 - k2) * 18}px)`}}>
        <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: kt * 2.4, color: M.chu, textTransform: 'uppercase', lineHeight: 1}}>{tren.text}</div>
        {giua && <div style={{fontFamily: BODY, fontSize: kt * 0.85, color: '#555', marginTop: kt * 0.3, opacity: ea(rr(f, giua.at, start), 0, 10)}}>{giua.text}</div>}
        {duoi && <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: kt * 2.4, color: M.chu, textTransform: 'uppercase', lineHeight: 1, marginTop: kt * 0.7}}>
          <TuTu text={duoi.text} f0={rr(f, duoi.at, start)} buoc={8} /></div>}
      </div>}
    </AbsoluteFill>
  );
};

// ───────────────── 9. Người trong thẻ (mẫu bố cục 3: thẻ "Bước 2 · Quay" chứa video quay mặt) ─────────────────
// {nho, buoc:[{so, ten, phu, at, video: true | hinh}]}
export const NguoiTrongThe = ({start, nho, buoc = []}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d, width: W, height: H} = useVideoConfig();
  const n = buoc.length, kt = H * 0.02, gap = 0.035 * W, w = Math.min(0.27 * W, (0.9 * W - gap * (n - 1)) / n), h = w * 1.1;
  const x0 = (W - (n * w + (n - 1) * gap)) / 2, y = (H - h) / 2 + 0.03 * H;
  return (
    <AbsoluteFill style={{...nenKem, opacity: Math.min(ea(f, 0, 8), raCanh(f, d))}}>
      {nho && <div style={{position: 'absolute', left: 0.05 * W, top: 0.07 * H, fontFamily: BODY, fontWeight: 800, fontSize: kt * 1.1, color: M.nhan,
        letterSpacing: 2, textTransform: 'uppercase'}}>{nho}</div>}
      <svg width={W} height={H} style={{position: 'absolute', inset: 0}}>
        {buoc.slice(1).map((b, i) => { const xa = x0 + (i + 1) * w + i * gap + 8, xb = xa + gap - 16, yy = y + h / 2; return (
          <line key={i} x1={xa} y1={yy} x2={xa + (xb - xa) * ea(rr(f, b.at, start), -8, 4, IO)} y2={yy} stroke={M.nhan} strokeWidth={3} strokeDasharray="10 9" />); })}
      </svg>
      {buoc.map((b, i) => { const k = ea(rr(f, b.at, start), 0, 16, EXPO), co = !!(b.video || b.hinh); return (
        <div key={i} style={{position: 'absolute', left: x0 + i * (w + gap), top: y, width: w, height: h, background: M.trang, borderRadius: kt * 0.7,
          overflow: 'hidden', boxShadow: '0 20px 50px rgba(30,30,40,.18)', opacity: k, transform: `translateY(${(1 - k) * 28}px) scale(${0.95 + 0.05 * k})`,
          display: 'flex', flexDirection: 'column'}}>
          <div style={{padding: `${kt * 0.9}px ${kt}px ${kt * 0.5}px`}}>
            <div style={{fontFamily: BODY, fontWeight: 800, fontSize: kt * 0.75, color: M.nhan, letterSpacing: 1.5}}>BƯỚC {b.so ?? i + 1}</div>
            <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: kt * 1.9, color: M.chu, textTransform: 'uppercase', lineHeight: 1.05}}>{b.ten}</div>
            {b.phu && <div style={{fontFamily: BODY, fontSize: kt * 0.8, color: M.mo, marginTop: kt * 0.2}}>{b.phu}</div>}</div>
          {co && <div style={{flex: 1, margin: kt * 0.6, marginTop: 0, borderRadius: kt * 0.45, overflow: 'hidden', background: '#ddd'}}>
            {b.video ? <Goc start={start} style={{objectPosition: b.pos || '50% 50%'}} /> : <Hinh nguon={b.hinh} start={start} />}</div>}
        </div>); })}
    </AbsoluteFill>
  );
};

// ───────────────── 10. Thẻ dọc tối cạnh người (mẫu 00:28–00:40) — lớp phủ ─────────────────
// {nho, lon:{text, at}, muc:[{so, text, at, hinh}], cuoi:{text, at}, phai}
export const TheDocToi = ({start, nho, lon, muc = [], cuoi, phai = true}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d, width: W, height: H} = useVideoConfig();
  const kt = H * 0.02, x = phai ? 0.655 * W : 0.035 * W, w = 0.31 * W, y = 0.05 * H, h = 0.9 * H;
  const mo = ea(f, 0, 12, IO);
  const hw = w * 0.36, hh = hw * 0.58;
  return (
    <AbsoluteFill style={{opacity: raCanh(f, d)}}>
      <div style={{position: 'absolute', left: x, top: y, width: w, height: h, background: '#1B1B1B', borderRadius: kt * 0.9, boxShadow: '0 24px 60px rgba(0,0,0,.5)',
        clipPath: `inset(0 0 ${(1 - mo) * 100}% 0 round ${kt * 0.9}px)`, padding: kt * 1.1, boxSizing: 'border-box'}}>
        {nho && <div style={{fontFamily: BODY, fontSize: kt * 0.8, color: M.mo, opacity: ea(f, 8, 16)}}>{nho}</div>}
        {lon && <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: kt * 2.6, color: M.sang, textTransform: 'uppercase', lineHeight: 1, marginTop: kt * 0.4}}>
          <TuTu text={lon.text} f0={rr(f, lon.at, start)} buoc={6} /></div>}
        <div style={{display: 'flex', flexDirection: 'column', gap: kt * 0.9, marginTop: kt * 1.2}}>
          {muc.map((m2, i) => { const k = ea(rr(f, m2.at, start), 0, 14, EXPO), da = rr(f, m2.at, start) >= 0; return (
            <div key={i} style={{display: 'flex', alignItems: 'center', gap: kt * 0.8, opacity: 0.25 + 0.75 * k}}>
              <div style={{flex: 'none', width: hw, height: hh, borderRadius: kt * 0.4, overflow: 'hidden', background: '#2a2a2a',
                border: `1.5px solid ${da ? M.nhan : M.vien}`}}>{da && <Hinh nguon={m2.hinh} start={start} />}</div>
              <div><div style={{fontFamily: BODY, fontWeight: 800, fontSize: kt * 0.75, color: M.nhan}}>{String(m2.so ?? i + 1).padStart(2, '0')}</div>
                <div style={{fontFamily: BODY, fontWeight: 700, fontSize: kt * 1.05, color: M.sang, lineHeight: 1.2}}>{m2.text}</div></div></div>); })}
        </div>
        {cuoi && <div style={{position: 'absolute', left: kt * 1.1, bottom: kt * 1.1, background: '#2a2a2a', color: M.sang, fontFamily: BODY, fontWeight: 600,
          fontSize: kt * 0.85, padding: `${kt * 0.35}px ${kt * 0.8}px`, borderRadius: 99, opacity: ea(rr(f, cuoi.at, start), 0, 10)}}>{cuoi.text}</div>}
      </div>
    </AbsoluteFill>
  );
};
