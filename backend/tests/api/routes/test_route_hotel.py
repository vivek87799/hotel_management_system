from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi.testclient import TestClient

from app.api.server import get_application

app = get_application()


client = TestClient(app)

class Coordinates:
    def __init__(self, latitude_radians:float=52.12773, longitude_radians:float=11.62916):
        self.latitude_radians = latitude_radians
        self.longitude_radians = longitude_radians

hotels_from_api = [
  {
    "id": "here:pds:place:276u3228-04fbe93c8c1a48fab345e1db7b9139c1",
    "hotel_api_id": "here:pds:place:276u3228-04fbe93c8c1a48fab345e1db7b9139c1",
    "hotel_name": "B&B Hotel Magdeburg",
    "position": [
      52.12598,
      11.62902
    ]
  },
  {
    "id": "here:pds:place:276u3228-0afb0501a5781de5ea285efa1b539596",
    "hotel_api_id": "here:pds:place:276u3228-0afb0501a5781de5ea285efa1b539596",
    "hotel_name": "Steigenberger",
    "position": [
      52.12937,
      11.62812
    ]
  },
  {
    "id": "here:pds:place:276u3228-900cdeb564fa430a9cd79a3ac91ed780",
    "hotel_api_id": "here:pds:place:276u3228-900cdeb564fa430a9cd79a3ac91ed780",
    "hotel_name": "Jugendherberge Magdeburg",
    "position": [
      52.12821,
      11.6322
    ]
  },
  {
    "id": "here:pds:place:276u3228-beb01e91ce6140a5ae05a3bbcaea48aa",
    "hotel_api_id": "here:pds:place:276u3228-beb01e91ce6140a5ae05a3bbcaea48aa",
    "hotel_name": "Maritim Hotel Magdeburg",
    "position": [
      52.1293,
      11.6314
    ]
  },
  {
    "id": "here:pds:place:276u3228-84dbaf6dd410410f3d084091cc0338c0",
    "hotel_api_id": "here:pds:place:276u3228-84dbaf6dd410410f3d084091cc0338c0",
    "hotel_name": "MARITIM Hotel Magdeburg",
    "position": [
      52.1293,
      11.6314
    ]
  }
]
def test_route_hotel_get_hotels_from_api():
    response = client.get("/api/hotel/{position}?latitude_radians=52.12773&longitude_radians=11.62916")
    assert response.status_code == 200
    assert response.json() == hotels_from_api

# position = Coordinates()
def test_status_for_no_hotels_found_get_hotels_from_api():
    response = client.get("/api/hotel/{position}?latitude_radians=0&longitude_radians=0")
    assert response.status_code == 200

list_of_hotels= [
  {
    "id": "here:pds:place:276u3228-04fbe93c8c1a48fab345e1db7b9139c1",
    "hotel_api_id": "here:pds:place:276u3228-04fbe93c8c1a48fab345e1db7b9139c1",
    "hotel_name": "B&B Hotel Magdeburg",
    "position": [
      52.12598,
      11.62902
    ]
  },
  {
    "id": "here:pds:place:276u3228-0afb0501a5781de5ea285efa1b539596",
    "hotel_api_id": "here:pds:place:276u3228-0afb0501a5781de5ea285efa1b539596",
    "hotel_name": "Steigenberger",
    "position": [
      52.12937,
      11.62812
    ]
  },
  {
    "id": "here:pds:place:276u3228-900cdeb564fa430a9cd79a3ac91ed780",
    "hotel_api_id": "here:pds:place:276u3228-900cdeb564fa430a9cd79a3ac91ed780",
    "hotel_name": "Jugendherberge Magdeburg",
    "position": [
      52.12821,
      11.6322
    ]
  },
  {
    "id": "here:pds:place:276u3228-beb01e91ce6140a5ae05a3bbcaea48aa",
    "hotel_api_id": "here:pds:place:276u3228-beb01e91ce6140a5ae05a3bbcaea48aa",
    "hotel_name": "Maritim Hotel Magdeburg",
    "position": [
      52.1293,
      11.6314
    ]
  },
  {
    "id": "here:pds:place:276u3228-84dbaf6dd410410f3d084091cc0338c0",
    "hotel_api_id": "here:pds:place:276u3228-84dbaf6dd410410f3d084091cc0338c0",
    "hotel_name": "MARITIM Hotel Magdeburg",
    "position": [
      52.1293,
      11.6314
    ]
  }
]

def test_status_for_hotels_found_get_hotels_from_api():
    response = client.get("/api/hotel/{position}?latitude_radians=52.12773&longitude_radians=11.62916")
    assert response.status_code == 200
    assert response.json() == list_of_hotels

hotels_in_db = [
  {
    "id": "here:pds:place:276u3228-0afb0501a5781de5ea285efa1b539596",
    "hotel_api_id": "here:pds:place:276u3228-0afb0501a5781de5ea285efa1b539596",
    "hotel_name": "Steigenberger",
    "position": [
      52.12937,
      11.62812
    ]
  },
  {
    "id": "here:pds:place:276u3228-900cdeb564fa430a9cd79a3ac91ed780",
    "hotel_api_id": "here:pds:place:276u3228-900cdeb564fa430a9cd79a3ac91ed780",
    "hotel_name": "Jugendherberge Magdeburg",
    "position": [
      52.12821,
      11.6322
    ]
  },
  {
    "id": "here:pds:place:276u3228-04fbe93c8c1a48fab345e1db7b9139c1",
    "hotel_api_id": "here:pds:place:276u3228-04fbe93c8c1a48fab345e1db7b9139c1",
    "hotel_name": "B&B Hotel Magdeburg",
    "position": [
      52.12598,
      11.62902
    ]
  },
  {
    "id": "here:pds:place:276u3228-beb01e91ce6140a5ae05a3bbcaea48aa",
    "hotel_api_id": "here:pds:place:276u3228-beb01e91ce6140a5ae05a3bbcaea48aa",
    "hotel_name": "Maritim Hotel Magdeburg",
    "position": [
      52.1293,
      11.6314
    ]
  },
  {
    "id": "here:pds:place:276u3228-84dbaf6dd410410f3d084091cc0338c0",
    "hotel_api_id": "here:pds:place:276u3228-84dbaf6dd410410f3d084091cc0338c0",
    "hotel_name": "MARITIM Hotel Magdeburg",
    "position": [
      52.1293,
      11.6314
    ]
  }
]

def test_get_hotels_from_db():
    response = client.get("/api/hotel/")
    assert response.status_code == 200
    assert response.json() == hotels_in_db


def test_persist_hotels_to_db():
    response = client.post("/api/hotel/{position}?latitude_radians=52.12773&longitude_radians=11.62916")
    assert response.status_code == 200
    assert response.json() == {"Hotels added successfully" : 5}



