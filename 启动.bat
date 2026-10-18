@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
rem Check the interpreter itself; an existing copied venv may be broken.
if not exist ".venv\Scripts\python.exe" goto rebuild
.venv\Scripts\python.exe -c "import sys; assert sys.version_info >= (3,10)" >nul 2>&1
if errorlevel 1 goto preserve
goto install
:preserve
set "OLDENV=.venv-invalid-%RANDOM%-%RANDOM%"
move ".venv" "%OLDENV%" >nul
if errorlevel 1 goto fail
echo 原有环境不可用，已改名保留为 %OLDENV%。
:rebuild
py -3 -m venv .venv
if errorlevel 1 goto fail
:install
.venv\Scripts\python.exe -c "import fastapi, uvicorn" >nul 2>&1
if errorlevel 1 goto dependencies
if not exist ".venv\greentrust-requirements.txt" goto dependencies
fc /b requirements.txt .venv\greentrust-requirements.txt >nul 2>&1
if errorlevel 1 goto dependencies
goto launch
:dependencies
.venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 goto fail
copy /y requirements.txt .venv\greentrust-requirements.txt >nul
:launch
.venv\Scripts\python.exe app.py --port 8910
if errorlevel 1 goto fail
goto end
:fail
echo 启动失败，请查看上方错误。需要Python 3.10以上和可联网的首次安装环境。
echo 请勿复制其他电脑的 .venv，打包时须排除所有虚拟环境及 __pycache__。
:end
pause
