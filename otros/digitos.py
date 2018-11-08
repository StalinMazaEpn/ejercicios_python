from time import time

def buscarMm():
    num = [10,100,1000,500,200]
    m1 = max(num)
    m2 = num.remove(max(num))
    m2 = max(num)
    print(num)
    num.remove(max(num))
    m3 = max(num)
    print(num)
    print(m1)
    print(m1,m2,m3)

def BMm():
   num =[10,100,1000,500,200,58,2574,969,14]
   m1 = num[0]
   m2 = 0
   for i in range(0,len(num)):
       if num[i] > m1:
           m1 = num[i]
       if num[i] > m1:
           m2 = num[i]
   print(m1)
   print(m2)


mezcla = ["pan","mortadela",2,3,True,False]
print(mezcla)
print(mezcla[0])
mezcla.insert(1,"empanada")
print(mezcla)
mivalor = mezcla.pop()
print(mivalor)
print(mezcla)
x =  mezcla.pop(1)
print(x)
print(mezcla)
