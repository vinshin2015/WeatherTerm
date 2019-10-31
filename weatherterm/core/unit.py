from enum import unique, auto

from weatherterm.core.base_enum import BaseEnum

@unique
class Unit(BaseEnum):
    CELCIUS = auto()
    FAHRENHEIT = auto()
