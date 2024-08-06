original = {'a':1, 'b':2, 'c':3}

def Invertirdiccionario(original):
    invertido={}
    for c, v in original.items():
        invertido[v] = c
    return invertido

invertido = Invertirdiccionario(original)
print(invertido)