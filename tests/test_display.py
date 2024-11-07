import unittest
from display import Display
from car_park import CarPark

class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("Moondalup", 100)
        self.display = Display(1, "Welcome to the car park", True, self.car_park)

    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.display_id, 1)
        self.assertEqual(self.display.message, "Welcome to the car park")
        self.assertEqual(self.display.is_on, True)
        self.assertIsInstance(self.display.car_park, CarPark)

    def test_update(self):
        message = self.display.update({"message": "Goodbye"})
        self.assertEqual(message, "Goodbye")

if __name__ == '__main__':
    unittest.main()