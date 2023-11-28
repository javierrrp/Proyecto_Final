import pygame
from pygame.sprite import Sprite
import random as ra
import time
from organismo import Organismo


class Animal(Organismo):
    def __init__(self, vida, energia, dieta, especies):
        super().__init__(0, 0, vida, energia)  # Ejemplo de posición inicial en (0, 0)
        self.dieta = dieta
        self.especies = especies

    def cazar(self):  
        pass
        
    def descomposicion(self):
        pass

class Leon(Animal):
    def __init__(self, vida, energia, dieta, especies):
        super().__init__(vida, energia, dieta, especies)
        self.vida = vida
        self.image = pygame.image.load("Animales/leon.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = ra.randint(0, 23) * 40 - 3  # Centrar en una casilla
        self.rect.y = ra.randint(0, 19) * 40 - 3 # Centrar en una casilla
        self.target_x = self.rect.x  # Destino x en casilla
        self.target_y = self.rect.y  # Destino y en casilla
        self.speed = 1  # Velocidad baja para moverse de casilla en casilla
        self.rango = ra.randint(0, 500)
        self.direction = None  # Dirección inicial

    def update(self):
        self.rango -= 1
        if self.rango < 0:
            self.rango = ra.randint(0, 500)
            self.direction = ra.choice(["up", "down", "left", "right"])
            # Calcular la nueva posición de destino dentro de la cuadrícula
            if self.direction == "up" and self.rect.y > 0:
                self.target_y = max(0, self.rect.y - 40)
            elif self.direction == "down" and self.rect.y < 760 - self.rect.height:
                self.target_y = min(760 - self.rect.height, self.rect.y + 40)
            elif self.direction == "left" and self.rect.x > 0:
                self.target_x = max(0, self.rect.x - 40)
            elif self.direction == "right" and self.rect.x < 920 - self.rect.width:
                self.target_x = min(920 - self.rect.width, self.rect.x + 40)

        # Mover hacia la posición de destino (suaviza el movimiento)
        if self.rect.x < self.target_x:
            self.rect.x += min(self.speed, self.target_x - self.rect.x)
        elif self.rect.x > self.target_x:
            self.rect.x -= min(self.speed, self.rect.x - self.target_x)
        elif self.rect.y < self.target_y:
            self.rect.y += min(self.speed, self.target_y - self.rect.y)
        elif self.rect.y > self.target_y:
            self.rect.y -= min(self.speed, self.rect.y - self.target_y)
class Leona(Animal):
    def __init__(self, vida, energia, dieta, especies):
        super().__init__(vida, energia, dieta, especies)
        self.vida = vida
        self.image = pygame.image.load("Animales/leona.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = ra.randint(0, 23) * 40 - 3  # Centrar en una casilla
        self.rect.y = ra.randint(0, 19) * 40 - 3 # Centrar en una casilla
        self.target_x = self.rect.x  # Destino x en casilla
        self.target_y = self.rect.y  # Destino y en casilla
        self.speed = 1  # Velocidad baja para moverse de casilla en casilla
        self.rango = ra.randint(0, 500)
        self.direction = None  # Dirección inicial

    def update(self):
        self.rango -= 1
        if self.rango < 0:
            self.rango = ra.randint(0, 500)
            self.direction = ra.choice(["up", "down", "left", "right"])
            # Calcular la nueva posición de destino dentro de la cuadrícula
            if self.direction == "up" and self.rect.y > 0:
                self.target_y = max(0, self.rect.y - 40)
            elif self.direction == "down" and self.rect.y < 760 - self.rect.height:
                self.target_y = min(760 - self.rect.height, self.rect.y + 40)
            elif self.direction == "left" and self.rect.x > 0:
                self.target_x = max(0, self.rect.x - 40)
            elif self.direction == "right" and self.rect.x < 920 - self.rect.width:
                self.target_x = min(920 - self.rect.width, self.rect.x + 40)

        # Mover hacia la posición de destino (suaviza el movimiento)
        if self.rect.x < self.target_x:
            self.rect.x += min(self.speed, self.target_x - self.rect.x)
        elif self.rect.x > self.target_x:
            self.rect.x -= min(self.speed, self.rect.x - self.target_x)
        elif self.rect.y < self.target_y:
            self.rect.y += min(self.speed, self.target_y - self.rect.y)
        elif self.rect.y > self.target_y:
            self.rect.y -= min(self.speed, self.rect.y - self.target_y)


class Cebra(Animal):
    def __init__(self, vida, energia, dieta, especies):
        super().__init__(vida, energia, dieta, especies)
        self.vida = vida
        self.image = pygame.image.load("Animales/cebra.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = ra.randint(0, 23) * 40 - 3  # Centrar en una casilla
        self.rect.y = ra.randint(0, 19) * 40 - 3 # Centrar en una casilla
        self.target_x = self.rect.x  # Destino x en casilla
        self.target_y = self.rect.y  # Destino y en casilla
        self.speed = 1  # Velocidad baja para moverse de casilla en casilla
        self.rango = ra.randint(0, 500)
        self.direction = None  # Dirección inicial

    def update(self):
        self.rango -= 1
        if self.rango < 0:
            self.rango = ra.randint(0, 500)
            self.direction = ra.choice(["up", "down", "left", "right"])
            # Calcular la nueva posición de destino dentro de la cuadrícula
            if self.direction == "up" and self.rect.y > 0:
                self.target_y = max(0, self.rect.y - 40)
            elif self.direction == "down" and self.rect.y < 760 - self.rect.height:
                self.target_y = min(760 - self.rect.height, self.rect.y + 40)
            elif self.direction == "left" and self.rect.x > 0:
                self.target_x = max(0, self.rect.x - 40)
            elif self.direction == "right" and self.rect.x < 920 - self.rect.width:
                self.target_x = min(920 - self.rect.width, self.rect.x + 40)

        # Mover hacia la posición de destino (suaviza el movimiento)
        if self.rect.x < self.target_x:
            self.rect.x += min(self.speed, self.target_x - self.rect.x)
        elif self.rect.x > self.target_x:
            self.rect.x -= min(self.speed, self.rect.x - self.target_x)
        elif self.rect.y < self.target_y:
            self.rect.y += min(self.speed, self.target_y - self.rect.y)
        elif self.rect.y > self.target_y:
            self.rect.y -= min(self.speed, self.rect.y - self.target_y)
class Cerdo(Animal):
    def __init__(self, vida, energia, dieta, especies):
        super().__init__(vida, energia, dieta, especies)
        self.vida = vida
        self.image = pygame.image.load("Animales/cerdo.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = ra.randint(0, 23) * 40 - 3  # Centrar en una casilla
        self.rect.y = ra.randint(0, 19) * 40 - 3 # Centrar en una casilla
        self.target_x = self.rect.x  # Destino x en casilla
        self.target_y = self.rect.y  # Destino y en casilla
        self.speed = 1  # Velocidad baja para moverse de casilla en casilla
        self.rango = ra.randint(0, 500)
        self.direction = None  # Dirección inicial

    def update(self):
        self.rango -= 1
        if self.rango < 0:
            self.rango = ra.randint(0, 500)
            self.direction = ra.choice(["up", "down", "left", "right"])
            # Calcular la nueva posición de destino dentro de la cuadrícula
            if self.direction == "up" and self.rect.y > 0:
                self.target_y = max(0, self.rect.y - 40)
            elif self.direction == "down" and self.rect.y < 760 - self.rect.height:
                self.target_y = min(760 - self.rect.height, self.rect.y + 40)
            elif self.direction == "left" and self.rect.x > 0:
                self.target_x = max(0, self.rect.x - 40)
            elif self.direction == "right" and self.rect.x < 920 - self.rect.width:
                self.target_x = min(920 - self.rect.width, self.rect.x + 40)

        # Mover hacia la posición de destino (suaviza el movimiento)
        if self.rect.x < self.target_x:
            self.rect.x += min(self.speed, self.target_x - self.rect.x)
        elif self.rect.x > self.target_x:
            self.rect.x -= min(self.speed, self.rect.x - self.target_x)
        elif self.rect.y < self.target_y:
            self.rect.y += min(self.speed, self.target_y - self.rect.y)
        elif self.rect.y > self.target_y:
            self.rect.y -= min(self.speed, self.rect.y - self.target_y)
class Jirafa(Animal):
    def __init__(self, vida, energia, dieta, especies):
        super().__init__(vida, energia, dieta, especies)
        self.vida = vida
        self.image = pygame.image.load("Animales/jirafa.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = ra.randint(0, 23) * 40 + (40 - self.rect.width) // 2 # Centrar en una casilla
        self.rect.y = ra.randint(0, 19) * 40 + (40 - self.rect.height) // 2 # Centrar en una casilla
        self.target_x = self.rect.x  # Destino x en casilla
        self.target_y = self.rect.y  # Destino y en casilla
        self.speed = 1  # Velocidad baja para moverse de casilla en casilla
        self.rango = ra.randint(0, 500)
        self.direction = None  # Dirección inicial

    def update(self):
        self.rango -= 1
        if self.rango < 0:
            self.rango = ra.randint(0, 500)
            self.direction = ra.choice(["up", "down", "left", "right"])
            # Calcular la nueva posición de destino dentro de la cuadrícula
            if self.direction == "up" and self.rect.y > 0:
                self.target_y = max(0, self.rect.y - 40)
            elif self.direction == "down" and self.rect.y < 760 - self.rect.height:
                self.target_y = min(760 - self.rect.height, self.rect.y + 40)
            elif self.direction == "left" and self.rect.x > 0:
                self.target_x = max(0, self.rect.x - 40)
            elif self.direction == "right" and self.rect.x < 920 - self.rect.width:
                self.target_x = min(920 - self.rect.width, self.rect.x + 40)

        # Mover hacia la posición de destino (suaviza el movimiento)
        if self.rect.x < self.target_x:
            self.rect.x += min(self.speed, self.target_x - self.rect.x)
        elif self.rect.x > self.target_x:
            self.rect.x -= min(self.speed, self.rect.x - self.target_x)
        elif self.rect.y < self.target_y:
            self.rect.y += min(self.speed, self.target_y - self.rect.y)
        elif self.rect.y > self.target_y:
            self.rect.y -= min(self.speed, self.rect.y - self.target_y)
class Elefante(Animal):
    def __init__(self, vida, energia, dieta, especies):
        super().__init__(vida, energia, dieta, especies)
        self.vida = vida
        self.image = pygame.image.load("Animales/elefante.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = ra.randint(0, 23) * 40 - 3  # Centrar en una casilla
        self.rect.y = ra.randint(0, 19) * 40 - 3 # Centrar en una casilla
        self.target_x = self.rect.x  # Destino x en casilla
        self.target_y = self.rect.y  # Destino y en casilla
        self.speed = 1  # Velocidad baja para moverse de casilla en casilla
        self.rango = ra.randint(0, 500)
        self.direction = None  # Dirección inicial

    def update(self):
        self.rango -= 1
        if self.rango < 0:
            self.rango = ra.randint(0, 500)
            self.direction = ra.choice(["up", "down", "left", "right"])
            # Calcular la nueva posición de destino dentro de la cuadrícula
            if self.direction == "up" and self.rect.y > 0:
                self.target_y = max(0, self.rect.y - 40)
            elif self.direction == "down" and self.rect.y < 760 - self.rect.height:
                self.target_y = min(760 - self.rect.height, self.rect.y + 40)
            elif self.direction == "left" and self.rect.x > 0:
                self.target_x = max(0, self.rect.x - 40)
            elif self.direction == "right" and self.rect.x < 920 - self.rect.width:
                self.target_x = min(920 - self.rect.width, self.rect.x + 40)

        # Mover hacia la posición de destino (suaviza el movimiento)
        if self.rect.x < self.target_x:
            self.rect.x += min(self.speed, self.target_x - self.rect.x)
        elif self.rect.x > self.target_x:
            self.rect.x -= min(self.speed, self.rect.x - self.target_x)
        elif self.rect.y < self.target_y:
            self.rect.y += min(self.speed, self.target_y - self.rect.y)
        elif self.rect.y > self.target_y:
            self.rect.y -= min(self.speed, self.rect.y - self.target_y)
        

class Jabali(Animal):
    def __init__(self, vida, energia, dieta, especies):
        super().__init__(vida, energia, dieta, especies)
        self.vida = vida
        self.image = pygame.image.load("Animales/jabali.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = ra.randint(0, 23) * 40 - 3  # Centrar en una casilla
        self.rect.y = ra.randint(0, 19) * 40 - 3 # Centrar en una casilla
        self.target_x = self.rect.x  # Destino x en casilla
        self.target_y = self.rect.y  # Destino y en casilla
        self.speed = 1  # Velocidad baja para moverse de casilla en casilla
        self.rango = ra.randint(0, 500)
        self.direction = None  # Dirección inicial

    def update(self):
        self.rango -= 1
        if self.rango < 0:
            self.rango = ra.randint(0, 500)
            self.direction = ra.choice(["up", "down", "left", "right"])
            # Calcular la nueva posición de destino dentro de la cuadrícula
            if self.direction == "up" and self.rect.y > 0:
                self.target_y = max(0, self.rect.y - 40)
            elif self.direction == "down" and self.rect.y < 760 - self.rect.height:
                self.target_y = min(760 - self.rect.height, self.rect.y + 40)
            elif self.direction == "left" and self.rect.x > 0:
                self.target_x = max(0, self.rect.x - 40)
            elif self.direction == "right" and self.rect.x < 920 - self.rect.width:
                self.target_x = min(920 - self.rect.width, self.rect.x + 40)

        # Mover hacia la posición de destino (suaviza el movimiento)
        if self.rect.x < self.target_x:
            self.rect.x += min(self.speed, self.target_x - self.rect.x)
        elif self.rect.x > self.target_x:
            self.rect.x -= min(self.speed, self.rect.x - self.target_x)
        elif self.rect.y < self.target_y:
            self.rect.y += min(self.speed, self.target_y - self.rect.y)
        elif self.rect.y > self.target_y:
            self.rect.y -= min(self.speed, self.rect.y - self.target_y)


class Leopardo(Animal):
    def __init__(self, vida, energia, dieta, especies):
        super().__init__(vida, energia, dieta, especies)
        self.vida = vida
        self.image = pygame.image.load("Animales/leopardo.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = ra.randint(0, 23) * 40 + (40 - self.rect.width) // 2 # Centrar en una casilla
        self.rect.y = ra.randint(0, 19) * 40 + (40 - self.rect.height) // 2 # Centrar en una casilla
        self.target_x = self.rect.x  # Destino x en casilla
        self.target_y = self.rect.y  # Destino y en casilla
        self.speed = 1  # Velocidad baja para moverse de casilla en casilla
        self.rango = ra.randint(0, 500)
        self.direction = None  # Dirección inicial

    def update(self):
        self.rango -= 1
        if self.rango < 0:
            self.rango = ra.randint(0, 500)
            self.direction = ra.choice(["up", "down", "left", "right"])
            # Calcular la nueva posición de destino dentro de la cuadrícula
            if self.direction == "up" and self.rect.y > 0:
                self.target_y = max(0, self.rect.y - 40)
            elif self.direction == "down" and self.rect.y < 760 - self.rect.height:
                self.target_y = min(760 - self.rect.height, self.rect.y + 40)
            elif self.direction == "left" and self.rect.x > 0:
                self.target_x = max(0, self.rect.x - 40)
            elif self.direction == "right" and self.rect.x < 920 - self.rect.width:
                self.target_x = min(920 - self.rect.width, self.rect.x + 40)

        # Mover hacia la posición de destino (suaviza el movimiento)
        if self.rect.x < self.target_x:
            self.rect.x += min(self.speed, self.target_x - self.rect.x)
        elif self.rect.x > self.target_x:
            self.rect.x -= min(self.speed, self.rect.x - self.target_x)
        elif self.rect.y < self.target_y:
            self.rect.y += min(self.speed, self.target_y - self.rect.y)
        elif self.rect.y > self.target_y:
            self.rect.y -= min(self.speed, self.rect.y - self.target_y)


class Suricata(Animal):
    def __init__(self, vida, energia, dieta, especies):
        super().__init__(vida, energia, dieta, especies)
        self.vida = vida
        self.image = pygame.image.load("Animales/suricata.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = ra.randint(0, 23) * 40 - 3  # Centrar en una casilla
        self.rect.y = ra.randint(0, 19) * 40 - 3 # Centrar en una casilla
        self.target_x = self.rect.x  # Destino x en casilla
        self.target_y = self.rect.y  # Destino y en casilla
        self.speed = 1  # Velocidad baja para moverse de casilla en casilla
        self.rango = ra.randint(0, 500)
        self.direction = None  # Dirección inicial

    def update(self):
        self.rango -= 1
        if self.rango < 0:
            self.rango = ra.randint(0, 500)
            self.direction = ra.choice(["up", "down", "left", "right"])
            # Calcular la nueva posición de destino dentro de la cuadrícula
            if self.direction == "up" and self.rect.y > 0:
                self.target_y = max(0, self.rect.y - 40)
            elif self.direction == "down" and self.rect.y < 760 - self.rect.height:
                self.target_y = min(760 - self.rect.height, self.rect.y + 40)
            elif self.direction == "left" and self.rect.x > 0:
                self.target_x = max(0, self.rect.x - 40)
            elif self.direction == "right" and self.rect.x < 920 - self.rect.width:
                self.target_x = min(920 - self.rect.width, self.rect.x + 40)

        # Mover hacia la posición de destino (suaviza el movimiento)
        if self.rect.x < self.target_x:
            self.rect.x += min(self.speed, self.target_x - self.rect.x)
        elif self.rect.x > self.target_x:
            self.rect.x -= min(self.speed, self.rect.x - self.target_x)
        elif self.rect.y < self.target_y:
            self.rect.y += min(self.speed, self.target_y - self.rect.y)
        elif self.rect.y > self.target_y:
            self.rect.y -= min(self.speed, self.rect.y - self.target_y)
