diccionario = {'Juan': 4.0, 'David': 6.0, 'Alan': 5.0, 'Angel': 7.5}
diccionario_1 = {'Manzana':1, 'Pera':2, 'Verde':3}

lista_1 = list(diccionario.items())
lista_2 = list(diccionario_1.items())

print(lista_1)
print(lista_2)

lista_final = lista_1 + lista_2
print(lista_final)

diccionario_final = dict(lista_final)
print(diccionario_final)