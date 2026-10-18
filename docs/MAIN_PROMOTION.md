# 主工作区架构替换与兼容验收

## 选择与基线
用户确认保留bb4afc5界面，替换main根架构。main已独立发展到d1587e4，用户明确选择保留main V3.2新模型，而非8909旧PCPS模型。

主工作区：C:\Users\river\Desktop\绿碳链证_主工作区（Git worktree，分支main）。原ICBC-cup-GreenTrust工作目录保留feature分支、未提交旧账本和未跟踪子项目，不被清空。
备份：ICBC主线_backup_promote_20261016_205802，103文件校验；backup/main-before-promote-20261016保留原main历史。

## 合并策略
- 新FastAPI启动器替换旧根WSGI启动；原main app移到legacy_main.py，作为模型数据适配和旧账本核验模块。
- carbon_model.py保留main版本，未用旧分支覆盖。核对文本一致（Git换行正常化可能导致原始字节差异）。
- 界面/方法表/八企业维度标签与main模型适配：等权五维20%、k5、1000唯一标尺、中文完整度。模型说明取API配置，不再保留三维40/35/25或750固定文案。
- 新历史查询接口/api/legacy-evidence/{digest}调用main增强摘要重算查验；与当前链/api/evidence接口隔离。
- 根static HTML与server/static/index.html改兼容跳转，避免两个旧首页误入口。其余静态资产保留兼容。
- README、Windows启动.bat、requirements、tests和CI同步新架构；旧说明标历史，不代表当前模型。

## 实测
- 新主工作区8910启动，首页200，八企业可读取。
- main V3.2：大唐43.5/B-、浙能38.2/B-、国投78.1/A；五项各20%，完整度分别完整/完整/部分，与原main模型一致。
- 38次unittest执行通过（包含继承重复，不是38独立用例）。
- 11项Edge页面检查通过：核心路径、同业强度一致、单变量实验与八企业分组、390px布局。
- 新工作区独立生成报告并提交manifest，material_match=true、chain OK。此测试只写新工作区忽略的运行数据，原8909数据不改变。
- 19个静态资源逐项HTTP请求无缺失。JS语法检查通过。

## 数据与发布边界
历史root chain_ledger.json保留main跟踪版本；原目录未提交账本和data/processed用户数据库不复制进Git提交、不重写。新工作区从独立运行数据起步，若后续需要迁移真实资料，须在停服务与备份后完整迁移当前两文件，不把旧格式根账本硬并入新哈希链。

远程git fetch仍Repository not found，无法确认最新GitHub或推送权限，不强制推送、不改远程地址、不建公开替代仓库。main本地合并后仍需GitHub Desktop授权账号Push origin，或在Agent设置连接仓库。

## 未验证/保留限制
未在新虚拟环境下载依赖，未运行bat双击、macOS/Linux、EXE、实体手机、Firefox或完整打印验收。不称正式银行模型或独立联盟链。main模型仍含历史定价函数/配额解释，其研究有效性未验证；默认界面使用中性偏离说明，不将其作为实际金融建议。评分不在当前画像manifest中，范围声明保留。现有旧ZIP未重新构建。
