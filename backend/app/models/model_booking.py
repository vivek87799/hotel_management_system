# from app.models.model_hotel import Hotels
from mongoengine import IntField, StringField, ReferenceField, DateTimeField
from app.models.model_hotel import Hotels
import mongoengine as db

# Define a booking collection
class Bookings(db.Document):
    hotel_id = ReferenceField(Hotels)
    checkin_date = DateTimeField(required=True)
    checkout_date = DateTimeField(required=True)
    guest_name = StringField(required=True)
    guest_email = StringField(required=True)
    guest_phone_number = StringField(required=True)
    amount = IntField(required=True)        

    