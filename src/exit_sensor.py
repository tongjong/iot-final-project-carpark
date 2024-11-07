import random

from sensor import Sensor

class ExitSensor(Sensor):
    def __str__(self):
        return f"Exir Sensor Active Status: {self.is_active}? 'Active' : 'Inactive'"

    def update_car_park(self, plate: str) -> None:
        self.car_park.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")

    def _scan_plate(self) -> str:
        return random.choice(self.car_park.car_plates)