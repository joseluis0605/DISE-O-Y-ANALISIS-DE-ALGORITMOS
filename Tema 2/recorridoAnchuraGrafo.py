from collections import deque


def bfs_aux(node, graph, visited):
    node_queue = deque()
    visited[node] = True
    node_queue.append(node)
    print("Nodo " + str(node), end=" ")
    while node_queue:
        aux = node_queue.popleft()
        for adj in graph[aux]:
            if not visited[adj]:
                visited[adj] = True
                node_queue.append(adj)
                print("Nodo " + str(adj), end=" ")


def bfs(graph):
    size = len(graph) - 1
    visited = [False] * (size + 1)  # otra alternativa al set
    for node in range (1, size + 1):
        if not visited[node]:
            bfs_aux(node, graph, visited)







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
graph_aux= [
    [],
    [2, 3],
    [1, 4],
    [1, 5],
    [2, 5],
    [4, 3]
]


bfs(graph_AdjList)

# END MAIN