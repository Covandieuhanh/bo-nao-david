// Chụp khung kiểm tra: node stills.mjs <giây> ... → ../check/stills/<giây>.jpg + sheet
import fs from 'node:fs';
import path from 'node:path';
import {bundle} from '@remotion/bundler';
import {renderStill, selectComposition} from '@remotion/renderer';
const out = path.resolve('../check/stills'); fs.mkdirSync(out, {recursive: true});
const serveUrl = await bundle({entryPoint: path.resolve('src/index.jsx')});
const composition = await selectComposition({serveUrl, id: 'show'});
for (const t of process.argv.slice(2)) {
  await renderStill({serveUrl, composition, frame: Math.round(Number(t) * 30), output: path.join(out, `${t}.jpg`), imageFormat: 'jpeg', jpegQuality: 80});
}
console.log('frames', composition.durationInFrames);
// Bản bundle chép CẢ thư mục clip vào thư mục tạm (vlog 48 clip ≈ 4,4 GB/lần) — không dọn thì đầy ổ sau vài chục lần chạy (2026-11-04)
fs.rmSync(serveUrl, {recursive: true, force: true});
