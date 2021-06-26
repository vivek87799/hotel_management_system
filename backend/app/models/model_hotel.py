from mongoengine import StringField, FloatField, ListField, ReferenceField
# from app.db.database import db

# from .model_booking import Bookings
import mongoengine as db
# Define a hotel collection
class Coordinates:
    def __init__(self, latitude_radians:float=52.12773, longitude_radians:float=11.62916):
        self.latitude_radians = latitude_radians
        self.longitude_radians = longitude_radians
class Hotels(db.Document):
    # id = StringField
    hotel_api_id = StringField(primary_key=True)
    hotel_name = StringField()
    position = ListField(FloatField())
    # bookings = (ReferenceField(Bookings))
    # TODO add number of bookings