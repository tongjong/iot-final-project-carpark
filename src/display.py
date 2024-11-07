class Display:
    def __init__(self, display_id: int, message: str, is_on: bool, car_park):
        self.display_id = display_id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park


    def update(self, data: dict):
        for key, value in data.items():
            return f"{key}: {value}"





