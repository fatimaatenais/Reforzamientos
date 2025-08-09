"""
4. Pedir al usuario que ingrese un nombre y apellidos el cual será usada
por un parámetro para una función que se creará e indicará cuantas letras
tiene el nombre solamente. Usar la función un mínimo de dos veces para dos
personas e indicar quien tiene el nombre con mayor número de caracteres
(condicional)
"""

def contar_letras_nombre(nombre_completo):
    nombre = nombre_completo.split()[0]
    return len(nombre)

persona1 = input("Ingrese nombre y apellido de la primera persona: ")
persona2 = input("Ingrese nombre y apellido de la segunda persona: ")

long1 = contar_letras_nombre(persona1)
long2 = contar_letras_nombre(persona2)

print(f"{persona1.split()[0]} tiene {long1} letras")
print(f"{persona2.split()[0]} tiene {long2} letras")

if long1 > long2:
    print(f"{persona1.split()[0]} tiene el nombre más largo")
elif long2 > long1:
    print(f"{persona2.split()[0]} tiene el nombre más largo")
else:
    print("Ambos nombres tienen la misma cantidad de letras")
