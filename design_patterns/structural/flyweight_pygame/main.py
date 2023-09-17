import random
import pygame
import sys

from forest import Tree, TreeType, TreeFactory, Forest


def tre():
    # Initialize Pygame
    pygame.init()

    # Screen dimensions
    screen_width = 800
    screen_height = 600

    # Colors
    white = (200, 200, 200)

    # Create the screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Tree with Transparent Background")

    ########
    # Load the sprite sheet containing the tree image
    sprite_sheet = pygame.image.load("tree-8240.png")  # Replace with your sprite sheet file
    # Create a copy of the sprite sheet with a transparent background
    tree_image = sprite_sheet.copy()
    # Define the scale factor (10% size)
    scale_factor = 0.1
    # Calculate the scaled dimensions
    scaled_width = int(tree_image.get_width() * scale_factor)
    scaled_height = int(tree_image.get_height() * scale_factor)
    # Scale the tree image to 10% size
    tree_image = pygame.transform.scale(tree_image, (scaled_width, scaled_height))

    # Define the position to blit (draw) the tree on the screen
    tree_x = 23
    tree_y = 22

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(white)

        # Blit (draw) the tree with a transparent background
        screen.blit(tree_image, (tree_x, tree_y))

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()


class Game:
    white = (200, 200, 200)

    def init(self):
        # Initialize Pygame
        pygame.init()

        # Screen dimensions
        self.screen_width = 800
        self.screen_height = 600

        # Colors

        # Create the screen
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Tree with Transparent Background")
        self._init_objects_once()

    def loop(self):
        # Game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self._render()

        # Quit Pygame
        pygame.quit()
        sys.exit()

    def _render(self):
        # Clear the screen
        self.screen.fill(self.white)

        self._draw_objects_loop()

        # Update the display
        pygame.display.flip()

    def _init_objects_once(self):
        """ We have 2000 trees, but need load texture only twice!"""
        self.forest = Forest()
        for _ in range(1000):
            x1 = random.randint(0, self.screen_width)
            x2 = random.randint(0, self.screen_width)
            y1 = random.randint(0, self.screen_height)
            y2 = random.randint(0, self.screen_height)
            self.forest.plant_tree(x1, y1, "tree1", "white", "tree-8240.png")
            self.forest.plant_tree(x2, y2, "tree2", "white", "tree-8258.png")

    def _draw_objects_loop(self):
        self.forest.draw(self.screen)


if __name__ == '__main__':
    game = Game()
    game.init()
    game.loop()
