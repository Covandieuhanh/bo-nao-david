#!/usr/bin/env node
// SOÁT CẢNH TRƯỚC KHI RENDER (khối 17, 2026-11-06): đọc kịch bản, báo lỗi đo được — không sửa gì, không render.
//   node soat-canh.mjs <dự án>     → in ra + ghi kiem-tra/soat.md · mã thoát 1 nếu có P0
// Mỗi lỗi một dòng: t=… · cảnh · vấn đề → cách sửa.
//   P0 hỏng hình / sai nội dung — phải sửa · P1 làm yếu video — nên sửa · P2 tinh chỉnh, giữ có chủ đích được
// Không thay việc xem bằng mắt (kiem-tra/anh-tinh.jpg, kiem-tra/bang-anh.jpg): chỉ bắt trước những lỗi đo được.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';

const P = path.resolve((process.argv[2] || '').replace(/^~/, process.env.HOME));
const SRC = path.join(P, 'chuyen-dong/src');
if (!process.argv[2] || !fs.existsSync(SRC)) { console.error('cách dùng: soat-canh.mjs <dự án>'); process.exit(2); }
const imp = (f) => import(pathToFileURL(path.join(SRC, f)).href);
const read = (f) => { try { return fs.readFileSync(path.join(SRC, f), 'utf8'); } catch { return ''; } };

let list = [], duration = 0, NGANG = false, CO_NGUOI = false, MAT = {};
if (fs.existsSync(path.join(SRC, 'canh.js'))) {
  list = (await imp('canh.js')).SCENES || [];
  const pj = (await imp('du-an.js')).default; duration = pj.duration || 0; NGANG = pj.width > pj.height && !pj.podcast;
  CO_NGUOI = !pj.podcast;   // khuôn 1 video: người nói trên hình (podcast chỉ tiếng thì không)
  try { MAT = (await imp('mat.js')).default || {}; } catch {}
} else if (fs.existsSync(path.join(SRC, 'danh-sach-cat.js'))) {   // ghép vlog, highlight người nói: lớp phủ phẳng, không có props
  const e = await imp('danh-sach-cat.js');
  list = (e.OVERLAYS || []).map((o, i) => ({id: o.id || `${o.type}-${i + 1}`, ...o}));
  duration = e.TOTAL || 0;   // TOTAL của khuôn ghép đã là giây (19/11/2026: chia FPS lần nữa → độ dài sai, giữ cảnh tính sai)
}
let HS = {};
try { HS = JSON.parse(read('ho-so.json')); } catch {}
const {holdEnds} = await imp('thu-vien/giu.js');
const K = HS.canh_minh_hoa || {}, MO_RA = K.mo_ra_s ?? 0.3, NHAN = K.nhan_max_chu ?? Infinity;   // không trần cứng (2026-11-07)

