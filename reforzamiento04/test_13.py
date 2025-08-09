"""
8. Crear una agenda basada en un diccionario donde los key serán los nombres
de las personas y sus “values” serán los números de teléfono de c/u.
Ingresarás por consola el nombre y el número de cada persona que serán
registrados en la agenda.
El programa también te permitirá buscar por nombre en el diccionario en caso
no exista mostrar un mensaje de “No se encuentra registrado en la agenda”
"""

agenda = {}

cantidad = int(input("¿Cuántas personas desea registrar? "))
for i in range(cantidad):
    nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
    telefono = input(f"Ingrese el teléfono de {nombre}: ")
    agenda[nombre] = telefono

buscar = input("Ingrese el nombre que desea buscar en la agenda: ")
if buscar in agenda:
    print(f"{buscar} está registrado con el número {agenda[buscar]}")
else:
    print("No se encuentra registrado en la agenda.")