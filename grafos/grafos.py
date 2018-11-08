import collections


def imprimir_grado(g):
    #veces = collections.Counter(g)
    #print(veces)
    for key, valor in g.items():
        print(key, '-->',len(valor))


v = {1,2,3,4,5,6}
v2 = {"a","b","c","d"}

e = {(1,2),(1,3),(1,4),(3,4)}
e2 = {("A","C"),("C","D"),("D","A"),("B","C")}


g1 = {1:[2,3,4],2:[1],3:[1,4],4:[1,3],5:[],6:[]}

imprimir_grado(g1)

