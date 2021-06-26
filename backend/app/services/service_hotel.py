
from typing import List
import json
# from app.db.database import db
from app.api.config import places_api, query_place, limit
from app.utils.helper_functions import api_call, filter_fields_from_api_response
from app.api.custom_logging import LogModule
from app.models.model_hotel import Hotels
import inspect
from typing import TypedDict, List

from pymongo.errors import DuplicateKeyError
from mongoengine import NotUniqueError 




def get_hotels_from_api_service(position:List[float]) -> List[dict]: 

    """
    service call to get a list of hotels near the give coordinate (e.g. 48.130323,11.576362)

    Parameters:
    argument1 (List[float]):  latitude_radians and longitude_radians
    argument1 (str):  place to query eg. hotel
    argument1 (int):  no. of places to retrive

    Returns:
    List[dict]: dict of hotels near the given coordinates

   """

    try:
        LogModule.log_enter_module(inspect.stack()[0][3])
        hotels_response = api_call(position)
        hotels = filter_fields_from_api_response(hotels_response)
        return hotels
    except Exception as error:
        LogModule.log_error(inspect.stack()[0][3], error)
    finally:
        LogModule.log_exit_module(inspect.stack()[0][3])

def get_hotels_from_db_service(id=None) -> List[dict]:
    """
    service call to get the list of hotels from the database

    Parameters:
    argument1 (List[float]):  latitude_radians and longitude_radians
    argument1 (str):  place to query eg. hotel
    argument1 (int):  no. of places to retrive

    Returns:
    List[dict]: dict of hotels near the given coordinates

   """
    
    try:
        LogModule.log_enter_module(inspect.stack()[0][3])
        # returns a mongoengine query parameter
        if id is None:
            hotels = Hotels.objects()
        else:
            hotels = Hotels.objects(id=id)
        # convert to python dict
        hotels_dict = [{"id": hotel.pk, "hotel_api_id": hotel.hotel_api_id,"hotel_name": hotel.hotel_name, "position": hotel.position} for hotel in hotels]
        for _h in hotels_dict:
            print(type(_h))
        return hotels_dict
    except Exception as error:
        LogModule.log_error(inspect.stack()[0][3], error)
    finally:
        LogModule.log_exit_module(inspect.stack()[0][3])


def add_hotels_to_DB_service(position: List[float]) -> List[Hotels]:
    """
    service call to add a list of hotels near a coordinate to the database

    Parameters:
    argument1 (List[float]):  latitude_radians and longitude_radians

    Returns:
    List[dict]: dict of hotels near the given coordinates

   """


    try:
        LogModule.log_enter_module(inspect.stack()[0][3])
        # Get hotels from the api

        _hotels_query = api_call(position)
        hotels = [Hotels(hotel_api_id=hotel["id"], hotel_name=hotel["title"], position=[hotel["position"]["lat"], hotel["position"]["lng"]])\
             for hotel in _hotels_query.get("items")]
        
        
        for _hotel in hotels:
            try:
                _hotel.save()
            except Exception as error:
                LogModule.log_error(inspect.stack()[0][3], error)
        # hotels = model_hotel.Hotels()      
        # convert to pythgon dict 
        return hotels
    except Exception as error:
        print("Error in adding ", error)
        LogModule.log_error(inspect.stack()[0][3], error)
    finally:
        LogModule.log_exit_module(inspect.stack()[0][3])