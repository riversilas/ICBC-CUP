"""绿碳链证根目录融合入口，原主线量化保存在legacy_main.py。"""
from pathlib import Path
import argparse,sys,webbrowser,threading
def main():
    p=argparse.ArgumentParser();p.add_argument('--port',type=int,default=8908);p.add_argument('--no-browser',action='store_true');a=p.parse_args()
    sys.path.insert(0,str(Path(__file__).resolve().parent/'server'))
    import uvicorn
    if not a.no_browser:threading.Timer(1.2,lambda:webbrowser.open(f'http://127.0.0.1:{a.port}')).start()
    uvicorn.run('app:app',app_dir=str(Path(__file__).resolve().parent/'server'),host='127.0.0.1',port=a.port)
if __name__=='__main__':main()
