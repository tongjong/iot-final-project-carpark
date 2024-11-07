from display import Display
from sensor import Sensor


class CarPark:
    def __init__(self, locations, displays: list[Display]=None, sensors: list[Sensor]=None):
        self.location = locations
        self.displays = displays or []
        self.sensors = sensors or []
        self.available_car_bays = 150
        self.car_plates = []

    def __str__(self):
        return f"Location: {self.location}\n Available Car Bays: {self.available_car_bays}"

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Component must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        if isinstance(component, Display):
            self.displays.append(component)



