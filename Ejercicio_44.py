diccionario = {'Juan':4.0, 'David': 6.0, 'Alan':5.0, 'Angel': 7.5}

def CalcularPromedio():
    suma = 0
    lista_calificaciones =[]
    for i in diccionario.values():
        lista_calificaciones.append(i)
    print(lista_calificaciones)

    for i in lista_calificaciones:
        suma += i
    print(suma)

    promedio = suma/len(lista_calificaciones)
    print(promedio)

CalcularPromedio()