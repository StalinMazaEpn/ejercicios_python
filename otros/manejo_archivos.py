import math
def creartxt():
    archi = open("datos.txt","w")
    archi.close()

def grabartxt():
    archi=open("datos.txt","a")
    archi.write("EPN 1\n")
    archi.write("ESFOT 2\n")
    archi.write("ASI3 \n")
    archi.close()

def leertxt():
    archi=open("harry.txt","r")
    linea=archi.readline()
    while linea!="":
        print(linea)
        linea=archi.readline()
    archi.close()

    
creartxt()
grabartxt()
leertxt()
