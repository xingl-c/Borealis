from fastapi import APIRouter


# 健康检查路由
health_router = APIRouter(prefix="", tags=["Health Check"])


@health_router.get("/health", summary="健康检查接口")
async def health_check():
    """
    健康检查接口  
    返回 200 OK 表示服务运行正常
    """
    return {"status": "ok", "message": "service is healthy"}