'''
def suma(a, b):
    total = a + b
    return total


a = int(input('numero 1: '))
b = int(input('numero 2: '))
print(suma(a, b))
# print(total)


def celular(n):
    for i in range(0, 5):
        print(i, 'celular 11', n)
        print('whatsapp +54911', n)


numero = int(input('su numero sin 11: '))
celular(numero)




def arriba(nombre):
    for u in nombre:

        print(u.upper())


nombre = input('su nombre: ')
arriba(nombre)
'''

l = ['limón', 'manzana', 'naranja', 'plátano', 'cereza', 'fresa', 'tomate']
l1 = ['limón1', 'manzana1', 'naranja1',
      'plátano1', 'cereza1', 'fresa1', 'tomate1']

buscar = input('Buscar: ')
# print(l.index(buscar))
# l1.index(buscar)
print(l.find(buscar))
