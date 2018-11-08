#AUTOR: STALIN_MAZA
#ALGORITMOS_FUNDAMENTALES
#EJERCICIOS CON GRAFOS
#caminos_grafos.py
#Version 3.1
#CREDITOS
#https://prezi.com/whwocd33f7bk/grafos-dirigidos-y-no-dirigidos/
#https://www.python.org/doc/essays/graphs/
#2017-Feb-05
#-----------------------GRAFOS------------------
#LAS RELACIONES DE ESTE GRAFO SERIAN ASI:
     #A -> B            #A -> C      #B -> C            #B -> D
     #C -> D            #D -> C      #E -> F            #F -> C
grafico = {'A': ['B', 'C'],
           'B': ['C', 'D'],
           'C':['D'],
           'D': ['C'],
           'E': ['F'],
           'F': ['C']}
#--------------------GRAFO DEL DEBER-------------------------
#La relacion de este ejercicio es asi:
    #IBARRA --> QUITO               #QUITO --> IBARRA
    #QUITO --> SANTO_D              #QUITO --> NAPO
    #QUITO --> CUENCA               #SANTO_D --> QUITO
    #SANTO_D --> GUAYAQUIL          #SANTO_D --> CUENCA
    #NAPO --> QUITO                 #NAPO --> CUENCA
    #NAPO --> MORONA_S              #GUAYAQUIL --> SANTO_D
    #GUAYAQUIL --> CUENCA           #GUAYAQUIL --> LOJA
    #CUENCA --> GUAYAQUIL           #CUENCA --> MORONA_S
    #CUENCA --> LOJA                #CUENCA --> QUITO
    #CUENCA --> NAPO                #MORONA_S --> NAPO
    #MORONA_S --> CUENCA            #MORONA_S --> LOJA
    #LOJA --> GUAYAQUIL             #LOJA --> CUENCA
    #LOJA -->  MORONA_S

ciudad = ["IBARRA","QUITO","SANTO_D","NAPO","GUAYAQUIL","CUENCA","MORONA_S","LOJA"]
carreteras = {"IBARRA":["QUITO"],
              "QUITO":["IBARRA","SANTO_D","NAPO","CUENCA"],
              "SANTO_D":["QUITO","GUAYAQUIL","CUENCA"],
              "NAPO":["QUITO","CUENCA","MORONA_S"],
              "GUAYAQUIL":["SANTO_D","CUENCA","LOJA"],
              "CUENCA":["GUAYAQUIL","MORONA_S","LOJA","QUITO","NAPO"],
              "MORONA_S":["NAPO","CUENCA","LOJA"],
              "LOJA":["GUAYAQUIL","CUENCA","MORONA_S"]}

#---------------FUNCIONES DE LOS GRAFOS---------------------
def ruta_cualquiera(grafico, inicio, fin, ruta = []): #determina la ruta mas larga
         ruta = ruta + [inicio] #es un diccionario con los nodos como claves de los mismos         
         if inicio == fin:             
             return ruta #cuando el arreglo ruta tiene al inicio y fin incluido retorna 
         if inicio not in grafico: #este arreglo y finaliza el ciclo
             return None #RETORNA NONE PORQUE UNO DE LOS VALORES DE INICIO O FIN NO EXISTEN EN EL GRAFICO          
         for nodo in grafico [inicio]:
             if nodo not in ruta:
                 nueva_ruta = ruta_cualquiera(grafico, nodo, fin, ruta) #funcion se llama a si misma                 
                 if nueva_ruta:                     
                     return nueva_ruta #retorna el valor de ruta larga
         return None #retorno cuando no encuentra ningun valor

def todas_las_rutas(grafico, inicio, fin, ruta = []): #determina todas las rutas posibles
        ruta = ruta + [inicio]  #guarda las rutas en un arreglo
        if inicio == fin: #cuando el inicio es igual al fin acaba la funcion y la retorna
            return [ruta]
        if inicio not in grafico: #NO RETORNA NINGUN VALOR SI ES QUE
            return None  #UNO DE LOS VALORES DE INICIO O FIN NO EXISTEN EN EL GRAFICO
        rutas = [] #crea un arreglo de las rutas
        for nodo in grafico[inicio]:
            if nodo not in ruta: #funcion se llama a si misma  con un ultimo argumento la ruta recorrida
                nuevas_rutas = todas_las_rutas(grafico, nodo, fin, ruta)
                for new_ruta in nuevas_rutas:
                    rutas.append(new_ruta) #añade las rutas encontradas
        return rutas
def ruta_mas_larga(inicio,final):
    todas = todas_las_rutas(carreteras, inicio,final)
    l = []    
    for i in range(len(todas)):
        larga = 5
        l.append(len(todas[i]))     #FUNCION QUE IMPRIME EL O LOS GRAFOS 
    for i in range(len(todas)):     #CON LA RUTA MAS LARGA Y LA MAS CORTA
        if len(todas[i]) == max(l):  #RECIBE UN DICCIONARIO DE RUTAS Y EL INICIO Y DESTINO          
            return todas[i]       
            
def ruta_mas_corta(grafico, inicio, fin, ruta = []):
        ruta = ruta + [inicio]
        if inicio == fin:            
            return ruta
        if inicio not in grafico:            
            return None #RETORNA NONE PORQUE UNO DE LOS VALORES DE INICIO O FIN NO EXISTEN EN EL GRAFICO
        mas_corto = None
        for nodo in grafico[inicio]:
            if nodo not in ruta:
                nueva_ruta = ruta_mas_corta(grafico, nodo, fin, ruta)
                if nueva_ruta:
                    if not mas_corto or len(nueva_ruta) < len(mas_corto):
                        mas_corto = nueva_ruta
        #print("Ruta mas corta es:\n",mas_corto)
        return mas_corto
#------------FUNCIONES PRINCIPALES--------------------------
def rutas_posibles(inicio,fin):
    todas = todas_las_rutas(carreteras, inicio, fin) #IMPRIME TODAS LAS RUTAS POSIBLES
    for i in range(len(todas)):
        print("\t\tRuta",i+1,"es: \n",todas[i],"\n")

def switch(seleccion):
    if seleccion <=4:
        print("\nLas ciudades iniciales son: \n",ciudad)
        inicio = input("Ingrese Inicio Ruta\n")
        fin = input("Ingrese Final Ruta\n")    
        if seleccion == 1:
            print("Ruta mas corta es: \n",ruta_mas_corta(carreteras, inicio, fin))
        elif seleccion == 2:
            rutas_posibles(inicio, fin)  #SWITCH QUE LLAMA A LAS FUNCIONES DE ACUERDO
        elif seleccion == 3:         #A LA OPCION DESEADA
            print("Ruta Cualquiera es: \n",ruta_cualquiera(carreteras, inicio, fin))
        elif seleccion == 4:
            print("Ruta mas Larga es: \n",ruta_mas_larga(inicio,fin))
    else: 
            print("Opcion no es del sistema")
    volver = input("Desea Continuar Y/N\n")
    if volver == "Y" or volver == "y":
        main()

def main():
    print("\tBienvenido al Menu Stalin - Grafos")
    print("\t1. Ruta Corta")
    print("\t2. Todos los caminos posibles") #FUNCION MAIN DEL PROGRAMA
    print("\t3. Ruta Cualquiera")
    print("\t4. Ruta Mas Larga")
    seleccion = int(input("Escoga su opcion: \n"))    
    switch(seleccion)

main()
