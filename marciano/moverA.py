# Mini-invaders, version 0.03
# (Imagen con teclado e imagen que rebota a la vez)
# Parte de la intro a Pygame, por Nacho Cabanes
 
import pygame
from pygame.locals import *    # Nuevo en la version 0.03
 
pygame.init()
 
ancho = 800
alto = 600
velocidadX = 1
velocidadY = 0
terminado = False
reloj = pygame.time.Clock()
 
pantalla = pygame.display.set_mode( (ancho, alto) )
pygame.key.set_repeat(1,50)    # Nuevo en la version 0.03
 
imagenMarciano = pygame.image.load("spaceinvader.png")
rectanguloMarciano = imagenMarciano.get_rect()
rectanguloMarciano.left = 1
rectanguloMarciano.top = 1
 
imagenNave = pygame.image.load("ufo.png")    # Nuevo en 0.03
rectanguloNave = imagenNave.get_rect()       # Nuevo en 0.03
rectanguloNave.left = ancho/2                # Nuevo en 0.03
rectanguloNave.top = alto-50                 # Nuevo en 0.03
 
imagenDisparo = pygame.image.load("disparo.png")    # Nuevo en 0.05
rectanguloDisparo = imagenDisparo.get_rect()        # Nuevo en 0.05
disparoActivo = False                               # Nuevo en 0.05

imagenDisparo2 = pygame.image.load("disparo.png")    # Nuevo en 0.05
rectanguloDisparo2 = imagenDisparo2.get_rect()        # Nuevo en 0.05
disparoActivo2 = False  

volver = True
 
while not terminado:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: terminado = True
 
    keys = pygame.key.get_pressed()          # Nuevo en 0.03         
    if keys[K_LEFT]:                         # Nuevo en 0.03
        rectanguloNave.left -= 3             # Nuevo en 0.03
    if keys[K_RIGHT]:                        # Nuevo en 0.03
        rectanguloNave.left += 3             # Nuevo en 0.03


    if   not disparoActivo2:         # Nuevo en 0.05
        disparoActivo2 = True                        # Nuevo en 0.05
        rectanguloDisparo2.left = rectanguloMarciano.left + 18  # Nuevo en 0.05
        rectanguloDisparo2.bottom = rectanguloMarciano.bottom - 10
        
 
    if keys[K_SPACE] and not disparoActivo:         # Nuevo en 0.05
        disparoActivo = True                        # Nuevo en 0.05
        rectanguloDisparo.left = rectanguloNave.left + 18  # Nuevo en 0.05
        rectanguloDisparo.top = rectanguloNave.top - 25              
    
    rectanguloMarciano.left += 3   
    if  rectanguloMarciano.right > ancho:
        rectanguloMarciano.left = 0

    if disparoActivo:                      # Nuevo en 0.05
        rectanguloDisparo.top -= 4        # Nuevo en 0.05
        b = rectanguloDisparo.top 
        print("b: ",b)
        if rectanguloDisparo.top <= 0:     # Nuevo en 0.05
            disparoActivo = False
            #volver = False

    if disparoActivo2 == True:                      # Nuevo en 0.05
        rectanguloDisparo2.bottom += 4 # Nuevo en 0.05
        c = rectanguloDisparo2.bottom
        d = rectanguloDisparo2.bottom
        print("c: ",c)
        c = c+1
        if c <= 0:     # Nuevo en 0.05
            print("c_metido",c)
            disparoActivo2 = False
       
        print("d:" ,d)
        if d >600:
            disparoActivo2 = False
     
    pantalla.fill( (0,0,0) )
    pantalla.blit(imagenMarciano, rectanguloMarciano)
    if disparoActivo:                      # Nuevo en 0.05
        pantalla.blit(imagenDisparo, rectanguloDisparo)  # Nuevo en 0.05
    if disparoActivo2:                      # Nuevo en 0.05
        pantalla.blit(imagenDisparo2, rectanguloDisparo2) 
    pantalla.blit(imagenNave, rectanguloNave)    # Nuevo en 0.03
    pygame.display.flip()
    reloj.tick(40)
 
pygame.quit()
