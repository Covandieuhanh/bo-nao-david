import { createRequire } from 'module';
const require = createRequire('/Users/moon/.nvm/versions/node/v24.18.0/thu-vien/node_modules/@playwright/cli/');
const { chromium } = require('playwright-core');
import fs from 'fs';
const SRC = process.argv[2], OUT = process.argv[3];
fs.mkdirSync(OUT, { recursive: true });
const browser = await chromium.launch({ channel: 'chrome' });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
const meta = {};
for (let n = 1; n <= 8; n++) {
  await page.goto('file://' + SRC + `/bai-${n}.html`, { waitUntil: 'networkidle' });
  await page.addStyleTag({ content: `.wrap{zoom:1!important;margin:0!important} *{animation:none!important;transition:none!important} x-icon{background:none!important;opacity:1!important} x-icon svg{width:100%;height:100%}` });
  await page.addScriptTag({ url: 'https://unpkg.com/lucide@0.460.0/dist/umd/lucide.min.js' }).catch(() => {});
  const missing = await page.evaluate(() => {
    const miss = [];
    for (const el of document.querySelectorAll('x-icon')) {
      const name = el.getAttribute('name');
      const alias = {Chat:'MessageCircle', Warning:'TriangleAlert'}; const node = window.lucide && window.lucide.icons[alias[name] || name];
      if (node) { const svg = window.lucide.createElement(node); el.innerHTML = ''; el.appendChild(svg); }
      else { miss.push(name); el.style.setProperty('background', 'currentColor', 'important'); el.style.borderRadius = '8px'; }
    }
    return miss;
  });
  await page.evaluate(() => document.fonts.ready);
  const info = await page.evaluate(() => [...document.querySelectorAll('section')].map(s => {
    const g = s.parentElement.querySelector('.ghichu');
    return { id: s.id, text: s.innerText.trim(), note: g ? g.innerText.trim() : '' };
  }));
  const title = await page.title();
  const secs = await page.$$('section');
  for (let i = 0; i < secs.length; i++) {
    await secs[i].screenshot({ path: `${OUT}/bai-${n}-${String(i + 1).padStart(2, '0')}.png` });
  }
  meta[n] = { title, slides: info };
  console.log(n, title, secs.length, 'missing icons:', [...new Set(missing)].join(','));
}
fs.writeFileSync(`${OUT}/meta.json`, JSON.stringify(meta, null, 1));
await browser.close();
