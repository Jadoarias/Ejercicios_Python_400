import math

def AreaPerimetro ():
    radio = int(input("Ingresa el radio: "))
    calarea = math.pi*(radio)**2
    calper = (2*math.pi)*radio
    print(calarea)
    print(calper)
    return

AreaPerimetro()