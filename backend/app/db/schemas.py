from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, conlist

class Position(BaseModel):
    position : conlist(float, min_items=2, max_items=2)

class Hotel(BaseModel):
    hotel_api_id : str
    hotel_name : str
    position : Position()
    bookings : str

class Booking(BaseModel):
    hotel_id : str
    checkin_date : datetime
    checkout_date : datetime
    amount : int
    guest_name : str
    guest_email : str
    guest_phone_number : str