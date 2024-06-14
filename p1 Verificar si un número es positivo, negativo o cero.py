# Problema 1 con Sentencia selectivas IF
n = float(input("Bienvenido ingrese un número: "))

#ciclo if para verificar si el numero es positivo, negativo o cero. 
if n > 0:
    print(f'El número es que ingresaste {n} es positivo')
elif n < 0:
    print(f'El número es que ingresaste {n} es negativo')
else:
    print(f'El número es que ingresaste {n} es cero')
