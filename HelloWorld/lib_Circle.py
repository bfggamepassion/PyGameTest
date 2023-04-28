import pygame

class Cercle:
    def __init__(self, x, y, radius,r ,g, b):
        self.x = x
        self.y = y
        self.radius = radius
        self.r = r
        self.g = g
        self.b = b
    
    def show(self,screen):
        pygame.draw.circle(screen, (self.r,self.g,self.b), (self.x, self.y), self.radius)
        