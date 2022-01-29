from Block import Block

class OverlapError(Exception):
    pass

class Tetris:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[None for x in range(width)] for y in range(height)]
        self._current_block = None  # Contains the block controlled by the player
        self.score = 0


    def _canFall(self, block):
        """
            Tells if a specific block can fall in the current configuration of the grid

            Parameters
            ----------
            block : Block
                The block that has to be checked

            Returns
            -------
            bool
                False : if something is under the block or it arrived at the bottom
                True  : otherwise (it can fall)
        """
        # Arrived at the bottom
        if (block.y + block.height-1) == self.height-1:
            return False

        # Checks the bottom of the block
        for coord in block.getBottomCoords():
            if self.grid[coord[1]][coord[0]] is not None:
                return False

        return True

    def _insertBlock(self, block):
        """
            Inserts the block in the grid. The position is specified in the block object.

            Parameters
            ----------
            block : Block
            The block to insert in the grid

            Raises
            -------
            RuntimeError
                If the new block overlaps with an existing block
        """
        for y in range(block.height):
            for x in range(block.width):
                if block.shape[y][x]:
                    if self.grid[block.y+y][block.x+x] is not None:
                        raise OverlapError("Blocks are overlapping")
                        
                    self.grid[block.y+y][block.x+x] = block
        
    def _removeBlock(self, block):
        """
            Removes the block in the grid. The position is specified in the block object.

            Parameters
            ----------
            block : Block
            The block to remove in the grid
        """
        for y in range(block.height):
            for x in range(block.width):
                if 0 <= block.y+y < self.height and 0 <= block.x+x < self.width:
                    if block.shape[y][x] and self.grid[block.y+y][block.x+x] == block:
                        self.grid[block.y+y][block.x+x] = None

    def _moveX(self, block, direction):
        """
            Moves the block to a specified direction along the x-axis (if possible).

            Parameters
            ----------
            block : Block
                The block to move
            direction : int
                The direction of the move

            Returns
            -------
            bool
                True  : on success
                False : otherwise

            Examples
            --------
                >>> _moveX(-1) represents a move to left
                >>> _moveX(1)  represents a move to right
        """
        old_position = block.x
        new_position = block.x + direction

        # Checks if it goes out of bounds
        if new_position < 0 or (new_position + block.width > self.width):
            return False

        try:
            self._removeBlock(block)
            block.x = new_position
            self._insertBlock(block)
            return True
        except OverlapError:
            # Revert the move
            self._removeBlock(block)
            block.x = old_position
            self._insertBlock(block)
            return False

    def _moveY(self, block, direction):
        """
            Moves the block a specific number of cells down (if possible).

            Parameters
            ----------
            block : Block
                The block to move
            direction : int
                The direction of the move. It must be >= 0

            Returns
            -------
            bool
                True  : on success
                False : otherwise
        """
        self._removeBlock(block)

        while self._canFall(block) and direction > 0:
            block.y = block.y + 1
            direction = direction - 1

        self._insertBlock(block)
    
    def moveLeft(self):
        """
            Moves the current block to left.
        """
        if self._current_block is not None:
            self._moveX(self._current_block, -1)

    def moveRight(self):
        """
            Moves the current block to right.
        """
        if self._current_block is not None:
            self._moveX(self._current_block, 1)

    def moveDown(self):
        """
            Moves the current block at the bottom.
        """
        if self._current_block is not None:
            self._moveY(self._current_block, self.height)

    def _isFullRow(self, row):
        """
            Checks if a row only contains blocks.

            Parameters
            ----------
            row : int
                The row to check

            Returns
            -------
            bool
                True  : if the row is full
                False : otherwise
        """
        for x in range(self.width):
            if self.grid[row][x] is None:
                return False
        return True

    def _resetRow(self, row):
        """
            Resets a specific row by setting everything to None.

            Parameters
            ----------
            row : int
                The row to reset
        """
        x = 0
        prev = None
        while x < self.width:
            if self.grid[row][x] != prev:
                self.grid[row][x].deleteShapeRow(row - self.grid[row][x].y) # Deletes the corrisponding row in the block shape
                prev = self.grid[row][x]
            self.grid[row][x] = None
            x = x + 1

    def _handleGravity(self):
        """
            Handles the gravity of the entire board.
        """
        for y in range(self.height - 2, -1, -1):
            for x in range(self.width):
                if self.grid[y][x] is not None and self._canFall(self.grid[y][x]):
                    self._moveY(self.grid[y][x], self.height)

    def rotate(self, clockwise):
        """
            Rotates the current block.

            Parameters
            ----------
            clockwise : bool
                If True, performs a clockwise rotation, couterclockwise otherwise
        """
        if self._current_block is not None:
            self._removeBlock(self._current_block)
            self._current_block.rotate(clockwise)
            try:
                self._insertBlock(self._current_block)
            except (OverlapError, IndexError):
                # Revert the rotation
                self._removeBlock(self._current_block)
                self._current_block.rotate(not clockwise)
                self._insertBlock(self._current_block)


    def nextStep(self):
        """
            Updates the grid to the next game cycle.

            Returns
            -------
            bool
                False : if the game is over
                True  : otherwise
        """
        if self._current_block is None:
            # Generates a new block
            new_block = Block(round(self.width / 2) - 2, 0)
            self._current_block = new_block
            try:
                self._insertBlock(new_block)
            except OverlapError:
                return False  # Game over
        else:
            if self._canFall(self._current_block):
                self._moveY(self._current_block, 1)
            else:
                self._current_block = None

                # Score update
                # The loop is used to handle a full row that is created after the fall of other blocks
                something_changed = True
                while something_changed:
                    something_changed = False

                    # Checks for full rows
                    for y in range(self.height - 1, -1, -1):
                        if self._isFullRow(y):
                            self._resetRow(y)
                            self.score = self.score + 1
                            something_changed = True

                    self._handleGravity()

        return True
