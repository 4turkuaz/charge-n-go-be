import urllib.parse

import requests


def get_lat_lng_from_address(address: str):
    url = f"https://nominatim.openstreetmap.org/search/{urllib.parse.quote(address)}?format=json"
    response = requests.get(url).json()
    lat, lng = (0, 0) if not response else (response[0]["lat"], response[0]["lon"])
    return {"lat": lat, "lng": lng}
