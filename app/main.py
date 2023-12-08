import uvicorn
from fastapi import FastAPI
import settings
from base_service.exceptions import error_middleware
from api.views import router
from utils.parser import start_process_pool


def init_app() -> FastAPI:
    app = FastAPI(
        title=settings.app.service_name,
        docs_url=f"{settings.app.url_prefix}/docs",
        redoc_url=f"{settings.app.url_prefix}/redoc",
        openapi_url=f"{settings.app.url_prefix}/openapi.json"
    )
    app.include_router(router, prefix=settings.app.url_prefix)
    app.middleware("http")(error_middleware)
    start_process_pool()
    return app


if __name__ == '__main__':
    uvicorn.run("main:init_app", host=settings.app.host, port=settings.app.port, log_level="info")