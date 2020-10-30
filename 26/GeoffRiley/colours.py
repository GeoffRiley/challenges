"""
    A list of colour constants as RGB tuples
"""
from typing import Union, Tuple, List

import pygame

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
SILVER = (192, 192, 192)

ColourValue = Union[
    pygame.Color, str, Tuple[int, int, int], List[int], int, Tuple[int, int, int, int]
]


def verify_colour(value: ColourValue) -> pygame.Color:
    """
    Accepts any of the allowed colour specifying formats and returns a pygame native Color object

    :param value: either pygame.Color, a string naming a standard colour, an RGB tuple,
        a list of integers (RGB or RGBA), a large integer (eg hexadecimal colour expression)
        or an RGBA tuple
    :return: pygame.Color representing the given colour
    """
    return pygame.Color(value)
