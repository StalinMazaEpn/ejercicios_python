#STALIN MAZA
#ALGORITMOS FUNDAMENTALES
#PRUEBA MATRICES

import numpy as np

def blanco():
    a = [[" "] * 9 for i in range(9)]
    m = len(a) #numero filas
    n = len(a[0]) #numero columnas
    z = m-1
    for i in range(m):
        for j in range(n):
            if i == j:
                a[i][j] = "X"  #RECORRE EL ARREGLO Y LLENA DE X LAS POSICIONES QUE CUMPLAN
                a [i][z] = "X" #DICHA CONDICION
        z = z -1       
    b =np.array(a)
    print(b)

def aleatorio():
    a = np.random.randint(3, size=(3, 3))
    print(a)
    return a #CREA UN ARREGLO DE NUMEROS ALEATORIOS HASTA EL 3 DE FORMA 3*3
    print("------------------------------------------------------\n")
    
def fila_LLena(f):
    lleno = False    
    for i in range(3):        
        c1 = [0,0,0]
        c2 = [1,1,1]
        c3 = [2,2,2] #COMPARA LAS FILAS CON LOS ARREGLOS PUESTOS Y SI CUMPLE CONDICION ESTA LLENA
        if np.array_equal(f[i], c1) or np.array_equal(f[i], c2) or np.array_equal(f[i],c3):
            lleno = True
            print("Fila LLena")
            break 
            
    if lleno == False:
        print("Fila no LLena")

def col_LLena(m):
    f = m.transpose()
    lleno = False    
    for i in range(3):        
        c1 = [0,0,0]
        c2 = [1,1,1] #COMPARA LAS COLUMNAS CON LOS ARREGLOS PUESTOS Y SI CUMPLE CONDICION ESTA LLENA
        c3 = [2,2,2] #PARA ESTO INVERTIMOS LA MATRIZ PARA TRABAJAR MAS FACILMENTE
        if np.array_equal(f[i], c1) or np.array_equal(f[i], c2) or np.array_equal(f[i],c3):
            lleno = True            
            print("Columna Llena" )
            break 
            
    if lleno == False:
        print("Columna no LLena")

def diag_llena(m):
    lleno = False
    lado = "None"
    for i in range(3):
        if m[0,0] == i and m[1,1] == i and m[2,2] == i :
            lleno = True
            lado = "Izquierda"
            break
        elif m[2,0] == i and m[1,1] == i and m[0,2] == i : #CONDICIONA LAS DIAGONALES
            lleno = True
            lado = "Derecha"
            break
    if lleno == True:
        print("Diagonal ", lado," esta llena")
    else:
        print("Diagonales no llenas")


def main():
    print("\t\tInicio del Programa")   
    print ("\nCrea e imprime un arreglo 9x9 lleno de espacios en blanco")
    print ("excepto las dos diagonales que contienen X\n")
    blanco()

    print ("\nCrea e imprime un arreglo 3x3. El valor de cada casillero")
    print ("es generado aleatoriamente y puede ser 0, 1 o 2\n")
    f = aleatorio()

    print ("\nIndica si el arreglo anterior tiene al menos una fila, una columna")
    print ("o una diagonal con valores iguales - necesario para tres-en-raya\n")
    fila_LLena(f)
    col_LLena(f)
    diag_llena(f)

main()
