from typing import List, Optional, TypedDict
import inspect
from fastapi import APIRouter,Depends, HTTPException, Response, status
from app.api.custom_logging import LogModule
from app.services import get_hotels_from_api_service, get_hotels_from_db_service, add_hotels_to_DB_service
from fastapi.responses import JSONResponse
from http import HTTPStatus


router = APIRouter()
class Coordinates:
    def __init__(self, latitude_radians:float=52.12773, longitude_radians:float=11.62916):
        self.latitude_radians = latitude_radians
        self.longitude_radians = longitude_radians

@router.get('/{position}')
async def get_hotels_from_api(*, position: Coordinates = Depends(Coordinates)) -> List[dict]:

    """Gives a ist of hotels near the give coordinate (e.g. 48.130323,11.576362)

    Parameters:
    argument1 (object):  latitude_radians and longitude_radians

    Returns:
    List[dict]: dict of hotels near the given coordinates

   """
    try:
        LogModule.log_enter_module(inspect.stack()[0][3])
        hotels = get_hotels_from_api_service([position.latitude_radians, position.longitude_radians])
        if len(hotels) == 0:
            # return JSONResponse(status_code=status.HTTP_204_NO_CONTENT.value)
            return Response(status_code=HTTPStatus.NO_CONTENT.value)
        else:   
            return JSONResponse(status_code=status.HTTP_200_OK, content=hotels)

    except Exception as error:
        LogModule.log_error(inspect.stack()[0][3], error)
    finally:
        LogModule.log_exit_module(inspect.stack()[0][3])


@router.get('/')
async def get_hotels_from_DB() -> List[dict]:

    """Gives a ist of hotels that are persisted in the database

    Parameters: None

    Returns:
    dict[dict]: dict of hotels near the given coordinates

   """
    try:
        LogModule.log_enter_module(inspect.stack()[0][3])
        hotels = get_hotels_from_db_service()
        
        return hotels
    except Exception as error:
        LogModule.log_error(inspect.stack()[0][3], error)
    finally:
        LogModule.log_exit_module(inspect.stack()[0][3])


@router.post('/{position}')
async def persist_hotels_from_api_to_db(position: Coordinates = Depends(Coordinates)) -> dict:

    """Save a ist of hotels near the give coordinate (e.g. 48.130323,11.576362) to the database

    Parameters:
    argument1 (object):  latitude_radians and longitude_radians

    Returns:
    dict[str: int]: {msg: number of hotels added to the database}

   """
    try:
        LogModule.log_enter_module(inspect.stack()[0][3])
        hotels = add_hotels_to_DB_service([position.latitude_radians, position.longitude_radians])
        
        return {"Hotels added successfully" : len(hotels)}
    except Exception as error:
        LogModule.log_error(inspect.stack()[0][3], error)
    finally:
        LogModule.log_exit_module(inspect.stack()[0][3])