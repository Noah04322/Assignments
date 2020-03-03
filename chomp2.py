#Noah Omordia


import pygame, sys, time, random
from pygame.locals import *
pygame.init()
mainClock = pygame.time.Clock()

width = 600
height = 600
windowSurface = pygame.display.set_mode((width, height), 0, 32)

pygame.display.set_caption('chomp')

movementSpeed = 10

moveLeft = False
moveRight = False
moveUp = False
moveDown = False
grow = False
shrink = False
angle = 0
left = False
right = False
up = True
down = False
growp = False
shrinkp = False
score = 0
fpizza = []
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


x = 84
maxpizza = 15
y = 72
x2 = 30
y2 = 30
player = pygame.Rect(278, 264, x, y)
pizza = pygame.Rect(288, 264, x2, y2)
playerImage = pygame.image.load('PixelArt.png')
pizzaImage = pygame.image.load('PngItem_3397262.png')
playerImageStretch = pygame.transform.scale(playerImage, (x, y))
pizzaImageStretch = pygame.transform.scale(pizzaImage, (x2, y2))

for i in range(15):
    fpizza.append(pygame.Rect(random.randint(0, 580), random.randint(0, 580), 30, 30))

if (len(fpizza)) < maxpizza:
    fpizza.append(pizzaImageStretch)

while True:

    windowSurface.fill(white)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if event.type == KEYDOWN:
        if event.key == K_UP or event.key == K_w:
            moveUp = True
        if event.key == K_DOWN or event.key == K_s:
            moveDown = True
        if event.key == K_LEFT or event.key == K_a:
            moveLeft = True
        if event.key == K_RIGHT or event.key == K_d:
            moveRight = True
        if event.key == K_SPACE:
            grow = True
        if event.key == K_z:
            shrink = True
        if event.key == K_t:
            growp == True
        if event.key == K_g:
            shrinkp == True
    if event.type == KEYUP:
        if event.key == K_UP or event.key == K_w:
            moveUp = False
        if event.key == K_DOWN or event.key == K_s:
            moveDown = False
        if event.key == K_LEFT or event.key == K_a:
            moveLeft = False
        if event.key == K_RIGHT or event.key == K_d:
            moveRight = False
        if event.key == K_SPACE:
            grow = False
        if event.key == K_z:
            shrink = False
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
    if player.left <= 0:
        player.left += 10
    if player.top <= 0:
        player.top += 10
    if player.bottom >= 600:
        player.bottom -= 10
    if player.right >= 600:
        player.right -= 10
    if moveUp == True:
        player.top -= movementSpeed
        if left == True:
            playerImageStretch = pygame.transform.rotate(playerImageStretch, -90)
            left = False
        if right == True:
            playerImageStretch = pygame.transform.rotate(playerImageStretch, 90)
            right = False
        if down == True:
            playerImageStretch = pygame.transform.flip(playerImageStretch, False, True)
            down = False
        up = True

    if moveDown == True:
        player.top += movementSpeed
        if left == True:
            playerImageStretch = pygame.transform.rotate(playerImageStretch, 90)
            left = False
        if right == True:
            playerImageStretch = pygame.transform.rotate(playerImageStretch, -90)
            right = False
        if up == True:
            playerImageStretch = pygame.transform.flip(playerImageStretch, False, True)
            up = False
        down = True

    if moveLeft == True:
        player.left -= movementSpeed
        if right == True:
            playerImageStretch = pygame.transform.rotate(playerImageStretch, 180)
            right = False
        if up == True:
            playerImageStretch = pygame.transform.rotate(playerImageStretch, 90)
            up = False
        if down == True:
            playerImageStretch = pygame.transform.rotate(playerImageStretch, -90)
            down = False
        left = True
    if moveRight == True:
        player.right += movementSpeed
        if left == True:
            playerImageStretch = pygame.transform.rotate(playerImageStretch, 180)
            left = False
        if up == True:
            playerImageStretch = pygame.transform.rotate(playerImageStretch, -90)
            up = False
        if down == True:
            playerImageStretch = pygame.transform.rotate(playerImageStretch, 90)
            down = False
        right = True

    if x == pizzaImageStretch and y == pizzaImageStretch:
        score += 1

    for slice in fpizza:
        if player.colliderect(slice):
            fpizza.remove(slice)
            score += 1

    if grow == True:
        x += 1
        y += 1
    if shrink == True:
        x -= 1
        y -= 1
    if  growp == True:
        x2 += 1
        y2 += 1
    if shrinkp == True:
        x2 -= 1
        y2 -= 1



    font = pygame.font.SysFont("none", 24)
    scoreText = "Score: " + str(score)
    text2 = font.render(scoreText, True, blue)
    windowSurface.blit(text2, (width - 100, 0))

    windowSurface.blit(playerImageStretch, player)
    for slice in fpizza:
        windowSurface.blit(pizzaImageStretch, slice)

    pygame.display.update()
    mainClock.tick(180)