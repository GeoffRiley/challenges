#!/bin/python3
"""
    GUI component: Label

    Descended from panel
"""
import pygame

from geoff_gui.alignment import Alignment
from geoff_gui.base_component import BaseComponent
from geoff_gui.colours import Colours, verify_colour
from geoff_gui.panel import Panel


class Label(Panel):
    def __init__(self, left: int, top: int,
                 display: pygame.Surface = None, parent: BaseComponent = None, **kwargs):
        width = 100
        height = 30
        text = kwargs.get('text', 'label')
        if 'text' in kwargs:
            kwargs.pop('text')
        self._anchor = {'h': left, 'v': top}
        super().__init__(left, top, width, height, display, parent, **kwargs)

        self.text = text
        self.border = False
        self.background_colour = verify_colour(Colours.TRANSPARENT)

    def _update_text_position(self):
        box: pygame.Rect
        img, box = self._text_graphic

        box.left = self.anchor['h'] - box.width // 2

        if self._text_align.h == Alignment.LEFT:
            box.left = self.anchor['h']
        elif self._text_align.h == Alignment.RIGHT:
            box.right = self.anchor['h']

        box.top = self.anchor['v'] - box.height // 2

        if self._text_align.v == Alignment.TOP:
            box.top = self.anchor['v']
        elif self._text_align.v == Alignment.BOTTOM:
            box.bottom = self.anchor['v']

        self._text_graphic = img, box

    @property
    def anchor(self):
        return self._anchor

    @anchor.setter
    def anchor(self, value):
        if isinstance(value, (tuple, list)) and len(value) == 2:
            self._anchor['h'] = value[0]
            self._anchor['v'] = value[1]
        elif isinstance(value, dict):
            self._anchor['h'] = value.get('h', self._anchor['h'])
            self._anchor['v'] = value.get('v', self._anchor['v'])
        else:
            raise ValueError('anchor must specify the horizontal (h) and vertical (v) co-ordinates')

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
