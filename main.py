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

# Ciro animado
image_path = "Ambiente/ciro.png"
image = pygame.image.load(image_path)
image_rect = image.get_rect()

# clase para crear el panel
class Panel:
    def __init__(self):
        self.ubicacionx = 800 + 200 # ubicacion en x
        self.ubicaciony = 0 # ubicacion en y
        self.ancho = 320 # ancho
        self.a = 768 # alto
        self.tormenta_button = pygame.Rect(1060, 300, 150, 50)  # Botón de tormenta
        self.lluvia_button = pygame.Rect(1060, 400, 150, 50)  # Botón de tormenta
        self.myFont = pygame.font.SysFont("Calibri", 30) # tipo de letra y tamaño
        self.myFont2 = pygame.font.SysFont("Calibri", 20) # lo mismo pero para otros datos
        
    def pintar(self):
        a = pygame.Rect(self.ubicacionx, self.ubicaciony, self.ancho, self.a) # crea el cuadrado en las coordenadas anteriores
        screen.fill((52,52,52), a) # pinta el panel de color gris

# ciclos para lluvia y tormenta y la frecuencia con la que esta ocurre
ciclos = 0
ciclos2 = 0
frecuencia = 500

# Sprites
nubes = pygame.sprite.Group()

# Blucle de las nubes
for i in range(150):
    nube = Ambiente.Tormenta()
    nubes.add(nube)

#musica
pygame.mixer.music.load('music.mp3') # Importa musica 
pygame.mixer.music.play(1)
pygame.mixer.music.set_volume(0.05) # nivel de volumen

#Crea animales
lista =[]
for i in range(0, 6):
    lista.append(Cerdo(100, 25, "Carnivoro", "Herviboro", ra.choice(["macho","hembra"])))
    lista.append(Tigre(100, 30, "Carnivoro", "Herviboro", ra.choice(["macho","hembra"])))
    lista.append(Leopardo(100, 40, "Carnivoro", "Herviboro", ra.choice(["macho","hembra"])))
    lista.append(Cebra(100, 20, "Herviboro", "Fotosintesis", ra.choice(["macho","hembra"])))
    lista.append(Jirafa(100, 10, "Herviboro", "Fotosintesis", ra.choice(["macho","hembra"])))
    lista.append(Insecto(100, 25, "Herviboro", "Fotosintesis", ra.choice(["macho","hembra"])))
    lista.append(Elefante(100, 40, "Herviboro", "Fotosintesis", ra.choice(["macho","hembra"])))
    lista.append(Suricata(100, 40, "Insectivoro", "Insecto", ra.choice(["macho","hembra"])))
 
# Agrega plantas alrededor del mapa
listaplantas = []
for i in range(0, 10):
    x = ra.randint(0, 11) * 40 + 1
    y = ra.randint(0, 8) * 40 + 1

    while x >= 960 or y >= 720:
        x = ra.randint(0, 11) * 40 + 1
        y = ra.randint(0, 8) * 40 + 1

    listaplantas.append(Planta1(x, y, 100, 12, "Tulipan", "Fotosintesis"))

for i in range(0, 10):
    x = ra.randint(12, 24) * 40 + 4
    y = ra.randint(0, 8) * 40 + 4

    while x >= 960 or y >= 720:
        x = ra.randint(12, 24) * 40 + 1
        y = ra.randint(0, 8) * 40 + 1
    listaplantas.append(Planta2(x, y, 100, 12, "Margaritas", "Fotosintesis"))

for i in range(0, 10):
    x = ra.randint(0, 11) * 40 + 4
    y = ra.randint(9, 18) * 40 + 4

    while x >= 960 or y >= 720:
        x = ra.randint(0, 11) * 40 + 1
        y = ra.randint(9, 18) * 40 + 1
    listaplantas.append(Planta2(x, y, 100, 12, "Tulipan", "Fotosintesis"))

for i in range(0, 10):
    x = ra.randint(12, 24) * 40 + 1
    y = ra.randint(9, 18) * 40 + 1

    while x >= 960 or y >= 720:
        x = ra.randint(12, 24) * 40 + 1
        y = ra.randint(9, 18) * 40 + 1
    listaplantas.append(Planta1(x, y, 100, 12, "Margaritas", "Fotosintesis"))

