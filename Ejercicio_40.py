
lista_resultado = []
lista_domicilio = []
conjunto_con_domi = set()


def comprasclientes():
    pregunta = input("Desea agregar informacion de compra: \n"
                     "si/no ")
    
    while True:
        if pregunta == "si":
            nombre = input('Ingresa nombre del cliente: ')
            dia = input('Ingrese dia de la compra: ')
            monto = input('Ingrese monto de compra: ')
            domicilio = input('Ingresa domicilio del cliente: ')
            resultado = (nombre, dia, monto, domicilio)
            lista_resultado.append(resultado)
            pregunta = input("Desea agregar informacion de compra: \n"
                     "si/no ")
            
        elif pregunta == 'no':
            print(lista_resultado)
            break

        else:
            print('No es una opcion valida')
            pregunta = input("Desea agregar informacion de compra: \n"
                     "si/no ")

    for i in lista_resultado:
        g = i[3]
        h = i[0]
        con_resul = (g,h)
        conjunto_con_domi.add(con_resul)
    print(conjunto_con_domi)
    

comprasclientes()

#PENDIENTE POR TERMINAR