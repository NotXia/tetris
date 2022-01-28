from Block import Block

class OverlapError(Exception):
    pass

class Tetris:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[None for x in range(width)] for y in range(height)]
        self._current_block = None # Contains the block controlled by the player


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
                if block.shape[y][x] and self.grid[block.y+y][block.x+x] == block:
                    self.grid[block.y+y][block.x+x] = None

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
            new_block = Block(round(self.width/2)-2, 0)
            self._current_block = new_block
            try:
                self._insertBlock(new_block)
            except OverlapError:
                return False # Game over
        else:
            if self._canFall(self._current_block):
                self._removeBlock(self._current_block)
                self._current_block.y = self._current_block.y + 1
                self._insertBlock(self._current_block)
            else:
                self._current_block = None

        return True


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
