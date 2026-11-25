// ĐƯỜNG MAY — cảnh tự vẽ mẫu (22/11/2026, tap-dji0022-2111; David: "màn hình mờ lại còn che nhân vật là hoàn toàn không đúng",
// "tôi đang nói với các đối tác thì có nên chỉ hiện một mình tôi không?"). Dùng khi người nói (một hay nhiều người) luôn phải hiện:
// hình vẽ nằm gọn trong CHỖ TRỐNG THẬT của khung `o` (đo từ ảnh đầu / giữa / cuối cảnh: trần, cửa kính, khoảng trên đầu), nền tấm
// tối có hạt (không làm mờ hình), mạch "đường may" nét đứt vẽ tiếp qua nhiều cảnh (mach.js — ý quay lại thì khâu tiếp lên hình cũ).
// Ba dạng (cùng một ngôn ngữ hình, chữ nguyên văn lời người nói, `*từ*` = từ nhấn chữ có chân):
//   dải chương : {so, nhan, ten}                                   → dải mảnh "01 │ NHÃN · TÊN PHẦN" (thay màn chương toàn khung)
//   đường may  : {tieu_de?, nut: [{text, at, cap?, capAt?, gach?}]}        → các nút trên đường khâu, nút đang nói sáng, nút cũ mờ;
//                nút có at < start = đã khâu ở cảnh trước (hiện ngay) → mạch vẽ tiếp
//   bộ vét     : {cong_cu: {text, at, gach}, vet: {text, at}, cap?: {text, at}} → bộ đồ chung bị gạch, bộ vét khâu dần (đỉnh "may đo")
//   thẻ lật 3D : {tieu_de?, the: [{text, at}]}                     → mỗi ý một thẻ lật vào đúng lúc nói, thẻ đang nói sáng (Sang Huỳnh)
//   gạch thay  : {tieu_de?, tieu_deAt?, thay: [{text, at, gach?, cap?, capAt?}]} → ý cũ bị gạch đỏ, mũi tên, ý mới to (Sang Huỳnh)
//   số mốc     : {tieu_de?, buoc: [{so, text, at}]}                → số to viền rỗng, bước đang nói tô đầy, thanh tiến trình (MagentX, Ali)
//   chương lớn : {so, nhan, ten, lon: true}                        → số to mờ phía sau, nhãn nhỏ, tên phần to (Sang Huỳnh)
//   thẻ tên    : {ten_the: {nhan?, ten: {text, at}, vai?: {text, at}}} → tên to + vai trò, lúc người nói tự giới thiệu (The Diary Of A CEO)
//   mảnh ghép  : {tieu_de?, ghep: [{text, at}, {text, at}]}        → hai mảnh trượt vào, khớp ở giữa (vẽ đúng vật — "kết nối", "mảnh ghép")
//   câu đắt    : {cau: {text, at}}                                 → một câu chữ to theo lời, một từ `*nhấn*` (The Diary Of A CEO)
//   lời nhắc   : {tieu_de?, nhac: [{text, at}]}                    → lệnh gửi AI thành bong bóng chat, lệnh đang nói sáng (Sang Huỳnh)
//   khuôn áo   : {khuon: {goc: {text, at}, sua: [{cho: 'eo'|'co', text, at}]}} → khuôn gốc nét đứt, chỗ sửa theo từng người sáng lên
// Hiệu ứng (rieng/hieu-ung.jsx): vao / ra = truot · lat-3d · xoay-3d · mo-man · phong · nhoe; quet = giây vệt sáng quét qua tấm.
// Đổi hiệu ứng qua các cảnh để video không lặp một kiểu.
// o = {x, y, w, h} phần khung 0–1, neo góc trên trái. canh.js: {type: 've', props: {ve: 'DuongMay', o, giuPhuDe: true, …}}
import React from 'react';
import {AbsoluteFill, Easing, interpolate, useCurrentFrame, useVideoConfig} from 'remotion';
import {BODY, C, HEAD, ease, pop, rel} from '../chu-de';
import {ChuHien} from '../thu-vien/chu-hien';
import {kieuChu} from '../thu-vien/chuyen-dong';
import {vaoRaKieu, QuetSang} from './hieu-ung';

