"""
6. Ingresar por consola 4 números mediante consola, crear un diccionario
donde los ‘key’ serán los números indicados y los valores serán los cubos de
las estos keys. Mostrar finalmente este diccionario.
"""

numeros = []
for i in range(4):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

cubos = {n: n**3 for n in numeros}

print("Diccionario de cubos:", cubos)