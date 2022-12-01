def sortCandidates(g):
    candidates = []
    for adjs in g:
        for (start, end, weight) in adjs:
            candidates.append((weight, start, end))
    candidates.sort()
    return candidates

def updateComponents(components, new_id, old_id):
    for i in range(1, len(components)):
        if components[i] == old_id:
            components[i] = new_id

def kruskal(g):
    candidates = sortCandidates(g) #ordenamos aristas en una lista
    components = list(range(len(g))) #lista ordenada ascendente todos os nodos
    count = len(components) - 1 #numero de nodos
    sol = 0 #contador solucion
    i = 0
    while count > 1 and len(candidates) > i: #mientras que no se acaben los nodos y no se acaben los componentes
        (weight, start, end) = candidates[i] #sacamos la informacion de cada candidatos
        if components[start] != components[end]: #
            sol += weight
            count -= 1
            updateComponents(components, components[start], components[end])
        i += 1
    return sol

#Kruskal
g = [
    [],
    [(1,3,1),(1,4,2),(1,7,6)],  #adyacentes del nodo 1
    [(2,5,2), (2,6,4), (2,7,7)],
    [(3,1,1), (3,4,3), (3,7,5)],
    [(4,1,2), (4,3,3),(4,5,1), (4,6,9)],
    [(5,2,2), (5,4,1), (5,7,8)],
    [(6,2,4), (6,4,9)],
    [(7,1,6),(7,2,7),(7,3,5),(7,5,8)]
]

sol = kruskal(g)
print(sol)