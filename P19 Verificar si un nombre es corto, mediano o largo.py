#Programa 19: Verificar si un nombre es corto, mediano o largo

nombre = input("Bienvenido ingrese un nombre: ")

lon_nombre = len(nombre)


if lon_nombre < 5:
    categoria = "corto"
elif 5 <= lon_nombre <= 8:
    categoria = "mediano"
else:
    categoria = "largo"


print(f'El nombre {nombre} es de longitud {lon_nombre} y se clasifica como nombre {categoria}')
