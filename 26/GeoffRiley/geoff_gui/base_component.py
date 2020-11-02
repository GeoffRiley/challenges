#!/bin/python3
"""
    GUI component: BaseComponent
    Abstract Base Class

    A foundation for visual GUI elements to be built upon

    ## `BaseComponent`

    | Component     | `BaseComponent`   |
    | ------------- | ----------------- | ------
    | _Properties_  |                   |
    |               | `name`            | `str`
    |               | `tag`             | `ANY`

    ### Inheritance

    `Object` -> `BaseComponent`
"""

from abc import ABC, abstractmethod
from typing import List

import pygame


class BaseComponent(ABC):
    def __init__(self, left: int, top: int, width: int, height: int,
                 display: pygame.Surface = None, parent: 'BaseComponent' = None):
        self.area: pygame.Rect = pygame.Rect(left, top, width, height)
        self.display: pygame.Surface = display
        self.parent: 'BaseComponent' = parent
        self.children: List['BaseComponent'] = list()
        self._tag: int = 0
        self._name: str = ''
        self._visible: bool = True
        self._disabled: bool = False

    @abstractmethod
    def draw(self) -> None:
        """
            Process draw requests

            :return: None
        """
        pass

    @abstractmethod
    def message(self, message: List[pygame.event.Event]) -> None:
        """
            Process event message queue passed in message

            :param message: List of event messages
            :return: None
        """
        pass

    @property
    def visible(self) -> bool:
        return self._visible

    @visible.setter
    def visible(self, value: bool) -> None:
        if isinstance(value, bool):
            self._visible = value
        else:
            raise TypeError(f'visible property requires a boolean value, received {type(value)} ({value})')

    @property
    def disabled(self) -> bool:
        return self._disabled

    @disabled.setter
    def disabled(self, value: bool) -> None:
        if isinstance(value, bool):
            self._disabled = value
        else:
            raise TypeError(f'disabled property requires a boolean value, received {type(value)} ({value})')

    @property
    def tag(self) -> int:
        return self._tag

    @tag.setter
    def tag(self, value: int) -> None:
        if isinstance(value, int):
            self._tag = value
        else:
            raise TypeError(f'tag property requires a integer value, received {type(value)} ({value})')

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError(f'name property requires a string value, received {type(value)} ({value})')

    def add_component(self, new_component: 'BaseComponent') -> None:
        new_component.parent = self
        if new_component.display is None:
            new_component.display = self.display
        self.children.append(new_component)
