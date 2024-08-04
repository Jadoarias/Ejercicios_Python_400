prueba_deportiva={'Jorge':500,'Diana':600,'Rodrigo':800,'Julia':750,'Li':900}

def EliminarClaves(nombre, v = 600 ):
    claves = {}
    for nombre, valor in prueba_deportiva.items():
        if valor > v:
            claves[nombre] = valor
    return claves
        
claves = EliminarClaves(prueba_deportiva)

print(claves)
