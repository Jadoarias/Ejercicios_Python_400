def maximo_de_tres(a,b,c):
    if a > b and a > c:
        print(f"El numero mayor es {a}")
    elif b > a and b > c:
        print(f"El numero mayor es {b}")
    else:
        print(f'El numero mayor es {c}')

maximo_de_tres(100,15,40)
