#!/usr/bin/env node
// SOÁT CẢNH TRƯỚC KHI RENDER (khối 17, 2026-11-06): đọc kịch bản, báo lỗi đo được — không sửa gì, không render.
//   node soat_canh.mjs <dự án>     → in ra + ghi check/soat.md · mã thoát 1 nếu có P0
// Mỗi lỗi một dòng: t=… · cảnh · vấn đề → cách sửa.
//   P0 hỏng hình / sai nội dung — phải sửa · P1 làm yếu video — nên sửa · P2 tinh chỉnh, giữ có chủ đích được
// Không thay việc xem bằng mắt (check/stills.jpg, check/sheet.jpg): chỉ bắt trước những lỗi đo được.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';

const P = path.resolve((process.argv[2] || '').replace(/^~/, process.env.HOME));
const SRC = path.join(P, 'motion/src');
if (!process.argv[2] || !fs.existsSync(SRC)) { console.error('cách dùng: soat_canh.mjs <dự án>'); process.exit(2); }
const imp = (f) => import(pathToFileURL(path.join(SRC, f)).href);
const read = (f) => { try { return fs.readFileSync(path.join(SRC, f), 'utf8'); } catch { return ''; } };

let list = [], duration = 0, NGANG = false;
if (fs.existsSync(path.join(SRC, 'scenes.js'))) {
  list = (await imp('scenes.js')).SCENES || [];
  const pj = (await imp('project.js')).default; duration = pj.duration || 0; NGANG = pj.width > pj.height && !pj.podcast;
} else if (fs.existsSync(path.join(SRC, 'edl.js'))) {   // ghép vlog, highlight người nói: lớp phủ phẳng, không có props
  const e = await imp('edl.js');
  list = (e.OVERLAYS || []).map((o, i) => ({id: o.id || `${o.type}-${i + 1}`, ...o}));
  duration = e.TOTAL ? e.TOTAL / (e.FPS || 30) : 0;
}
let HS = {};
try { HS = JSON.parse(read('hoso.json')); } catch {}
const {holdEnds} = await imp('lib/giu.js');
const K = HS.canh_minh_hoa || {}, MO_RA = K.mo_ra_s ?? 0.3, NHAN = K.nhan_max_chu ?? Infinity;   // không trần cứng (2026-11-07)

