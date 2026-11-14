// Tự tổng hợp hiệu ứng âm thanh + nhạc nền (không bản quyền): node tao-am-thanh.mjs
import fs from 'node:fs';

const SR = 48000;
const out = 'public/hieu-ung-am-thanh';
fs.mkdirSync(out, {recursive: true});

const wav = (name, L, R = L) => {
  const n = L.length, buf = Buffer.alloc(44 + n * 4);
  buf.write('RIFF', 0); buf.writeUInt32LE(36 + n * 4, 4); buf.write('WAVEfmt ', 8);
  buf.writeUInt32LE(16, 16); buf.writeUInt16LE(1, 20); buf.writeUInt16LE(2, 22);
  buf.writeUInt32LE(SR, 24); buf.writeUInt32LE(SR * 4, 28); buf.writeUInt16LE(4, 32); buf.writeUInt16LE(16, 34);
  buf.write('data', 36); buf.writeUInt32LE(n * 4, 40);
  for (let i = 0; i < n; i++) {
    buf.writeInt16LE(Math.round(Math.max(-1, Math.min(1, L[i])) * 32767), 44 + i * 4);
    buf.writeInt16LE(Math.round(Math.max(-1, Math.min(1, R[i])) * 32767), 46 + i * 4);
  }
  fs.writeFileSync(`${out}/${name}.wav`, buf);
};
const arr = (sec) => new Float32Array(Math.round(sec * SR));
const norm = (a, peak = 0.9) => { let m = 0; for (const v of a) m = Math.max(m, Math.abs(v)); for (let i = 0; i < a.length; i++) a[i] *= peak / (m || 1); return a; };
let seed = 7; const rnd = () => ((seed = (seed * 16807) % 2147483647) / 2147483647) * 2 - 1;
// Lọc một cực đơn giản
const lp = (a, fc) => { const k = 1 - Math.exp(-2 * Math.PI * fc / SR); let y = 0; for (let i = 0; i < a.length; i++) a[i] = y += k * (a[i] - y); return a; };
const hp = (a, fc) => { const b = Float32Array.from(a); lp(b, fc); for (let i = 0; i < a.length; i++) a[i] -= b[i]; return a; };

// whoosh: tiếng gió quét
{ const a = arr(0.55); let y1 = 0, y2 = 0;
  for (let i = 0; i < a.length; i++) { const t = i / a.length; const fc = 300 + 5000 * Math.sin(Math.PI * t);
    const k = 1 - Math.exp(-2 * Math.PI * fc / SR); y1 += k * (rnd() - y1); y2 += k * (y1 - y2);
    a[i] = (y1 - y2) * Math.sin(Math.PI * t) ** 2; }
  wav('whoosh', norm(a, 0.8)); }

// ding: chuông (3 cao độ tăng dần cho 1-2-3 năm)
[[1318.5, 'ding1'], [1568, 'ding2'], [1760, 'ding3'], [2093, 'ding4']].forEach(([f, name]) => {
  const a = arr(0.9);
  for (let i = 0; i < a.length; i++) { const t = i / SR;
    a[i] = (Math.sin(2 * Math.PI * f * t) + 0.45 * Math.sin(2 * Math.PI * f * 2.76 * t) * Math.exp(-t * 9) + 0.25 * Math.sin(2 * Math.PI * f * 5.4 * t) * Math.exp(-t * 18)) * Math.exp(-t * 4.5) * Math.min(1, t * 400); }
  wav(name, norm(a, 0.7)); });

// boom: trống trầm điện ảnh
{ const a = arr(1.4); let ph = 0;
  for (let i = 0; i < a.length; i++) { const t = i / SR; const f = 38 + 90 * Math.exp(-t * 7); ph += 2 * Math.PI * f / SR;
    a[i] = Math.sin(ph) * Math.exp(-t * 2.6) + 0.35 * rnd() * Math.exp(-t * 22); }
  lp(a, 2500); wav('boom', norm(a, 0.95)); }

// pop: bật chữ
{ const a = arr(0.12); let ph = 0;
  for (let i = 0; i < a.length; i++) { const t = i / SR; ph += 2 * Math.PI * (500 + 9000 * t) / SR; a[i] = Math.sin(ph) * Math.exp(-t * 35); }
  wav('pop', norm(a, 0.7)); }

// shutter: máy ảnh chụp (đóng băng khung)
{ const a = arr(0.25);
  for (let i = 0; i < a.length; i++) { const t = i / SR; a[i] = rnd() * (Math.exp(-t * 120) + (t > 0.09 ? 0.8 * Math.exp(-(t - 0.09) * 90) : 0)); }
  hp(a, 1500); wav('shutter', norm(a, 0.8)); }

// rewind: tua băng
{ const a = arr(0.8); let ph = 0;
  for (let i = 0; i < a.length; i++) { const t = i / a.length; const f = 200 + 1800 * t * t; ph += 2 * Math.PI * f / SR;
    a[i] = (Math.sign(Math.sin(ph)) * 0.35 + rnd() * 0.5) * Math.sin(Math.PI * t) * (0.7 + 0.3 * Math.sin(2 * Math.PI * 22 * i / SR)); }
  lp(a, 4000); wav('rewind', norm(a, 0.6)); }

