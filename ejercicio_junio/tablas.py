#tabla = int(input('Que tabla queres? '))
numero = 0

for i in range(0, 10):
    tabla = int(input('Que tabla queres? '))
    print('Tabla del:', tabla)
    while numero <= 10:
        print(numero, 'X', tabla, numero * tabla)
        numero += 1
    numero = 0
