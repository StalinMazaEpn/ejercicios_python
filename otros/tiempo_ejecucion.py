#time_it.py
#mide el tiempo de ejecucion de algun algoritmo
from time import time

def duracion(i,n):
    #captura la hora inicial
    inicio = time()
    #ejecuta algo
    j = 0
    for i in range(n):
        for k in range(int(n/2)):
            j = j+i
    #captura la hora final
    final = time()
    return final - inicio

def main():
    print("n\t duracion(n)")
    for i in range(50):
          n = i * 100
          print(n," ",duracion(i,n))
    
main()
