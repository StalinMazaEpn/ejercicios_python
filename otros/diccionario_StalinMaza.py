phones =  {"joss":4012,"maria":1547,"diana":1585,"wilmer":9658,"dayana":7484}
print(phones)
buscar = input("Ingrese Nombre del que desea buscar\n")
verificar = buscar in phones
if verificar == True:
    print("Si existe")
else:
    print("No Existe")

#editando el telefono de mi amiga joss
phones["joss"] = 8747
print(phones)

def funcion():
    return "Hola Mundo"

frase = funcion()
print(frase)
