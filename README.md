# Tetris
Tetris implementation in Python using Pygame.

## Installation
Run ```pip3 install -r requirements.txt``` to install the required libraries.

## Configuration
There are some configuration options in the [settings.py](src/settings.py) file.\
In particular to modify the game settings it is possible to change:
 - ```WIDTH``` and ```HEIGHT``` to set the grid size.
 - ```FALL_DELAY_START``` to set the starting blocks speed (higher the value is, slower the blocks will fall)
 - ```FALL_DELAY_SCORE_THRESHOLD``` to set the number of rows to align after which the speed will change
 - ```FALL_DELAY_DECREASE_RATE``` to set how much the speed will change


It is possible to modify or add new block shapes and colors by changing:
 - ```BLOCKS``` the list of possible shapes
 - ```COLORS``` the list of possible colors in RGB format

## Usage
Run ```python3 src/main.py``` to start the game.

### Controls
- ```A``` left move
- ```D``` right move
- ```S``` move to bottom
- ```Q``` counterclockwise rotation
- ```E``` clockwise rotation
