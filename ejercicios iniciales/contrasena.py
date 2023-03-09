contrasena = input('su contrasena: ')
veces = 1

while contrasena != 'hola' and veces < 10:
    print('Falsa')
    veces = veces+1
    print(veces, 'intento')
    print('Te quedan', 11-veces, 'intentos')
    contrasena = input('su contrasena: ')

if contrasena == 'hola':
    print('Verdadera')
else:
    print('intentaste:', veces, 'veces una contrasena invalida')
