# Contains enums and constants used across the application.

from enum import Enum

class SplitType(Enum):
    EQUAL = "EQUAL"
    PERCENT = "PERCENT"
    EXACT = "EXACT"