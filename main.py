from pygame_functions import *
import pygame as pg
import random, sys, time, math
from pygame.locals import *
#declaring variables
screenWidth = 600
screenHeight = 400
fps = 60
#setting screen size
screenSize(screenWidth, screenHeight)
setAutoUpdate(True)
ScreenX = 1
ScreenY = 1
#new Screen variables
office = False
fastFood = False
home = False
outside = False

increment = 0
#Variables to see if you're at edge of screen
xMax = False
yMax = False
yMin = False
xMin = False

xPos = 500
yPos = 500
xSpeed = 0
ySpeed = 0
setBackgroundImage("FINANCEGAME4.bmp")
person = makeSprite("personSprite.png")
while(xPos > 600):
    scrollBackground(600,0)
    ScreenX += 1
    xPos -= 600
while(yPos > 400):
    ScreenY += 1
    scrollBackground(0,400)
    yPos -= 400

    scrollBackground(0,416)
    yPos -= 416

showSprite(person)
moveSprite(person, xPos, yPos)
while True:
#key press to detect movement
    if keyPressed("up") and not yMin:
        if(yPos >= 0):
            ySpeed -= 2
        else:
            scrollBackground(0, 400)
            yPos = 400
            ScreenY += 1
    if keyPressed('down') and not yMax:
        #rotateSprite(person, -90)
        if(yPos <= 400):
            ySpeed += 2
        else:
            scrollBackground(0, -400)
            yPos = 0
            ScreenY -= 1
    if keyPressed('right') and not xMax:
        transformSprite(person, 0, 1, True)
        if(xPos <= 600):
            xSpeed += 2
        else:
            scrollBackground(600, 0)
            ScreenX += 1
            xPos = 0
    if keyPressed('left') and not xMin:
        transformSprite(person, 0,1, False)
        if(xPos >= 0):
            xSpeed -= 2
        else:
            scrollBackground(-600, 0)
            ScreenX -= 1
            xPos = 600
    if keyPressed('tab'):
        print('test')
        #this will then display the bars for hunger, happiness, fatigue, and fitness
    if keyPressed('space'):
        #insert function to enter building/perform action
        #print('Space pressed')
        if increment % 2 == 1:
            outside = True
            increment += 1
        else:
            outside = False
            increment += 1

        print (increment)
        #insert function to enter building/perform action
        #will check which screen it is on and see if its at a door, if it is it will enter the door
        #if(ScreenX == 1 and ScreenY ==1 and xPos == SMTH and yPos == ELSE):
        #fastFood = True
    
    xPos = MiscUtils.Loop(xPos + xSpeed, -100, 660)
    yPos = MiscUtils.Loop(yPos + ySpeed, -100, 560)

    if player.get_location() == "outside":
        #this allows the screen to change
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
    else:
        #these tests to see if you're indoors you do not leave the screen
        if xPos > 520:
            xMax = True
        else:
            xMax = False
            xPos += xSpeed
        if xPos < 10:
            xMin = True
        else:
            xMin = False
            xPos += xSpeed
        if yPos > 270:
            yMax = True
        else:
            yMax = False
            yPos += ySpeed
        if yPos < 10:
            yMin = True
        else:
            yMin = False
            yPos += ySpeed

    ySpeed = 0
    xSpeed = 0
    moveSprite(person, xPos, yPos)
    tick(fps)

endWait()
pg.quit()