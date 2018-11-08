#Algoritmos Fundamentales
#funmat.py
#Version 1.0
#Graficas de diferentes funciones.
#Autor: Stalin Maza
#2016-Nov-11
#Importando la libreria PYLAB de la Biblioteca matplotlib

#from pylab import *
import pylab as pl
import numpy as np
"""lista1 = [2,-4,6,-8,10,-10]
lista2 = [1,2,3,4,5,6]
plt.scatter(lista2,lista1)
#plt.plot(lista1)
plt.title("Grafica")
plt.xlabel("abscisa")   # Inserta el título del eje X 
plt.ylabel("ordenada")   # Inserta el título del eje Y
plt.show()
#Para Instalar la libreria matplotlib usamos estos comandos en el CMD de Windows.
#pip install matplotlib (ENTER)             #esta nos sirve para instalar la libreria
#python -m pip install --upgrade pip"""     #esta nos sirve para actualizar
                                            #el instalador paquetes de python

a = float(input('Valor de a: '))
x = np.arange(-5,5,0.1)
y = a*x**2 -4

ax = pl.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))



pl.plot(x,y,color="blue",label="cuadratica")

#pl.xlim(x.min() * 1.1, x.max() * 1.1)  #para ver de mejor manera
#pl.ylim(y.min() * 1.1, y.max() * 1.1)  #nuestro grafico 

pl.title('a*x^2')
pl.xlabel('X')
pl.ylabel('Y')
#pl.legend(loc='upper center')
pl. legend (bbox_to_anchor = (1, 1), loc = 1, borderaxespad = 0.)

pl.show()
