// Chụp khung kiểm tra: node anh-tinh.mjs <giây> ... → ../kiem-tra/anh-tinh/<giây>.jpg + sheet
import fs from 'node:fs';
import path from 'node:path';
import {bundleNhe} from './bundle-nhe.mjs';
import {renderStill, selectComposition} from '@remotion/renderer';
const out = path.resolve('../kiem-tra/anh-tinh'); fs.mkdirSync(out, {recursive: true});
const serveUrl = await bundleNhe('src/diem-vao.jsx');   // không chép video vào thư mục tạm (bundle-nhe.mjs)
// Dọn bản bundle cả khi lỗi (19/11/2026: chụp mốc quá độ dài → ném lỗi, thư mục tạm ở lại). Mốc quá độ dài bị bỏ qua, có báo.
try {
  const composition = await selectComposition({serveUrl, id: 'show'});
  const maxT = (composition.durationInFrames - 1) / composition.fps;
  for (const t of process.argv.slice(2)) {
    if (Number(t) > maxT) { console.warn(`bỏ mốc ${t} s: video dài ${maxT.toFixed(2)} s`); continue; }
    await renderStill({serveUrl, composition, frame: Math.round(Number(t) * composition.fps), output: path.join(out, `${t}.jpg`), imageFormat: 'jpeg', jpegQuality: 80, timeoutInMilliseconds: 120000});
  }
  console.log('frames', composition.durationInFrames);
} finally {
  fs.rmSync(serveUrl, {recursive: true, force: true});
}
