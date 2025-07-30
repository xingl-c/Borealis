from app import create_app
from app.core.settings import settings

# 创建 FastAPI 应用实例
app = create_app()

if __name__ == "__main__":
    import uvicorn

    # 启动 FastAPI 应用
    uvicorn.run(
        "main:app",
        host=settings.uvicorn_host,
        port=settings.uvicorn_port,
        reload=settings.uvicorn_reload,
        workers=settings.uvicorn_workers,
    )