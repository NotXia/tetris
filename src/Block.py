from settings import BLOCKS, COLORS
import random
import copy

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
        self.shape = copy.deepcopy(random.choice(BLOCKS))

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

    def clearRow(self, row):
        """
            Clears a specific row of the shape

            Parameters
            ----------
            row : int
                The row to delete
        """
        if 0 <= row < self.height:
            for i in range(self.width):
                self.shape[row][i] = None

    def _changeShape(self, shape):
        """
            Updates the shape of the block

            Parameters
            ----------
                shape : matrix
                    The new shape
        """
        self.shape = shape

        self.width = len(self.shape[0])
        self.height = len(self.shape)

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
            new_shape = list(zip(*reversed(self.shape)))        # 90° rotation
        else:
            new_shape = list(reversed(list(zip(*self.shape))))  # -90° rotation
        new_shape = [list(t) for t in new_shape]  # Convert to list

        self._changeShape(new_shape)

    def _isEmptyRow(self, row):
        """
            Checks if the row is empty

            Parameters
            ----------
            row : int
                The row to check

            Returns
            -------
            bool
                False : the row contains a solid block
                True  : otherwise
        """
        for x in range(self.width):
            if self.shape[row][x]:
                return False
        return True

    def dismantle(self):
        """
            Splits the current block into new blocks based on empty lines

            Returns
            -------
            new_blocks : list of Block
                The new blocks obtained after the split
        """
        new_blocks = []

        start = 0
        for i in range(self.height):
            if self._isEmptyRow(i):
                # Creates a new block if it is at least 1 block high
                if (len(self.shape[start:i]) > 0):
                    new_block = copy.deepcopy(self)
                    new_block.y = self.y + start
                    new_block._changeShape(new_block.shape[start:i])
                    new_blocks.append(new_block)
                start = i+1
        # Creates a block with the remaining part (if needed)
        if (len(self.shape[start:]) > 0):
            new_block = copy.deepcopy(self)
            new_block.y = self.y + start
            new_block._changeShape(new_block.shape[start:])
            new_blocks.append(new_block)

        return new_blocks
