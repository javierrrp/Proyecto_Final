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
        self.vida = 100
        self.image = pygame.image.load("Animales/leon.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = ra.randint(0,974)
        self.rect.y = ra.randint(0,768)
        self.speed = 2  # Velocidad muy baja para movimiento lento
        self.subpix = 6
        self.subx = self.rect.x * self.subpix + 3  # Ajuste para centrar en la casilla
        self.suby = self.rect.y * self.subpix + 3  # Ajuste para centrar en la casilla
        self.rango = ra.randint(0, 500)
        self.direction = None  # Dirección inicial

    def update(self):
        self.rango -= 1
        if self.rango < 0:
            self.rango = ra.randint(0, 500)
            direction = ra.randint(1, 4)
            if direction == 1:
                self.direction = "up"  # Actualiza la dirección en self.direction
            elif direction == 2:
                self.direction = "down"
            elif direction == 3:
                self.direction = "left"
            elif direction == 4:
                self.direction = "right"

        if self.direction == "up" and self.rect.y > 0:
            self.suby -= self.speed
        elif self.direction == "down" and self.rect.y < 768 - self.rect.height:
            self.suby += self.speed
        elif self.direction == "left" and self.rect.x > 768 + 300:
            self.subx -= self.speed
        elif self.direction == "right" and self.rect.x < 974 - self.rect.width:
            self.subx += self.speed
        else: 
            self.direction = ra.choice(["up", "down", "left", "right"])


        self.rect.x = round((self.subx - 3) / self.subpix)  # Ajuste para centrar en la casilla
        self.rect.y = round((self.suby - 3) / self.subpix)  # Ajuste para centrar en la casilla

class Leona(Animal):
    def __init__(self, vida, energia, dieta, especies):
        super().__init__(vida, energia, dieta, especies)
        self.vida = 100
        self.image = pygame.image.load("Animales/leona.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = ra.randint(0,974)
        self.rect.y = ra.randint(0,768)
        self.speed = 2  # Velocidad muy baja para movimiento lento
        self.subpix = 6
        self.subx = self.rect.x * self.subpix + 3  # Ajuste para centrar en la casilla
        self.suby = self.rect.y * self.subpix + 3  # Ajuste para centrar en la casilla
        self.rango = ra.randint(0, 500)
        self.direction = None  # Dirección inicial

    def update(self):
        self.rango -= 1
        if self.rango < 0:
            self.rango = ra.randint(0, 500)
            direction = ra.randint(1, 4)
            if direction == 1:
                self.direction = "up"  # Actualiza la dirección en self.direction
            elif direction == 2:
                self.direction = "down"
            elif direction == 3:
                self.direction = "left"
            elif direction == 4:
                self.direction = "right"

        if self.direction == "up" and self.rect.y > 0:
            self.suby -= self.speed
        elif self.direction == "down" and self.rect.y < 768 - self.rect.height:
            self.suby += self.speed
        elif self.direction == "left" and self.rect.x > 768 + 300:
            self.subx -= self.speed
        elif self.direction == "right" and self.rect.x < 974 - self.rect.width:
            self.subx += self.speed


        self.rect.x = round((self.subx - 3) / self.subpix)  # Ajuste para centrar en la casilla
        self.rect.y = round((self.suby - 3) / self.subpix)  # Ajuste para centrar en la casilla




class Cebra(Animal):
    def __init__(self, vida, energia, dieta, especies):
        super().__init__(vida, energia, dieta, especies)
        self.vida = 100
        self.image = pygame.image.load("Animales/cebra.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = ra.randint(0,974)
        self.rect.y = ra.randint(0,768)
        self.speed = 2
        self.subx = self.rect.x * 6  
        self.suby = self.rect.y * 6
        self.subpix = 6
        self.rango = ra.randint(0, 500)
        self.direction = None  

    def update(self):
        self.rango -= 1
        if self.rango < 0:
            self.rango = ra.randint(0, 500)
            direction = ra.randint(1, 4)
            if direction == 1:
                self.direction = "up"
            elif direction == 2:
                self.direction = "down"
            elif direction == 3:
                self.direction = "left"
            elif direction == 4:
                self.direction = "right"

        if self.direction == "up" and self.rect.y > 0:
            self.suby -= self.speed
        elif self.direction == "down" and self.rect.y < 768 - self.rect.height:
            self.suby += self.speed
        elif self.direction == "left" and self.rect.x > 768 + 300:
            self.subx -= self.speed
        elif self.direction == "right" and self.rect.x < 974 - self.rect.width:
            self.subx += self.speed

        self.rect.x = round(self.subx / self.subpix)
        self.rect.y = round(self.suby / self.subpix)
class Cerdo(Animal):
    def __init__(self, vida, energia, dieta, especies):
        super().__init__(vida, energia, dieta, especies)
        self.vida = 100
        self.image = pygame.image.load("Animales/cerdo.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = ra.randint(0,974)
        self.rect.y = ra.randint(0,768)
        self.speed = 1
        self.subx = self.rect.x * 6  
        self.suby = self.rect.y * 6
        self.subpix = 6
        self.rango = ra.randint(0, 500)
        self.direction = None  

    def update(self):
        self.rango -= 1
        if self.rango < 0:
            self.rango = ra.randint(0, 500)
            direction = ra.randint(1, 4)
            if direction == 1:
                self.direction = "up"
            elif direction == 2:
                self.direction = "down"
            elif direction == 3:
                self.direction = "left"
            elif direction == 4:
                self.direction = "right"

        if self.direction == "up" and self.rect.y > 0:
            self.suby -= self.speed
        elif self.direction == "down" and self.rect.y < 768 - self.rect.height:
            self.suby += self.speed
        elif self.direction == "left" and self.rect.x > 768 + 300:
            self.subx -= self.speed
        elif self.direction == "right" and self.rect.x < 974 - self.rect.width:
            self.subx += self.speed

        self.rect.x = round(self.subx / self.subpix)
        self.rect.y = round(self.suby / self.subpix)

class Jirafa(Animal):
    def __init__(self, vida, energia, dieta, especies):
        super().__init__(vida, energia, dieta, especies)
        self.vida = 100
        self.image = pygame.image.load("Animales/jirafa.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = ra.randint(0,974)
        self.rect.y = ra.randint(0,768)
        self.speed = 1
        self.subx = self.rect.x * 6  
        self.suby = self.rect.y * 6
        self.subpix = 6
        self.rango = ra.randint(0, 500)
        self.direction = None 

    def update(self):
        self.rango -= 1
        if self.rango < 0:
            self.rango = ra.randint(0, 500)
            direction = ra.randint(1, 4)
            if direction == 1:
                self.direction = "up" 
            elif direction == 2:
                self.direction = "down"
            elif direction == 3:
                self.direction = "left"
            elif direction == 4:
                self.direction = "right"

        if self.direction == "up" and self.rect.y > 0:
            self.suby -= self.speed
        elif self.direction == "down" and self.rect.y < 768 - self.rect.height:
            self.suby += self.speed
        elif self.direction == "left" and self.rect.x > 768 + 300:
            self.subx -= self.speed
        elif self.direction == "right" and self.rect.x < 974 - self.rect.width:
            self.subx += self.speed

        self.rect.x = round(self.subx / self.subpix)
        self.rect.y = round(self.suby / self.subpix)

class Elefante(Animal):
    def __init__(self, vida, energia, dieta, especies):
        super().__init__(vida, energia, dieta, especies)
        self.vida = 100
        self.image = pygame.image.load("Animales/elefante.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = ra.randint(0,974)
        self.rect.y = ra.randint(0,768)
        self.speed = 1
        self.subx = self.rect.x * 6  
        self.suby = self.rect.y * 6
        self.subpix = 6
        self.rango = ra.randint(0, 800)
        self.direction = None 

    def update(self):
        self.rango -= 1
        if self.rango < 0:
            self.rango = ra.randint(0, 500)
            direction = ra.randint(1, 4)
            if direction == 1:
                self.direction = "up" 
            elif direction == 2:
                self.direction = "down"
            elif direction == 3:
                self.direction = "left"
            elif direction == 4:
                self.direction = "right"

        if self.direction == "up" and self.rect.y > 0:
            self.suby -= self.speed
        elif self.direction == "down" and self.rect.y < 768 - self.rect.height:
            self.suby += self.speed
        elif self.direction == "left" and self.rect.x > 768 + 300:
            self.subx -= self.speed
        elif self.direction == "right" and self.rect.x < 974 - self.rect.width:
            self.subx += self.speed

        self.rect.x = round(self.subx / self.subpix)
        self.rect.y = round(self.suby / self.subpix)
    

class Jabali(Animal):
    def __init__(self, vida, energia, velocidad, dieta, especies):
        super().__init__(vida, energia, dieta, especies)
        self.vida = 100
        self.image = pygame.image.load("Animales/jabali.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = ra.randint(0,974)
        self.rect.y = ra.randint(0,768)
        self.speed = 2
        self.subx = self.rect.x * 6  
        self.suby = self.rect.y * 6
        self.subpix = 6
        self.rango = ra.randint(0, 500)
        self.direction = None 

    def update(self):
        self.rango -= 1
        if self.rango < 0:
            self.rango = ra.randint(0, 500)
            direction = ra.randint(1, 4)
            if direction == 1:
                self.direction = "up" 
            elif direction == 2:
                self.direction = "down"
            elif direction == 3:
                self.direction = "left"
            elif direction == 4:
                self.direction = "right"

        if self.direction == "up" and self.rect.y > 0:
            self.suby -= self.speed
        elif self.direction == "down" and self.rect.y < 768 - self.rect.height:
            self.suby += self.speed
        elif self.direction == "left" and self.rect.x > 768 + 300:
            self.subx -= self.speed
        elif self.direction == "right" and self.rect.x < 974 - self.rect.width:
            self.subx += self.speed

        self.rect.x = round(self.subx / self.subpix)
        self.rect.y = round(self.suby / self.subpix)


class Leopardo(Animal):
    def __init__(self, vida, energia, dieta, especies):
        super().__init__(vida, energia, dieta, especies)
        self.vida = 100
        self.image = pygame.image.load("Animales/leopardo.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = ra.randint(0,974)
        self.rect.y = ra.randint(0,768)
        self.speed = 2
        self.subx = self.rect.x * 6  
        self.suby = self.rect.y * 6
        self.subpix = 6
        self.rango = ra.randint(0, 500)
        self.direction = None 

    def update(self):
        self.rango -= 1
        if self.rango < 0:
            self.rango = ra.randint(0, 500)
            direction = ra.randint(1, 4)
            if direction == 1:
                self.direction = "up" 
            elif direction == 2:
                self.direction = "down"
            elif direction == 3:
                self.direction = "left"
            elif direction == 4:
                self.direction = "right"

        if self.direction == "up" and self.rect.y > 0:
            self.suby -= self.speed
        elif self.direction == "down" and self.rect.y < 768 - self.rect.height:
            self.suby += self.speed
        elif self.direction == "left" and self.rect.x > 768 + 300:
            self.subx -= self.speed
        elif self.direction == "right" and self.rect.x < 974 - self.rect.width:
            self.subx += self.speed

        self.rect.x = round(self.subx / self.subpix)
        self.rect.y = round(self.suby / self.subpix)


class Suricata(Animal):
    def __init__(self, vida, energia, velocidad, dieta, especies):
        super().__init__(vida, energia, dieta, especies)
        self.vida = 100
        self.image = pygame.image.load("Animales/suricata.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = ra.randint(0,974)
        self.rect.y = ra.randint(0,768)
        self.speed = 2
        self.subx = self.rect.x * 6  
        self.suby = self.rect.y * 6
        self.subpix = 6
        self.rango = ra.randint(0, 500)
        self.direction = None  

    def update(self):
        self.rango -= 1
        if self.rango < 0:
            self.rango = ra.randint(0, 500)
            direction = ra.randint(1, 4)
            if direction == 1:
                self.direction = "up" 
            elif direction == 2:
                self.direction = "down"
            elif direction == 3:
                self.direction = "left"
            elif direction == 4:
                self.direction = "right"

        if self.direction == "up" and self.rect.y > 0:
            self.suby -= self.speed
        elif self.direction == "down" and self.rect.y < 768 - self.rect.height:
            self.suby += self.speed
        elif self.direction == "left" and self.rect.x > 768 + 300:
            self.subx -= self.speed
        elif self.direction == "right" and self.rect.x < 974 - self.rect.width:
            self.subx += self.speed

        self.rect.x = round(self.subx / self.subpix)
        self.rect.y = round(self.suby / self.subpix)
