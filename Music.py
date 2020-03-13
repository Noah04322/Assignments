import pygame, sys, time, random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
x = 100
y = 50
xb = 100
yb = 50
xg = 100
yg = 50
xr = 100
yr = 50
x2 = 255
x3 = 410
x4 = 565
growblue = False
shrinkblue = False
growred = False
shrinkred = False
growgreen = False
shrinkgreen = False
growblack = False
shrinkblack = False
bluepause = False
greenloud = False
redplay = False
blackquiet = False
Volumeup = False
Volumedown = False


pygame.display.set_caption('music')

width = 800
height = 400
v = .5
windowSurface = pygame.display.set_mode((width, height), 0, 32)

pygame.mixer.music.load('BlippyTrance.mp3')
pygame.mixer.music.play(-1, 0)
pygame.mixer.music.set_volume(v)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    pygame.mixer.music.set_volume(v)
    windowSurface.fill(white)
    blueRect = pygame.draw.rect(windowSurface, blue, (100, 100, x, y))
    redRect = pygame.draw.rect(windowSurface, red, (280, 100, xr, yr))
    blackRect = pygame.draw.rect(windowSurface, black, (460, 100, xb, yb))
    greenRect = pygame.draw.rect(windowSurface, green, (640, 100, xg, yg))

    if event.type == MOUSEBUTTONDOWN:
        if event.pos[0]>= blueRect.left and event.pos[0] <= blueRect.right:
            growblue= True
            pygame.mixer.music.pause()
    if event.type == MOUSEBUTTONDOWN:
        if event.pos[0] >= blackRect.left and event.pos[0] <= blackRect.right:
            growblack = True
            Volumedown = True
    if event.type == MOUSEBUTTONDOWN:
        if event.pos[0] >= redRect.left and event.pos[0] <= redRect.right:
            growred = True
            pygame.mixer.music.unpause()
    if event.type == MOUSEBUTTONDOWN:
        if event.pos[0] >= greenRect.left and event.pos[0] <= greenRect.right:
            growgreen = True
            Volumeup = True
    if event.type == MOUSEBUTTONUP:
        if event.pos[0] >= blackRect.left and event.pos[0] <= blackRect.right:
            shrinkblack = True
    if event.type == MOUSEBUTTONUP:
        if event.pos[0] >= redRect.left and event.pos[0] <= redRect.right:
            shrinkred = True
    if event.type == MOUSEBUTTONUP:
        if event.pos[0] >= greenRect.left and event.pos[0] <= greenRect.right:
            shrinkgreen = True
    if event.type == MOUSEBUTTONUP:
        if event.pos[0] >= blueRect.left and event.pos[0] <= blueRect.right:
            shrinkblue = True

    if growblue == True:
        x = 200
        y = 100
    if growblack == True:
        xb = 200
        yb = 100
    if growgreen == True:
        xg = 200
        yg = 100
    if growred == True:
        yr = 100
        xr = 200
    if shrinkblack == True:
        xb = 100
        yb = 50
        growblack = False
        shrinkblack = False
    if shrinkgreen == True:
        xg = 100
        yg = 50
        growgreen = False
        shrinkgreen = False
    if shrinkred == True:
        xr = 100
        yr = 50
        growred = False
        shrinkred = False
    if shrinkblue == True:
        x = 100
        y = 50
        growblue= False
        shrinkblue = False
    if Volumeup == True and v <= 1 :
        v += .1
        Volumedown = False
        Volumeup = False
    if Volumedown == True and v >= 0:
        v -= .1
        Volumeup = False
        Volumedown = False

    print(v)
    pygame.display.update()
    mainClock.tick(60)