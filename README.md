# Tetris
Tetris implementation in Python using Pygame.

# Installation
Run ```pip3 install -r requirements.txt``` to install the required libraries.

# Configuration
There are some configuration options in the [settings.py](src/settings.py) file.\
In particular to modify the game settings it is possible to change:
 - ```WIDTH``` and ```HEIGHT``` to set the grid size.
 - ```FALL_DELAY_START``` to set the starting blocks's speed (higher the value is, slower the blocks will fall)
 - ```FALL_DELAY_SCORE_THRESHOLD``` to set the number of aligned rows after which the speed will change
 - ```FALL_DELAY_DECREASE_RATE``` to set how much the speed will change


# Usage
Run ```python src/main.py``` to start the game.
