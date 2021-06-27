from app.api.config import places_api, query_place, limit
from app.api.custom_logging import LogModule
from typing import List, TypedDict
import inspect
from app.api.message_constants import CustomSuccessMessage


def api_call(position: List[float], query: str=query_place, limit: int=limit) -> TypedDict:
    """helper function to get a list of hotels near the give coordinate (e.g. 48.130323,11.576362)

    Parameters:
    argument1 (List[float]):  latitude_radians and longitude_radians
    argument1 (str):  place to query eg. hotel
    argument1 (int):  no. of places to retrive

    Returns:
    dict[dict]: dict of hotels near the given coordinates

   """
    try:
        LogModule.log_enter_module(inspect.stack()[0][3])
        hotels_response = places_api.onebox_search(
            coordinates=position, query=query_place, limit=limit
        )

        hotels = hotels_response.as_dict()
        if len(hotels) == 0:
            assert False,  CustomSuccessMessage.NO_HOTELS_AVAILABLE_FOR_THE_POSITION 
              
        return hotels
    except AssertionError as error:
        assert False, error
    except Exception as error:
        LogModule.log_error(inspect.stack[0][3], error)
    finally:
        LogModule.log_exit_module()

def filter_fields_from_api_response(hotels: List[dict]) -> List[dict]:
    """
    filter fields from the api
    """
    hotels = [{"hotel_api_id": hotel["id"],"name": hotel["title"], "position": hotel["position"]} for hotel in hotels.get("items")]
    return hotels