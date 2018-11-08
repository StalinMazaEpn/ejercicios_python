def forma1():  
  ct = "S"
  lista = []
  max = int(input("Digite cuantos nombres desea ingresar:\n"))
  for i in range(max):
    nombre = input("Ingrese un Nombre\n")
    lista.append(nombre)     
  temp = input("Ingrese Nombre para Verificar\n")
  if temp in lista:
    print("El Nombre Si Existe")
  else:
    print("No existe dicho nombre")


def forma2():  
  lista2 = []
  max = int(input("Digite cuantos nombres desea ingresar:\n"))
  for i in range(max):
    nombre2 = input("Ingrese un Nombre\n")
    lista2.append(nombre2)
  temp = input("Ingrese Nombre para Verificar\n")
  for e in lista2:
    if e == temp:
      print("El Nombre Si Existe")
      break
    else:
      print("No existe dicho nombre")      
   

def forma3():
  max = int(input("Digite cuantos nombres desea ingresar:\n"))
  lista3 = []
  for i in range(max):
    nombre3 = input("Ingrese un Nombre\n")
    lista3.append(nombre3) 
  temp3 = input("Ingrese Nombre para Verificar\n")
  for i in range(0,len(lista3)) :
    if lista3[i] == temp3 :
      print("El Nombre Si Existe")
      break
    else :
      print("No existe dicho nombre")
      
forma2()
