import numpy as np
from colorama import Fore, init

def arbol():
    filas = int(input("Ingresa el numero de Filas\n"))    
    columnas = (filas*2)-1           
    print("filas ",filas)
    print("columnas ",columnas)   
    matrizC = [[None] * columnas for i in range(filas)]      
    for n in range(filas):        
        matrizC = llenar(filas,matrizC,columnas,n)  
    final = np.array(matrizC)
    ultima = final.reshape(filas,columnas)
    init(autoreset=True)
    #print(ultima)
    print(Fore.GREEN + str(ultima))    
             
def salir():
    msg=input("Presione Enter para Salir: ")
            
def llenar(filas,matriz,columnas,n):
    esp = filas - n -1
    ast = 1 + (n*2)
    lista = ["*"] * (columnas)
    a = len(lista)- esp
    for i in range(esp):
        lista[i] = "."    
    for j in range(a,len(lista)):
        lista[j] = "." 
    for x in range(columnas):
        matriz[n][x] = lista[x]
    return matriz

def piramide ():
    #init(autoreset=True)
    filas = int(input("Ingresa el numero de Filas\n"))
    init(autoreset=True)
    for n in range(filas):
        espacios = filas - n -1
        asteriscos = 1 + (n*2)
        print(Fore.GREEN + " " * espacios + "*" * asteriscos)        
    t = int(filas/4)
    for i in range(t):
        print(Fore.GREEN + " " * (filas-2) + "*"*3)
        
def salir():
    msg=input("Presione Enter para Salir: ")
    
def main():
    piramide()
    arbol()
    print("FELIZ NAVIDAD :)")
    salir()
    
main() 
