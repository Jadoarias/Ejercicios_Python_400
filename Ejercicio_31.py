def suma(a,b,c,d):
    lista = [a,b,c,d]
    contador = 0
    sum = 0
    for i in lista:
        contador = contador + 1
        sum += i
    print(contador)
    print(sum)


def multi(a,b,c,d):
    lista = [a,b,c,d]
    contador = 0
    mul = 1
    for i in lista:
        contador = contador + 1
        mul *= i
    print(contador)
    print(mul)

multi(1,2,3,4)