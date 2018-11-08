from pylab import *
"""lista1 = [2,-4,6,-8,10,-10]
lista2 = [1,2,3,4,5,6]
plt.scatter(lista2,lista1)
#plt.plot(lista1)
plt.title("Grafica")
plt.xlabel("abscisa")   # Inserta el título del eje X 
plt.ylabel("ordenada")   # Inserta el título del eje Y
plt.show()
#pip install matplotlib (ENTER)
#python -m pip install --upgrade pip"""

a = float(input('Valor de a: '))
x = np.arange(-10,10,0.5)
y = a*x**2 -4
plt.plot(x,y)
plt.title('a*x^2')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
