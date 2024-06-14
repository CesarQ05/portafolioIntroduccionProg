# Programa 12: Calcular el salario neto
s_bruto = float(input("Bienvenido ingrese su salario bruto: "))


if s_bruto > 2000:
    impuesto = s_bruto * 0.20
    sal_neto = s_bruto - impuesto
    print(f'El salario neto después de aplicar el impuesto es: ${sal_neto}')
else:
    salario_neto = s_bruto


print(f'El salario neto después de aplicar el impuesto es: ${salario_neto}')
