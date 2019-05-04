import pygame as pg
import random, sys, time, math
from pygame.locals import *

pg.init()
#declaring variables
fps = 60
display_width = 1500
display_length = 1071
gameDisplay = pygame.display.set_mode((display_width,display_length))
pygame.display.set_caption('Graphic Test')
fpsClock = pygame.time.Clock()
pygame.font.init()
levelFont = pygame.font.SysFont('Comic Sans MS', 60)
textsurface = levelFont.render('1', False, Black)
events = pg.event.get()

#function that will run the game
def gameLoop():
    game_Exit = False
    # game update thing
    while not game_Exit:
        for event in events:
            if event.type == QUIT:
                pg.quit()


gameLoop()
pg.quit()
