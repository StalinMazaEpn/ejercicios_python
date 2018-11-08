#STALIN_MAZA
#ALGORITMOS_FUNDAMENTALES
#EJERCICIOS CON GRAFOS
#ejer_grafo
#Version 2.1
#CREDITOS
#https://prezi.com/whwocd33f7bk/grafos-dirigidos-y-no-dirigidos/
#https://www.python.org/doc/essays/graphs/

#---------------LIBRERIAS---------------
import collections
#---------------GRAFOS------------------
#Los gráficos son redes que consisten en nodos conectados por aristas o arcos.
#En los gráficos dirigidos, las conexiones entre los nodos tienen una dirección,
#y se llaman arcos; En grafos no dirigidos, las conexiones no tienen dirección
#y se llaman bordes. Discutimos principalmente los gráficos dirigidos.
#Los algoritmos en los gráficos incluyen encontrar un camino entre dos nodos,
#encontrar el camino más corto entre dos nodos, determinar ciclos en el gráfico
#(un ciclo es un camino no vacío de un nodo a sí mismo), encontrar un camino
#que llega a todos los nodos "Problema del vendedor ambulante"), y así sucesivamente.
#A veces los nodos o arcos de un gráfico tienen pesos o costos asociados con ellos,
#y estamos interesados ​​en encontrar el camino más barato.
#Hay mucha literatura sobre algoritmos de gráficos, que son una parte importante
#de la matemática discreta. Los gráficos también tienen mucho uso#
#práctico en algoritmos de computadora. Ejemplos evidentes se pueden#
#encontrar en la gestión de redes, pero los ejemplos abundan en
#muchas otras áreas. Por ejemplo, las relaciones caller-callee en un#
#programa de computadora se pueden ver como un gráfico
#donde los ciclos indican la recursión, y los nodos inaccesibles
#representan el código muerto).

#LAS RELACIONES DE LOS GRAFOS SON ASI:
     #A -> B
     #A -> C
     #B -> C
     #B -> D
     #C -> D
     #D -> C
     #E -> F
     #F -> C
#GRAFO DE EJEMPLO--------------------------
#LAS RELACIONES DE LOS GRAFOS SON ASI:
     #A -> B
     #A -> C
     #B -> C
     #B -> D
     #C -> D
     #D -> C
     #E -> F
     #F -> C
grafico = {'A': ['B', 'C'],
              'B': ['C', 'D'],
              'C':['D'],
              'D': ['C'],
              'E': ['F'],
              'F': ['C']}
#GRAFO DEL DEBER----------------------------
#La relacion de esta es asi:
        #IBARRA --> QUITO
        #QUITO --> IBARRA,SANTO_D,NAPO,CUENCA
        #SANTO_D -->QUITO,GUAYAQUIL,CUENCA
        #NAPO --> QUITO,CUENCA,MORONA_S
        #GUAYAQUIL --> SANTO_D,CUENCA,LOJA
        #CUENCA --> GUAYAQUIL,MORONA_S,LOJA,QUITO,NAPO
        #MORONA_S -->  NAPO,CUENCA,LOJA
        #LOJA --> GUAYAQUIL,CUENCA.MORONA_S

carreteras = {"IBARRA":["QUITO"],
              "QUITO":["IBARRA","SANTO_D","NAPO","CUENCA"],
              "SANTO_D":["QUITO","GUAYAQUIL","CUENCA"],
              "NAPO":["QUITO","CUENCA","MORONA_S"],
              "GUAYAQUIL":["SANTO_D","CUENCA","LOJA"],
              "CUENCA":["GUAYAQUIL","MORONA_S","LOJA","QUITO","NAPO"],
              "MORONA_S":["NAPO","CUENCA","LOJA"],
              "LOJA":["GUAYAQUIL","CUENCA","MORONA_S"]}
#---------------FUNCIONES DE LOS GRAFOS---..------------------

def ruta_mas_larga(grafico, inicio, fin, ruta = []):
         ruta = ruta + [inicio] #es un diccionario con los nodo
         #print(".....",ruta) 
         if inicio == fin:
             return ruta #cuando el arreglo ruta tiene al inicio y fin incluido retorna 
         if inicio not in grafico: #este arreglo y finaliza el ciclo
             return None           
         for nodo in grafico [inicio]:
             if nodo not in ruta:
                 nueva_ruta = ruta_mas_larga(grafico, nodo, fin, ruta) #funcion se llama a si misma
                 print("Nodo",nodo)
                 if nueva_ruta:                     
                     return nueva_ruta #retorna el valor de ruta larga
         return None #retorno cuando no encuentra ningun valor

#Este es un diccionario cuyas claves son los nodos de la gráfica.
#Para cada clave, el valor correspondiente es una lista que contiene
#los nodos que están conectados por un arco directo desde este nodo.
#Esto es lo más simple posible (incluso más simple
#los nodos podrían ser representados por números en lugar de nombres,
#pero los nombres son más convenientes y se pueden hacer fácilmente
#para transportar más información, como nombres de ciudades).
#Escribamos una función simple para determinar una ruta entre dos nodos.
#Se necesita un gráfico y los nodos de inicio y fin como argumentos.
#Devolverá una lista de nodos (incluidos los nodos de inicio y fin)
#que comprende la ruta. Cuando no se puede encontrar ninguna ruta, devuelve None.
#El mismo nodo no se producirá más de una vez en la ruta devuelta
#(es decir, no contendrá ciclos).
#El algoritmo utiliza una técnica importante llamada retroceso :
#intenta cada posibilidad a su vez hasta encontrar una solución.


