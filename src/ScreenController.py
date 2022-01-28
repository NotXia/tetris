from settings import *

class ScreenController:
    def __init__(self, pygame):
        self.pygame = pygame

        screen_width = WIDTH*(CELL_SIZE-1) + 150
        screen_height = HEIGHT*(CELL_SIZE-1)
        self._screen = pygame.display.set_mode([screen_width, screen_height])

    def _drawCell(self, x, y, color):
        """
            Draws the cell of a specific position. Does not render on screen.

            Parameters
            ----------
            x, y : int
                Coordinates of the cell

            color : Tuple (int, int, int)
                RGB color of the cell
        """
        cell_distance = CELL_SIZE - 1
        self.pygame.draw.rect(self._screen, color, (x*cell_distance, y*cell_distance, CELL_SIZE, CELL_SIZE))
        self.pygame.draw.rect(self._screen, BORDER_COLOR, (x*cell_distance, y*cell_distance, CELL_SIZE, CELL_SIZE), width=1, border_radius=1) # Border

    def initUI(self):
        """
            Initializes and renders the user interface
        """
        self._screen.fill(BACKGROUND_COLOR)
        
        for y in range(HEIGHT):
            for x in range(WIDTH):
                self._drawCell(x, y, EMPTY_COLOR)

        self.pygame.display.update()

    def update(self, grid):
        """
            Renders the board

            Parameters
            ----------
            Grid : matrix
                The current state of the board
        """
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if grid[y][x] is not None:
                    self._drawCell(x, y, grid[y][x].color)
                else:
                    self._drawCell(x, y, EMPTY_COLOR)
                
        self.pygame.display.update()
