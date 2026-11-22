// ĐƯỜNG MAY — cảnh tự vẽ mẫu (22/11/2026, tap-dji0022-2111; David: "màn hình mờ lại còn che nhân vật là hoàn toàn không đúng",
// "tôi đang nói với các đối tác thì có nên chỉ hiện một mình tôi không?"). Dùng khi người nói (một hay nhiều người) luôn phải hiện:
// hình vẽ nằm gọn trong CHỖ TRỐNG THẬT của khung `o` (đo từ ảnh đầu / giữa / cuối cảnh: trần, cửa kính, khoảng trên đầu), nền tấm
// tối có hạt (không làm mờ hình), mạch "đường may" nét đứt vẽ tiếp qua nhiều cảnh (mach.js — ý quay lại thì khâu tiếp lên hình cũ).
// Ba dạng (cùng một ngôn ngữ hình, chữ nguyên văn lời người nói, `*từ*` = từ nhấn chữ có chân):
//   dải chương : {so, nhan, ten}                                   → dải mảnh "01 │ NHÃN · TÊN PHẦN" (thay màn chương toàn khung)
//   đường may  : {tieu_de?, nut: [{text, at, cap?, capAt?, gach?}]}        → các nút trên đường khâu, nút đang nói sáng, nút cũ mờ;
//                nút có at < start = đã khâu ở cảnh trước (hiện ngay) → mạch vẽ tiếp
//   bộ vét     : {cong_cu: {text, at, gach}, vet: {text, at}, cap?: {text, at}} → bộ đồ chung bị gạch, bộ vét khâu dần (đỉnh "may đo")
// o = {x, y, w, h} phần khung 0–1, neo góc trên trái. canh.js: {type: 've', props: {ve: 'DuongMay', o, giuPhuDe: true, …}}
import React from 'react';
import {AbsoluteFill, Easing, useCurrentFrame, useVideoConfig} from 'remotion';
import {BODY, C, HEAD, ease, pop, rel} from '../chu-de';
import {ChuHien} from '../thu-vien/chu-hien';
import {kieuChu} from '../thu-vien/chuyen-dong';

const O_MAC_DINH = {x: 0.305, y: 0.075, w: 0.41, h: 0.18};
const dai = (t) => Math.max(1, ...String(t ?? '').replace(/\*/g, '').split('\n').map((l) => l.length));
const tien = (f, a, n = 22) => ease(f, a, a + n, 0, 1, Easing.out(Easing.exp));   // tiến độ vẽ 0..1

// Nền tấm: tối, có hạt (nền hạt — kiểu "giấy ảnh"), không làm mờ hình phía sau
const Tam = ({w, h, r, children, op, dy}) => (
  <div style={{position: 'absolute', inset: 0, opacity: op, transform: `translateY(${dy}px)`}}>
    <div style={{position: 'absolute', inset: 0, borderRadius: r, overflow: 'hidden',
      background: 'linear-gradient(180deg, rgba(13,13,16,0.93), rgba(13,13,16,0.88))', border: '1.5px solid rgba(255,255,255,0.09)',
      boxShadow: '0 18px 50px rgba(0,0,0,0.45)'}}>
      <svg width={w} height={h} style={{position: 'absolute', inset: 0, opacity: 0.09, mixBlendMode: 'screen'}}>
        <filter id="hat"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch" /></filter>
        <rect width={w} height={h} filter="url(#hat)" />
      </svg>
    </div>
    {children}
  </div>
);

// Kim khâu ở đầu đường may
const Kim = ({x, y, s}) => (
  <g transform={`translate(${x} ${y}) rotate(-38) scale(${s})`}>
    <line x1={0} y1={0} x2={30} y2={0} stroke={C.text} strokeWidth={3} strokeLinecap="round" />
    <ellipse cx={25} cy={0} rx={3.2} ry={1.4} fill="none" stroke={C.dim} strokeWidth={1.2} />
  </g>
);

