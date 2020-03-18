import sys
import os
import random
import time
import pygame
import math
from pygame.locals import *
from wall import Wall
from ray import Ray




#Initialize pygame
pygame.init()
pygame.font.init()
#Fonts and gavkground
scorefont = pygame.font.SysFont('Comic Sans MS',40)
gameoverfont = pygame.font.SysFont('Comic Sans MS',40)
algofont = pygame.font.SysFont('Arial',20)


ray1 = Ray(150,150,0)
ray2 = Ray(150,150,math.pi/2)
ray3 = Ray(150,150,math.pi)
ray4 = Ray(150,150,math.pi*3/2)
rays=[ray1,ray2,ray3,ray4]

wall =Wall(120,[140,140])


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
    for item in rays:
        item.draw_ray(screen)
        

        #If collides with collidecirc but not wall.circ: reflect

    tickcounter+=1
    pygame.display.flip()
    clock.tick(30)




