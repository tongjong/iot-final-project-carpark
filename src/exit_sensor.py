import random
from typing import override

from sensor import Sensor

class ExitSensor(Sensor):
    def __str__(self):
        return f"Exir Sensor Active Status: {self.is_active}? 'Active' : 'Inactive'"

    def update_car_park(self, plate: str) -> str:
        self.car_park.remove_car(plate)
        return f"Outgoing 🚗 vehicle detected. Plate: {plate}"

    def _scan_plate(self) -> str:
        return random.choice(self.car_park.car_plates)

    @override
    def detect_vehicle(self) -> None:
        plate = self._scan_plate()
        self.update_car_park(plate)