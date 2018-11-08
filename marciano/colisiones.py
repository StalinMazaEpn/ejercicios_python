# Mini-invaders, version 0.06
# (Comprobac. de colisiones)
# Parte de la intro a Pygame, por Nacho Cabanes
 
import pygame
from pygame.locals import *
 
pygame.init()
 
ancho = 800
alto = 600
velocidadX = 3
velocidadY = 3
terminado = False
 
pantalla = pygame.display.set_mode( (ancho, alto) )
pygame.key.set_repeat(1,25)
reloj = pygame.time.Clock()
 
imagenMarciano = pygame.image.load("spaceinvader.png")
rectanguloMarciano = imagenMarciano.get_rect()
rectanguloMarciano.left = 200
rectanguloMarciano.top = 100
 
imagenNave = pygame.image.load("nave.png")
rectanguloNave = imagenNave.get_rect()
rectanguloNave.left = ancho/2
rectanguloNave.top = alto-50
 
imagenUfo = pygame.image.load("ufo.png")
rectanguloUfo = imagenUfo.get_rect()
rectanguloUfo.top = 20
 
imagenDisparo = pygame.image.load("disparo.png")
rectanguloDisparo = imagenDisparo.get_rect()
disparoActivo = False
marcianoVisible = True      # Nuevo en la version 0.06
ufoVisible = True           # Nuevo en la version 0.06
 
while not terminado:
    # ---- Comprobar acciones del usuario ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT: terminado = True
 
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        rectanguloNave.left -= 8
    if keys[K_RIGHT]:
        rectanguloNave.left += 8
    if keys[K_SPACE] and not disparoActivo:
        disparoActivo = True
        rectanguloDisparo.left = rectanguloNave.left + 18
        rectanguloDisparo.top = rectanguloNave.top - 25
 
    # ---- Actualizar estado ----
    rectanguloMarciano.left += velocidadX
    rectanguloMarciano.top += velocidadY
    if rectanguloMarciano.left < 0 or rectanguloMarciano.right > ancho:
        velocidadX = -velocidadX
    if rectanguloMarciano.top < 0 or rectanguloMarciano.bottom > alto:
        velocidadY = -velocidadY
 
    rectanguloUfo.left += 2
    if rectanguloUfo.right > ancho:
        rectanguloUfo.left = 0
 
    if disparoActivo:
        rectanguloDisparo.top -= 25 #controla velocidad disparo
        if rectanguloDisparo.top <= 0:
            disparoActivo = False
 
    # ---- Comprobar colisiones ----
    if marcianoVisible:                                        # Nuevo en 0.06
        if rectanguloNave.colliderect( rectanguloMarciano ):   # Nuevo en 0.06
            terminado = True                                   # Nuevo en 0.06
 
        if disparoActivo:                                        # Nuevo en 0.06
            if rectanguloDisparo.colliderect( rectanguloMarciano): # Nuevo en 0.06
                marcianoVisible = False                          # Nuevo en 0.06
                disparoActivo = False                            # Nuevo en 0.06
 
    if disparoActivo:                                      # Nuevo en 0.06
        if rectanguloDisparo.colliderect( rectanguloUfo) : # Nuevo en 0.06
            ufoVisible = False                             # Nuevo en 0.06
            disparoActivo = False                          # Nuevo en 0.06
 
    if not ufoVisible and not marcianoVisible:             # Nuevo en 0.06
        terminado = True                                   # Nuevo en 0.06
 
    # ---- Dibujar elementos en pantalla ----
    pantalla.fill( (0,0,0) )
    if marcianoVisible:                                    # Nuevo en 0.06
        pantalla.blit(imagenMarciano, rectanguloMarciano)
    if ufoVisible:                                         # Nuevo en 0.06
        pantalla.blit(imagenUfo, rectanguloUfo)
    if disparoActivo:
        pantalla.blit(imagenDisparo, rectanguloDisparo)
    pantalla.blit(imagenNave, rectanguloNave)
    pygame.display.flip()
 
    # ---- Ralentizar hasta 40 fotogramas por segundo  ----
    reloj.tick(40)
 
# ---- Final de partida ----
pygame.quit()
