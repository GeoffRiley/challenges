#!/bin/python3
"""
    GUI component: BaseComponent
    Abstract Base Class

    A foundation for visual GUI elements to be build upon
"""

from abc import ABC, abstractmethod, abstractproperty
from typing import List

import pygame


class BaseComponent(ABC):
    def __init__(self, left: int, top: int, width: int, height: int,
                 display: pygame.Surface = None, parent: 'BaseComponent' = None):
        self.area = pygame.Rect(left, top, width, height)
        self.display = display
        self.parent = parent
        self.children = list()
        self._name = ''
        self._visible = True
        self._disabled = False

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
    def visible(self, value: bool):
        if isinstance(value, bool):
            self._visible = value
        else:
            raise TypeError(f'visible property requires a boolean value, received {type(value)} ({value})')

    @property
    def disabled(self):
        return self._disabled

    @disabled.setter
    def disabled(self, value):
        if isinstance(value, bool):
            self._disabled = value
        else:
            raise TypeError(f'disabled property requires a boolean value, received {type(value)} ({value})')

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError(f'name property requires a string value, received {type(value)} ({value})')

    def add_component(self, new_component: 'BaseComponent'):
        new_component.parent = self
        if new_component.display is None:
            new_component.display = self.display
        self.children.append(new_component)
