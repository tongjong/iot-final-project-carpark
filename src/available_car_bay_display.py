from display import Display


class AvailableCarBayDisplay(Display):
    def __init__(self, message: int):
        super().__init__(message)

    def display(self):
        return f"displaying available car bays + {self.message}"