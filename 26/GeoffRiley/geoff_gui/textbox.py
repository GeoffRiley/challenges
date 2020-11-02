#!/bin/python3
"""
    GUI component: TextBox

    Descended from Panel
"""
from typing import Callable, List, Tuple

import pygame.freetype
from pygame import freetype

from geoff_gui.control_component import ControlComponent
from geoff_gui.base_component import BaseComponent
from geoff_gui.colours import Colours, ColourValue, verify_colour


class TextBox(ControlComponent):
    def __init__(self, left: int, top: int, width: int,
                 display: pygame.Surface = None, parent: BaseComponent = None, **kwargs):
        height = 48
        text = kwargs.get('text', '')
        if 'text' in kwargs:
            kwargs.pop('text')
        self._max_entry_len = kwargs.get('maxLength', 0)
        if 'maxLength' in kwargs:
            kwargs.pop('maxLength')
        self.onChange: Callable[[BaseComponent, Tuple[int, int]], None] = kwargs.get('onChange', lambda *x: None)
        if 'onChange' in kwargs:
            kwargs.pop('onChange')
        self._anchor = {'h': left, 'v': top}
        super().__init__(left, top, width, height, display, parent, **kwargs)

        self.background_colour: ColourValue = verify_colour(Colours.WHITE)
        self.colour: ColourValue = verify_colour(Colours.BLACK)
        self.cursor_color: ColourValue = verify_colour(Colours.RED)

        # Ready to receive keystrokes?
        self._started_text_input: bool = False
        self.active: bool = False
        self.cursor_text: str = text
        self.cursor_pos: int = 0
        self.ime_editing: bool = False
        self.editing_text: str = ''
        self.editing_pos: int = 0

    def draw(self) -> None:
        if self.visible:
            super().draw()
            paint_rect = self.area.copy()
            paint_rect.top = paint_rect.centery
            paint_rect.left += 25
            l = self._font.render_to(self.display, paint_rect, self.cursor_text[:self.cursor_pos], self.colour,
                                     self.background_colour)
            paint_rect.x += l.width
            if self.editing_text != '':
                m1 = self._font.render_to(self.display, paint_rect, self.editing_text[:self.editing_pos], self.colour,
                                          self.background_colour, freetype.STYLE_UNDERLINE)
                paint_rect.x += m1.width
                c = self._font.render_to(self.display, paint_rect, '|', self.cursor_color, self.background_colour)
                paint_rect.x += c.width
                m2 = self._font.render_to(self.display, paint_rect, self.editing_text[self.editing_pos:], self.colour,
                                          self.background_colour, freetype.STYLE_UNDERLINE)
                paint_rect.x += m2.width
            else:
                c = self._font.render_to(self.display, paint_rect, '|', self.cursor_color, self.background_colour)
                paint_rect.x += c.width
            r = self._font.render_to(self.display, paint_rect, self.cursor_text[self.cursor_pos:], self.colour,
                                     self.background_colour)

    def message(self, message: List[pygame.event.Event]) -> None:
        if not self.disabled:
            for event in message:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.active = self.area.collidepoint(event.pos)
                if self.active:
                    if not self._started_text_input:
                        # let the system know that we're dealing with text input
                        pygame.key.start_text_input()
                        self._started_text_input = True

                    if event.type == pygame.KEYDOWN:
                        if self.ime_editing:
                            if len(self.editing_text) == 0:
                                self.ime_editing = False
                            continue
                        key = event.key
                        if key == pygame.K_BACKSPACE:
                            if len(self.cursor_text) > 0 and self.cursor_pos > 0:
                                self.cursor_text = self.cursor_text[:self.cursor_pos - 1] + self.cursor_text[
                                                                                            self.cursor_pos:]
                                self.cursor_pos -= 1
                        elif key == pygame.K_DELETE:
                            self.cursor_text = self.cursor_text[:self.cursor_pos] + self.cursor_text[
                                                                                    self.cursor_pos + 1:]
                        elif key == pygame.K_HOME:
                            self.cursor_pos = 0
                        elif key == pygame.K_LEFT:
                            if self.cursor_pos > 0:
                                self.cursor_pos -= 1
                        elif key == pygame.K_RIGHT:
                            if self.cursor_pos < len(self.cursor_text):
                                self.cursor_pos += 1
                        elif key == pygame.K_END:
                            self.cursor_pos = len(self.cursor_text)
                        elif key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                            pygame.key.stop_text_input()
                            self._started_text_input = False
                    elif event.type == pygame.TEXTINPUT:
                        self.ime_editing = False
                        self.editing_text = ''
                        self.cursor_text = self.cursor_text[:self.cursor_pos] + event.text + self.cursor_text[
                                                                                             self.cursor_pos:]
                        self.cursor_pos += len(event.text)
                    elif event.type == pygame.TEXTEDITING:
                        self.ime_editing = True
                        self.editing_text = event.text
                        self.editing_pos = event.start
                else:
                    if self._started_text_input:
                        # let the system know that we've stopped dealing with text input
                        pygame.key.stop_text_input()
                        self._started_text_input = False

        super().message(message)
