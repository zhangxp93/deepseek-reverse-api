"""Start server script with environment loading"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Import and run the server
if __name__ == "__main__":
    import uvicorn
    from asgiref.wsgi import WsgiToAsgi
    # 显式导入你的 server 模块中的 Flask app
    from server import app

    port = int(os.environ.get('PORT', 8000))
    host = os.environ.get('HOST', '0.0.0.0')

    print(f"Starting DeepSeek AI Reverse API Server on {host}:{port}")
    print(f"Features: Account Pool, Vless Proxy Support, OpenAI Compatible API (ASGI Mode)")

    # 核心魔法：把 WSGI (Flask) 转换成 ASGI (Uvicorn 兼容)
    asgi_app = WsgiToAsgi(app)

    uvicorn.run(
        asgi_app,  # 直接传递转换后的对象，不再传字符串
        host=host,
        port=port,
        reload=False,
        log_level=os.environ.get('LOG_LEVEL', 'info').lower()
    )