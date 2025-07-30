from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    全局配置类，继承自 pydantic-settings 的 BaseSettings，可自动读取 .env 文件或环境变量。
    """
    # pydantic 的配置，env_file 指定 .env 文件路径，extra=ignore 忽略未定义的环境变量
    model_config = {"env_file": ".env", "extra": "ignore"}

    # -------------------------------------------------
    # Uvicorn 运行参数
    # -------------------------------------------------
    uvicorn_host: str = Field(
        default="0.0.0.0",
        description="默认主机地址"
    )
    uvicorn_port: int = Field(
        default=8000,
        description="默认端口"
    )
    uvicorn_reload: bool = Field(
        default=True,
        description="是否启用热重载，开发环境建议开启"
    )
    uvicorn_workers: int = Field(
        default=1,
        description="仅在 reload=False 时有效，默认为 1"
    )


# 单例
@lru_cache
def get_settings() -> Settings:
    """获取全局配置实例，使用 lru_cache 缓存以提高性能"""
    return Settings()


# 获取全局配置实例
settings = get_settings()