const O_MAC_DINH = {x: 0.305, y: 0.075, w: 0.41, h: 0.18};
const dai = (t) => Math.max(1, ...String(t ?? '').replace(/\*/g, '').split('\n').map((l) => l.length));
const tien = (f, a, n = 22) => ease(f, a, a + n, 0, 1, Easing.out(Easing.exp));   // tiến độ vẽ 0..1

// Nền tấm: tối, có hạt (nền hạt — kiểu "giấy ảnh"), không làm mờ hình phía sau. v = vaoRaKieu (hiệu ứng vào / ra của cảnh)
const Tam = ({w, h, r, children, v, quet}) => (
  <div style={v.boc}><div style={v.khoi}>
    <div style={{position: 'absolute', inset: 0, borderRadius: r, overflow: 'hidden',
      background: 'linear-gradient(180deg, rgba(13,13,16,0.93), rgba(13,13,16,0.88))', border: '1.5px solid rgba(255,255,255,0.09)',
      boxShadow: '0 18px 50px rgba(0,0,0,0.45)'}}>
      <svg width={w} height={h} style={{position: 'absolute', inset: 0, opacity: 0.09, mixBlendMode: 'screen'}}>
        <filter id="hat"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch" /></filter>
        <rect width={w} height={h} filter="url(#hat)" />
      </svg>
    </div>
    {children}
    {quet != null && <QuetSang a={quet} w={w} h={h} r={r} />}
  </div></div>
);

// Kim khâu ở đầu đường may
const Kim = ({x, y, s}) => (
  <g transform={`translate(${x} ${y}) rotate(-38) scale(${s})`}>
    <line x1={0} y1={0} x2={30} y2={0} stroke={C.text} strokeWidth={3} strokeLinecap="round" />
    <ellipse cx={25} cy={0} rx={3.2} ry={1.4} fill="none" stroke={C.dim} strokeWidth={1.2} />
  </g>
);

