# LIMEHOME - Hotel Management System 

####  Functional Features:


This is a lightweight Hotel Management System with backend api
 [Detailed infromation of the application can be found here](https://vivek87799.github.io/hotel_management_system/)

 [The application hosted on heroku](https://powerful-wildwood-21999.herokuapp.com/docs)

Endpoint features:

-> An endpoint that returns a list of hotels near given coordinates (e.g. 48.130323,11.576362)
Takes the latitude and longitude in radians as input and ueses a external an api<> to get the hotels around the area (Input is a list of float)

-> An endpoint to add a list of hotels near given coordinates (e.g. 48.130323,11.576362) to the application database
Takes the latitude and longitude and the hotels obtained from the api<> is persisted on to the Database. (Input is a list of float)

-> An endpoint to get the list of hotels that are persisted on to the application database


-> An endpoint to create a new booking for a given hotel.
A booking has the following attributes:
Hotel ID
Checkin date
Checkin date
Amount
Guest name
Guest email
Guest phone number

    Validations:
    - "hotel_id" should have been persisted on to the application database
    - checkout date should be later than the checkout date
    - guest_email should contain "@" to qualify as a vaild email
    - Every hotel can have a max of 10 bookings

-> An endpoint that return the list of bookings for a given hotel.
    Input is a hotel ID

#### Technical Details

Below are the tools that have been used. For a detailed libraries and version please refer requirements.txt


|         | Tool           |   
| ------------- |:-------------:| 
| Webframework      | FastAPI | 
| Database      | Mongodb      | 
| server | uvicorn      | 
| API documentation | swagger ui      |
| Validations | pydantic      | 
| Testing tool | pytest      | 
| Logging  | python logger      | 
| container-dev | docker      | 
| Hoisting | Heroku      | 


#### Run
```
$git checkout develop/stage
$docker-compose up 
```

#### Test
Required testing files have been added to the application. 
Test log of the application have also been attached
```
$pytest  
```

For more functional and technical documents please refer docs folder.
