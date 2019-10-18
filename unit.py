from enum import Enum

from .base_enum import BaseEnum

@unique
class Unit(BaseEnum):
    CELCIUS = auto()
    FAHRENHEIT = auto()
