from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi.testclient import TestClient

from app.api.server import get_application
from app.api.message_constants import CustomErrorMessage, CustomSuccessMessage

from app.db import schemas

app = get_application()


client = TestClient(app)

class Coordinates:
    def __init__(self, latitude_radians:float=52.12773, longitude_radians:float=11.62916):
        self.latitude_radians = latitude_radians
        self.longitude_radians = longitude_radians
new_booking = {
    "hotel_id": "dddd",
  "checkin_date":"2021-04-27T13:02:03.344Z",
  "checkout_date": "2021-05-27T13:02:03.344Z",
  "amount": 0,
  "guest_name": "string",
  "guest_email": "str@ing",
  "guest_phone_number": "string"
}      


"""

def test_add_booking():
    response = client.post("/api/booking", headers={"X-Token": "coneofsilence"},json = {
    "hotel_id": "dddd",
  "checkin_date":"2021-04-27T13:02:03.344Z",
  "checkout_date": "2021-05-27T13:02:03.344Z",
  "amount": 0,
  "guest_name": "string",
  "guest_email": "str@ing",
  "guest_phone_number": "string"
}      ,)
    assert response.status_code == 307
    assert response.json() == str(CustomSuccessMessage.BOOKING_NOT_AUTHORIZED_FOR_THE_HOTEL)
"""



booked_hotel = [
  {
    "hotel_id": {
      "_cls": "Hotels"
    },
    "checkin_date": "2021-06-27T21:26:02.836000",
    "checkout_date": "2021-06-27T21:26:02.836000",
    "guest_name": "string",
    "guest_email": "stri@ng",
    "guest_phone_number": "string",
    "amount": 0
  }
]

# position = Coordinates()
def test_existing_booking():
    response = client.get("/api/booking/here%3Apds%3Aplace%3A276u3228-04fbe93c8c1a48fab345e1db7b9139c1")
    print(response.status_code, response.json())
    assert response.status_code == 200
    assert response.json() == booked_hotel


# position = Coordinates()
def test_non_existing_booking():
    response = client.get("/api/booking/wrongbooking666")
    print(response.status_code, response.json())
    assert response.status_code == 200
    assert response.json() == str(CustomErrorMessage.BOOKING_DOES_NOT_EXIST)



