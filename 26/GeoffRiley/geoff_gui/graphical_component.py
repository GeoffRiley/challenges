#!/bin/python3
"""
    GUI component: GraphicalComponent
    Abstract Base Class

    ## `GraphicalComponent`

    | Component     | `GraphicalComponent`  |
    | ------------- | --------------------- | -------
    | _Properties_  |                       |
    |               | `name` *              | `str`
    |               | `tag` *               | `ANY`
    |               | `area`                | `Rect`
    |               | `visible`             | `bool`
    | _Methods_     |                       |
    |               | `hide()`              |
    |               | `show()`              |

    * Inherited

    ### Inheritance

    `BaseComponent` -> `GraphicalComponent`

"""

from abc import ABC, abstractmethod
from typing import List

import pygame

from geoff_gui.base_component import BaseComponent


class GraphicalComponent(BaseComponent):
    ...
