# Mini-invaders, version 0.05
# (Disparo al pulsar Espacio)
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
 
imagenDisparo = pygame.image.load("disparo.png")    # Nuevo en 0.05
rectanguloDisparo = imagenDisparo.get_rect()        # Nuevo en 0.05
disparoActivo = False                               # Nuevo en 0.05
 
while not terminado:
    # ---- Comprobar acciones del usuario ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT: terminado = True
 
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        rectanguloNave.left -= 4
    if keys[K_RIGHT]:
        rectanguloNave.left += 4
    if keys[K_SPACE] and not disparoActivo:         # Nuevo en 0.05
        disparoActivo = True                        # Nuevo en 0.05
        rectanguloDisparo.left = rectanguloNave.left + 18  # Nuevo en 0.05
        rectanguloDisparo.top = rectanguloNave.top - 25    # Nuevo en 0.05
 
    # ---- Actualizar estado ----
    rectanguloMarciano.left += velocidadX
    rectanguloMarciano.top += velocidadY
    if rectanguloMarciano.left < 0 or rectanguloMarciano.right > ancho:
        velocidadX = -velocidadX
    if rectanguloMarciano.top < 0 or rectanguloMarciano.bottom > alto:
        velocidadY = -velocidadY
 
    rectanguloUfo.left += 3
    if rectanguloUfo.right > ancho:
        rectanguloUfo.left = 0
 
    if disparoActivo:                      # Nuevo en 0.05
        rectanguloDisparo.top -= 4         # Nuevo en 0.05
        if rectanguloDisparo.top <= 0:     # Nuevo en 0.05
            disparoActivo = False          # Nuevo en 0.05
 
    # ---- Dibujar elementos en pantalla ----
    pantalla.fill( (0,0,0) )
    pantalla.blit(imagenMarciano, rectanguloMarciano)
    pantalla.blit(imagenUfo, rectanguloUfo)
    if disparoActivo:                      # Nuevo en 0.05
        pantalla.blit(imagenDisparo, rectanguloDisparo)  # Nuevo en 0.05
    pantalla.blit(imagenNave, rectanguloNave)
    pygame.display.flip()
 
    # ---- Ralentizar hasta 40 fotogramas por segundo  ----
    reloj.tick(40)
 
pygame.quit()
