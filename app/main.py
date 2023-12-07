import logging
import uvicorn
from fastapi import FastAPI
import settings
from base_service.exceptions import error_middleware
from api.views import router


logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def init_app() -> FastAPI:
    app = FastAPI(
        title=settings.app.service_name,
        docs_url=f"{settings.app.url_prefix}/docs",
        redoc_url=f"{settings.app.url_prefix}/redoc",
        openapi_url=f"{settings.app.url_prefix}/openapi.json"
    )
    app.include_router(router, prefix=settings.app.url_prefix)
    app.middleware("http")(error_middleware)
    return app


if __name__ == '__main__':
    uvicorn.run("main:init_app", host=settings.app.host, port=settings.app.port, log_level="info")