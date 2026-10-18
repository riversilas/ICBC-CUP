# 维护与接口说明

## 1. 入口与目录

| 路径 | 用途 |
|---|---|
| `app.py` | 推荐命令行入口，支持`--port`和`--no-browser`，监听127.0.0.1 |
| `server/app.py` | FastAPI路由；`/`及`/app`提供工作台，导引由前端插入 |
| `server/static/` | 当前生效HTML、CSS、JS、SVG与图标 |
| `carbon_model.py` | 当前V3.2分项、等权综合分、等级和资料完整度 |
| `legacy_main.py` | 当前参考模型的数据适配与旧账本兼容函数，不作为新服务入口 |
| `server/carbon_profile.py` | Scope1/2画像、原值与跨期变化 |
| `server/profile_extensions.py` | 补充资料、修订号与SQLite持久化 |
| `server/profile_evidence.py` | 冻结报告、版本关系、材料比对 |
| `server/chain.py`、`chain_visual.py` | 本地链读写及只读副本演示 |
| `data/carbon_disclosure_ledger.json` | 三家参考模型台账 |
| `data/processed/radar_attachment_snapshot.json` | 当前画像使用的附件观测，不因改模型自动被覆盖 |
| `data/raw/esg_announcements.json` | 公开报告索引 |
| `tests/` | 单元与隔离运行数据测试 |

根目录`static/`与历史设计说明不是当前页面入口。不要同时维护两份工作台；修改前用浏览器Network确认真实请求。历史文档记录当时实现，不覆盖README标明的当前V3.2模型。

## 2. 开发与运行

```powershell
py -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python app.py --port 8910 --no-browser
```

`--no-browser`只是不自动打开浏览器，不停止HTTP服务。不要从项目根目录直接用`uvicorn app:app`：根`app.py`是启动器，不导出FastAPI对象。通过上述启动器运行最稳妥。

静态文件修改通常刷新即可；修改Python模块需要重启对应端口服务。先确认PID与命令行，再停止目标进程，不能批量结束所有Python/Node。

## 3. 数据与报告契约

画像、独立参考评分和冻结报告是不同对象：

1. 画像由当前样本与已保存补充计算。
2. `/api/main-quant/{code}`提供独立V3.2模型结果，不应与旧演示指标混成同一年度数据。
3. 冻结报告使用登记时的manifest。不要显示时重新读取当前画像来覆盖历史报告。
4. 当前报告不包含独立参考评分完整快照；若要扩展，需版本化保存输入、年度、方法、参数、输出与来源，而非只塞一个总分。
5. 旧账本与新链格式不同，不能拼接列表迁移。旧摘要通过独立兼容接口处理。

参考模型第五轴不能替代履约配额核定；历史定价函数不等于实际授信政策。保留当前计算不意味着已证明其经济有效性。

## 4. 主要接口

浏览器运行后可访问自动生成的 [API说明](http://127.0.0.1:8910/docs)，或 `/openapi.json`。端口改变时URL一并改变。当前部分接口直接接收字典，请以实现及实际响应为准，不将文档UI当作严格输入契约的全部保证。

| 方法与路径 | 用途 |
|---|---|
| `GET /api/carbon-profiles` | 八家企业画像列表 |
| `GET /api/carbon-profile/{code}` | 原值、年度、变化、补充与来源 |
| `GET /api/main-quant/{code}` | 独立模型数据；未收录企业返回404 |
| `GET /api/carbon-profile/{code}/supplements` | 已保存补充与修订号 |
| `POST /api/carbon-profile/{code}/supplements` | 保存补充；优先使用页面表单，不手工拼请求 |
| `GET /api/carbon-profile/{code}/freeze-preview` | 冻结前预览；当前前端不完整展示全部差异 |
| `POST /api/carbon-profile/{code}/freeze` | 生成或复用登记版本；请求应带当前`expected_revision` |
| `GET /api/evidence/recent` | 最近登记记录 |
| `GET /api/evidence/{digest}` | 登记内容、版本与链状态 |
| `GET /api/evidence/{digest}/manifest` | 下载JSON登记包 |
| `POST /api/evidence/verify` | 查询/比对提交材料 |
| `GET /api/evidence/chain-map` | 本地链可视化数据 |
| `POST /api/evidence/chain-demo` | 内存副本篡改/断链/重算，不保存真实账本 |
| `GET /api/legacy-evidence/{digest}` | 旧根账本查询与payload摘要复算 |

`/api/companies`及`/api/company/{code}`仍有历史兼容内容，不能代替当前画像或独立模型接口用于正式排名。

## 5. 备份、恢复与更新

- 当前运行数据：`data/processed/chain_ledger.json`与`data/processed/profile_extensions.sqlite3`。
- 先停止服务，再一起复制两个文件。若仍有SQLite的`-wal`/`-shm`文件，保留完整备份并检查是否还有连接，不能在活动写入时只拷主库。
- 备份包含用户补充信息，按内部资料保存，不上传GitHub。
- 恢复前先备份现状；停服务后用同一套备份恢复两文件。用页面查询既有报告，再核对补充记录，确认后继续使用。
- 不靠清空账本解决冲突，不修改历史JSON来“修分数”。代码或模型更新生成新内容，历史记录保持原样。
- 更新源码前检查`git status`，保留本地未提交文件；避免直接整目录覆盖。跨数据版本恢复前另行确认兼容性。

根目录旧`chain_ledger.json`在历史上被追踪，不应顺手加入当前运行数据。不要使用`git add .`上传所有本地材料。

## 6. 测试

```powershell
.venv\Scripts\python -m unittest discover -s tests -p "test_*.py" -v
```

已有用例包含继承，测试执行次数不等于独立用例数。新增写入测试必须使用临时账本与数据库，不对演示现场数据保存表单或生成报告。

建议人工检查：导引进入→大唐量化→雷达/来源→可选补充→生成报告→下载JSON→查询与比对→副本体验→单变量实验→八企业分组。分别记录桌面、390px、减少动态、键盘和打印结果。

当前CI配置在`.github/workflows/tests.yml`。本机测试通过不等于GitHub Actions已运行，也不等于安装包已测试。

## 7. 部署与安全

这不是生产部署指南。服务默认只供本机使用，没有完整登录、用户隔离、上传审核、权限系统及公网运维配置。GitHub Pages只能托管静态内容，不能运行FastAPI或保存本机账本；不要仅上传HTML后宣称全站已部署。

如要公网服务，需另行设计身份权限、TLS、备份、审计、敏感资料处理、限流与可恢复存储。本仓库目前不提供已验证的一键公网方案。

## 8. 发布检查

- 入口、依赖和README与实际源码相同；旧ZIP/EXE不能自动代表新版本。
- `git status`无未解决冲突，模型/数据变更有明确说明。
- 暂存区没有凭据、PDF原文、运行数据库、测试报告或用户登记包。
- 测试通过，并说明未测平台和打印路径。
- Push后核对远程commit；认证失败只说明失败，不重写远程地址或强制推送。
- 未选择许可证前，不承诺代码和第三方材料可自由商用或再发布。
