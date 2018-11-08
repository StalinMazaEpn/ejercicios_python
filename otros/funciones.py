#Algoritmos Fundamentales
#funciones.py
#Version 2.0
#Funciones, Listas, Busqueda en Python, Uso While y For
#Autor: Stalin Maza
#2016-Oct-30

import sys
global lista
def menu(lista):
    palabra = input("Ingrese la palabra que desea buscar: \n")
    print("Bienvenido al Menu de Busqueda en Python")
    print("Escoga la Opcion que Desee")
    print("1. Busqueda mediante funciones de Python")
    print("2. Busqueda recorriendo la lista con el estilo Python")
    print("3. Busqueda recorriendo la lista al estilo Java o C++")
    opcion = int(input())
    switch(lista, opcion,palabra)
    #Este es el menu que imprime las opciones de busqueda y despues
    #este llama a la funcion del switch.
    
def repetir(lista):
    escoger = input("Ingrese S si desea continuar o N si desea salir\n")
    while escoger == "S" or escoger == "s":
        menu(lista)
    print ("Programa Terminado")
    sys.exit()
    #aqui damos la opcion al usuario de si desea continuar en el programa
        
def switch(lista,opcion,palabra):    
    if opcion == 1:
        primer_M(lista,palabra)
        repetir(lista)
    elif opcion == 2:
        segundo_M(lista,palabra)
        repetir(lista)
    elif opcion == 3:
        tercer_M(lista,palabra)
        repetir(lista)
    else :
        repetir(lista)
        #aqui realizamos las opciones del switch de acuerdo a lo que escoga
        #el usuario.
        
def ingreso_datos():
    lista = []
    elemento = input("Ingrese un nuevo elemento de la lista: ")
    while elemento != "":
        lista.append(elemento)
        elemento = input("Ingrese un nuevo elemento de la lista: ")
    print("La lista generada es: ", lista)
    menu(lista)
    #aqui nosotros damos la opcion al usuario de ingresar los datos a la lista
    #y acabara cuando se ingrese un valor null

def primer_M(lista, palabra):
    print (palabra in lista)    # función booleana
    if palabra in lista:
        print ("la palabra", palabra, "fue encontrada en la lista", lista)
    else:
        print ("la palabra", palabra, "NO fue encontrada en la lista", lista)
    #El Primer método de busqueda el cual utiliza una funcion en python y nos
    #devuelve un valor booleano.

def segundo_M(lista, palabra):
    for elemento in lista:
        if elemento == palabra:
            print ("la palabra", palabra, "corresponde al elemento", elemento)
        else:
            print ("la palabra", palabra, "NO corresponde al elemento", elemento)
    #El Segundo método utiliza un for que recorre la lista con el estilo de python
    #es decir buscar y recorrer el arreglo sin utilizar algun indice.

def tercer_M(lista, palabra):
    n = len(lista)
    for i in range(n):
        if lista[i] == palabra:
            print ("la palabra", palabra, "corresponde al elemento", i, "que es", lista[i])
        else:
            print ("la palabra", palabra, "NO corresponde al elemento", i, "que es", lista[i])
    #El Ultimo método utiliza una forma similar a C++ o Java la cual recorre la lista utilizando
    #un indice que nos informa la posicion en la cual esta ubicado cada elemento.
    
def main():
    print("\tBienvenido al Menu de Busqueda Stalin ")
    ingreso_datos()
    #Funcion Main que llama a las demas funciones que siguen llamandose recursivamente.          
    
main()
