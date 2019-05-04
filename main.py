from pygame_functions import *
import pygame as pg
import random, sys, time, math
from pygame.locals import *
from player import Player
from miscutils import MiscUtils

#declaring variables
screenWidth = 600
screenHeight = 416
fps = 60
#setting screen size
screenSize(screenWidth, screenHeight)
setAutoUpdate(True)

player = Player()

xPos = 500
yPos = 500
player.set_coord(xPos, yPos)
xSpeed = 0
ySpeed = 0
setBackgroundImage("city2.jpg")
while(xPos > 600):
    scrollBackground(600,0)
    xPos -= 600
while(yPos > 416):
    scrollBackground(0,416)
    yPos -= 416

while True:
#key press to detect movement
    if keyPressed("up"):
        #rotateSprite(person, 90)
        if(yPos >= 0):
            ySpeed -= 2
        else:
            scrollBackground(0, 416)
            yPos = 416
    if keyPressed('down'):
        #rotateSprite(person, -90)
        if(yPos <= 416):
            ySpeed += 2
        else:
            scrollBackground(0, -416)
            yPos = 0
    if keyPressed('right'):
        if(xPos <= 600):
            xSpeed += 2
        else:
            scrollBackground(600, 0)
            xPos = 0

    if keyPressed('left'):
        if(xPos >= 0):
            xSpeed -= 2
        else:
            scrollBackground(-600, 0)
            xPos = 600
    if keyPressed('tab'):
        print('test')
    #if keyPressed('space'):
        #insert function to enter building/perform action
    xPos = MiscUtils.Loop(xPos + xSpeed, -100, 660)
    yPos = MiscUtils.Loop(yPos + ySpeed, -100, 560)

    ySpeed = 0
    xSpeed = 0
    player.set_coord(xPos, yPos)
    player.draw()
    tick(fps)

endWait()
pg.quit()