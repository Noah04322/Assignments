import pygame, sys, time, random
from pygame.locals import *
pygame.init()
mainClock = pygame.time.Clock()

lives = 3
lives2 = 3

width = 800
height = 600
windowSurface = pygame.display.set_mode((width, height), 0, 32)

pygame.display.set_caption('Star Wars!')

movementSpeed = 10
projectileSpeed = 30
scrollSpeed = 6
iambecomespeed = 200

shotFrameCounter = 0
targetFrameCounter = 0
collisionFrameCounter = 0

shots = []
shots2 = []
targets = []
lifeblocks = []
nopain = []
death = []


maxLives = 3
score = 0

maxTargets = 5
lifes = 4
maxShots = 3
Finvincible = 1
iambecome = 1

moveLeft = False
moveLeft2 = False
moveRight = False
moveRight2 = False

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

x = 48
y = 48
t = 40

player = pygame.Rect(273, 20, x, t)
player2 = pygame.Rect(273, 530, x, t)

bg = pygame.Rect(0, -100, 10, 10)
shoot = False
shoot2 = False

background = pygame.image.load('Resources/Images/StarsPattern.png')
Da_Ship = pygame.image.load('Resources/Images/marrio.jpeg')
SS_Falcon = pygame.image.load('Resources/Images/SS Falcon.png').convert()
Rover = pygame.image.load('Resources/Images/World.png').convert()
The_World = pygame.image.load('Resources/Images/tuskc.png').convert()
pew = pygame.mixer.Sound('Resources/Audio/Gun+1.wav')
pew2 = pygame.mixer.Sound('Resources/Audio/Gun+Shot2.wav')
boom = pygame.mixer.Sound('Resources/Audio/Explosion+1.wav')
boom7 = pygame.mixer.Sound('Resources/Audio/boom7.wav')
space = pygame.mixer.music.load('Resources/Audio/Space Fighter Loop.mp3')

DASHIP = pygame.transform.scale(Da_Ship, (x, y))
FALCON = pygame.transform.scale(SS_Falcon, (x ,y))
ROVER = pygame.transform.scale(Rover, (x,y))
THE_WORLD = pygame.transform.scale(The_World, (x,y))

mcounter = 1
mouset = True
yellowrect = pygame.draw.rect(windowSurface, yellow, (400, 550, 30, 30))
greenRect = pygame.draw.rect(windowSurface, green, (250, 10, 500, 300))
titleFont = pygame.font.SysFont("none", 60)
myText = "Welcome to Space War! Here are the rules:"
text = titleFont.render(myText, True, black)

