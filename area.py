import pygame
class Area():
    def __init__(self,mw, x=0, y=0, width=10, height=10, color=(135,248,255)):
        """ область: прямоугольник в нужном месте и нужного цвета """
        #запоминаем прямоугольник:
        self.rect = pygame.Rect(x, y, width, height)
        #цвет заливки - или переданный параметр, или общий цвет фона
        self.fill_color = color
        self.mw = mw
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(self.mw, self.fill_color, self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)      
    def colliderect(self, rect):
        return self.rect.colliderect(rect)