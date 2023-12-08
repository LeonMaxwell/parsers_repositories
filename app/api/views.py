from fastapi import APIRouter
from fastapi.responses import JSONResponse

import settings

router = APIRouter(tags=["parsers"])


@router.get("/repos")
async def get_repos():
    query = "SELECT * FROM repositories"
    result = settings.app.db.execute_query(query)
    return JSONResponse({"data": result}, status_code=200)


@router.get("/repos/{langage}")
async def get_repos_by_language(langage: str):
    query = "SELECT * FROM repositories WHERE language='%s'" % (langage)
    result = settings.app.db.execute_query(query)
    return JSONResponse({"data": result}, status_code=200)



