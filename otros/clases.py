import random

class Imagen():
    def direccion(self,url):
        return url
    def crearM(self):
        matriz = [[0] * 4 for i in range(3)]
        return matriz
    def aleatorio(self):
        a = random.randrange(0,3)
        b = random.randrange(0,2)
        #print(a,b)
        c = (a,b)
        print(c,type(c))
        
        
    
#a = Example()
#a.func1()
a = Imagen()
#print(a.direccion("/img"))
#print(a.crearM())
for i in range(6):
    a.aleatorio()   
