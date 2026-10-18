# macOS 启动与故障处理 guidance

## 适用范围

这是Python源码版，不是Mac App。Windows的`启动.bat`、`.exe`和`.venv\Scripts`不能在Mac运行。Intel及Apple Silicon均使用本机Python创建环境；不要从Windows或另一台Mac复制虚拟环境。

本轮补齐Mac启动入口、LF换行、执行权限及Mac CI配置。尚未取得具体Mac报错，也未完成实体Mac人工验收，因此不能保证已排除所有环境问题。

## 1. 推荐启动方法

1. 从仓库main取得完整源码并解压到自己可写的文件夹；不要直接从ZIP中运行。
2. 从 https://www.python.org/downloads/macos/ 安装Python 3.10或以上版本。重新打开“终端”，运行 `python3 --version` 确认。
3. 在终端输入`cd `（末尾有空格），将项目文件夹拖进去，再回车。路径中含中文或空格没关系；确保进入后能看到`app.py`、`requirements.txt`和`start.command`。
4. 执行：

```bash
bash start.command
```

脚本会创建独立的`.venv-macos`并安装依赖，之后打开 http://127.0.0.1:8910/ 。首次安装需要联网；依赖已安装且清单不变时跳过pip安装。

运行时终端不要关闭。停止时在该终端按 **Control+C**，不是Command+C。

### 双击方式

如果希望双击启动，先在项目目录执行一次：

```bash
chmod u+x start.command
```

然后双击`start.command`。ZIP解压可能丢失执行权限，因此即使仓库已设可执行，仍可能需要这一步。没有权限时优先使用`bash start.command`，不要使用`sudo`启动网站。

若macOS提示来源限制，核实源码来源并按所在组织的安全要求处理；不要全局关闭Gatekeeper、不要删除整个下载目录的隔离属性。

## 2. 手动启动（脚本失败时）

在项目根目录逐条执行：

```bash
python3 --version
python3 -m venv .venv-macos
.venv-macos/bin/python -m pip install -r requirements.txt
.venv-macos/bin/python app.py --port 8910
```

不需要激活环境，也不需要Homebrew或全局pip安装。若不想自动打开浏览器，在最后加`--no-browser`，然后手动打开地址。

只执行`app.py`、没有传`--port`时，当前默认端口是8908；文档明确指定8910以避免混淆。

## 3. 常见错误

| 现象 | 处理 |
|---|---|
| `python3: command not found` | 安装Python后重开终端；不要用系统Python2或`py`（Windows Launcher） |
| Python低于3.10 | 安装新版后确认`python3 --version`；已有旧环境请先改名备份，再创建 |
| `Permission denied`执行start.command | 用`bash start.command`，或仅对该文件执行`chmod u+x start.command` |
| `bad interpreter`、`^M` | 重新取得本次修复版本；仓库将.command/.sh固定为LF。旧下载文件不要经Windows编辑器保存成CRLF |
| 环境里只有Scripts没有bin | 那是Windows虚拟环境；不要复用。Mac启动器使用独立`.venv-macos` |
| `externally-managed-environment` | 使用上面的venv命令，别用`--break-system-packages`或sudo pip |
| 无法创建虚拟环境、数据库只读 | 将完整项目复制到本人可写目录，避免只读磁盘映像、受限共享目录；不要递归放宽所有文件权限 |
| 安装依赖出现证书错误 | 检查时间、网络和Python证书。python.org安装包附带的`Install Certificates.command`可按官方安装说明运行；不要使用`--trusted-host`绕过校验 |
| 端口占用 | 原窗口可能已有服务；不要重复启动。换端口可用`PORT=8911 bash start.command`，然后打开8911地址 |
| 没自动打开浏览器 | 终端服务仍在时，手动访问显示的http地址；浏览器打开失败不等于后端失败 |
| 页面打不开 | 确认服务窗口未退出、端口一致。127.0.0.1指当前Mac，不能用它访问另一台Windows上的服务 |
| 动画静止 | 查看网页是否提示“遵循系统减少运动设置”。这是辅助功能行为，不影响数据；不需要关闭系统安全措施 |
| 图表/样式像旧版 | 使用浏览器强制刷新，或在新窗口打开当前端口；确认不是旧源码包 |
| 查不到Windows上的旧报告 | Mac本地账本是独立的。需要按备份恢复步骤迁移对应运行数据，单拷JSON下载包不会创建本地登记记录 |

如果`.venv-macos`损坏或Python升级导致环境不能使用，停止服务，将该目录改名为`.venv-macos.backup`后重新运行。不要删除`data/processed`，那里是报告与补充记录。

## 4. 验证启动是否成功

页面打开后：

1. 选择“开始示例 · 大唐发电”，确认能看到数据和参考评分。
2. 展开雷达，确认年度和缺项说明正常。
3. 到第四步独立查询已有记录；干净项目没有记录是正常的。可自行生成演示报告，再下载JSON进行比对。
4. 刷新页面、重启服务，确认已保存数据仍在。

数据边界、完整四步与打印说明见[使用指南](USER_GUIDE.md)。Safari打印分页和系统字体需在实际Mac检查；不将Windows测试当作Mac验证。

## 5. 迁移已有资料

先停止来源电脑和Mac上的服务，再备份并迁移同一次保存的：

- `data/processed/chain_ledger.json`
- `data/processed/profile_extensions.sqlite3`

不要混用不同日期文件，不复制`.venv`或`.venv-macos`，也不要用根目录旧账本覆盖新链。保留原件，恢复后查询已知摘要并核对补充记录。具体见[维护说明](MAINTENANCE.md)。

## 6. 需要反馈时提供什么

提供Mac芯片（Intel/Apple Silicon）、macOS版本、浏览器版本、`python3 --version`、执行的完整命令及第一条报错。截图应包含出错位置，但不要包含敏感登记包或银行输入。

本仓库新增macOS CI检查启动与核心接口；只有GitHub Actions实际运行通过才可称该CI通过。CI不替代真实Safari/Chrome交互、打印和双击权限验收。
