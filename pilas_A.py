import random

def esperar():
    msg=input ("...")

def imprimirPila(p):
    size=len(p)
    for i in range (size):
        #print (p[i])
        print (p[size - i- 1])

def main():
    cajas=[]
    print("cajas=",cajas)
    t=0
    #agrega elementos a la pila
    for i in range (4):
        x=int(100*random.random())
        cajas.append(x)               
    #   imprime la pila
        imprimirPila(cajas)
        esperar()    
#elimina un elemento de la pila

    for i in range (len(cajas)):
        cajas.pop()
        imprimirPila(cajas)
        esperar()
        
main()
    
    
