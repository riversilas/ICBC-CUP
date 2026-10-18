/* Local Google Material Symbols Outlined. See icons/LICENSE and icons/SOURCES.md.
 * Presentation only: never rewrites labels, handlers, API calls or business state.
 */
(() => {
  'use strict';
  const icon_rules = [
    ['#lookup', 'search'],
    ['#refreshRecent, #refreshChain, #labRefresh, #mergeRevision', 'refresh'],
    ['#freezeBtn, #printReport, #previewSupplement, #editSupplementJson', 'description'],
    ['#startExample, button[data-code]:not(.company-card), .company-card .company-bottom b', 'domain'],
    ['#directVerify, #compare, #useNodeForVerification', 'manage_search'],
    ['#specialNotes, .tip > button', 'help'],
    ['#queryHistory, #loadLegacy', 'history'],
    ['#saveSupplement', 'check_circle'],
    ['#clearMaterial, .dialog-x', 'close'],
    ['#prevBtn', 'arrow_back'],
    ['#nextBtn', 'arrow_forward'],
    ['#simpleDemoAction, #simpleBreak, #simpleRecompute, #runScenario', 'science'],
    ['.report-actions a[download]', 'download'],
    ['.original-stepbar [data-step="1"] b', 'domain'],
    ['.original-stepbar [data-step="2"] b', 'analytics'],
    ['.original-stepbar [data-step="3"] b', 'description'],
    ['.original-stepbar [data-step="4"] b', 'manage_search']
  ];
  function decorate_icons(root) {
    if (!root.querySelectorAll) return;
    for (const [selector, icon_name] of icon_rules) {
      if (root.matches?.(selector)) root.setAttribute('data-material-icon', icon_name);
      root.querySelectorAll(selector).forEach(element => {
        element.setAttribute('data-material-icon', icon_name);
      });
    }
  }
  decorate_icons(document);
  // Only scan new subtrees, not every node after each mutation. The CSS pseudo
  // element survives textContent updates; no observer writes to button children.
  const icon_observer = new MutationObserver(records => {
    for (const record of records) {
      record.addedNodes.forEach(node => {
        if (node.nodeType === Node.ELEMENT_NODE) decorate_icons(node);
      });
    }
  });
  icon_observer.observe(document.body, {childList: true, subtree: true});
})();
