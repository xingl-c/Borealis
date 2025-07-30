from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.core.lifespan import lifespan               # 应用生命周期管理
from app.api.v1.docs import docs_router             # 自定义 Swagger / ReDoc 路由
from app.api.v1.health import health_router         # 健康检查路由


def create_app() -> FastAPI:
    """
    工厂函数：创建并返回 FastAPI 应用实例。

    主要完成以下初始化工作：
    1. 注册生命周期钩子（启动/关闭）。
    2. 关闭 FastAPI 自动生成的 /docs 与 /redoc，改用自定义路由。
    3. 挂载静态文件目录，为 Swagger UI / ReDoc 提供前端资源。
    4. 配置全局跨域中间件（CORS）。
    5. 注册业务路由（docs、health 等）。
    """
    # 实例化 FastAPI，禁用默认文档入口，使用自定义路由
    app = FastAPI(
        lifespan=lifespan,
        docs_url=None,       # 关闭默认 /docs
        redoc_url=None,      # 关闭默认 /redoc
    )
    app.openapi_version = "3.0.0"

    # -------------------- 路由注册 --------------------
    app.include_router(docs_router)    # 自定义 Swagger UI & ReDoc
    app.include_router(health_router)  # 健康检查

    # -------------------- 静态资源 --------------------
    # 将本地 "static" 目录挂载到 /static，供前端页面引用
    app.mount("/static", StaticFiles(directory="static"), name="static")

    # -------------------- 中间件 ----------------------
    # 全局 CORS 配置：开发阶段允许所有来源、所有方法、所有头
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app