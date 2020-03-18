import pygame
import math


class Wall:


    def __init__(self, wallSize, wallPosition):
        self.size=wallSize
        self.x=wallPosition[0]
        self.y=wallPosition[1]
        self.circ=pygame.Rect(self.x,self.y,self.size,self.size)
        self.collidecirc = pygame.Rect(self.x,self.y,self.size+4,self.size+4)



    
    def draw_wall(self,screen):
        self.circ=pygame.Rect(self.x,self.y,self.size,self.size)
        pygame.draw.circle(screen,pygame.Color(0,0,0),(round(self.x),round(self.y)),self.size+4)
        pygame.draw.circle(screen,pygame.Color(200,200,200),(round(self.x),round(self.y)),self.size)
