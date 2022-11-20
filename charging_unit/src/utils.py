import urllib.parse

import requests

from charging_unit.src.common.location import Location


def get_lat_lng_from_address(address: str) -> Location:
    print('heh')
    url = f"https://nominatim.openstreetmap.org/search/{urllib.parse.quote(address)}?format=json"
    response = requests.get(url).json()
    if not response:
        return Location(0, 0).to_json()
    lat, lng = response[0]["lat"], response[0]["lon"]
    return Location(lat=lat, lng=lng)
