"""
5. Crear una función que aceptará por parámetro dos valores que serán
ingresados por el usuario, una lista donde los valores serán llenados por el
usuario también y un segundo parámetro que eliminará de la lista que fue
ingresada a la función, finalmente el output de la función será la lista
actualizada sin el valor que se sacará de la lista. Mostrar también la lista
original y el número que fue eliminado.
"""

def eliminar_valor(lista, valor):
    lista_actualizada = lista.copy()
    if valor in lista_actualizada:
        lista_actualizada.remove(valor)
    return lista_actualizada

lista_original = []
for i in range(5):
    lista_original.append(int(input(f"Ingrese valor {i+1}: ")))

valor_a_eliminar = int(input("Ingrese el valor a eliminar: "))

lista_nueva = eliminar_valor(lista_original, valor_a_eliminar)

print("Lista original:", lista_original)
print("Valor eliminado:", valor_a_eliminar)
print("Lista actualizada:", lista_nueva)
