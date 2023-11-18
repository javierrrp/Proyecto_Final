import pygame
from pygame.sprite import Sprite
import random as ra

class Leon(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Animales/leon.png").convert_alpha()  # Agrega la imagen del león
        self.rect = self.image.get_rect()  # Crea un rectángulo con las dimensiones de la imagen

        self.nF = ra.randint(1, 3)  # Resto de atributos iniciales...
        self.nX = ra.randint(0, 800)
        self.nY = ra.randint(0, 600)
        self.nR = ra.randint(0, 500)
        self.dX = 0
        self.dY = 0
        self.nV = ra.randint(1, 3)

    def update(self):
        self.nR -= 1
        if self.nR < 0:
            # Restablecer posición y velocidad
            self.nR = ra.randint(0, 500)
            self.nV = ra.randint(1, 3)

            # Lógica para actualizar la dirección del león...
            nDir = ra.randint(1, 9)
            if nDir == 1: # Norte ?
                self.dX = +0 ; self.dY = -1
            if nDir == 2: # Este ?
                self.dX = +1 ; self.dY = 0
            if nDir == 3: # Sur ?
                self.dX = +0 ; self.dY = +1
            if nDir == 4: # Oeste ?
                self.dX = -1 ; self.dY = +0
            if nDir == 5: # Detenido ?
                self.dX = +0 ; self.dY = +0
            
        # Actualizar la posición del león
        self.rect.x += self.dX
        self.rect.y += self.dY
