"""
4. Crear un diccionario con 6 departamentos del país.
- Borrar cualquier departamento, usando la palabra reservada del.
- Actualizar el penúltimo departamento por otro.

- Comprobar que no existe este departamento borrado dentro del
diccionario.
"""

departamentos = {"dep1" : "Lima", "dep2" : "Lambayeque", "dep3" : "Junín", "dep4" : "Piura", "dep5" : "Áncash", "dep6" : "Loreto"}

del departamentos["dep6"]
print(departamentos)

departamentos["dep5"] = "Cajamarca"
print("Diccionario nuevo:", departamentos)

if "dep6" not in departamentos:
    print("El departamento eliminado ya no está en el diccionario.")
