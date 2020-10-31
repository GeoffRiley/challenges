#!/bin/python3
"""
    GUI support class: Alignment

    Convenient definition of alignment values various elements
"""
from typing import Tuple, Union


class Alignment:
    LEFT = 0
    CENTER = 1
    RIGHT = 2
    TOP = 3
    MIDDLE = 4
    BOTTOM = 5

    def __init__(self, horiz: Union['Alignment', None] = None,
                 vert: Union['Alignment', None] = None):
        self._horizontal = horiz or self.LEFT
        self._vertical = vert or self.TOP

    def __repr__(self):
        return self.hv

    @property
    def horizontal(self):
        return self._horizontal

    @horizontal.setter
    def horizontal(self, value):
        if self.is_horizontal(value):
            self._horizontal = value

    @property
    def h(self):
        return self._horizontal

    @property
    def vertical(self):
        return self._vertical

    @vertical.setter
    def vertical(self, value):
        if self.is_vertical(value):
            self._vertical = value

    @property
    def v(self):
        return self._vertical

    @property
    def hv(self) -> Tuple['Alignment', 'Alignment']:
        return self.h, self.v

    @hv.setter
    def hv(self, value: Tuple['Alignment', 'Alignment']) -> None:
        for v in value:
            if self.is_horizontal(v):
                self._horizontal = v
            if self.is_vertical(v):
                self._vertical = v

    @classmethod
    def is_horizontal(cls, align: 'Alignment') -> bool:
        return align in [cls.LEFT, cls.CENTER, cls.RIGHT]

    @classmethod
    def is_vertical(cls, align: 'Alignment') -> bool:
        return align in [cls.TOP, cls.MIDDLE, cls.BOTTOM]
