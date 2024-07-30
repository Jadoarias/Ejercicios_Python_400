#Define una funcion llamada 'es_palindromo' que toma un argumento llamado 'frase'
def es_palindromo():

#Convertir la frase a minusculas, para asegurarnos de que la comparacion 
#no se vea afectada por las diferencias entre mayusculas y minusculas. Por ejemplo, 'A' y 'a'
    frase = frase.lower()

#Eliminar espacios, reemplaza todos los espacios en 'frase' con una cadena vacia (es decir, elimina los espacios)
#Para que la frase se compare sin importar los espacios entre las palabras
#Ejemplo:
    # Entrada: 'hola mundo'
    # Salida: 'holamundo'
    frase = frase.replace(' ', '')

#Eliminar todos los espacios de la frase
#Esto se hace reemplazando todos los espacios con una cadena vacia 
    frase_invertida = frase[::-1]

#Comparar la frase original (sin espacios y en minusculas) con su version invertida.
#Si son iguales, la frase es un palindromo
    return frase == frase_invertida
#Ejemplo de uso
frase = input("Ingresa una frase: ")
if es_palindromo(frase):
    print("La frase es un palindromo")
else:
    print("La frase no es un palindromo")