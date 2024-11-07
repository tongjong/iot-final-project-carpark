from display import Display


class AvailableCarBayDisplay(Display):
    def __init__(self, message: str):
        super().__init__(message)

    def display(self):
        return "displaying available car bays"