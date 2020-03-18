
import pygame
import math


class Ray:



    def __init__(self,x,y,orientation):
        self.x=x
        self.y=y
        self.vel=1
        self.xv=self.vel*math.cos(orientation)
        self.yv=self.vel*math.sin(orientation)
        self.raySegments=[]




    #line(surface,color,startpos,endpos)
    def draw_ray(self,screen):
        self.raySegments.append([(self.x,self.y),(self.x+self.xv,self.y+self.yv)])
        self.x+=self.xv
        self.y+=self.yv
        for item in self.raySegments:
            pygame.draw.line(screen,(0,0,0),item[0],item[1],3)



        

        