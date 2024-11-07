from car_park import CarPark


class Sensor:
    def __init__(self, car_park: CarPark, is_active: bool=False):
        self.car_park = car_park
        self.is_active = is_active
