#!/bin/python3
"""
    GUI component: panel
"""
import pygame
from dataclasses import dataclass
from typing import Tuple, List

from base_component import BaseComponent
from colours import *


class Panel(BaseComponent):

    def __init__(self, left: int, top: int, width: int, height: int,
                 display: pygame.Surface, parent: BaseComponent = None):
        super().__init__(left, top, width, height, display, parent)
        self.border: bool = True
        self.colour: Tuple[int, int, int] = SILVER
        self.border_colour: Tuple[int, int, int] = BLACK

    def draw(self):
        if self.border:
            pygame.draw.rect(self.display, self.border_colour, self.area.inflate(2, 2))
        pygame.draw.rect(self.display, self.colour, self.area)

    def message(self, message: List[pygame.event.Event]) -> None:
        for event in message:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(f'Clicked {pos}')
