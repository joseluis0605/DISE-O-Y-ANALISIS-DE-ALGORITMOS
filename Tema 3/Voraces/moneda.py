# vamos a hacer el problema de la moneda con un algoritmo schedule
# vamos a sacar el minimo de monedas para pagar x cantidad

# vamos a necesitar un array de monedas donde vamos a tener todas las monedas posibles


def moneda(monedasPermitidas, dineroActual):
    monedasElegidas = []

    for moneda in range(0, len(monedasPermitidas)):
        valor = monedasPermitidas[moneda]
        while valor <= dineroActual:
            if dineroActual - valor >= 0:
                monedasElegidas.append(valor)
                dineroActual = dineroActual - valor

    print(monedasElegidas)


def ordenarMayorMenor(monedasPermitidas):
    tam= len(monedasPermitidas)
    for j in range(0,tam):
        for i in range(0, tam-1):
            if monedasPermitidas[i]<monedasPermitidas[i+1]:
                aux= monedasPermitidas[i]
                monedasPermitidas[i]= monedasPermitidas[i+1]
                monedasPermitidas[i+1]= aux


if __name__ == '__main__':
    monedasPermitidas = [1, 2, 5, 10, 20, 50]
    ordenarMayorMenor(monedasPermitidas)
    dineroAcutal = 29

    moneda(monedasPermitidas, dineroAcutal)
