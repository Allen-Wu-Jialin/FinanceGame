from pygame_functions import *
import pygame as pg
import random, sys, time, math
from pygame.locals import *

#declaring variables
screenWidth = 1000
screenHeight = 750
fps = 60
#setting screen size
screenSize(screenWidth, screenHeight)
setAutoUpdate(True)


xPos = 500
yPos = 350
xSpeed = 0
ySpeed = 0
setBackgroundImage("city.jpg")
person = makeSprite("personSprite.png")
showSprite(person)
moveSprite(person, xPos, yPos)

while True:
#key press to detect movement
    if keyPressed("up"):
        #rotateSprite(person, 90)
        ySpeed -= 2
    if keyPressed('down'):
        #rotateSprite(person, -90)
        ySpeed += 2
    if keyPressed('right'):
        rotateSprite(person, 0, True)
        xSpeed += 2
    if keyPressed('left'):
        rotateSprite(person, 0, False)
        xSpeed -= 2
    xPos += xSpeed
    if xPos > 560:
        xPos = -100
    elif xPos < -100:
        xPos = 560
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