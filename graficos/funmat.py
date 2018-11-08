#Algoritmos Fundamentales
#funmat.py
#Version 2.2
#Graficas de diferentes funciones.
#Autor: Stalin Maza
#2016-Nov-13
#Importando la libreria PYLAB de la Biblioteca matplotlib
#Ver Nota al Final

import pylab as pl    #librerias necesarias para graficar
import numpy as np
import sys            #libreria para poder usar el sys.exit()
#FUNCIONES  MATEMATICAS
def cuad(i1,i2):
    a = int(input("Ingrese el valor A\n"))
    b = int(input("Ingrese el valor B\n")) #pidiendo valores para las variables
    c = int(input("Ingrese el valor C\n"))
    x = np.arange(i1,i2,0.5)               #dandole un rango de valores que tome X
    y = ((a*(x* x))+(b*x)+c)               #calculando valores en Y de acuerdo a los X
    imprimir(x,y,"ax^2+bx+c")              #imprimiendo la grafica dandole un titulo

def lineal(i1,i2):     
    m = int(input("Ingrese el valor M\n"))
    b = int(input("Ingrese el valor de C\n"))   #pidiendo valores para las variables
    x = np.arange(i1,i2,0.5)                    #dandole un rango de valores que tome X
    y = (m*x)+b                                 #calculando valores en Y de acuerdo a los X
    imprimir(x,y,"mx+b")                        #imprimiendo la grafica dandole un titulo

def expon(i1,i2):
    a = int(input("Ingrese el valor a\n"))    #pidiendo valores para las variable
    x = np.arange(i1,i2,0.5)                  #dandole un rango de valores que tome X
    y = a * np.exp(x)                         #calculando valores en Y de acuerdo a los X
    imprimir(x,y,"a*e(x)")                    #imprimiendo la grafica dandole un titulo

def logarit():
    m = int(input("Ingrese el valor minimo del rango de X\n"))   #pidiendo valores para el rango que tomara X
    n = int(input("Ingrese el valor maximo del rango de X\n"))
    if m <= 0:                                                   #comprobando que no inserten numeros menores
        print("El logaritmo solo acepta numeros mayores que O")  #o iguales a 0 porque logaritmica no acepta eso
        return 0
    else:
        x = np.arange(m,n,0.1)   #dandole un rango de valores que tome X de acuerdo a lo ingresado anteriormente
        y = np.log(x)            #calculando valores en Y de acuerdo a los X
        imprimir(x,y,"log(X)")   #imprimiendo la grafica dandole un titulo 


def menu():
    print("\tBienvenido al Menu de Grafica de Funciones en Python")
    print("1. Lineal")
    print("2. Cuadratica")   #Este es la funcion que imprime el menu y 
    print("3. Exponencial")  #llama al switch de acuerdo a la opcion escogida
    print("4. Logaritmica")
    print("5. Salir")
    opcion = int(input("Ingrese la opcion que desea:\n"))
    switch(opcion)
       
def repetir():
    escoger = input("Ingrese S si desea continuar o N si desea salir\n")
    while escoger == "S" or escoger == "s":
        menu()          #afuncion donde damos la opcion al usuario de si desea continuar en el programa
    print ("Programa Terminado")
    sys.exit()
            
def switch(opcion):    
    if opcion == 1:
        lineal(-5,5)
        repetir()
    elif opcion == 2:
        cuad(-5,5)
        repetir()
    elif opcion == 3:      #funcion donde realizamos las opciones del switch
        expon(-5,5)        #de acuerdo a lo que escoga el usuario
        repetir()
    elif opcion == 4:
        logarit()
        repetir()
    elif opcion == 5 :
        sys.exit()
    else :
        menu()

def imprimir(x,y,name):
    pl.suptitle("Graficando Funciones en Python")
    pl.plot(x,y,color="blue",)    #Datos a Graficar y Color de la Linea A Graficar.
    pl.title(name)                #Nombre del Grafico
    pl.xlabel('X')                #Da un nombre al Eje X
    pl.ylabel('Y')                #Da un nombre al Eje Y
    pl.axvline(0, color = 'g')    #dibuja una linea en el eje X
    pl.axhline(0, color = 'g')    #dibuja una linea en el eje Y
    pl.show()                     #muestra el grafico
        
def main():
    menu()    #funcion que llama a la impresion del menu

main()

#Nota:
#Para Instalar la libreria matplotlib usamos estos comandos en el CMD de Windows.
#pip install matplotlib (ENTER)           #esta nos sirve para instalar la libreria
#python -m pip install --upgrade pip"""   #esta nos sirve para actualizar
                                          #el instalador paquetes de python
