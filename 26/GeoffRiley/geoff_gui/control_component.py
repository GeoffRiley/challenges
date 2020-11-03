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

from geoff_gui.base_component import BaseComponent
from geoff_gui.graphical_component import GraphicalComponent


class ControlComponent(GraphicalComponent):
    def __init__(self, rect: pygame.Rect,
                 display: pygame.Surface = None, parent: BaseComponent = None):
        super().__init__(rect, display, parent)
        self._disabled: bool = False
        self._children: List[GraphicalComponent] = list()

    @property
    def disabled(self) -> bool:
        return self._disabled

    @disabled.setter
    def disabled(self, value: bool) -> None:
        if isinstance(value, bool):
            self._disabled = value
        else:
            raise TypeError(f'disabled property requires a boolean value, received {type(value)} ({value})')

    def draw(self) -> None:
        """
            Process draw requests

            :return: None
        """
        for c in self._children:
            c.draw()

    def message(self, message: List[pygame.event.Event]) -> None:
        """
            Process event message queue passed in message

            :param message: List of event messages
            :return: None
        """
        for c in self._children:
            c.message(message)

    def add_component(self, new_component: GraphicalComponent) -> None:
        new_component.parent = self
        if new_component.display is None:
            new_component.display = self._display
        self._children.append(new_component)
