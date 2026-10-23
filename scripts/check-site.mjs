import assert from 'node:assert/strict';
import { readFileSync, readdirSync } from 'node:fs';
import MarkdownIt from 'markdown-it';
import { renderBody, resolveLink } from './site-markdown.mjs';

const data = JSON.parse(readFileSync('site/.vitepress/catalogue.json', 'utf8'));
const dist = 'site/.vitepress/dist/';
for (const name of ['index', 'skills', 'agents', 'templates', 'sources']) {
  const html = readFileSync(dist + name + '.html', 'utf8');
  assert(html.includes('/assets/'), `${name}: assets need the domain-root base`);
  assert(!/(?:href|src)="\/ai-setup\//.test(html), `${name}: legacy project paths must be absent`);
  for (const route of ['skills', 'agents', 'templates', 'sources']) assert(html.includes(`href="/${route}.html`));
  assert(html.includes('Skip to content'));
  if (name === 'index') continue;
  for (const item of data[name]) {
    assert.equal(html.split(`id="${item.id}"`).length - 1, 1, `${name}: ${item.id} must occur exactly once`);
    for (const file of item.formats || [item]) {
      if (file.url) assert(html.includes(file.url.replaceAll('&', '&amp;')), `${file.path}: missing source URL`);
    }
  }
  assert(!/<input\b/.test(html), 'Search must be absent before JS enhancement');
}
assert.deepEqual(readdirSync(dist).filter(name => name.endsWith('.html')).sort(), ['404.html', 'agents.html', 'index.html', 'skills.html', 'sources.html', 'templates.html']);
const md = new MarkdownIt({ html: false });
const escaped = renderBody(md, { path: 'skills/tdd/SKILL.md', body: '<script>alert(1)</script> {{ dangerous() }}\n\n[relative](references/foo.md)' }, data);
assert(!escaped.includes('<script>'));
assert(escaped.includes('{{ dangerous() }}'));
assert(escaped.includes('https://github.com/jny986/ai-setup/blob/main/skills/tdd/references/foo.md'));
assert.equal(resolveLink('../git/SKILL.md', 'skills/tdd/SKILL.md', data), '/skills.html#skill-git');
assert.equal(resolveLink('https://example.com', 'skills/tdd/SKILL.md', data), 'https://example.com');
console.log('Static routes, catalogue coverage, production paths and inert Markdown checks passed.');
