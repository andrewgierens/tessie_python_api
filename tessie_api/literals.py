from typing import Literal
from enum import Enum


MapStyle = Literal["light", "dark"]
DistanceFormat = Literal["mi", "km"]
TemperatureFormat = Literal["c", "f"]
Format = Literal["json", "csv"]
Seat = Literal[
    "all",
    "front_left",
    "front_right",
    "rear_left",
    "rear_center",
    "rear_right",
    "third_row_left",
    "third_row_right",
]


class ClimateKeeperMode(Enum):
    DISABLE = 0
    DOG_MODE = 2
    CAMP_MODE = 3