// sting: hợp âm đi lên cho tiêu đề
{ const a = arr(2.2); const notes = [523.25, 659.25, 783.99, 1046.5];
  notes.forEach((f, k) => { const s = k * 0.09;
    for (let i = Math.round(s * SR); i < a.length; i++) { const t = i / SR - s;
      a[i] += (Math.sin(2 * Math.PI * f * t) + 0.3 * Math.sin(4 * Math.PI * f * t) + 0.15 * Math.sin(6 * Math.PI * f * t)) * Math.exp(-t * 1.6) * Math.min(1, t * 300); } });
  wav('sting', norm(a, 0.6)); }

// tada: chúc mừng (kèn đồng giả lập)
{ const a = arr(2.0); const chord = [[523.25, 0], [659.25, 0], [783.99, 0], [1046.5, 0.18], [1318.5, 0.18]];
  chord.forEach(([f, s]) => { let ph = 0;
    for (let i = Math.round(s * SR); i < a.length; i++) { const t = i / SR - s; ph += 2 * Math.PI * f * (1 + 0.004 * Math.sin(2 * Math.PI * 5.5 * t)) / SR;
      let v = 0; for (let h = 1; h <= 6; h++) v += Math.sin(h * ph) / h; a[i] += v * Math.min(1, t * 30) * Math.exp(-Math.max(0, t - 0.5) * 2.2); } });
  lp(a, 3500); wav('tada', norm(a, 0.6)); }

// Nhạc nền 118 BPM, vòng hợp âm C - Am - F - G, ~80 s
{ const BPM = 118, beat = 60 / BPM, dur = 80, L = arr(dur), R = arr(dur);
  const chords = [[261.63, 329.63, 392], [220, 261.63, 329.63], [174.61, 220, 261.63], [196, 246.94, 293.66]];
  const bassRoot = [65.41, 55, 43.65, 49];
  const add = (buf, i0, gen, len) => { for (let i = 0; i < len && i0 + i < buf.length; i++) buf[i0 + i] += gen(i / SR); };
  const nBeats = Math.floor(dur / beat);
  for (let b = 0; b < nBeats; b++) {
    const t0 = Math.round(b * beat * SR), bar = Math.floor(b / 4), ch = chords[bar % 4], root = bassRoot[bar % 4];
    // kick
    let ph = 0; const kick = (t) => { ph += 2 * Math.PI * (45 + 100 * Math.exp(-t * 30)) / SR; return 0.9 * Math.sin(ph) * Math.exp(-t * 7); };
    add(L, t0, kick, SR * 0.35); ph = 0; add(R, t0, kick, SR * 0.35);
    // clap ở phách 2 và 4
    if (b % 2 === 1) { const c = (t) => 0.35 * rnd() * (Math.exp(-t * 30) + 0.5 * Math.exp(-Math.abs(t - 0.012) * 300)); add(L, t0, c, SR * 0.2); add(R, t0, c, SR * 0.2); }
    // hi-hat nửa phách
    const hh = (t) => 0.12 * rnd() * Math.exp(-t * 90);
    add(L, t0 + Math.round(beat * SR / 2), hh, SR * 0.05); add(R, t0 + Math.round(beat * SR / 2) + 40, hh, SR * 0.05);
    // bass nảy theo móc 1/8
    [0, 0.5].forEach((o, k) => { const f = root * (k ? 2 : 1); let p = 0;
      const bass = (t) => { p += 2 * Math.PI * f / SR; return 0.32 * (Math.sin(p) + 0.3 * Math.sin(2 * p)) * Math.exp(-t * 6); };
      add(L, t0 + Math.round(o * beat * SR), bass, SR * beat * 0.5); p = 0; add(R, t0 + Math.round(o * beat * SR), bass, SR * beat * 0.5); });
    // hợp âm pluck ở phách lệch (off-beat) kiểu vui tươi
    ch.forEach((f, k) => { const pl = (t) => 0.07 * (Math.sin(2 * Math.PI * f * 2 * t) + 0.4 * Math.sin(2 * Math.PI * f * 4 * t)) * Math.exp(-t * 9);
      add(k % 2 ? L : R, t0 + Math.round(beat * SR / 2), pl, SR * 0.4); add(k % 2 ? R : L, t0 + Math.round(beat * SR / 2), (t) => 0.5 * pl(t), SR * 0.4); });
    // giai điệu chuông nhỏ mỗi 2 phách
    if (b % 2 === 0) { const mel = [ch[2] * 2, ch[1] * 2, ch[0] * 4, ch[2] * 2][(b / 2) % 4];
      add(L, t0, (t) => 0.06 * Math.sin(2 * Math.PI * mel * t) * Math.exp(-t * 5), SR * 0.6);
      add(R, t0, (t) => 0.06 * Math.sin(2 * Math.PI * mel * t) * Math.exp(-t * 5), SR * 0.6); }
  }
  lp(L, 9000); lp(R, 9000);
  let m = 0; for (let i = 0; i < L.length; i++) m = Math.max(m, Math.abs(L[i]), Math.abs(R[i]));
  for (let i = 0; i < L.length; i++) { L[i] = Math.tanh(L[i] / m * 1.2) * 0.8; R[i] = Math.tanh(R[i] / m * 1.2) * 0.8; }
  wav('nhac', L, R); }

console.log('ok', fs.readdirSync(out).join(' '));
