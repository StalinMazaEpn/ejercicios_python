#Escuela Politecnica Nacional
#Programacion Avanzada
#Matrices - Stalin Maza
#Version 1.0
import sys
def suma_matrices():
    matriz1 = [[4,5,6,7,8],[3,5,7,9,11],[2,12,22,32,42],
    [4,4,4,4,4],[1,4,7,10,13]]
    matriz2 = [[7,7,7,7,7],[9,9,9,9,9],[8,8,8,8,8],
    [1,6,11,16,21],[5,5,5,5,5]]
    matrizC = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    for i in range(len(matriz1)):
        for j in range(len(matriz2)):
            a = matriz1[i][j]
            b = matriz2[i][j]
            matrizC[i][j] = (a+b)
            #print(a)
    print("Esta es la primera matriz:\n", matriz1)
    print("Esta es la segunda matriz:\n",matriz2)
    print("Esta es la matriz resultante:\n",matrizC)
    repetir()
    #Esta funcion realiza la suma de dos matrices 5 * 5 con datos quemados
    #puede cambiarse para que sea el usuario el que llene pero el principio es
    #el mismo.
def numero_par():
    valor =int(input("Ingrese un numero\n"))
    if valor < 0:
        print("Numeros Negativos no Funcionan")
        sys.exit()
    if(valor%2 == 0):
         print(valor , "es par")
    else:
         print(valor ,"no es par")
    repetir()
    #Esta funcion realiza el calculo de un numero par con el uso del "%".

def numero_cinco():
    numero =int(input("Ingrese un numero\n"))
    if numero == 0:
        print("Cero no es un divisor valido")
        sys.exit()
    if numero < 0:
        print("Numeros Negativos no Funcionan")
        sys.exit()
    if(numero%5 == 0):
         print(numero , "es divisible para 5")
    else:
         print(numero ,"no es divisible para 5")
    repetir()
    #Esta funcion realiza el calculo de un numero divisible para el numero 5
    #con el uso del "%".

def repetir():
    escoger = input("Ingrese S si desea continuar o N si desea salir\n")
    while escoger == "S" or escoger == "s":
        menu()
    print ("Programa Terminado")
    sys.exit()
    #aqui se realiza la repeticion del menu utilizando un bucle while

def switch(opcion):
    if opcion == 1:
        suma_matrices()
    elif opcion == 2:
        numero_par()
    elif opcion == 3:
        numero_cinco()
    elif opcion == 4:
        sys.exit()
    else :
        print("Opcion no corresponde al sistema")
        repetir()
        #Este es el switch donde de acuerdo a lo que escoge el usuario se
        #realiza alguna accion.

def menu():
    print("\tBienvenido al Menu de Funciones.")
    print("Escoga la Opcion que desee realizar: ")
    print("  1. Suma de Matrices 5*5")
    print("  2. Determinar si un numero es par")
    print("  3. Determinar si un numero es divisible para 5")
    print("  4. Salir")
    opcion = int(input())
    switch(opcion)
    #Aqui esta la impresion del menu y la llamada al switch

def main():
    menu()
    #la funcion principal que realiza la llamada a las demas funciones.

main()
