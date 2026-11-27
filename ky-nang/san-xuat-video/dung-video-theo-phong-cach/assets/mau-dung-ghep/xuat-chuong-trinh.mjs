// Render bản cuối có tiếng rồi chuẩn hoá âm lượng mạng xã hội: node xuat-chuong-trinh.mjs → ../video-hoan-chinh.mp4
// Một đoạn (xem thử intro…): node xuat-chuong-trinh.mjs <từ giây> <đến giây> <tên.mp4> → ../<tên.mp4>
import {execFileSync, spawnSync} from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import {bundleNhe} from './bundle-nhe.mjs';
import {renderMedia, selectComposition} from '@remotion/renderer';

const [a, b, name] = process.argv.slice(2);
const raw = path.resolve(name ? `../kiem-tra/ban-xuat-tho-${name}` : '../kiem-tra/ban-xuat-tho.mp4');
const out = path.resolve(`../${name || 'video-hoan-chinh.mp4'}`);
fs.mkdirSync(path.dirname(raw), {recursive: true});
const FULL_RENDER = a === undefined;
// CỔNG TỰ CHỌN (19/11/2026, David: "mọi lựa chọn đều phải được tự động setup phù hợp với nội dung của tài nguyên nguồn"):
// render đầy đủ chỉ chạy khi soát cảnh không còn P0 — gồm cả "chưa chẩn đoán" (ke-hoach-canh.md mục Chẩn đoán) và "cả video một kiểu lớp phủ".
// BO_QUA_SOAT=1 chỉ khi David cho phép.
{
  const SOAT = process.env.SOAT_CANH || [
    '.claude/skills/dung-video-theo-phong-cach/scripts/soat-canh.mjs',
    '.agents/skills/video-style-edit/scripts/soat-canh.mjs',
  ].map((p) => path.join(process.env.HOME || '', p)).find((p) => fs.existsSync(p));
  if (FULL_RENDER && !process.env.BO_QUA_SOAT) {
    if (!SOAT || !fs.existsSync(SOAT)) {
      console.error('DỪNG: thiếu soat-canh.mjs. Cài skill hoặc đặt SOAT_CANH tới script của repo.');
      process.exit(1);
    }
    const r = spawnSync(process.execPath, [SOAT, path.resolve('..')], {stdio: 'inherit'});
    if (r.status !== 0) { console.error('DỪNG: bước soát cảnh chưa đạt hoặc chưa chạy được. Xem ../kiem-tra/soat.md và thông báo ở trên.'); process.exit(1); }
  }
}
const serveUrl = await bundleNhe('src/diem-vao.jsx');   // không chép video vào thư mục tạm (bundle-nhe.mjs)
const composition = await selectComposition({serveUrl, id: 'show'});
const t0 = Date.now();
let last = -1;
await renderMedia({serveUrl, composition, codec: 'h264', crf: 18, audioCodec: 'aac', audioBitrate: '256k', concurrency: 3, ...(a !== undefined ? {frameRange: [Math.round(Number(a) * composition.fps), Math.round(Number(b) * composition.fps) - 1]} : {}), timeoutInMilliseconds: 120000, offthreadVideoThreads: 2,
  outputLocation: raw,
  onProgress: ({progress}) => { const p = Math.floor(progress * 10) * 10; if (p !== last) { last = p; process.stdout.write(`${p}% `); } }});
console.log(`\nrender ${((Date.now() - t0) / 1000).toFixed(0)}s`);
// Hiệu ứng + nhạc dễ làm chạm 0 dB. loudnorm MỘT lượt rồi nén AAC cho đỉnh thật −1,0 dB, vượt chuẩn −1,5 (AI bắt ở kiểm cuối vlog
// 10/11/2026) → đo độ to bản thô, tăng đúng mức còn thiếu tới −14 LUFS, chặn đỉnh ở 192 kHz (≈ đỉnh thật) tại −2 dB; lệch nhỏ còn lại
// do chuan-am.py chỉnh. +0,6 dB bù phần limiter ăn bớt.
const ff = fs.existsSync('/opt/homebrew/bin/ffmpeg') ? '/opt/homebrew/bin/ffmpeg' : 'ffmpeg';
const ebur = spawnSync(ff, ['-hide_banner', '-nostats', '-i', raw, '-map', '0:a', '-af', 'ebur128', '-f', 'null', '-'], {encoding: 'utf8'}).stderr;
const inI = Number([...ebur.matchAll(/I:\s+(-?[\d.]+) LUFS/g)].pop()?.[1] ?? -14);
const gain = (-14 - inI + 0.6).toFixed(2);
execFileSync(ff, ['-v', 'error', '-y', '-i', raw, '-c:v', 'copy', '-af',
  `volume=${gain}dB,aresample=192000,alimiter=limit=0.79:level=disabled:attack=5:release=60,aresample=48000`,
  '-c:a', 'aac', '-b:a', '256k', '-movflags', '+faststart', out]);
// Chuẩn âm lượng chung (khối 09): lệch mục tiêu thì chỉnh cả bài
execFileSync('python3', ['-I', path.join(process.env.HOME, '.claude/skills/dung-video-theo-phong-cach/scripts/chuan-am.py'), out], {stdio: 'inherit'});
console.log('xong', out);
// Bản bundle chép CẢ thư mục clip vào thư mục tạm (vlog 48 clip ≈ 4,4 GB/lần) — không dọn thì đầy ổ sau vài chục lần chạy (2026-11-04)
fs.rmSync(serveUrl, {recursive: true, force: true});
