#!/bin/python3
"""
    GUI support class: Alignment

    Convenient definition of alignment values various elements
"""
from enum import Enum


class Alignment(Enum):
    LEFT = 0
    CENTER = 1
    RIGHT = 2
    TOP = 3
    MIDDLE = 4
    BOTTOM = 5

    @classmethod
    def is_horizontal(cls, align: 'Alignment') -> bool:
        return align in [cls.LEFT, cls.CENTER, cls.RIGHT]

    @classmethod
    def is_vertical(cls, align: 'Alignment') -> bool:
        return align in [cls.TOP, cls.MIDDLE, cls.BOTTOM]
