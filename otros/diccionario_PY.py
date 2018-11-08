#---------------LIBRERIAS---------------
import collections

a= 127
c = 170
b = a%2==0
print(b)
def contarR():
    lista = ['a','b','a',"c","d","d","d"]    
    #for i in range
    diccionario= collections.Counter(lista)
    diccionario = dict(diccionario)
    print(diccionario)   #EJERCICIO CONTADOR PARA PROBAR- NO PERTENECE A ESTE EJERCICIO EN GENERAL
    
contarR()
