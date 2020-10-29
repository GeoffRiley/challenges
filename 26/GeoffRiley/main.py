#!/bin/python3
"""
    pygame gui implementation
    possibly with a calculator and a pelmanism game
"""
import pygame
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
