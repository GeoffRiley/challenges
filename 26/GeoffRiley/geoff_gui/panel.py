#!/bin/python3
"""
    GUI component: Panel

    Descended from BaseComponent
"""
from typing import List

import pygame.freetype

from geoff_gui.base_component import BaseComponent
from geoff_gui.colours import ColourValue, verify_colour
from geoff_gui.container_component import ContainerComponent


class Panel(ContainerComponent):

    def __init__(self, rect: pygame.Rect,
                 display: pygame.Surface = None,
                 parent: BaseComponent = None, **kwargs):
        super().__init__(rect, display, parent, **kwargs)

        self._update_text_graphic()

    def draw(self) -> None:
        super().draw()

    def message(self, message: List[pygame.event.Event]) -> None:
        super().message(message)

    @property
    def margin(self) -> int:
        return self._margin

    @margin.setter
    def margin(self, value: int):
        if isinstance(value, int):
            self._margin = value

    @property
    def border_colour(self) -> ColourValue:
        return self._border_colour

    @border_colour.setter
    def border_colour(self, value: ColourValue):
        self._border_colour = verify_colour(value)

    @property
    def corner_radius(self) -> int:
        return self._corner_radius

    @corner_radius.setter
    def corner_radius(self, value: int) -> None:
        self._corner_radius = value

    @property
    def clicked(self) -> bool:
        return self._clicked

    @property
    def name(self) -> str:
        return self._text if len(self._name) == 0 else self._name
