lista = ['perro', 'gato', 'gallina', 'perro', 'vaca', 'vaca', 'delfin']

def EliminarDuplicados():
    print(lista)
    lista_conjuntos = set(lista)
    print(lista_conjuntos)
    frecuencia = {}
    for i in lista_conjuntos:
        if i in frecuencia:
            frecuencia[i] =+ 1
        else:
            frecuencia[i] = 1
    print(frecuencia)

EliminarDuplicados()