import sys
import os
import random
import time
import pygame
import math
from pygame.locals import *
from ball import Ball
from wall import Wall




#Initialize pygame
pygame.init()
pygame.font.init()
#Fonts and gavkground
scorefont = pygame.font.SysFont('Comic Sans MS',40)
gameoverfont = pygame.font.SysFont('Comic Sans MS',40)
algofont = pygame.font.SysFont('Arial',20)

ball=Ball(10)

wall =Wall(120,[150,150])


screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Illumination")

start_time = None
clock = pygame.time.Clock ()
tickcounter=0

while True:

    screen.fill(pygame.Color(200,200,200))

    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    wall.draw_wall(screen)
    ball.draw_ball(screen)
    ball.move_ball(400);


    tickcounter+=1
    pygame.display.flip()
    clock.tick(30)




