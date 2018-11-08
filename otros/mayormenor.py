#EPN-ESFOT
#ALGORITMOS FUNDAMENTALES
#mayormenor.py
#Version 2.1
#Autor: Stalin Maza

import random
from time import time 

def tres_menores(lista):
    temp = lista[1:4]    #funcion que me hace los tres menores
    return temp          #para esto le mando la lista y la ordeno

def tres_mayores(lista):
    temp = lista[1:4]      #funcion que me hace los tres menores
    return temp            #para esto le mando la lista y la ordeno
        
def generar2(cantidad,min,max):
    numeros = []
    while len(numeros) < cantidad:     #aqui genero los numeros randomicamente sin 
        numero = random.randint(min, max) #controlar si se repiten o no y me retorna una lista
        numeros.append(numero)  #Nota: para controlar deberiamos añadir un if dentro del
    return numeros              #while que verifico si el numero creado ya esta insertado

def main():
    min =100000   #numeros que dan la cantidad de la lista a crearse
    max = 1000000
    print("\t\tStalin Maza - Algoritmos Fundamentales\n")
    print("N","\t Tiempo de Ejecucion")
    for i in range(min,max,min):
        inicio = time()
        lista = generar2(i,min,max)
        tres_menores(sorted(lista))                 #aqui llamamos a las funciones enviandoles
        tres_mayores(sorted(lista, reverse = True)) #de parametros la lista creada randomicamente
        final = time()
        print(i ,"\t",final - inicio)  #imprimimos el tiempo que se demoro en ejecutar
    
    
main()