def end(lives,lives2):
    while True:
        windowSurface.fill(black)
        windowSurface.blit(background, bg)
        bg.left -= scrollSpeed
        if bg.left < -800:
            bg.left = 0
        pygame.display.update()
        if lives <= 0:
            font = pygame.font.SysFont("none", 24)
            scoreText = ("Player 2 WINS!")
            text2 = font.render(scoreText, True, white)
            windowSurface.blit(text2, (10, 10))
            thatRect = pygame.draw.rect(windowSurface, green, (50, 300, 390, 100))
            myText = "End Game?"

            thisRect = pygame.draw.rect(windowSurface, green, (50, 450, 390, 100))
            myText2 = "New Game?"

            text = titleFont.render(myText, True, black)
            textRect = text.get_rect()
            textRect.centerx = thatRect.centerx
            textRect.centery = thatRect.centery
            windowSurface.blit(text, textRect)

            text2 = titleFont.render(myText2, True, black)
            textRect2 = text.get_rect()
            textRect2.centerx = thisRect.centerx
            textRect2.centery = thisRect.centery
            windowSurface.blit(text2, textRect2)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.pos[0] >= thatRect.left and event.pos[0] <= thatRect.right and event.pos[
                        1] >= thatRect.top and \
                            event.pos[1] <= thatRect.bottom:
                        print("endgame selected!")
                        pygame.quit()
                        sys.exit()

                if event.type == MOUSEBUTTONDOWN:
                    if event.pos[0] >= thisRect.left and event.pos[0] <= thisRect.right and event.pos[
                        1] >= thisRect.top and \
                            event.pos[1] <= thisRect.bottom:
                        pygame.mixer.music.unpause()
                        print("newgame selected")
                        startgame()
                        chooseship()

                if event.type == QUIT:
                    print("quit selected!")
                    pygame.quit()
                    sys.exit()

        if lives2 <= 0:
            font = pygame.font.SysFont("none", 24)
            scoreText = ("Player 1 WINS!")
            text2 = font.render(scoreText, True, white)
            windowSurface.blit(text2, (10, 10))
            thatRect = pygame.draw.rect(windowSurface, green, (50, 300, 390, 100))
            myText = "End Game?"

            thisRect = pygame.draw.rect(windowSurface, green, (50, 450, 390, 100))
            myText2 = "New Game?"

            text = titleFont.render(myText, True, black)
            textRect = text.get_rect()
            textRect.centerx = thatRect.centerx
            textRect.centery = thatRect.centery
            windowSurface.blit(text, textRect)

            text2 = titleFont.render(myText2, True, black)
            textRect2 = text.get_rect()
            textRect2.centerx = thisRect.centerx
            textRect2.centery = thisRect.centery
            windowSurface.blit(text2, textRect2)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.pos[0] >= thatRect.left and event.pos[0] <= thatRect.right and event.pos[
                        1] >= thatRect.top and \
                            event.pos[1] <= thatRect.bottom:
                        print("endgame selected!")
                        pygame.quit()
                        sys.exit()

                if event.type == MOUSEBUTTONDOWN:
                    if event.pos[0] >= thisRect.left and event.pos[0] <= thisRect.right and event.pos[
                        1] >= thisRect.top and \
                            event.pos[1] <= thisRect.bottom:
                        pygame.mixer.music.unpause()
                        print("newgame selected")
                        startgame()
                        chooseship()

                if event.type == QUIT:
                    print("quit selected!")
                    pygame.quit()
                    sys.exit()
                pygame.display.update()

