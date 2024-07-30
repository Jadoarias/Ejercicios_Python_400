lista = []
numeros = 0
while True:
    numeros = int(input("Ingrese un numero: "))
    if numeros != 0:
        lista.append(numeros)
    else:
        break
print(lista)


