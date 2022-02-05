# Screen settings
BACKGROUND_COLOR = (255, 255, 255)
SCORE_COLOR = (255, 50, 50)

# Grid's cell settings
CELL_SIZE = 25
BORDER_COLOR = (50, 50, 50)
EMPTY_COLOR = (255, 255, 255)


# Game settings
WIDTH, HEIGHT = 10, 20
FPS = 15

FALL_DELAY_START = 300
FALL_DELAY_DECREASE_RATE = 1.05
FALL_DELAY_SCORE_THRESHOLD = 1

COLORS = [(200, 0, 0), (0, 200, 0), (0, 0, 200), (200, 200, 0), (0, 200, 200), (200, 0, 200), (192, 192, 192), (128, 128, 128)]

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