import pygame
import sys
import random
from pygame import gfxdraw
from pygame.colordict import THECOLORS


class BaseGame:

    def __init__(self):
        # Initialize Pygame

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
        running = True
        clock = pygame.time.Clock()
        while running:
            # keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    self._handle_key_down(event.key)
                if event.type == pygame.KEYUP:
                    self._handle_key_up(event.key)

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

    def _draw_objects_loop(self):
        for i in range(15):
            for j in range(15):
                gfxdraw.pixel(self.screen, i + self.frame_no, j, THECOLORS['brown'])
        # pygame.draw.line(self.screen, THECOLORS['brown'], (0,0), (self.frame_no, self.frame_no))


    def _handle_key_down(self, key: int):
        print(f"Down: a {key}")
        # print(f"Down: w {keys[pygame.K_w]}")

    def _handle_key_up(self, key: int):
        print(f"UP: a {key}")
        # print(f"UP: w {keys[pygame.K_w]}")


if __name__ == '__main__':
    game = Game()
    game.game_loop()
