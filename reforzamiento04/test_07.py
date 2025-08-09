"""

2. Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar
el valor del salario y DNI en consola. También elimina el key edad de tu
diccionario, incluyendo su valor. Mostrar finalmente el diccionario
actualizado.
"""

#Ejercicio 1:
datos = {"nombre" : "Fátima", "edad" : "17", "salario" : "6000"}
datos.values()

list(datos.values())
print("Lista:", list(datos.values()))

#Ejericio 2:
datos["DNI"] = "78945612"
print("Lista actualizada:",datos)
print(datos["salario"], datos["DNI"])

del datos["edad"]
print("Diccionario actualizado:", datos)




