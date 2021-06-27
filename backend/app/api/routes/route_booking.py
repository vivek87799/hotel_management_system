from typing import Dict, List, Optional, TypedDict
import inspect
from fastapi import APIRouter,Depends, HTTPException, Response, status
# from app.db.schemas import Booking as booking_schema
from app.db import schemas
from app.models.model_booking import Bookings as booking_model
from app.api.custom_logging import LogModule
# from app.services import add_booking_service, get_hotel_bookings_service
from app.services import service_booking
from fastapi.responses import JSONResponse
from app.api.message_constants import CustomSuccessMessage, CustomErrorMessage
from http import HTTPStatus

router = APIRouter()

#TODO Add endpoint to query based on booking id 

@router.post('/')
def add_booking(new_booking: schemas.Booking) -> str:
    """
    Add a new bookings to a hotel

    Parameters:
    argument1 (Booking):  booking schema

    Returns:
    str: Success or Failure message

   """

    try:
        LogModule.log_enter_module(inspect.stack()[0][3])
        
        # Create a booking_model object
        booking = booking_model(hotel_id=new_booking.hotel_id, checkin_date=new_booking.checkin_date, \
            checkout_date=new_booking.checkout_date,\
            amount=new_booking.amount, guest_name=new_booking.guest_name, guest_email=new_booking.guest_email,\
                guest_phone_number=new_booking.guest_phone_number)
        
        # Call service to add booking to the collection
        booking_status = service_booking.add_booking(booking)
        return JSONResponse(status_code=status.HTTP_200_OK, content=str(CustomSuccessMessage.BOOKING_SCCESSFULL))
    
    except AssertionError as error:
        return JSONResponse(status_code=status.HTTP_200_OK, content=str(error))

    except Exception as error:
        return JSONResponse(status_code=status.HTTP_200_OK, content=str(error))
    
    finally:
        LogModule.log_exit_module(inspect.stack()[0][3])


@router.get('/{hotel_id}')
def get_hotel_bookings(hotel_id: str):
    """Returns a ist of bookings for a hotel

    Parameters:
    argument1 (str):  hotel_id

    Returns:
    List[dict]: List of bookings for the hotel

   """
    try:
        LogModule.log_enter_module(inspect.stack()[0][3])
        
        # Call service to get bookings for the given hotel_id
        booking = service_booking.get_hotel_bookings(hotel_id)
        return booking

    except AssertionError as error:
        return JSONResponse(status_code=status.HTTP_200_OK, content=str(error))
    
    except Exception as error:
        LogModule.log_error(inspect.stack()[0][3], error)
    
    finally:
        LogModule.log_exit_module(inspect.stack()[0][3])


    


