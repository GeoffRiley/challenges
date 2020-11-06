#!/bin/python3
"""
    GUI component: TextBox

    Descended from Panel
"""
from typing import Callable, List

import pygame.freetype
from pygame import freetype

from geoff_gui.base_component import BaseComponent
from geoff_gui.colours import Colours, ColourValue, verify_colour
from geoff_gui.control_component import ControlComponent

onChangeEvent = Callable[[BaseComponent, str, str], None]


class TextBox(ControlComponent):

    def __init__(self, left: int, top: int, width: int,
                 display: pygame.Surface = None, parent: BaseComponent = None, **kwargs):
        height = 48
        text = kwargs.get('text', '')
        rect = pygame.Rect(left, top, width, height)
        if 'text' in kwargs:
            kwargs.pop('text')
        self._max_entry_len = kwargs.get('maxLength', 0)
        if 'maxLength' in kwargs:
            kwargs.pop('maxLength')
        self._onChange: onChangeEvent = kwargs.get('onChange', lambda *x: None)
        if 'onChange' in kwargs:
            kwargs.pop('onChange')
        self._anchor = {'h': left, 'v': top}
        super().__init__(rect, display, parent)

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
            left_part = self._font.render_to(self.display,
                                             paint_rect,
                                             self.cursor_text[:self.cursor_pos],
                                             self.colour,
                                             self.background_colour)
            paint_rect.x += left_part.width
            if self.editing_text != '':
                mid_part1 = self._font.render_to(self.display,
                                                 paint_rect,
                                                 self.editing_text[:self.editing_pos],
                                                 self.colour,
                                                 self.background_colour,
                                                 freetype.STYLE_UNDERLINE)
                paint_rect.x += mid_part1.width
                cursor_part = self._font.render_to(self.display,
                                                   paint_rect,
                                                   '|', self.cursor_color,
                                                   self.background_colour)
                paint_rect.x += cursor_part.width
                mid_part2 = self._font.render_to(self.display,
                                                 paint_rect,
                                                 self.editing_text[self.editing_pos:],
                                                 self.colour,
                                                 self.background_colour,
                                                 freetype.STYLE_UNDERLINE)
                paint_rect.x += mid_part2.width
            else:
                cursor_part = self._font.render_to(self.display,
                                                   paint_rect,
                                                   '|',
                                                   self.cursor_color,
                                                   self.background_colour,
                                                   freetype.STYLE_STRONG)
                paint_rect.x += cursor_part.width + 4
            right_part = self._font.render_to(self.display,
                                              paint_rect,
                                              self.cursor_text[self.cursor_pos:],
                                              self.colour,
                                              self.background_colour)
            paint_rect.x += right_part.width

    def message(self, message: List[pygame.event.Event]) -> None:
        if not self.disabled:
            before_event = self.cursor_text
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
                                self.cursor_text = (self.cursor_text[:self.cursor_pos - 1] +
                                                    self.cursor_text[self.cursor_pos:])
                                self.cursor_pos -= 1
                        elif key == pygame.K_DELETE:
                            self.cursor_text = (self.cursor_text[:self.cursor_pos] +
                                                self.cursor_text[self.cursor_pos + 1:])
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
                        self.cursor_text = (self.cursor_text[:self.cursor_pos] +
                                            event.text +
                                            self.cursor_text[self.cursor_pos:])
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
            if before_event != self.cursor_text:
                self.onChange(self, before_event, self.cursor_text)

        super().message(message)

    @property
    def onChange(self) -> onChangeEvent:
        return self._onChange

    @onChange.setter
    def onChange(self, value: onChangeEvent) -> None:
        self._onChange = value
