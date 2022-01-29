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
    [
        [True, True, True],
        [None, True, None],
    ],
    [
        [None, True, True],
        [True, True, None],
    ],
    [
        [True, True, None],
        [None, True, True],
    ],
]

COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (192, 192, 192), (128, 128, 128)]

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
        self.shape = random.choice(BLOCKS).copy()

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
                while y >= 0 and self.shape[y][x] is None:
                    y = y-1

                if self.shape[y][x] is not None:  # Could be a column without solid block
                    coords.append((self.x + x, self.y + y + 1))

        return coords

    def deleteShapeRow(self, row):
        """
            Deletes a row of the shape and updates the size.

            Parameters
            ----------
            row : int
                The row to delete
        """
        if 0 <= row < self.height:
            del self.shape[row]
            self.height = len(self.shape)

            if self.height > 0:
                self.width = len(self.shape[0])
            else:
                self.width = 0

    def rotate(self, clockwise=True):
        """
            Rotates the shape of the block.

            Parameters
            ----------
            clockwise : bool, optional
                If True, it performs a 90° rotation
                If False, it performs a -90° rotation
        """
        if clockwise:
            self.shape = list(zip(*reversed(self.shape)))  # 90°
        else:
            self.shape = list(reversed(list(zip(*self.shape))))  # -90°

        # Convert to list
        self.shape = [list(t) for t in self.shape]

        self.width = len(self.shape[0])
        self.height = len(self.shape)
