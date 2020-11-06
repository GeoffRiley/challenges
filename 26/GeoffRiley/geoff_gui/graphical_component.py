#!/bin/python3
"""
    GUI component: GraphicalComponent
    Abstract Base Class

    ## `GraphicalComponent`

    | Component     | `GraphicalComponent`  |
    | ------------- | --------------------- | -------
    | _Properties_  |                       |
    |               | `name` *              | `str`
    |               | `tag` *               | `ANY`
    |               | `area`                | `Rect`
    |               | `visible`             | `bool`
    | _Methods_     |                       |
    |               | `hide()`              |
    |               | `show()`              |

    * Inherited

    ### Inheritance

    `BaseComponent` -> `GraphicalComponent`

"""
from typing import List, Tuple, Any

import pygame

from geoff_gui.alignment import Alignment
from geoff_gui.base_component import BaseComponent
from geoff_gui.colours import ColourValue, verify_colour, Colours


class GraphicalComponent(BaseComponent):

    def __init__(self, rect: pygame.Rect,
                 display: pygame.Surface = None,
                 parent: BaseComponent = None,
                 **kwargs):
        super().__init__(parent)
        self._area: pygame.Rect = rect  # pygame.Rect(left, top, width, height)
        self._visible: bool = True
        self._display: pygame.Surface = display
        self._colour: ColourValue = verify_colour(Colours.BLACK)
        self._background_colour: ColourValue = verify_colour(Colours.SILVER)
        self._use_anchor: bool = False
        self._anchor = {'h': rect.left, 'v': rect.top}
        self._text: str = ''
        self._text_graphic: Tuple[Any, pygame.Rect] = None, rect
        self._text_margin: int = 4
        self._font_size = 14
        self._font_name = 'calibri,sans'
        self._font: pygame.freetype.Font = pygame.freetype.SysFont(self._font_name, self._font_size)
        self._font.origin = True
        self._text_align: Alignment = Alignment(Alignment.CENTER, Alignment.MIDDLE)

    @property
    def area(self) -> pygame.Rect:
        return self._area

    @property
    def visible(self) -> bool:
        return self._visible

    def hide(self) -> None:
        self._visible = False

    def show(self) -> None:
        self._visible = True

    @property
    def display(self):
        return self._display

    @display.setter
    def display(self, value):
        self._display = value

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str):
        self._text = value
        self._update_text_graphic()

    @property
    def text_margin(self) -> int:
        return self._text_margin

    @text_margin.setter
    def text_margin(self, value: int):
        assert isinstance(value, int)
        self._text_margin = value

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

    @property
    def use_anchor(self) -> bool:
        return self._use_anchor

    @use_anchor.setter
    def use_anchor(self, value: bool):
        assert isinstance(value, bool)
        self._use_anchor = value
        self._update_text_position()

    @property
    def anchor(self):
        return self._anchor

    @anchor.setter
    def anchor(self, value):
        if isinstance(value, (tuple, list)) and len(value) == 2:
            self._anchor['h'] = value[0]
            self._anchor['v'] = value[1]
            self._use_anchor = True
        elif isinstance(value, dict):
            self._anchor['h'] = value.get('h', self._anchor['h'])
            self._anchor['v'] = value.get('v', self._anchor['v'])
            self._use_anchor = True
        else:
            raise ValueError('anchor must specify the horizontal (h) and vertical (v) co-ordinates')
        self._update_text_position()

    def _update_text_graphic(self):
        self._text_graphic = self._font.render(self.text, self.colour, self.background_colour)
        self._update_text_position()

    def _update_text_position(self):
        box: pygame.Rect
        img, box = self._text_graphic

        try:
            if self.use_anchor:
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
            else:
                holder: pygame.Rect = self.area
                box.center = holder.center

                if self.text_align.h == Alignment.LEFT:
                    box.left = holder.left + self.text_margin
                elif self.text_align.h == Alignment.RIGHT:
                    box.right = holder.right - self.text_margin

                if self.text_align.v == Alignment.TOP:
                    box.top = holder.top + self.text_margin
                elif self.text_align.v == Alignment.BOTTOM:
                    box.bottom = holder.bottom - self.text_margin

        finally:
            self._text_graphic = img, box

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

    def draw(self) -> None:
        """
            Process draw requests

            :return: None
        """
        pass

    def message(self, message: List[pygame.event.Event]) -> None:
        """
            Process event message queue passed in message

            :param message: List of event messages
            :return: None
        """
        pass
