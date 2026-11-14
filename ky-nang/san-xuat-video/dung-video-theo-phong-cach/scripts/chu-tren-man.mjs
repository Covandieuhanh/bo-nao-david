#!/usr/bin/env node
// BẢNG TỰ SỬA CHỮ (khối 03 + 07, 2026-11-06): David sửa chữ / số trên màn hình và phụ đề trong một file chữ, không cần Claude.
//   node chu-tren-man.mjs xuat <dự án>            → <dự án>/chu-tren-man.txt (kèm bản gốc .chu-tren-man.json để nhận biết thay đổi)
//   node chu-tren-man.mjs ap <dự án> [--render]   → ghi phần đã sửa vào canh.js / phu-de.js, báo cảnh cần render lại
//                                                   --render: render lại đúng các cảnh đó + xuất lại video-hoan-chinh.mp4
// An toàn: sao lưu vào kiem-tra/truoc-sua-chu/ trước khi ghi · chữ vừa bị sửa ở cả bảng lẫn kịch bản → KHÔNG ghi, liệt kê để hỏi ·
// ghi xong đọc thử lại kịch bản, lỗi thì trả bản cũ · không đoán khi không xác định được chỗ cần sửa.
// Chưa làm: dự án ghép (danh-sach-cat.js / ke-hoach.json) — sửa qua Claude.
import fs from 'node:fs';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import {fileURLToPath, pathToFileURL} from 'node:url';

const [cmd, arg] = process.argv.slice(2);
const P = path.resolve((arg || '').replace(/^~/, process.env.HOME));
const SRC = path.join(P, 'chuyen-dong/src');
const F = {scenes: path.join(SRC, 'canh.js'), caps: path.join(SRC, 'phu-de.js'), sheet: path.join(P, 'chu-tren-man.txt'), base: path.join(P, '.chu-tren-man.json'), cho: path.join(P, '.chu-tren-man.cho.json')};
if (!['xuat', 'ap'].includes(cmd) || !arg || !fs.existsSync(F.scenes)) {
  console.error('cách dùng: chu-tren-man.mjs xuat|ap <dự án> [--render] (dự án có chuyen-dong/src/canh.js)');
  process.exit(2);
}
const fresh = async (f) => import(pathToFileURL(f).href + '?t=' + Date.now());

const SKIP = new Set(['id', 'type', 'icon', 'photo', 'mode', 'pos', 'kind', 'credit', 'src', 'place', 'c']);
const NUMS = new Set(['to', 'value', 'upto', 'total']);
const hasLetter = (s) => /[\p{L}\p{N}]/u.test(s);
// Mọi giá trị trong một cảnh theo đúng thứ tự viết: strings = mọi chuỗi (để đếm vị trí), edit = phần được sửa
const walk = (o, pre, out) => {
  for (const [k, v] of Object.entries(o)) {
    const p = pre ? `${pre}.${k}` : k;
    if (typeof v === 'string') { out.strings.push(v); if (!SKIP.has(k) && hasLetter(v)) out.edit.push({path: p, value: v}); }
    else if (typeof v === 'number') { if (NUMS.has(k)) out.edit.push({path: p, value: v, num: true, key: k}); }
    else if (v && typeof v === 'object') walk(v, p, out);
  }
  return out;
};
const show = (v) => String(v).replace(/\\/g, '\\\\').replace(/\n/g, '\\n');
const unshow = (s) => s.replace(/\\(n|\\)/g, (_, c) => (c === 'n' ? '\n' : '\\'));
const mmss = (t) => `${Math.floor(t / 60)}:${String(Math.floor(t % 60)).padStart(2, '0')}`;

async function collect() {
  const m = await fresh(F.scenes);
  const rows = [];
  (m.SCENES || []).forEach((s) => {
    walk({...(s.props || {})}, '', {strings: [], edit: []}).edit.forEach((e) =>
      rows.push({region: 'scene', owner: s.id, start: s.start, type: s.type, ...e}));
  });
  (m.TOPICS || []).forEach((t, i) => { if (t.text) rows.push({region: 'topics', owner: `TOPICS`, idx: i, start: t.at, path: 'text', value: t.text}); });
  const caps = fs.existsSync(F.caps) ? (await fresh(F.caps)).default || [] : [];
  caps.forEach((c, i) => rows.push({region: 'caps', owner: 'phu-de', idx: i, start: c.start, path: 'text', value: c.text}));
  return rows;
}

