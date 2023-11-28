import pygame
from pygame.sprite import Sprite
import random as ra
import time
from organismo import Organismo


class Planta(Organismo):
    def __init__(self, posicionx, posiciony, vida, energia):
        super().__init__(posicionx, posiciony, vida, energia)
    
    def fotosintesis(self):
        pass
    def reproduccion(self):
        pass


class Planta1(Planta):
    def __init__(self, posicionx, posiciony, vida, energia):
        super().__init__(posicionx, posiciony, vida, energia)
        self.image = pygame.image.load("Planta/d2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = posicionx
        self.rect.y = posiciony

class Planta2(Planta):
    def __init__(self, posicionx, posiciony, vida, energia):
        super().__init__(posicionx, posiciony, vida, energia)
        self.image = pygame.image.load("Planta/d.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = posicionx
        self.rect.y = posiciony