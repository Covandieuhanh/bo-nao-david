// Chụp khung kiểm tra (PNG trong suốt): node preview.mjs <id>@<giây tuyệt đối trong video gốc> ...
import fs from 'node:fs';
import path from 'node:path';
import {bundle} from '@remotion/bundler';
import {renderStill, selectComposition} from '@remotion/renderer';
import project from './src/project.js';

const FPS = project.fpsNum / project.fpsDen;
const fr = (s) => Math.round(s * FPS);
const out = path.resolve('../check/motion');
fs.mkdirSync(out, {recursive: true});
// Video gốc cho cảnh cần chiếu lại hình (màn chốt `cta`): public/goc.mp4 → davinci/media/<source>
{ const lnk = path.resolve('public/goc.mp4'); fs.rmSync(lnk, {force: true});
  const src = path.resolve('../davinci/media', project.source || 'video_goc.mp4');   // liên kết cứng (bundler không chép symlink)
  if (!project.podcast && fs.existsSync(src)) { try { fs.linkSync(fs.realpathSync(src), lnk); } catch { fs.copyFileSync(src, lnk); } } }
const serveUrl = await bundle({entryPoint: path.resolve('src/index.jsx')});
for (const arg of process.argv.slice(2)) {
  const [id, t] = arg.split('@');
  const comp = await selectComposition({serveUrl, id});
  const frame = Math.min(comp.durationInFrames - 1, Math.max(0, fr(Number(t)) - fr(comp.defaultProps.start)));
  await renderStill({serveUrl, composition: comp, frame, output: path.join(out, `${id}@${t}.png`), imageFormat: 'png'});
  console.log('ok', id, t, frame);
}

// Dọn bản bundle tạm (chép cả public/ — không dọn thì đầy ổ, 2026-11-04)
fs.rmSync(serveUrl, {recursive: true, force: true});
