import nltk
from nltk.book import *
import re, string

def quitarC (text):
    return re.sub('[%s]' % re.escape(string.punctuation), '', text)


def leertxt():
    lista = []
    total = [] 
    numero = 0
    archi=open("lectura100.txt","r")
    linea=archi.readline()
    while linea!="":
        #print(linea)
        linea=archi.readline()
        linea2  = quitarC(linea)
        linea3 = linea2.strip()
        linea4 = linea3.lower() 
        lista = linea4.split(" ")
        for i in range(len(lista)):
            valor = lista[i]
            total.append(valor)    
    archi.close()    
    return total

comparar = leertxt()
fdist1 = FreqDist(comparar)
a = len(fdist1)
b = fdist1.most_common(a)
print("\n\tFrecuencia\n",b)
print(len(b))