const icons = new Set([...read('thu-vien/bieu-tuong.jsx').matchAll(/^\s*'?([a-zA-Z-]+)'?:\s*[\[(<'`]/gm)].map((m) => m[1]));
const modes = (f) => new Set([...read(f).matchAll(/mode === '([a-z-]+)'/g)].map((m) => m[1]));
const MODES = {illus: new Set(['single', 'flow', 'vs', 'count', 'list']), diagram: modes('thu-vien/so-do.jsx')};
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
    if (it.icon && icons.size && !icons.has(it.icon)) bao('P0', it.at ?? s.start, s.id, `không có biểu tượng "${it.icon}"`, 'đổi tên hoặc vẽ thêm ở bieu-tuong.jsx');
    if (it.at != null && (it.at < s.start - 0.01 || it.at >= last)) bao('P0', it.at, s.id, `"${it.label || it.icon || 'phần tử'}" hiện ngoài cảnh (${fmt(s.start)}–${fmt(last)})`, 'dời mốc at hoặc kéo dài cảnh');
  }
  // màn trống đầu cảnh (11/11/2026: illus flow 63,4 s mà phần tử đầu 67,6 s → 4 s nền tối che người, không chữ)
  const dau = Math.min(...items.map((x) => x.at ?? s.start), s.num ? s.num.at ?? s.start : Infinity);
  if ((s.type === 'illus' || s.type === 'diagram') && items.length && dau - s.start > 1.2)
    bao('P0', s.start, s.id, `màn trống ${fmt(dau - s.start)} s đầu cảnh (phần tử đầu hiện lúc ${fmt(dau)})`, `dời start về ~${fmt(dau - 0.5)}`);
  // kiểu chưa chạy đúng ở khung ngang (11/11/2026, video cuộc gọi): kinetic không hiện, action đẩy câu trích xuống đáy
  // lower (22/11/2026, tap-dji0022-2111): ở khung ngang không hiện gì mà phụ đề vẫn nhường → trống chữ
  if (NGANG && (s.type === 'kinetic' || s.type === 'action' || s.type === 'lower'))
    bao('P0', s.start, s.id, `kiểu "${s.type}" lỗi ở khung ngang`, 'dùng cảnh tự vẽ ở chỗ trống (ve) hoặc bocuc the-canh');
  // KHÔNG CHE / LÀM MỜ NGƯỜI ĐANG NÓI (David 21/11 + 22/11/2026: "màn hình mờ lại còn che nhân vật là hoàn toàn không đúng"):
  // mẫu 1 video có người trên hình → cảnh toàn khung, nền người mờ, màn chương toàn khung đều chặn. Chỉ được khi đoạn đó
  // không có người nói trên hình (cắt sang màn hình máy, cảnh trống): ghi props.khong_nguoi = true.
  if (CO_NGUOI && !s.khong_nguoi && (FULL.has(s.type) && s.type !== 'cta' || s.phong === 'nguoi-mo' || (s.type === 'bocuc' && ['chuong', 'muc-luc', 'tren-duoi', 'o-tron'].includes(s.kieu))))
    bao('P0', s.start, s.id, `"${[s.type, s.kieu || s.mode].filter(Boolean).join(':')}" phủ / làm mờ người đang nói trên hình`, 'đặt hình vào chỗ trống thật của khung (cảnh tự vẽ ve có vị trí o), hoặc ghi khong_nguoi: true nếu đoạn đó không có người trên hình');
  // KHUNG NHIỀU NGƯỜI (David 22/11/2026: "tôi đang nói với các đối tác thì có nên chỉ hiện một mình tôi không?"):
  // không thu riêng người đang nói vào ô — người xem cần thấy đang nói với ai
  if (s.type === 'bocuc' && ['o-nguoi', 'o-tron'].includes(s.kieu) && s.khung !== 'ca-hai' && ((MAT[s.id] || {}).nguoi || []).length >= 2)
    bao('P0', s.start, s.id, `khung có ${MAT[s.id].nguoi.length} người mà "${s.kieu}" chỉ giữ người đang nói`, 'dùng nhãn ở chỗ trống (ve) để mọi người vẫn hiện, hoặc khung: \'ca-hai\'');
  if (s.type === 'bocuc' && s.kieu === 'the-canh' && ((MAT[s.id] || {}).nguoi || []).length >= 2)
    bao('P1', s.start, s.id, 'thẻ cạnh người trong khung nhiều người: hết chỗ trống sẽ tự thu người đang nói vào ô', 'chụp thử; tự thu vào ô thì đổi sang nhãn ở chỗ trống (ve)');
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

  if (s.type === 've' && !s.ve) bao('P0', s.start, s.id, 'cảnh tự vẽ thiếu props.ve (tên component trong rieng/diem-vao.js)', 'đặt ve: \'TenComponent\'');
  if (s.type === 'nhan' && !(s.text || s.icon || s.zoom > 1 || s.toi)) bao('P0', s.start, s.id, 'điểm nhấn trống (không chữ, biểu tượng, zoom hay làm tối)', 'thêm ít nhất một kiểu');
  // bố cục (bo-cuc.jsx): chữ trong thẻ phải hiện trong cảnh; không giới hạn số dòng — tự cân theo khung (dọc: ít thứ cùng lúc)
  if (s.type === 'bocuc') for (const d of [...(s.dong || []), ...((s.noi_dung && s.noi_dung.props && s.noi_dung.props.dong) || [])])
    if (d.at != null && (d.at < s.start - 0.01 || d.at >= s.end)) bao('P0', d.at, s.id, `dòng "${d.text}" hiện ngoài cảnh`, 'dời mốc at hoặc kéo dài cảnh');
  // ít chữ (huong-dan-lua-chon.md bước 4a, 20/11/2026): nhãn mỗi nút sơ đồ / minh hoạ 1–3 chữ nguyên văn
  if (s.type === 'illus' || s.type === 'diagram') for (const it of items)
    if (it.label && words(it.label) > 4) bao('P1', it.at ?? s.start, s.id, `nhãn "${it.label}" ${words(it.label)} chữ — hình nói thay lời thì ít chữ`, 'rút còn 1–3 chữ đắt nhất (nguyên văn)');
  // một chỗ sáng: tầng / cột ≥ 3 mục mà không bật mot_diem → mục sáng cố định, không theo lời
  if (s.type === 'diagram' && (s.mode === 'tang' || s.mode === 'cot') && items.length >= 3 && !s.mot_diem)
    bao('P2', s.start, s.id, `"${s.mode}" ${items.length} mục, chỗ sáng không theo lời`, 'thêm mot_diem: true nếu các mục được nói lần lượt');
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
  : [s.type, s.type === 've' ? s.ve : null, s.mode || s.kieu].filter(Boolean).join(':');   // cảnh tự vẽ: tên component + props.kieu (dạng hình)
// Nhóm theo hình người xem thấy. Đổi nội dung trong cùng ô nhãn không tạo ra cách kể khác.
const nhomThiGiac = (s) => {
  if (s.type === 'nhan' || s.type === 'pow' || (s.type === 've' && s.ve === 'NhanTram')) return 'nhan-canh-nguoi';
  if (s.type === 'bocuc' && s.kieu === 'the-canh' && (s.dong || []).length <= 1) return 'nhan-canh-nguoi';
  if (s.type === 've' && s.ve === 'DuongMay') {
    const dang = ['the', 'thay', 'buoc', 'ghep', 'khuon', 'nhac', 'cau', 'ten_the'].find((key) => s[key]);
    return `DuongMay:${dang || (s.nut?.length ? 'nut' : 'chuong')}`;
  }
  return kieu(s);
};
const cachDung = (s) => s.type === 've' && s.ve === 'DuongMay' ? nhomThiGiac(s) : kieu(s);
const CO_DINH = new Set(['hud', 'title', 'pinTitle', 'teaserTag', 'cta', 'hook', 'round', 'outro', 'location', 'action']);
const noiDungThiGiac = list.map(flat).filter((s) => !CO_DINH.has(s.type));
const BO_QUA = new Set(['hook', 'cta', 'action']);   // mở đầu, màn hành động, màn chốt có chỗ cố định
const chuoi = list.map(flat).filter((s) => !BO_QUA.has(s.type)).sort((a, b) => a.start - b.start);
for (let i = 1; i < chuoi.length; i++) {
  const a = chuoi[i - 1], b = chuoi[i];
  if (kieu(a) === kieu(b) && b.tu_buoc == null)
    bao('P2', b.start, b.id, `cùng kiểu "${kieu(b)}" với cảnh liền trước "${a.id}"`, 'đổi kiểu một cảnh, hoặc vẽ tiếp mạch (tu_buoc)');
}
// CỔNG TỰ CHỌN (huong-dan-lua-chon.md, 19/11/2026 — 6 tập dựng bằng mẫu ghép không có chẩn đoán, cả video chỉ chữ nhấn + tít):
// (1) phải có ke-hoach-canh.md mục "## Chẩn đoán" ở thư mục dự án; (2) cả video một kiểu lớp phủ nội dung → P0, trừ khi
// ke-hoach-canh.md ghi "Một kiểu có chủ đích: <lý do>". Lớp cố định (dấu kênh, tít, màn chốt…) không tính là kiểu.
{
  let kh = ''; try { kh = fs.readFileSync(path.join(P, 'ke-hoach-canh.md'), 'utf8'); } catch {}
  const cd = (kh.split(/^##[ \t]+Chẩn đoán[^\n]*\n/m)[1] || '').split(/^##[ \t]+/m)[0];
  const duAnMoi = fs.existsSync(path.join(P, 'yeu-cau.md'));
  if (!/^##\s*Chẩn đoán/m.test(kh))
    bao('P0', 0, 'ke-hoach-canh.md', 'chưa chẩn đoán, chưa tự chọn theo nội dung', 'chạy chan-doan.py rồi ghi mục "## Chẩn đoán" theo thiet-ke-bo-cuc/huong-dan-lua-chon.md');
  else if (!/Thẩm mỹ:/.test(kh))
    bao('P1', 0, 'ke-hoach-canh.md', 'chẩn đoán chưa có dòng "Thẩm mỹ:" (nền, kiểu hình, chuyển cảnh, nhạc)', 'huong-dan-lua-chon.md bước 2b');
  // tiết chế (huong-dan-lua-chon.md bước 4a, 20/11/2026): chỉ dựng hình cho ý khó hiểu nếu chỉ nghe
  if (/^##\s*Chẩn đoán/m.test(kh) && !/Tiết chế:/.test(kh))
    bao('P1', 0, 'ke-hoach-canh.md', 'chẩn đoán chưa có dòng "Tiết chế:" (ý nào cần hình, ý nào để người nói)', 'huong-dan-lua-chon.md bước 4a');
  // Mục nguồn phải chỉ đúng cảnh, kể cả cảnh chỉ dùng chữ hoặc biểu tượng.
  if (/^##\s*Chẩn đoán/m.test(kh)) {
    const dong = (kh.match(/^\s*Nguồn kho:[ \t]*([^\n]*)/m) || [])[1] || '';
    const nguon = new Map(dong.split(';').flatMap((muc) => {
      const [id, mau] = muc.split('←').map((text) => text.trim());
      return id && mau ? [[id, mau]] : [];
    }));
    for (const s of noiDungThiGiac)
      if (!nguon.has(s.id))
        bao('P1', s.start, s.id, 'chưa chỉ rõ mẫu áp dụng cho cảnh', 'ghi <id> ← <nguồn, mã ca hoặc tên cách đã học> trong dòng Nguồn kho');
  }
  {
    const PHU = list.map(flat).filter((x) => FULL.has(x.type) || x.type === 'bocuc' || x.type === 've').map((x) => [x.start, held[x.id]?.end ?? x.end]).sort((a, b) => a[0] - b[0]);
    let phu = 0, den = -Infinity;
    for (const [a, b] of PHU) { const a2 = Math.max(a, den); if (b > a2) { phu += b - a2; den = b; } }
    if (duration >= 45 && phu / duration > 0.45)
      bao('P1', 0, 'cả video', `hình phủ ${Math.round(100 * phu / duration)} % thời lượng — dễ rối, phân tán`, 'bỏ hình ở ý dễ hiểu khi nghe (kể chuyện, cảm xúc, câu ngắn tự rõ), giữ người nói + phụ đề');
  }
  // KHO DÙNG TỰ DO (David 22/11/2026: "không nhất thiết là phải có một cái luật gì đấy gọi là cố định … tận dụng tối đa các cái bộ tài
  // nguyên đã học"): không còn cổng "chỉ dùng khi có dấu hiệu". Chỉ giữ lỗi kỹ thuật của mẫu.
  {
    for (const x of list.map(flat).filter((x) => x.type === 'bocuc' && x.kieu === 'dung-hay'))
      if ((x.cap || []).length < 2) bao('P2', x.start, x.id, `"dung-hay" chỉ ${(x.cap || []).length} cặp — khuôn lặp đẹp nhất từ 2 cặp`, 'một cặp thì illus vs cũng được');
    let caps = []; try { caps = (await imp('phu-de.js')).default || []; } catch {}
    for (const c of caps) if ((c.hl || []).filter((h) => h.startsWith('^')).length > 1)
      bao('P1', c.start, 'phu-de', `dòng "${c.text.slice(0, 40)}…" có ${(c.hl || []).filter((h) => h.startsWith('^')).length} từ khoá to`, 'mỗi dòng tối đa một mục "^"');
  }
  // LẬP LUẬN THEO NGƯỜI XEM (thiet-ke-bo-cuc/nhu-cau-nguoi-xem.md): "Loại:" cho cả video + mỗi cảnh nội dung một dòng
  // "- <id> · Cần: <nguyên lý> · Vì: … · Làm: …". Tên hợp lệ đọc từ thiet-ke-bo-cuc/nguyen-ly.json (một nguồn cho người và máy).
  // Dự án cũ (không có yeu-cau.md — tạo trước khi có bước này) thì hai lỗi chặn hạ thành P1 để dựng lại bản cũ không bị chặn.
  {
    let NL = {loai: {}, nguyen_ly: {}};
    try { NL = JSON.parse(fs.readFileSync(new URL('../../thiet-ke-bo-cuc/nguyen-ly.json', import.meta.url), 'utf8')); } catch {}
    const cu = !fs.existsSync(path.join(P, 'yeu-cau.md'));
    const chan = cu ? 'P1' : 'P0', ghiCu = cu ? ' (dự án cũ: chỉ nhắc)' : '';
    // Kiểm chứng lựa chọn trước khi chạy bản đầy đủ. Hình xem thử vẫn cần người dựng đánh giá.
    const coNoiDung = (value) => value && /[\p{L}\p{N}]/u.test(value) && !/^<.*>$/.test(value);
    const thamMy = cd.match(/^\s*Đối chiếu thẩm mỹ:[ \t]*(.+?)[ \t]*·[ \t]*Chọn:[ \t]*(.+?)[ \t]*·[ \t]*Vì:[ \t]*(.+)$/m);
    const khac = (a, b) => a.normalize('NFC').trim().toLowerCase() !== b.normalize('NFC').trim().toLowerCase();
    if (duAnMoi && (!thamMy || !thamMy.slice(1).every(coNoiDung) || !khac(thamMy[1], thamMy[2])))
      bao('P0', 0, 'ke-hoach-canh.md', 'thiếu đối chiếu hai hướng thẩm mỹ', 'ghi hướng khác, hướng chọn và lý do theo bước 2b');
    const quyetDinh = new Map([...cd.matchAll(/^[-*]?[ \t]*([^\s·]+)[ \t]*·[ \t]*Lựa chọn:[ \t]*(.+?)[ \t]*·[ \t]*Ứng viên khác:[ \t]*(.+?)[ \t]*·[ \t]*Vì sao chọn:[ \t]*(.+)$/gm)]
      .map((m) => [m[1], m.slice(2)]));
    for (const s of noiDungThiGiac) {
      const thucTe = cachDung(s);
      const d = quyetDinh.get(s.id);
      if (duAnMoi && (!d || !d.every(coNoiDung) || !khac(d[0], d[1])))
        bao('P0', s.start, s.id, 'thiếu so sánh cách thể hiện cho ý này', `ghi Lựa chọn: ${thucTe} · Ứng viên khác: … · Vì sao chọn: …`);
      else if (d && d[0].trim() !== thucTe)
        bao('P0', s.start, s.id, `kế hoạch chọn "${d[0]}" nhưng mã cảnh đang dùng "${thucTe}"`, 'đồng bộ kế hoạch và mã cảnh');
    }
    const norm = (t) => t.normalize('NFC').toLowerCase().trim();
    const loaiDong = cd.match(/^\s*Loại:\s*(.+)$/m);
    if (/^##\s*Chẩn đoán/m.test(kh)) {
      if (!loaiDong) bao(chan, 0, 'ke-hoach-canh.md', `chẩn đoán chưa có dòng "Loại:" (loại nội dung cả video)${ghiCu}`, 'thiet-ke-bo-cuc/nhu-cau-nguoi-xem.md mục 1');
      else if (!Object.keys(NL.loai).some((k) => loaiDong[1].includes(k))) bao('P1', 0, 'ke-hoach-canh.md', `"Loại: ${loaiDong[1].slice(0, 40)}" không có trong nguyen-ly.json`, `dùng một trong: ${Object.keys(NL.loai).join(', ')}`);
    }
    const BO = new Set(['hud', 'title', 'pinTitle', 'teaserTag', 'cta', 'hook', 'round', 'outro', 'location', 'lower', 'endcard', 'cover', 'captions', 'sides', 'stage']);
    const noiDung = list.map(flat).filter((x) => !BO.has(x.type));
    const dongCan = [...cd.matchAll(/^\s*[-*]?\s*([^\s·]+)\s*·\s*Cần:\s*([^·\n]+)/gm)].map((m) => ({id: m[1], can: m[2]}));
    const tenNL = Object.keys(NL.nguyen_ly).map(norm);
    if (noiDung.length && !dongCan.length) bao(chan, 0, 'ke-hoach-canh.md', `${noiDung.length} cảnh nội dung mà không dòng "Cần:" nào — chưa lập luận người xem cần gì${ghiCu}`, 'mỗi cảnh: "- <id> · Cần: <nguyên lý> · Vì: … · Làm: …" (nhu-cau-nguoi-xem.md mục 4)');
    else for (const x of noiDung) {
      const d = dongCan.find((c) => c.id === x.id);
      if (!d) { bao('P1', x.start, x.id, 'cảnh chưa có dòng "Cần: · Vì: · Làm:"', 'ghi cái khó của người xem và nguyên lý giải nó'); continue; }
      if (!d.can.split(/[+,/]/).map(norm).some((t) => tenNL.includes(t))) bao('P1', x.start, x.id, `"Cần: ${d.can.trim()}" không phải tên nguyên lý`, 'dùng đúng tên ở nhu-cau-nguoi-xem.md mục 2–3');
    }
    // yêu cầu người dùng (huong-dan-lua-chon.md bước 0b)
    let yc = ''; try { yc = fs.readFileSync(path.join(P, 'yeu-cau.md'), 'utf8'); } catch {}
    const ycThat = yc.replace(/<!--[\s\S]*?-->/g, '').split('\n').filter((l) => l.trim() && !/^\s*[#>]/.test(l)).length;
    if (ycThat && !/^\s*Yêu cầu:/m.test(cd)) bao('P1', 0, 'ke-hoach-canh.md', 'yeu-cau.md có yêu cầu mà Chẩn đoán chưa có dòng "Yêu cầu:"', 'huong-dan-lua-chon.md bước 0b');
    // ảnh được gọi phải có trong public/anh (thiếu là hỏng hình)
    const anh = new Set(); const tim = (o) => { if (o && typeof o === 'object') for (const [k, v] of Object.entries(o)) { if (k === 'photo' && typeof v === 'string') anh.add(v); else tim(v); } };
    tim(list);
    for (const a of anh) if (!fs.existsSync(path.join(P, 'chuyen-dong/public/anh', a))) bao('P0', 0, 'ảnh', `"${a}" không có trong chuyen-dong/public/anh`, 'chép ảnh (them-anh/) vào public/anh hoặc sửa tên');
  }
  const nhom = new Map();
  for (const s of noiDungThiGiac) {
    const k = nhomThiGiac(s);
    nhom.set(k, (nhom.get(k) || 0) + 1);
  }
  const loai = new Set(nhom.keys());
  const coY = /^\s*Một kiểu có chủ đích:[ \t]*\S.*$/m.test(kh);
  const [nhomChinh, soCanh = 0] = [...nhom.entries()].sort((a, b) => b[1] - a[1])[0] || [];
  if (!coY && loai.size > 1 && soCanh >= 3 && soCanh * 3 >= noiDungThiGiac.length * 2)
    bao('P1', 0, 'cả video', `${soCanh}/${noiDungThiGiac.length} cảnh cùng cách trình bày ${nhomChinh}`,
      'xem liền các cảnh nhấn, đổi cách kể ở ý phù hợp và ghi bằng chứng trong bản xem thử');
  if (duration >= 45 && loai.size <= 1 && !coY)
    bao('P0', 0, 'cả video', `chỉ ${loai.size ? `một kiểu lớp phủ (${[...loai][0]})` : 'không có lớp phủ nội dung'} suốt ${fmt(duration)} s`,
      'đi lại huong-dan-lua-chon.md bước 4 cho từng ý (liệt kê, so sánh, bước, con số, câu then chốt…), hoặc ghi "Một kiểu có chủ đích: …"');
  else if (duration >= 300 && loai.size <= 2 && !coY)
    bao('P1', 0, 'cả video', `video ${fmt(duration / 60)} phút chỉ ${loai.size} kiểu lớp phủ (${[...loai].join(', ')})`, 'xem lại huong-dan-lua-chon.md bước 4');
  // Đối chiếu lịch sử khi phiên dựng có yêu cầu. Không lấy độ mới làm tiêu chí chọn cảnh.
  // TẬN DỤNG KHO, ĐỔI HIỆU ỨNG (David 22/11/2026: "học nhiều mà không thấy ứng dụng được thì phí quá" — rồi: không cần luật cố định,
  // dùng tự do, đa dạng mà gọn): nhắc (P1, không chặn) khi video gần như lặp lại các kiểu của 3 tập gần nhất trong ~/Movies.
  if (process.env.THU_MUC_DOI_CHIEU_CANH) {
    const kieuVe = nhomThiGiac;
    const cur = new Set(list.map(flat).filter((x) => !CO_DINH.has(x.type)).map(kieuVe));
    const goc = process.env.THU_MUC_DOI_CHIEU_CANH, cu = [];
    const quet = (d, sau) => { try { for (const n of fs.readdirSync(d)) {
      const f = path.join(d, n, ...sau, 'chuyen-dong/src/canh.js');
      if (fs.existsSync(f) && path.resolve(path.join(d, n, ...sau)) !== P && !/^tap-thu-/.test(n)) cu.push([fs.statSync(f).mtimeMs, f]); } } catch {} };
    quet(goc, ['2-ban-day-du']); quet(path.join(goc, 'vlog'), []);
    const ba = cu.sort((a, b) => b[0] - a[0]).slice(0, 3), daDung = new Set();
    for (const [, f] of ba) try { for (const s of ((await import(pathToFileURL(f).href)).SCENES || []).map(flat)) if (!CO_DINH.has(s.type)) daDung.add(kieuVe(s)); } catch {}
    const moi = [...cur].filter((k) => !daDung.has(k));
    if (ba.length && cur.size && !moi.length)
      bao('P2', 0, 'cả video', `chỉ ${moi.length} kiểu khác ${ba.length} tập gần nhất (${moi.join(', ') || 'không có'}) — video sẽ trông giống các tập trước`,
        'đổi hiệu ứng / chuyển cảnh bằng kiểu khác trong kho (thiet-ke-bo-cuc/bo-cuc.md, rieng/ của khuôn) hoặc tự viết, giữ gọn');
  }
}
// mở đầu 3 giây
if (false && list.length && !list.map(flat).some((s) => s.start <= 0.5 && ['hook', 'chips', 'pow', 'kinetic'].includes(s.type)))
  bao('P2', 0, 'mở đầu', 'không có thẻ tít trong 0,5 s đầu', 'kiểm tra khối 06 (đoạn ghép mở vlog / teaser podcast thì bỏ qua)');

const tong = lines.P0.length + lines.P1.length + lines.P2.length;
const out = [`# Soát cảnh — ${list.length} cảnh · P0 ${lines.P0.length} · P1 ${lines.P1.length} · P2 ${lines.P2.length}`];
for (const m of ['P0', 'P1', 'P2']) if (lines[m].length) out.push(`\n## ${m}`, ...lines[m].map((x) => `- ${x}`));
if (noiDungThiGiac.length) out.push('\n## Cách thể hiện trong mã', ...noiDungThiGiac.map((s) =>
  `- ${s.id} · ${cachDung(s)} · nhóm hình: ${nhomThiGiac(s)}`));
if (!tong) out.push('Không thấy lỗi đo được. Vẫn cần xem kiem-tra/anh-tinh.jpg bằng mắt.');
fs.mkdirSync(path.join(P, 'kiem-tra'), {recursive: true});
fs.writeFileSync(path.join(P, 'kiem-tra/soat.md'), out.join('\n') + '\n');
console.log(out.join('\n'));
process.exitCode = lines.P0.length ? 1 : 0;
