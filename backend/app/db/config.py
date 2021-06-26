# mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false

from herepy import PlacesApi

title = "LIMEHOME - Hotel Management system"
description = "Backend api for Hotel Management System"
version = 0.1

api_key = "2w1zATmOw49ZUKS2iJZQp2CdSqpldiGixyWGbgdFaEU"
query_place = "hotel"
limit = 5

places_api = PlacesApi(api_key=api_key)

class Settings:
    database_name = "HMS001"
    user = "admin"
    password = "admin"

    DB_URI = "mongodb+srv://{}:{}@hms001.j1nvm.mongodb.net/{}?retryWrites=true&w=majority".format(user, password, database_name)
