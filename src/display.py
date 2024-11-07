from enum import Enum
from abc import ABC, abstractmethod

class DisplayType(Enum):
    WEATHER = 1
    AVAILABLE_CAR_BAYS = 2
    COMMUNITY = 3

class Display(ABC):
    def __init__(self, message: [str,int]):
        self.message = message

    @abstractmethod
    def display(self):
        pass



