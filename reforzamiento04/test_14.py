"""
9. Una empresa desea gestionar las facturas pendientes que tiene por pagar,
para esto se creará un diccionario donde tendrá por key el número de factura
“00054” y su value será el coste de la factura. El programa tendrá la opción
de pedir nueva factura (por consola) que se agregará al diccionario. Cada vez
que el área de contabilidad pague una factura se pedirá el número de factura
que fue cancelada, si existe mostrar un mensaje donde indicará “La factura
ya está cancelada” caso contrario “El número de factura no existe”.
Considerar que cada vez que se realice algún pago o ingreso de una nueva
factura se mostrará inmediatamente al diccionario actualizado.
"""

facturas = {}

while True:
    opcion = input("\n1. Agregar nueva factura\n2. Pagar factura\n3. Salir\nElige una opción: ")

    if opcion == "1":
        numero = input("Ingrese el número de factura: ")
        coste = float(input("Ingrese el coste de la factura: "))
        facturas[numero] = coste
        print("Factura agregada.")
        print("Facturas actuales:", facturas)  # Mostrar actualización

    elif opcion == "2":
        numero = input("Ingrese el número de factura a pagar: ")
        if numero in facturas:
            del facturas[numero]
            print("La factura ya está cancelada.")
        else:
            print("El número de factura no existe.")
        print("Facturas actuales:", facturas)  # Mostrar actualización

    elif opcion == "3":
        break

    else:
        print("Opción inválida.")
