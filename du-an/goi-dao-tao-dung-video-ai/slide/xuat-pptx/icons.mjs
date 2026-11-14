// icons.mjs <thư mục ra> <Tên:màu> …  → <thư mục ra>/<Tên>-<màu>.png (256px, nền trong, nét Lucide)
import { createRequire } from 'module';
const require = createRequire('/Users/moon/.nvm/versions/node/v24.18.0/lib/node_modules/@playwright/cli/');
const { chromium } = require('playwright-core');
const [out, ...items] = process.argv.slice(2);
const b = await chromium.launch({ channel: 'chrome' });
const p = await b.newPage({ viewport: { width: 256, height: 256 } });
await p.setContent('<html><body style="margin:0;background:transparent"><div id="i" style="width:256px;height:256px"></div></body></html>');
await p.addScriptTag({ url: 'https://unpkg.com/lucide@0.460.0/dist/umd/lucide.min.js' });
for (const it of items) {
  const [name, color] = it.split(':');
  const ok = await p.evaluate(([n, c]) => {
    const node = window.lucide.icons[n]; if (!node) return false;
    const svg = window.lucide.createElement(node);
    svg.setAttribute('width', '256'); svg.setAttribute('height', '256'); svg.setAttribute('stroke', '#' + c); svg.setAttribute('stroke-width', '1.75');
    const d = document.getElementById('i'); d.innerHTML = ''; d.appendChild(svg); return true;
  }, [name, color]);
  if (!ok) { console.log('missing', name); continue; }
  await p.locator('#i').screenshot({ path: `${out}/${name}-${color}.png`, omitBackground: true });
}
await b.close();
