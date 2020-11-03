#!/bin/python3
"""
    GUI component: Label

    Descended from panel
"""
import pygame

from geoff_gui.alignment import Alignment
from geoff_gui.base_component import BaseComponent
from geoff_gui.colours import Colours, verify_colour
from geoff_gui.graphical_component import GraphicalComponent


class Label(GraphicalComponent):
    def __init__(self, left: int, top: int,
                 display: pygame.Surface = None, parent: BaseComponent = None, **kwargs):
        width = 100
        height = 30
        text = kwargs.get('text', 'label')
        if 'text' in kwargs:
            kwargs.pop('text')
        super().__init__(pygame.Rect(left, top, width, height), display, parent, **kwargs)

        self.text = text
        self.background_colour = verify_colour(Colours.TRANSPARENT)

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str):
        self._text = value
        self._update_text_graphic()
        self.area.width = self._text_graphic[1].width
        self.area.height = self._text_graphic[1].height
        self._update_text_graphic()
