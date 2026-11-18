// Chụp khung kiểm tra: node anh-tinh.mjs <giây> ... → ../kiem-tra/anh-tinh/<giây>.jpg + sheet
import fs from 'node:fs';
import path from 'node:path';
import {bundleNhe} from './bundle-nhe.mjs';
import {renderStill, selectComposition} from '@remotion/renderer';
const out = path.resolve('../kiem-tra/anh-tinh'); fs.mkdirSync(out, {recursive: true});
const serveUrl = await bundleNhe('src/diem-vao.jsx');   // không chép video vào thư mục tạm (bundle-nhe.mjs)
const composition = await selectComposition({serveUrl, id: 'show'});
for (const t of process.argv.slice(2)) {
  await renderStill({serveUrl, composition, frame: Math.round(Number(t) * 30), output: path.join(out, `${t}.jpg`), imageFormat: 'jpeg', jpegQuality: 80, timeoutInMilliseconds: 120000});
}
console.log('frames', composition.durationInFrames);
// Bản bundle chép CẢ thư mục clip vào thư mục tạm (vlog 48 clip ≈ 4,4 GB/lần) — không dọn thì đầy ổ sau vài chục lần chạy (2026-11-04)
fs.rmSync(serveUrl, {recursive: true, force: true});
