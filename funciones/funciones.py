lista = [1, 1.50, 'hola']
lista1 = 'hola como estas'
lista3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]
for a in lista:
    print(a)

for b in lista1:
    print(b)

print('aaaa', max(lista3))
print(max(1, 2, 3, 4, 5, 6, 7, 8, 9))
print(max(1, 1))
print(lista1[4])
print(min(True, False))


print(len(lista3))
print(len(lista1))
print(len(lista))
print(len('19191919919911'))
print(max([1, 2, 3, 4, 31]))
print(len([1, 2, 3, 4]))
print(lista3)

### funcion map()
lista = [1,2,3,4,5,6,7,8,9,0]
def es_par(x):
    if x %2 == 0:
        return x,'es par'
    else:
        return x, 'es impar'
    
lista_p = list(map(es_par,lista))
print(lista_p)

edades = [34, 13, 8, 42, 23, 17,18]

def es_menor(x):
    if x <=17:
        return x, 'es menor'
    else:
        return x ,'es mayor'
    
mayores = list(map(es_menor,edades))
print(mayores)

def solo_mayor(x):
    return x>=18
mayor = list(filter(solo_mayor,edades))
mayor = str(mayor)
print("".join(mayor))
print(mayor)

import datetime

x = datetime.datetime.now()
print(x)

def productos():
    libreria = list()
    producto = input('ingrese producto: ')
    libreria.append(producto)
    return print(libreria)

productos()