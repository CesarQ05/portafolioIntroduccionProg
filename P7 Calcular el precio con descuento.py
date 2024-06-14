# Problema 7: Calcular el precio con descuento
pre = float(input("Bienvenido ingrese el precio del producto: "))

#utilizamos el if si el precio es mayor a $100 y aplicar el descuento si corresponde
if pre > 100:
    des = pre * 0.10
    p_final = pre - des
    print(f'El precio final después de aplicar un descuento del 10% es: ${p_final}')
else:
    pr_final = pre
    print(f'El precio final es: ${pr_final}')
