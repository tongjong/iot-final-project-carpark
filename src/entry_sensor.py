from sensor import Sensor

class EntrySensor(Sensor):
    def __str__(self):
        return f"Entry Sensor Active Status: {self.is_active}? 'Active' : 'Inactive'"

    def update_car_park(self, plate: str) -> None:
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")