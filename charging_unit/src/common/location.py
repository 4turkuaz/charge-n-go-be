class Location:
    def __init__(self, lat: float, lng: float):
        self.lat = lat
        self.lng = lng

    def __str__(self):
        return str(self.to_json())

    def to_json(self):
        return {
            "lat": self.lat,
            "lng": self.lng
        }
