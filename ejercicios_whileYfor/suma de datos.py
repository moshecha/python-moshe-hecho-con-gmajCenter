numero = int(input('Numero: '))
total = 0
cantidadN = 0
while numero != 0 and numero > 0:
    total += numero
    cantidadN += 1
    print('Total:', total, 'Veces:', cantidadN)
    numero = int(input('Numero: '))

for a in range(0, cantidadN+1):
    print(a, 'Total:', total, 'Veces:', cantidadN)
