#Noah Omordia, 2/11/20, Mr.Acosta

import pygame, sys, time, random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()
y2 = 35
x = 350
y = 35
y3 = 280
x2 = 25
x3 = 625

move = False
movementSpeed = 20
movementSpeed2 = 20
circleMovement = 10
circleMovementx = 10
circleMovementy = 10
moveUp = False
moveDown = False
moveUP2 = False
moveDOWN2 = False

downLeft = 'downleft'
downRight = 'downright'
upLeft = 'upleft'
upRight = 'upright'

scorex = 0
p1score = 0
p2score = 0
scorey = 0
width = 700
height = 600
moveBall = False
moveyball = False
windowSurface = pygame.display.set_mode((width, height), 0, 32)

pygame.display.set_caption('Pong')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
circleL = [-1,1]
circlev = random.choice(circleL)
windowSurface = pygame.display.set_mode((width,height))




while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    if event.type == KEYDOWN:
        if event.key == K_UP:
            moveUp = True
        if event.key == K_DOWN:
            moveDown = True

    if event.type == KEYUP:
        if event.key == K_UP:
            moveUp = False
        if event.key == K_DOWN:
            moveDown = False
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.key == K_SPACE:
            moveBall = True
            moveyball = True
    if event.type == KEYDOWN:
        if event.key == K_w:
            moveUP2 = True
        if event.key == K_s:
            moveDOWN2 = True
    if event.type == KEYDOWN:
        if event.key == K_c:
            restart = True

    if event.type == KEYUP:
        if event.key == K_w:
            moveUP2 = False
        if event.key == K_s:
            moveDOWN2 = False

    if moveUp == True:
        y -= movementSpeed
    if moveDown == True:
        y += movementSpeed
    if moveUP2 == True:
        y2 -= movementSpeed2
    if moveDOWN2 == True:
        y2 += movementSpeed2

    windowSurface.fill(black)
    font = pygame.font.SysFont("none", 24)
    scoreText = "Score: " + str(p2score)
    text2 = font.render(scoreText, True, blue, black)
    windowSurface.blit(text2, (50, 0))

    scoreText = "Score: " + str(p1score)
    text3 = font.render(scoreText, True, red, black)
    windowSurface.blit(text3, (550, 0))

    x2 = 25
    x3 = 625

    player1 = pygame.draw.rect(windowSurface, red, (x3, y, 40, 125))
    player2 = pygame.draw.rect(windowSurface, blue, (x2, y2, 40, 125))
    circle = pygame.draw.circle(windowSurface, white, (x, y3), 10)


    if x >= 700:
        p1score += 1
        moveyball = False
        moveBall = False
        x = 350
        y3 = 280
    if x <= 0:
        p2score += 1
        moveyball = False
        moveBall = False
        x = 350
        y3 = 280

    if p2score >= 3:
        circleMovementy = 0
        circleMovementx = 0
        windowSurface.fill(black)
        font = pygame.font.SysFont("none", 68)
        textb = font.render("RED WINS!", True, red, black)
        windowSurface.blit(textb, (250,280))
    if p1score >= 3:
        circleMovementx = 0
        circleMovementy = 0
        windowSurface.fill(black)
        font = pygame.font.SysFont("none", 68)
        textl = font.render("BLUE WINS!", True, blue, black)
        windowSurface.blit(textl,(250,280))
    if y == 600 and y2 == 600 and y == 0 and y2 == 0:
        x3 -= 20
        x2 -= 20
    if y3 <= 0:
        circleMovementy = circleMovementy * -1
    if y3 >= 600:
        circleMovementy = circleMovementy * -1
    if x == x3:
        x = x * -1
    if x == x2:
        x = x * -1

    if x > player1.left and player1.top < y3 < player1.bottom:
        circleMovementx = circleMovementx * -1
    if x < player2.right and player2.top < y3 < player2.bottom:
        circleMovementx = circleMovementx * -1
    if moveBall == True:
        x += circleMovementx * circlev
    if moveyball == True:
        y3 += circleMovementy * circlev


    pygame.display.update()
    mainClock.tick(60)

#Overall, It's alright. It satisfied the parameters, although it is late. I am curious as to how I could make it best out of 3. I might change it into that later Anyway this is my pong game.