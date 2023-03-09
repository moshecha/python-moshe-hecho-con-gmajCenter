def edad(a, b, c, d):
    print(a, '/', b, '/', c)

    return 'edad', d-c


d = int(input('anio actual '))
a = int(input('fecha nacimiento '))
b = int(input('mes nacimiento '))
c = int(input('anio nacimiento '))

print(edad(a, b, c, d))
