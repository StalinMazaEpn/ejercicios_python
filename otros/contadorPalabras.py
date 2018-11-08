def leertxt():
    numero = 0
    archi=open("texto.txt","r")
    linea=archi.readline()
    while linea!="":
        print(linea)
        linea=archi.readline()    
    archi.close()

def creartxt():
    archi = open("contar.txt","w")
    archi.close()
    
def grabartxt2():
    archi=open("contar.txt","a")
    archi.write("El resultado es: " + a )
    archi.close()
    
def grabartxt(numero):
    print(numero)
    a = str(numero)
    archi=open("contar.txt","a")
    archi.write("El resultado es: " + a )
    archi.close()

def main():
    #creartxt()
    leertxt()
    
    
main()
