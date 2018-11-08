#ESCUELA POLITECNICA NACIONAL
#ESCUELA DE FORMACION DE TECNOLOGOS
#EXAMEN BIMESTRAL
#PROGRAMACION AVANZADA
#INTEGRANTES.PY
#VERSION 1.0
#INTEGRANTES:
        #CAMPOVERDE VARGAS JORGE CRISTIAN
        #CENTENO ROCHA JOHANA MISHEL
        #MAZA CAÑAR JERSON STALIN
        #PADILLA PERALVO EDISON GEOVANNNY
        #TIBANTA LEGÑA MARIA FERNANDA
from time import*
import math
def creartxt2(nombre):
    archi = open(nombre,"w") #ESTA FUNCION CREA LOS ARCHIVOS DE TEXTO
    archi.close() #RECIBE EL NOMBRE DEL ARCHIVO DE TEXTO
    
def grabartxt2(cadena,name):
    archi=open(name,"a") #ESTA FUNCION GRABA LA CADENA EN EL ARCHIVO DE TEXTO
    archi.write(cadena + "\n") #RECIBE EL NOMBRE DEL ARCHIVO DE TEXTO DONDE GRABAR
    archi.close()

def names():
    m1 = "CAMPOVERDE VARGAS JORGE CRISTIAN"
    m2 = "CENTENO ROCHA JOHANA MISHEL"
    m3 = "MAZA CAÑAR JERSON STALIN"  #ESTAS SON CADENAS PEQUEÑAS CON 
    m4 = "PADILLA PERALVO EDISON GEOVANNNY" #LOS NOMBRES DE CADA UNO DE 
    m5 = "TIBANTA LEGÑA MARIA FERNANDA" #LOS INTEGRANRES
    e = " " #CADENA QUE CONTIENE UN ESPACIO
    total = m1 + e + m2 + e + m3 + e + m4 + e + m5 #AQUI SE CONCATENA LOS INTEGRANTES
    return total #AQUI RETORNA LA CADENA FINAL

def mainscrip():
    creartxt2("nombres.txt")
    creartxt2("nombres2.txt") #AQUI CREO LOS ARCHIVOS TXT
    for i in range (690):
        grabartxt2(names(),"nombres.txt") #AQUI LLENO EL ARCHIVO REPITIENDO N VECES HASTA Q PESE APROX 100 KB
        
    print("PRIMERO CREADO CORRECTAMENTE") #MENSAJE DE FINALIZACION
    for i in range (7040):
        grabartxt2(names(),"nombres2.txt") #AQUI LLENO EL ARCHIVO REPITIENDO N VECES HASTA Q PESE APROX 1024 KB
    print("SEGUNDO CREADO CORRECTAMENTE")#MENSAJE DE FINALIZACION

#Concurrecias del  texto
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

def mainC():
    leertxt()



#Volumenes de la piscina

def pis_rect():
    print ("Volumen de una piscina rectangular")
    a=float(input("Ingrese el valor la altura: "))
    b=float(input("Ingrese el valor del largo de la piscina: "))
    c=float(input("Ingrese el valor del ancho de la piscina: "))
    volumenR=a*b*c
    v = round(volumenR,2)
    print("Volumen de la priscina en forma de prisma rectangular es: ", v)


def pis_elip():
    print ("Volumen de una piscina eliptica")
    a=float(input("Ingrese el valor del radio1: "))
    b=float(input("Ingrese el valor del redio2: "))
    c=float(input("Ingrese el valor del radio3: "))
    volumenE=4/3*math.pi*a*b*c
    v2 = round(volumenE,2)
    print("Volumen de la piscina elipsoide es: ", v2)


def pis_cir():
    print ("Volumen de una piscina cilindrica")
    r=float(input("Ingrese el valor del radio: "))
    h=float(input("Ingrese el valor de la altura: "))
    pi=3.14
    volumenC=math.pi*r**2*h
    v3 = round(volumenC,2)
    print("Volumen de una piscina eliptica es: ", v3)
    
def menu_piscina():
    opcion2=0;
    e=False
    while(e ==False):
        print("Calcular el volumen de una piscina")
        print("1.Volumen de forma rectangular")
        print("2.Volumen de forma eliptica")
        print("3.volumen de forma cilindrica")
        print("4.Salir")
        opcion2=int(input("Seleccione: \n"))
        if (opcion2==1):
            
            pis_rect()
            menu()
        if (opcion2==2):
            
            pis_elip()
            menu()
        if (opcion2==3):
            
            pis_cir()
            menu()
        if (opcion2==4):
            print ("Adios")
        e=True
    

def menu():
    opcion=0;
    p = False
    while(p == False):
        print("\tMenu del programa")
        print("1.Scrip y Concurrencias")
        print("2.Calcular el volumen de una piscina ")
        print("3.Salir")
        opcion=int(input("Ingrese la opcion que desea elegir: \n"))
        if (opcion==1):
            print("generar un scrip de 100 KB y un scrip de 1024 KB")
            mainscrip()
            print("Ocurrencias en  el  texto")
            mainC()
        if (opcion==2):
            print("el volumen ")
            menu_piscina()
        if (opcion==3):
            print ("Adios")
            p = True


menu()
