from sensor import Sensor

class ExitSensor(Sensor):
    def __str__(self):
        return f"Exir Sensor Active Status: {self.is_active}? 'Active' : 'Inactive'"