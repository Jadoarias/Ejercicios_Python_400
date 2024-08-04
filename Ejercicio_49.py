prueba_deportiva={'Jorge':500,'Diana':600,'Rodrigo':800,'Julia':750,'Li':900}
lista_prueba_deportiva = []

def Valorminimoymaximo():
    for i in prueba_deportiva.values():
        lista_prueba_deportiva.append(i)
    print(lista_prueba_deportiva)
    print(max(lista_prueba_deportiva))
    print(min(lista_prueba_deportiva))

Valorminimoymaximo()