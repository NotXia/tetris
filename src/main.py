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

    if not tetris.nextStep():
        print("Game over")
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pass

    screenController.update(tetris.grid)

pygame.quit()