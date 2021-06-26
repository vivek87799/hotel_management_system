from fastapi import APIRouter
from app.api.routes.demo_route import router as demo_router
from app.api.routes.route_hotel import router as hotel_router

router = APIRouter()
router.include_router(demo_router, prefix="/demo_route", tags=["demo_route"])
router.include_router(hotel_router, prefix="/hotel", tags=['Hotel'])