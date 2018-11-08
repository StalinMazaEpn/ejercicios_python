import math

def raices_C():
    a = int(input("Ingrese el valor de A\n"))
    b = int(input("Ingrese el valor de B\n"))
    c = int(input("Ingrese el valor de C\n"))
    key = 2 * a
    if a <= 0:
        print("el valor de 0 debe ser mayor que 0")       
  
    else:
        discriminante = b**2 - (4*a*c)
        if discriminante < 0:
            print("No hay solucion")
        else:
            temp2 = discriminante ** 0.5
            resultado1 = (-b + temp2)/2*a
            resultado2 = (-b - temp2)/2*a
            #print("Las raices son: " , resultado1," ",resultado2)
            grabartxt(resultado1,resultado2)

def creartxt():
    archi = open("resultados.txt","w")
    archi.close()

def grabartxt(resultado1,resultado2):
    print(resultado1, resultado2)
    a = str(resultado1)
    b = str(resultado2)
    archi=open("resultados.txt","a")
    archi.write("El resultado es: " + a + b )
    archi.close()

    
def main():
    creartxt()
    raices_C()
    
main()
