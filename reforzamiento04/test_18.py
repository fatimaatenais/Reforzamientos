"""
Funciones:
1. Pedir dos números positivos mediante terminal al usuario. Mostrar
como salida el número cuya sumatoria de dígitos es el mayor y los números
cuya sumatoria de dígitos es menor que 10. Utilizar una o más funciones, según
sea conveniente.
"""

def suma_digitos(num):
    return sum(int(d) for d in str(num))

num1 = int(input("Ingrese el primer número positivo: "))
num2 = int(input("Ingrese el segundo número positivo: "))

suma1 = suma_digitos(num1)
suma2 = suma_digitos(num2)

if suma1 > suma2:
    print(f"El número con mayor suma de dígitos es {num1} con {suma1}")
elif suma2 > suma1:
    print(f"El número con mayor suma de dígitos es {num2} con {suma2}")
else:
    print(f"Ambos números tienen la misma suma de dígitos ({suma1})")

for n in (num1, num2):
    if suma_digitos(n) < 10:
        print(f"{n} tiene suma de dígitos menor que 10")
