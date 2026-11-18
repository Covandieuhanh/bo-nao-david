// Bundle KHÔNG chép video (18/11/2026 — bản dài 54 phút: bundle chép public 4,7 GB vào thư mục tạm, ổ đầy giữa chừng).
// public tạm chỉ chứa file nhỏ; file > 50 MB (video gốc) được nối cứng (hard link) thẳng vào bản bundle → không tốn thêm ổ.
// Xoá bản bundle sau render chỉ xoá liên kết, file gốc còn nguyên.
import {bundle} from '@remotion/bundler';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';

export async function bundleNhe(entry) {
  const pub = path.resolve('public');
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'public-nhe-'));
  const big = [];
  const walk = (rel = '') => {
    for (const e of fs.readdirSync(path.join(pub, rel), {withFileTypes: true})) {
      const r = path.join(rel, e.name);
      if (e.isDirectory()) { fs.mkdirSync(path.join(tmp, r), {recursive: true}); walk(r); }
      else if (fs.statSync(path.join(pub, r)).size > 50e6) big.push(r);
      else fs.copyFileSync(path.join(pub, r), path.join(tmp, r));
    }
  };
  walk();
  const serveUrl = await bundle({entryPoint: path.resolve(entry), publicDir: tmp});
  for (const r of big) {
    const dst = path.join(serveUrl, 'public', r);
    fs.mkdirSync(path.dirname(dst), {recursive: true});
    fs.rmSync(dst, {force: true});
    try { fs.linkSync(path.join(pub, r), dst); }
    catch { fs.copyFileSync(path.join(pub, r), dst, fs.constants.COPYFILE_FICLONE); }   // khác ổ: bản sao APFS (không tốn chỗ nếu cùng ổ APFS)
  }
  fs.rmSync(tmp, {recursive: true, force: true});
  return serveUrl;
}
