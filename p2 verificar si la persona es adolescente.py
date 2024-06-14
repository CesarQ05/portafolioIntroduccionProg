# Problema 2: Determinar si una persona es adolescente
e = int(input("Bienvenido ingresa tu edad: "))

#ciclo if para verificar si es adolescente o no
if 13 <= e <= 19:
    print(f'Segun la edad que ingresaste {e} eres un adolescente')
else:
    print(f'Segun la edad que ingresaste {e} no eres un adolescente')
