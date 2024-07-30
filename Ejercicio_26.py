from fractions import Fraction

def fracciones(a,b):
    print(Fraction(a,b))
fracciones(4,5)

def sumafracciones(a,b,c,d):
    suma = Fraction(a,b) + Fraction(c,d)
    print(suma)
sumafracciones(7,8,9,5)