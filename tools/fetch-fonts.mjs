// Baixa os subsets latinos das fontes do Google Fonts e gera static/css/fonts.css
import { mkdir, writeFile } from 'node:fs/promises';

const CSS_URL =
  'https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600;700&family=Instrument+Serif:ital@0;1&display=swap';
const UA =
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36';

const OUT_DIR = new URL('../static/fonts/', import.meta.url);
await mkdir(OUT_DIR, { recursive: true });

const css = await fetch(CSS_URL, { headers: { 'User-Agent': UA } }).then((r) => r.text());

const blocks = css.match(/@font-face\s*\{[^}]*\}/g) ?? [];
const wanted = [];

for (const block of blocks) {
  if (!block.includes('U+0000-00FF')) continue; // apenas subset latin
  const family = /font-family:\s*'([^']+)'/.exec(block)?.[1];
  const style = /font-style:\s*([^;]+);/.exec(block)?.[1].trim() ?? 'normal';
  const weight = /font-weight:\s*([^;]+);/.exec(block)?.[1].trim() ?? '400';
  const url = /url\((https:[^)]+\.woff2)\)/.exec(block)?.[1];
  const range = /unicode-range:\s*([^;]+);/.exec(block)?.[1].trim();
  if (!family || !url) continue;
  wanted.push({ family, style, weight, url, range });
}

let out = '/* Fontes locais geradas por tools/fetch-fonts.mjs — Sora, Inter, Instrument Serif (Google Fonts, SIL Open Font License 1.1) */\n';

for (const f of wanted) {
  const slug = `${f.family.toLowerCase().replace(/\s+/g, '-')}-${f.style}-${f.weight}`;
  const buf = Buffer.from(await fetch(f.url, { headers: { 'User-Agent': UA } }).then((r) => r.arrayBuffer()));
  await writeFile(new URL(slug + '.woff2', OUT_DIR), buf);
  out +=
    `@font-face{font-family:'${f.family}';font-style:${f.style};font-weight:${f.weight};` +
    `font-display:swap;src:url('../fonts/${slug}.woff2') format('woff2');` +
    (f.range ? `unicode-range:${f.range};` : '') +
    '}\n';
  console.log('baixado', slug, buf.length, 'bytes');
}

await writeFile(new URL('../static/css/fonts.css', import.meta.url), out);
console.log('total de fontes:', wanted.length);