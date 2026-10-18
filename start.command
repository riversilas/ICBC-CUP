#!/bin/bash
# macOS entry point. No sudo, global install, or Gatekeeper changes.
set -eu
cd "$(dirname "$0")"
fail() { printf '\n启动失败：%s\n请查看 docs/MACOS_GUIDANCE.md。\n' "$1" >&2; exit 1; }
if ! command -v python3 >/dev/null 2>&1; then
  fail '未找到 python3。请先从 python.org 安装 Python 3.10 或以上版本，再重新打开终端。'
fi
python3 -c 'import sys; sys.exit(0 if sys.version_info >= (3,10) else 1)' || fail 'Python 版本低于3.10。请安装新版Python。'
VENV='.venv-macos'
if [ -d "$VENV" ] && [ ! -x "$VENV/bin/python" ]; then
  fail '.venv-macos不是可用的Mac虚拟环境。请将此目录改名备份，再重新启动；不要复制Windows的虚拟环境。'
fi
if [ ! -x "$VENV/bin/python" ]; then
  printf '正在创建Mac专用Python环境……\n'
  python3 -m venv "$VENV" || fail '无法创建虚拟环境。请检查Python安装和文件夹写入权限。'
fi
PY="$VENV/bin/python"
"$PY" -c 'import sys; sys.exit(0 if sys.version_info >= (3,10) else 1)' || fail '已有虚拟环境版本过低。请将.venv-macos改名备份，再重试。'
STAMP="$VENV/greentrust-requirements.txt"
if [ ! -f "$STAMP" ] || ! cmp -s requirements.txt "$STAMP" || ! "$PY" -c 'import fastapi, uvicorn' >/dev/null 2>&1; then
  printf '正在安装项目依赖，首次需要联网……\n'
  "$PY" -m pip install -r requirements.txt || fail '依赖安装失败。请检查上方网络、证书或Python错误，不要关闭证书校验。'
  cp requirements.txt "$STAMP"
fi
PORT="${PORT:-8910}"
"$PY" -c 'import sys; p=int(sys.argv[1]); assert 1<=p<=65535' "$PORT" || fail 'PORT必须是1到65535的整数。'
"$PY" -c 'import socket,sys; s=socket.socket(); s.bind(("127.0.0.1",int(sys.argv[1]))); s.close()' "$PORT" || fail '端口无法监听，可能已占用。可使用 PORT=8911 bash start.command；不要结束所有Python进程。'
printf '\n浏览器访问：http://127.0.0.1:%s/\n按 Control+C 停止服务。\n' "$PORT"
exec "$PY" app.py --port "$PORT"
