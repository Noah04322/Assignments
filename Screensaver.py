import pygame, sys, time
from pygame.locals import *
import random

pygame.init()


width = 600
height = 600
windowSurface = pygame.display.set_mode((width, height), 0, 32)

pygame.display.set_caption('ScreenSaver')

up = 'up'
down = 'down'
left = 'left'
right = 'right'

downLeft = 'downleft'
downRight = 'downright'
upLeft = 'upleft'
upRight = 'upright'

movementSpeed = 10

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
windowSurface.fill(white)

colors = [black, white, red, green, blue]

redRect = {'rect':pygame.Rect(230, 120, 50, 50), 'color': blue , 'dir':downRight}

dabox = [redRect]
x = 30

while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


        windowSurface.fill(white)

        for b in dabox:
            if b['dir'] == downLeft:
                b['rect'].left -= movementSpeed
                b['rect'].top += movementSpeed
            if b['dir'] == downRight:
                b['rect'].left += movementSpeed
                b['rect'].top += movementSpeed
            if b['dir'] == upLeft:
                b['rect'].left -= movementSpeed
                b['rect'].top -= movementSpeed
            if b['dir'] == upRight:
                b['rect'].left += movementSpeed
                b['rect'].top -= movementSpeed


            if b['rect'].right > width:
                b['color'] = (random.randint(0,255), random.randint(0,255),random.randint(0,255))
                if b['dir'] == upRight:
                    b['dir'] = downLeft
                if b['dir'] == downRight:
                    b['dir'] = upLeft

            if b['rect'].bottom > height:
                b['color'] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                if b['dir'] == downLeft:
                    b['dir'] = upRight
                if b['dir'] == downRight:
                    b['dir'] = upLeft

            if b['rect'].top < 0:
                b['color'] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                if b['dir'] == upLeft:
                    b['dir'] = downLeft
                if b['dir'] == upRight:
                    b['dir'] = downRight

            if b['rect'].left < 0:
                b['color'] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
                if b['dir'] == downLeft:
                    b['dir'] = downRight
                if b['dir'] == upLeft:
                    b['dir'] = upRight

            pygame.draw.rect(windowSurface, b['color'], b['rect'])

        pygame.display.update()
        time.sleep(.01)





