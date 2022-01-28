from settings import *

class ScreenController:
    def __init__(self, pygame):
        self.pygame = pygame

        screen_width = WIDTH*(CELL_SIZE-1) + 200
        screen_height = HEIGHT*(CELL_SIZE-1)
        self._screen = pygame.display.set_mode([screen_width, screen_height])

        self._font = pygame.font.Font(pygame.font.get_default_font(), 32)

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

        # Score 
        self.updateScore(0)

        # Grid
        for y in range(HEIGHT):
            for x in range(WIDTH):
                self._drawCell(x, y, EMPTY_COLOR)

        self.pygame.display.update()

    def renderGrid(self, grid):
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

    def updateScore(self, score):
        """
            Updates the score

            Parameters
            ----------
            score : int
                The score to show
        """
        score_container = self.pygame.draw.rect(self._screen, BACKGROUND_COLOR, (WIDTH*(CELL_SIZE-1), 50, 200, 50))
        score_text = self._font.render(f"{score}", True, SCORE_COLOR)
        score_rect = score_text.get_rect()
        score_rect.center = score_container.center
        self._screen.blit(score_text, score_rect)



