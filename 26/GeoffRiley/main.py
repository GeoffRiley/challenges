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
        pygame.display.set_caption('Living with tomatoes')
        self.gui_root = Panel(0, 0, WIDTH, HEIGHT, True, False, BLUE, BLACK)

    def draw(self):
        pass

    def run(self):
        """
        This is the main run loop: it keeps the system running
        """
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(FPS)
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    continue
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

        pygame.quit()


if __name__ == '__main__':
    main = GeoffGui()
    main.run()
