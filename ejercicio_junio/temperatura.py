nombre = input('su nombre porfa: ')

temperatura = float(input('su temperatura?! '))

if temperatura < 37.5 and temperatura > 20:
    print(nombre, 'No tiene fiebre')
elif temperatura > 40:
    print('ESTAS INSOLADO BYBY', nombre, 'anda a la heladera')
elif temperatura < 35:
    print(nombre, 'ESTAS CONGELADO!!!!! ANDA A LA ESTUFA URGENTE!!!!!')
else:
    print(nombre, 'Tienes fiebre')
    contacto = input('estubo en contacto estrecho? ')
    if contacto == 'si':
        print(nombre, 'AISLATE!!!')
    elif contacto == 'no':
        print(nombre, 'ES SOLO GRIPE!!!!!')
    else:
        print('no entiendo hu?')
