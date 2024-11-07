from enum import Enum
from car_park import CarPark

class DisplayType(Enum):
    WEATHER = 1
    AVAILABLE_CAR_BAYS = 2
    COMMUNITY = 3

class Display:
    def __init__(self, type: DisplayType , message: [str, int], car_park: CarPark ):
        self.message = message
        self.type = type
        self.car_park = car_park

    def display(self):
        if self.type == self.type.WEATHER:
            return "displaying weather"
        elif self.type == self.type.AVAILABLE_CAR_BAYS:
            return "displaying available car bays"
        elif self.type == self.type.COMMUNITY:
            return "displaying community messages"



