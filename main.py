import pygame, sys
from pygame.locals import *
from pygame.sprite import Sprite
import random as ra
import time
from organismo import *
from animal import *
from planta import *

# Inicializar Pygame
pygame.init()

# Crear ventana de Simulador
nRes = [1268, 768, 960]
screen = pygame.display.set_mode((nRes[0],nRes[1]))

celda = 40

#colores de las celdas
matriz = [
    [(238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118)],
    [(238, 249, 118), (0, 149, 29), (0, 149, 29), (0, 149, 29), (0, 149, 29), (0, 149, 29), (0, 149, 29), (0, 149, 29), (238, 249, 118), (170, 253, 152), (238, 249, 118), (238, 249, 118), (170, 253, 152), (170, 253, 152), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (170, 253, 152),(238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118)],
    [(238, 249, 118), (0, 149, 29), (0, 149, 29), (0, 149, 29), (0, 149, 29), (0, 149, 29), (0, 149, 29), (0, 149, 29), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (170, 253, 152), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118)],
    [(238, 249, 118), (238, 249, 118), (238, 249, 118), (0, 149, 29), (238, 249, 118), (238, 249, 118), (238, 249, 118), (0, 149, 29), (238, 249, 118), (170, 253, 152), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (191, 191, 191), (191, 191, 191), (191, 191, 191), (170, 253, 152), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118)],
    [(238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (170, 253, 152), (170, 253, 152), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118)],
    [(238, 249, 118), (191, 191, 191), (238, 249, 118), (238, 249, 118), (191, 191, 191), (191, 191, 191), (191, 191, 191), (191, 191, 191), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118)],
    [(238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (191, 191, 191), (191, 191, 191), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118)],
    [(238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (170, 253, 152), (170, 253, 152), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118)],
    [(238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (191, 191, 191), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118)],
    [(238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118)],
    [(238, 249, 118), (191, 191, 191), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (170, 253, 152), (170, 253, 152), (238, 249, 118), (170, 253, 152), (170, 253, 152), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118)],
    [(238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (170, 253, 152), (170, 253, 152), (238, 249, 118), (238, 249, 118), (238, 249, 118), (170, 253, 152), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118)],
    [(238, 249, 118), (238, 249, 118), (238, 249, 118), (255, 255, 255 ), (255, 255, 255), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118)],
    [(238, 249, 118), (238, 249, 118), (238, 249, 118), (255, 255, 255 ), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (191, 191, 191), (238, 249, 118), (238, 249, 118), (238, 249, 118), (170, 253, 152), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118)],
    [(238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (170, 253, 152), (191, 191, 191), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (191, 191, 191), (191, 191, 191), (238, 249, 118), (238, 249, 118), (191, 191, 191), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118)],
    [(238, 249, 118), (238, 249, 118), (238, 249, 118), (255, 255, 255 ), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (191, 191, 191), (238, 249, 118), (238, 249, 118), (238, 249, 118), (170, 253, 152), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118)],
    [(238, 249, 118), (238, 249, 118), (238, 249, 118), (255, 255, 255 ), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (191, 191, 191), (238, 249, 118), (238, 249, 118), (238, 249, 118), (170, 253, 152), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118)],
    [(238, 249, 118), (238, 249, 118), (238, 249, 118), (255, 255, 255 ), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (191, 191, 191), (238, 249, 118), (238, 249, 118), (238, 249, 118), (170, 253, 152), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118)],
    [(238, 249, 118), (238, 249, 118), (238, 249, 118), (255, 255, 255 ), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (191, 191, 191), (238, 249, 118), (238, 249, 118), (238, 249, 118), (170, 253, 152), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118)],
    [(238, 249, 118), (238, 249, 118), (238, 249, 118), (255, 255, 255 ), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (191, 191, 191), (238, 249, 118), (238, 249, 118), (238, 249, 118), (170, 253, 152), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118), (238, 249, 118)],]

# Icono y titulo
pygame.display.set_caption('Proyecto Final (Simulador Sabana)')
icono = pygame.image.load('Logo.ico')
pygame.display.set_icon(icono)

# Imagen de fondo
fondo = pygame.image.load('map.png')
fondo_rect = fondo.get_rect()

# Ciclos
lluvia = False
Tormenta = False

