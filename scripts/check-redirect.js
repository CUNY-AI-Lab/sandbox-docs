import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
const pages = fs.readdirSync('.').filter(name => name.endsWith('.md') && name !== 'README.md').map(name => name.slice(0, -3));
for (const file of ['index.html', '404.html']) {
  const html = fs.readFileSync(file, 'utf8');
  const script = html.match(/<script id="docs-redirect">([\s\S]*?)<\/script>/)?.[1];
  assert.ok(script, `${file} must include its redirect`);
  assert.ok(html.includes('<noscript>'));
  assert.ok(!html.includes('marked.min.js'));
  function redirect(pathname, hash = '', search = '') {
    let destination;
    vm.runInNewContext(script, { URL, location: { pathname, hash, search, replace(url) { destination = url; } } });
    return destination;
  }
  for (const page of pages) {
    const target = `https://ailab.gc.cuny.edu/sandbox-docs/${page === 'index' ? '' : page + '/'}`;
    assert.equal(redirect('/sandbox-docs/', '#' + page), target);
    assert.equal(redirect('/sandbox-docs/index.html', '#' + page), target);
    for (const suffix of ['/', '.html', '.md', '']) {
      assert.equal(redirect(`/sandbox-docs/${page}${suffix}`, '#section', '?from=old'), target + '?from=old#section');
    }
  }
  assert.equal(redirect('/sandbox-docs/basic-concepts.html', '#models'), 'https://ailab.gc.cuny.edu/sandbox-docs/basic-concepts/#models');
  assert.equal(redirect('/sandbox-docs/basic-concepts/', '#system-prompts'), 'https://ailab.gc.cuny.edu/sandbox-docs/basic-concepts/#system-prompts');
  assert.equal(redirect('/sandbox-docs/', '#https://other.example'), 'https://ailab.gc.cuny.edu/sandbox-docs/#https://other.example');
  assert.equal(redirect('/sandbox-docs/unknown/'), 'https://ailab.gc.cuny.edu/sandbox-docs/');
  console.log(`PASS ${file}: ${pages.length} article redirects, queries, anchors and fixed destination`);
}
