from sensor import Sensor

class EntrySensor(Sensor):
    def __str__(self):
        return f"Entry Sensor Active Status: {self.is_active}? 'Active' : 'Inactive'"