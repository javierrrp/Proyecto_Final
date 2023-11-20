import pygame
from pygame.sprite import Sprite
import random as ra

class Animal(Sprite):
    def __init__(self, vida, energia, velocidad, dieta, especies):
        super().__init__()
        self.vida = vida
        self.energia = energia
        self.velocidad = velocidad
        self.dieta = dieta
        self.especies = especies

class Leon(Animal):
    def __init__(self, vida, energia, velocidad, dieta, especies):
        super().__init__(vida, energia, velocidad, dieta, especies)
        # Atributos específicos del león
        self.image = pygame.image.load("Animales/leon.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 100  
        self.rect.y = 100 
        self.speed = 1  
        self.direction = ra.choice(["up", "down", "left", "right"])  
        self.subx = 0
        self.suby = 0
        self.subpix = 3

    def update(self):
        # Método de actualización específico del león
        if self.direction == "up":
            self.suby -= self.speed
        elif self.direction == "down":
            self.suby += self.speed
        elif self.direction == "left":
            self.subx -= self.speed
        elif self.direction == "right":
            self.subx += self.speed
    
        self.rect.x = round(self.subx / self.subpix)
        self.rect.y = round(self.suby / self.subpix)

class Cebra(Animal):
    def __init__(self, vida, energia, velocidad, dieta, especies):
        super().__init__(vida, energia, velocidad, dieta, especies)
        self.image = pygame.image.load("Animales/cebra.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 100  
        self.rect.y = 100 
        self.speed = 1  
        self.direction = ra.choice(["up", "down", "left", "right"])  
        self.subx = 0
        self.suby = 0
        self.subpix = 3
        self.dieta = dieta
        self.especies = especies

    def update(self):
        # Método de actualización específico del león
        if self.direction == "up":
            self.suby -= self.speed
        elif self.direction == "down":
            self.suby += self.speed
        elif self.direction == "left":
            self.subx -= self.speed
        elif self.direction == "right":
            self.subx += self.speed
    
        self.rect.x = round(self.subx / self.subpix)
        self.rect.y = round(self.suby / self.subpix)


    