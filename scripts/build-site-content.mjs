import { spawnSync } from 'node:child_process';
import { readFileSync, writeFileSync } from 'node:fs';
import MarkdownIt from 'markdown-it';
import { renderBody, renderCodeBlock } from './site-markdown.mjs';

const result = spawnSync('python3', ['scripts/build-site-data.py'], { stdio: 'inherit' });
if (result.status !== 0) process.exit(result.status ?? 1);
const data = JSON.parse(readFileSync('site/.vitepress/catalogue.json', 'utf8'));
const md = new MarkdownIt({ html: false, linkify: false });
for (const item of [...data.skills, ...data.agents.flatMap(agent => agent.formats)]) {
  item.html = renderBody(md, item, data);
  if (item.configuration) item.html = `<pre><code class="language-yaml">${md.utils.escapeHtml(item.configuration)}</code></pre>` + item.html;
  delete item.body;
}
for (const item of data.templates) {
  item.html = renderCodeBlock(md, readFileSync(item.path, 'utf8'), item.language);
  delete item.body;
}
writeFileSync('site/.vitepress/content.json', JSON.stringify(data));
