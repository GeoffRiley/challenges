#!/bin/python3
"""
    GUI component: Button

    Descended from panel
"""
import pygame
from typing import Tuple, List

from base_component import BaseComponent
from panel import Panel
from colours import *


class Button(Panel):
    def __init__(self, left: int, top: int,
                 display: pygame.Surface = None, parent: BaseComponent = None, **kwargs):
        width = kwargs.get('width', 60)
        if 'width' in kwargs:
            kwargs.pop('width')
        height = kwargs.get('height', 30)
        if 'height' in kwargs:
            kwargs.pop('height')
        super().__init__(left, top, width, height, display, parent, **kwargs)
        self._colour_button = SILVER
        self._colour_hover = GREY
        self._colour_click = WHITE

    def draw(self):
        if self.visible:
            pos = pygame.mouse.get_pos()
            if self.area.collidepoint(pos):
                self.background_colour = self._colour_hover
            else:
                self.background_colour = self._colour_button
            super().draw()

    def message(self, message: List[pygame.event.Event]) -> None:
        if not self.disabled:
            ...