export const DuongMay = ({sceneId, start, o = O_MAC_DINH, so, nhan, ten, lon, tieu_de, tieu_deAt, nut = [], the, thay, buoc, cong_cu, vet, cap,
  khuon, nhac, cau, ghep, ten_the, vao = 'truot', ra = 'nhoe', quet}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d, width: W, height: H} = useVideoConfig();
  const kc = kieuChu(sceneId);
  const v = vaoRaKieu(f, d, {vao, ra});
  const qA = quet != null ? rel(quet, start) : null;          // khung bắt đầu vệt sáng quét qua tấm
  const x = o.x * W, y = o.y * H, w = o.w * W, h = o.h * H;
  const box = {position: 'absolute', left: x, top: y, width: w, height: h};

  // ── màn chương lớn trong chỗ trống (học Sang Huỳnh 07/11: số to mờ phía sau, nhãn nhỏ màu nhấn, tên phần to)
  if (so != null && lon) {
    const pd = h * 0.16, rr = h * 0.14;
    const fsT = Math.min(h * 0.3, (w * 0.72) / (dai(ten) * 0.55 + 0.5));
    return (
      <AbsoluteFill>
        <div style={box}>
          <Tam w={w} h={h} r={rr} v={v} quet={qA}>
            <div style={{position: 'absolute', left: pd * 0.4, top: h * 0.02, fontFamily: HEAD, fontWeight: 800, fontSize: h * 0.98, lineHeight: 0.98,
              color: 'transparent', WebkitTextStroke: '2.5px rgba(255,122,69,0.5)', transform: `translateX(${(1 - tien(f, 0, 30)) * -30}px)`}}>
              {String(so).padStart(2, '0')}</div>
            <div style={{position: 'absolute', left: w * 0.26, right: pd, top: 0, bottom: 0, display: 'flex', flexDirection: 'column', justifyContent: 'center', gap: h * 0.04}}>
              {nhan && <div style={{fontFamily: BODY, fontWeight: 700, fontSize: h * 0.1, letterSpacing: 3, color: C.accent, textTransform: 'uppercase'}}>
                <ChuHien text={nhan} a={5} kieu={kc} /></div>}
              <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: fsT, lineHeight: 1.05, color: C.text, textTransform: 'uppercase'}}>
                <ChuHien text={ten} a={10} kieu={kc} /></div>
            </div>
          </Tam>
        </div>
      </AbsoluteFill>
    );
  }

  // ── dải chương
  if (so != null) {
    const fs = Math.min(H * 0.03, (w - H * 0.1) / (dai(`${nhan} · ${ten}`) * 0.62 + 2));
    return (
      <AbsoluteFill>
        <div style={{...box, height: 'auto', display: 'flex', justifyContent: 'center', perspective: 1100}}>
          <div style={{display: 'flex', alignItems: 'stretch', borderRadius: fs * 0.5, overflow: 'hidden', background: 'rgba(13,13,16,0.9)',
            border: '1.5px solid rgba(255,255,255,0.09)', boxShadow: '0 14px 40px rgba(0,0,0,0.45)', ...v.khoi, inset: undefined, position: 'relative'}}>
            {qA != null && <QuetSang a={qA} w={w} h={fs * 2} />}
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
          <Tam w={w} h={h} r={r} v={v} quet={qA}>
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

  // ── thẻ lật 3D: mỗi ý một thẻ lật vào (xoay quanh trục dọc) đúng lúc nói, thẻ đang nói viền cam, thẻ cũ lùi nhẹ
  if (the) {
    const n = Math.max(1, the.length), gap = h * 0.08, top = tieu_de ? h * 0.3 : pad, cao = h - top - pad * 0.8;
    const rong = (w - pad * 2 - gap * (n - 1)) / n;
    const fsT = Math.min(cao * 0.36, ...the.map((u) => rong / (dai(u.text) * 0.5 + 0.9)));
    const at = the.map((u) => rel(u.at, start));
    const cuoi = at.reduce((k, a, i) => (f >= a ? i : k), -1);
    return (
      <AbsoluteFill>
        <div style={box}>
          <Tam w={w} h={h} r={r} v={v} quet={qA}>
            {tieu_de && <div style={{position: 'absolute', left: pad * 1.2, top: pad * 0.6, fontFamily: BODY, fontWeight: 700, fontSize: h * 0.095,
              letterSpacing: 3, color: C.accent, textTransform: 'uppercase'}}><ChuHien text={tieu_de} a={4} kieu={kc} /></div>}
            {the.map((u, i) => {
              if (f < at[i] - 1) return null;
              const p = interpolate(f, [at[i], at[i] + 16], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.out(Easing.back(1.4))});
              const sang = i === cuoi;
              return (
                <div key={i} style={{position: 'absolute', left: pad + i * (rong + gap), top, width: rong, height: cao, perspective: 900}}>
                  <div style={{position: 'absolute', inset: 0, borderRadius: h * 0.08, background: sang ? 'rgba(255,122,69,0.14)' : 'rgba(255,255,255,0.05)',
                    border: `2px solid ${sang ? C.accent : 'rgba(255,255,255,0.12)'}`, display: 'flex', alignItems: 'center', justifyContent: 'center',
                    transform: `rotateY(${(1 - p) * -95}deg) scale(${sang ? 1 : 0.96})`, transformOrigin: '50% 50%', opacity: Math.min(1, p * 2) * (sang ? 1 : 0.75),
                    backfaceVisibility: 'hidden'}}>
                    <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: fsT, lineHeight: 1.1, textAlign: 'center', whiteSpace: 'pre-line',
                      color: sang ? C.text : C.muted, textTransform: 'uppercase'}}><ChuHien text={u.text} a={at[i] + 6} kieu={kc} /></div>
                  </div>
                </div>
              );
            })}
          </Tam>
        </div>
      </AbsoluteFill>
    );
  }

  // ── thẻ tên + vai trò (học The Diary Of A CEO ca 10: tên + vai trò ngay lần đầu người nói tự giới thiệu, ngắn, một lần):
  //    {ten_the: {nhan?, ten: {text, at}, vai: {text, at}}} — chữ nguyên văn lúc người nói tự nói tên / việc đang làm
  if (ten_the) {
    const aT = rel(ten_the.ten.at, start), aV = ten_the.vai ? rel(ten_the.vai.at, start) : Infinity;
    const fsT = Math.min(h * 0.36, (w * 0.5) / (dai(ten_the.ten.text) * 0.56 + 0.4));
    const pV = f >= aV ? tien(f, aV, 16) : 0;
    return (
      <AbsoluteFill>
        <div style={box}>
          <Tam w={w} h={h} r={r} v={v} quet={qA}>
            <div style={{position: 'absolute', left: pad * 1.3, top: 0, bottom: 0, display: 'flex', alignItems: 'center', gap: pad * 0.9}}>
              <div style={{width: 5, height: h * 0.56, borderRadius: 3, background: C.accent, transform: `scaleY(${tien(f, aT - 6, 14)})`}} />
              <div>
                {ten_the.nhan && <div style={{fontFamily: BODY, fontWeight: 700, fontSize: h * 0.095, letterSpacing: 3, color: C.accent, textTransform: 'uppercase'}}>
                  <ChuHien text={ten_the.nhan} a={2} kieu={kc} /></div>}
                {f >= aT - 1 && <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: fsT, lineHeight: 1.05, color: C.text, textTransform: 'uppercase', letterSpacing: 2}}>
                  <ChuHien text={ten_the.ten.text} a={aT} kieu={kc} /></div>}
              </div>
            </div>
            {ten_the.vai && f >= aV - 1 && <div style={{position: 'absolute', right: pad * 1.3, top: 0, bottom: 0, display: 'flex', alignItems: 'center',
              opacity: pV, transform: `translateX(${(1 - pV) * 20}px)`}}>
              <div style={{fontFamily: BODY, fontWeight: 700, fontSize: h * 0.13, lineHeight: 1.2, color: C.muted, textAlign: 'right', whiteSpace: 'pre-line'}}>
                <ChuHien text={ten_the.vai.text} a={aV} kieu={kc} /></div></div>}
          </Tam>
        </div>
      </AbsoluteFill>
    );
  }

  // ── mảnh ghép (vẽ đúng vật đang nói — học Ali Abdaal ca 13): hai mảnh trượt vào từ hai bên, khớp nhau ở giữa đúng lúc nói;
  //    {tieu_de?, ghep: [{text, at}, {text, at}], khop?: giây hai mảnh chạm (mặc định lúc mảnh 2 vào)}
  if (ghep) {
    const top = tieu_de ? h * 0.3 : pad, cao = h - top - pad * 0.8, rong = (w - pad * 3) / 2, nu = cao * 0.22;
    const at = ghep.map((u) => rel(u.at, start));
    const fsG = Math.min(cao * 0.32, ...ghep.map((u) => (rong - nu * 2) / (dai(u.text) * 0.52 + 0.8)));
    const cx = w / 2;
    // mảnh trái có núm nhô sang phải, mảnh phải có hốc lõm bên trái (cùng bán kính) → khớp khít khi chạm
    const trai = `M0 0 H${rong} V${cao / 2 - nu} A${nu} ${nu} 0 1 1 ${rong} ${cao / 2 + nu} V${cao} H0 Z`;
    const phai = `M0 0 H${rong} V${cao} H0 V${cao / 2 + nu} A${nu} ${nu} 0 1 0 0 ${cao / 2 - nu} Z`;
    return (
      <AbsoluteFill>
        <div style={box}>
          <Tam w={w} h={h} r={r} v={v} quet={qA}>
            {tieu_de && <div style={{position: 'absolute', left: pad * 1.2, top: pad * 0.6, fontFamily: BODY, fontWeight: 700, fontSize: h * 0.095,
              letterSpacing: 3, color: C.accent, textTransform: 'uppercase'}}><ChuHien text={tieu_de} a={4} kieu={kc} /></div>}
            {ghep.map((u, i) => {
              if (f < at[i] - 1) return null;
              const p = tien(f, at[i], 18), ben = i === 0 ? -1 : 1;
              const x = i === 0 ? cx - rong + ben * (1 - p) * w * 0.12 : cx + ben * (1 - p) * w * 0.12;
              const sang = i === at.reduce((k, a, j) => (f >= a ? j : k), -1);
              const khop = at.length > 1 && f >= at[1] + 14;
              return (
                <div key={i} style={{position: 'absolute', left: x, top, width: rong + (i === 0 ? nu : 0), height: cao, opacity: Math.min(1, p * 1.5)}}>
                  <svg width={rong + nu} height={cao} style={{position: 'absolute', inset: 0, overflow: 'visible'}}>
                    <path d={i === 0 ? trai : phai} fill={sang || khop ? 'rgba(255,122,69,0.16)' : 'rgba(255,255,255,0.06)'}
                      stroke={sang || khop ? C.accent : C.dim} strokeWidth={2.5} />
                  </svg>
                  <div style={{position: 'absolute', left: i === 0 ? 0 : nu, width: rong - nu, top: 0, height: cao, display: 'flex', alignItems: 'center',
                    justifyContent: 'center', fontFamily: HEAD, fontWeight: 800, fontSize: fsG, lineHeight: 1.1, textAlign: 'center', whiteSpace: 'pre-line',
                    color: sang || khop ? C.text : C.muted, textTransform: 'uppercase'}}><ChuHien text={u.text} a={at[i] + 4} kieu={kc} /></div>
                </div>
              );
            })}
          </Tam>
        </div>
      </AbsoluteFill>
    );
  }

  // ── câu đắt (học The Diary Of A CEO ca 1: một câu đắt chữ to theo lời, một từ nhấn đổi màu): chữ to giữa tấm
  if (cau) {
    const fsC = Math.min(h * 0.3, (w - pad * 2.4) / (dai(cau.text) * 0.5 + 0.4));
    return (
      <AbsoluteFill>
        <div style={box}>
          <Tam w={w} h={h} r={r} v={v} quet={qA}>
            <div style={{position: 'absolute', inset: 0, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: `0 ${pad * 1.2}px`,
              fontFamily: HEAD, fontWeight: 800, fontSize: fsC, lineHeight: 1.1, color: C.text, textTransform: 'uppercase', textAlign: 'center', whiteSpace: 'pre-line'}}>
              <ChuHien text={cau.text} a={rel(cau.at, start)} kieu={kc} /></div>
          </Tam>
        </div>
      </AbsoluteFill>
    );
  }

  // ── lời nhắc gửi AI (học Sang Huỳnh 07/11 #5 "thẻ lời nhắc phóng to"): các lệnh hiện thành bong bóng chat xếp từ trái sang phải,
  //    lệnh đang nói sáng, lệnh cũ mờ; nhãn trái là người nhận (chữ nguyên văn, vd "ném vào AI")
  if (nhac) {
    const n = Math.max(1, nhac.length), gap = h * 0.07, top = tieu_de ? h * 0.32 : pad, cao = h - top - pad * 0.9;
    // ô rộng theo độ dài chữ (lệnh dài không bị chữ nhỏ), cùng một cỡ chữ cho mọi bong bóng
    const tong = nhac.reduce((k, u) => k + dai(u.text) * 0.58 + 1.8, 0);
    const fsN = Math.min(cao * 0.34, (w - pad * 2 - gap * (n - 1)) / tong);
    const rongs = nhac.map((u) => (dai(u.text) * 0.58 + 1.8) * fsN), lefts = rongs.map((_, i) => pad + rongs.slice(0, i).reduce((k, x) => k + x + gap, 0));
    const at = nhac.map((u) => rel(u.at, start));
    const cuoi = at.reduce((k, a, i) => (f >= a ? i : k), -1);
    return (
      <AbsoluteFill>
        <div style={box}>
          <Tam w={w} h={h} r={r} v={v} quet={qA}>
            {tieu_de && <div style={{position: 'absolute', left: pad * 1.2, top: pad * 0.6, fontFamily: BODY, fontWeight: 700, fontSize: h * 0.095,
              letterSpacing: 3, color: C.accent, textTransform: 'uppercase', opacity: f >= rel(tieu_deAt ?? start, start) ? 1 : 0}}>
              <ChuHien text={tieu_de} a={rel(tieu_deAt ?? start, start) + 2} kieu={kc} /></div>}
            {nhac.map((u, i) => {
              if (f < at[i] - 1) return null;
              const p = pop(f, at[i]), sang = i === cuoi;
              return (
                <div key={i} style={{position: 'absolute', left: lefts[i], top: top + (1 - p) * 12, width: rongs[i], height: cao,
                  opacity: Math.min(1, p * 1.4) * (sang ? 1 : 0.6), transform: `scale(${0.9 + 0.1 * p})`, transformOrigin: '0% 100%'}}>
                  <div style={{position: 'absolute', inset: 0, bottom: cao * 0.12, borderRadius: `${h * 0.08}px ${h * 0.08}px ${h * 0.08}px ${h * 0.02}px`,
                    background: sang ? C.accent : 'rgba(255,255,255,0.1)', display: 'flex', alignItems: 'center', gap: fsN * 0.4, padding: `0 ${fsN * 0.6}px`}}>
                    <span style={{fontFamily: HEAD, fontWeight: 800, fontSize: fsN * 0.9, color: sang ? '#120C09' : C.accent}}>›</span>
                    <span style={{fontFamily: BODY, fontWeight: 700, fontSize: fsN, lineHeight: 1.15, whiteSpace: 'nowrap', color: sang ? '#120C09' : C.text}}>
                      <ChuHien text={u.text} a={at[i] + 3} kieu={kc} /></span>
                  </div>
                </div>
              );
            })}
          </Tam>
        </div>
      </AbsoluteFill>
    );
  }

  // ── khuôn áo (vẽ đúng vật đang nói — học Ali Abdaal ca 13): khuôn gốc nét đứt, rồi chỗ được sửa theo từng người sáng lên (eo, cổ)
  if (khuon) {
    const s = (h - pad * 2) / 150, vx = pad * 1.6, lx = vx + 150 * s;
    const VEST = 'M30 12 L50 2 L60 22 L70 2 L90 12 L112 34 L102 146 L18 146 L8 34 Z';
    const aG = rel(khuon.goc.at, start), pG = tien(f, aG, 30);
    const CHO = {eo: 'M14 92 Q60 84 106 92', co: 'M30 12 L50 2 L60 22 L70 2 L90 12'};
    const sua = khuon.sua || [];
    const as = sua.map((u) => rel(u.at, start));
    const cuoi = as.reduce((k, a, i) => (f >= a ? i : k), -1);
    const fsK = Math.min(h * 0.17, (w - lx - pad * 2) / ((sua.length + 1) * 6.2));
    return (
      <AbsoluteFill>
        <div style={box}>
          <Tam w={w} h={h} r={r} v={v} quet={qA}>
            <svg width={w} height={h} style={{position: 'absolute', inset: 0}}>
              <g transform={`translate(${vx} ${pad}) scale(${s})`}>
                <path d={VEST} fill="none" stroke={C.muted} strokeWidth={4} strokeDasharray="10 7" strokeLinejoin="round"
                  style={{strokeDasharray: '10 7', opacity: 0.35 + 0.65 * pG}} />
                {sua.map((u, i) => f >= as[i] && (
                  <path key={i} d={CHO[u.cho]} fill="none" stroke={C.accent} strokeWidth={7} strokeLinecap="round" strokeLinejoin="round"
                    style={{strokeDasharray: 200, strokeDashoffset: 200 * (1 - tien(f, as[i], 16))}} opacity={i === cuoi ? 1 : 0.55} />))}
              </g>
            </svg>
            <div style={{position: 'absolute', left: lx, right: pad, top: 0, bottom: 0, display: 'flex', alignItems: 'center', gap: fsK * 0.8}}>
              {f >= aG - 1 && <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: fsK, color: cuoi < 0 ? C.text : C.muted, textTransform: 'uppercase', whiteSpace: 'nowrap'}}>
                <ChuHien text={khuon.goc.text} a={aG} kieu={kc} /></div>}
              {sua.map((u, i) => f >= as[i] - 1 && (
                <React.Fragment key={i}>
                  <span style={{color: C.accent, fontFamily: HEAD, fontSize: fsK * 0.8}}>+</span>
                  <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: fsK, color: i === cuoi ? C.text : C.muted, textTransform: 'uppercase', whiteSpace: 'nowrap'}}>
                    <ChuHien text={u.text} a={as[i]} kieu={kc} /></div>
                </React.Fragment>))}
            </div>
          </Tam>
        </div>
      </AbsoluteFill>
    );
  }

  // ── gạch thay (học Sang Huỳnh 07/11 "thẻ cạnh mặt: gạch chữ cũ thì hiện chữ mới"): ý cũ bị gạch, mũi tên, ý mới to và sáng
  if (thay) {
    const n = Math.max(1, thay.length), top = tieu_de ? h * 0.3 : pad, cao = h - top - pad * 0.9;
    const muiTen = h * 0.22, slot = (w - pad * 2 - muiTen * (n - 1)) / n;
    const at = thay.map((u) => rel(u.at, start));
    const cuoi = at.reduce((k, a, i) => (f >= a ? i : k), -1);
    const fsG = Math.min(cao * 0.42, ...thay.map((u) => slot / (dai(u.text) * 0.52 + 0.6)));
    return (
      <AbsoluteFill>
        <div style={box}>
          <Tam w={w} h={h} r={r} v={v} quet={qA}>
            {tieu_de && <div style={{position: 'absolute', left: pad * 1.2, top: pad * 0.6, fontFamily: BODY, fontWeight: 700, fontSize: h * 0.095,
              letterSpacing: 3, color: C.accent, textTransform: 'uppercase', opacity: f >= rel(tieu_deAt ?? start, start) ? 1 : 0}}>
              <ChuHien text={tieu_de} a={rel(tieu_deAt ?? start, start) + 2} kieu={kc} /></div>}
            {thay.map((u, i) => {
              if (f < at[i] - 1) return null;
              const p = pop(f, at[i]), sang = i === cuoi;
              const g = u.gach != null ? tien(f, rel(u.gach, start), 12) : 0;
              const left = pad + i * (slot + muiTen);
              return (
                <React.Fragment key={i}>
                  {i > 0 && <div style={{position: 'absolute', left: left - muiTen, width: muiTen, top, height: cao, display: 'flex', alignItems: 'center',
                    justifyContent: 'center', color: C.accent, fontFamily: HEAD, fontSize: fsG * 0.8, opacity: Math.min(1, p * 1.5)}}>→</div>}
                  <div style={{position: 'absolute', left, width: slot, top, height: cao, display: 'flex', flexDirection: 'column', alignItems: 'center',
                    justifyContent: 'center', opacity: Math.min(1, p * 1.3) * (1 - 0.5 * g) * (sang || g ? 1 : 0.8),
                    transform: `translateY(${(1 - p) * 10}px) scale(${1 - 0.08 * g})`}}>
                    <div style={{position: 'relative', fontFamily: HEAD, fontWeight: 800, fontSize: fsG, lineHeight: 1.1, textAlign: 'center',
                      whiteSpace: 'pre-line', color: sang && !g ? C.text : C.muted, textTransform: 'uppercase'}}>
                      <ChuHien text={u.text} a={at[i]} kieu={kc} />
                      {g > 0 && <div style={{position: 'absolute', left: '-4%', top: '50%', height: Math.max(5, fsG * 0.14), width: `${g * 108}%`,
                        background: '#EF4444', borderRadius: 3, transform: 'rotate(-4deg)'}} />}
                    </div>
                    {u.cap && f >= rel(u.capAt ?? u.at, start) - 1 && <div style={{marginTop: h * 0.03, fontFamily: BODY, fontWeight: 700, fontSize: h * 0.115,
                      color: g ? '#F87171' : C.muted}}><ChuHien text={u.cap} a={rel(u.capAt ?? u.at, start)} kieu={kc} /></div>}
                  </div>
                </React.Fragment>
              );
            })}
          </Tam>
        </div>
      </AbsoluteFill>
    );
  }

  // ── số mốc (học MagentX 20/11 "số thứ tự to làm mốc" + Ali Abdaal 10/11 "thanh tiến trình, mục hiện tại sáng"): mỗi bước một số to
  //    viền rỗng, bước đang nói số tô đầy màu nhấn, thanh dưới chạy tới bước đang nói
  if (buoc) {
    const n = Math.max(1, buoc.length), top = tieu_de ? h * 0.27 : pad, cao = h - top - pad * 1.1, slot = (w - pad * 2) / n;
    const at = buoc.map((u) => rel(u.at, start));
    const cuoi = at.reduce((k, a, i) => (f >= a ? i : k), -1);
    const fsS = cao * 0.98, fsL = Math.min(cao * 0.36, ...buoc.map((u) => (slot - fsS * 0.7) / (dai(u.text) * 0.52 + 0.4)));
    const den = cuoi < 0 ? 0 : (cuoi + tien(f, at[cuoi], 18)) / n;
    return (
      <AbsoluteFill>
        <div style={box}>
          <Tam w={w} h={h} r={r} v={v} quet={qA}>
            {tieu_de && <div style={{position: 'absolute', left: pad * 1.2, top: pad * 0.55, fontFamily: BODY, fontWeight: 700, fontSize: h * 0.095,
              letterSpacing: 3, color: C.accent, textTransform: 'uppercase'}}><ChuHien text={tieu_de} a={4} kieu={kc} /></div>}
            {buoc.map((u, i) => {
              const hien = f >= at[i] - 1, sang = i === cuoi, p = hien ? pop(f, at[i]) : 0;
              return (
                <div key={i} style={{position: 'absolute', left: pad + i * slot, width: slot, top, height: cao, display: 'flex', alignItems: 'center',
                  gap: fsS * 0.12, opacity: hien ? (sang ? 1 : 0.55) : 0.22}}>
                  <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: fsS, lineHeight: 0.9, color: sang ? C.accent : 'transparent',
                    WebkitTextStroke: `2px ${sang ? C.accent : C.dim}`, transform: `scale(${0.85 + 0.15 * (hien ? p : 1)})`, transformOrigin: '50% 60%'}}>{u.so}</div>
                  {hien && <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: fsL, lineHeight: 1.08, color: sang ? C.text : C.muted,
                    textTransform: 'uppercase', whiteSpace: 'pre-line'}}><ChuHien text={u.text} a={at[i] + 4} kieu={kc} /></div>}
                </div>
              );
            })}
            <div style={{position: 'absolute', left: pad, right: pad, bottom: pad * 0.55, height: 4, borderRadius: 2, background: 'rgba(255,255,255,0.1)'}}>
              <div style={{width: `${den * 100}%`, height: '100%', borderRadius: 2, background: C.accent}} />
            </div>
          </Tam>
        </div>
      </AbsoluteFill>
    );
  }

  // ── đường may: các nút khâu theo lời
  const n =Math.max(1, nut.length), x0 = pad * 1.4, x1 = w - pad * 1.4, slot = (x1 - x0) / n;
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
        <Tam w={w} h={h} r={r} v={v} quet={qA}>
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
