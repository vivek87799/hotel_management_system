from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, conlist, validator

class Position(BaseModel):
    position : conlist(float, min_items=2, max_items=2)

class Hotel(BaseModel):
    hotel_api_id : str
    hotel_name : str
    position : List[float]
    bookings : str

class Booking(BaseModel):
    hotel_id : str
    checkin_date : datetime
    checkout_date : datetime
    amount : int
    guest_name : str
    guest_email : str
    guest_phone_number : str


    @validator('checkout_date')
    def date_validator_(cls, checkout_date, values):
        if values["checkin_date"] > checkout_date:
            raise ValueError("You cannot checkout before checking in")
        return checkout_date

    @validator('guest_email')
    def not_valid_email(cls, guest_email, values):
        if "@" not in guest_email:
            raise ValueError("Invalid email")
        return guest_email
    

    
