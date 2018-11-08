#EPN-ESFOT
#ALGORITMOS FUNDAMENTALES
#TIEMPOS EJECUCION DE UN SCRIPT
#STALIN MAZA
#VERSION 3.2
from time import time   #importamos la libreria time 

def fact_recursivo(n):  #en esta funcion recursiva se plantea un caso base
    if n <= 1:          #un caso base cuando es <= 1 para que nos retorne 1
        return 1        #y en el otro caso retorna el valor n multiplicado por
    else:               #la misma funcion recursiva pero con valor de n-1        
        return n * fact_recursivo(n-1)

def fact_iterativo(n):
    factorial = 1       #en esta funcion iterativa realizamos un bucle for que se
    for i in range(n):  #repite hasta el valor n donde la variable factorial es igual
        factorial *= (i + 1) #a la misma variable multiplicada por la suma del valor de (i+1)
    return factorial

def main():    
    temp = 0
    temp2 = 0  #variables a utilizar para mostrar datos
    limite = 20
    print("\t\tALGORITMO RECURSIVO")
    print("n","\tResultado","\t\tTiempo Transcurrido") #IMPRESION DEL FACTORIAL RECURSIVO
    inicio = time() #GUARDANDO EL TIEMPO INICIAL
    for n1 in range(limite):  #BUCLE QUE LE DA VALORES HASTA EL LIMITE ESTABLECIDO
        temp = fact_recursivo(n1) #GUARDANDO EL VALOR DEL FACTORIAL DE N
        final = time()            #GUARDANDO EL TIEMPO FINAL
        print(n1,"\t",temp,"\t\t",final - inicio)
    print("\t\tALGORITMO ITERATIVO")
    print("n","\tResultado","\t\tTiempo Transcurrido") #IMPRESION DEL FACTORIAL ITERATIVO
    inicio2 = time() #GUARDANDO EL TIEMPO INICIAL
    for n2 in range(limite):     #BUCLE QUE LE DA VALORES HASTA EL LIMITE ESTABLECIDO
        temp2 = fact_iterativo(n2)  #GUARDANDO EL VALOR DEL FACTORIAL DE N 
        final2 = time()             #GUARDANDO EL TIEMPO FINAL
        print(n2,"\t",temp2,"\t\t",final2 - inicio2)   
            
main()
