#Algoritmos FUndamentales
#Stalin Maza

from time import time

def lista_append(n):
    inicio = time()
    lista = []
    for i in range(n):
        lista.append(i)

    fin = time()   
    return fin - inicio

#llenar lista mediante generador
def lista_generador(n):
    inicio = time()
    lista = [i for i in range(n)]
    fin = time()
    return fin - inicio

def main():
    print("n\t    Tiempo Duracion \t  Tiempo Generador")
    for i in range(10):
        n = i * 1000000
        print(n,"\t" , lista_append(n),"\t",lista_generador(n))
        
main()
