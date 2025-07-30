from fastapi import APIRouter
from fastapi.openapi.docs import (
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
    get_redoc_html,
)

# API 文档路由
docs_router = APIRouter(prefix="", tags=["docs"])


@docs_router.get("/docs", include_in_schema=False, summary="Swagger UI 文档页面")
async def custom_swagger_ui_html():
    """自定义 Swagger UI"""
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="API - Swagger UI",
        swagger_js_url="/static/swagger/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger/swagger-ui.css",
    )


@docs_router.get("/docs/oauth2-redirect", include_in_schema=False, summary="Swagger UI OAuth2 回调地址")
async def swagger_ui_redirect():
    """OAuth2 回调地址"""
    return get_swagger_ui_oauth2_redirect_html()


@docs_router.get("/redoc", include_in_schema=False, summary="ReDoc 文档页面")
async def redoc_html():
    """ReDoc 页面"""
    return get_redoc_html(
        openapi_url="/openapi.json",
        title="API - ReDoc",
        redoc_js_url="/static/redoc/redoc.standalone.js",
    )