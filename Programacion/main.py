import pygame, sys
from pygame.locals import *
from pygame.sprite import Sprite, Group
import random as ra
import time
from organismo import *
from ambiente import *
from animal import *
from planta import *


# x = 560 
# x = 600 
# y = 640

# Inicializar Pygame
pygame.init()

# Crear ventana de Simulador
nRes = [1268, 760, 960]
screen = pygame.display.set_mode((nRes[0],nRes[1]))

clock = pygame.time.Clock()

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


#Icono y titulo
pygame.display.set_caption('Proyecto Final (Simulador Sabana)')
icono = pygame.image.load('Logo.ico')
pygame.display.set_icon(icono)


clock = pygame.time.Clock()



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
        self.myFont2 = pygame.font.SysFont("Calibri", 20)
    
    

    

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
    def textos(self):
        myFont = pygame.font.SysFont("Calibri", 30)

ciclos = 0
ciclos2 = 0
frecuencia = 1000

# Sprites
nubes = pygame.sprite.Group()

# Blucle de las nubes

for i in range(100):
    nube = Ambiente.Tormenta()
    nubes.add(nube)



#Crea animales

lista =[]
for i in range(0,4):
    lista.append(Cerdo(100, 25, "Omnivoro", ra.choice(["Mamifero", "Tulipan", "Herviboro", "Margaritas"]), ra.choice(["macho","hembra"])))
    lista.append(Tigre(100, 30, "Carnivoro", ra.choice(["Mamifero", "Herviboro"]), ra.choice(["macho","hembra"])))
    lista.append(Leopardo(100, 40, "Carnivoro", ra.choice(["Mamifero", "Herviboro"]), ra.choice(["macho","hembra"])))
    lista.append(Cebra(100, 20, "Herviboro", "Fotosintesis", ra.choice(["macho","hembra"])))
    lista.append(Jirafa(100, 10, "Herviboro", "Fotosintesis", ra.choice(["macho","hembra"])))
    lista.append(Elefante(100, 40, "Herviboro", "Fotosintesis", ra.choice(["macho","hembra"])))
    lista.append(Suricata(100, 40, "Insectivoro", ra.choice(["Tulipan", "Margaritas", "Insecto"]), ra.choice(["macho","hembra"])))
    lista.append(Insecto(100, 25, "Insecto", ra.choice(["Tulipan", "Margaritas"]), ra.choice(["macho","hembra"])))

# Agrega plantas alrededor del mapa
listaplantas = []
for i in range(0, 6):
    x = ra.randint(21, 24) * 40 + 1
    y = ra.randint(5, 6) * 40 + 1

    listaplantas.append(Planta2(x, y, 100, 12, "Tulipan", "Fotosintesis"))

for i in range(0, 5):
    x = ra.randint(0, 1) * 40 + 4
    y = ra.randint(3, 4) * 40 + 4

    listaplantas.append(Planta1(x, y, 100, 12, "Margaritas", "Fotosintesis"))

for i in range(0, 2):
    x = ra.randint(0, 1) * 40 + 4
    y = 18 * 40 + 4

    listaplantas.append(Planta2(x, y, 100, 12, "Tulipan", "Fotosintesis"))

for i in range(0, 20):
    x = ra.randint(19, 24) * 40 + 1
    y = ra.randint(12, 18) * 40 + 1

    listaplantas.append(Planta1(x, y, 100, 12, "Margaritas", "Fotosintesis"))
# Creacion animales
all_sprites = pygame.sprite.Group()
all_sprites.add(listaplantas , lista)
 

dibujado = Panel()


# Banderas de Eventos Climaticos
# lluvia
C_lluvia = 0
F_lluvia = 2
llover = False
V_lluvia = 2

# tormenta
C_Tormenta = 0
F_tormenta = 2
tormenta = False
V_tormenta = 2


# Hora
hora = 0
velocidad = 100

ciclos_lluvia = 0 
duracion_lluvia = 5 * ra.randint(24, 48)
gotas = [Ambiente.lluvia() for _ in range(500)]
duracion_tormenta = 5 * 96  # Define la duración de la tormenta en ciclos
ciclos_tormenta = 0





#contador de kills

plantas_muertas = 0
herviboros_muertos = 0
carnivoros_muertos = 0
omniboros_muertos = 0
insectos_muertos = 0
insectivoros_muertos = 0




