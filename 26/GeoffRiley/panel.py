#!/bin/python3
"""
    GUI component: Panel

    Descended from BaseComponent
"""
from typing import Tuple, List

import pygame
import pygame.freetype

from alignment import Alignment
from base_component import BaseComponent
from colours import *
from mouse_buttons import MouseButtons


class Panel(BaseComponent):

    def __init__(self, left: int, top: int, width: int, height: int,
                 display: pygame.Surface = None, parent: BaseComponent = None, **kwargs):
        super().__init__(left, top, width, height, display, parent)
        self._text: str = ''
        self._font = pygame.freetype.SysFont('sans', 12)
        self._vertical_alignment: Alignment = Alignment.MIDDLE
        self._horizontal_alignment: Alignment = Alignment.CENTER
        self.margin: int = 4
        self._colour: Tuple[int, int, int] = BLACK
        self._background_colour: Tuple[int, int, int] = SILVER
        self.border: bool = True
        self._border_colour: Tuple[int, int, int] = BLACK

        self._update_text_graphic()

        self.onClick = kwargs.get('onClick', lambda *x: None)
        self.onMouseDown = kwargs.get('onMouseDown', lambda *x: None)
        self.onMouseOver = kwargs.get('onMouseOver', lambda *x: None)
        self.onMouseUp = kwargs.get('onMouseUp', lambda *x: None)

    def draw(self):
        if self.visible:
            if self.border:
                pygame.draw.rect(self.display, self.border_colour, self.area.inflate(2, 2))
            pygame.draw.rect(self.display, self.background_colour, self.area)
            if self._text.strip() != '':
                self.display.blit(self._text_graphic[0], self._text_graphic[1])
            for c in self.children:
                c.draw()

    def message(self, message: List[pygame.event.Event]) -> None:
        if not self.disabled:
            for event in message:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    button_affected = event.button
                    if button_affected == MouseButtons.LEFT:
                        self.onClick(pos)
                    else:
                        self.onMouseDown(pos, button_affected)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.onMouseUp(event.pos, event.button)
                if event.type == pygame.MOUSEMOTION:
                    self.onMouseOver(event.pos, event.buttons)
            for c in self.children:
                c.message(message)

    def _update_text_graphic(self):
        self._text_graphic = self._font.render(self.text, self.colour, self.background_colour)
        self._update_text_position()

    def _update_text_position(self):
        img, box = self._text_graphic
        box.center = self.area.center

        if self._horizontal_alignment == Alignment.LEFT:
            box.left = self.area.left + self.margin
        elif self._horizontal_alignment == Alignment.RIGHT:
            box.right = self.area.right - self.margin

        if self._vertical_alignment == Alignment.TOP:
            box.top = self.area.top + self.margin
        elif self._vertical_alignment == Alignment.BOTTOM:
            box.bottom = self.area.bottom - self.margin

        self._text_graphic = img, box

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str):
        self._text = value
        self._update_text_graphic()

    @property
    def vertical_alignment(self):
        return self._vertical_alignment

    @vertical_alignment.setter
    def vertical_alignment(self, value: Alignment):
        if Alignment.is_vertical(value):
            self._vertical_alignment = value
            self._update_text_position()

    @property
    def horizontal_alignment(self):
        return self._horizontal_alignment

    @horizontal_alignment.setter
    def horizontal_alignment(self, value: Alignment):
        if Alignment.is_horizontal(value):
            self._horizontal_alignment = value
            self._update_text_position()

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, value):
        self._colour = verify_colour(value)

    @property
    def background_colour(self):
        return self._background_colour

    @background_colour.setter
    def background_colour(self, value):
        self._background_colour = verify_colour(value)
        self._update_text_graphic()

    @property
    def border_colour(self):
        return self._border_colour

    @border_colour.setter
    def border_colour(self, value):
        self._border_colour = verify_colour(value)
