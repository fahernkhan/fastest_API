from process import *
from fastapi import APIRouter, Response

router = APIRouter()

@router.get("/genre/{year}")
async def search_by_year(year:str):
    _ = {"data":search_movie_by_year(year)}
    return _