lista = [1, 2, 3, 3, 4, 1, 6, 7, 7]

def contar_elementos():
    frecuencias = {}
    for i in lista:
        if i in frecuencias:
            frecuencias[i] += 1
        else:
            frecuencias[i] = 1
    print(frecuencias) 

contar_elementos()