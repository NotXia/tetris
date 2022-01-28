import random

BLOCKS = [
    [
        [True, True, True], 
        [True, None, None], 
    ],
    [
        [True, True, True], 
        [None, None, True], 
    ],
    [
        [True, True], 
        [True, True], 
    ],
    [
        [True, True, True, True], 
    ],
]

COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

class Block:
    def __init__(self, x, y):
        """
            Initialize a block with a random shape and color.

            Parameters
            ----------
            x, y : int
                (x, y) coordinates referring to the top-left corner of the block
        """
        self.x, self.y = x, y
        self.color = random.choice(COLORS)
        self.shape = random.choice(BLOCKS)

        self.width = len(self.shape[0])
        self.height = len(self.shape)


    def getBottomCoords(self):
        """
            Returns the coordinates of the bottom of the block.

            Returns
            -------
            coords : list of tuples (int, int)
                List of tuples containing the coordinates (x, y)

            Examples
            --------
            For the following 'L' shaped block, it returns the coordinates of the cells marked with X
            [True, True, True]
            [True,  X,    X  ]
              X
        """
        coords = []

        for x in range(self.width):
            # Starting from the bottom, the position below the first solid cell is considered
            if self.shape[self.height-1][x] is not None:
                coords.append((self.x + x, self.y + self.height))
            else:
                # Searches for the first solid cell
                y = self.height-2
                while self.shape[y][x] is None:
                    y = y-1

                coords.append((self.x + x, self.y + y+1))

        return coords