import numpy as np
from time import sleep
a = [[1],[2]]
a = np.array(a)
print(a)
#a = np.array([5,3,8,9])
"""print(a)
print(type(a))
print(a[3])
print(a[:3]) #posicion o hasta final-1
print(a[1:3]) #posicion inicial y final-1
print(a[1:]) #posicion inicial hasta el fin
b=np.array([9,6,4,2,1])
print(b[2:2])
print(b[:]) #posicion inicio hasta el fin
print(b[0:]) #posicion inicio hasta el fin
r = np.arange(10)
print(r)
lista = range(10)
print(lista)
for i in lista:
    print(i)
r2 = np.arange(100,120)
print(r2)
r3 = np.arange(100,120,5)
print(r3)
r4 = np.arange(120,80,-5)
print(r4)
print(type(r3))
print(len(r2))
a2 = a.reshape(2,2)
print(a2)
#a3 = a.reshape(4,1)
#print(a3)
#print("a2-0: ",a2[0], "a2-1: ",a2[1])
#print(a2[0,0])
#print(a2[0,1])
#print(a2[1,0])
#print(a2[1,1])
#METODOS DE RECORRER UN ARREGLO

a2 = a.reshape(2,2)
#print(a2)
m = len(a2) #numero filas
n = len(a2[0]) #numero columnas
print("RECORRIENDO POR FILAS")
for i in range(m):
    print("fila: ", i)
    for j in range(n):
        print(a2[i,j])
        
print("RECORRIENDO POR COLUMNAS")
for j in range(n):
    print("columna:", j)
    for i in range(m):
        print(a2[i,j])

b = np.array([[7,4,1],[8,9,5]])
print("B",b)
c = np.array([[7,4,1],[8,9,5],[-3,-4,-7]])
#print(c)
#print(b.shape)
n2 = b.shape[0] #filas
m2 = b.shape[1] #columnas
print("n2: ",n2,"es filas")
print("m2: ",m2,"es columnas")
print("B tiene: ", n2," filas y ", m2," columnas")
print("filas")
for i in range(n2):
    print("fila: ", i)
    for j in range(m2):
        print(b[i,j])
print("columnas")
for j in range(m2):
    print("columna: ", j)
    for i in range(n2):
         print(b[i,j])
b1 = b.reshape(1,n2*m2)
b2 = b.reshape(m2,n2)
print("B2",".................",b2)
z = np.arange(60)
print(z)
#crea un arreglo de 6 elementos a partir de 2 arreglos de 3 elementos
z2 =z.reshape(10,6)
print("Z2\n",".............",z2)
z3 = z.reshape(3,5,4)
print("Z3\n",z3,"..........")
z4 = z.reshape(5,2,3,2) #5 arreglos que contienen 2 arreglos y cada arreglo contiene 3 filas y 2 columnas
print("Z4\n",".............",z4)

ceros = np.zeros(100).reshape(20,5)
print(ceros)
unos = np.ones(40).reshape(4,10)
print(unos)
aleatorios = np.random.randint(5,size=10)
print(aleatorios) """

"""def cambiar_val():
    f = np.zeros(120).reshape(10,12)
    print(f)
    n = f.shape[0]
    print("n",n)
    m = f.shape[1]
    print("m",m)
    print("GRAFICO") 
    for i in range(int(n/2)+1,n):
        for j in range(m):
            if j>i:
                f[i,j]=1
    print(f)

    
def print_array2(w):
    print("W VALE: ", w)
    if w%2 == 0: #si w es par
        a = np.zeros(300).reshape(20,15)
        estado = 1
    else:
        a = np.ones(300).reshape(20,15)
        estado = 0
    print(a+"[0m")

def main():
    for w in range(10):
        print_array2(w)
        sleep(1)
        
    
#main()
