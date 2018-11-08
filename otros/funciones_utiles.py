import functools

def reducir():
    def multiplicar(x, y):
        print(x * y)  # muestra el resultado parcial
        return x * y

    lista = [1, 2, 3, 4]
    valor = functools.reduce(multiplicar, lista)
    print(valor)  # muestra el resultado final



def m():
    l=[0.0, 0.0, 1.0, 0.0, 0.25, 0.25]
    print("PROMEDIO NUMEROS FLOTANTES: ",sum(map(float,l)))

def filtro():
    # La función verifica si un número es negativo
    def esneg(numero):
        # Devuelve True/False según sea o no nº negativo
        return (numero < 0)

    lista5 = [-3, -2, 0, 1, 9, -5]

    # Muestra los números negativos de la lista
    # La función esneg() es llamada para comprobar, 
    # uno a uno, todos los números de la lista
    print("NUMEROS NEGATIVOS: ",list(filter(esneg, lista5)))


print("\nFuncion Filtro", filtro())
print("\nFuncion Filtro",m())
print("\nFuncion Filtro",reducir())
