lista_caracteres = []
contador = 0

while True:
    if contador < 5:
        contador += 1
        caracteres = input('Ingresa un caracter: ')
        lista_caracteres.append(caracteres)
    else:
        print(lista_caracteres)
        break

frecuencias = {}

for i in lista_caracteres:
    if i in frecuencias:
        frecuencias[i] += 1
    else:
        frecuencias[i] = 1

print(frecuencias)

nueva_lista_caracteres = []
for b, c in frecuencias.items():
    nueva_lista_caracteres.append((b,c))
print(nueva_lista_caracteres)