const icons = new Set([...read('lib/Icons.jsx').matchAll(/^\s*'?([a-zA-Z-]+)'?:\s*[\[(<'`]/gm)].map((m) => m[1]));
const modes = (f) => new Set([...read(f).matchAll(/mode === '([a-z-]+)'/g)].map((m) => m[1]));
const MODES = {illus: new Set(['single', 'flow', 'vs', 'count', 'list']), diagram: modes('lib/Diagram.jsx')};
const FULL = new Set(['illus', 'diagram', 'action', 'cta', 'card', 'montage', 'recap', 'converge', 'master', 'gens', 'build']);

const words = (t) => String(t ?? '').replace(/\*/g, '').trim().split(/\s+/).filter(Boolean).length;
const need = (t) => 0.5 + 0.3 * words(t);          // đủ đọc: 0,5 s + 0,3 s mỗi từ
const fmt = (t) => (Math.round(t * 10) / 10).toFixed(1).replace('.', ',');
const lines = {P0: [], P1: [], P2: []};
const bao = (m, t, id, msg, fix) => lines[m].push(`t=${fmt(t)} · ${id} · ${msg} → ${fix}`);

const flat = (o) => ({...o, ...(o.props || {})});
const held = Object.fromEntries(holdEnds(list, duration || Infinity, HS).map((s) => [s.id, s]));

for (const raw of list) {
  const s = flat(raw), end = held[s.id]?.end ?? s.end, last = end - MO_RA;
  if (!(s.end > s.start)) { bao('P0', s.start, s.id, `hết (${s.end}) không sau đầu (${s.start})`, 'sửa mốc cảnh'); continue; }
  if (s.type in MODES && MODES[s.type].size && !MODES[s.type].has(s.mode || (s.type === 'illus' ? 'single' : 'tang')))
    bao('P0', s.start, s.id, `không có kiểu "${s.mode}"`, 'dùng kiểu trong khối 07');
  const items = Array.isArray(s.items) ? s.items.filter((x) => x && typeof x === 'object' && !Array.isArray(x)) : [];
  for (const it of items) {
    if (it.icon && icons.size && !icons.has(it.icon)) bao('P0', it.at ?? s.start, s.id, `không có biểu tượng "${it.icon}"`, 'đổi tên hoặc vẽ thêm ở Icons.jsx');
    if (it.at != null && (it.at < s.start - 0.01 || it.at >= last)) bao('P0', it.at, s.id, `"${it.label || it.icon || 'phần tử'}" hiện ngoài cảnh (${fmt(s.start)}–${fmt(last)})`, 'dời mốc at hoặc kéo dài cảnh');
  }
  // màn trống đầu cảnh (11/11/2026: illus flow 63,4 s mà phần tử đầu 67,6 s → 4 s nền tối che người, không chữ)
  const dau = Math.min(...items.map((x) => x.at ?? s.start), s.num ? s.num.at ?? s.start : Infinity);
  if ((s.type === 'illus' || s.type === 'diagram') && items.length && dau - s.start > 1.2)
    bao('P0', s.start, s.id, `màn trống ${fmt(dau - s.start)} s đầu cảnh (phần tử đầu hiện lúc ${fmt(dau)})`, `dời start về ~${fmt(dau - 0.5)}`);
  // kiểu chưa chạy đúng ở khung ngang (11/11/2026, video cuộc gọi): kinetic không hiện, action đẩy câu trích xuống đáy
  if (NGANG && (s.type === 'kinetic' || s.type === 'action'))
    bao('P0', s.start, s.id, `kiểu "${s.type}" lỗi ở khung ngang`, 'dùng bocuc the-canh / o-nguoi hoặc illus');
  if (NGANG && s.type === 'card' && (s.steps || s.items || []).length > 4)
    bao('P1', s.start, s.id, `thẻ ${(s.steps || s.items).length} dòng tràn ở khung ngang`, 'dùng bocuc the-canh / muc-luc');
  if (s.num && typeof s.num.to !== 'number') bao('P0', s.start, s.id, 'con số không phải dạng số', 'ghi num.to là số');

  // đủ thời gian đọc: mỗi chữ tính từ lúc hiện tới lúc bị thay / cảnh mờ
  const mid = s.mode === 'chuyen-giao' ? items.slice(1, -1) : s.mode === 'doi-trang-thai' ? items : [];
  const doc = (txt, a, z) => { if (words(txt) && a < z && z - a + 0.01 < need(txt)) bao('P1', a, s.id, `"${txt}" chỉ hiện ${fmt(z - a)} s, cần ${fmt(need(txt))} s`, 'dời lúc hiện sớm hơn, kéo dài cảnh hoặc rút chữ'); };
  if (mid.length) {
    const sorted = [...mid].sort((a, b) => (a.at ?? s.start) - (b.at ?? s.start));
    sorted.forEach((it, i) => doc(it.label, it.at ?? s.start, i < sorted.length - 1 ? sorted[i + 1].at : last));
  } else for (const it of items) doc(it.label, it.at ?? s.start, last);
  // nhãn tóm tắt: phải kịp đọc (P1). Câu trích chạy theo lời (quote) không tính: người xem đang nghe đúng câu đó.
  // Thẻ tít / màn chốt có độ dài theo hồ sơ riêng (khối 06, 08) → chỉ nhắc P2 khi thiếu hẳn hơn 1 s.
  if (s.label) doc(s.label, s.start, last);
  const big = s.text || (Array.isArray(s.lines) ? s.lines.join(' ') : '');
  if (big && last - s.start + 1 < need(big)) bao('P2', s.start, s.id, `"${big}" chỉ hiện ${fmt(last - s.start)} s, cần ${fmt(need(big))} s`, 'cân nhắc rút chữ');

  if (s.type === 've' && !s.ve) bao('P0', s.start, s.id, 'cảnh tự vẽ thiếu props.ve (tên component trong rieng/index.js)', 'đặt ve: \'TenComponent\'');
  if (s.type === 'nhan' && !(s.text || s.icon || s.zoom > 1 || s.toi)) bao('P0', s.start, s.id, 'điểm nhấn trống (không chữ, biểu tượng, zoom hay làm tối)', 'thêm ít nhất một kiểu');
  // bố cục (BoCuc.jsx): chữ trong thẻ phải hiện trong cảnh; không giới hạn số dòng — tự cân theo khung (dọc: ít thứ cùng lúc)
  if (s.type === 'bocuc') for (const d of [...(s.dong || []), ...((s.noi_dung && s.noi_dung.props && s.noi_dung.props.dong) || [])])
    if (d.at != null && (d.at < s.start - 0.01 || d.at >= s.end)) bao('P0', d.at, s.id, `dòng "${d.text}" hiện ngoài cảnh`, 'dời mốc at hoặc kéo dài cảnh');
  if (s.type === 'illus' && s.label && words(s.label) > NHAN) bao('P1', s.start, s.id, `nhãn "${s.label}" ${words(s.label)} chữ (tối đa ${NHAN})`, 'rút còn cụm đắt nhất');

  // đứng yên quá lâu: phần tử cuối đã hiện + đã đủ đọc mà cảnh còn hơn 3 s
  if ((s.type === 'illus' || s.type === 'diagram') && !s.compact) {   // compact: khuôn dọc có chữ chính chạy theo lời, không đứng yên
    const lastAt = Math.max(s.start, ...items.map((x) => x.at ?? s.start), s.num ? s.num.at + (s.num.dur || 1.2) : 0);
    const texts = [s.label, ...items.map((x) => x.label)].filter(Boolean);
    const rest = last - lastAt - Math.max(0, ...texts.map(need));
    if (rest > 3) bao('P2', lastAt, s.id, `hình đứng yên ${fmt(rest)} s sau khi đọc xong`, 'rút cảnh hoặc thêm phần tử theo lời');
  }
}

// chồng cảnh toàn màn hình
const fulls = list.map(flat).filter((s) => FULL.has(s.type)).sort((a, b) => a.start - b.start);
for (let i = 1; i < fulls.length; i++) if (fulls[i].start < fulls[i - 1].end - 0.01)
  bao('P1', fulls[i].start, fulls[i].id, `chồng lên "${fulls[i - 1].id}" (hết ${fmt(fulls[i - 1].end)})`, 'dời mốc, mỗi lúc một điểm nhìn');
// không hai cảnh cùng kiểu liền nhau (khối 07, 2026-11-10); cảnh vẽ tiếp cùng mạch (tu_buoc) được nối
const kieu = (s) => s.type === 'nhan' ? `nhan:${s.icon ? 'icon' : s.text ? 'text' : s.zoom > 1 ? 'zoom' : 'toi'}`
  : [s.type, s.mode || s.kieu].filter(Boolean).join(':');
const BO_QUA = new Set(['hook', 'cta', 'action']);   // mở đầu, màn hành động, màn chốt có chỗ cố định
const chuoi = list.map(flat).filter((s) => !BO_QUA.has(s.type)).sort((a, b) => a.start - b.start);
for (let i = 1; i < chuoi.length; i++) {
  const a = chuoi[i - 1], b = chuoi[i];
  if (kieu(a) === kieu(b) && b.tu_buoc == null)
    bao('P2', b.start, b.id, `cùng kiểu "${kieu(b)}" với cảnh liền trước "${a.id}"`, 'đổi kiểu một cảnh, hoặc vẽ tiếp mạch (tu_buoc)');
}
// mở đầu 3 giây
if (false && list.length && !list.map(flat).some((s) => s.start <= 0.5 && ['hook', 'chips', 'pow', 'kinetic'].includes(s.type)))
  bao('P2', 0, 'mở đầu', 'không có thẻ tít trong 0,5 s đầu', 'kiểm tra khối 06 (đoạn ghép mở vlog / teaser podcast thì bỏ qua)');

const tong = lines.P0.length + lines.P1.length + lines.P2.length;
const out = [`# Soát cảnh — ${list.length} cảnh · P0 ${lines.P0.length} · P1 ${lines.P1.length} · P2 ${lines.P2.length}`];
for (const m of ['P0', 'P1', 'P2']) if (lines[m].length) out.push(`\n## ${m}`, ...lines[m].map((x) => `- ${x}`));
if (!tong) out.push('Không thấy lỗi đo được. Vẫn cần xem check/stills.jpg bằng mắt.');
fs.mkdirSync(path.join(P, 'check'), {recursive: true});
fs.writeFileSync(path.join(P, 'check/soat.md'), out.join('\n') + '\n');
console.log(out.join('\n'));
process.exitCode = lines.P0.length ? 1 : 0;
