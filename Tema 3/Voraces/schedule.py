##### ALGORITMO PLAZO FIJO #######

def schedule(data):
    candidatos = set()  # vamos a meter a todos los candidatos
    tam = len(data['profit'])

    for i in range(0, tam):
        candidatos.add(i)

    listaResultado = [-1] * tam
    ultimaActividad = max(data['deadLine'])  # maxima actividad para partir de ahi
    i = 0
    while i <= ultimaActividad and candidatos:  # vamos a iterar hasta la fecha mas tardia
        indexMaximo = indiceMax(data, candidatos)  # nos va a sacar el maximo de los candidatos
        candidatos.remove(indexMaximo)
        found = False
        posicion = data['deadLine'][indexMaximo]
        while posicion >= 0 and not found:
            if listaResultado[posicion] == -1:
                listaResultado[posicion] = indexMaximo
                found = True
            else:
                posicion = posicion - 1
        i = i + 1
    print(listaResultado)


def indiceMax(data, candidatos):
    maxValor = 0
    maxIndice = -1

    for i in candidatos:
        aux = data['profit'][i]
        if aux > maxValor:
            maxIndice = i
            maxValor = aux

    return maxIndice


# Schedule
data = {
    'profit': [50, 10, 15, 30],
    'deadLine': [2, 1, 2, 1]
}

schedule(data)
