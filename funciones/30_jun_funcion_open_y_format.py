
notas = open("funciones/notas.txt")

for linea in notas:
    print(linea)


# funcion format
numero_con_decimal = float(input('ingrese un numero para format: '))
numero_con_decimal = format(numero_con_decimal, "3f")
print(numero_con_decimal)

numero = float(input('un numero para '))
print(abs(numero))
print(round(numero))
print(pow(numero, 2))
