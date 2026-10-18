/* Saved light/dark preference wins; otherwise follow system.
 * Clicks persist the resolved opposite theme. Icons are local Google SVGs. */
(() => {
  'use strict';
  const theme_button = document.getElementById('themeToggle');
  if (!theme_button) return;
  const system_query = window.matchMedia ? window.matchMedia('(prefers-color-scheme: dark)') : null;
  let manual_dark = null;
  try {
    const saved_theme = localStorage.getItem('gc-theme');
    if (saved_theme === 'dark' || saved_theme === 'light') manual_dark = saved_theme === 'dark';
  } catch (_) { /* Storage unavailable: keep system fallback. */ }
  const is_dark = () => manual_dark === null ? !!system_query?.matches : manual_dark;
  function apply_theme() {
    const dark = is_dark();
    if (dark) document.documentElement.setAttribute('data-theme', 'dark');
    else document.documentElement.removeAttribute('data-theme');
    theme_button.setAttribute('data-theme-icon', dark ? 'dark_mode' : 'light_mode');
    const action_label = dark ? '切换到浅色模式' : '切换到深色模式';
    theme_button.setAttribute('aria-label', action_label);
    theme_button.setAttribute('title', action_label);
    theme_button.setAttribute('aria-pressed', String(dark));
    const theme_meta = document.querySelector('meta[name=theme-color]');
    if (theme_meta) theme_meta.setAttribute('content', dark ? '#0c1812' : '#123e30');
  }
  theme_button.onclick = () => {
    manual_dark = !is_dark();
    try { localStorage.setItem('gc-theme', manual_dark ? 'dark' : 'light'); } catch (_) {}
    apply_theme();
  };
  if (system_query) {
    const system_changed = () => { if (manual_dark === null) apply_theme(); };
    if (system_query.addEventListener) system_query.addEventListener('change', system_changed);
    else if (system_query.addListener) system_query.addListener(system_changed);
  }
  apply_theme();
})();
