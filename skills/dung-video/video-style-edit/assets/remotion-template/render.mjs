// Render cảnh thành ProRes 4444 có kênh alpha (render_preview.py ghép lên video gốc): node render.mjs [id ...]  (id 'hai-ben' = hai bên khung ngang, 'phu-de' = phụ đề)
import fs from 'node:fs';
import path from 'node:path';
import {bundle} from '@remotion/bundler';
import {renderMedia, selectComposition} from '@remotion/renderer';
import {SCENES} from './src/scenes.js';
import output from './src/output.js';

const out = path.resolve('../davinci/media');
fs.mkdirSync(out, {recursive: true});
const only = new Set(process.argv.slice(2));
// KHOÁ RENDER (11/11/2026: ghép bản cuối lúc the_cuoi còn đang render → video mất màn kết 20 s): render_preview.py thấy khoá thì dừng
const KHOA = path.join(out, '.dang-render'); fs.writeFileSync(KHOA, String(process.pid));
process.on('exit', () => fs.rmSync(KHOA, {force: true}));
// Video gốc cho cảnh cần chiếu lại hình (màn chốt `cta`): public/goc.mp4 → davinci/media/<source>
import project from './src/project.js';
{ const lnk = path.resolve('public/goc.mp4'); fs.rmSync(lnk, {force: true});
  const src = path.resolve('../davinci/media', project.source || 'video_goc.mp4');   // liên kết cứng (bundler không chép symlink)
  if (!project.podcast && fs.existsSync(src)) { try { fs.linkSync(fs.realpathSync(src), lnk); } catch { fs.copyFileSync(src, lnk); } } }
const serveUrl = await bundle({entryPoint: path.resolve('src/index.jsx')});
for (const s of SCENES) {
  if (only.size && !only.has(s.id)) continue;
  // TIEP=1 node render.mjs: bỏ qua cảnh đã có .mov (chạy tiếp sau khi một cảnh lỗi) — 2026-11-08
  if (process.env.TIEP && fs.existsSync(path.join(out, `${s.id}.mov`))) continue;
  // cảnh chiếu lại video gốc (ô người, màn chốt): đọc khung từ file gốc lớn → ít luồng hơn để không quá hạn chờ
  const vid = s.type === 'cta' || (s.type === 'bocuc' && (s.props?.kieu ?? 'o-nguoi') === 'o-nguoi');
  const composition = await selectComposition({serveUrl, id: s.id});
  const t0 = Date.now();
  await renderMedia({serveUrl, composition, codec: 'prores', proResProfile: '4444', pixelFormat: 'yuva444p10le',
    imageFormat: 'png', concurrency: vid ? 2 : 4, timeoutInMilliseconds: 240000, muted: true, outputLocation: path.join(out, `${s.id}.mov`)});
  console.log(`${s.id} ${composition.durationInFrames} khung ${((Date.now() - t0) / 1000).toFixed(0)}s`);
}
// Phụ đề chạy suốt video, nền trong suốt → phu_de.mov (render_preview đè lên trên cùng)
const caps = (await import('./src/captions.js')).default;
if (caps.length && (!only.size || only.has('phu-de'))) {
  const composition = await selectComposition({serveUrl, id: 'phu-de'});
  const t0 = Date.now();
  await renderMedia({serveUrl, composition, codec: 'prores', proResProfile: '4444', pixelFormat: 'yuva444p10le',
    imageFormat: 'png', concurrency: 4, timeoutInMilliseconds: 240000, muted: true, outputLocation: path.join(out, 'phu_de.mov')});
  console.log(`phu-de ${composition.durationInFrames} khung ${((Date.now() - t0) / 1000).toFixed(0)}s`);
}
// Màn hình bìa (COVER) 1 s, nền đặc → bia.mp4; render_preview.py ghép trước video
const {COVER} = await import('./src/scenes.js');
if (COVER && (!only.size || only.has('bia'))) {
  const composition = await selectComposition({serveUrl, id: 'bia'});
  await renderMedia({serveUrl, composition, codec: 'h264', crf: 14, concurrency: 4, timeoutInMilliseconds: 240000, muted: true, outputLocation: path.join(out, 'bia.mp4')});
  console.log(`bia ${composition.durationInFrames} khung`);
}
// Highlight podcast: thẻ cuối (highlight.js → endcard), nền đặc → the_cuoi.mp4; render_preview.py ghép SAU video
const HLD = (await import('./src/highlight.js')).default;
const {ENDCARD_ON} = await import('./src/endcard.js');   // highlight podcast hoặc thẻ cuối nhận diện (mọi video có chủ đề)
{ const f = path.join(out, 'the_cuoi.mp4'); if (!ENDCARD_ON) fs.rmSync(f, {force: true});
  else if (!only.size || only.has('the-cuoi')) {
    const composition = await selectComposition({serveUrl, id: 'the-cuoi'});
    await renderMedia({serveUrl, composition, codec: 'h264', crf: 14, concurrency: 4, timeoutInMilliseconds: 240000, muted: true, outputLocation: f});
    console.log(`the-cuoi ${composition.durationInFrames} khung`);
  } }
// Podcast: sân khấu nền chạy suốt video, nền đặc → H.264 (podcast_base.py ghép tiếng → video_goc.mp4)
// (project đã import ở đầu file)
if (project.podcast && (!only.size || only.has('nen'))) {
  const composition = await selectComposition({serveUrl, id: 'nen'});
  const t0 = Date.now();
  await renderMedia({serveUrl, composition, codec: 'h264', crf: 18, concurrency: 4, timeoutInMilliseconds: 240000, muted: true,
    outputLocation: path.join(out, 'nen.mp4')});
  console.log(`nen ${composition.durationInFrames} khung ${((Date.now() - t0) / 1000).toFixed(0)}s`);
}
// Chế độ pillar: hai bên khung chạy suốt video, nền đặc → H.264 (nhẹ, không cần alpha); pillar_base.py ghép video vào giữa
if (output?.layout === 'pillar' && (!only.size || only.has('hai-ben'))) {
  const composition = await selectComposition({serveUrl, id: 'hai-ben'});
  const t0 = Date.now();
  await renderMedia({serveUrl, composition, codec: 'h264', crf: 16, concurrency: 4, timeoutInMilliseconds: 240000, muted: true,
    outputLocation: path.join(out, 'hai_ben.mp4')});
  console.log(`hai-ben ${composition.durationInFrames} khung ${((Date.now() - t0) / 1000).toFixed(0)}s`);
}

// Dọn bản bundle tạm (chép cả public/ — không dọn thì đầy ổ, 2026-11-04)
fs.rmSync(serveUrl, {recursive: true, force: true});
