def conversionD(claves):
    lista = []
    for i in claves:
        a = i
        lista.append(a)
    return lista


def contarR(lista):
    diccionario = {}
    for i in lista:
        num = lista.count(i)
        nuevo = {i:num}
        diccionario.update(nuevo)
    return diccionario

def actualizar(diccionario,lista):   
    print("%%%%%",diccionario)
    claves = diccionario.keys()
    compar1 = conversionD(claves)
    i = 0
    elem = 0
    print("lista",lista)
    """for i in range(len(lista)):
        print("Lista",i)
        a = lista[i]
        elem = diccionario.get(a)
        print("elem",type(elem))
        print("a",a,"num",elem)
        a = lista[i]
        if a in lista:
            num = lista.count(a)
            print("num",type(num))
            #enviar = num + elem
            #print(enviar)
            #print(type(enviar))
            nuevo = {a:num}
            diccionario.update(nuevo)"""
           
    #print("actualizado",diccionario)
    print("...................................")
    for i in range(len(lista)):
        a = lista[i]
        print("a",a)
        repet = lista.count(a)
        print("a",a,"repeat",repet)
        if repet == 1: 
            nuevo = {a:1}
            print("if......................",nuevo)
            diccionario.update(nuevo)
            break
        else:
            if a in compar1  :
               actual = diccionario.get(a)
               mandar = actual + 1
               nuevo = {a:mandar}
               print("else: ",nuevo)
               diccionario.update(nuevo)
            else:
                mandar = repet
                print("VALOR C",mandar)
                nuevo = {a:mandar}
                diccionario.update(nuevo)
                
    print(",,,,,,,,,,,,,")
    return diccionario

    
#diccionario={'house':1,'red':2,'bed':3,'mama':4}
#lista = ["house","red","house","house"]
#temp = actualizar(diccionario,lista)
#print("..................................")
#lista2 = ["house","red","red"]
#actualizar(temp,lista2)
diccionario={'house':1,'red':1,'bed':1,'mama':1}
temp = {}
for i in range(2):    
    lista = ["house","house","manjar","manjar","new"]
    temp = actualizar(diccionario,lista)
    print("---")
    print("temp",temp)
#print(temp)    
#print(contarR(lista))
