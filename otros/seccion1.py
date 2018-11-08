#STALIN MAZA
#ALGORITMOS FUNDAMENTALES
#PRUEBA MATRICES

import numpy as np

def unidimensional():
    matriz1 = np.arange(16,36)
    print(matriz1)
    print("------------------------------------------------------\n")
    
def arregloU():
    arreglo = np.ones(240).reshape(12,20)
    print(arreglo)
    print("------------------------------------------------------\n")

def aleatorio():
    a = np.random.randint(99, size=(3, 8))
    print(a)
    return a
    print("------------------------------------------------------\n")

def identidad():
    a = np.zeros(36).reshape(6,6) 
    m = len(a) #numero filas
    n = len(a[0]) #numero columnas    
    for i in range(m):
        for j in range(n):
            if i == j:
                a[i][j] = 1
    print(a)
    print("------------------------------------------------------\n")

def tri(b):
    a = b.reshape(2,3,4)
    print(a)
    print("------------------------------------------------------\n")

def main():
    print("\t\tInicio del Programa")    
    print ("Crea e imprime un arreglo de unidimensional con valores consecutivos del 16 al 35")
    unidimensional()
    print ("Crea e imprime un arreglo 12x20 lleno de unos")
    arregloU()
    print ("Crea un arreglo 6x6 lleno de ceros, pero con la diagonal llena de unos -matriz identidad")
    identidad()
    print ("Crea un arreglo 3x8 lleno de números enteros aleatorios con valores entre 0 y 99")
    B = aleatorio() 
    print ("Genera un arreglo tri-dimensional a partir del arreglo anterior")
    tri(B)

main()
