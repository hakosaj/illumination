import pygame
import math


class Ball:



    def __init__(self,ballRadius):
        self.x=100
        self.y=100
        self.xv=0.1
        self.yv=1
        self.radius=5
        self.circ=pygame.Rect(self.x,self.y,self.radius,self.radius)

    def centerX(self):
        return self.x+0.5*self.radius

    def centerY(self):
        return self.y+0.5*self.radius



    def draw_ball(self,screen):
        self.circ=pygame.Rect(self.x,self.y,self.radius,self.radius)
        pygame.draw.circle(screen,pygame.Color(0,0,0),(round(self.x),round(self.y)),self.radius+2)
        pygame.draw.circle(screen,pygame.Color(255,0,0),(round(self.x),round(self.y)),self.radius)


    def move_ball(self,width):
        #if (self.y-self.radius>0 and self.y+self.radius+<height-60):
        if (self.y-self.radius>0):
            self.y+=self.yv
        else:
            self.yv=-self.yv
            self.y+=self.yv

        if (self.x-self.radius>0 and self.x+self.radius<width):
            self.x+=self.xv
        else:
            self.xv=-self.xv
            self.x+=self.xv

        