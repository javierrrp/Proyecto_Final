import pygame
from pygame.sprite import Sprite
import random as ra
import time
from organismo import Organismo


class Animal(Organismo):
    def __init__(self, vida, energia, dieta, especies, sexo):
        super().__init__(0, 0, vida, energia)  # Ejemplo de posición inicial en (0, 0)
        self.dieta = dieta
        self.especies = especies
        self.sexo = sexo
        self.image = pygame.Surface((40, 40))  # Un cuadrado de 40x40 píxeles por defecto
        self.image.fill((255, 255, 255)) 
        self.rect = self.image.get_rect()
        self.rect.x = ra.randint(0, 24) * 40 # Centrar en una casilla
        self.rect.y = ra.randint(0, 18) * 40 # Centrar en una casilla
        self.target_x = self.rect.x  # Destino x en casilla
        self.target_y = self.rect.y  # Destino y en casilla
        self.speed = 1  # Velocidad baja para moverse de casilla en casilla
        self.rango = ra.randint(0, 100)
        self.direction = None  # Dirección inicial
        self.movimiento = True
    
    def update(self):
        if self.movimiento: 
            self.rango -= 1
            if self.rango < 0:
                self.rango = ra.randint(0, 100)
                self.direction = ra.choice(["up", "down", "left", "right", "stop"])
                # Calcular la nueva posición de destino dentro de la cuadrícula
                grid_x = self.rect.x // 40 * 40
                grid_y = self.rect.y // 40 * 40
                
                if self.direction == "up" and self.rect.y > 0:
                    self.target_y = max(0, grid_y - 40)
                elif self.direction == "down" and self.rect.y < 760 - self.rect.height:
                    self.target_y = min(760 - self.rect.height, grid_y + 40)
                elif self.direction == "left" and self.rect.x > 0:
                    self.target_x = max(0, grid_x - 40)
                elif self.direction == "right" and self.rect.x < 920 - self.rect.width:
                    self.target_x = min(920 - self.rect.width, grid_x + 40)
                elif self.direction == "stop" and self.rect.x < 920 - self.rect.width:
                    self.target_x = 0


            # Mover hacia la posición de destino (suaviza el movimiento)
            if self.rect.x < self.target_x:
                self.rect.x += min(self.speed, self.target_x - self.rect.x)
            elif self.rect.x > self.target_x:
                self.rect.x -= min(self.speed, self.rect.x - self.target_x)
            elif self.rect.y < self.target_y:
                self.rect.y += min(self.speed, self.target_y - self.rect.y)
            elif self.rect.y > self.target_y:
                self.rect.y -= min(self.speed, self.rect.y - self.target_y)

    def cazar(self):  
        pass
        
    def descomposicion(self):
        pass


class Tigre(Animal):
    def __init__(self, vida, energia, dieta, especies, sexo):
        super().__init__(vida, energia, dieta, especies, sexo)
        self.vida = vida
        self.image = pygame.image.load("Animales/tigre.png").convert_alpha()


    def update(self):
        super().update()

class Cebra(Animal):
    def __init__(self, vida, energia, dieta, especies, sexo):
        super().__init__(vida, energia, dieta, especies, sexo)
        self.vida = vida
        self.image = pygame.image.load("Animales/cebra.png").convert_alpha()


    def update(self):
        super().update()
class Cerdo(Animal):
    def __init__(self, vida, energia, dieta, especies, sexo):
        super().__init__(vida, energia, dieta, especies, sexo)
        self.vida = vida
        self.image = pygame.image.load("Animales/cerdo.png").convert_alpha()
  

    def update(self):
        super().update()
class Jirafa(Animal):
    def __init__(self, vida, energia, dieta, especies, sexo):
        super().__init__(vida, energia, dieta, especies, sexo)
        self.vida = vida
        self.image = pygame.image.load("Animales/jirafa.png").convert_alpha()


    def update(self):
        super().update()
class Elefante(Animal):
    def __init__(self, vida, energia, dieta, especies, sexo):
        super().__init__(vida, energia, dieta, especies, sexo)
        self.vida = vida
        self.image = pygame.image.load("Animales/elefante.png").convert_alpha()


    def update(self):
        super().update()
        

class Jabali(Animal):
    def __init__(self, vida, energia, dieta, especies, sexo):
        super().__init__(vida, energia, dieta, especies, sexo)
        self.vida = vida
        self.image = pygame.image.load("Animales/jabali.png").convert_alpha()


    def update(self):
        super().update()

class Leopardo(Animal):
    def __init__(self, vida, energia, dieta, especies, sexo):
        super().__init__(vida, energia, dieta, especies, sexo)
        self.vida = vida
        self.image = pygame.image.load("Animales/leopardo.png").convert_alpha()

    def update(self):
        super().update()


class Suricata(Animal):
    def __init__(self, vida, energia, dieta, especies, sexo):
        super().__init__(vida, energia, dieta, especies, sexo)
        self.vida = vida
        self.image = pygame.image.load("Animales/suricata.png").convert_alpha()

    def update(self):
        super().update()

class Insecto(Animal):
    def __init__(self, vida, energia, dieta, especies, sexo):
        super().__init__(vida, energia, dieta, especies, sexo)
        self.vida = vida
        self.image = pygame.image.load("Animales/insecto.png").convert_alpha()

    def update(self):
        super().update()