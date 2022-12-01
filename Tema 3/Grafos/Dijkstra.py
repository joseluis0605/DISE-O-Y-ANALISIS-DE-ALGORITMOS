#### ALGORITMO DE DIJKSTRA #####
# recorremos un grafo ponderado y mostramos el camino minimo hacia cualquier otro nodo

def dijkstra(origen,g): #le pasamos nodo origen y grafo

    tam= len(g)

    visitado= [-1]*(tam+1)
    distancia= [99999]*(tam) #en cada indice se almacena la distancia al nodo
    distancia[origen]=0 # la distancia al origen va a ser siempre 0
    visitado.append(origen)

    for star, end, peso in g[origen]: #cogemos los adyacentes del origen
        distancia[end]= peso # metemos la distancia que hay entre origen y sus adyacentes

    for i in range(2, len(g)): #recorremos empezando por el 2 ya que hemos iterado una vez antes
        adyacenteMinimo=minimaDistancia(distancia, visitado) #sacamos el nodo adyacente que es menor
        visitado.append(adyacenteMinimo)
        for star, end, peso in g[adyacenteMinimo]: #recorremos los adyacentes
            distancia[end]= min(distancia[end], distancia[star]+peso)

    return distancia

def minimaDistancia(distancia, visitado):
    indiceAdyacenteMinimo= -1
    valorMinimo=99999
    for distanciaNodo in range(1,len(distancia)): # nos recorremos las distancias
        if distanciaNodo not in visitado and valorMinimo>distancia[distanciaNodo]: #vemos que el indice (nodo) no esta visitado y que sea menor que el aux
            valorMinimo= distancia[distanciaNodo]
            indiceAdyacenteMinimo= distanciaNodo
    return indiceAdyacenteMinimo

#Dijkstra
g = [
    [],
    [(1,2,5),(1,4,3)],
    [(2,5,1)],
    [],
    [(4,2,1),(4,3,11),(4,5,6)],
    [(5,3,1)]
]

node = 1
sol = dijkstra(node, g)

print(sol)