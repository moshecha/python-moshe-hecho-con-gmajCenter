from ctypes.wintypes import HLOCAL


salario = int(input('ingrese su salario  '))
edad = int(input('ingrese su edad  '))

if (salario > 50000 and edad < 65):
    print('puede acceder ')
else:
    print("no puede acceder")
