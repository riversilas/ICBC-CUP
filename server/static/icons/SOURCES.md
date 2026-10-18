# 本地功能图标来源与许可

- 作者 / 项目：Google / Material Design Icons，Material Symbols Outlined。
- 官方仓库：https://github.com/google/material-design-icons
- 固定核验版本：`49d4db35df873165d6bd6ba09b063c7dafbac2f4`（2026-10-09 Update Symbols）。
- 核验日期：2026-10-17。许可：Apache License 2.0，完整上游文本见本目录 `LICENSE`。
- 路径模板：`symbols/web/{name}/materialsymbolsoutlined/{name}_48px.svg`。
- 画布：48px，viewBox `0 -960 960 960`；页面通过 CSS mask 等比例显示为 18px 并继承 currentColor。没有改写 SVG 路径，也没有引入字体。

## 实际来源证据

此次 raw.githubusercontent.com / jsDelivr 连接出现重置，尝试的 fonts.gstatic.com search v17/v20 返回 404；这些失败地址**不是**此次交付资源的来源。最终通过官方 GitHub Contents API（api.github.com）固定到上述提交，取得 base64 原始文件，解码并核对 Git blob SHA-1。

`SOURCES.json` 逐个记录 30 个 SVG 与 LICENSE 的实际 API URL、HTTP 200、上游路径、blob SHA-1、SHA-256、字节数和替换前哈希，便于重现核验。示例：

https://api.github.com/repos/google/material-design-icons/contents/symbols/web/search/materialsymbolsoutlined/search_48px.svg?ref=49d4db35df873165d6bd6ba09b063c7dafbac2f4

## 既有资产审计

原目录共 30 个 SVG：21 个与固定提交原件逐字节一致，直接复用；以下 9 个与该提交不一致，因此不能据此证实原始下载来源，本次统一替换为从上述 API 实际取得的官方原件：

`help.svg`、`hub.svg`、`info.svg`、`lock.svg`、`search.svg`、`sync_problem.svg`、`token.svg`、`warning.svg`、`workspace_premium.svg`。

替换后全部 30 个 SVG 与固定提交原件一致，未下载整库。这里的“不一致”不代表原文件一定不是历史官方版本；未查证的历史来源不作断言。

## 接入范围与边界

`../material-icons.css` 和 `../material-icons.js` 在当前 `../app.html` 加载，统一查询、刷新、报告、企业画像、帮助、修订历史、补充记录、下载、步骤和前后步操作。仅取 14 种图标用于本轮映射；其余保留为已核验的小型本地资源集。银行查验使用 manage_search，避免用认证徽章暗示企业真实性认证。

通过稳定选择器加 data-material-icon 与空内容伪元素：不重写按钮文字、事件或业务状态。文字 textContent 更新不会删除伪元素，动态新增的按钮子树由 MutationObserver 装饰；公司卡片只在“查看画像”处显示图标，不破坏其网格。装饰伪元素 content 为空，不进入可访问名称。文字、原 ARIA 名称及禁用状态保留。原有紧凑问号/关闭控件以本地 help/close 图标显示，原字符仍保留在 DOM 中，forced-colors / mask 不支持时回退；打印隐藏装饰图标。

所有运行时图标引用均为 `/static/icons/*.svg` 同源地址，无远程 CDN、字体或脚本。本文的外部链接只用于来源审计，页面不会运行时请求。`../logo-mark.svg` 是独立品牌 Logo，完全不在 Google 图标许可与替换范围内，保持原样。

## 修改前备份

项目外目录：`C:\Users\86137\AppData\Local\Temp\greenchain-icons-backup-20261017-124538`。

包含本次改动前的 `server/static/app.html` 与上述 9 个 SVG，以及 SHA-256 清单。新增文件无需覆盖旧文件；回退时恢复备份文件，并移除本次新增接入文件/许可来源文件/测试与说明即可。未修改数据、API、模型算法或历史存证；未重启服务。

## 明暗切换图标补充

2026-10-17 新增 light_mode.svg 与 dark_mode.svg，同样从上述固定提交的官方 Contents API 下载并核验 Git blob SHA-1，逐项哈希见 SOURCES.json。当前共32个本地SVG；顶部主题按钮使用太阳/月亮表示下一次点击将切换到的模式，默认随系统，手动选择仅在当前页面生效。
