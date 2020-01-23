
import pygame, sys, time, random
from pygame.locals import *


pygame.init()
mainClock = pygame.time.Clock()


width = 500
height = 500
windowSurface = pygame.display.set_mode((width, height), 0, 32)

pygame.display.set_caption('WASD')


moveLeft = False
moveRight = False
moveUp = False
moveDown = False

x = 300
y = 300

movementSpeed = 5

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    windowSurface.fill(white)

    if event.type == KEYDOWN:
        if event.key == K_UP or event.key == K_w:
            moveUp = True
        if event.key == K_DOWN or event.key == K_s:
            moveDown = True
        if event.key == K_LEFT or event.key == K_a:
            moveLeft = True
        if event.key == K_RIGHT or event.key == K_d:
            moveRight = True

    if event.type == KEYUP:
        if event.key == K_UP or event.key == K_w:
            moveUp = False
        if event.key == K_DOWN or event.key == K_s:
            moveDown = False
        if event.key == K_LEFT or event.key == K_a:
            moveLeft = False
        if event.key == K_RIGHT or event.key == K_d:
            moveRight = False
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

    if x == -30:
        x = 470
    if x == 530:
        x = 30
    if y == -30:
        y = 470
    if y == 530:
        y = 30

    if moveUp == True:
        y -= movementSpeed
    if moveDown == True:
       y += movementSpeed
    if moveLeft == True:
        x -= movementSpeed
    if moveRight == True:
        x += movementSpeed

    windowSurface.fill(white)

    pygame.draw.circle(windowSurface, black, (x, y), 30)

    pygame.display.update()
    mainClock.tick(60)