contrasena = input('contrasena: ')
tropical_1 = 300
tropical_2 = 700
ganancia = 1.3
confeccion = 500

if contrasena == 'moshe' or contrasena == 'tela':
    tropical_1 = int(input('valor de tropical de 1.50m.: '))
    tropical_2 = int(input('valor de tropical de 3m: '))
    print(tropical_1, 'Y', tropical_2)
else:
    nombre = input('su nombre: ')
    print(nombre, 'Bienvenido!')
ancho = float(input('ancho 1.50 o 3m? '))

while ancho != 1.5 and ancho != 1.50 and ancho != 3:
    print('Ancho no valido')
    ancho = float(input('ancho 1.50 o 3m? '))

if ancho == 1.50:
    largo = float(input('cual es el largo? '))
    print('El precio del mantel es: $',
          (largo * tropical_1 * ganancia) + confeccion)
elif ancho == 3:
    largo = float(input('cual es el largo? '))
    print('El precio del mantel es: $',
          (largo * tropical_2 * ganancia) + confeccion)
