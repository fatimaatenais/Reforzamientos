"""
2. Crea una función que al ingresar dos números por parámetro mostrará
todos los cuadrados de los números que hay entre ellos (Usar la función una
vez y mostrar el resultado por consola). Los números serán ingresados y
solicitados al usuario.
"""

def cuadrados_entre(a, b):
    for i in range(a, b+1):
        print(f"El cuadrado de {i} es {i**2}")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
cuadrados_entre(min(num1, num2), max(num1, num2))
