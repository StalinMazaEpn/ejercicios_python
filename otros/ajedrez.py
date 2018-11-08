#STALIN MAZA
#ALGORITMOS FUNDAMENTALES
#PRUEBA MATRICES

import numpy as np

def tablero():
    a = [["-"] * 8 for i in range(8)]
    blanco = " "
    m = len(a) #numero filas
    n = len(a[0]) #numero columnas   
    for i in range(m):
        for j in range(n):
            if i%2==0 and j%2==0:                
                a[i][j] = blanco
            elif i%2!= 0 and j%2!= 0:                
                a[i][j] = blanco              
    b =np.array(a)
    print(b)    
    return b

def peones(m):
    for i in range(8):
        m [1][i] = "P"
        m [6][i] = "P"
    return m

def colocarF(m,a,b,c,d,e):
    m [a][b] = e
    m [a][c] = e
    m [d][b] = e
    m [d][c] = e
    return m

def reyes(m):
    m [0][4] = "R"
    m [7][4] = "R"
    m [0][3] = "Q"
    m [7][3] = "Q"
    return m
    
def ubicar(m):
    a1 = peones(m)
    a2 = colocarF(a1,0,0,7,7,"T") #TORRES
    a3 = colocarF(a2,0,1,6,7,"C") #CABALLOS
    a4 = colocarF(a2,0,2,5,7,"A") #ALFILES
    final = reyes(a4) #REYES
    print(final)

        
def main():
    print("\t\tInicio del Programa") 
    print ("Crea e imprime un tablero de ajedrez. Es un arreglo 8x8")
    print ("Los casilleros blancos contienen espacios en blanco")
    print ("Los casilleros negros contienen guiones -\n")
    a = tablero()

    print ("\nColoca las piezas de ajedrez en el tablero")
    print("en la posición de inicio del juego con estos codigos: ")
    print ("P=peón, T=torre, C=caballo, A=alfil, R=rey, Q=reina\n")
    ubicar(a)

main()
