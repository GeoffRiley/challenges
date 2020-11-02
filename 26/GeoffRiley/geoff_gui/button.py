#!/bin/python3
"""
    GUI component: Button

    Descended from panel
"""
from typing import List

import pygame

from geoff_gui.control_component import ControlComponent
from geoff_gui.base_component import BaseComponent
from geoff_gui.colours import Colours, ColourValue, verify_colour


class Button(ControlComponent):
    def __init__(self, left: int, top: int,
                 display: pygame.Surface = None, parent: BaseComponent = None, **kwargs):
        width: int = kwargs.get('width', 60)
        if 'width' in kwargs:
            kwargs.pop('width')
        height: int = kwargs.get('height', 30)
        if 'height' in kwargs:
            kwargs.pop('height')
        super().__init__(left, top, width, height, display, parent, **kwargs)
        self.corner_radius = 4
        self._button_colour: ColourValue = verify_colour(Colours.SILVER)
        self._hover_colour: ColourValue = verify_colour(Colours.GREY)
        self._click_colour: ColourValue = verify_colour(Colours.WHITE)

    def draw(self) -> None:
        if self.visible:
            pos = pygame.mouse.get_pos()
            if self.area.collidepoint(pos):
                self.background_colour = self._click_colour if self._clicked else self._hover_colour
            else:
                self.background_colour = self._button_colour
            super().draw()

    def message(self, message: List[pygame.event.Event]) -> None:
        if not self.disabled:
            super().message(message)

    @property
    def button_colour(self) -> ColourValue:
        return self._button_colour

    @button_colour.setter
    def button_colour(self, value: ColourValue) -> None:
        self._button_colour = verify_colour(value)

    @property
    def hover_colour(self) -> ColourValue:
        return self._hover_colour

    @hover_colour.setter
    def hover_colour(self, value: ColourValue) -> None:
        self._hover_colour = verify_colour(value)

    @property
    def click_colour(self) -> ColourValue:
        return self._click_colour

    @click_colour.setter
    def click_colour(self, value: ColourValue) -> None:
        self._click_colour = verify_colour(value)
