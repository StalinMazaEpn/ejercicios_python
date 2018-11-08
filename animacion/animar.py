#!/usr/bin/env python
# _*_ coding: utf-8 _*_ 
import pygame
import sys
from pygame.locals import *


def imagen(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error as message:
            raise SystemExit(message)
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image


def escoger(r,imagen):
    imgs = []
    sheet = pygame.image.load(imagen).convert()
    colorkey = sheet.get_at((0, 0))
    sheet.set_colorkey(colorkey, RLEACCEL)
    for i in r:
        rTmp = Rect(i)
        imgTmp = pygame.Surface(rTmp.size, flags=pygame.SRCALPHA).convert_alpha()
        imgTmp.blit(sheet, (0, 0), rTmp)  
        imgs.append( imgTmp )
    print(imgs,"img____s",type(imgs))
    return imgs      


def mover_personaje(imagen):
    teclado = pygame.key.get_pressed()        
    izquierda = [(0,0,34,61),(33,0,45,61),(75,0,55,61),(130,0,40,61),
                (170,0,45,61),(220,0,45,61),(270,0,44,61),(310,0,43,61),(352,0,45,61)]
    derecha = [(380,0,45,61),(337,0,44,61),(285,0,51,61),(245,0,40,61),
                (200,0,45,61),(150,0,40,61),(105,0,40,61),(62,0,40,61),(20,0,40,61)]
    print("IZQUIERDA",len(izquierda))
    print("DERECHA",len(derecha))
    
    numero = 0

    imgs = []
    imgs2 = []
    sheet = pygame.image.load(imagen).convert()
    colorkey = sheet.get_at((0, 0))
    sheet.set_colorkey(colorkey, RLEACCEL)
    #for i in r:
    #    rTmp = Rect(i)
     #   imgTmp = pygame.Surface(rTmp.size, flags=pygame.SRCALPHA).convert_alpha()
      #  imgTmp.blit(sheet, (0, 0), rTmp)  
       # imgs.append( imgTmp )
    #print(imgs,"img____s",type(imgs))

    for i in derecha:
                rTmp = Rect(i)
                imgTmp = pygame.Surface(rTmp.size, flags=pygame.SRCALPHA).convert_alpha()
                imgTmp.blit(sheet, (0, 0), rTmp)  
                imgs2.append( imgTmp )

    
    if teclado[K_RIGHT] : # ubicacionp1 <=860 detecta colision en pared derecha
            #a = escoger(derecha)
            numero = 1
            for i in derecha:
                rTmp = Rect(i)
                imgTmp = pygame.Surface(rTmp.size, flags=pygame.SRCALPHA).convert_alpha()
                imgTmp.blit(sheet, (0, 0), rTmp)  
                imgs.append( imgTmp )
    elif teclado[K_LEFT] :
            #b = escoger(izquierda)   
            numero = 2
            for i in izquierda:
                rTmp = Rect(i)
                imgTmp = pygame.Surface(rTmp.size, flags=pygame.SRCALPHA).convert_alpha()
                imgTmp.blit(sheet, (0, 0), rTmp)  
                imgs.append( imgTmp )
    print(imgs2,"img2____s","tipo",type(imgs2))
    return imgs2
    
    
    """posicionDer[0]=(0,0,34,61)#posicion de cada sprite x,y, ancho, alto
    posicionDer[1]=(33,0,45,61)
    posicionDer[2]=(75,0,55,61)
    posicionDer[3]=(130,0,40,61)
    posicionDer[4]=(170,0,45,61)
    posicionDer[5]=(220,0,45,61)
    posicionDer[6]=(270,0,44,61)
    posicionDer[7]=(310,0,43,61)
    posicionDer[8]=(352,0,45,61)
   
    posicionIzq[0]=(380,0,45,61)
    posicionIzq[1]=(337,0,44,61)
    posicionIzq[2]=(285,0,51,61)
    posicionIzq[3]=(245,0,40,61)
    posicionIzq[4]=(200,0,45,61)
    posicionIzq[5]=(150,0,40,61)
    posicionIzq[6]=(105,0,40,61)
    posicionIzq[7]=(62,0,40,61)
    posicionIzq[8]=(20,0,40,61)"""

    

    
class Nave(pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen=imagen 
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left
    def mover(self,vx,vy):
       self.rect.move_ip(vx,vy)
    def update(self,superficie):
        superficie.blit(self.imagen,self.rect)



def main(): 
    pygame.init()
    print("Inicio")
    screen = pygame.display.set_mode((320, 200))
    imgN=pygame.image.load("p1.png").convert_alpha()
    nave1=Nave(imgN)
    sheet = pygame.image.load('character.png').convert()
    colorkey = sheet.get_at((0, 0))
    sheet.set_colorkey(colorkey, RLEACCEL)

    imgs = []
    print("Inicio2")
    personaje1= imagen('personaje1.png',True)#sprites personaje1
    personaje1_inv= pygame.transform.flip(personaje1,True,False);
    print("Inicio3")   
    r = [(0, 0, 64, 64), (64, 0, 64, 64), (128, 0, 64, 64) ] # (x, y, w, h)  
    for i in r:
        rTmp = Rect(i)
        imgTmp = pygame.Surface(rTmp.size, flags=pygame.SRCALPHA).convert_alpha()
        imgTmp.blit(sheet, (0, 0), rTmp)  
        imgs.append( imgTmp )



    print(len(r))
    print("imgs_primero",imgs,len(imgs),"typo",print(type(imgs)))
    contador = 0
    y = 0
    mover = 0
    cm = mover_personaje("personaje1.png")
    print("ccm",type(cm))
    salir = False

    ggg = 0
    h = 0
    while salir != True:
        #screen.fill((0,255,0))
        #screen.blit(imgs[contador], (0,y))
        for e in pygame.event.get():
            if e.type == QUIT:
                salir = True
                #sys.exit(0)
            elif e.type == KEYDOWN:            
                if e.key == K_w:
                    mover = 1                
                    print("mover",mover)
                    if contador < 2:
                        contador = contador + 1
                        y = y + 1
                        nave1.mover(0,mover)
                    else:
                        contador = 0
                if e.key == K_RIGHT:
                    if ggg < 7:
                        ggg = ggg+1                        
                        h = h + 1
                    else:                        
                        ggg = 0                
                mover = 0
                print("CONTADOR",contador,y)
                print("ggg",ggg)
                print("hhh",h)
        #nave1.update(screen)
        screen.fill((0,255,0))
        screen.blit(imgs[contador], (0,y))
        screen.blit(cm[ggg],(h,0))        
        #h = h + 1
        pygame.display.flip()
    pygame.quit()

main()
