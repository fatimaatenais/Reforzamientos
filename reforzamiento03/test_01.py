# Plantear las variables

soles_01 = 456.50
soles_02 = 379.80
soles_03 = 123.12

# Tasa de cambio

tasa_de_cambio = 3.56

# Convertir

dolar_01 = soles_01 / tasa_de_cambio
dolar_02 = soles_02 / tasa_de_cambio
dolar_03 = soles_03 / tasa_de_cambio

print("Conversión de soles a dolares:")
print("S/ {} --> $ {}".format(soles_01, f"{dolar_01:.2f}"))
print("S/ {} --> $ {}".format(soles_02, f"{dolar_02:.2f}"))
print("S/ {} --> $ {}".format(soles_03, f"{dolar_03:.2f}"))
