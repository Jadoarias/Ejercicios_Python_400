def EsBisiesto(anio):
    """Determina si un año es bisiesto."""
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def DiasDelMes(mes, anio):
    """Devuelve el número de días en un mes dado el año."""
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mes == 2 and EsBisiesto(anio):
        return 29
    return dias_por_mes[mes - 1]

def ValidarFecha(dia, mes, anio):
    """Valida si la fecha proporcionada es correcta."""
    if anio < 1:
        return False
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > DiasDelMes(mes, anio):
        return False
    return True

def LeerFecha():
    """Lee una fecha del usuario, valida y la devuelve como una tupla (día, mes, año)."""
    while True:
        try:
            dia = int(input("Ingresa el día: "))
            mes = int(input("Ingresa el mes: "))
            anio = int(input("Ingresa el año: "))
            if ValidarFecha(dia, mes, anio):
                return dia, mes, anio
            else:
                print("Fecha inválida. Por favor, ingresa una fecha correcta.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa números enteros para el día, mes y año.")

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
