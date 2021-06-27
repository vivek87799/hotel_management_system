from typing import List
import json
# from app.db.database import db
from app.api.custom_logging import LogModule
from app.models.model_booking import Bookings as Booking_model
from app.api.message_constants import CustomErrorMessage
import inspect
from typing import TypedDict, List

from pymongo.errors import DuplicateKeyError
from mongoengine import NotUniqueError 
from http import HTTPStatus


def add_booking(booking: Booking_model):
    """
    Add a new bookings to a hotel

    Parameters:
    argument1 (Booking):  booking schema

    Returns:
    str: Success or Failure message

   """
    try:
        LogModule.log_enter_module(inspect.stack()[0][3])
        # TODO 
        try:
            # Ger bookings for the given hotel_id
            no_bookings = Booking_model.objects(hotel_id=booking.hotel_id).count()
        except Exception as error:
            assert False, CustomErrorMessage.BOOKING_NOT_AUTHORIZED_FOR_THE_HOTEL
        

        # if less than 10 add booking else raise custom exception
        if no_bookings < 10:
            try:
                booked = booking.save()
            except Exception as error:
                assert False, CustomErrorMessage.MAXIMUM_BOOKING_FOR_THE_HOTEL
            
            return True
        else:
            LogModule.log_error(inspect.stack()[0][3], CustomErrorMessage.BOOKING_NOT_AUTHORIZED_FOR_THE_HOTEL)
            assert False, CustomErrorMessage.BOOKING_NOT_AUTHORIZED_FOR_THE_HOTEL

    except AssertionError as error:
        assert False, error
    except Exception as error:
        LogModule.log_error(inspect.stack()[0][3], error)
    
    finally:
        LogModule.log_exit_module(inspect.stack()[0][3])

def get_hotel_bookings(hotel_id: str):
    """
    Returns a ist of bookings for a hotel

    Parameters:
    argument1 (str):  hotel_id

    Returns:
    List[dict]: List of bookings for the hotel

   """
    try:
        LogModule.log_enter_module(inspect.stack()[0][3])
        
        # Ger bookings for the given hotel_id
        bookings = Booking_model.objects(hotel_id=hotel_id)
        LogModule.log_message(bookings, inspect.stack()[0][3])

        # convert ot list of python dict
        bookings_json = [{"hotel_id":booking["hotel_id"], "checkin_date":booking["checkin_date"], \
            "checkout_date":booking["checkout_date"], "guest_name":booking["guest_name"], "guest_email":booking["guest_email"],\
                 "guest_phone_number":booking["guest_phone_number"], "amount":booking["amount"]} for booking in bookings] 
        
        # If no bookings found for the hotel raise assertion error
        if len(bookings) == 0:
            assert False , CustomErrorMessage.BOOKING_DOES_NOT_EXIST
        return bookings_json

    except AssertionError as error:
        assert False, error
    except Exception as error:
        LogModule.log_error(inspect.stack()[0][3], error)
    finally:
        LogModule.log_exit_module(inspect.stack()[0][3])