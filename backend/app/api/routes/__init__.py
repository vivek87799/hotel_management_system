from fastapi import APIRouter
from app.api.routes.demo_route import router as demo_router

router = APIRouter()
router.include_router(demo_router, prefix="/demo_route", tags=["demo_route"])