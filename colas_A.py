from time import time
import random

def esperar():
    msg=input("...")

def duracion(n):
    inicio = time()
    j = 0
    for i in range(n):
        for k in range(int(n/2)):
            j = j + k
    fin = time()    

def main():
    clientes = []
    print("CLIENTES",clientes)
    t=0
    for i in range(10):
        r=int(10*random.random())
        print("r=",r)
        if r< 9:
            x = int(100*random.random())
            clientes.append(x)
            
        print(i,"\tClientes",clientes)
        esperar()

        t=t+1
        if t ==2:
            if len(clientes)>0:
                clientes.pop(0)
            t=0

    #for i in range(10):
     #   clientes.pop(0)
      #  print(i,"\tClientes",clientes)
       # esperar()



main()
