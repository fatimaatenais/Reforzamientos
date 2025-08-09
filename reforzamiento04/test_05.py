"""
5. Ingresar por consola el tamaño de una lista, luego empezarás a ingresar los
datos mediante consola también (5 compañías relacionadas con al mundo de
TI) y harás una copia donde adrede agregarás nombres que estarán
repetidos (mediante consola) para que finalmente muestres otra lista donde
solo se mostrará los nombres no repetidos y también te mostrará la lista
inicial
"""

usuario = int(input("¿Cuántas compañías vas a guardar?: "))
companias = []

for i in range(usuario):
    nombre = input(f"Ingrese el nombre de la compañía {i + 1}: ")
    companias.append(nombre)

companias_con_repetidos = companias.copy()
cantidad_extra = int(input("¿Cuántos nombres adicionales (con repetidos) quieres agregar? "))
for i in range(cantidad_extra):
    nombre_extra = input(f"Ingrese el nombre extra {i+1} (puede ser repetido): ")
    companias_con_repetidos.append(nombre_extra)

companias_sin_repetidos = []
for nombre in companias_con_repetidos:
    if nombre not in companias_sin_repetidos:
        companias_sin_repetidos.append(nombre)

print("\nLista inicial:", companias)
print("Lista sin repetidos:", companias_sin_repetidos)