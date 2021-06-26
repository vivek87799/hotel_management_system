import mongoengine as db
from mongoengine import StringField, FloatField, ListField, ReferenceField

from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, conlist


class Settings:
    database_name = "HMS001"
    user = "admin"
    password = "admin"

    DB_URI = "mongodb+srv://{}:{}@hms001.j1nvm.mongodb.net/{}?retryWrites=true&w=majority".format(user, password, database_name)

# Establishing connection to the database
try:
    # db.connect(host="mongodb://127.0.0.1:27017/HMS001")
    db.connect(db=Settings.database_name, host=Settings.DB_URI)
    
except Exception as error:
    # log the exception
    print("logging error", error)

class Position(BaseModel):
    position : conlist(float, min_items=2, max_items=2)

# from .model_booking import Bookings


"""
def get_db():
    
    try:
        db.connect(db=Settings.database_name, username=Settings.user, password=Settings.password, host=Settings.DB_URI)
    except Exception as error:
        # log the exception
        pass
    return db

"""


if __name__ == "__main__":
    # Define a hotel collection
    class Hotels(db.Document):
        # id = StringField
        hotel_api_id = StringField(primary_key=True)
        hotel_name = StringField()
        position = ListField(FloatField())
        # bookings = (ReferenceField(Bookings))
        # TODO add number of bookings
    test_val = Hotels(hotel_api_id= "here:pds:place:276u3228-84dbaf6dd410410f3d084091cc0338c0",
    hotel_name= "MARITIM Hotel demo",
    position=[52.1293, 11.6314])
    test_val.save()
    print("connection to the database")