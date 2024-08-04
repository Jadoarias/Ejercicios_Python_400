diccionario = {'Juan': 4.0, 'David': 6.0, 'Alan': 5.0, 'Angel': 7.5}

def filtrar_por_valor(estudiantes, nota_aprobatoria=5.0):
    aprobados = {}
    for nombre, nota in estudiantes.items():
        if nota > nota_aprobatoria:
            aprobados[nombre] = nota
    return aprobados

# Llamada a la función
aprobados = filtrar_por_valor(diccionario)
print(aprobados)