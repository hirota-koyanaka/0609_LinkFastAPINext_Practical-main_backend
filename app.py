import sys
import os

# backendディレクトリをPythonパスに追加
sys.path.append(os.path.abspath("backend"))

# backend/app.pyからアプリケーションをインポート
from backend.app import app

# このファイルが直接実行された場合
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
