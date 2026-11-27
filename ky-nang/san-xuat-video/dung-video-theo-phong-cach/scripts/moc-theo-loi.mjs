// Mốc chuyển động trên lưới khung hình, lấy từ bản chép lời từng từ đã đối chiếu với tiếng.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';

const ms = (s) => {
  const [h, m, sec, mili] = s.split(/[:,.]/).map(Number);
  return ((h * 60 + m) * 60 + sec) * 1000 + mili;
};
const tokens = (s) => s.normalize('NFC').toLocaleLowerCase('vi')
  .match(/[\p{L}\p{N}]+/gu) || [];

export function docMocTu(srt) {
  return srt.trim().split(/\r?\n[ \t]*\r?\n/).flatMap((block) => {
    const m = block.match(/(\d\d:\d\d:\d\d[,.]\d{3})\s*-->\s*(\d\d:\d\d:\d\d[,.]\d{3})[^\r\n]*\r?\n([\s\S]*)/);
    if (!m) return [];
    const tu = tokens(m[3]);
    if (tu.length > 1) throw new Error('Cần SRT từng từ. Gặp một mục chứa nhiều từ: ' + m[3].trim());
    return tu.map((text) => ({text, dau: ms(m[1]), cuoi: ms(m[2])}));
  });
}

export function ganMoc(tu, {cum, tuGiay, denGiay, canh = 'dau', goc = 0}, fps) {
  if (!Number.isFinite(fps) || fps <= 0 || !Number.isFinite(goc) ||
    !Number.isFinite(tuGiay) || !Number.isFinite(denGiay) || denGiay <= tuGiay ||
    !['dau', 'cuoi'].includes(canh) || typeof cum !== 'string') {
    throw new Error('Sai khai báo cụm lời, khoảng tìm hoặc FPS');
  }
  const phrase = tokens(cum);
  if (!phrase.length) throw new Error('Cụm lời trống');
  const matches = tu.flatMap((w, i) => {
    const last = tu[i + phrase.length - 1];
    if (!last || w.dau < tuGiay * 1000 - 0.01 || last.cuoi > denGiay * 1000 + 0.01 ||
      !phrase.every((text, j) => tu[i + j]?.text === text)) return [];
    return [canh === 'cuoi' ? last.cuoi : w.dau];
  });
  if (matches.length !== 1) throw new Error(`“${cum}” có ${matches.length} kết quả, cần đúng một kết quả trong đoạn đã chọn`);
  const giayLoi = matches[0] / 1000 - goc;
  if (giayLoi < 0) throw new Error('Cụm lời nằm trước đầu đoạn dựng');
  const khung = Math.ceil(giayLoi * fps - 1e-8);
  return {giayLoi, khung, at: khung / fps};
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) {
  try {
    const [srt, json] = process.argv.slice(2);
    if (!srt || !json) throw new Error('Cách dùng: node moc-theo-loi.mjs moc-tung-tu.srt yeu-cau-moc.json');
    const config = JSON.parse(fs.readFileSync(json, 'utf8'));
    const tu = docMocTu(fs.readFileSync(srt, 'utf8'));
    const out = config.moc.map((m) => ({...m, ...ganMoc(tu, m, config.fps)}));
    console.log(JSON.stringify(out, null, 2));
  } catch (e) {
    console.error(e.message);
    process.exitCode = 1;
  }
}
