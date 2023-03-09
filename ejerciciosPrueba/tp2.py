'''
numero = int(input('un nro: '))

while numero > 0:
    if (numero % 3) == 0:
        print(numero, 'mult 3')
    numero -= 2

for x in range(5, 100, 20):
    print(x)
numeroo = int(input('num: '))

for i in range(0, numeroo):
    print('hell', i)

numero = int(input('un num: '))

for i in range(1, numero):
    if (i % 2) == 0:
        print('par')
    else:
        print('impar', i)

numero = int(input('num: '))
while numero <= 20:
    print('el num mayor a 20')
    numero = int(input('num: '))

print(numero % 5)
'''
#Es necesario importar las depencendias necesarias
from datetime import date
from datetime import datetime

#Día actual
today = date.today()

#Fecha actual
now = datetime.now()

print(today)
print(now)

print("El día actual es {}".format(today.day))
print("El mes actual es {}".format(today.month))
print("El año actual es {}".format(today.year))

print("El día actual es {}".format(now.day))
print("El mes actual es {}".format(now.month))
print("El año actual es {}".format(now.year))

print("La hora actual es {}".format(now.hour))
print("El minuto actual es {}".format(now.minute))
print("El segundo actual es {}".format(now.second))

fecha = (f'{format(today.day)}/{format(today.month)}/{(today.year)}')
print(fecha)