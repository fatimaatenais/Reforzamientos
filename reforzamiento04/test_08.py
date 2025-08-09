"""
3. Convertir tu diccionario a una lista y mostrar en consola el tipo de datos
final que tienes.
"""

fatima = {"color" : "negro", "curso" : "Física", "banda" : "Green day", "edad" : 17}
fatima.values()

list(fatima.values())

for elemento in list(fatima.values()):
    print(elemento, "es de tipo", type(elemento))

