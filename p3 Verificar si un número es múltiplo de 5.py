# Problema 3: Verificar si un número es múltiplo de 5
m = int(input("Bienvenido ingrese un número: "))

#ciclo if para verificar si el numeroe s multiplo de 5
if m % 5 == 0:
    print(f'Segun el numero que ingresaste {m} es múltiplo de 5')
else:
    print(f'Segun el numero que ingresaste {m} no es múltiplo de 5')