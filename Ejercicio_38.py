lista_de_pasajeros = [('Juan', 15639, 'Cartagena'), ('Camilo', 78569, 'Caracas'), ('Laura', 14563, 'Caracas'), ('David', 4569, 'Bogota') ]
lista_de_origen = [('Argentina', 'Buenos Aires')]
resultado = None


def pasajeros():
        nombre = input("Ingresa el nombre del pasajero: ")
        dni = int(input("Ingresa el dni: "))
        destino = input('Ingresa ciudad destino: ')
        pasajero = (nombre, dni, destino)
        lista_de_pasajeros.append(pasajero)
        print(lista_de_pasajeros)

def origen():
    pais_origen = input('Ingresa nombre del pais destino: ')
    ciudad_origen = input('Ingresa la ciudad destino: ')
    origen = (pais_origen, ciudad_origen)
    lista_de_origen.append(origen)
    print(origen)   

def dni_ciudad_destino():
    dni_consulta = int(input('Ingresa el dni del pasajero, para conocer la ciudad destino: '))
    for i in lista_de_pasajeros:
        if dni_consulta == i[1]:
            resultado = (i[0], i[2])
            break

    if resultado:
     print(resultado)
    else:
     print('el dni es incorrecto')
    
def ciudad_pasajeros():
    consulciudad = input('Ingresa la ciudad a consultar el numero de pasajeros totales: ')
    contador = 0
    for i in lista_de_pasajeros:
        if consulciudad == i[2]:
            contador +=1
    print(contador)
    


programa = input('Bienvenido al consultor de vuelos \n'
                 'Selecciona la opcion deseada: \n'
                 '1- Agregar pasajeros a la lista de viajeros \n'
                 '2- Agregar ciudades a la lista de ciudades de origen \n'
                 '3- Dado el DNI de un pasajero, ver a qué ciudad viaja \n'
                 '4- Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad \n'
                 '5- Salir del programa \n')

if programa == "1":
    pasajeros()
elif programa == '2':
    origen()
elif programa == '3':
     dni_ciudad_destino()
elif programa == '4':
    ciudad_pasajeros()
else:
    print('Saliste del Programa')



    


