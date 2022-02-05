import pygame
from settings import *
from Tetris import Tetris
from ScreenController import ScreenController

pygame.init()
pygame.display.set_caption("Tetris")
tetris = Tetris(WIDTH, HEIGHT) # Game controller
screenController = ScreenController(pygame)

screenController.initUI()

fall_delay = FALL_DELAY_START
fall_prev_tick = 0
score_at_last_delay_update = 0

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(FPS)

    events = pygame.event.get()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        tetris.moveLeft()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        tetris.moveRight()
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        tetris.moveDown()

    # To prevent uncontrollable rotation
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                tetris.rotate(clockwise=True)
            if event.key == pygame.K_q:
                tetris.rotate(clockwise=False)

    if pygame.time.get_ticks() - fall_prev_tick >= fall_delay:  # Handles game's speed
        if not tetris.nextStep():
            # Game over
            screenController.gameOver()
            # Waits an input to close the game
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                        running = False
        fall_prev_tick = pygame.time.get_ticks()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Increases the speed if the threshold is reached
    if tetris.score != score_at_last_delay_update and tetris.score % FALL_DELAY_SCORE_THRESHOLD == 0:
        fall_delay = fall_delay / FALL_DELAY_DECREASE_RATE
        score_at_last_delay_update = tetris.score
        
    screenController.renderGrid(tetris.grid)
    screenController.updateScore(tetris.score)
    screenController.renderNextBlock(tetris.next_block)

pygame.quit()
