"""""Ejemplo Paso a Paso
Vamos a desglosar cómo funciona la función con el ejemplo maximo_comun_divisor_recursivo(84, 75).

Primera llamada:

a = 84
b = 75
b no es 0, así que calculamos a % b:
84 % 75 = 9
Llamamos a la función recursivamente con a = 75 y b = 9.

Segunda llamada:

a = 75
b = 9
b no es 0, así que calculamos a % b:
75 % 9 = 3
Llamamos a la función recursivamente con a = 9 y b = 3.

Tercera llamada:

a = 9
b = 3
b no es 0, así que calculamos a % b:
9 % 3 = 0
Llamamos a la función recursivamente con a = 3 y b = 0.
Cuarta llamada (caso base):

a = 3
b = 0
b es 0, así que retornamos a, que es 3.
Entonces, el resultado final es 3, que es el MCD de 84 y 75."""""


def maximo_comun_divisor_recursivo(a, b):
    if b == 0:
        return a
    return maximo_comun_divisor_recursivo(b, a % b)

print(maximo_comun_divisor_recursivo(84,75))