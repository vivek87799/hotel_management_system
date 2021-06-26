from typing import List, TypedDict
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def demo_route() -> TypedDict:
    welcome_msg = {"message":"Demo route for Limehome HMS"}
    return welcome_msg