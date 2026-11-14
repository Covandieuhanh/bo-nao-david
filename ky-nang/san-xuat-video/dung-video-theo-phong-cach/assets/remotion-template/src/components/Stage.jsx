// Sân khấu nền cho video PODCAST (không có hình gốc) — chạy suốt video, nền đặc, render một lần thành video_goc.mp4.
// Dọc 1080×1920 hoặc NGANG 1920×1080 thiết kế toàn khung (podframe.js). Thanh thời gian + phụ đề ở lớp phu-de (trên cùng).
// Trên: tên chương trình (nếu người dùng đưa) + tên tập (trích lời). Giữa: ý đang bàn (TOPICS, trích lời) — tự ẩn khi có lớp phủ.
// Dưới: sóng âm theo giọng thật (envelope.js), màu theo người đang nói; tên người nói CHỈ hiện khi biết tên (lời nói/người dùng
// đưa) — không tự đặt nhãn kiểu "Người dẫn". Ngang: thêm vòng sóng phát theo giọng ở bên phải.
import React from 'react';
import {AbsoluteFill, Img, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {BODY, C, HEAD, ease, pop} from '../theme';
import {SCENES, STAGE, TOPICS, fr} from '../scenes';
import {FULL} from '../layout';
import {LAND, PF, PF_W, VN} from '../podframe';
import SPEAKERS from '../speakers.js';
import HL from '../highlight.js';
import ENVELOPE from '../envelope.js';
import {BrandMark} from './Overlays';

const SPK = [C.accent, C.accent2 || '#7DB8FF'];   // màu người 0, người 1
const L = LAND ? {
  headTop: 70, titleSize: 38, titleW: 1240,
  topic: {top: 290, w: 1080, max: 118}, wave: {top: 690, h: 105, n: 96}, ring: {x: 1560, y: 400, r: 120}, map: {top: 598, size: 22, maxTopic: 92},
} : {
  headTop: 226, titleSize: 36, titleW: PF_W,
  topic: {top: 560, w: PF_W, max: 104}, chips: {top: 1030}, wave: {top: 1145, h: 100, n: 44}, map: {top: 900, size: 24, maxTopic: 92},
};

const last = (list, f, key = 'at') => {
  let i = -1;
  list.forEach((x, k) => { if (f >= fr(x[key])) i = k; });
  return i;
};

const useLevel = (f) => {
  const {fps} = useVideoConfig();
  const env = ENVELOPE.v || [];
  const k = Math.round(f * (ENVELOPE.fps || 30) / fps);
  return (o = 0) => env[Math.min(env.length - 1, Math.max(0, k + o))] || 0;
};

const Bars = ({f, color, on}) => {
  const level = useLevel(f);
  const {n, top, h} = L.wave;
  const gap = LAND ? 8 : 6, w = (PF_W - gap * (n - 1)) / n;
  return (
    <div style={{position: 'absolute', left: PF.left, top, width: PF_W, height: h, display: 'flex', alignItems: 'center', gap}}>
      {Array.from({length: n}).map((_, i) => {
        // mỗi cột lấy độ lớn tiếng lệch vài khung + hình chuông ở giữa → sóng "chạy" theo giọng, không giật
        const bell = 0.35 + 0.65 * Math.sin(Math.PI * (i + 0.5) / n);
        const jitter = 0.6 + 0.4 * Math.abs(Math.sin(i * 12.9898 + f * 0.21));
        const v = Math.min(1, level(-Math.abs(i - n / 2) % 6) * bell * jitter * 0.95);
        return <div key={i} style={{width: w, height: Math.max(6, v * h), borderRadius: w / 2,
          background: on ? color : C.dim, opacity: on ? 0.55 + 0.45 * v : 0.5}} />;
      })}
    </div>
  );
};

// Ngang: vòng tròn đồng tâm phát theo giọng (lấp khoảng phải, khung không bao giờ đứng yên)
const Ring = ({f, color, on}) => {
  const level = useLevel(f);
  const {x, y, r} = L.ring;
  const v = level();
  return (
    <>
      {[0, 1, 2].map((i) => {
        const t = ((f / 45 + i / 3) % 1);
        return <div key={i} style={{position: 'absolute', left: x, top: y, width: r * 2, height: r * 2, borderRadius: r,
          border: `3px solid ${on ? color : C.dim}`, opacity: (1 - t) * (on ? 0.5 : 0.2),
          transform: `translate(-50%, -50%) scale(${0.7 + t * 0.9})`}} />;
      })}
      <div style={{position: 'absolute', left: x, top: y, width: r * 1.1, height: r * 1.1, borderRadius: r,
        background: on ? color : C.dim, opacity: 0.9, transform: `translate(-50%, -50%) scale(${0.85 + 0.25 * v})`,
        boxShadow: on ? `0 0 ${60 + 60 * v}px ${color}88` : 'none', display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
        <svg width={r * 0.55} height={r * 0.55} viewBox="0 0 24 24" fill="none" stroke={C.bg} strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round">
          <rect x="9" y="3" width="6" height="11" rx="3" /><path d="M5 11a7 7 0 0 0 14 0M12 18v3" />
        </svg>
      </div>
    </>
  );
};

export const Stage = () => {
  const f = useCurrentFrame();
  const {show = '', title = '', speakers = []} = STAGE || {};
  const turns = SPEAKERS.turns || [];
  const ti = last(turns, f, 'start');
  const now = ti >= 0 && f < fr(turns[ti].end) + 6 ? turns[ti].spk : -1;   // ai đang nói (−1: lặng)
  const color = SPK[Math.max(0, now) % SPK.length];
  const named = speakers.filter((s) => s && s.name);
  // Ý đang bàn: ẩn khi lớp phủ (thẻ, chữ to, hook) chiếm vùng giữa
  const busy = SCENES.some((s) => !FULL.has(s.type) && f >= fr(s.start) - 6 && f < fr(s.end) + 6);
  const ki = last(TOPICS || [], f);
  const kw = ki >= 0 ? TOPICS[ki] : null;
  const kIn = kw ? pop(f, fr(kw.at)) : 0;
  // BẢN ĐỒ CHƯƠNG TÍCH LUỸ (David duyệt 2026-11-05, học Hieu Nguyen: người xem luôn biết mình đang ở đâu): ≥ 3 TOPICS → mỗi phần thêm
  // một thẻ số + tên phần dưới ý đang bàn; 5,5 s trước màn chốt hiện cả bản đồ làm TÓM TẮT (thay ý đang bàn). STAGE.map = false để tắt.
  const {durationInFrames: DUR, fps: FPS0} = useVideoConfig();
  const MAP = (TOPICS || []).length >= 3 && DUR / FPS0 > 300 && !(STAGE && STAGE.map === false);   // chỉ tập dài > 5 phút (ít mà sâu)
  const ctaS = (SCENES.find((s) => s.type === 'cta') || {}).start;
  const recap = MAP && ctaS != null && f >= fr(ctaS - 5.5) && f < fr(ctaS) ? ease(f, fr(ctaS - 5.5), fr(ctaS - 5.5) + 10) : 0;
  const kSize = kw ? Math.min(MAP ? L.map.maxTopic : L.topic.max, Math.floor(L.topic.w / (Math.max(...kw.text.split('\n').map((l) => l.length)) * 0.46))) : 0;
  const drift = Math.sin(f / 240) * 8;
  const {fps: FPSv} = useVideoConfig();
  const bgs = Array.isArray(STAGE && STAGE.bg) ? STAGE.bg : [];
  const bgSrc = bgs.filter((b) => f >= fr(b.at || 0)).pop() || null;
  // THẺ CHƯƠNG (PO-1): 3 s đầu mỗi ý lớn hiện "PHẦN n" trên ý đang bàn (đánh số theo TOPICS)
  const chapIn = kw ? ease(f, fr(kw.at), fr(kw.at) + 8) * (1 - ease(f, fr(kw.at) + fr(3), fr(kw.at) + fr(3.6))) : 0;
  return (
    <AbsoluteFill style={{background: C.bg}}>
      <AbsoluteFill style={{background: `radial-gradient(circle at ${(LAND ? 35 : 45) + drift}% ${(LAND ? 40 : 36) - drift / 2}%, rgba(255,122,69,0.16), transparent 58%)`}} />
      {/* NỀN "LẮNG" (David duyệt 2026-11-04, học VOV / Tu Thân / Minh Niệm radio): STAGE.bg = [{at, src}] ảnh/tranh trong public/
          (chỉ tranh/ảnh có giấy phép hoặc David đưa) — chuyển động rất chậm (Ken Burns), phủ tối để chữ đọc rõ; không có thì lưới tối như cũ */}
      {bgSrc ? <AbsoluteFill>
        <Img src={staticFile(bgSrc.src)} style={{width: '100%', height: '100%', objectFit: 'cover',
          transform: `scale(${1.04 + Math.min(0.1, ((f - fr(bgSrc.at || 0)) / FPSv) * 0.0016)})`, transformOrigin: '50% 40%'}} />
        <AbsoluteFill style={{background: 'linear-gradient(180deg, rgba(13,13,16,0.55), rgba(13,13,16,0.78))'}} />
      </AbsoluteFill>
      : <AbsoluteFill style={{backgroundImage: `linear-gradient(${C.line} 2px, transparent 2px), linear-gradient(90deg, ${C.line} 2px, transparent 2px)`,
        backgroundSize: '120px 120px', backgroundPosition: `0 ${(f * 0.3) % 120}px`, opacity: 0.3,
        maskImage: 'radial-gradient(circle at 50% 42%, black, transparent 75%)'}} />}
      {/* Tên chương trình (nếu có) + tên tập */}
      <div style={{position: 'absolute', left: PF.left, top: L.headTop, width: L.titleW}}>
        {/* dấu kênh chung ● DAVID │ tên chương trình (thay ô tên chương trình cũ — nhận diện 4 loại video, 2026-11-04) */}
        <BrandMark topic={show} style={{marginBottom: 16}} />
        {title && <div style={{fontFamily: BODY, fontWeight: 700, fontSize: L.titleSize, lineHeight: 1.25, color: C.text,
          textWrap: 'balance'}}>{title}</div>}
      </div>
      {/* Ý đang bàn */}
      {kw && (
        <div style={{position: 'absolute', left: PF.left, width: L.topic.w, top: L.topic.top, opacity: busy || recap || (HL && HL.chu_chinh) ? 0 : 1}}>
          {(TOPICS || []).length > 1 && <div style={{position: 'absolute', top: -kSize * 0.75, fontFamily: HEAD, fontWeight: 800,
            fontSize: Math.round(kSize * 0.42), letterSpacing: 4, color: C.accent, opacity: chapIn}}>PHẦN {ki + 1}</div>}
          <div style={{overflow: 'hidden', paddingTop: kSize * VN.top, marginTop: -kSize * VN.top, paddingBottom: kSize * VN.bot, marginBottom: -kSize * VN.bot}}>
            {kw.text.split('\n').map((l, i) => (
              <div key={`${ki}-${i}`} style={{fontFamily: HEAD, fontWeight: 800, fontSize: kSize, lineHeight: VN.lh, color: i ? C.accent : C.text,
                marginTop: i ? kSize * VN.gap : 0,   // chừa chỗ dấu nặng dòng trên + dấu chồng dòng dưới
                textTransform: 'uppercase', transform: `translateY(${(1 - kIn) * 110}%)`}}>{l}</div>
            ))}
          </div>
          <div style={{height: 9, marginTop: 26, borderRadius: 5, background: C.accent, width: `${ease(f, fr(kw.at) + 6, fr(kw.at) + 20) * 40}%`}} />
        </div>
      )}
      {/* bản đồ chương: các phần đã qua (mờ, có số) + phần đang nói (cam) */}
      {MAP && ki >= 0 && !recap && (
        <div style={{position: 'absolute', left: PF.left, width: L.topic.w, top: L.map.top, display: 'flex', alignItems: 'center', gap: 10, opacity: busy ? 0 : 1}}>
          {TOPICS.slice(0, ki + 1).map((t, i) => {
            const on = i === ki, a = ease(f, fr(t.at), fr(t.at) + 10);
            if (!on) return (   // phần đã qua: chỉ chấm số (luôn gọn một dòng — tên đầy đủ có ở tóm tắt cuối)
              <div key={i} style={{width: L.map.size * 1.7, height: L.map.size * 1.7, borderRadius: L.map.size, border: `2px solid ${C.dim}`, opacity: a * 0.7,
                background: 'rgba(255,255,255,0.06)', color: C.text, fontFamily: HEAD, fontWeight: 800, fontSize: L.map.size * 0.85,
                display: 'flex', alignItems: 'center', justifyContent: 'center'}}>{i + 1}</div>);
            return (
              <div key={i} style={{display: 'flex', alignItems: 'center', gap: 8, padding: '5px 14px 5px 6px', borderRadius: 30, opacity: a * (on ? 1 : 0.62),
                background: on ? C.accent : 'rgba(255,255,255,0.06)', border: `2px solid ${on ? C.accent : C.dim}`}}>
                <div style={{width: L.map.size * 1.35, height: L.map.size * 1.35, borderRadius: L.map.size, background: on ? C.bg : C.dim, color: on ? C.accent : C.text,
                  fontFamily: HEAD, fontWeight: 800, fontSize: L.map.size * 0.85, display: 'flex', alignItems: 'center', justifyContent: 'center'}}>{i + 1}</div>
                <div style={{fontFamily: BODY, fontWeight: 700, fontSize: L.map.size, color: on ? C.bg : C.text, whiteSpace: 'nowrap'}}>{t.text.replace(/\n/g, ' ')}</div>
              </div>
            );
          })}
        </div>
      )}
      {/* tóm tắt cả bài (5,5 s trước màn chốt) */}
      {recap > 0 && (
        <div style={{position: 'absolute', left: PF.left, width: L.topic.w, top: LAND ? 230 : 520, opacity: recap,
          display: 'grid', gridTemplateColumns: LAND && TOPICS.length > 5 ? '1fr 1fr' : '1fr', columnGap: 40, rowGap: LAND ? 16 : 18}}>
          {TOPICS.map((t, i) => (
            <div key={i} style={{display: 'flex', alignItems: 'center', gap: 16, opacity: ease(f, fr(ctaS - 5.5) + i * 3, fr(ctaS - 5.5) + i * 3 + 8)}}>
              <div style={{minWidth: 52, height: 52, borderRadius: 26, background: C.accent, color: C.bg, fontFamily: HEAD, fontWeight: 800, fontSize: 30,
                display: 'flex', alignItems: 'center', justifyContent: 'center'}}>{i + 1}</div>
              <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: LAND ? 38 : 40, lineHeight: 1.2, paddingTop: '0.1em', color: C.text, textTransform: 'uppercase'}}>{t.text.replace(/\n/g, ' ')}</div>
            </div>
          ))}
        </div>
      )}
      {LAND && <Ring f={f} color={color} on={now >= 0} />}
      {/* Tên người nói — chỉ khi biết tên */}
      {named.length > 0 && (
        <div style={LAND   // ngang: dưới vòng micro (lớp phủ canh trái không chạm tới); dọc: hàng trên sóng âm
          ? {position: 'absolute', left: L.ring.x - 260, width: 520, top: L.ring.y + L.ring.r + 30, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 10}
          : {position: 'absolute', left: PF.left, width: PF_W, top: L.chips.top, display: 'flex', gap: 40}}>
          {speakers.map((s, i) => s && s.name && (
            <div key={i} style={{display: 'flex', alignItems: 'center', gap: 14, opacity: now === i ? 1 : 0.45}}>
              <div style={{width: 18, height: 18, borderRadius: 9, background: SPK[i % SPK.length],
                boxShadow: now === i ? `0 0 ${16 + 8 * Math.sin(f / 6)}px ${SPK[i % SPK.length]}` : 'none'}} />
              <div style={{fontFamily: BODY, fontWeight: 700, fontSize: 34, color: C.text, whiteSpace: 'nowrap'}}>{s.name}</div>
              {s.role && <div style={{fontFamily: BODY, fontWeight: 500, fontSize: 26, color: C.muted, whiteSpace: 'nowrap'}}>{s.role}</div>}
            </div>
          ))}
        </div>
      )}
      <Bars f={f} color={color} on={now >= 0} />
    </AbsoluteFill>
  );
};
