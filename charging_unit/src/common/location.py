class Location:
    def __init__(self, lat: float, lng: float):
        self.lat = lat
        self.lng = lng

    def __str__(self):
        return f"({'{:.4f}'.format(self.lat)}, {'{:.4f}'.format(self.lng)})"
