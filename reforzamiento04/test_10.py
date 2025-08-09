"""
5. Ingresar el nombre de tu carrera dentro de los valores que tienes en tu
diccionario.
- Mostrar en consola los valores de tu carrera y nombre agregándolos a
una variable c/u
"""

datos = {"nombre": "Fátima", "edad": 17, "salario": 1500}
carrera_ingresada = input("Ingresa tu carrera: ")

datos["carrera"] = carrera_ingresada

nombre = datos["nombre"]
carrera = datos["carrera"]

print("Nombre:", nombre)
print("Carrera:", carrera)
