import collections

"""diccionario = {'color': '1', 'marca': '8', 'talle': '4'}
clave = diccionario.keys()
clave2 = diccionario.values()
print(clave)
print(clave2)
i = 0
for claves,keys in diccionario.items():
    if "color" in diccionario:
        i = int(diccionario[claves]) + 1
        print(diccionario[claves])
        diccionario[claves] = 2
print(diccionario)   """   
"""#for claves,keys in diccionario.items():
 #   if diccionario.has_key("color"):
  #      i = int(diccionario[claves]) + 1
   #     print(diccionario[claves])
    #    diccionario[claves] = 2
print(diccionario)"""

diccionario2={'house':1,'red':2,'bed':3,'mama':4}
i = 0
print(diccionario2)
mami = diccionario2.keys()
print(mami)
for k,v in diccionario2.items():
    if k in diccionario2:
        print('Si tiene la clave buscada')
        i = int(diccionario2.get(k))+ 1
        diccionario2.setdefault(k,i)
    else:
        print("No existe la clave buscada")
        print(k,"->",v)
print(diccionario2)

#futbolistas = { 'house':1,'red':2,'bed':3,'mama':4}
#print(futbolistas)
#futbolistas.setdefault('Cesc',10)
#print(futbolistas)
#elem = futbolistas.get("house") #obteniendo valor
#print("clave: ",elem)
