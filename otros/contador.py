import time

i = 0
m =  True

from tkinter import Label

def contador(limite):
    global m
    while m != False:
        global i        
        print("Tiempo Limite: " , i)
        i = i + 1
        if i >=limite+1:
            m = False
        time.sleep(1)
        
def regresivo(inicio):    
    m =  True
    while m!= False:
        print("Tiempo Limite: " , inicio)
        inicio = inicio -1
        if inicio <= 0:
            m = False
        time.sleep(1)   
    
#contador(5)
#regresivo(6)
regresivo(60)