const keyOf = (r) => `${r.region}|${r.owner}|${r.idx ?? ''}|${r.path}`;

if (cmd === 'xuat') {
  const rows = await collect();
  const out = ['# CHỮ TRÊN MÀN HÌNH — chỉ sửa phần sau dấu | rồi lưu file. Không đổi số ở đầu dòng. \\n = xuống dòng.',
    '# Xong chạy lệnh "ap" (khối 03). Chữ phụ đề giữ đúng lời đã nói; số thì chỉ ghi số.', ''];
  const base = {};
  let group = null, n = 0;
  for (const r of rows) {
    const g = r.region === 'scene' ? `## ${r.owner} · ${mmss(r.start)} · ${r.type}` : r.region === 'topics' ? '## Ý đang bàn (podcast)' : '## Phụ đề';
    if (g !== group) { if (group) out.push(''); out.push(g); group = g; }
    n += 1;
    const id = String(n).padStart(3, '0');
    out.push(`${id}${r.region === 'scene' ? '' : ` (${mmss(r.start)})`} | ${show(r.value)}`);
    base[id] = {key: keyOf(r), region: r.region, owner: r.owner, idx: r.idx, path: r.path, value: r.value, num: !!r.num, numKey: r.key};
  }
  fs.writeFileSync(F.sheet, out.join('\n') + '\n');
  fs.writeFileSync(F.base, JSON.stringify(base, null, 1));
  console.log(`${F.sheet} (${n} dòng)`);
  process.exit(0);
}

// ---------- ap ----------
if (!fs.existsSync(F.sheet) || !fs.existsSync(F.base)) { console.error('Chưa có bảng: chạy "xuat" trước.'); process.exit(2); }
const base = JSON.parse(fs.readFileSync(F.base, 'utf8'));
const edits = [], lost = [];
const seen = new Set();
for (const line of fs.readFileSync(F.sheet, 'utf8').split('\n')) {
  const m = /^(\d{3})(?: \([^)]*\))? \| ?(.*)$/.exec(line);
  if (!m) continue;
  seen.add(m[1]);
  const b = base[m[1]];
  if (!b) { lost.push(`dòng ${m[1]} không có trong bản gốc`); continue; }
  const v = unshow(m[2].trimEnd());
  if (b.num) {
    const num = Number(v.replace(',', '.'));
    if (!Number.isFinite(num)) { lost.push(`dòng ${m[1]}: "${v}" không phải số`); continue; }
    if (num !== b.value) edits.push({...b, id: m[1], next: num});
  } else if (v !== b.value) {
    if (!v.trim()) { lost.push(`dòng ${m[1]}: đang để trống (muốn bỏ chữ này thì nhờ Claude)`); continue; }
    edits.push({...b, id: m[1], next: v});
  }
}
for (const id of Object.keys(base)) if (!seen.has(id)) lost.push(`dòng ${id} đã bị xoá khỏi bảng`);
if (lost.length) { console.log('Chưa ghi gì vì bảng có chỗ chưa ổn:'); lost.forEach((x) => console.log(`- ${x}`)); process.exit(1); }
const WANT_RENDER = process.argv.includes('--render');
const HERE = path.dirname(fileURLToPath(import.meta.url));
const pending = () => { try { return JSON.parse(fs.readFileSync(F.cho, 'utf8')); } catch { return []; } };
// Render các cảnh đang chờ (kể cả từ lần "ap" trước chưa render) rồi xuất lại bản cuối
const renderNow = (ids) => {
  const env = {...process.env, PATH: `/opt/homebrew/bin:${path.dirname(process.execPath)}:${process.env.PATH}`};
  const r = spawnSync(process.execPath, ['xuat-video.mjs', ...ids], {cwd: path.join(P, 'chuyen-dong'), stdio: 'inherit', env});
  if (r.status) process.exit(r.status);
  const q = spawnSync('python3', ['-I', path.join(HERE, 'xem-truoc-ban-dung.py'), P], {stdio: 'inherit', env});
  if (q.status) process.exit(q.status);
  fs.rmSync(F.cho, {force: true});
  console.log(`Xong: ${path.join(P, 'video-hoan-chinh.mp4')}`);
};
if (!edits.length) {
  const cho = pending();
  if (WANT_RENDER && cho.length) { console.log(`Bảng không đổi thêm. Render các cảnh đang chờ: ${cho.join(' ')}`); renderNow(cho); }
  else console.log(cho.length ? `Bảng không đổi thêm. Còn chờ render: ${cho.join(' ')}` : 'Bảng không có thay đổi.');
  process.exit(0);
}

