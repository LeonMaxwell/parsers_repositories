import logging
from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse

router = APIRouter(tags=["parsers"])


@router.get("/start_parser")
async def get_test():
    return 200, "Ok"

