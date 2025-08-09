"""
2. Crear un programa en Python donde tendrás una lista con 6 departamentos,
el programa te pedirá ingresar 2 departamentos el cual el segundo
departamento que ingreses sustituirá al primero de la lista.
"""
departamentos = ["Lambayeque", "Tumbes", "Piura", "Lima", "Ica", "Loreto"]

dato = input("Ingrese el departamento que desea reemplazar: ")
dato_02 = input("Ingrese un nuevo departamento: ")

if dato in departamentos:
    indice = departamentos.index(dato)
    departamentos[indice] = dato_02
    print("\nLista actualizada:")
    print(departamentos)
else:
    print(f"El departamento '{dato}' no esta en la lista")