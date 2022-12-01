#funciones a usar

def dfsRec(node, graph, visit):
    visit.add(node)
    print("visiting node "+ str(node), end = "\n")
    for nodoActual in graph[node]:
        if nodoActual not in visit:
            dfsRec(nodoActual, graph, visit)

def dfs(g): #funcion que devuelve el recorrido en profundidad
    n= len(g) - 1
    visited= set()
    for v in range(1, n+1):
        if v not in visited:
            dfsRec(v,g,visited)


# MAIN

# lista de adyacencia

graph_AdjList = [  # estamos haciendo una lista de listas
    [], # eliminamos lo que es la fila y columna 0
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

dfs(graph_AdjList)

# END MAIN
