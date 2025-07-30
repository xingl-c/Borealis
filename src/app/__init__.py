from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.docs import docs_router
from app.api.v1.health import health_router


def create_app() -> FastAPI:
    app = FastAPI(docs_url=None, redoc_url=None)
    app.openapi_version = "3.0.0"
    app.include_router(docs_router)
    app.include_router(health_router)
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app