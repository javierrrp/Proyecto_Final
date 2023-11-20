import pygame
from pygame.sprite import Sprite
import random as ra
import time

class Animal(Sprite):
    def __init__(self, vida, energia, dieta, especies):
        super().__init__()
        self.vida = vida
        self.energia = energia
        self.dieta = dieta
        self.especies = especies

class Leon(Animal):
    def __init__(self, vida, energia, velocidad, dieta, especies):
        super().__init__(vida, energia, dieta, especies)
        self.image = pygame.image.load("Animales/leon.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.speed = 1
        self.subx = 0
        self.suby = 0
        self.subpix = 6
        self.rango = ra.randint(0, 500)
        self.direction = None  # Agrega una dirección inicial

    def update(self):
        self.rango -= 1
        if self.rango < 0:
            self.rango = ra.randint(0, 500)
            direction = ra.randint(1, 4)
            if direction == 1:
                self.direction = "up" # Actualiza la dirección en self.direction
            elif direction == 2:
                self.direction = "down"
            elif direction == 3:
                self.direction = "left"
            elif direction == 4:
                self.direction = "right"

        if self.direction == "up" and self.rect.y > 0:
            self.suby -= self.speed
        elif self.direction == "down" and self.rect.y < 600 - self.rect.height:
            self.suby += self.speed
        elif self.direction == "left" and self.rect.x > 0:
            self.subx -= self.speed
        elif self.direction == "right" and self.rect.x < 800 - self.rect.width:
            self.subx += self.speed

        self.rect.x = round(self.subx / self.subpix)
        self.rect.y = round(self.suby / self.subpix)

class Cebra(Animal):
    def __init__(self, vida, energia, dieta, especies):
        super().__init__(vida, energia, dieta, especies)
        self.image = pygame.image.load("Animales/cebra.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = ra.randint(0,800)
        self.rect.y = ra.randint(0,600)
        self.speed = 1
        self.subx = 0
        self.suby = 0
        self.subpix = 6
        self.rango = ra.randint(0, 500)
        self.direction = None  # Agrega una dirección inicial

    def update(self):
        self.rango -= 1
        if self.rango < 0:
            self.rango = ra.randint(0, 500)
            direction = ra.randint(1, 4)
            if direction == 1:
                self.direction = "up" # Actualiza la dirección en self.direction
            elif direction == 2:
                self.direction = "down"
            elif direction == 3:
                self.direction = "left"
            elif direction == 4:
                self.direction = "right"

        if self.direction == "up" and self.rect.y > 0:
            self.suby -= self.speed
        elif self.direction == "down" and self.rect.y < 600 - self.rect.height:
            self.suby += self.speed
        elif self.direction == "left" and self.rect.x > 0:
            self.subx -= self.speed
        elif self.direction == "right" and self.rect.x < 800 - self.rect.width:
            self.subx += self.speed

        self.rect.x = round(self.subx / self.subpix)
class Cerdo(Animal):
    def __init__(self, vida, energia, dieta, especies):
        super().__init__(vida, energia, dieta, especies)
        self.image = pygame.image.load("Animales/cerdo.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = ra.randint(0,800)
        self.rect.y = ra.randint(0,600)
        self.speed = 1
        self.subx = 0
        self.suby = 0
        self.subpix = 6
        self.rango = ra.randint(0, 500)
        self.direction = None  # Agrega una dirección inicial

    def update(self):
        self.rango -= 1
        if self.rango < 0:
            self.rango = ra.randint(0, 500)
            direction = ra.randint(1, 4)
            if direction == 1:
                self.direction = "up" # Actualiza la dirección en self.direction
            elif direction == 2:
                self.direction = "down"
            elif direction == 3:
                self.direction = "left"
            elif direction == 4:
                self.direction = "right"

        if self.direction == "up" and self.rect.y > 0:
            self.suby -= self.speed
        elif self.direction == "down" and self.rect.y < 600 - self.rect.height:
            self.suby += self.speed
        elif self.direction == "left" and self.rect.x > 0:
            self.subx -= self.speed
        elif self.direction == "right" and self.rect.x < 800 - self.rect.width:
            self.subx += self.speed

        self.rect.x = round(self.subx / self.subpix)

class Jirafa(Animal):
    def __init__(self, vida, energia, dieta, especies):
        super().__init__(vida, energia, dieta, especies)
        self.image = pygame.image.load("Animales/jirafa.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = ra.randint(0,800)
        self.rect.y = ra.randint(0,600)
        self.speed = 1
        self.subx = 0
        self.suby = 0
        self.subpix = 6
        self.rango = ra.randint(0, 500)
        self.direction = None  # Agrega una dirección inicial

    def update(self):
        self.rango -= 1
        if self.rango < 0:
            self.rango = ra.randint(0, 500)
            direction = ra.randint(1, 4)
            if direction == 1:
                self.direction = "up" # Actualiza la dirección en self.direction
            elif direction == 2:
                self.direction = "down"
            elif direction == 3:
                self.direction = "left"
            elif direction == 4:
                self.direction = "right"

        if self.direction == "up" and self.rect.y > 0:
            self.suby -= self.speed
        elif self.direction == "down" and self.rect.y < 600 - self.rect.height:
            self.suby += self.speed
        elif self.direction == "left" and self.rect.x > 0:
            self.subx -= self.speed
        elif self.direction == "right" and self.rect.x < 800 - self.rect.width:
            self.subx += self.speed

        self.rect.x = round(self.subx / self.subpix)

class Elefante(Animal):
    def __init__(self, vida, energia, dieta, especies):
        super().__init__(vida, energia, dieta, especies)
        self.image = pygame.image.load("Animales/elefante.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = ra.randint(0,800)
        self.rect.y = ra.randint(0,600)
        self.speed = 1
        self.subx = 0
        self.suby = 0
        self.subpix = 6
        self.rango = ra.randint(0, 500)
        self.direction = None  # Agrega una dirección inicial

    def update(self):
        self.rango -= 1
        if self.rango < 0:
            self.rango = ra.randint(0, 500)
            direction = ra.randint(1, 4)
            if direction == 1:
                self.direction = "up" # Actualiza la dirección en self.direction
            elif direction == 2:
                self.direction = "down"
            elif direction == 3:
                self.direction = "left"
            elif direction == 4:
                self.direction = "right"

        if self.direction == "up" and self.rect.y > 0:
            self.suby -= self.speed
        elif self.direction == "down" and self.rect.y < 600 - self.rect.height:
            self.suby += self.speed
        elif self.direction == "left" and self.rect.x > 0:
            self.subx -= self.speed
        elif self.direction == "right" and self.rect.x < 800 - self.rect.width:
            self.subx += self.speed

        self.rect.x = round(self.subx / self.subpix)

    