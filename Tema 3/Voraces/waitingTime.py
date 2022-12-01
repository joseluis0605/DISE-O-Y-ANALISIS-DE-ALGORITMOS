

def minimoTiempo(data):
    acumuladorTiempo= 0
    candidatos= set()
    tam= len(data['cliente'])

    for i in range(0,tam):
        candidatos.add(i)

    for i in range(0,tam):
        menorValor, menorIndice= getMenor(data, candidatos)
        candidatos.remove(menorIndice)
        print("menor valor "+str(menorValor)+" menor indice "+str(menorIndice))
        acumuladorTiempo= acumuladorTiempo + acumuladorTiempo+ menorValor
        print("acumulador actual "+str(acumuladorTiempo))

    acumuladorTiempo= acumuladorTiempo / tam
    print(acumuladorTiempo)

def getMenor(data, candidatos):
    menorIndice= -1
    menorValor= 9999999

    for i in candidatos:
        aux= data['valor'][i]
        if aux< menorValor:
            menorIndice=i
            menorValor= aux

    return menorValor, menorIndice

############ MAIN ##############

data = {
    'valor': [5, 10, 3],
    'cliente': [1, 2, 3]
}

minimoTiempo(data)