import pygame
from settings import *
from Tetris import Tetris
from ScreenController import ScreenController

pygame.init()
tetris = Tetris(WIDTH, HEIGHT) # Game controller
screenController = ScreenController(pygame)

screenController.initUI()

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        tetris.moveLeft()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        tetris.moveRight()
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        tetris.moveDown()
    if keys[pygame.K_e]:
        tetris.rotate(clockwise=True)
    if keys[pygame.K_q]:
        tetris.rotate(clockwise=False)

    if not tetris.nextStep():
        print("Game over")
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screenController.renderGrid(tetris.grid)
    screenController.updateScore(tetris.score)

pygame.quit()