// Kịch bản có bị sửa từ lúc xuất bảng không?
const now = Object.fromEntries((await collect()).map((r) => [keyOf(r), r.value]));
const conflicts = edits.filter((e) => now[e.key] !== e.value);
if (conflicts.length) {
  console.log('Chưa ghi gì: những chữ này đã đổi trong kịch bản sau khi xuất bảng. Hỏi David giữ bản nào, hoặc xuất lại bảng:');
  conflicts.forEach((c) => console.log(`- dòng ${c.id}: bảng "${c.next}" · kịch bản "${now[c.key] ?? '(không còn)'}"`));
  process.exit(1);
}

// Tìm và thay đúng literal trong mã nguồn
const LIT = /'(?:[^'\\\n]|\\.)*'|"(?:[^"\\\n]|\\.)*"|`(?:[^`\\]|\\.)*`/g;
const dec = (l) => l.slice(1, -1).replace(/\\(.)/g, (_, c) => ({n: '\n', t: '\t'}[c] ?? c));
const enc = (v, q) => q + v.replace(/\\/g, '\\\\').replace(new RegExp(q, 'g'), `\\${q}`).replace(/\n/g, '\\n') + q;
const literals = (src, from, to) => [...src.slice(from, to).matchAll(LIT)].map((m) => ({i: from + m.index, raw: m[0], val: dec(m[0])}));

