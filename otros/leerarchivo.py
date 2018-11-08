import re, string

def quitarC (text):
    return re.sub('[%s]' % re.escape(string.punctuation), '', text)

archivo = open("harry23.txt",'r')
i = 0
for linea in archivo.readlines():
    linea2  = quitarC(linea)
    linea3 = linea2.strip()
    linea4 = linea3.lower()
    lista = linea4.split(" ")
    if i == 0:
        a = lista[0]
        linea5= a.replace("ï»¿", '')
        lista.remove(a)
        lista.append(linea5)
    print(lista)
    i = i+1
    
#'\ufeff
#s = u'word1 \ufeffword2'
#>>> s = s.replace(u'\ufeff', '')
#>>> s
#u'word1 word2'"""