# Bucle del Programa
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtener la hora actual
    hora = (ciclos // 60) % 240
    minutos = (ciclos % 60)

    # Ciclos
    ciclos += 1
    if ciclos >= 1440:
        hora += 1
        ciclos = 0
        for animal in lista:  # Itera sobre la lista de animales
            animal.vida -= 3
            if animal.vida <= 0:
                animal.movimiento = False
                animal.image = pygame.transform.flip(animal.image, False, True)

    # para que cada ciclo sea de 1 hora

    ciclos2 += 1

    ciclos_pantalla = ciclos2 // 60 # para que cada ciclo dure 1 hora

    dias = ciclos // 1440  # para que ocurra 

    # Cambiar el fondo según la hora
    if 4 <= hora < 5:
        fondo_actual = fondo5
    elif 5 <= hora < 6:
        fondo_actual = fondo4
    elif 6 <= hora < 7:
        fondo_actual = fondo3
    elif 7 <= hora < 8:
        fondo_actual = fondo2
    elif 8 <= hora < 12:
        fondo_actual = fondo
    elif 12 <= hora < 16:
        fondo_actual = fondo2
    elif 16 <= hora < 18:
        fondo_actual = fondo3
    elif 18 <= hora < 20:
        fondo_actual = fondo4
    elif 20 <= hora < 22:
        fondo_actual = fondo5
    else:
        fondo_actual = fondo6

        # Controlar eventos de los botones
    if event.type == MOUSEBUTTONDOWN and event.button == 1:
        boton_clickeado = dibujado.check_button_click(event)
        if boton_clickeado == "tormenta":
            tormenta = not tormenta
        elif boton_clickeado == "lluvia":
            llover = not llover

    # Dibujar la matriz
    screen.blit(fondo_actual, fondo_actual.get_rect())
    


    # Controlar la lluvia y la tormenta
    if ciclos % frecuencia == 0:
        evento_climatico = ra.choice(["lluvia", "tormenta"])
        if not (llover or tormenta):
            if evento_climatico == "lluvia":
                llover = True
            elif evento_climatico == "tormenta":
                tormenta = True
    
     # Mostrar lluvia o tormenta
    if llover and ciclos_lluvia < duracion_lluvia:
        for gota in gotas:
            gota.mostrar()
        ciclos_lluvia += 1
    else:
        llover = False

    if tormenta and ciclos_tormenta < duracion_tormenta:
        nubes.update()
        nubes.draw(screen)
        ciclos_tormenta += 1
    else:
        tormenta = False



    #Dibujar Lineas en la matriz 
    #Color, inicio y fin, resolucion, Grosor de linea
    for i in range(1, len(matriz)):
        pygame.draw.line(screen, (0, 0, 0), (0, i * celda), (1024, i * celda), 1)
    for j in range(1, len(matriz[0])):
        pygame.draw.line(screen, (0, 0, 0), (j * celda, 0), (j * celda, 768), 1)
    
   
    

    for sprite in all_sprites:
        colisiones = pygame.sprite.spritecollide(sprite, all_sprites, False)
        for colision in colisiones:
            if isinstance(colision, Animal) and isinstance(sprite, Animal):
                if colision.dieta == "Carnivoro" and sprite.dieta == ra.choice(["Herviboro", "Insectivoro", "Omnivoro"]):
                    sprite.kill()
                    herviboros_muertos +=1
                    insectivoros_muertos += 1
                    omniboros_muertos +=1
                elif colision.dieta == "Insectivoro" and sprite.dieta == "Insecto":
                    sprite.kill()
                    insectos_muertos +=1
                elif colision.dieta == "Omnivoro" and sprite.dieta == ra.choice(["Carnivoro", "Herviboro", "Insectivoro"]):
                    sprite.kill()
                    carnivoros_muertos +=1
                    herviboros_muertos +=1
            elif isinstance(colision, Animal) and isinstance(sprite, Planta):
                if colision.dieta == "Herviboro" and sprite.dieta == "Fotosintesis":
                    sprite.kill()
                    plantas_muertas += 1 
                if colision.dieta == "Omnivoro" and sprite.dieta == "Fotosintesis":
                    sprite.kill()
                    plantas_muertas += 1 

    for animal in lista:
        animal.update()
        nuevas_criaturas = animal.colision_y_reproduccion(lista)
        if nuevas_criaturas is not None:
            lista.append(nuevas_criaturas)





    all_sprites.draw(screen)
    all_sprites.update()


    
    dibujado.pintar()
    dibujado.botones()
    dibujado.textos()


    dia = dibujado.myFont.render(f'Dias: {dias:2d}', True, (220, 220, 220))
    screen.blit(dia, (1020, 20))
    texto_ciclos = dibujado.myFont.render(f'Ciclos: {ciclos_pantalla:2d}', True, (220, 220, 220))
    screen.blit(texto_ciclos, (1020, 50))
    tiempo = dibujado.myFont.render(f'Hora: {hora:02d}:{minutos:02d}', True, (220, 220, 220))
    screen.blit(tiempo, (1020, 80))
    tiempo = dibujado.myFont2.render(f'Plantas muertas : {plantas_muertas:01d}', True, (220, 220, 220))
    screen.blit(tiempo, (1020, 300))
    tiempo = dibujado.myFont2.render(f'Carnivoros muertos : {carnivoros_muertos:01d}', True, (220, 220, 220))
    screen.blit(tiempo, (1020, 320))
    tiempo = dibujado.myFont2.render(f'Herviboros muertos : {herviboros_muertos:01d}', True, (220, 220, 220))
    screen.blit(tiempo, (1020, 340))
    tiempo = dibujado.myFont2.render(f'Insectivoro muertos : {insectivoros_muertos:01d}', True, (220, 220, 220))
    screen.blit(tiempo, (1020, 360))
    tiempo = dibujado.myFont2.render(f'Insectos muertos : {insectos_muertos:01d}', True, (220, 220, 220))
    screen.blit(tiempo, (1020, 380))

    pygame.display.flip()
    clock.tick(40)
    
