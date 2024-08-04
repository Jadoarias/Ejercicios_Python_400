palabra = 'Llego del trabajo cansada y aun cansada hago la cena llego del trabajo cansada y aun en ese estado hago la cena'

lista_palabra = palabra.split()
print(lista_palabra)

frecuencias = {}

for i in lista_palabra:
    if i in frecuencias:
        frecuencias[i] += 1
    else:
        frecuencias[i] = 1
print(frecuencias) 