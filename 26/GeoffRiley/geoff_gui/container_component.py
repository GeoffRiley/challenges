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
from typing import List

import pygame

from geoff_gui.base_component import BaseComponent
from geoff_gui.control_component import ControlComponent
from geoff_gui.graphical_component import GraphicalComponent


class ContainerComponent(ControlComponent):

    def __init__(self, rect: pygame.Rect,
                 display: pygame.Surface = None,
                 parent: BaseComponent = None,
                 **kwargs):
        super().__init__(rect, display, parent, **kwargs)
        self._children: List[GraphicalComponent] = list()

    def draw(self) -> None:
        """
            Process draw requests

            :return: None
        """
        super().draw()

        for c in self._children:
            c.draw()

    def message(self, message: List[pygame.event.Event]) -> None:
        """
            Process event message queue passed in message

            :param message: List of event messages
            :return: None
        """
        super().message(message)

        for c in self._children:
            c.message(message)

    def add_component(self, new_component: GraphicalComponent) -> None:
        new_component.parent = self
        if new_component.display is None:
            new_component.display = self._display
        self._children.append(new_component)
