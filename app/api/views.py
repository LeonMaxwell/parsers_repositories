import logging
from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from utils.parser import start_process_pool

router = APIRouter(tags=["parsers"])

@router.get("/test1")
async def get_test():
    start_process_pool()
    return 200, "Ok"

