# ORGANIZACION TOPOLOGICA
from collections import deque


def topoSortRec(data, k):
    data["state"][k] = "VISITED"
    data["time"] += 1
    data["d"][k] = data["time"]
    for adj in data["graph"][k]:
        if data["state"][adj] == "NOT VISITED":
            topoSortRec(data, adj)
    data["state"][k] = "FINISH"   # Color negro
    data["time"] += 1
    data["f"][k] = data["time"]
    data["sol"].appendleft(k)

def toposort(g):

    # Información que nos va a resultar útil para resolver el problema
    data = {
        "graph": g,  # Puntero al grafo
        "state": dict(),  # Estado: blanco, gris, negro
        "d": dict(),    # Descubrimiento, lo que va antes de '/'
        "f": dict(),    # Final, lo que va después de '/'
        "time": 0,
        "sol": deque()
    }
    for k in g.keys():
        data["state"][k] = "NOT VISITED"
        data["d"][k] = 0
        data["f"][k] = 0
    for k in g.keys():
        if data["state"][k] == "NOT VISITED":
            topoSortRec(data, k)

    print(data["sol"])


# Main prog.
graph = dict()

graph = {
    # Descripción enumerativa de lo que queremos hacer:
    "calcetines": ["zapatos"],
    "pantalon":["zapatos", "cinturon"],
    "camisa": ["cinturon", "jersey"],
    "zapatos": [],
    "cinturon": [],
    "jersey": []
}

toposort(graph)
