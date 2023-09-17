import unittest.mock
from unittest.mock import MagicMock

from forest import Forest


@unittest.mock.patch("pygame.image")
@unittest.mock.patch("pygame.transform")
def test_forest(im, tr):
    forset = Forest()
    forset.plant_tree(12, 16, 'Oak', 'brown', 'oak.png')
    forset.plant_tree(12, 23, 'Oak', 'brown', 'oak.png')
    forset.plant_tree(12, 23, 'Oak', 'brown', 'oak.png')
    forset.plant_tree(12, 43, 'Birch', 'brown', 'birch.png')
    forset.plant_tree(3232, 233, 'Birch', 'brown', 'birch.png')
    forset.plant_tree(2, 23, 'Birch', 'brown', 'birch.png')
    forset.plant_tree(11, 22, 'Birch', 'brown', 'birch.png')
    forset.plant_tree(11, 23, 'Birch', 'white', 'birch.png')

    screen = MagicMock()
    forset.draw(screen)
