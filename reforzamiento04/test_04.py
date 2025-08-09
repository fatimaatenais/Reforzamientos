"""
4. Tienes una lista con 5 nombres de estudiantes. Crear un programa que te
pedirá ingresar el nombre de un estudiante, la cuál será eliminada de lista
inicial en caso que no exista en la lista mostrar un mensaje donde indique
que no se encuentre en la lista y luego esta será agregada a la lista.
Finalmente mostrar la lista actualizada en consola.
"""

alumnos = ["Fernando", "María", "Juan", "Dulce", "Mariana"]

nombre = input("Ingrese el nombre del estudiante: ")

if nombre in alumnos:
    alumnos.remove(nombre)
    print(f"{nombre} fue eliminado de la lista.")
else:
    print(f"{nombre} no se encuentra en la lista, se agregará.")
    alumnos.append(nombre)
print("Lista actualizada:", alumnos)
