from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    """异步生命周期管理器，处理启动和关闭逻辑"""
    for sub in ("swagger", "redoc"):
        (Path("static") / sub).mkdir(parents=True, exist_ok=True)
    yield