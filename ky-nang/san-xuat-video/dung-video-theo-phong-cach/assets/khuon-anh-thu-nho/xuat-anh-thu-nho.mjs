// node thumb/xuat-anh-thu-nho.mjs '<props JSON>' <ảnh ra .png> — chạy trong <dự án>/motion (dùng node_modules của dự án)
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {bundle} from '@remotion/bundler';
import {renderStill, selectComposition} from '@remotion/renderer';

const here = path.dirname(fileURLToPath(import.meta.url));
const [json, out] = process.argv.slice(2);
const inputProps = JSON.parse(json);
// public riêng (chỉ ảnh nền) — không để bundler chép cả public/ của dự án (clip video nặng)
const serveUrl = await bundle({entryPoint: path.join(here, 'diem-vao.jsx'), publicDir: path.join(here, 'public')});
const comp = await selectComposition({serveUrl, id: 'thumb', inputProps});
await renderStill({serveUrl, composition: comp, frame: 0, output: path.resolve(out), imageFormat: 'png', inputProps});
fs.rmSync(serveUrl, {recursive: true, force: true});
console.log('ok', out);
