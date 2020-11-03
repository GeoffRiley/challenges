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
from typing import List, Any

import pygame


class BaseComponent(ABC):
    def __init__(self, parent: 'BaseComponent' = None):
        self._parent: 'BaseComponent' = parent
        self._tag: Any = None
        self._name: str = ''

    @abstractmethod
    def message(self, message: List[pygame.event.Event]) -> None:
        """
            Process event message queue passed in message

            :param message: List of event messages
            :return: None
        """
        pass

    @property
    def tag(self) -> Any:
        return self._tag

    @tag.setter
    def tag(self, value: Any) -> None:
        self._tag = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError(f'name property requires a string value, received {type(value)} ({value})')

