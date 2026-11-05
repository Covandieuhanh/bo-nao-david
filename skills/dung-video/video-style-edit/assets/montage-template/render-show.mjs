// Render bản cuối có tiếng rồi chuẩn hoá âm lượng mạng xã hội: node render-show.mjs → ../video-final.mp4
// Một đoạn (xem thử intro…): node render-show.mjs <từ giây> <đến giây> <tên.mp4> → ../<tên.mp4>
import {execFileSync} from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import {bundle} from '@remotion/bundler';
import {renderMedia, selectComposition} from '@remotion/renderer';

const [a, b, name] = process.argv.slice(2);
const raw = path.resolve(name ? `../check/raw-${name}` : '../check/raw-render.mp4');
const out = path.resolve(`../${name || 'video-final.mp4'}`);
fs.mkdirSync(path.dirname(raw), {recursive: true});
const serveUrl = await bundle({entryPoint: path.resolve('src/index.jsx')});
const composition = await selectComposition({serveUrl, id: 'show'});
const t0 = Date.now();
let last = -1;
await renderMedia({serveUrl, composition, codec: 'h264', crf: 18, audioCodec: 'aac', audioBitrate: '256k', concurrency: 3, ...(a !== undefined ? {frameRange: [Math.round(Number(a) * composition.fps), Math.round(Number(b) * composition.fps) - 1]} : {}), timeoutInMilliseconds: 120000, offthreadVideoThreads: 2,
  outputLocation: raw,
  onProgress: ({progress}) => { const p = Math.floor(progress * 10) * 10; if (p !== last) { last = p; process.stdout.write(`${p}% `); } }});
console.log(`\nrender ${((Date.now() - t0) / 1000).toFixed(0)}s`);
// Hiệu ứng + nhạc dễ làm chạm 0 dB → loudnorm về -14 LUFS, đỉnh -1.5 dB
const ff = fs.existsSync('/opt/homebrew/bin/ffmpeg') ? '/opt/homebrew/bin/ffmpeg' : 'ffmpeg';
execFileSync(ff, ['-v', 'error', '-y', '-i', raw, '-c:v', 'copy', '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000',
  '-c:a', 'aac', '-b:a', '256k', '-movflags', '+faststart', out]);
console.log('xong', out);
// Bản bundle chép CẢ thư mục clip vào thư mục tạm (vlog 48 clip ≈ 4,4 GB/lần) — không dọn thì đầy ổ sau vài chục lần chạy (2026-11-04)
fs.rmSync(serveUrl, {recursive: true, force: true});
