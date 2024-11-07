from display import Display
from sensor import Sensor


class CarPark:
    def __init__(self, locations, capacity: int, displays: list[Display]=None, sensors: list[Sensor]=None):
        self.location = locations
        self.displays = displays or []
        self.sensors = sensors or []
        self.available_car_bays = capacity
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

    def add_car(self, car_plate: str):
        self.car_plates.append(car_plate)
        self.update_displays()

    def remove_car(self, car_plate: str):
        self.car_plates.remove(car_plate)
        self.update_displays()

    def update_displays(self):
        data = {"available_bays": self.available_bays}
        for display in self.displays:
            display.update(data)

    @property
    def available_bays(self):
        available_bays = self.available_car_bays - len(self.car_plates)
        return 0 if available_bays < 0 else available_bays



