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
    |               | `disabled` *          | `bool`
    |
    | _Methods_     |                       |
    |               | `hide()` *            |
    |               | `show()` *            |
    |               | `disable()` *         |
    |               | `enable()` *          |
    |

    * Inherited

    ### Inheritance

    `BaseComponent` -> `GraphicalComponent` -> `ControlComponent` -> `ContainerComponent`
"""
from abc import abstractmethod
from typing import List, Callable, Tuple

import pygame

from geoff_gui.base_component import BaseComponent
from geoff_gui.colours import ColourValue, verify_colour, Colours
from geoff_gui.control_component import ControlComponent
from geoff_gui.mouse_buttons import MouseButtons


class ContainerComponent(ControlComponent):
    def __init__(self, rect: pygame.Rect,
                 display: pygame.Surface = None,
                 parent: BaseComponent = None,
                 **kwargs):
        super().__init__(rect, display, parent, **kwargs)

    def draw(self) -> None:
        """
            Process draw requests

            :return: None
        """
        super().draw()

    def message(self, message: List[pygame.event.Event]) -> None:
        """
            Process event message queue passed in message

            :param message: List of event messages
            :return: None
        """
        super().message(message)
