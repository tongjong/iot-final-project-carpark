from enum import Enum
from abc import ABC, abstractmethod
from typing import Union

class DisplayType(Enum):
    WEATHER = 1
    AVAILABLE_CAR_BAYS = 2
    COMMUNITY = 3

class Display(ABC):
    def __init__(self, message: Union[str,int]):
        self.message = message

    @abstractmethod
    def display(self):
        pass



