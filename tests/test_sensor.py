import unittest
from tkinter import Entry

from exit_sensor import ExitSensor
from entry_sensor import EntrySensor
from car_park import  CarPark

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("Moondalup", 100)
        self.exit_sensor = ExitSensor(1, self.car_park, True)
        self.entry_sensor = EntrySensor(1, self.car_park, True)

    def test_sensor_initialised_with_all_attributes(self):
        self.assertIsInstance(self.exit_sensor, ExitSensor)
        self.assertEqual(self.exit_sensor.is_active, True)
        self.assertIsInstance(self.entry_sensor, EntrySensor)
        self.assertEqual(self.entry_sensor.is_active, True)

    def test_detect_vehicle_with_entry_sensor(self):
        self.entry_sensor.detect_vehicle()
        self.assertEqual(len(self.car_park.car_plates), 1)
        self.assertEqual(self.car_park.car_plates[0][:5], "Fake-")

    def test_detect_vehicle_with_exit_sensor(self):
        self.entry_sensor.detect_vehicle()
        self.assertEqual(len(self.car_park.car_plates), 1)

        self.exit_sensor.detect_vehicle()
        self.assertEqual(len(self.car_park.car_plates), 0)



if __name__ == '__main__':
    unittest.main()