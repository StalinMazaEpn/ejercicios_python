def trianguloPascal(n):
    # creamos una lista que contendra los dos primeras lineas
    lista = [[1],[1,1]]
    # bucle que se generara tantas veces como lineas vayamos a tener
    for i in range(1,n):
        # inicializamos la linea
        linea = [1]
        # bucle por cada uno de los valores de la anterior linea
        for j in range(0,len(lista[i])-1):
            # añadimos a la lista los nuevos valores
            # sumamos el valor de la lista anterior con el siguinte
            linea.extend([ lista[i][j] + lista[i][j+1] ])
        # añadimos el ultimo valor a la nueva linea
        # siempre es un 1 igual que el primero
        linea += [1]
        # añadimos la linea a la lista
        lista.append(linea)
    #devolvemos la lista ya creada
    return lista

try:
    n = int(input("Numero de lineas para triangulo de Pascal: "))
    resultado = trianguloPascal(n)
    # mostramos el resultado
    for i in resultado:
        print(i)
except:
    print("\nTiene que ser un valor numerico")

