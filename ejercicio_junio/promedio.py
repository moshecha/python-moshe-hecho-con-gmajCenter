nota1 = float(input('tu nota 1 '))
nota2 = float(input('tu nota 2 '))
nota3 = float(input('tu nota 3 '))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 6:
    print('tu promedio es: ', promedio, 'APROBADO')
else:
    print('tu promedio es: ', promedio, 'DESAPROBADO')
