import pygame, sys
from pygame.locals import *
from pygame.sprite import Sprite
import random as ra
import time


class Organismo(Sprite):
    def __init__(self, posicionx, posiciony, vida, energia):
        super().__init__()
        self.posicionx = posicionx
        self.posiciony = posiciony
        self.vida = vida
        self.energia = energia