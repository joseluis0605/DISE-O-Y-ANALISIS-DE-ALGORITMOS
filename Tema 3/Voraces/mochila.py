##### algoritmo de la mochila ######

def greedyKnapsack(data):

    tam= len(data['profit'])

# nos creamos los candidatos para meterlos en el conjunto
    candidatos= set()
    for i in range(0, tam):
        candidatos.add(i)

#nos creamos la variable peso maximo que almacena el volumen de la mochila
#tenemos una variable booleana que almacena si esta lleno o no
    pesoMax= data['maxWeight']
    estaLleno= False
    resultado= [0]*tam

    while not  estaLleno and candidatos:

#buscamos el que mejor proporcion beneficio/volumen tiene y borramos el candidato
        mejorIndice= mejorItem(candidatos, data)
        candidatos.remove(mejorIndice)

        pesoMax= pesoMax-data['weight'][mejorIndice]

        if pesoMax >= 0:
            resultado[mejorIndice]= 1
        else:
            pesoMax= pesoMax+ data['weight'][mejorIndice]
            estaLleno= True
            resultado[mejorIndice]= (pesoMax/ data['weight'][mejorIndice] )

    print(resultado)


def mejorItem(candidatos, data): #BUSCAMOS LA MEJOR PROPORCION
    mejorIndice=-1
    mejorProporcion=-1

    for i in candidatos:
        proporcion= data['profit'][i] / data['weight'][i]
        if proporcion > mejorProporcion:
            mejorIndice= i
            mejorProporcion= proporcion
    return  mejorIndice


#knapsack
#main program
data = {}
data['profit'] = [20, 30, 66, 40, 60]
data['weight'] = [10, 20, 30, 40, 50]
data['maxWeight'] = 100

greedyKnapsack(data)
