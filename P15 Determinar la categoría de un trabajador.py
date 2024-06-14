# Programa 15: Determinar la categoría de un trabajador
as_experiencia = float(input("Bienvenido ingrese sus años de experiencia: "))


if as_experiencia < 2:
    categoria = "Junior"
elif 2 <= as_experiencia <= 5:
    categoria = "Semi-Senior"
else:
    categoria = "Senior"


print(f'La categoría del trabajador es: {categoria}')