# Creacion animales
all_sprites = pygame.sprite.Group()
all_sprites.add(listaplantas , lista)
 

dibujado = Panel()

# Banderas de Eventos Climaticos
# lluvia
llover = False

# tormenta
tormenta = False

movimiento = True
# Hora
hora = 0
velocidad = 100

#contador de kills
muertes = 0
plantas_muertas = 0
vivos = (len(lista))
plantas_vivas = (len(listaplantas))

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

    # para que cada ciclo sea de 1 hora

    ciclos2 += 1

    ciclos_pantalla = ciclos2 // 60 # para que cada ciclo dure 1 hora

    dias = ciclos2 // 1440  # para que cada 24 ciclos avance 1 hora

    # Cambiar el fondo según la hora
    if 4 <= hora < 5:
        fondo_actual = fondo5
    elif 5 <= hora < 6:
        fondo_actual = fondo4
    elif 6 <= hora < 7:
        fondo_actual = fondo3
        for animal in lista:
            animal.despertar(all_sprites)
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
        for animal in lista:
            animal.dormir(all_sprites)

    # Dibujar la matriz
    screen.blit(fondo_actual, fondo_actual.get_rect())

    # Controlar la lluvia y la tormenta
    if ciclos % frecuencia == 0:
        evento_climatico = ra.choice(["lluvia", "tormenta"]) # que escoga uno a la vez
        if not (llover or tormenta): # no ocurran al mismo tiempo
            if evento_climatico == "lluvia":
                llover = True # activa la lluvia
                duracion_lluvia = 5 * ra.randint(24, 48)  # Define la duración de la lluvia
                ciclos_lluvia = 0 
                gotas = [Ambiente.lluvia() for _ in range(500)]
            elif evento_climatico == "tormenta":
                tormenta = True # activa la tormenta
                duracion_tormenta = 10 * ra.randint(24, 48) 
                ciclos_tormenta = 0
    
    #Dibujar Lineas en la matriz 
    #Color, inicio y fin, resolucion, Grosor de linea
    for i in range(1, len(matriz)):
        pygame.draw.line(screen, (0, 0, 0), (0, i * celda), (1024, i * celda), 1)
    for j in range(1, len(matriz[0])):
        pygame.draw.line(screen, (0, 0, 0), (j * celda, 0), (j * celda, 768), 1)
    
     # Mostrar lluvia o tormenta
    if llover and ciclos_lluvia < duracion_lluvia:
        for gota in gotas:
            gota.mostrar()
        ciclos_lluvia += 1
    else:
        llover = False

    if tormenta and ciclos_tormenta < duracion_tormenta:
        all_sprites.add(nubes)
        ciclos_tormenta += 1
    else:
        tormenta = False
        all_sprites.remove(nubes)

    for sprite in all_sprites: # inicia el ciclo en todos los sprites
        if (isinstance(sprite, Animal) or isinstance(sprite, Planta)) and hasattr(sprite, 'vivo') and sprite.vivo: # verifica si el sprite es animal o planta y si tiene un atributo llamado 'vivo' 
            colisiones = pygame.sprite.spritecollide(sprite, all_sprites, False) # detecta las colisiones en el sprite actual y todos los demás
            for colision in colisiones: # inicia un bucle a traves de cada sprite en la lista 'colisiones'
                # verifica si el sprite que colisiona es una instancia de la clase animal tiene un atributo llamado vivo
                if isinstance(colision, Animal) and hasattr(colision, 'vivo') and colision.vivo and isinstance(colision, Animal) and colision != sprite:
                    if (sprite.rect.x // 40 == colision.rect.x // 40 and sprite.rect.y // 40 == colision.rect.y // 40): #Para que la colision sea dentro de una casilla
                        if isinstance(colision, Animal) and isinstance(sprite, Animal):  # verifica si colisionaron los animales
                            if colision.dieta == "Insectivoro" and sprite.dieta == "Insecto": # verifica si los animales que se comen entre si
                                colision.vida += 50  # aumenta la vida
                                sprite.vivo = False # lo mata
                                muertes += 1 # aumenta el contador de muertes
                                vivos -= 1 # aumenta el contador de vivos
                        elif isinstance(colision, Animal) and isinstance(sprite, Planta): # colisione el animal con la planta
                            if colision.dieta == "Herviboro" and sprite.dieta == "Fotosintesis": # 
                                colision.vida += 50
                                sprite.kill()
                                plantas_muertas += 1
                                plantas_vivas -= 1
                            if colision.dieta == "Omnivoro" and sprite.dieta == "Fotosintesis":
                                colision.vida += 20
                                sprite.kill()
                                plantas_muertas += 1
                                plantas_vivas -= 1

    for sprite in all_sprites:
        if isinstance(sprite, Animal) and hasattr(sprite, 'vivo') and sprite.vivo:
            sprite.vida -= 0.01  
            if sprite.vida <= 0:
                sprite.vida = 0
                sprite.vivo = False
                muertes += 1
                vivos -= 1
            if sprite.vida < 90:
                colisiones = pygame.sprite.spritecollide(sprite, all_sprites, False)
            for colision in colisiones:
                if isinstance(colision, Animal) and hasattr(colision, 'vivo') and colision.vivo and isinstance(colision, Animal) and colision != sprite:
                    if (sprite.rect.x // 40 == colision.rect.x // 40 and sprite.rect.y // 40 == colision.rect.y // 40):
                        if isinstance(colision, Animal) and isinstance(sprite, Animal):
                            if colision.dieta == "Carnivoro" and sprite.dieta == ra.choice(["Herviboro", "Insectivoro", "Omnivoro"]):
                                colision.vida += 50
                                sprite.vivo = False
                                muertes += 1
                                vivos -= 1
                            elif colision.dieta == "Omnivoro" and sprite.dieta == ra.choice(["Carnivoro", "Herviboro", "Insectivoro"]):
                                colision.vida += 50
                                sprite.vivo = False
                                muertes += 1
                                vivos -= 1

    for sprite in all_sprites:
        if isinstance(sprite, Animal) and hasattr(sprite, 'vivo'):
            if sprite.vivo:
                if sprite.rect.collidepoint(pygame.mouse.get_pos()):
                    vida_porcentaje = (sprite.vida / 100.0) * 100
                    barrita = min(vida_porcentaje, 40)
                    pygame.draw.rect(screen, (255, 0, 0), (sprite.rect.x, sprite.rect.y - 10, 40, 5))
                    pygame.draw.rect(screen, (0, 255, 0), (sprite.rect.x, sprite.rect.y - 10, barrita, 5))
                    
    all_sprites.draw(screen)
    all_sprites.update()

    dibujado.pintar()
    screen.blit(image, (1000, 500))

    dia = dibujado.myFont.render(f'Dias: {dias:2d}', True, (220, 220, 220))
    screen.blit(dia, (1020, 20))
    texto_ciclos = dibujado.myFont.render(f'Ciclos: {ciclos_pantalla:2d}', True, (220, 220, 220))
    screen.blit(texto_ciclos, (1020, 50))
    tiempo = dibujado.myFont.render(f'Hora: {hora:02d}:{minutos:02d}', True, (220, 220, 220))
    screen.blit(tiempo, (1020, 80))
    tiempo = dibujado.myFont2.render(f'Animales Vivos : {vivos:02d}', True, (220, 220, 220))
    screen.blit(tiempo, (1020, 200))
    tiempo = dibujado.myFont2.render(f'Animales Muertos :  {muertes:01d}', True, (220, 220, 220))
    screen.blit(tiempo, (1020, 220))
    tiempo = dibujado.myFont2.render(f'Plantas Vivas : {plantas_vivas:02d}', True, (220, 220, 220))
    screen.blit(tiempo, (1020, 240))
    tiempo = dibujado.myFont2.render(f'Flores Muertas : {plantas_muertas:01d}', True, (220, 220, 220))
    screen.blit(tiempo, (1020, 260))
    tiempo = dibujado.myFont2.render('Se', True, (0, 0, 0))
    screen.blit(tiempo, (1050, 525))
    tiempo = dibujado.myFont2.render('Entiende?', True, (0, 0, 0))
    screen.blit(tiempo, (1025, 545))

    pygame.display.flip()
    clock.tick(60)
    