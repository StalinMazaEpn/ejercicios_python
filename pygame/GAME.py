#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escrito por Daniel Fuentes B.
# Licencia: X11/MIT license http://www.opensource.org/licenses/mit-license.php
# https://www.pythonmania.net/es/2010/03/25/tutorial-pg-2-ventana-e-imagenes/

# ---------------------------
# Importacion de los módulos
# ---------------------------

import pygame as pg
from pygame.locals import *
import sys

# Constantes
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------

# ------------------------------
# Funcion principal del juego
# ------------------------------

def main():
    pg.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("tutorial pg parte 2")

    # cargamos el fondo y una imagen (se crea objetos "Surface")
    fondo = pg.image.load("fondo.jpg").convert()
    tux = pg.image.load("tux.png").convert_alpha()   

    # el bucle principal del juego
    salir = False
    while salir != True:
        # Posibles entradas del teclado y mouse
        for event in pg.event.get():
            if event.type == pg.QUIT:
                salir = True
         # Indicamos la posicion de las "Surface" sobre la ventana
        screen.blit(fondo, (0, 0))
        screen.blit(tux, (550, 200))
        # se muestran lo cambios en pantalla
        pg.display.flip()
        
    pg.quit()   


main()
