import area
import pygame

class Picture(area.Area):
    def __init__(self,mw, filename, x=0, y=0, width=10, height=10):
        area.Area.__init__(self,mw, x=x, y=y, width=width, height=height, color=(135,248,255))
        self.image = pygame.image.load(filename)
    
    def draw(self):
        self.mw.blit(self.image, (self.rect.x, self.rect.y))