export const DuongMay = ({sceneId, start, o = O_MAC_DINH, so, nhan, ten, tieu_de, nut = [], cong_cu, vet, cap}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d, width: W, height: H} = useVideoConfig();
  const kc = kieuChu(sceneId);
  const vao = ease(f, 0, 12), ra = ease(f, d - 9, d, 1, 0, Easing.in(Easing.cubic));
  const op = Math.min(vao, ra), dy = (1 - vao) * -14;
  const x = o.x * W, y = o.y * H, w = o.w * W, h = o.h * H;
  const box = {position: 'absolute', left: x, top: y, width: w, height: h};

  // ── dải chương
  if (so != null) {
    const fs = Math.min(H * 0.03, (w - H * 0.1) / (dai(`${nhan} · ${ten}`) * 0.62 + 2));
    return (
      <AbsoluteFill style={{opacity: op}}>
        <div style={{...box, height: 'auto', display: 'flex', justifyContent: 'center', transform: `translateY(${dy}px)`}}>
          <div style={{display: 'flex', alignItems: 'stretch', borderRadius: fs * 0.5, overflow: 'hidden', background: 'rgba(13,13,16,0.86)',
            border: '1.5px solid rgba(255,255,255,0.09)', boxShadow: '0 14px 40px rgba(0,0,0,0.45)'}}>
            <div style={{background: C.accent, color: '#120C09', fontFamily: HEAD, fontWeight: 800, fontSize: fs * 1.15,
              padding: `${fs * 0.3}px ${fs * 0.6}px`, display: 'flex', alignItems: 'center'}}>{String(so).padStart(2, '0')}</div>
            <div style={{display: 'flex', alignItems: 'center', gap: fs * 0.5, padding: `${fs * 0.3}px ${fs * 0.8}px`, whiteSpace: 'nowrap'}}>
              {nhan && <span style={{fontFamily: BODY, fontWeight: 700, fontSize: fs * 0.72, letterSpacing: 2.5, color: C.accent, textTransform: 'uppercase'}}>
                <ChuHien text={nhan} a={4} kieu={kc} /></span>}
              <span style={{fontFamily: HEAD, fontWeight: 800, fontSize: fs * 1.1, color: C.text, textTransform: 'uppercase', letterSpacing: 1}}>
                <ChuHien text={ten} a={9} kieu={kc} /></span>
            </div>
          </div>
        </div>
      </AbsoluteFill>
    );
  }

  const pad = h * 0.16, r = h * 0.14;

  // ── bộ vét (đỉnh): bộ đồ chung bị gạch → bộ vét khâu dần
  if (vet) {
    const aC = rel(cong_cu?.at ?? start, start), aG = cong_cu?.gach != null ? rel(cong_cu.gach, start) : Infinity;
    const aV = rel(vet.at, start), aK = cap ? rel(cap.at, start) : Infinity;
    const pC = tien(f, aC), pG = f >= aG ? tien(f, aG, 12) : 0, pV = f >= aV - 18 ? tien(f, aV - 18, 40) : 0;
    const s = (h - pad * 2) / 150;                       // cỡ hình vẽ theo chiều cao tấm
    const hx = pad + 10, vx = w * 0.4, lx = vx + 140 * s;
    const fsV = Math.min(h * 0.3, (w - lx - pad) / (dai(vet.text) * 0.48 + 0.4));
    const VEST = 'M30 12 L50 2 L60 22 L70 2 L90 12 L112 34 L102 146 L18 146 L8 34 Z';
    return (
      <AbsoluteFill>
        <div style={box}>
          <Tam w={w} h={h} r={r} op={op} dy={dy}>
            <svg width={w} height={h} style={{position: 'absolute', inset: 0}}>
              <defs><clipPath id={`khau-${sceneId}`}><rect x={0} y={0} width={w} height={pad + 150 * s * pV} /></clipPath></defs>
              {/* bộ đồ chung: hộp công cụ, bị gạch */}
              <g transform={`translate(${hx} ${pad + 20 * s}) scale(${s})`} opacity={(0.35 + 0.65 * pC) * (1 - 0.6 * pG)}>
                <rect x={0} y={34} width={110} height={78} rx={10} fill="none" stroke={C.muted} strokeWidth={5} style={{strokeDasharray: 400, strokeDashoffset: 400 * (1 - pC)}} />
                <path d="M36 34 V18 H74 V34" fill="none" stroke={C.muted} strokeWidth={5} strokeLinejoin="round" />
                <line x1={0} y1={66} x2={110} y2={66} stroke={C.muted} strokeWidth={3} />
                {pG > 0 && <path d="M-6 26 L116 120 M116 26 L-6 120" stroke="#EF4444" strokeWidth={8} strokeLinecap="round" style={{strokeDasharray: 160, strokeDashoffset: 160 * (1 - pG)}} />}
              </g>
              {/* đường khâu nối sang bộ vét */}
              <line x1={hx + 125 * s} y1={h * 0.5} x2={vx - 14 * s} y2={h * 0.5} stroke={C.accent} strokeWidth={3.5} strokeDasharray="12 9" opacity={0.85}
                style={{clipPath: `inset(0 ${(1 - Math.min(1, pV * 1.6)) * 100}% 0 0)`}} />
              {/* bộ vét: nét đứt khâu từ trên xuống, rồi lên màu */}
              <g transform={`translate(${vx} ${pad}) scale(${s})`} clipPath={`url(#khau-${sceneId})`}>
                <path d={VEST} fill={C.accentSoft} opacity={pV} />
                <path d={VEST} fill="none" stroke={C.accent} strokeWidth={4.5} strokeDasharray="10 7" strokeLinejoin="round" />
                <path d="M50 2 L60 62 L70 2" fill="none" stroke={C.accent} strokeWidth={4} />
                <circle cx={60} cy={88} r={4} fill={C.accent} /><circle cx={60} cy={112} r={4} fill={C.accent} />
              </g>
              {pV > 0 && pV < 0.97 && <Kim x={vx + 112 * s} y={pad + 146 * s * pV} s={s * 1.4} />}
            </svg>
            {cong_cu && f >= aC - 1 && <div style={{position: 'absolute', left: hx - 4, top: pad + 128 * s, width: 125 * s, textAlign: 'center',
              fontFamily: BODY, fontWeight: 600, fontSize: h * 0.1, color: C.muted, opacity: 1 - 0.5 * pG}}>
              <ChuHien text={cong_cu.text} a={aC} kieu={kc} /></div>}
            {f >= aV - 1 && <div style={{position: 'absolute', left: lx + pad * 0.6, top: h * 0.5 - fsV * (cap ? 0.95 : 0.6),
              fontFamily: HEAD, fontWeight: 800, fontSize: fsV, lineHeight: 1.12, color: C.text, textTransform: 'uppercase'}}>
              <ChuHien text={vet.text} a={aV} kieu={kc} /></div>}
            {cap && f >= aK - 1 && <div style={{position: 'absolute', left: lx + pad * 0.6, top: h * 0.5 + fsV * 0.45,
              fontFamily: BODY, fontWeight: 600, fontSize: h * 0.1, color: C.muted}}>
              <ChuHien text={cap.text} a={aK} kieu={kc} /></div>}
          </Tam>
        </div>
      </AbsoluteFill>
    );
  }

  // ── đường may: các nút khâu theo lời
  const n = Math.max(1, nut.length), x0 = pad * 1.4, x1 = w - pad * 1.4, slot = (x1 - x0) / n;
  const seamY = h * (tieu_de ? 0.66 : 0.6);
  const xs = nut.map((_, i) => x0 + slot * (i + 0.5));
  const as = nut.map((u) => (u.at < start ? -1000 : rel(u.at, start)));
  const ps = as.map((a) => (a < 0 ? 1 : tien(f, a, 20)));
  const hienCuoi = as.reduce((k, a, i) => (f >= a ? i : k), -1);        // nút đang nói = nút mới nhất đã hiện
  let dau = x0;
  ps.forEach((p, i) => { if (p > 0) dau = Math.max(dau, (i ? xs[i - 1] : x0) + ((xs[i]) - (i ? xs[i - 1] : x0)) * p); });
  const dangKhau = ps.some((p) => p > 0 && p < 0.97);
  // cỡ chữ nút: vừa bề ngang ô, và vừa chiều cao từ dưới dòng tiêu đề tới đường may (chữ 2 dòng không chạm tiêu đề)
  const soDong = Math.max(1, ...nut.map((u) => String(u.text).split('\n').length));
  const caoCo = seamY - h * 0.07 - (tieu_de ? pad * 0.7 + h * 0.15 : pad * 0.6);
  const fs = Math.min(h * 0.2, caoCo / (soDong * 1.18), ...nut.map((u) => slot / (dai(u.text) * 0.5 + 0.8)));
  return (
    <AbsoluteFill>
      <div style={box}>
        <Tam w={w} h={h} r={r} op={op} dy={dy}>
          {tieu_de && <div style={{position: 'absolute', left: pad * 1.2, top: pad * 0.7, fontFamily: BODY, fontWeight: 700, fontSize: h * 0.095,
            letterSpacing: 3, color: C.accent, textTransform: 'uppercase'}}><ChuHien text={tieu_de} a={4} kieu={kc} /></div>}
          <svg width={w} height={h} style={{position: 'absolute', inset: 0}}>
            <line x1={x0} y1={seamY} x2={x1} y2={seamY} stroke="rgba(255,255,255,0.10)" strokeWidth={2} />
            <line x1={x0} y1={seamY} x2={dau} y2={seamY} stroke={C.accent} strokeWidth={4} strokeDasharray="14 9" strokeLinecap="round" />
            {xs.map((cx, i) => ps[i] > 0 && (
              <circle key={i} cx={cx} cy={seamY} r={9 * Math.min(1, ps[i] * 1.4)} fill={C.bg}
                stroke={i === hienCuoi ? C.accent : C.dim} strokeWidth={4} />))}
            {dangKhau && <Kim x={dau} y={seamY} s={h / 180} />}
          </svg>
          {nut.map((u, i) => {
            if (ps[i] <= 0 && f < as[i] - 1) return null;
            const sang = i === hienCuoi;
            const g = u.gach != null ? ease(f, rel(u.gach, start), rel(u.gach, start) + 10) : 0;
            const p = as[i] < 0 ? 1 : pop(f, as[i]);
            return (
              <div key={i} style={{position: 'absolute', left: xs[i] - slot / 2, width: slot, bottom: h - seamY + h * 0.07, textAlign: 'center',
                opacity: (sang ? 1 : 0.8) * (1 - 0.45 * g) * Math.min(1, p * 1.3), transform: `translateY(${(1 - p) * 10}px)`}}>
                <div style={{position: 'relative', display: 'inline-block', fontFamily: HEAD, fontWeight: 800, fontSize: fs, lineHeight: 1.1,
                  color: sang ? C.text : C.muted, textTransform: 'uppercase', whiteSpace: 'pre-line'}}>
                  <ChuHien text={u.text} a={as[i] < 0 ? 0 : as[i]} kieu={as[i] < 0 ? 'dong' : kc} />
                  {g > 0 && <div style={{position: 'absolute', left: 0, top: '52%', height: Math.max(3, fs * 0.08), width: `${g * 100}%`, background: C.accent}} />}
                </div>
                {u.cap && (() => { const ca = u.capAt != null ? rel(u.capAt, start) : (as[i] < 0 ? 0 : as[i] + 6);
                  return f >= ca - 1 && <div style={{fontFamily: BODY, fontWeight: 600, fontSize: Math.max(fs * 0.5, h * 0.09), color: C.muted, position: 'absolute',
                    top: '100%', left: 0, right: 0, transform: `translateY(${h * 0.13}px)`}}><ChuHien text={u.cap} a={ca} kieu={kc} /></div>; })()}
              </div>
            );
          })}
        </Tam>
      </div>
    </AbsoluteFill>
  );
};
