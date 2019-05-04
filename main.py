from pygame_functions import *
import pygame as pg
import random, sys, time, math
from pygame.locals import *

#declaring variables
screenWidth = 600
screenHeight = 416
fps = 60
#setting screen size
screenSize(screenWidth, screenHeight)
setAutoUpdate(True)


xPos = 500
yPos = 500
xSpeed = 0
ySpeed = 0
setBackgroundImage("city2.jpg")
person = makeSprite("personSprite.png")
while(xPos > 600):
    scrollBackground(600,0)
    xPos -= 600
while(yPos > 416):
    scrollBackground(0,416)
    yPos -= 416
showSprite(person)
moveSprite(person, xPos, yPos)

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
        rotateSprite(person, 0, True)
        if(xPos <= 600):
            xSpeed += 2
        else:
            scrollBackground(600, 0)
            xPos = 0
    if keyPressed('left'):
        rotateSprite(person, 0, False)
        if(xPos >= 0):
            xSpeed -= 2
        else:
            scrollBackground(-600, 0)
            xPos = 600
    if tabClick():
        print('test')
    #if keyPressed('space'):
        #insert function to enter building/perform action
    xPos += xSpeed
    if xPos > 660:
        xPos = -100
    elif xPos < -100:
        xPos = 660
    yPos += ySpeed  
    if yPos > 560:
        yPos = -100
    elif yPos < -100:
        yPos = 560
    ySpeed = 0
    xSpeed = 0
    moveSprite(person, xPos, yPos)
    tick(fps)

endWait()
pg.quit()