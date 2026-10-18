# 本地 Material Symbols 功能图标接入（2026-10-17）

## 修改清单

- `server/static/app.html`：仅新增本地 CSS/JS 引用，带版本参数。
- 新增 `server/static/material-icons.css`、`material-icons.js`：14 种本地图标用于查询、刷新、企业、报告、帮助、历史、补充、下载与步骤；文字与业务代码不变，支持动态子树和 textContent 更新。
- `server/static/icons/`：21 个 SVG 复用，9 个替换为 Google 官方固定提交原件；详见 `SOURCES.md` 与逐文件 `SOURCES.json`。新增官方完整 Apache 2.0 `LICENSE`。
- 新增 `tests/test_material_icons.cjs`：5 项独立 Node 测试。
- 品牌 `logo-mark.svg` 哈希与修改前一致；未作为功能图标替换。

## 来源

Google 官方仓库 `google/material-design-icons`，固定提交 `49d4db35df873165d6bd6ba09b063c7dafbac2f4`。通过官方 GitHub Contents API HTTP 200 取得并验证 Git blob SHA-1 / SHA-256。原件为 Material Symbols Outlined 48px，页面等比显示 18px。全部运行时引用为同源本地 SVG，不依赖 CDN / 图标字体。外部链接仅在来源说明中，不参与运行时请求。

## 备份

`C:\Users\86137\AppData\Local\Temp\greenchain-icons-backup-20261017-124538`

所有被覆盖的既有文件（app.html 和 9 个 SVG）均在修改前完整备份；含 SHA-256 清单与基线。

## 验证结果

- `node --check`：server/static 下 8 个 JS 文件全部通过；新增 Node 测试脚本语法通过。
- `node --test tests/test_material_icons.cjs`：5/5 通过。
- `.venv\Scripts\python.exe -X utf8 -m unittest discover -s tests -v`：38/38 通过。既有测试对写入使用临时账本 / 数据库路径。
- 运行中 `http://127.0.0.1:8910/`：入口 HTTP 200；35 个本地资源 HTTP 200（CSS、JS、30 SVG、许可及来源文件）。
- 使用已有 Playwright Core + 已有 Chromium 1223，不安装浏览器或依赖。真实页面检查：企业卡片/列表重新渲染、企业画像动态帮助和补充按钮、步骤 2/3 按钮文字改变后保留箭头图标、步骤 4 刷新按钮、说明弹窗关闭、forced-colors 与打印隐藏装饰图标。
- 浏览器记录：0 pageerror、0 外部请求、0 失败请求；390px 文档宽度=390px，无页面横向溢出。测试拦截所有非 GET API 请求，未操作生成报告或保存补充。
- 截图目录：`C:\Users\86137\.openclaw\workspace\artifacts\greenchain-icons-20261017`，含桌面企业/画像/核验、手机企业截图与 results.json。
- **视觉未验收**：截图已生成，但视觉工具因认证失败不可用，当前模型亦不支持图像输入；不能仅凭截图生成声称图标美观、对齐或所有屏幕视觉通过。未执行完整键盘/屏幕阅读器验收。

## 数据与运行边界

未编辑 API、数据算法、后端代码或配置，未重启服务。源文件基线对比显示既有文件只有 app.html 和上述 9 个 SVG 改变。检查期间额外观察到基线中没有的 `data/processed/chain_ledger.json`（内有报告记录）；该文件不是本次图标实施的目标文件，未擅自删除/覆盖，也不将它算作图标改动。浏览器测试已禁止非 GET API 写入；不能以此断言运行中的项目没有其他并发数据活动。

请用户刷新页面（必要时 Ctrl+F5）加载本地静态改动，并人工检查图标外观；不需要重启服务。
