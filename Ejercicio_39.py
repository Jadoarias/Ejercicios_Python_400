lista_nombre_pila_nivel_primario = []
lista_nombre_pila_nivel_secundario = []

nombre_pila_nivel_primario = None
nombre_pila_nivel_secundario = None

while True:
    if nombre_pila_nivel_primario != 'x':
        nombre_pila_nivel_primario = input('Ingresa los nombres de pila de los alumnos nivel primario: ')
        lista_nombre_pila_nivel_primario.append(nombre_pila_nivel_primario)
    else:
        break
print('Finalizo el Ingreso')
lista_nombre_pila_nivel_primario.remove('x')
conjunto_lista_nombre_pila_nivel_primario = set(lista_nombre_pila_nivel_primario)
print(conjunto_lista_nombre_pila_nivel_primario)


while True:
    if nombre_pila_nivel_secundario != 'x':
       nombre_pila_nivel_secundario = input('Ingresa los nombres de pila de los alumnos nivel secundario: ')
       lista_nombre_pila_nivel_secundario.append(nombre_pila_nivel_secundario)
    else:
        break
print('Finalizo el ingreso')
lista_nombre_pila_nivel_secundario.remove('x')
conjunto_lista_nombre_pila_nivel_secundario = set(lista_nombre_pila_nivel_secundario)
print(conjunto_lista_nombre_pila_nivel_secundario)

for i in conjunto_lista_nombre_pila_nivel_primario:
    for a in conjunto_lista_nombre_pila_nivel_secundario:
        if i == a:
            print(a)

nombre_unicos = conjunto_lista_nombre_pila_nivel_primario - conjunto_lista_nombre_pila_nivel_secundario
print(nombre_unicos)



