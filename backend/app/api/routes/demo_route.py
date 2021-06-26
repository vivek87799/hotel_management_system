from typing import List
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_all_cleanings() -> List[dict]:
    welcome_msg = [
        {"Demo route for Limehome HMS"}
    ]
    return welcome_msg