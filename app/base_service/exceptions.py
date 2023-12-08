import logging
import traceback
from starlette.responses import JSONResponse
from fastapi import Request

logger = logging.getLogger(__name__)


async def error_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        error_message = str(e)
        logger.error(traceback.format_exc())
        return JSONResponse(content={
            'data': None,
            'error_type': 'Internal Server Error',
            'error_message': error_message
        }, status_code=500)