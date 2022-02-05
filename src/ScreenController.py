from settings import *

class ScreenController:
    def __init__(self, pygame):
        self.pygame = pygame

        self._screen_width = WIDTH*(CELL_SIZE-1) + 200
        self._screen_height = HEIGHT*(CELL_SIZE-1)
        self._screen = pygame.display.set_mode([self._screen_width, self._screen_height])

        # The x coordinate where the grid ends and anything else can be rendered without overlapping
        self._GRID_END_X = WIDTH*(CELL_SIZE-1) + 1

    def _drawSquare(self, x, y, color, texture=False):
        """
            Draws a square at a specific position. Does not render on screen.

            Parameters
            ----------
            x, y : int
                Coordinates of the cell

            color : Tuple (int, int, int)
                RGB color of the cell
            
            texture : bool
                If True the square will be drawn with a more complex texture
        """
        if texture:
            color_offset = 15
            darker_color  = [x-color_offset if x > color_offset     else x for x in color]
            lighter_color = [x+color_offset if x < 255-color_offset else x for x in color]
            self.pygame.draw.rect(self._screen, lighter_color, (x, y, CELL_SIZE, CELL_SIZE))        # Top and left color
            self.pygame.draw.rect(self._screen, darker_color, (x+5, y+5, CELL_SIZE-5, CELL_SIZE-5)) # Bottom and right color
            self.pygame.draw.rect(self._screen, color, (x+5, y+5, CELL_SIZE-10, CELL_SIZE-10))      # Main color
        else:
            self.pygame.draw.rect(self._screen, color, (x, y, CELL_SIZE, CELL_SIZE))

        self.pygame.draw.rect(self._screen, BORDER_COLOR, (x, y, CELL_SIZE, CELL_SIZE), width=1, border_radius=1)

    def _drawCell(self, x, y, color, solid=False):
        """
            Draws the cell of a specific position of the game grid. Does not render on screen.

            Parameters
            ----------
            x, y : int
                Coordinates of the cell

            color : Tuple (int, int, int)
                RGB color of the cell

            solid : bool
                Specify if the block is solid
        """
        cell_distance = CELL_SIZE - 1
        self._drawSquare(x*cell_distance, y*cell_distance, color, solid)

    def initUI(self):
        """
            Initializes and renders the user interface.
        """
        self._screen.fill(BACKGROUND_COLOR)

        # Score 
        self.updateScore(0)

        # Grid
        for y in range(HEIGHT):
            for x in range(WIDTH):
                self._drawCell(x, y, EMPTY_COLOR)

        self._initNextBlock()

        self.pygame.display.update()

    def renderGrid(self, grid):
        """
            Renders the board.

            Parameters
            ----------
            Grid : matrix
                The current state of the board
        """
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if grid[y][x] is not None:
                    self._drawCell(x, y, grid[y][x].color, solid=True)
                else:
                    self._drawCell(x, y, EMPTY_COLOR)
                
        self.pygame.display.update()

    def _centerText(self, text, font_size, text_color, background_color, position, size):
        """
            Renders the text centered in a rectangle container.

            Parameters
            ----------
                text : String
                    Text to render

                font_size : int
                    Font size

                textColor, backgroundColor : (int, int, int)
                    RGB color for the text and the background

                position : (int, int)
                    (x, y) coordinates for the top-left corner of the rectangle

                size : (int, int)
                    (width, height) for the rectangle
        """
        font = self.pygame.font.Font(self.pygame.font.get_default_font(), font_size)
        container = self.pygame.draw.rect(self._screen, background_color, (position[0], position[1], size[0], size[1]))
        text = font.render(text, True, text_color)
        rect = text.get_rect()
        rect.center = container.center
        self._screen.blit(text, rect)

    def updateScore(self, score):
        """
            Updates the score.

            Parameters
            ----------
            score : int
                The score to show
        """
        self._centerText(
            text = f"{score*100}",
            font_size = 30,
            text_color = SCORE_COLOR, 
            background_color = BACKGROUND_COLOR,
            position = (self._GRID_END_X, 10), 
            size = (200, 50)
        )

    def _drawNextBlockCell(self, x, y, color, solid=False):
        """
            Draws the cell of a specific position of the next block grid. Does not render on screen.

            Parameters
            ----------
            x, y : int
                Coordinates of the cell

            color : Tuple (int, int, int)
                RGB color of the cell
            
            solid : bool
                Specify if the block is solid
        """
        start_x = self._GRID_END_X + 75
        start_y = 120
        shift = (CELL_SIZE - 1)

        self._drawSquare(start_x + (x-1)*shift, start_y + y*shift, color, solid)


    def _initNextBlock(self):
        """
            Initialize the area to display the next block.
        """
        self._centerText(
            text = f"Next",
            font_size = 22,
            text_color = (0, 0, 0),
            background_color = BACKGROUND_COLOR,
            position = (self._GRID_END_X, 80),
            size = (200, 50)
        )

        # 3x4 grid to display the next block
        for x in range(0, 4):
            for y in range(0, 3):
                self._drawNextBlockCell(x, y, EMPTY_COLOR)

    def renderNextBlock(self, block):
        """
            Renders the next block in the UI

            Parameters
            ----------
            block : Block
                The block to render
        """
        # Cleares the previous block
        for x in range(0, 4):
            for y in range(0, 3):
                self._drawNextBlockCell(x, y, EMPTY_COLOR)

        for y in range(block.height):
            for x in range(block.width):
                if block.shape[y][x]:
                    self._drawNextBlockCell(x, y, block.color, solid=True)

        self.pygame.display.update()

    def gameOver(self):
        """
            Renders the game over screen
        """
        self._centerText(f"GAME OVER", 32, (255, 0, 0), BACKGROUND_COLOR, (0, 0), (self._screen_width, self._screen_height))
        self.pygame.display.update()
