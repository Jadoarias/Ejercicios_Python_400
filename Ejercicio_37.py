# A) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista.
# Finalizar al ingresar el número 0, el cual no debe guardarse.

lista = []
numeros = 0
while True:
    numeros = int(input("Ingrese un numero para la lista: "))
    if numeros != 0:
        lista.append(numeros)
    else:
        break
print(lista)

# B) A continuacion, solicitar al usuario que ingrese un numero,
# y, si el numero esta en la lista, eliminar su primera ocurrencia.
# Mostrar un mensaje si no es posible eliminar.

numero = int(input("Ingrese un numero: "))

if numero in lista:
        lista.remove(numero)
        print(f'el numero {numero} esta y se elimino de la lista')
        print(lista)
else:
        print(f"el numero {numero} no esta, no esposible eliminarlo")

# C) Recorrer la lista para imprimir la sumatoria de todos los elementos
suma = 0
for i in lista:
      suma = suma + i
print(f'La suma de los numeros es {suma}')

# D) Solicitar al usuario otro numero y crear una lista con los elementos de la lista 
# original que sean menores que el numero dado. Imprimir esta nueva lista, iterando por ella

numerocriterio = int(input("Ingresa un numero para el criterio: "))

# Creamos una lista vacia
nueva_lista = []

# Itera sobre cada elemento de la lista original
for i in lista:
      if i < numerocriterio:
        nueva_lista.append(i)
print(nueva_lista)

# Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos
# elementos, cada una compuesta por un numero de la lista original y la
# cantidad de veces que aparece en ella. Por ejemplo, si la lista original es 
# [5,16,2,5,57,5,2], la nueva lista contendra: [(5,3),(16,1),(2,2), (57,1)]

frecuencias = {}

# Contar la frecuencia de cada elemento en la lista
for a in lista: 
    # Inicialmente como el valor no esta frecuencias, se ejecuta el else, para agregarlo al diccionario
    # con el contador de 1, luego que se repita el numero se ejecuta la primera
    # condicion aumentando el resultado
    if a in frecuencias:
        frecuencias[a] += 1
    else:
        frecuencias[a] = 1

nueva_lista_tuplas = []
for b,c in frecuencias.items():
    nueva_lista_tuplas.append((b,c))
print(nueva_lista_tuplas)


