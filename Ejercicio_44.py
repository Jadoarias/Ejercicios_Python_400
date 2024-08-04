diccionario = {'Juan':4.0, 'David': 6.0, 'Alan':5.0, 'Angel': 7.5}


def CalcularPromedio():
    suma = 0
    lista_nombres =[]
    for i in diccionario.values():
        lista_nombres.append(i)
    print(lista_nombres)

    for i in lista_nombres:
        suma += i
    print(suma)

CalcularPromedio()