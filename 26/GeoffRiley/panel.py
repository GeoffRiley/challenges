#!/bin/python3
"""
    GUI component: panel
"""
from dataclasses import dataclass
from typing import Tuple
from colours import *


@dataclass
class Panel:
    left: int
    top: int
    width: int
    height: int
    visible: bool = True
    border: bool = True
    background_colour: Tuple[int,int,int] = SILVER
    border_colour: Tuple[int, int, int] = BLACK
