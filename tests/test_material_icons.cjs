const {test} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const crypto = require('node:crypto');
const static_dir = path.join(__dirname, '../server/static');
const source = fs.readFileSync(path.join(static_dir, 'material-icons.js'), 'utf8');
const css = fs.readFileSync(path.join(static_dir, 'material-icons.css'), 'utf8');
function harness() {
  const button = {textContent: '查询记录', attributes: {}, setAttribute(key, value) {this.attributes[key] = value;}};
  let callback;
  const document = {body: {}, querySelectorAll(selector) {return selector === '#lookup' ? [button] : [];}};
  class MutationObserver {constructor(fn) {callback = fn;} observe(target, options) {assert.equal(target, document.body); assert.deepEqual(JSON.parse(JSON.stringify(options)), {childList: true, subtree: true});}}
  vm.runInNewContext(source, {document, MutationObserver, Node: {ELEMENT_NODE: 1}});
  return {button, callback};
}
test('decorates existing query button without rewriting its label', () => {
  const {button} = harness();
  assert.equal(button.attributes['data-material-icon'], 'search');
  assert.equal(button.textContent, '查询记录');
});
test('textContent updates retain the icon selector', () => {
  const {button} = harness(); button.textContent = '正在查询…';
  assert.equal(button.attributes['data-material-icon'], 'search');
  assert.match(css, /\[data-material-icon\]::before/);
});
test('new dynamic subtree is decorated and text nodes are ignored', () => {
  const {button, callback} = harness(); delete button.attributes['data-material-icon'];
  const subtree = {nodeType: 1, matches: () => false, querySelectorAll: selector => selector === '#lookup' ? [button] : []};
  callback([{addedNodes: [{nodeType: 3}, subtree]}]);
  assert.equal(button.attributes['data-material-icon'], 'search');
});
test('all CSS masks are local and exist; no remote runtime dependencies', () => {
  const urls = [...css.matchAll(/url\("([^"\n]*)"\)/g)].map(match => match[1]).filter(Boolean);
  assert.ok(urls.length >= 14);
  for (const url of urls) {assert.ok(url.startsWith('/static/icons/')); assert.ok(fs.existsSync(path.join(static_dir, url.replace('/static/', '').split('?')[0])));}
  assert.doesNotMatch(css, /@import|@font-face|https?:/);
  assert.doesNotMatch(source, /fetch\(|https?:/);
});
test('all local SVGs and Apache license match verified upstream hashes', () => {
  const audit = JSON.parse(fs.readFileSync(path.join(static_dir, 'icons/SOURCES.json'), 'utf8'));
  assert.ok(audit.files.filter(file => file.file.endsWith('.svg')).length >= 30);
  for (const file of audit.files) {
    const bytes = fs.readFileSync(path.join(static_dir, 'icons', file.file));
    assert.equal(crypto.createHash('sha256').update(bytes).digest('hex'), file.sha256, file.file);
  }
});
