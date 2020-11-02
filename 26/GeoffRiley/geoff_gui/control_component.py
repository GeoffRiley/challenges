#!/bin/python3
"""
    GUI component: ControlComponent
    Abstract Base Class

    ## `ControlComponent`

    | Component     | `ControlComponent`    |
    | ------------- | --------------------- |--------
    | _Properties_  |                       |
    |               | `name` *              | `str`
    |               | `tag` *               | `ANY`
    |               | `area` *              | `Rect`
    |               | `visible` *           | `bool`
    |               | `disabled`            | `bool`
    | _Methods_     |                       |
    |               | `hide()` *            |
    |               | `show()` *            |
    |               | `disable()`           |
    |               | `enable()`            |

    * Inherited

    ### Inheritance

    `BaseComponent` -> `GraphicalComponent` -> `ControlComponent`
"""

from abc import ABC, abstractmethod
from typing import List

import pygame

from geoff_gui.graphical_component import GraphicalComponent


class ControlComponent(GraphicalComponent):
    ...
