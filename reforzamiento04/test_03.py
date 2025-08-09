"""
3. Crea una lista vacía, luego ingresa sus valores (10 valores numéricos) y
finalmente muestra la suma y la media de los números ingresado
insertados en la terminal
"""
numeros = []

for x in range(10):
    valor = float(input(f"Ingrese el numero {x+1}: "))
    numeros.append(valor)
print("LISTA FINAL:",numeros)