let scenesSrc = fs.readFileSync(F.scenes, 'utf8');
let capsSrc = fs.existsSync(F.caps) ? fs.readFileSync(F.caps, 'utf8') : '';
const fail = [];
const mod = await fresh(F.scenes);
const blockOf = (src, id) => {
  const re = new RegExp(`\\bid:\\s*['"\`]${id.replace(/[-/\\^$*+?.()|[\]{}]/g, '\\$&')}['"\`]`);
  const m = re.exec(src);
  if (!m) return null;
  const rest = src.slice(m.index + m[0].length);
  const nx = /\bid:\s*['"`]/.exec(rest), close = /\n\];/.exec(rest);
  const span = Math.min(nx ? nx.index : Infinity, close ? close.index : Infinity);
  return span === Infinity ? null : [m.index, m.index + m[0].length + span];
};
const getByPath = (o, p) => p.split('.').reduce((a, k) => (a == null ? a : a[k]), o);

// thay từ cuối file lên đầu để không lệch vị trí
const plan = {scenes: [], caps: []};
for (const e of edits) {
  if (e.region === 'caps') {
    const start = capsSrc.indexOf('export default');
    const texts = [...capsSrc.slice(start).matchAll(/\btext:\s*('(?:[^'\\\n]|\\.)*'|"(?:[^"\\\n]|\\.)*"|`(?:[^`\\]|\\.)*`)/g)];
    const m = texts[e.idx];
    if (!m || dec(m[1]) !== e.value) { fail.push(e); continue; }
    plan.caps.push({i: start + m.index + m[0].length - m[1].length, len: m[1].length, text: enc(e.next, m[1][0])});
  } else if (e.region === 'topics') {
    const a = scenesSrc.search(/export const TOPICS\s*=\s*\[/), z = a < 0 ? -1 : scenesSrc.indexOf('\n];', a);
    if (a < 0 || z < 0) { fail.push(e); continue; }
    const same = literals(scenesSrc, a, z).filter((l) => l.val === e.value);
    if (same.length !== 1) { fail.push(e); continue; }
    plan.scenes.push({i: same[0].i, len: same[0].raw.length, text: enc(e.next, same[0].raw[0])});
  } else {
    const scene = (mod.SCENES || []).find((s) => s.id === e.owner), blk = blockOf(scenesSrc, e.owner);
    if (!scene || !blk) { fail.push(e); continue; }
    if (e.num) {
      const hits = [...scenesSrc.slice(...blk).matchAll(new RegExp(`\\b${e.numKey}:\\s*${String(e.value).replace('.', '\\.')}\\b`, 'g'))];
      if (hits.length !== 1) { fail.push(e); continue; }
      const h = hits[0], n = h[0].length - String(e.value).length;
      plan.scenes.push({i: blk[0] + h.index + n, len: String(e.value).length, text: String(e.next)});
      continue;
    }
    const lits = literals(scenesSrc, ...blk).slice(1).filter((l) => l.val === e.value);   // bỏ literal id
    if (lits.length === 1) { plan.scenes.push({i: lits[0].i, len: lits[0].raw.length, text: enc(e.next, lits[0].raw[0])}); continue; }
    // cùng chữ nhiều chỗ: lấy theo thứ tự viết, chỉ khi số lần khớp đúng với dữ liệu
    const w = walk({...(scene.props || {})}, '', {strings: [], edit: []});
    const samePaths = w.edit.filter((x) => x.value === e.value).map((x) => x.path);
    const k = samePaths.indexOf(e.path), all = w.strings.filter((x) => x === e.value).length;
    if (lits.length && lits.length === all && all === samePaths.length && k >= 0) plan.scenes.push({i: lits[k].i, len: lits[k].raw.length, text: enc(e.next, lits[k].raw[0])});
    else fail.push(e);
  }
}
if (fail.length) {
  console.log('Chưa ghi gì: không xác định chắc được chỗ sửa của những dòng này (nhờ Claude sửa):');
  fail.forEach((e) => console.log(`- dòng ${e.id} (${e.owner}): "${e.value}"`));
  process.exit(1);
}
const patch = (src, ops) => [...ops].sort((a, b) => b.i - a.i).reduce((s, o) => s.slice(0, o.i) + o.text + s.slice(o.i + o.len), src);

// Sao lưu → ghi → đọc thử
const bak = path.join(P, 'kiem-tra/truoc-sua-chu');
fs.mkdirSync(bak, {recursive: true});
fs.copyFileSync(F.scenes, path.join(bak, 'canh.js'));
if (capsSrc) fs.copyFileSync(F.caps, path.join(bak, 'phu-de.js'));
const scenesOld = scenesSrc, capsOld = capsSrc;
if (plan.scenes.length) fs.writeFileSync(F.scenes, patch(scenesSrc, plan.scenes));
if (plan.caps.length) fs.writeFileSync(F.caps, patch(capsSrc, plan.caps));

let bad = null;
const after = await collect().catch((err) => { bad = err.message; return []; });
if (!bad) {
  const map = Object.fromEntries(after.map((r) => [keyOf(r), r.value]));
  const wrong = edits.filter((e) => map[e.key] !== e.next);
  if (wrong.length) bad = `dòng ${wrong.map((e) => e.id).join(', ')} không ra đúng chữ đã sửa`;
}
if (bad) {
  fs.writeFileSync(F.scenes, scenesOld); if (capsOld) fs.writeFileSync(F.caps, capsOld);
  console.log(`Đã trả lại bản cũ vì đọc thử không đạt: ${bad}`);
  process.exit(1);
}
// Bản gốc mới: bảng và kịch bản khớp nhau
for (const e of edits) base[e.id].value = e.next;
fs.writeFileSync(F.base, JSON.stringify(base, null, 1));

const ids = [...new Set([...pending(), ...edits.map((e) => (e.region === 'caps' ? 'phu-de' : e.region === 'topics' ? 'nen' : e.owner))])];
fs.writeFileSync(F.cho, JSON.stringify(ids));
console.log(`Đã ghi ${edits.length} chỗ. Bản trước khi sửa: ${bak}`);
edits.forEach((e) => console.log(`- ${e.owner}: "${e.value}" → "${e.next}"`));
console.log(`Cần render lại: ${ids.join(' ')}`);

spawnSync(process.execPath, [path.join(HERE, 'soat-canh.mjs'), P], {stdio: 'inherit'});

if (WANT_RENDER) renderNow(ids);
else console.log(`Khi sẵn sàng xuất lại: node chu-tren-man.mjs ap "${P}" --render (hoặc nhờ Claude). Nên chụp thử nếu chữ dài hơn trước.`);
