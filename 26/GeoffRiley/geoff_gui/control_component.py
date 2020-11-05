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
from typing import List, Callable, Tuple

import pygame

from geoff_gui.base_component import BaseComponent
from geoff_gui.colours import ColourValue, Colours, verify_colour
from geoff_gui.graphical_component import GraphicalComponent
from geoff_gui.mouse_buttons import MouseButtons


class ControlComponent(GraphicalComponent):
    def __init__(self, rect: pygame.Rect,
                 display: pygame.Surface = None,
                 parent: BaseComponent = None,
                 **kwargs):
        super().__init__(rect, display, parent)
        self._disabled: bool = False
        self._disabled_count: int = 0
        self._children: List[GraphicalComponent] = list()

        self._margin: int = 4
        self.border: bool = True
        self._border_colour: ColourValue = verify_colour(Colours.BLACK)
        self._corner_radius: int = 0

        self._clicked: bool = False

        self.onClick: Callable[[BaseComponent, Tuple[int, int]], None] = kwargs.get('onClick', lambda *x: None)
        self.onMouseDown: Callable[[BaseComponent, Tuple[int, int], int], None] = kwargs.get('onMouseDown',
                                                                                             lambda *x: None)
        self.onMouseOver: Callable[[BaseComponent, Tuple[int, int], int, int], None] = kwargs.get('onMouseOver',
                                                                                                  lambda *x: None)
        self.onMouseUp: Callable[[BaseComponent, Tuple[int, int], int], None] = kwargs.get('onMouseUp', lambda *x: None)

    @property
    def disabled(self) -> bool:
        return self._disabled

    def disable(self) -> None:
        self._disabled_count += 1
        self._disabled = True

    def enable(self) -> None:
        self._disabled_count -= 1
        assert self._disabled_count >= 0
        if self._disabled_count == 0:
            self._disabled = False

    def draw(self) -> None:
        """
            Process draw requests

            :return: None
        """
        if self.visible:
            if self.border:
                pygame.draw.rect(self.display, self._border_colour,
                                 self.area.inflate(self._margin // 2, self._margin // 2),
                                 border_radius=self._corner_radius)
            if self.background_colour.a > 0:
                pygame.draw.rect(self.display, self.background_colour, self.area,
                                 border_radius=self._corner_radius)
            if self._text.strip() != '':
                self.display.blit(self._text_graphic[0], self._text_graphic[1])

        for c in self._children:
            c.draw()

    def message(self, message: List[pygame.event.Event]) -> None:
        """
            Process event message queue passed in message

            :param message: List of event messages
            :return: None
        """
        if not self.disabled:
            for event in message:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    if self.area.collidepoint(pos):
                        button_affected = event.button
                        if button_affected == MouseButtons.LEFT:
                            self.onClick(self, pos)
                            self._clicked = True
                        self.onMouseDown(self, pos, button_affected)
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = event.pos
                    if self.area.collidepoint(pos):
                        self.onMouseUp(self, pos, event.button)
                if event.type == pygame.MOUSEMOTION:
                    pos = event.pos
                    if self.area.collidepoint(pos):
                        self.onMouseOver(self, pos, event.rel, event.buttons)
            if not pygame.mouse.get_pressed(3)[0]:
                self._clicked = False

        for c in self._children:
            c.message(message)

    def add_component(self, new_component: GraphicalComponent) -> None:
        new_component.parent = self
        if new_component.display is None:
            new_component.display = self._display
        self._children.append(new_component)
