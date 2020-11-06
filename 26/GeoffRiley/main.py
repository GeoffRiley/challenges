#!/bin/python3
"""
    pygame gui implementation
    possibly with a calculator and a pelmanism game
"""
import pygame

from geoff_gui.alignment import Alignment
from geoff_gui.base_component import BaseComponent
from geoff_gui.button import Button
from geoff_gui.colours import Colours
from geoff_gui.label import Label
from geoff_gui.panel import Panel
from geoff_gui.textbox import TextBox

# Version check
if pygame.get_sdl_version() < (2, 0, 0):
    raise Exception("This example requires pygame 2.")

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
        limits = self.display.get_rect()
        self.gui_root = Panel(limits, self.display)

        x_spacing = WIDTH // 4
        for x in range(3):
            for y in range(3):
                b = Button((x + 1) * x_spacing - 30, y * 50 + 25)
                b.text = f'Btn ({x},{y})'
                b.vertical_alignment = [Alignment.TOP, Alignment.MIDDLE, Alignment.BOTTOM][y]
                b.horizontal_alignment = [Alignment.LEFT, Alignment.CENTER, Alignment.RIGHT][x]
                b.tag = y * 3 + x + 1
                b.onClick = self.take_click
                self.gui_root.add_component(b)

        self.label1 = Label(WIDTH // 2, HEIGHT // 2, text='HELLO')
        self.label1.font_size = 25
        self.label1.text_align = (Alignment.CENTER, Alignment.MIDDLE)

        self.textbox1 = TextBox(WIDTH // 2, HEIGHT // 2 + 100, 200)
        self.textbox1.onChange = self.text_entered

        self.gui_root.add_component(self.label1)
        self.gui_root.add_component(self.textbox1)

    def take_click(self, comp: BaseComponent, pos: tuple):
        repos = [
            (Alignment.RIGHT, Alignment.BOTTOM),
            (Alignment.CENTER, Alignment.BOTTOM),
            (Alignment.LEFT, Alignment.BOTTOM),
            (Alignment.RIGHT, Alignment.MIDDLE),
            (Alignment.CENTER, Alignment.MIDDLE),
            (Alignment.LEFT, Alignment.MIDDLE),
            (Alignment.RIGHT, Alignment.TOP),
            (Alignment.CENTER, Alignment.TOP),
            (Alignment.LEFT, Alignment.TOP),
        ]
        self.label1.text_align = repos[comp.tag - 1]
        self.label1.text = f'Clicked {comp.tag}'

    def text_entered(self, comp: BaseComponent, before_text: str, after_text: str) -> None:
        self.label1.text = after_text

    def draw(self):
        self.gui_root.draw()
        pygame.draw.line(self.display, Colours.BLUE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
        pygame.draw.line(self.display, Colours.BLUE, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2))
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
            self.gui_root.message(messages)

        pygame.quit()


if __name__ == '__main__':
    main = GeoffGui()
    main.run()