def chooseship():
    shotFrameCounter = 0
    targetFrameCounter = 0
    collisionFrameCounter = 0

    shots = []
    shots2 = []
    targets = []
    lifeblocks = []
    nopain = []
    death = []

    maxLives = 3
    score = 0

    maxTargets = 5
    lifes = 4
    maxShots = 3
    Finvincible = 1
    iambecome = 1

    moveLeft = False
    moveLeft2 = False
    moveRight = False
    moveRight2 = False

    x = 48
    y = 54

    player = pygame.Rect(273, 20, x, y)
    player2 = pygame.Rect(273, 530, x, y)

    bg = pygame.Rect(0, -100, 10, 10)
    shoot = False
    shoot2 = False

    lives = 3
    lives2 = 3

    mcounter = 1
    safe = 0
    safe2 = 0
    mouset = True
    while mouset:
        windowSurface.fill(black)
        windowSurface.blit(background, bg)
        bg.left -= scrollSpeed
        if bg.left < -800:
            bg.left = 0
        blueRect = pygame.draw.rect(windowSurface, blue, (200, 100, 60, 60))
        redRect = pygame.draw.rect(windowSurface, red, (200, 300, 60, 60))
        greenRect = pygame.draw.rect(windowSurface, green, (400, 100, 60, 60))
        whiteRect = pygame.draw.rect(windowSurface, white, (400, 300, 60, 60))
        firstship = "The World"
        secondship = "Rover"
        thirdship = "Inevitability"
        fourthship = "Falcon"
        daFont = pygame.font.SysFont("none", 20)
        hrship = daFont.render(firstship, True, blue)
        windowSurface.blit(hrship, (200, 170))
        rhship = daFont.render(secondship, True, red)
        windowSurface.blit(rhship, (200, 370))
        ssship = daFont.render(thirdship, True, green)
        windowSurface.blit(ssship, (400, 170))
        tship = daFont.render(fourthship, True, white)
        windowSurface.blit(tship, (400, 370))

        windowSurface.blit(THE_WORLD, blueRect)
        windowSurface.blit(ROVER, redRect)
        windowSurface.blit(DASHIP, greenRect)
        windowSurface.blit(FALCON, whiteRect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.pos[0] >= greenRect.left and event.pos[0] <= greenRect.right and event.pos[
                    1] >= greenRect.top and event.pos[1] <= greenRect.bottom:
                    if mcounter == 2:
                        ship2 = DASHIP
                        shipname = ("daship")
                        mouset = False
                if event.pos[0] >= blueRect.left and event.pos[0] <= blueRect.right and event.pos[1] >= blueRect.top and \
                        event.pos[1] <= blueRect.bottom:
                    if mcounter == 2:
                        ship2 = THE_WORLD
                        shipname = ("world")
                        mouset = False
                if event.pos[0] >= redRect.left and event.pos[0] <= redRect.right and event.pos[1] >= redRect.top and \
                        event.pos[1] <= redRect.bottom:
                    if mcounter == 2:
                        ship2 = ROVER
                        shipname = ("Rover")
                        mouset = False
                if event.pos[0] >= whiteRect.left and event.pos[0] <= whiteRect.right and event.pos[
                    1] >= whiteRect.top and \
                        event.pos[1] <= whiteRect.bottom:
                    if mcounter == 2:
                        ship2 = FALCON
                        shipname = ("Falcon")
                        mouset = False
            if event.type == MOUSEBUTTONDOWN:
                if event.pos[0] >= greenRect.left and event.pos[0] <= greenRect.right and event.pos[
                    1] >= greenRect.top and event.pos[1] <= greenRect.bottom:
                    if mcounter == 1:
                        ship1 = DASHIP
                        shipname = ("daship")
                        mcounter = 2
                if event.pos[0] >= blueRect.left and event.pos[0] <= blueRect.right and event.pos[1] >= blueRect.top and \
                        event.pos[1] <= blueRect.bottom:
                    if mcounter == 1:
                        ship1 = THE_WORLD
                        shipname = ("mworld")
                        mcounter = 2
                if event.pos[0] >= redRect.left and event.pos[0] <= redRect.right and event.pos[1] >= redRect.top and \
                        event.pos[1] <= redRect.bottom:
                    if mcounter == 1:
                        ship1 = ROVER
                        shipname = ("Rover")
                        mcounter = 2
                if event.pos[0] >= whiteRect.left and event.pos[0] <= whiteRect.right and event.pos[
                    1] >= whiteRect.top and \
                        event.pos[1] <= whiteRect.bottom:
                    if mcounter == 1:
                        ship1 = FALCON
                        shipname = ("Falcon")
                        mcounter = 2

    ship1 = pygame.transform.rotate(ship1, 180)

    great = True
    while great:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    moveLeft = True
                if event.key == K_RIGHT:
                    moveRight = True
                if event.key == K_p:
                    shoot = True
                    pew2.play()
                if event.key == K_a:
                    moveLeft2 = True
                if event.key == K_d:
                    moveRight2 = True
                if event.key == K_SPACE:
                    shoot2 = True
                    pew.play()
            if event.type == KEYUP:
                if event.key == K_LEFT:
                    moveLeft = False
                if event.key == K_RIGHT:
                    moveRight = False
                if event.key == K_p:
                    shoot = False
                if event.key == K_a:
                    moveLeft2 = False
                if event.key == K_d:
                    moveRight2 = False
                if event.key == K_SPACE:
                    shoot2 = False
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        if moveLeft2 == True:
            if player2.left > 0:
                player2.left -= movementSpeed
        if moveRight2 == True:
            if player2.right < width:
                player2.right += movementSpeed
        if moveLeft == True:
            if player.left > 0:
                player.left -= movementSpeed
        if moveRight == True:
            if player.right < width:
                player.right += movementSpeed
        windowSurface.fill(black)
        windowSurface.blit(background, bg)
        bg.left -= scrollSpeed
        if bg.left < -800:
            bg.left = 0
        windowSurface.blit(ship1, player)
        windowSurface.blit(ship2, player2)
        for target in targets[:]:
            if target.left < - 20:
                targets.remove(target)
        for life in lifeblocks[:]:
            if life.left < - 20:
                lifeblocks.remove(life)
        for invincible in nopain[:]:
            if invincible.left < - 20:
                nopain.remove(invincible)
        for dead in death[:]:
            if dead.left < -20:
                death.remove(dead)

        if shoot == True and (len(shots) < maxShots):
            shots.append(pygame.Rect(player.centerx - 3, player.centery - 3, 6, 6))
        for i in range(len(shots)):
            pygame.draw.rect(windowSurface, green, shots[i])
            shots[i].bottom += projectileSpeed
            if shots[i].colliderect(player2):
                lives2 -= 1
                shots[i].top = 600
                boom7.play()
            for target in targets[:]:
                if shots[i].colliderect(target):
                    targets.remove(target)
                    lives -= 1
                    shots[i].top = 600
                    boom.play()
            for life in lifeblocks[:]:
                if shots[i].colliderect(life):
                    lifeblocks.remove(life)
                    lives += 1
                    shots[i].top = 600
                    boom.play()
            for invincible in nopain[:]:
                if shots[i].colliderect(invincible):
                    nopain.remove(invincible)
                    if safe == 0:
                        safe = 30
                        maxLives -= 1
            for dead in death[:]:
                if shots[i].colliderect(dead):
                    lives2 = 1
                    shots[i].top = 600
                    boom.play()
            if safe > 0:
                if safe % 3 == 0:
                    boom.play()
                    ship1.set_alpha(255)
                    safe -= 1
                else:
                    ship1.set_alpha(0)
            else:
                ship1.set_alpha(255)


        if shoot2 == True and (len(shots2) < maxShots):
            shots2.append(pygame.Rect(player2.centerx - 3, player2.centery - 3, 6, 6))
        for i in range(len(shots2)):
            pygame.draw.rect(windowSurface, red, shots2[i])
            shots2[i].bottom -= projectileSpeed
            if shots2[i].colliderect(player):
                lives -= 1
                boom7.play()
            for target in targets[:]:
                if shots2[i].colliderect(target):
                    targets.remove(target)
                    lives2 -= 1
                    shots2[i].bottom = 0
            for life in lifeblocks[:]:
                if shots2[i].colliderect(life):
                    lifeblocks.remove(life)
                    lives2 += 1
                    shots2[i].bottom = 0
            for invincible in nopain[:]:
                if shots2[i].colliderect(invincible):
                    invincible.left = -10
                    if safe2 == 0:
                        safe2 = 30
            for dead in death[:]:
                if shots2[i].colliderect(dead):
                    lives = 1
                    shots2[i].bottom = 0
            if safe2 > 0:
                if safe2 % 3 == 0:
                    boom.play()
                    ship2.set_alpha(255)
                    safe2 -= 1
                else:
                    ship2.set_alpha(0)
            else:
                ship2.set_alpha(255)

        for shot in shots[:]:
            if shot.top > 620:
                shots.remove(shot)
        for shot in shots[:]:
            if shot.colliderect(player2):
                shot.top = 600

        for shot2 in shots2[:]:
            if shot2.bottom < 0:
                shots2.remove(shot2)
        for shot2 in shots2[:]:
            if shot2.colliderect(player):
                shot2.bottom = 0

        z = random.randint(0, 23)
        if z == 4:
            if len(targets) < maxTargets:
                targets.append(pygame.Rect(width + 20, random.randint(100, height - 100), 40, 20))
        if z == 13:
            if len(lifeblocks) < lifes:
                lifeblocks.append(pygame.Rect(width + 20, random.randint(100, height - 100), 40, 20))
        if z == 5:
            if len(nopain) < Finvincible:
                nopain.append(pygame.Rect(width + 20, random.randint(100, height - 100), 40, 20))
        if z == 1:
            if len(death) < iambecome:
                death.append(pygame.Rect(width + 20, random.randint(100, height - 100), 40, 20))

        for i in range(len(targets)):
            pygame.draw.rect(windowSurface, red, targets[i])
            targets[i].left -= movementSpeed
        for i in range(len(lifeblocks)):
            pygame.draw.rect(windowSurface, blue, lifeblocks[i])
            lifeblocks[i].left -= movementSpeed
        for i in range(len(nopain)):
            pygame.draw.rect(windowSurface, black, nopain[i])
            nopain[i].left -= movementSpeed
        for i in range(len(death)):
            pygame.draw.rect(windowSurface, white, death[i])
            death[i].left -= iambecomespeed

        font = pygame.font.SysFont("none", 20)
        scoreText = "Lives: " + str(lives)
        text2 = font.render(scoreText, True, green)
        windowSurface.blit(text2, (10, 10))

        font = pygame.font.SysFont("none", 20)
        scoreText = "Lives: " + str(lives2)
        text3 = font.render(scoreText, True, red)
        windowSurface.blit(text3, (750, 560))

        pygame.display.update()
        mainClock.tick(60)
        if safe > 0:
            safe -= 1
        if safe2 > 0:
            safe2 -= 1
        if lives <= 0 or lives2 <= 0:
            end(lives,lives2)
def playmusic():
    v = .1
    pygame.mixer.music.load('Resources/Audio/Space Fighter Loop.mp3')
    pygame.mixer.music.play(-1, 0)
    pygame.mixer.music.set_volume(v)

def startgame():
    game = True
    realgame = False
    while game:
        windowSurface.fill(black)
        windowSurface.blit(background, bg)
        bg.left -= scrollSpeed
        if bg.left < -800:
            bg.left = 0
        greenRect = pygame.draw.rect(windowSurface, green, (200, 250, 390, 100))
        titleFont = pygame.font.SysFont("none", 90)
        myText = "Start game?"
        text = titleFont.render(myText, True, black)
        textRect = text.get_rect()
        textRect.centerx = windowSurface.get_rect().centerx
        textRect.centery = windowSurface.get_rect().centery
        windowSurface.blit(text, textRect)
        bigFont = pygame.font.SysFont("none", 100)
        Spacewar = "SPACE WAR"
        text3 = bigFont.render(Spacewar, True, red)
        windowSurface.blit(text3, (200, 100))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.pos[0] >= greenRect.left and event.pos[0] <= greenRect.right and event.pos[1] >= greenRect.top and event.pos[1] <= greenRect.bottom:
                    playmusic()
                tules = True
                while tules:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == MOUSEBUTTONDOWN:
                            if event.pos[0] >= yellowrect.left and event.pos[0] <= yellowrect.right and event.pos[
                                1] >= yellowrect.top and \
                                    event.pos[1] <= yellowrect.bottom:
                                chooseship()
                        pygame.display.update()
                    windowSurface.fill(black)
                    windowSurface.blit(background, bg)
                    bg.left -= scrollSpeed
                    if bg.left < -800:
                        bg.left = 0
                    yellowrect = pygame.draw.rect(windowSurface, yellow, (400, 550, 30, 30))
                    greenRect = pygame.draw.rect(windowSurface, green, (30, 10, 720, 40))
                    redrect = pygame.draw.rect(windowSurface, red, (60, 150, 70, 40))
                    bluerect = pygame.draw.rect(windowSurface, blue, (60, 220, 70, 40))
                    blackrect = pygame.draw.rect(windowSurface, black, (60, 290, 70, 40))
                    whiterect = pygame.draw.rect(windowSurface, white, (60, 360, 70, 40))
                    rulered = "if you hit the red rectangle, you lose a life"
                    ruleblue = "if you hit the blue rectangle, you get a life"
                    ruleblack = "if you hit the black rectangle, you are invisible (but it itself is basically invisible) until you shoot"
                    rulewhite = " if you hit the white rectangle, the other character gets their lives reduced to one life(you can try to hit it, anyway.)"
                    titleFont = pygame.font.SysFont("none", 50)
                    myText = "Welcome to Space War! Here are the rules:"
                    text = titleFont.render(myText, True, black)
                    Start = "READY? PRESS THE YELLOW BUTTON!"
                    text3 = titleFont.render(Start, True, blue)
                    windowSurface.blit(text3, (75, 500))
                    windowSurface.blit(text, greenRect)
                    littleFont = pygame.font.SysFont("none", 20)
                    tusk = pygame.font.SysFont("none", 18)
                    text4 = littleFont.render(rulered, True, red)
                    windowSurface.blit(text4, (160, 150))
                    text5 = littleFont.render(ruleblue, True, blue)
                    windowSurface.blit(text5, (160, 220))
                    text6 = littleFont.render(ruleblack, True, white)
                    windowSurface.blit(text6, (160, 290))
                    text7 = tusk.render(rulewhite, True, white)
                    windowSurface.blit(text7, (160, 360))
                    pygame.display.update()
        pygame.display.update()
startgame()





