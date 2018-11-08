import re, string

def leertxt(name):
    total = 0
    archi=open(name,"r")
    linea=archi.readline()
    while linea!="":
        quitarC(linea)
        linea2 = quitarC(linea)
        linea3 = linea2.split()
        total = total + len(linea3)
        linea=archi.readline()
    print("Del archivo ",name,"el total de palabras es: " , total)
    archi.close()
    
def quitarC (text):
    return re.sub('[%s]' % re.escape(string.punctuation), '', text)

def sobreescribirT():
    archi = open('texto.txt', 'a') # Indicamos el valor 'a'.
    archi.write('Sobrescribiendo el archivo\n')
    outfile.close()
    # Leemos el contenido para comprobar que ha sobreescrito el contenido.
    leer = open('texto.txt', 'r')
    print(leer.read())
    # Cerramos el fichero.
    infile.close()
    
leertxt("harry23.txt")
