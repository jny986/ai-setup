import path from 'node:path';

const repo = 'https://github.com/jny986/ai-setup/blob/main/';

export function renderCodeBlock(md, body, language) {
  const label = md.utils.escapeHtml(language);
  // Line spans preserve blank lines when VitePress prepares clipboard text.
  const code = body.split('\n').map(line => `<span class="line">${md.utils.escapeHtml(line)}</span>`).join('\n');
  return `<div class="language-${label}"><button type="button" title="Copy code" data-copied="Copied" class="copy"></button><span class="lang">${label}</span><pre tabindex="0"><code>${code}</code></pre></div>`;
}

export function resolveLink(href, source, data) {
  if (/^(?:[a-z][a-z\d+.-]*:|\/\/)/i.test(href)) return href;
  if (href.startsWith('#')) return repo + source + href;
  const [file, fragment = ''] = href.split('#');
  const target = path.posix.normalize(path.posix.join(path.posix.dirname(source), file));
  for (const section of ['skills', 'agents', 'templates']) {
    const item = data[section].find(item => item.path === target || item.formats?.some(format => format.path === target));
    if (item && !fragment) return `/${section}.html#${item.id}`;
  }
  return repo + target + (fragment ? '#' + fragment : '');
}

// Render as inert HTML data, never as a Vue template. Raw source HTML is escaped.
export function renderBody(md, item, data) {
  if (item.language && item.language !== 'markdown') {
    return `<pre><code class="language-${md.utils.escapeHtml(item.language)}">${md.utils.escapeHtml(item.body)}</code></pre>`;
  }
  const tokens = md.parse(item.body, {});
  const walk = tokens => {
    for (const token of tokens) {
      if (token.type === 'link_open') token.attrSet('href', resolveLink(token.attrGet('href'), item.path, data));
      if (token.type === 'image' && !/^(?:[a-z][a-z\d+.-]*:|\/\/)/i.test(token.attrGet('src'))) token.attrSet('src', 'https://raw.githubusercontent.com/jny986/ai-setup/main/' + path.posix.normalize(path.posix.join(path.posix.dirname(item.path), token.attrGet('src'))));
      // Keep the catalogue hierarchy: source headings start at h3.
      if (token.type.startsWith('heading_')) token.tag = `h${Math.min(6, Number(token.tag.slice(1)) + 2)}`;
      if (token.children) walk(token.children);
    }
  };
  walk(tokens);
  return md.renderer.render(tokens, md.options, {});
}
