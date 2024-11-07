import random

from car_park import CarPark
from abc import ABC, abstractmethod


class Sensor(ABC):
    def __init__(self, car_park: CarPark, is_active: bool=False):
        self.car_park = car_park
        self.is_active = is_active

    @abstractmethod
    def update_car_park(self, plate: str):
        pass

    def detect_vehicle(self) -> None:
        plate = self._scan_plate()
        self.update_car_park(plate)

    def _scan_plate(self) -> str:
        return 'Fake-' + format(random.randint(0, 999), '03d')
