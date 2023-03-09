
print('1- menu')
print('2- texto')
print('3- calcular compras')
print('4- sumar digitos')
print('0- salir')

opcion = int(input('ingerse opcion: '))

while(opcion != 0):
    if opcion == 1:
        print('1- menu')
        print('2- texto')
        print('3- salir')
        opcion = int(input('ingerse opcion: '))

    elif opcion == 2:
        print('hola, este es el texto!!!')

        opcion = int(input('ingerse opcion: '))
    elif opcion == 3:
        compra = int(input('valor de compra: '))
        total = 0
        while compra != 0:
            if compra > 0:
                total = total + compra
                print('hasta aqui: $', total)
                compra = int(input('valor de compra: '))
            else:
                print('valor negativo')
                compra = int(input('valor de compra: '))

        if total >= 1000:
            print('descuento de: $', total * 0.1)
            total = total - (total*0.1)

        print('valor total: $', total)
        opcion = int(input('ingerse opcion: '))

    elif opcion == 4:
        suma = 0
        n = int(input('numero positivo'))

        while n != 0:
            digito = n % 10
            suma += digito
            n = n//10
        print('suma de los digitos:', suma)
        opcion = int(input('ingerse opcion: '))
    else:
        print('ingrese numero correcto')
        opcion = int(input('ingerse opcion: '))


print('chau saliste!')


frase = input('frase: ')
l = input('letra para buscar posicion: ')
i = 0
while i != len(frase):
    if l != frase[i]:
        print(' no se encontro', i)
        i += 1
        continue
    print('se encontro la posicion', i)
    break