#Clases 
class Panel:
    def __init__(self):
        self.ubicacionx = 800 + 200
        self.ubicaciony = 0
        self.ancho = 320
        self.a = 768
        self.tormenta_button = pygame.Rect(1060, 500, 150, 50)  # Botón de tormenta
        self.lluvia_button = pygame.Rect(1060, 400, 150, 50)  # Botón de tormenta
        self.myFont = pygame.font.SysFont("Calibri", 30)
    
    def pintar(self):
        a = pygame.Rect(self.ubicacionx, self.ubicaciony, self.ancho, self.a)
        screen.fill((52,52,52), a)

    def botones(self):
        # lluvia
        texto_lluvia = self.myFont.render("Lluvia", True, (220, 220, 220))
        pygame.draw.rect(screen, (70, 189, 34), self.lluvia_button, 0)
        screen.blit(texto_lluvia, (1100, 410))
        if self.lluvia_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (100, 220, 100), self.lluvia_button, 0)

        # tormenta
        texto_tormenta = self.myFont.render("Tormenta", True, (220, 220, 220))
        pygame.draw.rect(screen, (255, 0, 0), self.tormenta_button, 0)
        screen.blit(texto_tormenta, (1080, 510))
        if self.tormenta_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (255, 100, 100), self.tormenta_button, 0)

    def check_button_click(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if self.tormenta_button.collidepoint(pygame.mouse.get_pos()):
                return "tormenta"
            elif self.lluvia_button.collidepoint(pygame.mouse.get_pos()):
                return "lluvia"
        return False


class Ambiente:
    def __init__(self, counter):
        self.counter = 0
    class lluvia:
        #Constructor
        def __init__(self):
            #posicionx 
            self.x = ra.randint(0, 1024)
            #posiciony
            self.y = ra.randint(-200, -20)
            #Velocidad al caer en eje y
            self.yspeed = ra.uniform(1, 5)
            self.tamaño = ra.randint(10, 20)
            

        def mostrar(self):
            self.y += self.yspeed
            self.yspeed += 2

            if self.y > 768:
                self.y = ra.randint(-200, -20)
                self.yspeed = ra.uniform(5, 1)

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
            self.velocidad_x = ra.randrange(1 , 2) # Velocidad horizontal aleatoria

        def update(self):
            self.rect.x += self.velocidad_x
            if self.rect.right > nRes[2] + 100:
                self.rect.x = ra.randrange(-1000, 0)
                self.rect.y = ra.randrange(-30, 100)
                self.velocidad_x = ra.randrange(1 , 2) # Cambiar horizontal aleatoria



gotas = [Ambiente.lluvia() for _ in range(50)]
ciclos = 0

#Crea animales
lista =[]
for i in range(0,2):
    lista.append(Leon(100, 30, "Carnivoro", "sada"))
    lista.append(Leona(100, 40, "Carnivoro", "sada"))
    lista.append(Cebra(100, 20, "Herviboro", "sada"))
    lista.append(Cebra(100, 20, "Herviboro", "sada"))
    lista.append(Cerdo(100, 25, "Omnivoro", "Mamifero"))
    lista.append(Jirafa(100, 10, "Herviboro", "Mamifero"))
    lista.append(Elefante(100, 40, "Herviboro", "L. africana Blumenbach, 1797"))
    lista.append(Leopardo(100, 40, "Carnivoro", "sada"))
    lista.append(Leopardo(100, 40, "Carnivoro", "sada"))
    lista.append(Suricata(100, 40, "Insectivoro", "sada", "s"))
    lista.append(Jabali(100, 40, "Omnivoro", "sada", "s"))


# Agrega plantas alrededor del mapa
listaplantas = []
for i in range(0,10):
    listaplantas.append(Planta1(ra.randint(0, 950), ra.randint(0, 768), 100, 12))
    listaplantas.append(Planta2(ra.randint(0, 950), ra.randint(0, 768), 100, 12))

# Creacion animales
all_sprites = pygame.sprite.Group()
all_sprites.add(lista, listaplantas)


dibujado = Panel()

# Sprites
nubes = pygame.sprite.Group()

# Blucle de las nubes

for i in range(500):
    nube = Ambiente.Tormenta()
    nubes.add(nube)

# Banderas de Eventos Climaticos
llover = False
tormenta = False


# Hora
hora = 0
# Bucle del Programa
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Controlar eventos de los botones
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            boton_clickeado = dibujado.check_button_click(event)
            if boton_clickeado == "tormenta":
                tormenta = not tormenta
            elif boton_clickeado == "lluvia":
                llover = not llover

    # Dibujar la matriz
    screen.blit(fondo, fondo_rect)

    # Ciclos
    ciclos += 1
    if ciclos >= 1000:
        hora += 1
        ciclos = 0

    # Verificar eventos climáticos
    if hora > 10 and not llover and not tormenta:
        llover = True
        tormenta = False
        nubes.empty()  # Vaciar el grupo de nubes para que no se muestren durante la lluvia
    if hora > 20:
        llover = False
        tormenta = True

    #Dibujar la matriz
    screen.blit(fondo, fondo_rect)
    

    #Dibujar Lineas en la matriz 
    #Color, inicio y fin, resolucion, Grosor de linea
    for i in range(1, len(matriz)):
        pygame.draw.line(screen, (0, 0, 0), (0, i * celda), (1024, i * celda), 1)
    for j in range(1, len(matriz[0])):
        pygame.draw.line(screen, (0, 0, 0), (j * celda, 0), (j * celda, 768), 1)
    



    # Mostrar lluvia o tormenta
    if llover:
        for gota in gotas:
            gota.mostrar()

    all_sprites.draw(screen)
    all_sprites.update()

    if tormenta:
        nubes.update()
        nubes.draw(screen)

    for sprite in lista:
        colisiones = pygame.sprite.spritecollide(sprite, lista, False)
        for colision in colisiones:
            if isinstance(colision, Animal) and isinstance(sprite, Animal):
                if colision.dieta == "Carnivoro" and sprite.dieta == "Herviboro":
                    sprite.kill()

    dibujado.pintar()
    dibujado.botones()
    pygame.display.flip()