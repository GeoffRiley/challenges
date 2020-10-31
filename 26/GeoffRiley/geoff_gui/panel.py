#!/bin/python3
"""
    GUI component: Panel

    Descended from BaseComponent
"""
from typing import Callable, List, Tuple

import pygame.freetype

from geoff_gui.alignment import Alignment
from geoff_gui.base_component import BaseComponent
from geoff_gui.colours import Colours, ColourValue, verify_colour
from geoff_gui.mouse_buttons import MouseButtons


class Panel(BaseComponent):

    def __init__(self, left: int, top: int, width: int, height: int,
                 display: pygame.Surface = None, parent: BaseComponent = None, **kwargs):
        super().__init__(left, top, width, height, display, parent)
        self._text: str = ''
        self._font_size = 12
        self._font_name = 'calibri,sans'
        self._font: pygame.freetype.Font = pygame.freetype.SysFont(self._font_name, self._font_size)
        self._text_align: Alignment = Alignment(Alignment.CENTER, Alignment.MIDDLE)
        self._margin: int = 4
        self._colour: ColourValue = verify_colour(Colours.BLACK)
        self._background_colour: ColourValue = verify_colour(Colours.SILVER)
        self.border: bool = True
        self._border_colour: ColourValue = verify_colour(Colours.BLACK)
        self._corner_radius: int = 0

        self._update_text_graphic()

        self._clicked: bool = False

        self.onClick: Callable[[BaseComponent, Tuple[int, int]], None] = kwargs.get('onClick', lambda *x: None)
        self.onMouseDown: Callable[[BaseComponent, Tuple[int, int], int], None] = kwargs.get('onMouseDown',
                                                                                             lambda *x: None)
        self.onMouseOver: Callable[[BaseComponent, Tuple[int, int], int, int], None] = kwargs.get('onMouseOver',
                                                                                                  lambda *x: None)
        self.onMouseUp: Callable[[BaseComponent, Tuple[int, int], int], None] = kwargs.get('onMouseUp', lambda *x: None)

    def draw(self) -> None:
        if self.visible:
            if self.border:
                pygame.draw.rect(self.display, self.border_colour,
                                 self.area.inflate(self._margin // 2, self._margin // 2),
                                 border_radius=self._corner_radius)
            if self.background_colour.a > 0:
                pygame.draw.rect(self.display, self.background_colour, self.area,
                                 border_radius=self._corner_radius)
            if self._text.strip() != '':
                self.display.blit(self._text_graphic[0], self._text_graphic[1])
            for c in self.children:
                c.draw()

    def message(self, message: List[pygame.event.Event]) -> None:
        if not self.disabled:
            for c in self.children:
                c.message(message)
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

    def _update_text_graphic(self):
        self._text_graphic = self._font.render(self.text, self.colour, self.background_colour)
        self._update_text_position()

    def _update_text_position(self):
        img, box = self._text_graphic
        box.center = self.area.center

        if self._text_align.h == Alignment.LEFT:
            box.left = self.area.left + self._margin
        elif self._text_align.h == Alignment.RIGHT:
            box.right = self.area.right - self._margin

        if self._text_align.v == Alignment.TOP:
            box.top = self.area.top + self._margin
        elif self._text_align.v == Alignment.BOTTOM:
            box.bottom = self.area.bottom - self._margin

        self._text_graphic = img, box

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str):
        self._text = value
        self._update_text_graphic()

    @property
    def margin(self) -> int:
        return self._margin

    @margin.setter
    def margin(self, value: int):
        if isinstance(value, int):
            self._margin = value

    @property
    def text_align(self):
        return self._text_align

    @text_align.setter
    def text_align(self, value):
        if isinstance(value, tuple):
            self._text_align.hv = value
            self._update_text_position()

    @property
    def vertical_alignment(self) -> Alignment:
        return self._text_align.v

    @vertical_alignment.setter
    def vertical_alignment(self, value: Alignment):
        if Alignment.is_vertical(value):
            self._text_align.vertical = value
            self._update_text_position()

    @property
    def horizontal_alignment(self) -> Alignment:
        return self._text_align.h

    @horizontal_alignment.setter
    def horizontal_alignment(self, value: Alignment):
        if Alignment.is_horizontal(value):
            self._text_align.horizontal = value
            self._update_text_position()

    @property
    def colour(self) -> ColourValue:
        return self._colour

    @colour.setter
    def colour(self, value: ColourValue):
        self._colour = verify_colour(value)

    @property
    def background_colour(self) -> ColourValue:
        return self._background_colour

    @background_colour.setter
    def background_colour(self, value: ColourValue):
        self._background_colour = verify_colour(value)
        self._update_text_graphic()

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

    @property
    def font_size(self):
        return self._font_size

    @font_size.setter
    def font_size(self, value):
        self._font_size = value
        self._font: pygame.freetype.Font = pygame.freetype.SysFont(self._font_name, self._font_size)
        self._update_text_graphic()

    @property
    def font_name(self):
        return self._font_name

    @font_name.setter
    def font_name(self, value):
        self._font_name = value
        self._font: pygame.freetype.Font = pygame.freetype.SysFont(self._font_name, self._font_size)
        self._update_text_graphic()
