from charging_unit.src.common.location import Location
import requests
import urllib.parse


def get_lat_lng_from_address(address: str) -> Location:
    url = f"https://nominatim.openstreetmap.org/search/{urllib.parse.quote(address)}?format=json"
    response = requests.get(url).json()
    lat, lng = response[0]["lat"], response[0]["lng"]

    return Location(lat=lat, lng=lng)