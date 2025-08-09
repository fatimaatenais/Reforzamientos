"""
Strings:
1. Dada una frase u oración encontrar que palabra es la que tiene más
caracteres y cuántos caracteres tiene
Input: “La programación en Python es poderosa”
Output: “programación” – 12 caracteres
"""


frase = "La programación en Python es poderosa"
palabras = frase.split()

palabra_mas_larga = max(palabras, key=len)
longitud = len(palabra_mas_larga)

print(f"{palabra_mas_larga} - {longitud} caracteres")
