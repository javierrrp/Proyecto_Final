import pygame, sys
from pygame.locals import *
from pygame.sprite import Sprite
import random as ra
import time


class Organismo(Sprite):
    def __init__(self, posicionx=0, posiciony=0, vida=100, energia=50):
        super().__init__()
        self.posicionx = posicionx
        self.posiciony = posiciony
        self.vida = vida
        self.energia = energia