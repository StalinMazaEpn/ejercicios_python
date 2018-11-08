#ESCUELA POLITECNICA NACIONAL
#Escuela de formacion de tecnologos

#### Examen 1 2016 -Grupo 3
#Integrantes: CAMPOVERDE VARGAS	JORGE	CRISTIAN
#             CENTENO	ROCHA	JOHANA	MISHEL
#             MAZA CAÑAR  JERSON  STALIN
#             PADILLA PERALVO	EDISON GEOVANNY
#             TIBANTA LEGÑA MARIA FERNANDA

from time import *

def creartxt(name):
    archi=open(name,'w')
    archi.close
    

def grabartxt(repetidas,resultado):
    archi=open('resultados.txt','a')          #Crea el archivo donde se almacena los resultados
    archi.write('Numero de palabras repetidas es :' + str(repetidas) )
    archi.write("\t Tiempo transcurrido:" + str(resultado) )
    
def leertxt():
    creartxt("resultados.txt")
    repetidas=0
    clave='JORGE'
    archi=open ('nombres.txt','r')
    
    t_inicial=time()                          #Abre el archivo 
    linea=archi.readline()                    # lee la linea del archivo
    palabras=linea.split(' ')                 # separa la linea leida quitando los espacios
    cadena=len(palabras)                      #cadena es igualada al numero de palabras que fueron separadas en el comando anterior
    for i in range(cadena-1):                 # i en el rango de la cadena
        if palabras[i]==clave:                # evalua si la posicion de i de palabras es igual a la clave que es Harry
            repetidas=repetidas+1             #si encuentra la coinsidencia repetidas aumenta
    while linea != "":                        #repite todo lo mencionado antes hasta que no haya lineas
        linea=archi.readline()
        palabras=linea.split(' ')
        cadena=len(palabras)
        for i in range(cadena):
            if palabras[i]==clave:
                repetidas=repetidas+1
                
    t_final=time()
    resultado=t_final-t_inicial
    
    archi.close()
    grabartxt(repetidas,resultado)

def main():
    leertxt()

main()
