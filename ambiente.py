import pygame
from pygame.locals import *
from pygame.sprite import Sprite
import random as ra

nRes = [1268, 768, 960]
screen = pygame.display.set_mode((nRes[0],nRes[1]))

# Imagen de fondo
fondo = pygame.image.load('mapa/map.png')
fondo2 = pygame.image.load('mapa/map2.png')
fondo3 = pygame.image.load('mapa/map3.png')
fondo4 = pygame.image.load('mapa/map4.png')
fondo5 = pygame.image.load('mapa/map5.png')
fondo6 = pygame.image.load('mapa/map6.png')
fondo_rect = fondo.get_rect()
fondo_rect2 = fondo2.get_rect()
fondo_rect3 = fondo3.get_rect()
fondo_rect4 = fondo4.get_rect()
fondo_rect5 = fondo5.get_rect()
fondo_rect6 = fondo6.get_rect()


class Ambiente:
    def __init__(self, counter):
        self.counter = 0
    class lluvia:
        #Constructor
        def __init__(self):
            #posicionx 
            self.x = ra.randint(0, 1024)
            #posiciony
            self.y = ra.randint(-1500, -20)
            #Velocidad al caer en eje y
            self.yspeed = ra.uniform(10, 50)
            self.tamaño = ra.randint(10, 20)
            

        def mostrar(self):
            self.y += self.yspeed
            self.yspeed += 50

            if self.y > 768:
                self.y = ra.randint(-200, -20)
                self.yspeed = ra.uniform(100, 50)

            pygame.draw.line(screen, (25, 41, 237), (self.x, self.y), (self.x, self.y+self.tamaño), 2)

    class Tormenta(Sprite):
        def __init__(self):
            super().__init__()
            self.nube = ra.randrange(3)
            if self.nube == 1:
                self.image = pygame.transform.scale(pygame.image.load("Ambiente/nube.png").convert(), (50, 50))
                self.rect = self.image.get_rect()
                self.radius = 25
            elif self.nube == 0:
                self.image = pygame.transform.scale(pygame.image.load("Ambiente/nube.png").convert(), (75, 75))
                self.rect = self.image.get_rect()
                self.radius = 37
            elif self.nube == 2:
                self.image = pygame.transform.scale(pygame.image.load("Ambiente/nube.png").convert(), (100, 100))
                self.rect = self.image.get_rect()
                self.radius = 50
            self.image.set_colorkey((0,0,0))

            self.rect.x = ra.randrange(-1000, 0)
            self.rect.y = ra.randrange(-30, 100)
            self.velocidad_x = ra.randrange(1 , 5) # Velocidad horizontal aleatoria
            self.transparencia = 0

        def update(self):
            self.rect.x += self.velocidad_x
            if self.rect.right > nRes[2] + 100:
                self.rect.x = ra.randrange(-1000, 0)
                self.rect.y = ra.randrange(-30, 100)
                self.velocidad_x = ra.randrange(1 , 5) # Velocidad horizontal aleatoria

            self.transparencia = min(255, self.transparencia + 1)
            self.image.set_alpha(self.transparencia)
