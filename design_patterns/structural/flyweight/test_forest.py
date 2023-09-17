from forest import Tree, TreeType, TreeFactory, Forest


def test_heavy_memory_draw():
    oak_type = TreeType('Oak', 'brown', 'oak.png')
    oak = Tree(12, 12, oak_type)
    # light
    oak.draw('<thick canvas>')

    # if I use tree type each time I draw tree with everything
    oak_type.draw('<thick canvas>', 22, 33)


def test_trees():
    oak = TreeType('Oak', 'brown', 'oak.png')
    birch = TreeType('Birch', 'light', 'birch.png')
    chestnut = TreeType('Oak', 'light', 'oak.png')
    spruce = TreeType('Spruce', 'delicate', 'spruce.png')

    TreeFactory.tree_types =  [oak, birch, chestnut, spruce]
    TreeFactory.get_tree_type('Oak', 'brown', "oak.pnga")



def test_forest():
    forset = Forest()
    forset.plant_tree(12, 16, 'Oak', 'brown', 'oak.png')
    forset.plant_tree(12, 23, 'Oak', 'brown', 'oak.png')
    forset.plant_tree(12, 23, 'Oak', 'brown', 'oak.png')
    forset.plant_tree(12, 43, 'Birch', 'brown', 'birch.png')
    forset.plant_tree(3232, 233, 'Birch', 'brown', 'birch.png')
    forset.plant_tree(2, 23, 'Birch', 'brown', 'birch.png')
    forset.plant_tree(11, 22, 'Birch', 'brown', 'birch.png')
    forset.plant_tree(11, 23, 'Birch', 'white', 'birch.png')

    forset.draw('<my canvas>')