def todas_las_rutas(grafico, inicio, fin, ruta = []):
        ruta = ruta + [inicio]
        if inicio == fin:
            return [ruta]
        if inicio not in grafico:
            return []
        rutas = []
        for nodo in grafico[inicio]:
            if nodo not in ruta:
                nuevas_rutas = todas_las_rutas(grafico, nodo, fin, ruta)
                for new_ruta in nuevas_rutas:
                    rutas.append(new_ruta)
        return rutas

#La segunda instrucción 'if' sólo es necesaria en el caso de que haya nodos
#que estén listados como puntos finales para arcos pero que no tengan arcos
#salientes ellos mismos y no estén listados en el gráfico en absoluto.
#Tales nodos también podrían estar contenidos en el gráfico
#con una lista vacía de arcos salientes, pero a veces es más conveniente
#no requerir esto.
#Tenga en cuenta que mientras el usuario llama a find_graph ()
#con tres argumentos, se llama a sí mismo con un cuarto argumento:
#la ruta que ya ha sido recorrida.
#El valor predeterminado de este argumento es la lista vacía, '[]',
#lo que significa que no se han recorrido todavía nodos.
#Este argumento se utiliza para evitar ciclos
#(el primer 'IF' dentro del bucle 'for'). El argumento 'path' no se modifica:
#la asignación "path = path + [start]" crea una nueva lista.
#Si hubiéramos escrito "path.append (start)" en su lugar,
#habríamos modificado la variable 'path' en la persona que llama,
#con resultados desastrosos.
#(Usando tuplas, podríamos haber estado seguros de que esto no ocurriría,
#a costa de tener que escribir "path = path + (start,)"
#ya que "(start)" no es una tupla singleton - es sólo un paréntesis expresión

#Es sencillo cambiar esta función para devolver una lista de todas las rutas
#(sin ciclos) en lugar de la primera ruta que encuentra:

def ruta_mas_corta(grafico, inicio, fin, ruta = []):
        ruta = ruta + [inicio]
        if inicio == fin:
            return ruta
        if inicio not in grafico:
            return None
        mas_corto = None
        for nodo in grafico[inicio]:
            if nodo not in ruta:
                nueva_ruta = ruta_mas_corta(grafico, nodo, fin, ruta)
                if nueva_ruta:
                    if not mas_corto or len(nueva_ruta) < len(mas_corto):
                        mas_corto = nueva_ruta
        return mas_corto


#------------FUNCIONES PRINCIPALES--------------------------
def ruta_larga():
    algun = ruta_mas_larga(carreteras, 'GUAYAQUIL', 'LOJA')
    print("Ruta es: ", algun)
    
def rutas_posibles():
    todas = todas_las_rutas(carreteras, 'IBARRA', 'LOJA') #IMPRIME TODAS LAS RUTAS POSIBLES
    for i in range(len(todas)):
        print("Ruta: ",i+1,"es: \n",todas[i],"\n")

def ruta_corta():
    corta = ruta_mas_corta(carreteras, 'IBARRA', 'LOJA') #IMPRIME LA RUTA MAS CORTA
    print("Ruta mas corta es:\n",corta)
    
def ruta_mas_larga_y_mas_corta():
    todas = todas_las_rutas(carreteras, 'IBARRA', 'LOJA')
    l = []    
    for i in range(len(todas)):
        larga = 5
        l.append(len(todas[i]))     #FUNCION QUE IMPRIME EL O LOS GRAFOS 
    for i in range(len(todas)):     #CON LA RUTA MAS LARGA Y LA MAS CORTA
        if len(todas[i]) == max(l):  #RECIBE UN DICCIONARIO DE RUTAS Y EL INICIO Y DESTINO          
            print("Ruta(s) mas Larga(s):\n",todas[i])
        if len(todas[i]) == min(l):
            print("Ruta(s) mas Corta(s):\n",todas[i])
#-----------FUNCION QUE NO FORMA PARTE DEL EJEMPLO--------------            
def contarR():
    lista = ['a','b','a',"c","d"]
    veces = lista.count('a')
    #for i in range
    diccionario= collections.Counter(lista)
    diccionario = dict(diccionario)
    print(diccionario)   #EJERCICIO CONTADOR PARA PROBAR- NO PERTENECE A ESTE EJERCICIO EN GENERAL
    print(veces)

#contarR()
def switch(i):
    if i == 1:
        ruta_mas_larga_y_mas_corta()
    elif i == 2:
        ruta_corta()
    elif i == 3:
        rutas_posibles()  #SWITCH QUE LLAMA A LAS FUNCIONES DE ACUERDO
    elif i == 4:         #A LA OPCION DESEADA
        ruta_larga()
    elif i >= 5:
        print("Opcion no es del sistema")

def main():
    print("\tBienvenido al Menu Stalin - Grafos")
    print("\t1. Camino mas Largo y Mas Corto")
    print("\t2. Camino mas Corto")
    print("\t3. Todos los caminos posibles") #FUNCION MAIN DEL PROGRAMA
    print("\t4. Ruta Larga")
    seleccion = int(input("Escoga su opcion: \n"))
    print("\nEl Grafo Inicial es: \n",carreteras,"\n")
    switch(seleccion)

main()
