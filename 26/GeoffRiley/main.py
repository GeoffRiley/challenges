#!/bin/python3
"""
    pygame gui implementation
    possibly with a calculator and a pelmanism game
"""
import pygame

from alignment import Alignment
from button import Button
from colours import *
from panel import Panel

# pygame generic parameters
WIDTH, HEIGHT = 800, 600
FPS = 50


class GeoffGui:
    # The gui_root will have all other elements attached to it
    gui_root: Panel

    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Gooey ooey ooey')
        self.gui_root = Panel(0, 0, WIDTH, HEIGHT, self.display)

        for x in range(3):
            for y in range(3):
                b = Button(x * 175 + 25, y * 50 + 25, width=150, height=40)
                b.text = f'Button ({x},{y})'
                b.vertical_alignment = [Alignment.TOP, Alignment.MIDDLE, Alignment.BOTTOM][y]
                b.horizontal_alignment = [Alignment.LEFT, Alignment.CENTER, Alignment.RIGHT][x]
                self.gui_root.add_component(b)

    def draw(self):
        self.gui_root.draw()
        pygame.display.update()

    def run(self):
        """
        This is the main run loop: it keeps the system running
        """
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(FPS)
            self.draw()
            messages = pygame.event.get()
            for event in messages:
                if event.type == pygame.QUIT:
                    running = False
                    continue
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
            self.gui_root.message(messages)

        pygame.quit()


if __name__ == '__main__':
    main = GeoffGui()
    main.run()
