from fastapi import APIRouter
from app.api.routes.demo_route import router as demo_router
from app.api.routes.route_hotel import router as hotel_router
from app.api.routes.route_booking import router as booking_router

router = APIRouter()
router.include_router(hotel_router, prefix="/hotel", tags=['Hotel'])
router.include_router(booking_router, prefix="/booking", tags=['Booking'])