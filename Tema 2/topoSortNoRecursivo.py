# algoritmo de ordenacion topologico sin uso de recursividad
# GRAFO ACICLICO DIRIGIDO
# TENEMOS EN CUENTA QUE LOS ELEMENTOS DEL GRAFO, DENTRO DE LA LISTA SON LOS GRADOS DE ENTRADA
from collections import deque


def topologicoSort(g):
    tam = len(g)
    contadorGrado = [0] * tam  # contar el grado de entrada que tiene cada nodo

    for indice in range(0, tam):
        contadorGrado[indice] = len(g[indice])

    listaAux = []  # nos cramos una lista con los nodos de grado 0

    for indice in range(0, tam):
        if contadorGrado[indice] == 0:
            listaAux.append(indice)

    resultado = []
    while listaAux:
        cogidoPila = listaAux.pop(len(listaAux) - 1)  # cogemos ultimo elemento lista
        for indice in range(0, tam):  # recorremos el grafo para reducir 1 a los que tengan
            if cogidoPila in g[indice]:
                contadorGrado[indice] = contadorGrado[indice] - 1
                if contadorGrado[indice] == 0:
                    listaAux.append(indice)

        resultado.append(cogidoPila)

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
    topologicoSort(g)
