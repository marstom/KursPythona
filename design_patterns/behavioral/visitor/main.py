import pygame
import sys
import random
from pygame import gfxdraw
from pygame.colordict import THECOLORS

from shape import Dot, Shape, JSONVisitor, Circle, Rectangle


class BaseGame:

    def __init__(self):
        # Initialize Pygame
        self.running = True

        pygame.init()
        self.frame_no = 0

        # Screen dimensions
        self.screen_width = 800
        self.screen_height = 600

        # Colors
        self.white = (255, 255, 255)

        # Create the screen
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Shapes")
        self._init_objects_once()

    def game_loop(self):
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    self._handle_key_down(event.key)
                if event.type == pygame.KEYUP:
                    self._handle_key_up(event.key)

            keys = pygame.key.get_pressed()
            self._handle_pressed(keys)
            self.__render()
            clock.tick(60)

        pygame.quit()
        sys.exit()

    def __render(self):
        # Clear the screen
        self.screen.fill(self.white)
        self.frame_no += 1
        self._draw_objects_loop()
        # Update the display
        pygame.display.flip()


class Game(BaseGame):
    def _init_objects_once(self):
        print("Init object once")
        self.dot = Dot(self.screen, gfxdraw.pixel, THECOLORS.get("brown"))
        self.circle = Circle(self.screen, pygame.draw.circle, THECOLORS.get("blue4"), 50)
        self.circle.move(231, 321)
        rect = pygame.Rect(100, 200, 20, 50)
        self.rect = Rectangle(self.screen, pygame.draw.rect, rect, THECOLORS.get("coral"))

        self.visitor = JSONVisitor()

    def _draw_objects_loop(self):
        self.circle.draw()
        self.rect.draw()
        self.dot.draw()

    def _handle_key_down(self, key: int):
        """Single hit"""
        if key == pygame.K_q:
            self.running = False
        print(f"Down: a {key}")

    def _handle_key_up(self, key: int):
        """Single up"""
        print(f"UP: a {key}")
        print(f"visit dot json: {self.visitor.visit_dot(self.dot)}")
        print(f"visit circle json: {self.visitor.visit_circle(self.circle)}")
        print(f"visit rect json: {self.visitor.visit_rectangle(self.rect)}")

    def _handle_pressed(self, keys: tuple):
        """Constant move"""
        if keys[pygame.K_d]:
            self.dot.move(2, 0)
        if keys[pygame.K_a]:
            self.dot.move(-2, 0)
        if keys[pygame.K_w]:
            self.dot.move(0, -2)
        if keys[pygame.K_s]:
            self.dot.move(0, 2)


if __name__ == '__main__':
    game = Game()
    game.game_loop()
