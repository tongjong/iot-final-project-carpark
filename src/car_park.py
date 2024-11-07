from display import Display
from sensor import Sensor


class CarPark:
    def __init__(self, locations, displays: [Display]=None, sensors: [Sensor]=None):
        self.location = locations
        self.display = displays or []
        self.sensor = sensors or []
        self.available_car_bays = 150
        self.car_plates = [str]

    def __str__(self):
        return f"Location: {self.location}\n Available Car Bays: {self.available_car_bays}"



