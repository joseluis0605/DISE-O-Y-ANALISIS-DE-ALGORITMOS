##### RECORRIDO EN PROFUNDIDAD ########
from collections import deque


def profundidad (g):
    tam= len(g)
    visitado= set()

    for nodo in range(0, tam):
        if nodo not in visitado: # cada subgrafo que haya nos metemos
            recursivo(g, visitado, nodo)

def recursivo(g, visitado, nodo):
    print(nodo)
    visitado.add(nodo)
    for nodoAux in g[nodo]:
        if nodoAux not in visitado:
            recursivo(g, visitado, nodoAux)

##### RECORRIDO EN ANCHURA ######

def anchura (g):
    tam= len(g)
    visitado= set()

    for nodo in range(0,tam):
        if nodo not in visitado: # vamos a acceder aqui por cada subgrafo
            visitandoSubgrafo(g, nodo, visitado)

def visitandoSubgrafo(g, nodo, visitado):
    cola= deque()
    print(nodo)
    visitado.add(nodo)
    cola.append(nodo)

    while cola:
        nodoPadre= cola.popleft()
        for nodoHijo in g[nodoPadre]:
            if nodoHijo not in visitado:
                print(nodoHijo)
                cola.append(nodoHijo)
                visitado.add(nodoHijo)

##### ORDENACION TOPOSORT #######

def toposort(g):

    tam= len(g)
    contadorHijo= [0]*tam

    for nodo in range(0,tam):
        contadorHijo[nodo]= len(g[nodo])

    pilaCeros=[]

    for i in range(0, tam):
        if contadorHijo[i]==0:
            pilaCeros.append(i)

    resultado=[]
    while pilaCeros:
        nodoActual= pilaCeros.pop(len(pilaCeros)-1)
        for i in range(0,tam):
            if nodoActual in g[i]:
                contadorHijo[i]= contadorHijo[i]-1
                if contadorHijo[i]==0:
                    pilaCeros.append(i)
        resultado.append(nodoActual)

    print(resultado)


if __name__ == '__main__':
    g = [  # estamos haciendo una lista de listas
        [],  # eliminamos lo que es la fila y columna 0
        [],  # adyacentes del nodo 1
        [0, 1],
        [],
        [0, 2],
        [1],
        [2, 5],
        []
    ]
    toposort(g)



    graph_AdjList = [  # estamos haciendo una lista de listas
        [],  # eliminamos lo que es la fila y columna 0
        [2, 4, 8],  # adyacentes del nodo 1
        [1, 3, 4],
        [2, 4, 5],
        [1, 2, 3, 7],
        [3, 6],
        [5, 7],
        [4, 6, 9],
        [1, 9],
        [7, 8]
    ]
