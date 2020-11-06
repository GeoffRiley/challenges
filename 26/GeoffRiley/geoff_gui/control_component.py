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

from typing import List, Callable, Tuple

import pygame

from geoff_gui.base_component import BaseComponent
from geoff_gui.colours import ColourValue, Colours, verify_colour
from geoff_gui.graphical_component import GraphicalComponent
from geoff_gui.mouse_buttons import MouseButtons

onMouseUpEvent = Callable[[BaseComponent, Tuple[int, int], int], None]

onMouseOverEvent = Callable[[BaseComponent, Tuple[int, int], int, int], None]

onMouseDownEvent = Callable[[BaseComponent, Tuple[int, int], int], None]

onClickEvent = Callable[[BaseComponent, Tuple[int, int]], None]


class ControlComponent(GraphicalComponent):

    def __init__(self, rect: pygame.Rect,
                 display: pygame.Surface = None,
                 parent: BaseComponent = None,
                 **kwargs):
        super().__init__(rect, display, parent)
        self._disabled: bool = False
        self._disabled_count: int = 0

        self._margin: int = 4
        self.border: bool = True
        self._border_colour: ColourValue = verify_colour(Colours.BLACK)
        self._corner_radius: int = 0

        self._clicked: bool = False

        self._onClick: onClickEvent = kwargs.get('onClick', lambda *x: None)
        self._onMouseDown: onMouseDownEvent = kwargs.get('onMouseDown', lambda *x: None)
        self._onMouseOver: onMouseOverEvent = kwargs.get('onMouseOver', lambda *x: None)
        self._onMouseUp: onMouseUpEvent = kwargs.get('onMouseUp', lambda *x: None)

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

    @property
    def onClick(self) -> onClickEvent:
        return self._onClick

    @onClick.setter
    def onClick(self, value: onClickEvent) -> None:
        self._onClick = value

    @property
    def onMouseDown(self) -> onMouseDownEvent:
        return self._onMouseDown

    @onMouseDown.setter
    def onMouseDown(self, value: onMouseDownEvent) -> None:
        self._onMouseDown = value

    @property
    def onMouseOver(self) -> onMouseOverEvent:
        return self._onMouseOver

    @onMouseOver.setter
    def onMouseOver(self, value: onMouseOverEvent) -> None:
        self._onMouseOver = value

    @property
    def onMouseUp(self) -> onMouseUpEvent:
        return self._onMouseUp

    @onMouseUp.setter
    def onMouseUp(self, value: onMouseUpEvent) -> None:
        self._onMouseUp = value

    @property
    def corner_radius(self) -> int:
        return self._corner_radius

    @corner_radius.setter
    def corner_radius(self, value: int) -> None:
        self._corner_radius = value

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
                self.display.blit(*self._text_graphic)

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
