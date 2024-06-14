# Programa 20: Calcular la tarifa de un taxi
dist = float(input(" Bienvenido ingrese la distancia recorrida en kilómetros: "))


ta_inicial = 2.50 
ta_adicional = 2.00  

if dist <= 10:
    ta_total = dist * ta_inicial
else:
    ta_total = 10 * ta_inicial + (dist - 10) * ta_adicional
print(f'La tarifa total del taxi es: ${ta_total}')
