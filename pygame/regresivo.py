import pygame as pg
import random
import time

negro = (0,0,0)
verde = (0,200,0)
amarillo =(200,20,20) 
m = True
def regresivo(inicio):
    
    global m
    while m!= False:
        print(inicio)
        inicio = inicio -1
        if inicio <= 0:
            m = False            
        time.sleep(1)
        return inicio


def main():
    pg.init()
    pantalla = pg.display.set_mode((500,500))
    fuente1 = pg.font.SysFont("Arial",20,True,False)
    info = fuente1.render("Haga click sobre los recs",0,(255,255,255))
    salir = False
    reloj1 = pg.time.Clock()
    while salir != True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                salir = True            
        reloj1.tick(20)        
        pantalla.fill(negro)        
        pantalla.blit(info,(5,5))       
        segundos = str(regresivo(5))             
        contador = fuente1.render(segundos,0,(155,155,255))
        pantalla.blit(contador,(300,5))
        pg.display.update()

    pg.quit()

main()
