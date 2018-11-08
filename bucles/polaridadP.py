from textblob import TextBlob
import re, string
#pip install -U textblob
#python -m textblob.download_corpora

def llenar(m):
    a = [None] * m 
    return a

def quitarC (text):
    return re.sub('[%s]' % re.escape(string.punctuation), '', text)

def comprobar(m):
    if m > 0:
        print("Buenas Sentencias")
    elif m == 0:
        print("Sentencias Nulas")
    else:
        print("Malas Sentencias")
    
def leertxt():
    lista = []
    total = []    
    a = 0
    numero = llenar(10)
    archi=open("oraciones.txt","r")
    linea=archi.readline()
    while linea!="":
        #print(linea)
        linea=archi.readline()
        linea2  = quitarC(linea)
        linea3 = linea2.strip()
        linea4 = linea3.lower() 
        #lista = linea4.split(" ")
        total.append(linea4)
    j = 0
    for i in range(len(total)):
        valor = total[i]
        blob =  TextBlob(valor)        
        for sentence in blob.sentences:
            a = sentence.sentiment.polarity
            print("Polaridad de:",sentence,"es",a)
        numero[j] = a
        j = j+1
    total = sum(map(float,numero))
    promedio = total/len(numero)
    comprobar(promedio)
    archi.close()    
    return total


leertxt()
