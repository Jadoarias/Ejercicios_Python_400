def EsBisiesto(anio):
    """Determina si un año es bisiesto."""
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def DiasDelMes(mes, anio):
    """Devuelve el número de días en un mes dado el año."""
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mes == 2 and EsBisiesto(anio):
        return 29
    return dias_por_mes[mes - 1]

def LeerFecha():
    """Lee una fecha del usuario y la devuelve como una tupla (día, mes, año)."""
    dia = int(input("Ingresa el día: "))
    mes = int(input("Ingresa el mes: "))
    anio = int(input("Ingresa el año: "))
    return dia, mes, anio

def Calcular_Dia_Juliano(dia, mes, anio):
    """Calcula el día juliano para una fecha dada."""
    dia_juliano = 0
    for m in range(1, mes):
        dia_juliano += DiasDelMes(m, anio)
    dia_juliano += dia
    return dia_juliano

def principal():
    dia, mes, anio = LeerFecha()
    dia_juliano = Calcular_Dia_Juliano(dia, mes, anio)
    print(f"El día juliano para la fecha {dia}/{mes}/{anio} es: {dia_juliano}")

# Llamada a la función principal
principal()
