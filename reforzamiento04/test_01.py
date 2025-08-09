"""
Listas:
1. Escribir un programa donde ingresarás el tamaño de la lista mediante
consola, este tamaño servirá para ingresar una cantidad X de nombres de
alumnos. Ingresarás los nombres mediante consola también.
Se quiere mostrar finalmente el tamaño de la lista y todos los nombres de
la lista que fueron ingresados.
"""

lista_tmn = int(input("¿Cuántos alumnos quiere ingresar?: "))
alumnos = []

for x in range(lista_tmn):
    nombre = input(f"Ingrese el nombre del alumno {x+1}: ")
    alumnos.append(nombre)

print("\nCantidad de alumnos ingresados:", len(alumnos))
print("Lista de alumnos:")
for alumno in alumnos:
    print(alumno)
