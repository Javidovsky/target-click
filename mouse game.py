import math
import pygame
from pygame import mixer
import random

# initialise
pygame.init()

# screen
screen = pygame.display.set_mode((1600, 900))

# sound
hitnoise = mixer.Sound("./assets/hit.mp3")

# title background logo stuff
pygame.display.set_caption("mouse click game")
icon = pygame.image.load("./assets/target.png")
pygame.display.set_icon(icon)

ground = pygame.image.load("./assets/widetallground.png")

def floor():
    screen.blit(ground, (0, 800))

# target
targetImg = pygame.image.load("./assets/target.png")
targetx = 100
targety = 100
newtargetx = 0
newtargety = 0

def target(x, y):
    screen.blit(targetImg, (x, y))

def checkcollision(object1xpos, object1ypos, object1xlength, object1ylength, object2xpos, object2ypos, object2xlength, object2ylength):
    rect1 = pygame.Rect(object1xpos, object1ypos, object1xlength, object1ylength)
    rect2 = pygame.Rect(object2xpos, object2ypos, object2xlength, object2ylength)
    if rect1.colliderect(rect2):
        return True

def checkcollisionwithmouse(objectposx, objectposy, objectlengthx, objectlengthy):
    mousex, mousey = pygame.mouse.get_pos()
    if objectlengthx >= mousex - objectposx >= 0 and objectlengthy >= mousey - objectposy >= 0:
        return True

# score
scorevalue = 0
font = pygame.font.Font("freesansbold.ttf",32)

def showscore(x, y):
    score = font.render("Score: " + str(scorevalue), True, (255,255,255))
    screen.blit(score, (x,y))

def showlastscore(x, y):
    score = font.render("Last score: " + str(scorevalue), True, (255,255,255))
    screen.blit(score, (x,y))

# timer
timervalue = 0
timertextx = 700
timertexty = 10

lastsec = 0

def showtimer(x, y):
    timer = font.render("Timer: " + str(15 - timervalue), True, (255,255,255))
    screen.blit(timer, (x,y))

# title screen
titleImg = pygame.image.load("./assets/titlescreen.png")

def titlescreen(x, y):
    screen.blit(titleImg, (x, y))

# misc
start_ticks = pygame.time.get_ticks()

running = True
menu = True
game = True
while running:
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                menu = False
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and checkcollisionwithmouse(targetx, targety, 64, 64):
                scorevalue = 0
                hitnoise.play()
                targetx = random.randint(50, 1500)
                targety = random.randint(50, 600)
                game = True
                menu = False
        # rgb
        screen.fill((113, 196, 210))
        # floor
        floor()
        # target
        targetx = 768
        targety = 368
        target(targetx, targety)
        #score
        showlastscore(10, 10)
        lastsec = 0
        timervalue = 0
        start_ticks = pygame.time.get_ticks()
        # titlescreen
        titlescreen(0, 0)
        # update
        pygame.display.update()
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                menu = False
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and checkcollisionwithmouse(targetx, targety, 64, 64):
                hitnoise.play()
                scorevalue += 1
                targetx = random.randint(50, 1500)
                targety = random.randint(50, 600)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu = True
                    game = False
        # rgb
        screen.fill((113, 196, 210))
        # floor
        floor()
        # target
        target(targetx,targety)
        # score
        showscore(10, 10)
        # timer
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        if seconds > 15:
            game = False
            menu = True
        if seconds - lastsec >= 1:
            lastsec += 1
            timervalue += 1
        showtimer(650, 10)
        # update
        pygame.display.update()
