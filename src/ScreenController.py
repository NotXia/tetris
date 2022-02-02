from settings import *

class ScreenController:
    def __init__(self, pygame):
        self.pygame = pygame

        screen_width = WIDTH*(CELL_SIZE-1) + 200
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

    def _centerText(self, text, font_size, text_color, background_color, position, size):
        """
            Renders the text centered in a rectangle container

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
            Updates the score

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
            position = (WIDTH*(CELL_SIZE-1), 50), 
            size = (200, 50)
        )




