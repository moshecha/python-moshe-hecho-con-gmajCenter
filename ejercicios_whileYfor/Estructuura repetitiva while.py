'''#numero = int(input('canttidad de veces '))
uno = 1
while (uno < numero):
    print('hola', uno)
    uno = uno + 1
'''
tabla = 1
numero = 1
print('TABLAS')
repetir = input('Te digo las tablas? ')

while repetir == 'si':

    while (tabla < 10):
        print('Tabla del', tabla)
        numero = 1
        tabla = tabla + 1
        while numero <= 10:
            print(tabla, 'X', numero, '=', numero * tabla)
            numero = numero + 1
    repetir = input('te las repito? ')
    if repetir == 'si':
        tabla = 1
    else:
        print('saludos!')
        tabla = 10
