def superposicion(lista1, lista2):
    #Recorrer cada elemento de la primera lista
    for elemento1 in lista1:
    #Recorrer cada elemento de la segunda lista
        for elemento2 in lista2:
    # Comparar el elemento actual de la primera lista con el elemento actual de la segunda lista
            if elemento1 == elemento2:
            #Si encontramos un elemento comun, devolvemos True.
             return True
    # Si el bucle termina sin encontrar ningun elemento comun, devolvemos False.
    return False

lista1 = [1, 2, 3, 4]
lista2 = [4, 5, 6, 7]
if superposicion(lista1, lista2):
    print("Las listas tienen al menos un miembro en común.")
else:
    print("Las listas no tienen ningún miembro en común.")